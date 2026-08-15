#!/usr/bin/env python3
"""Generate content/publications/ from data/publications.yaml.

The bibliography lives in one file so it can be read, sorted and diffed as a
whole; these page bundles are build output that happens to be committed. Same
arrangement AcademicPages uses with markdown_generator/.

    python3 tools/gen_publications.py            regenerate
    python3 tools/gen_publications.py --check    exit 1 if anything is stale
    python3 tools/gen_publications.py --from-doi 10.1007/s10546-023-00797-y
                                                 append a Crossref entry

`--check` is what makes the arrangement safe: without it, someone edits a
generated file, the change survives locally, and the next regeneration silently
reverts it. Running it in `make check` turns that into a build failure with an
instruction attached.
"""

import argparse
import datetime
import difflib
import json
import os
import re
import shutil
import sys
import urllib.parse
import urllib.request

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required:  pip3 install pyyaml")

SOURCE = "data/publications.yaml"
OUTDIR = "content/publications"
KNOWN_TYPES = ("article-journal", "paper-conference", "report")
TODAY = datetime.date.today().isoformat()

BANNER = (
    "# ⚠️ GENERATED FILE — DO NOT EDIT.\n"
    "# Source: data/publications.yaml   Regenerate: make publications\n"
    "# Edits here are silently reverted the next time the generator runs.\n"
)


def q(s):
    """Double-quoted YAML scalar."""
    return '"%s"' % str(s).replace("\\", "\\\\").replace('"', '\\"')


def render(pub):
    """One publication dict -> the full text of its index.md."""
    out = ["---", BANNER.rstrip("\n"), "title: %s" % q(pub["title"]), "", "authors:"]
    out += ["  - %s" % a for a in pub["authors"]]
    out += [
        "",
        "date: %s" % pub["date"],
        "publishDate: %s" % pub.get("publish_date", pub["date"]),
        "",
        "publication_types:",
        "  - %s" % pub["type"],
        "",
        "publication:",
    ]
    # `status` is appended to the venue because the citation view has no slot of
    # its own for it. It goes on BOTH name and short_name: the list on
    # /publications/ renders short_name when one is set, so appending only to
    # `name` leaves the status visible on the entry's own page but missing from
    # the list — which is the place that matters, since that is what a reader
    # sees without clicking.
    suffix = " (%s)" % pub["status"] if pub.get("status") else ""
    out.append("  name: %s" % q(pub["venue"] + suffix))
    if pub.get("venue_short"):
        out.append("  short_name: %s" % q(pub["venue_short"] + suffix))
    for key, field in (("volume", "volume"), ("pages", "pages"),
                       ("publisher", "publisher")):
        if pub.get(key):
            out.append("  %s: %s" % (field, q(pub[key])))

    if pub.get("doi"):
        # DOI goes in `links`, not `hugoblox.ids.doi`: the citation view gates
        # its link block on top-level `doi`/`links` only, so an id alone renders
        # no button, and setting both renders the button twice.
        out += ["", "links:", "  - type: doi",
                "    url: https://doi.org/%s" % pub["doi"]]

    if pub.get("abstract"):
        out += ["", "abstract: |"]
        out += ["  " + ln if ln.strip() else "" for ln in pub["abstract"].rstrip().split("\n")]

    out += ["", "summary: %s" % q(pub["summary"])]

    if pub.get("tags"):
        out += ["", "tags:"] + ["  - %s" % t for t in pub["tags"]]

    if pub.get("featured"):
        out += ["", "featured: true"]

    out += ["---"]
    if pub.get("body"):
        out += ["", pub["body"].rstrip()]
    return "\n".join(out) + "\n"


def validate(pubs):
    problems, seen = [], set()
    for i, p in enumerate(pubs):
        where = p.get("slug") or "entry #%d" % (i + 1)
        for field in ("slug", "title", "authors", "date", "type", "venue", "summary"):
            if not p.get(field):
                problems.append("%s: missing required field `%s`" % (where, field))
        if p.get("slug") in seen:
            problems.append("%s: duplicate slug" % where)
        seen.add(p.get("slug"))
        if p.get("type") and p["type"] not in KNOWN_TYPES:
            problems.append(
                "%s: type %r has no block on /publications/ and would render "
                "nowhere (expected one of %s)" % (where, p["type"], ", ".join(KNOWN_TYPES)))
        if p.get("date") and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(p["date"])):
            problems.append("%s: date %r is not YYYY-MM-DD" % (where, p["date"]))
        if p.get("doi", "").startswith("http"):
            problems.append("%s: doi should be bare, without the https://doi.org/ prefix" % where)
        # Anything dated in the future has not happened yet: the paper is not in
        # print, the conference has not been held. Without a `status` it renders
        # in the list as though it were done. Flagged rather than inferred, so
        # the generated output does not change meaning on its own the day the
        # date rolls past — it fails the build and asks for a decision instead.
        if (p.get("type") in ("article-journal", "paper-conference")
                and not p.get("doi") and not p.get("status")
                and str(p.get("date", "")) > TODAY):
            suggestion = ("in preparation" if p.get("type") == "article-journal"
                          else "abstract submitted")
            problems.append(
                "%s: dated in the future (%s) with no DOI and no `status` — it "
                "will read as already published/presented. Add e.g. "
                "`status: %s`." % (where, p.get("date"), suggestion))
    return problems


def load():
    with open(SOURCE, encoding="utf-8") as fh:
        pubs = yaml.safe_load(fh)
    problems = validate(pubs)
    if problems:
        print("%s has %d problem(s):" % (SOURCE, len(problems)))
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    return pubs


def sync(check_only):
    pubs = load()
    wanted = {p["slug"]: render(p) for p in pubs}
    stale = []

    for slug, text in sorted(wanted.items()):
        path = os.path.join(OUTDIR, slug, "index.md")
        current = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                current = fh.read()
        if current == text:
            continue
        stale.append(slug)
        if check_only:
            if current is None:
                print("  missing:  %s" % path)
            else:
                print("  stale:    %s" % path)
                diff = difflib.unified_diff(
                    current.splitlines(), text.splitlines(),
                    fromfile="on disk", tofile="generated", lineterm="", n=1)
                for line in list(diff)[2:10]:
                    print("            " + line)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print("  wrote %s" % path)

    # Orphans: a bundle whose slug is no longer in the source. Removing a
    # publication should mean deleting one entry, not remembering to delete a
    # directory too.
    if os.path.isdir(OUTDIR):
        for name in sorted(os.listdir(OUTDIR)):
            d = os.path.join(OUTDIR, name)
            if not os.path.isdir(d) or name in wanted:
                continue
            stale.append(name)
            if check_only:
                print("  orphan:   %s/ is not in %s" % (d, SOURCE))
            else:
                shutil.rmtree(d)
                print("  removed %s/ (no longer in %s)" % (d, SOURCE))

    if check_only:
        if stale:
            print("\n%d publication page(s) out of sync with %s." % (len(stale), SOURCE))
            print("Those pages are generated — edit %s, then run: make publications" % SOURCE)
            return 1
        print("  %d publication pages match %s" % (len(wanted), SOURCE))
        return 0

    if not stale:
        print("  %d publication pages already up to date" % len(wanted))
    return 0


def from_doi(doi):
    """Append a Crossref-derived entry to the source file."""
    doi = doi.strip().replace("https://doi.org/", "")
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={
        "User-Agent": "sotarolab.github.io publication importer (mailto:sfotarol@gmail.com)"})
    with urllib.request.urlopen(req, timeout=30) as fh:
        msg = json.load(fh)["message"]

    authors = [("%s %s" % (a.get("given", ""), a.get("family", ""))).strip()
               for a in msg.get("author", [])]
    parts = (msg.get("published") or msg.get("issued") or {}).get("date-parts", [[]])[0]
    date = "%04d-%02d-%02d" % (parts[0], parts[1] if len(parts) > 1 else 1,
                               parts[2] if len(parts) > 2 else 1)
    ctype = {"journal-article": "article-journal",
             "proceedings-article": "paper-conference",
             "report": "report"}.get(msg.get("type"), "article-journal")

    entry = {
        "slug": "%s-VENUE-TOPIC" % date[:4],
        "title": (msg.get("title") or [""])[0],
        "authors": authors,
        "date": date,
        "type": ctype,
        "venue": (msg.get("container-title") or [""])[0],
        "volume": msg.get("volume", ""),
        "pages": msg.get("page", ""),
        "doi": msg.get("DOI", doi),
        "summary": "TODO: one or two sentences, written as the finding.",
        "tags": ["TODO"],
    }
    entry = {k: v for k, v in entry.items() if v not in ("", [], None)}

    block = yaml.dump([entry], allow_unicode=True, sort_keys=False, width=80)
    with open(SOURCE, "a", encoding="utf-8") as fh:
        fh.write("\n" + block)
    print("Appended to %s:\n" % SOURCE)
    print(block)
    print("Now set `slug`, write `summary`, fix `tags`, then: make publications")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit 1; do not write")
    ap.add_argument("--from-doi", metavar="DOI",
                    help="append an entry fetched from Crossref")
    args = ap.parse_args()
    if args.from_doi:
        return from_doi(args.from_doi)
    return sync(args.check)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Generate content/research.md from data/research.yaml.

The page is prose plus media strips, and the strips are HTML with class names
that assets/js/research-strip.js and assets/css/custom/06-figures.css key off.
Keeping that markup in a generator means editing the page never involves
touching it: the YAML holds the words and the file paths, this script holds the
markup. Same arrangement as tools/gen_publications.py.

    python3 tools/gen_research.py            regenerate
    python3 tools/gen_research.py --check    exit 1 if the page is stale

`--check` runs in `make check`: a hand-edit to the generated page becomes a
build failure with an instruction attached, instead of surviving locally and
being silently reverted by the next regeneration.
"""

import argparse
import difflib
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required:  pip3 install pyyaml")

SOURCE = "data/research.yaml"
TARGET = "content/research.md"

BANNER = (
    "# ⚠️ GENERATED FILE — DO NOT EDIT.\n"
    "# Source: data/research.yaml   Regenerate: make research\n"
    "# Edits here are silently reverted the next time the generator runs.\n"
)


def q(s):
    """Double-quoted YAML scalar."""
    return '"%s"' % str(s).replace("\\", "\\\\").replace('"', '\\"')


def strip_figure(fig):
    """One video/image figure dict -> the <figure> markup inside the strip."""
    kind = "video" if "video" in fig else "image"
    src = fig[kind]
    # Sizing, from smallest footprint to largest:
    #   (default)       the strip's 560px card width
    #   width: 680px    any CSS length — sets --fig-w for this figure only
    #   wide: true      full rail (class styled in 06-figures.css) — for
    #                   panoramic multi-panel figures illegible at card size
    cls = "rstrip-item rstrip-item--wide" if fig.get("wide") else "rstrip-item"
    style = "--ar: %s" % fig["ratio"]
    if fig.get("width"):
        style += "; --fig-w: %s" % fig["width"]
    out = ['  <figure class="%s" style="%s">' % (cls, style),
           '    <div class="rstrip-frame">']
    if kind == "video":
        # data-src not src: research-strip.js swaps it in when the figure
        # scrolls into view, so an off-screen video costs nothing to load.
        out += ['      <video class="rstrip-media"',
                '        data-src="%s"' % src,
                '        poster="%s"' % fig["poster"],
                '        muted loop playsinline controls preload="none"',
                '        aria-label="%s"></video>' % fig["alt"]]
    else:
        out += ['      <img class="rstrip-media" src="%s"' % src,
                '        loading="lazy" alt="%s">' % fig["alt"]]
    out.append('    </div>')
    if fig.get("caption"):
        out.append('    <figcaption class="rstrip-cap">')
        out += ['      ' + ln if ln.strip() else ''
                for ln in fig["caption"].rstrip().split("\n")]
        out.append('    </figcaption>')
    out.append('  </figure>')
    return out


def section_text(sec):
    """Prose + rendered figures for one section, as unindented lines."""
    lines = sec["text"].rstrip().split("\n")
    figures = sec.get("figures") or []

    # Consecutive video/image figures share one strip; an `html` figure is
    # passed through untouched and breaks the run.
    i = 0
    while i < len(figures):
        fig = figures[i]
        if "html" in fig:
            lines += [""] + fig["html"].rstrip().split("\n")
            i += 1
            continue
        run = []
        while i < len(figures) and "html" not in figures[i]:
            run.append(figures[i])
            i += 1
        lines += ["", '<div class="rstrip-align not-prose">', '<div class="rstrip">']
        for f in run:
            lines += [""] + strip_figure(f)
        lines += ["", "</div>", "</div>"]
    return lines


def render(doc):
    page = doc["page"]
    out = ["---", BANNER.rstrip("\n"),
           "title: %s" % q(page["title"]),
           "summary: %s" % q(page["summary"]),
           "date: %s" % page["date"],
           "type: landing",
           "",
           "design:",
           "  spacing: %s" % q(page["spacing"]),
           "",
           "sections:"]
    for sec in doc["sections"]:
        out.append("  - block: markdown")
        if sec.get("id"):
            out.append("    id: %s" % sec["id"])
        out += ["    content:",
                "      title: %s" % q(sec["title"]),
                "      text: |-"]
        out += ["        " + ln if ln.strip() else ""
                for ln in section_text(sec)]
        out += ["    design:",
                "      columns: '1'"]
    out.append("---")
    return "\n".join(out) + "\n"


def validate(doc):
    problems = []
    if not isinstance(doc, dict) or "page" not in doc or "sections" not in doc:
        return ["%s must have top-level `page:` and `sections:`" % SOURCE]
    for field in ("title", "summary", "date", "spacing"):
        if not doc["page"].get(field):
            problems.append("page: missing `%s`" % field)
    for i, sec in enumerate(doc["sections"]):
        where = sec.get("title") or "section #%d" % (i + 1)
        if not sec.get("title"):
            problems.append("%s: missing `title`" % where)
        if not sec.get("text"):
            problems.append("%s: missing `text`" % where)
        for fig in sec.get("figures") or []:
            kinds = [k for k in ("video", "image", "html") if k in fig]
            if len(kinds) != 1:
                problems.append("%s: each figure needs exactly one of "
                                "`video`/`image`/`html`" % where)
                continue
            kind = kinds[0]
            if kind == "html":
                continue
            if not re.match(r"^\d+/\d+$", str(fig.get("ratio", ""))):
                problems.append("%s: %s figure needs `ratio: width/height` "
                                "(e.g. 1280/1100)" % (where, kind))
            if not fig.get("alt"):
                problems.append("%s: %s figure needs `alt` — it is the "
                                "screen-reader description" % (where, kind))
            if kind == "video" and not fig.get("poster"):
                problems.append("%s: video figure needs `poster` — without it "
                                "the lazy-loaded player is a blank box until "
                                "clicked" % where)
            # The path itself (does the file exist?) is qc.sh's job: it checks
            # the BUILT site, which also covers assets/ processed by Hugo.
            for key in (kind, "poster"):
                v = fig.get(key)
                if v and not str(v).startswith("/media/"):
                    problems.append("%s: `%s: %s` should start with /media/ "
                                    "(files live in static/media/ or "
                                    "assets/media/)" % (where, key, v))
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit 1; do not write")
    args = ap.parse_args()

    with open(SOURCE, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    problems = validate(doc)
    if problems:
        print("%s has %d problem(s):" % (SOURCE, len(problems)))
        for p in problems:
            print("  - " + p)
        return 1

    text = render(doc)
    current = None
    if os.path.exists(TARGET):
        with open(TARGET, encoding="utf-8") as fh:
            current = fh.read()

    if args.check:
        if current == text:
            print("  %s matches %s" % (TARGET, SOURCE))
            return 0
        print("  stale:    %s" % TARGET if current is not None
              else "  missing:  %s" % TARGET)
        if current is not None:
            diff = difflib.unified_diff(
                current.splitlines(), text.splitlines(),
                fromfile="on disk", tofile="generated", lineterm="", n=1)
            for line in list(diff)[2:10]:
                print("            " + line)
        print("\n%s is generated — edit %s, then run: make research"
              % (TARGET, SOURCE))
        return 1

    if current == text:
        print("  %s already up to date" % TARGET)
    else:
        with open(TARGET, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("  wrote %s" % TARGET)
    return 0


if __name__ == "__main__":
    sys.exit(main())

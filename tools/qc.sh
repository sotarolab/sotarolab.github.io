#!/usr/bin/env bash
#
# Pre-publish checks for sotarolab.github.io.
#
# Every assertion here corresponds to a bug that was actually live on this site
# at some point — placeholder profile URLs, figures pointing at files that were
# never added, links to deleted pages, stock template copy. They are cheap to
# check and expensive to notice by eye.
#
#   ./tools/qc.sh          build, then check
#   ./tools/qc.sh --fast   check the existing public/ without rebuilding
#
# Exit status is 1 if any check fails. Warnings do not fail the run.

set -uo pipefail
cd "$(dirname "$0")/.."

RED=$'\033[31m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; DIM=$'\033[2m'; OFF=$'\033[0m'
fails=0
warns=0

pass() { printf '  %sok%s   %s\n' "$GREEN" "$OFF" "$1"; }
fail() { printf '  %sFAIL%s %s\n' "$RED" "$OFF" "$1"; fails=$((fails + 1)); }
warn() { printf '  %swarn%s %s\n' "$YELLOW" "$OFF" "$1"; warns=$((warns + 1)); }
head_() { printf '\n%s\n' "$1"; }

# ── 1. Build ────────────────────────────────────────────────────────────────
if [ "${1:-}" = "--fast" ]; then
  head_ "1. Build (skipped — using existing public/)"
  [ -d public ] && pass "public/ exists" || { fail "public/ missing; run without --fast"; exit 1; }
else
  head_ "1. Build"
  build_log=$(hugo --gc --minify 2>&1)
  if [ $? -ne 0 ]; then
    fail "hugo build failed"
    printf '%s\n' "$build_log" | sed 's/^/       /'
    exit 1
  fi
  pass "hugo build clean"
  if printf '%s' "$build_log" | grep -qi 'WARN'; then
    warn "build emitted warnings:"
    printf '%s' "$build_log" | grep -i 'WARN' | sed 's/^/       /'
  fi
fi

# ── 1b. Generated content is in sync ────────────────────────────────────────
# content/publications/ is generated from data/publications.yaml. Without this
# check, a hand-edit to a generated page survives locally and is silently
# reverted by the next regeneration.
head_ "1b. Generated content"
if python3 tools/gen_publications.py --check; then
  pass "content/publications/ matches data/publications.yaml"
else
  fail "content/publications/ is out of sync — edit data/publications.yaml, then: make publications"
fi

# ── 1c. CV PDF and page agree ───────────────────────────────────────────────
# resume/ is upstream of the download: the resume is written
# in Word, exported with the phone number removed, and `make cv-pdf` copies it
# to static/uploads/cv.pdf. The /cv/ page is maintained BY HAND from the same
# resume, which is where drift can now enter — the download stays current while
# the page silently falls behind.
#
# So there are two things to check, in the new direction:
#   1. the published PDF matches the newest export in resume/
#   2. the page sources are not older than that export
# And one that has to hold whichever way the pipeline runs: no phone number in
# the published copy. That is the leak the whole arrangement exists to prevent,
# so it is verified here as well as at import — a file could be dropped into
# static/uploads/ without going through the Makefile.
head_ "1c. CV PDF"
cv_src=$(ls -t resume/*.pdf 2>/dev/null | head -1)
if [ ! -f static/uploads/cv.pdf ]; then
  warn "static/uploads/cv.pdf missing — run: make cv-pdf"
elif command -v pdftotext >/dev/null 2>&1 \
     && pdftotext static/uploads/cv.pdf - 2>/dev/null \
        | grep -qE '\(?[0-9]{3}\)?[ .-][0-9]{3}[ .-][0-9]{4}'; then
  fail "static/uploads/cv.pdf contains a phone-like number — the published CV is public"
elif [ -z "$cv_src" ]; then
  warn "no PDF in resume/ — cannot tell whether the published CV is current"
elif ! cmp -s "$cv_src" static/uploads/cv.pdf; then
  fail "static/uploads/cv.pdf differs from $cv_src — run: make cv-pdf"
else
  stale=""
  for src in data/authors/me.yaml content/cv.md; do
    [ "$cv_src" -nt "$src" ] && stale="$stale $src"
  done
  if [ -z "$stale" ]; then
    pass "published CV matches resume/ and the page is current"
  else
    warn "resume is newer than:$stale — the /cv/ page may have fallen behind the resume"
  fi
fi

# ── 2. No placeholders ship ─────────────────────────────────────────────────
# Checked against the BUILT SITE, not the sources: a placeholder inside a YAML
# or HTML comment is fine, one that reaches a reader is not.
head_ "2. Placeholders"
placeholders=(
  'REPLACE-ME'
  '0000-0000-0000-0000'
  'I enjoy making things'
  'Lorem ipsum'
  'YOUR-ORCID'
  'YOUR-ID'
)
for p in "${placeholders[@]}"; do
  hits=$(grep -rlF "$p" public/ 2>/dev/null | grep -v '/index.json$' | head -5)
  if [ -n "$hits" ]; then
    fail "placeholder \"$p\" is live on:"
    printf '%s\n' "$hits" | sed "s|^|       ${DIM}|;s|$|${OFF}|"
  fi
done
[ "$fails" -eq 0 ] && pass "no placeholder strings in published output"

# ── 3. Referenced media exists ──────────────────────────────────────────────
# A /media/... path that resolves to nothing renders as a broken image or a
# video frame that never loads — invisible in a build log.
#
# HTML comments are stripped first: several pages carry commented-out example
# paths as notes on where a future figure should go. Those are documentation,
# not references.
media_refs=$(python3 - <<'PY'
import re, pathlib
pat = re.compile(r'/media/[A-Za-z0-9._/-]+\.(?:png|jpg|jpeg|gif|webp|svg|mp4|webm)')
out = set()
for f in pathlib.Path('content').rglob('*.md'):
    text = re.sub(r'<!--.*?-->', '', f.read_text(encoding='utf-8', errors='replace'), flags=re.S)
    out.update(pat.findall(text))
print('\n'.join(sorted(out)))
PY
)
head_ "3. Media references"
missing_media=0
while IFS= read -r ref; do
  [ -z "$ref" ] && continue
  if [ ! -e "public${ref}" ]; then
    fail "missing media: $ref"
    missing_media=$((missing_media + 1))
  fi
done <<< "$media_refs"
[ "$missing_media" -eq 0 ] && pass "every /media/ path referenced in content/ exists"

# ── 4. Internal links resolve ───────────────────────────────────────────────
# Catches links left behind by a deleted or renamed page.
head_ "4. Internal links"
broken_links=0
while IFS= read -r link; do
  [ -z "$link" ] && continue
  case "$link" in
    /media/*|/uploads/*|/css/*|/js/*|*.xml|*.json) continue ;;
  esac
  path="public${link}"
  if [ ! -e "$path" ] && [ ! -e "${path%/}/index.html" ] && [ ! -e "${path%/}.html" ]; then
    fail "broken internal link: $link"
    broken_links=$((broken_links + 1))
  fi
done < <(grep -rhoE '\]\(/[A-Za-z0-9._/-]*\)' content/ | sed 's/^](//;s/)$//' | sort -u)
[ "$broken_links" -eq 0 ] && pass "every internal markdown link resolves to a built page"

# ── 4b. Declared aliases actually resolve ───────────────────────────────────
# `aliases:` in front matter is accepted silently even when the site config
# disables alias generation, so an old URL can 404 while the source looks
# correct. See the note on `disableAliases` in config/_default/hugo.yaml.
head_ "4b. Aliases"
alias_list=$(python3 - <<'PY'
import pathlib, re
out = []
for f in pathlib.Path('content').rglob('*.md'):
    text = f.read_text(encoding='utf-8', errors='replace')
    m = re.search(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        continue
    fm = m.group(1)
    am = re.search(r'^aliases:\s*\n((?:\s*-\s*\S+\n?)+)', fm, re.M)
    if am:
        out += re.findall(r'-\s*(\S+)', am.group(1))
print('\n'.join(sorted(set(out))))
PY
)
alias_missing=0
alias_count=0
while IFS= read -r al; do
  [ -z "$al" ] && continue
  al=${al//\'/}; al=${al//\"/}
  alias_count=$((alias_count + 1))
  if [ ! -e "public${al%/}/index.html" ]; then
    fail "declared alias 404s: $al — check \`disableAliases\` in config/_default/hugo.yaml"
    alias_missing=$((alias_missing + 1))
  fi
done <<< "$alias_list"
if [ "$alias_count" -eq 0 ]; then
  pass "no aliases declared"
elif [ "$alias_missing" -eq 0 ]; then
  pass "$alias_count declared alias(es) resolve"
fi

# ── 5. Publication completeness ─────────────────────────────────────────────
# /publications/ renders one block per publication_type. An entry with a type
# no block filters on is built, reachable by URL, and invisible in the list.
head_ "5. Publications"
known_types="article-journal paper-conference report"
pub_problems=0
for f in content/publications/*/index.md; do
  [ -e "$f" ] || continue
  slug=$(basename "$(dirname "$f")")
  type=$(awk '/^publication_types:/{getline; gsub(/^[ \t-]+|[ \t]+$/,""); print; exit}' "$f")
  if [ -z "$type" ]; then
    fail "$slug: no publication_types"
    pub_problems=$((pub_problems + 1))
  elif ! printf '%s' "$known_types" | grep -qw -- "$type"; then
    fail "$slug: publication_type \"$type\" has no block on /publications/ — it will render nowhere"
    pub_problems=$((pub_problems + 1))
  fi
  grep -q '^publication:' "$f" || { fail "$slug: no publication.name (venue)"; pub_problems=$((pub_problems + 1)); }
  # A journal article or report needs either a DOI or an explicit unpublished
  # status, or a reader cannot tell a published paper from a draft. Conference
  # abstracts are exempt: most are never assigned a DOI, and the venue line
  # already says what they are.
  if [ "$type" != "paper-conference" ]; then
    if ! grep -q 'type: doi' "$f" && ! grep -qi 'in preparation\|in review\|submitted\|preprint' "$f"; then
      warn "$slug: no DOI and no in-preparation/submitted status"
    fi
  fi
done
[ "$pub_problems" -eq 0 ] && pass "all publications have a venue and a renderable type"

# ── 6. Custom assets resolve ────────────────────────────────────────────────
# custom-assets.html emits the site's stylesheet and scripts under STABLE
# names, unfingerprinted and without SRI. That is deliberate: fingerprinted
# names plus GitHub Pages' ten-minute HTML cache meant every deploy left
# returning visitors asking for a stylesheet that had just been deleted, and
# the site rendered as the raw theme until their cache expired.
#
# The check that matters now is the plain one: every asset the built pages
# reference actually exists in public/. A renamed source file, or a bundle
# name changed in one place and not the other, would ship a broken link that
# builds cleanly.
head_ "6. Custom assets"
asset_bad=0
asset_checked=0
# `hugo --minify` drops the attribute quotes, so match both quoted and bare.
for url in $(grep -rhoE '(href|src)="?/(css/custom-bundle[^" >]*|js/[^" >]*)' public/index.html public/research/index.html 2>/dev/null \
             | sed -E 's/^(href|src)="?//' | sort -u); do
  asset_checked=$((asset_checked + 1))
  if [ ! -e "public${url}" ]; then
    fail "referenced asset missing from the build: $url"
    asset_bad=$((asset_bad + 1))
  fi
done
if [ "$asset_checked" -eq 0 ]; then
  fail "found no custom asset references on the built pages — the extractor has stopped matching"
elif [ "$asset_bad" -eq 0 ]; then
  pass "$asset_checked custom asset references all resolve"
fi

# ── 7. Custom CSS integrity ─────────────────────────────────────────────────
# A CSS comment that quotes a comment-closing delimiter ends early, and the
# parser then discards the following rule. Silent: clean build, rendered page,
# one colour missing in one theme. It has happened here twice.
head_ "7. Custom CSS"
css_bundle=$(ls -t public/css/custom-bundle*.css 2>/dev/null | head -1)
if [ -z "$css_bundle" ]; then
  fail "no custom-bundle CSS in public/css/ — the asset pipeline did not run"
elif python3 tools/check_css.py "$css_bundle"; then
  pass "comments well-formed and all design tokens defined for both themes"
else
  fail "custom CSS bundle has malformed comments or missing tokens"
fi

# ── 8. Contact rail ordering ────────────────────────────────────────────────
# assets/css/custom/03-biography.css labels link #1 "Contact" and injects a
# "Profiles" heading above link #2, because the block gives no grouping data to
# key off. So the first link must be the e-mail.
head_ "8. Author profile"
first_link=$(awk '/^links:/{f=1;next} f&&/^ *- icon:/{c++} f&&c==1&&/^ *url:/{print $2; exit}' data/authors/me.yaml)
case "$first_link" in
  mailto:*) pass "first profile link is the e-mail (required by the Contact/Profiles labelling)" ;;
  *) fail "first entry in me.yaml \`links\` is \"$first_link\", not a mailto: — it will be labelled Contact" ;;
esac

# ── 9. Stray TODOs (report only) ────────────────────────────────────────────
head_ "9. Outstanding TODOs"
todo_files=$(grep -rlE 'TODO' content/ data/ 2>/dev/null | sort)
if [ -n "$todo_files" ]; then
  printf '%s\n' "$todo_files" | sed "s|^|       ${DIM}|;s|$|${OFF}|"
  printf '  %sinfo%s %s file(s) carry a TODO (not a failure)\n' "$DIM" "$OFF" "$(printf '%s\n' "$todo_files" | wc -l | tr -d ' ')"
else
  pass "no TODOs outstanding"
fi

# ── Summary ─────────────────────────────────────────────────────────────────
printf '\n'
if [ "$fails" -gt 0 ]; then
  printf '%s%d check(s) failed%s, %d warning(s)\n' "$RED" "$fails" "$OFF" "$warns"
  exit 1
fi
printf '%sAll checks passed%s (%d warning(s))\n' "$GREEN" "$OFF" "$warns"

# sotarolab.github.io
#
#   make serve   local preview with drafts, at http://localhost:1313
#                (served from memory; it does not touch public/, so it can run
#                alongside make check without the two overwriting each other)
#   make build   production build into public/
#   make check   build + pre-publish checks (see tools/qc.sh)
#   make clean   remove build output and caches
#
# `make check` is the one to run before pushing. CI runs the same script.

.DEFAULT_GOAL := help
.PHONY: help serve build check check-fast clean publications pub-from-doi project cv-pdf

help:
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

serve: ## Local preview with drafts and future-dated content
	hugo server -D -F --disableFastRender --renderToMemory

build: publications ## Production build into public/
	hugo --gc --minify

check: ## Build, then run all pre-publish checks
	@./tools/qc.sh

check-fast: ## Run checks against the existing public/ without rebuilding
	@./tools/qc.sh --fast

clean: ## Remove build output and caches
	rm -rf public resources .hugo_build.lock hugo_stats.json

# ── Publications ────────────────────────────────────────────────────────────
# content/publications/ is GENERATED from data/publications.yaml. Edit the YAML,
# never the page bundles. `make check` fails if the two have drifted.
publications: ## Regenerate content/publications/ from data/publications.yaml
	@python3 tools/gen_publications.py

# content/research.md is hand-written markdown — no generator. Figures go in
# via the rfig/rstrip shortcodes (layouts/_shortcodes/), which fail the build
# if a figure is missing its ratio, alt text, or video poster.

pub-from-doi: ## Append a publication from Crossref (DOI=10.xxxx/yyyy)
	@test -n "$(DOI)" || { echo "usage: make pub-from-doi DOI=10.1007/s10546-023-00797-y"; exit 1; }
	@python3 tools/gen_publications.py --from-doi "$(DOI)"

project: ## Scaffold a project (SLUG=name)
	@test -n "$(SLUG)" || { echo "usage: make project SLUG=my-tool"; exit 1; }
	hugo new content/projects/$(SLUG)/index.md --kind project

# ── CV PDF ──────────────────────────────────────────────────────────────────
# static/uploads/cv.pdf is the resume exported from Word, copied out of resume/.
# It is NOT generated from the site: the Word layout is the one people download.
#
# Direction reversed 2026-08-17. This target used to PRINT the built /cv/ page
# to PDF, which guaranteed the two could not drift but produced a printed web
# page rather than a designed resume. Now resume/ is upstream of the download,
# and /cv/ is maintained alongside it by hand — `make check` compares their
# timestamps and complains when the page falls behind.
#
# The phone-number guard survives the reversal, because the risk did: the
# source resume carries a personal number, this repo and the site are public,
# and the whole point of the redacted export is that the published copy has it
# removed. The guard now checks what is being IMPORTED rather than exported,
# and refuses rather than publishing a leak.
CV_SRC = $(shell ls -t resume/*.pdf 2>/dev/null | head -1)
cv-pdf: ## Publish static/uploads/cv.pdf from the newest PDF in resume/
	@test -n "$(CV_SRC)" || { echo "no PDF in resume/ — export one from Word first"; exit 1; }
	@pdftotext "$(CV_SRC)" - 2>/dev/null | grep -qE '\(?[0-9]{3}\)?[ .-][0-9]{3}[ .-][0-9]{4}' \
	  && { echo "$(CV_SRC) contains a phone-like number; refusing to publish it"; exit 1; } || true
	@mkdir -p static/uploads
	@cp "$(CV_SRC)" static/uploads/cv.pdf
	@echo "published static/uploads/cv.pdf from $(CV_SRC)"

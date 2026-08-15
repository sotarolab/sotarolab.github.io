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
# static/uploads/cv.pdf is printed from the built /cv/ page, so it carries the
# same redactions as the site (no phone number, no client names). Re-run this
# after any change to data/authors/me.yaml or content/cv.md. Requires Chrome.
CHROME ?= /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
cv-pdf: build ## Regenerate static/uploads/cv.pdf from the built /cv/ page
	@test -x "$(CHROME)" || { echo "Chrome not found at $(CHROME); set CHROME=..."; exit 1; }
	@mkdir -p static/uploads
	@( cd public && python3 -m http.server 18313 >/dev/null 2>&1 & echo $$! > /tmp/cvpdf.pid ); sleep 1; \
	"$(CHROME)" --headless=new --disable-gpu --no-pdf-header-footer \
	  --print-to-pdf=static/uploads/cv.pdf http://localhost:18313/cv/ 2>/dev/null; \
	kill $$(cat /tmp/cvpdf.pid) 2>/dev/null; rm -f /tmp/cvpdf.pid
	@pdftotext static/uploads/cv.pdf - 2>/dev/null | grep -qE '\(?[0-9]{3}\)?[ .-][0-9]{3}[ .-][0-9]{4}' \
	  && { echo "cv.pdf contains a phone-like number; refusing"; rm -f static/uploads/cv.pdf; exit 1; } \
	  || echo "wrote static/uploads/cv.pdf"

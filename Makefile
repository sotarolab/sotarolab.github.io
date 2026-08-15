# sotarolab.github.io
#
#   make serve   local preview with drafts, at http://localhost:1313
#   make build   production build into public/
#   make check   build + pre-publish checks (see tools/qc.sh)
#   make clean   remove build output and caches
#
# `make check` is the one to run before pushing. CI runs the same script.

.DEFAULT_GOAL := help
.PHONY: help serve build check check-fast clean publications pub-from-doi project research

help:
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

serve: ## Local preview with drafts and future-dated content
	hugo server -D -F --disableFastRender

build: publications research ## Production build into public/
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

# content/research.md is GENERATED from data/research.yaml — same arrangement.
research: ## Regenerate content/research.md from data/research.yaml
	@python3 tools/gen_research.py

pub-from-doi: ## Append a publication from Crossref (DOI=10.xxxx/yyyy)
	@test -n "$(DOI)" || { echo "usage: make pub-from-doi DOI=10.1007/s10546-023-00797-y"; exit 1; }
	@python3 tools/gen_publications.py --from-doi "$(DOI)"

project: ## Scaffold a project (SLUG=name)
	@test -n "$(SLUG)" || { echo "usage: make project SLUG=my-tool"; exit 1; }
	hugo new content/projects/$(SLUG)/index.md --kind project

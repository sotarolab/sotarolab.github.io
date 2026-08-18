# sotarolab.github.io

Personal academic website for Sebastian Otarola-Bustos — atmospheric and
hydrologic scientist.

Built with [Hugo](https://gohugo.io/) and the
[Hugo Blox academic-cv](https://github.com/HugoBlox/hugo-theme-academic-cv)
theme (MIT), deployed to GitHub Pages by GitHub Actions on every push to `main`.

## Local development

```bash
make serve     # preview at localhost:1313, with drafts and future-dated content
make check     # production build + all pre-publish checks
```

`make help` lists every target.

## How content is organised

| What | Where |
| --- | --- |
| About page (bio, animation strip, news) | `content/_index.md` |
| Research, Projects, Teaching, CV pages | `content/research.md`, `content/projects/`, `content/teaching/`, `content/cv.md` |
| Experience and education | `data/authors/me.yaml` |
| Publications | `data/publications.yaml` → `make publications` |
| Site styling | `assets/css/custom/*.css`, concatenated in load order |

`content/publications/` is **generated** — edit `data/publications.yaml` and run
`make publications`, or `make pub-from-doi DOI=10.xxxx/yyyy` to append an entry
from Crossref. Editing the generated pages directly gets overwritten.

See [docs/CONTENT.md](docs/CONTENT.md) for the full editing guide.

## Downloadable CV

`static/uploads/cv.pdf` is published from the resume in `resume/`, which is
gitignored — see [resume/README.md](resume/README.md). `make cv-pdf` copies it
into place and refuses any file containing a phone number, since this repo and
the site are public.

## Checks

`make check` builds the site and then verifies it: no placeholder strings, no
broken internal links, every figure has alt text, every referenced asset exists,
design tokens are defined for both themes, and the published CV is current and
carries no phone number. `tools/qc.sh` is the script; it exits non-zero on
failure.

# sotarolab.github.io

Personal site for Sebastian Otarola-Bustos — machine learning and atmospheric science, weather extremes.

Built with [Hugo](https://gohugo.io/) + the [HugoBlox academic-cv](https://github.com/HugoBlox/hugo-theme-academic-cv) theme (MIT licensed), deployed to GitHub Pages via GitHub Actions on every push to `main`.

## Local development

```bash
pnpm install
hugo server
```

## Adding publications

Drop a `publications.bib` file at the repo root and push to `main` — the `Import Publications From Bibtex` workflow opens a PR converting it into pages under `content/publications/`.

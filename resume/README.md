# resume/

The source CV lives here — the Word document and whatever PDF was last exported
from it. This is the upstream copy: `/cv/` on the site is written *from* it, so
when the resume changes, the text here is what gets copied across into
`data/authors/me.yaml` (experience, education) and `content/cv.md` (summary,
skills).

## Nothing in here is committed

`.gitignore` ignores `resume/*` wholesale and allowlists only this README. That
is deliberate and worth not undoing:

- This repo is **public**.
- The resume carries a **personal phone number**, which the published site
  does not (see the note in `content/cv.md`).
- **Git history is permanent.** A file committed once and deleted in the next
  commit is still retrievable by anyone who clones the repo. There is no
  "delete it later" — the only safe move is never committing it.

Because it is an allowlist, a new file dropped in here — `.docx`, `.tex`, a
fresh export — is ignored automatically. Nothing to remember.

## The trade-off

Ignored means not backed up and not synced between machines. Keep the real
copy wherever you already keep documents. If you want the resume genuinely
version-controlled, that belongs in a **separate private repo** — which is
also where the Overleaf-synced LaTeX project would live if that pipeline gets
built.

## Updating the site from a new version

1. Drop the new export in here.
2. `pdftotext -layout resume/<file>.pdf -` to read it out.
3. Copy changed bullets into `data/authors/me.yaml` and `content/cv.md`.
4. `make cv-pdf` to regenerate `static/uploads/cv.pdf` — the published PDF is
   printed from the rendered `/cv/` page, so it inherits the site's redactions
   and cannot drift from what the page shows.
5. `make check`.

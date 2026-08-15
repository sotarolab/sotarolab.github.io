# sotarolab.github.io

Personal academic site for Sebastian Otarola-Bustos. Hugo Blox (Wowchemy) v2,
schema 2.0, deployed to GitHub Pages.

**Read [docs/CONTENT.md](docs/CONTENT.md) before editing.** It covers where each
kind of content lives, how to add a publication or project, and which CSS rules
are keyed to upstream template internals.

## Commands

```bash
make serve    # preview at localhost:1313
make check    # build + pre-publish checks — run before pushing
```

## The short version

- `data/authors/me.yaml` is the spine: role, affiliations, links, education,
  experience. Both the About page and `/cv/` render from it. Exception: the
  bio prose lives in `content/_index.md` (the biography block's `text`
  field, above the animation strip) — the block renders `text` INSTEAD of
  the yaml bio, so the strip could only join the bio by bringing the prose
  with it.
- `data/publications.yaml` is the whole bibliography. Everything under
  `content/publications/` is GENERATED from it by `tools/gen_publications.py`
  — never edit those pages; `make check` fails if they drift.
- `data/research.yaml` is the whole Research page — prose and figures per
  section. `content/research.md` is GENERATED from it by `tools/gen_research.py`
  (`make research`); never edit it directly, `make check` fails if it drifts.
- Factual source of truth is `Sebastian_Otarola-Bustos_CV_human.pdf` (repo
  root, gitignored — it carries a personal phone number). Facts on the site
  come from that document; never invent credentials, dates, or claims. The
  bio's register was redrafted 2026-08-14 at Sebastian's request (modelled on
  jcsandov.github.io: standing → methods → "My work spans" bullets) and he
  approved the wording — its closing interest sentence is still his CV
  wording verbatim. Elsewhere, prefer his wording; substantive rewrites need
  his sign-off.
- Nav: About / Research / Projects / Publications / Teaching / CV. Research is
  what the work studies; Projects is what is built and running. `/blog/` exists
  but is unlinked while it has one post.
- Custom CSS lives in `assets/css/custom/*.css`, concatenated in filename order.
  Never put CSS back into a head-hook `<style>` tag — two rules were silently
  dead behind unbalanced comment delimiters in the old inline file. Never quote
  a comment-closing delimiter inside a CSS comment either: CSS comments do not
  nest, and doing so recreates exactly that bug. `make check` catches both.

## Positioning constraint

Sebastian is employed and the site is public. It must **not** read as a job
search: no "seeking a postdoctoral position", no "looking to move into". The bio
closes on interest — "I am interested in applied research at the intersection
of…" — which is his own wording. That framing belongs in application materials,
not here.

## Outstanding

- Google Scholar is live in `me.yaml` (verified profile, placed before
  GitHub). ORCID remains commented out: Sebastian has an existing iD but
  lost access to its email (Aug 2026) — he'll recover it via ORCID support;
  never create a new iD for him. `make check` fails the build if a
  placeholder URL ever goes live.
- The CV's Papers and Conferences sections assign co-authors to the two
  2026/2027 works in opposite order. The site follows the Conferences
  assignment (Giani & Valenzuela → CMIP6 Chile; Buahin → LSTM/hydrology);
  flagged with `TODO` in all four affected files pending confirmation.

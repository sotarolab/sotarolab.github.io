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
- Figures rendered from code ship a light AND a dark canvas
  (`rfig`'s `image_dark=`), because a white plot glares on the dark theme.
  `~/dev/caudal` and `~/dev/chile-super-extremes` each grew a
  `viz.style.dark()` context and a `--dark` flag that re-run the SAME builders
  and write `*_dark.png`; never hand-edit or recolour a rendered figure, and
  never let a dark render overwrite the file the paper builds from.
- `content/research.md` is the whole Research page, hand-written markdown —
  edit it directly, no generator. Figures go in via the `rfig`/`rstrip`
  shortcodes in `layouts/_shortcodes/`, which own the `.rstrip` markup that
  `research-strip.js` and `06-figures.css` are keyed to, and which fail the
  BUILD if a figure lacks `ratio`, `alt`, or (for video) `poster`. It was
  generated from `data/research.yaml` until 2026-08-15 — dropped because the
  prose is edited far more often than the figures.
- Factual source of truth is `Sebastian_Otarola-Bustos_CV_human.pdf` (repo
  root, gitignored — it carries a personal phone number). Facts on the site
  come from that document; never invent credentials, dates, or claims. The
  bio's register was redrafted 2026-08-14 at Sebastian's request (modelled on
  jcsandov.github.io: standing → methods → "My work spans" bullets) and he
  approved the wording — its closing interest sentence is still his CV
  wording verbatim. Elsewhere, prefer his wording; substantive rewrites need
  his sign-off.
- Nav: About / Research / Projects / Publications / Teaching / CV. Research is
  what the work studies; Projects is what is built and running. Project pages
  open with the `applinks` shortcode (the live app as a primary button — the
  theme's own `links:` render is a small text link and was missed), carry a
  `featured.jpg` card cover marked `preview_only`, and document the app with
  real captures under `static/media/projects/`. Interactive teaching tools are
  self-contained HTML in `static/apps/<slug>/`, framed by a page under
  `content/teaching/<slug>/` tagged `Interactive`. `/blog/` exists
  but is unlinked while it has one post.
- Figure images open full-size on click (`assets/js/figure-lightbox.js` +
  `10-lightbox.css`), site-wide and JS-optional. It binds BOTH theme variants
  of a paired figure — binding only the visible one breaks as soon as a reader
  uses the theme toggle.
- No social share row anywhere: the theme's sharer is opt-OUT, so
  `config/_default/hugo.yaml` cascades `share: false` over `/**`. A new
  content file would otherwise bring X/Facebook/WhatsApp buttons back.
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

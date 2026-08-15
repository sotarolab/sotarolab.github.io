# Editing this site

A Hugo Blox (Wowchemy) site. `docs/` is outside `content/`, so nothing here is
published.

```
make serve    # preview at localhost:1313, with drafts
make check    # build + pre-publish checks — run this before pushing
make clean
```

---

## Where everything lives

Every piece of text and media on the site is edited in exactly one file, then
`make serve` (already running? it live-reloads) or `make check` before pushing.
The two GENERATED pages regenerate with one command each.

| What | Where |
|---|---|
| Your name, role, affiliations, links, education, experience | `data/authors/me.yaml` |
| Bio prose + homepage animation strip | `content/_index.md` (biography block's `text`) |
| Research page — every section's prose and figures | **`data/research.yaml`** (page is generated: `make research`) |
| Page structure (which blocks, in what order) | `content/*.md` front matter |
| Publications | **`data/publications.yaml`** (pages are generated: `make publications`) |
| Projects | `content/projects/<slug>/index.md` |
| Teaching (mentoring, TA record, course) | `content/teaching/` |
| Navigation | `config/_default/menus.yaml` |
| Site title, tagline, theme, features | `config/_default/params.yaml` |
| Colours | `data/themes/primer.yaml` |
| Custom CSS | `assets/css/custom/*.css` |
| Custom JS | `assets/js/*.js` |
| Videos, posters, PDFs | `static/media/…` |
| Images Hugo should process (avatar, figures) | `assets/media/…` |

**`me.yaml` is the spine.** The About page and `/cv/` both render from it —
editing it changes both. Nothing about your experience or education is written
in a content file.

### `assets/media/` vs `static/media/`

- `assets/` — Hugo processes it: resizing, format conversion, fingerprinting.
  Use for images. Referenced by the pipeline (the avatar resolves by author
  slug).
- `static/` — copied verbatim to the site root. Use for video, posters, PDFs,
  anything large or already optimised. Referenced by literal path:
  `/media/research/clip.mp4`.

---

## Editing the Research page

> **`content/research.md` is generated output. Never edit it.**
> The page lives in **`data/research.yaml`** — one entry per section.

```bash
# edit data/research.yaml, then:
make research     # regenerate the page (live preview picks it up)
```

Each section is `title` + `text` (markdown), plus an optional `figures` list.
The schema, with a copy-paste example of every figure kind, is documented in
the header of `data/research.yaml`.

**To replace a video or image:** drop the new file in `static/media/research/`,
update the `video:`/`image:` (and `poster:`) path in `data/research.yaml`, run
`make research`. `make check` fails if a referenced path does not exist in the
built site, and the drift check fails if the page was hand-edited instead.

The point of generating this page: the media strips are HTML whose class names
(`.rstrip`, `--ar`, `data-src`) are keyed to `assets/js/research-strip.js` and
`assets/css/custom/06-figures.css`. The generator owns that markup, so editing
a caption or swapping a file can never break the lazy-loading or the layout.

## Adding a publication

> **`content/publications/*/index.md` is generated output. Never edit it.**
> The whole bibliography lives in **`data/publications.yaml`**.

This is the one convention borrowed wholesale from AcademicPages, which keeps
its bibliography in a single tabular file and generates the per-paper pages from
it. The point is that the entire publication record is visible, sortable and
diffable in one place, instead of spread across a dozen near-identical page
bundles where a missing field is invisible until someone notices the page looks
wrong.

**For a published paper** — let Crossref fill in the metadata rather than
transcribing it:

```bash
make pub-from-doi DOI=10.1007/s10546-023-00797-y   # appends to data/publications.yaml
# then edit that entry: set `slug`, write `summary`, fix `tags`
make publications                                  # regenerate the pages
```

**For unpublished work** — add an entry to `data/publications.yaml` by hand and
run `make publications`. Every field is documented in the header of that file.

Three things that will bite you:

1. **`type` decides which section it lands in.** `/publications/` renders one
   block per type — `article-journal`, `paper-conference`, `report`. Any other
   value builds fine, gets a URL, and appears in **no** list. Both the generator
   and `make check` reject it.

2. **`make check` fails if a generated page has been hand-edited.** That is the
   point: without it, the edit survives locally and is silently reverted by the
   next regeneration. The fix is always the same — move the change into
   `data/publications.yaml` and regenerate.

3. **`doi` is bare** — `10.1007/s10546-023-00797-y`, not the full URL. The
   generator emits it as a `links:` entry rather than `hugoblox.ids.doi`,
   because the citation view gates its link block on top-level `doi`/`links`
   only: an id alone renders no button, and setting both renders it twice.

`featured: true` surfaces an entry in **Selected Publications** on the homepage.
Keep that to about three.

### The name-variant problem

You are indexed under at least five forms across these papers (`Otarola Bustos,
Sebastian F.`, `Otárola-Bustos, Sebastián F.`, `Otárola, Sebastián`, …). Each
entry here matches its own paper of record, which is correct. The consequence is
off this site: Google Scholar and ORCID will not merge them automatically. They
need claiming by hand on both profiles.

## Adding a project

```bash
make project SLUG=my-tool
```

Projects appear on `/projects/`, which has its own nav item. The split is
deliberate: **Research** is what the work studies (threads, with figures),
**Projects** is what is built and running. The `Live Forecast Platforms` thread
on `/research/` links across.

## Adding a news post

`content/blog/<slug>/index.md`. Note `/blog/` is currently **not linked from the
nav** and not shown on the homepage. To surface news again, add a `collection`
block with `page_type: blog` to `content/_index.md` and a nav entry.

---

## Styling

All custom CSS is in `assets/css/custom/`, concatenated **in filename order** —
hence the numeric prefixes, because the cascade depends on it.

| File | Scope |
|---|---|
| `01-tokens.css` | Colour and measure tokens. Start here. |
| `02-header-nav.css` | Header bar, active-nav underline |
| `03-biography.css` | About sidebar, contact rail, affiliations |
| `04-sections.css` | Section rails, headings, experience cards, citations |
| `05-typography.css` | Prose colours, links, focus, selection |
| `06-figures.css` | `.rstrip` videos and the `.mtw` mountain-wave canvas |

Add a file and it is picked up automatically. `layouts/_partials/hooks/head-end/custom-assets.html`
is the only hook; it concatenates, minifies, fingerprints, and emits Subresource
Integrity hashes.

> **Do not reorder `minify` and `fingerprint`** in that hook. The hash must
> describe the bytes that actually ship, or the browser silently refuses to
> apply the stylesheet and the page renders unstyled. `make check` re-derives
> both hashes from the published files.

Most rules in `03-` and `04-` are workarounds keyed to the utility classes the
upstream blox templates emit. They are stable for a given module version but
**will** need revisiting after `make upgrade`-style module bumps. Each carries a
comment saying what breakage to expect. The tell that one has broken: the
sidebar reverts to centred icon circles, or section headings stop sharing a left
edge.

### Two things that used to be positional and no longer are

- **Affiliation icons** are chosen by whether the entry has a `url:` (→ building
  glyph) or not (→ map pin), via `:has(a)`. Reorder `affiliations` freely.
- **Figure aspect ratios** are declared inline on each `<figure>` in
  `content/research.md` as `style="--ar: 1280/1100"`. Add or reorder panels
  without touching CSS.

One coupling remains and cannot be removed from CSS alone: the sidebar link list
is labelled **Contact** (link 1) / **Profiles** (links 2+) purely by position,
because the block exposes no grouping data. **E-mail must stay first** in
`me.yaml` → `links`. `make check` asserts it.

---

## What `make check` verifies

1. The site builds.
2. No placeholder strings (`REPLACE-ME`, a zeroed ORCID, stock template copy)
   reach the published output.
3. Every `/media/...` path referenced in `content/` exists.
4. Every internal markdown link resolves to a page that was actually built.
5. Every publication has a venue and a type that some block will render.
6. Fingerprinted assets match their SRI hashes.
7. The first author link is the e-mail.
8. Outstanding `TODO`s are listed (informational).

Every one of these corresponds to a bug that was live on this site at some
point. CI runs the same script.

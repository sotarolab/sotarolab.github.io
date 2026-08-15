---
title: Publications
summary: Peer-reviewed articles, conference contributions, and technical reports.
cms_exclude: true
type: landing

design:
  spacing: '3rem'

# Grouped by type rather than shown as one date-ordered list, mirroring the
# CV's own Papers / Conferences split. Each block filters the same
# `content/publications/` folder on `publication_type`, so a new entry lands in
# the right group automatically from its `publication_types` front matter — no
# edit here is needed when adding a paper.
#
# ⚠️ If you add a `publication_types` value not covered below, its entries will
# silently render nowhere. The values in use are article-journal,
# paper-conference and report; add a block if you introduce another.
#
# `view: citation` renders each entry as a formatted reference rather than a
# card — style is set by `content.citations.style` in params.yaml (APA). This is
# the AcademicPages convention: a publication list should look like a reference
# list, because that is how it gets read.
sections:
  # Page title. A landing page does not render its own `title`, and without
  # this the page opened straight into "Journal Articles" while /research/ and
  # /cv/ both lead with their name. The first-section rule in
  # assets/css/custom/04-sections.css sets this one at page-title scale.
  - block: markdown
    content:
      title: 'Publications'
      text: |-
        Peer-reviewed articles, conference contributions, and technical reports.
        Work in preparation is marked as such.
    design:
      columns: '1'

  - block: collection
    id: journal-articles
    content:
      title: Journal Articles
      text: ''
      count: 0
      filters:
        folders:
          - publications
        publication_type: 'article-journal'
      order: desc
    design:
      view: citation

  - block: collection
    id: conference-presentations
    content:
      title: Conference Presentations
      text: ''
      count: 0
      filters:
        folders:
          - publications
        publication_type: 'paper-conference'
      order: desc
    design:
      view: citation

  - block: collection
    id: reports
    content:
      title: Reports
      text: ''
      count: 0
      filters:
        folders:
          - publications
        publication_type: 'report'
      order: desc
    design:
      view: citation
---

<!--
  ⚠️ NAME VARIANTS. Sebastian is indexed under at least five forms across these
  papers:

    Otarola Bustos, Sebastian F.   (BLM 2023)
    Otárola-Bustos, Sebastián F.   (JAMC 2022)
    Otárola, Sebastián             (GRL 2016)
    Otarola-Bustos, Sebastian      (BAMS 2019, WFIP2)
    Otarola-Bustos, S.             (BAMS 2019, Perdigão)

  Each byline here matches its own paper of record. The practical consequence is
  off this site: Google Scholar and ORCID will not merge these automatically, so
  all five need claiming by hand on both profiles or the citation record stays
  fragmented.

  Once a Google Scholar ID exists, add a line above pointing at the full list;
  reviewers routinely go looking for it.

  To add a publication, see docs/CONTENT.md — or run:
      hugo new content/publications/<year-venue-slug>/index.md -k publication
-->

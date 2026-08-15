---
title: Publications
summary: Peer-reviewed articles and conference contributions.
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
# silently render nowhere. The values rendered here are article-journal and
# paper-conference. The Reports block was removed 2026-08-15, so a `report`
# entry would build a page that nothing links to — add a block back if reports
# ever return.
#
# `view: citation` renders each entry as a formatted reference rather than a
# card — style is set by `content.citations.style` in params.yaml (APA). This is
# the AcademicPages convention: a publication list should look like a reference
# list, because that is how it gets read.
sections:
  # NB the page opens straight into "Journal Articles": the title block that
  # used to sit here (an H1 "Publications" plus a line of blurb) was removed
  # 2026-08-15 at Sebastian's request. A landing page does not render its own
  # `title`, so /publications/ now has no page-level heading, unlike /research/
  # and /cv/. That is deliberate — the section headings are self-explanatory
  # and the nav already says where you are. The first-section rule in
  # assets/css/custom/04-sections.css now scales "Journal Articles" as the
  # page title, which is why it reads larger than "Conference Presentations".

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

---

---
title: Publications
summary: Peer-reviewed articles and conference contributions.
cms_exclude: true
type: landing

design:
  spacing: '3rem'

# Grouped by type rather than shown as one date-ordered list, mirroring the.
sections:
  # NB the page opens straight into "Journal Articles": the title block that.

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

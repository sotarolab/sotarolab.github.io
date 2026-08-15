---
title: 'Projects'
summary: Live forecast platforms with continuous data ingestion from operational weather models and observation networks.
date: 2026-08-11
type: landing

design:
  spacing: '3rem'

sections:
  - block: markdown
    content:
      title: 'Projects'
      # The opening line used to read "Running applications rather than figures
      # in a paper". Cut 2026-08-15 (Sebastian): it set the work against
      # academic publishing, which is dismissive and is not the point — the
      # point is the operational property, that these ingest live data on a
      # schedule and keep running unattended.
      #
      # The closing line pointed at /research/ as "the forecasting research
      # behind them" until 2026-08-15. Removed as untrue at Sebastian's
      # request: /research/ documents downscaling, AR-flood streamflow and
      # boundary-layer meteorology — not these platforms, and the section that
      # did cover them was moved out. The replacement is his framing of why he
      # builds them, and claims nothing about what another page contains.
      text: |-
        Operational applications: each ingests live data from weather
        forecasting models and observation networks on a fixed cycle, and keeps
        running unattended. Both are public and deployed.

        Coming from weather forecasting, I like building applications for
        high-impact weather events, using the data science and development side
        of my work to put forecasts somewhere they can actually be used.
    design:
      columns: '1'

  # `folders: [projects]` picks up every page bundle in this section. The
  # section's own _index.md is not a bundle, so it does not list itself.
  #
  # article-grid, not the flat date-title-summary list it was until 2026-08-15:
  # each bundle now ships a featured.jpg of the application itself, so the card
  # view has a real screenshot to show instead of the empty image placeholder
  # that made the flat list the better choice before. Card image handling is in
  # assets/css/custom/08-project-links.css (`.projects-grid`).
  - block: collection
    id: live-tools
    content:
      title: ''
      text: ''
      filters:
        folders:
          - projects
    design:
      view: article-grid
      columns: 2
      show_date: false
      show_read_time: false
      css_class: 'projects-grid'
      # The page's `spacing: '3rem'` applies to every block, and stacking the
      # intro's bottom padding on the grid's top padding left the cards
      # floating well clear of the paragraph that introduces them. The grid
      # belongs to that paragraph, so it gets no top padding of its own.
      spacing:
        padding: [0, 0, '3rem', 0]
---

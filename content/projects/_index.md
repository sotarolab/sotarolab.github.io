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
      # The opening line used to read "Running applications rather than figures.
      text: |-
        Operational applications: each ingests live data from weather
        forecasting models and observation networks on a fixed cycle, and keeps
        running unattended. Both are public and deployed.

        Coming from weather forecasting, I like building applications for
        high-impact weather events, using the data science and development side
        of my work to put forecasts somewhere they can actually be used.
    design:
      columns: '1'

  # `folders: [projects]` picks up every page bundle in this section. The.
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
      # The page's `spacing: '3rem'` applies to every block, and stacking the.
      spacing:
        padding: [0, 0, '3rem', 0]
---

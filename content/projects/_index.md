---
title: 'Projects'
summary: Live forecast platforms — running applications with continuous data ingestion from operational weather models and observations.
date: 2026-08-11
type: landing

design:
  spacing: '3rem'

sections:
  - block: markdown
    content:
      title: 'Projects'
      text: |-
        Running applications rather than figures in a paper: each ingests live
        data from operational weather forecasting models and observational
        networks, and keeps doing so without me. The forecasting research behind
        the calibration is on the
        [research page](/research/#live-forecast-platforms).
    design:
      columns: '1'

  # `folders: [projects]` picks up every page bundle in this section. The
  # section's own _index.md is not a bundle, so it does not list itself.
  - block: collection
    id: live-tools
    content:
      title: ''
      text: ''
      filters:
        folders:
          - projects
    design:
      # Flat list rather than `article-grid` — the card view renders a large
      # image placeholder per item, and neither project has a cover image.
      view: date-title-summary
      columns: 1
---

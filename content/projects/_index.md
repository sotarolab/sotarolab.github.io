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
      text: |-
        
        I complement my research and scientific programming background with software development initiatives. Particularly, I build live weather forecasting platforms that integrate operational model runs, real-time observations, machine learning, bias-correction algorithms, and modern interactive visualizations for decision support, with a focus on hydrometeorological extremes. Below you can explore some of the live platforms I currently mantain:

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

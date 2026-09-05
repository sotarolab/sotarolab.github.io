---
title: 'CV'
summary: Industry and academic experience, education, technical skills, and teaching.
date: 2026-08-09
type: landing

# Keep the old /experience/ URL working — this page replaced it.
aliases:
  - /experience/

design:
  spacing: '4rem'

# Experience and education are sourced from `data/authors/me.yaml`.
# Skills and teaching are written inline below — see the note on each block.
# Section order mirrors the source CV: summary, education, skills, research
# experience (independent + PhD), industry experience, teaching. The grouped
# timelines use the site override of the resume-experience block
# (layouts/_partials/hbx/blocks/resume-experience/block.html), which adds
# `title`, `filter_tags`, and show_experience/show_education options.
sections:
  - block: markdown
    content:
      title: 'Curriculum Vitae'
      text: |-
        <!-- Print-only masthead: hidden on screen (the site header already
             names him), shown in the generated PDF, which is a standalone
             document. NO phone number here on purpose. -->
        <div class="cv-print-header">
          <h1>Sebastian F. Otarola-Bustos, PhD</h1>
          <p>Rockville, MD · sfotarol@gmail.com · linkedin.com/in/sotarolab</p>
        </div>

        I am an atmospheric and hydrologic data scientist with a PhD in Atmospheric Sciences and four years of industry experience in data science and Machine Learning (ML) development for weather and hydrologic forecasting. For my PhD, I participated in two major field experiments on the U.S. west coast, where I operated scientific instrumentation to study atmospheric flows over complex terrain to improve boundary-layer parameterizations in weather models.

        I pursue independent research projects with a focus on operational pipelines and forecast verification, including deep learning for streamflow, climate downscaling, and live evaluation of AI and physics-based weather models.
    # Download button paused (Sep 2026) while the CV content is being revised;
    # static/uploads/cv.pdf was removed at the same time. To restore, put the
    # PDF back and append the button to the text above:
    #   <a class="applinks-btn applinks-btn--primary" href="/uploads/cv.pdf"
    #      download="Sebastian-Otarola-Bustos-Resume.pdf">
    #     Download CV (PDF)
    #   </a>
    design:
      columns: '1'

  # Education only — the experience timelines follow after the skills, as in
  # the source CV.
  - block: resume-experience
    content:
      username: me
    design:
      show_experience: false

  # Written inline rather than rendered from `me.yaml` by the `resume-skills`.
  - block: markdown
    content:
      title: 'Technical Skills'
      text: |-
        <!-- The trailing two spaces after each group name are a markdown hard
             line break — without them the label runs inline with its list. -->
        **Machine Learning & AI**  
        PyTorch • scikit-learn • CNNs • LSTM • gradient boosting • diffusion
        models • anomaly detection • forecast verification (Brier, reliability,
        NSE/KGE) • bias correction • extreme value analysis • AI-assisted
        development

        **Programming & Computational Stack**  
        Python • MATLAB • Git • SQL, SQLite, PostgreSQL • Docker • C++ • Linux
        • HTML • Cloud Computing • ArcGIS Pro

        **Atmospheric Models & Observations**  
        NWP Forecasting Systems (GFS, ECMWF IFS/AIFS, NAM, HRRR, WRF) • CMIP6
        • ERA5 • Satellite Remote Sensing (Sentinel-1, Sentinel-2, GOES) •
        Field instrumentation (Doppler lidar, microwave radiometer, radar,
        flux towers)
    design:
      columns: '1'

  # Independent research and the PhD, under one heading as in the source CV.
  - block: resume-experience
    content:
      username: me
      title: 'Research Experience'
      filter_tags: ['Independent', 'Academic']
    design:
      # No `date_format` here: this block prints `start`/`end` from me.yaml.
      show_education: false

  - block: resume-experience
    content:
      username: me
      title: 'Industry Experience'
      filter_tags: ['Industry']
    design:
      show_education: false

  # Deliberately a pointer, not a copy. The full record lives on /teaching/;
  # duplicating it here would mean two copies to keep in step, and they would
  # drift the first time one is edited.
  - block: markdown
    content:
      title: 'Teaching & Mentoring'
      text: |-
        Engineering mentoring at Hazen and Sawyer since 2022, and graduate
        teaching assistantships in environmental hydrology and fluid mechanics at
        Notre Dame. See [Teaching](/teaching/) for the full record.
    design:
      columns: '1'

  # NOTE: `resume-awards` and `resume-languages` are intentionally omitted while
  # `awards` and `languages` are empty in data/authors/me.yaml — an empty block
  # still renders its heading, leaving a bare title on the page.
---

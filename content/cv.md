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

        I am an atmospheric and hydrologic scientist. I hold a PhD in Fluid
        Dynamics and have 4 years of industry experience in water modeling and
        data science. For my PhD, I participated in two major field campaigns on
        the U.S. west coast, where I operated scientific instrumentation to study
        atmospheric flows over complex terrain to improve boundary layer
        parameterizations in weather models.

        At Hazen, I specialize in hydraulic and hydrologic modeling, GIS
        analysis, and Machine Learning (ML) for predictive modeling in flood and
        water supply projects. Outside of my role at Hazen, I pursue independent
        applied research projects and academic collaborations.

        <a class="applinks-btn applinks-btn--primary" href="/uploads/cv.pdf"
           download="Sebastian-Otarola-Bustos-Resume.pdf">
          Download CV (PDF)
        </a>
    design:
      columns: '1'

  - block: resume-experience
    content:
      username: me
    design:
      # No `date_format` here: this block prints `start`/`end` from me.yaml.
      is_education_first: false

  # Written inline rather than rendered from `me.yaml` by the `resume-skills`.
  - block: markdown
    content:
      title: 'Technical Skills'
      text: |-
        <!-- The trailing two spaces after each group name are a markdown hard
             line break — without them the label runs inline with its list. -->
        **Programming & Computational Stack**  
        Python Programming • MATLAB • GitHub Workflows • SQL, SQLite, PostgreSQL
        • Docker • C++ • Linux • HTML • Cloud Computing • LLMS • Agentic AI
        Workflows • ArcGIS Pro • H&H Modeling Software

        **Atmospheric & Climate Models**  
        NWP Forecasting Systems (GFS, ECMWF IFS/AIFS, NAM, HRRR, WRF) • CMIP6
        Project • ERA 5 • Remote Sensing (Sentinel 1, Sentinel 2, GOES)
    design:
      columns: '1'

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

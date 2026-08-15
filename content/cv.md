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

        My background spans water resources engineering, atmospheric fluid
        dynamics, and applied machine learning, in industry and in research.

        <!-- The PDF at the repo root is deliberately NOT the one published: it
             carries a personal phone number and this site is public and
             crawlable. What ships is static/uploads/cv.pdf, PRINTED FROM THIS
             PAGE, so it inherits the page's redactions (no client names, no
             project numbers, no phone) and cannot drift from it:

               make serve                       # or any local build
               "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
                 --headless=new --disable-gpu --no-pdf-header-footer \
                 --print-to-pdf=static/uploads/cv.pdf \
                 http://localhost:1313/cv/

             Layout comes from assets/css/custom/12-print.css. Regenerate it
             whenever the CV content changes. To publish a hand-made PDF
             instead, drop it at the same path; only remove the phone number
             first. -->
        <a class="applinks-btn applinks-btn--primary" href="/uploads/cv.pdf" download>
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

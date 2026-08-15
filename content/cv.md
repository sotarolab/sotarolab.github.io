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
        My background spans water resources engineering, atmospheric fluid
        dynamics, and applied machine learning — in industry and in research.

        <!-- The PDF at the repo root is deliberately NOT published: it carries a
             personal phone number and this site is public and crawlable. To
             offer a download, export a web version without it, save to
             `static/uploads/cv.pdf`, and uncomment the line below. -->
        <!-- [Download CV (PDF)](/uploads/cv.pdf) -->
    design:
      columns: '1'

  - block: resume-experience
    content:
      username: me
    design:
      # No `date_format` here: this block prints `start`/`end` from me.yaml
      # literally rather than parsing and reformatting them, so the dates are
      # written in human form there instead.
      #
      # Experience first — the applied record is the differentiator here, and
      # the PhD is visible in the education block right below it.
      is_education_first: false

  # Written inline rather than rendered from `me.yaml` by the `resume-skills`
  # block, which draws a 1–5 proficiency bar per item and requires a `level`.
  # The CV lists these unrated, and self-rated proficiency is a public claim
  # many reviewers discount. Two groups, verbatim from the CV — edit here.
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
        Notre Dame — see [Teaching](/teaching/) for the full record.
    design:
      columns: '1'

  # NOTE: `resume-awards` and `resume-languages` are intentionally omitted while
  # `awards` and `languages` are empty in data/authors/me.yaml — an empty block
  # still renders its heading, leaving a bare title on the page.
---

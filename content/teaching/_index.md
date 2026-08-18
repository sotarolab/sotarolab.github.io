---
title: Teaching
summary: Engineering mentoring at Hazen and Sawyer, and graduate teaching at Notre Dame.
type: landing

# `docs` type for the pages nested under this section — gives each course its.

cascade:
  - target:
      path: '{/teaching/*/**}'
    type: docs
    params:
      show_breadcrumb: true

sections:
  # No intro block: the page opens straight on the record. "Professional
  # Mentoring" is therefore the first section, and takes the page-title
  # treatment that 04-sections.css gives a landing page's first heading.
  # Verbatim from the Teaching & Mentoring section of the CV. /cv/ links here
  # rather than repeating it, so there is one copy to keep current.
  - block: markdown
    id: professional-mentoring
    content:
      title: 'Professional Mentoring'
      text: |-
        **Engineering Mentoring — Hazen and Sawyer** · Aug 2022 – Present

        - Mentored junior engineers in hydraulic modeling (InfoWater Pro,
          PCSWMM), GIS software, and Python-based workflows to automate
          labor-intensive tasks and increase work accuracy.
        - Trained junior engineers and scientists in GitHub workflows and best
          development practices for collaborative data science and machine
          learning projects.
    design:
      columns: '1'

  - block: markdown
    id: graduate-teaching
    content:
      title: 'Graduate Teaching'
      text: |-
        **Graduate Teaching Assistant — University of Notre Dame** · 2017 – 2018

        - **CE 30455: Environmental Hydrology** (Fall 2017, Fall 2018). Conducted
          office hours and problem-solving sessions ahead of mid-terms and
          exams. Graded homework, mid-terms, and exams. Prepared laboratory
          demonstrations (Prof. Andrew Kennedy).
        - **CE 30460: Fluid Mechanics** (Spring 2017, Spring 2018). Conducted
          office hours and problem-solving sessions ahead of mid-terms and
          exams. Graded homework, mid-terms, and exams (Prof. David Richter).
    design:
      columns: '1'
---

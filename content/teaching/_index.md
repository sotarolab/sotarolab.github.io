---
title: Teaching
summary: Engineering mentoring at Hazen and Sawyer, graduate teaching at Notre Dame, and a course proposal in machine learning for weather extremes.
type: landing

# `docs` type for the pages nested under this section — gives each course its
# own sidebar and breadcrumb. The target pattern must track the section's own
# path: this section was `content/courses/` until it was renamed to match the
# /teaching/ nav item, and a stale pattern here fails silently (the pages build,
# they just lose the docs chrome).
cascade:
  - target:
      path: '{/teaching/*/**}'
    type: docs
    params:
      show_breadcrumb: true

sections:
  - block: markdown
    content:
      title: 'Teaching'
      text: |-
        I teach mostly by mentoring — engineers moving into modelling and machine
        learning — and taught undergraduate hydrology and fluid mechanics during
        my PhD.
    design:
      columns: '1'

  # Verbatim from the Teaching & Mentoring section of the CV. /cv/ links here
  # rather than repeating it, so there is one copy to keep current.
  - block: markdown
    content:
      title: 'Mentoring'
      text: |-
        **Engineering Mentoring — Hazen and Sawyer** · Aug 2022 – Present

        - Mentored junior engineers in hydraulic modeling (InfoWater Pro,
          PCSWMM), GIS software, and Python-based workflows to automate
          labor-intensive tasks and increase work accuracy.
        - Trained junior engineers and scientists in GitHub workflows and best
          development practices in collaborative data science and machine
          learning projects.
    design:
      columns: '1'

  - block: markdown
    content:
      title: 'Graduate Teaching'
      text: |-
        **Graduate Teaching Assistant — University of Notre Dame** · 2017 – 2018

        - **CE 30455: Environmental Hydrology** (Fall 2017, Fall 2018). Conducted
          office hours and problem-solving sessions ahead of mid-terms. Graded
          homework, mid-terms, and exams. Prepared laboratory demonstrations
          (Prof. Andrew Kennedy).
        - **CE 30460: Fluid Mechanics** (Spring 2017, Spring 2018). Conducted
          office hours and problem-solving sessions ahead of mid-terms. Graded
          homework, mid-terms, and exams (Prof. David Richter).
    design:
      columns: '1'

  # Course pages are sections tagged `Course`, hence `kinds: [section]` — a
  # plain page with the same tag would not be matched.
  - block: collection
    id: courses
    content:
      title: 'Course Development'
      text: |-
        A course I have designed and would be glad to teach.
      filters:
        tag: Course
        kinds:
          - section
    design:
      view: date-title-summary
      columns: 1
---

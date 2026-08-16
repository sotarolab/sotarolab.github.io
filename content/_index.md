---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      # BOTH the bio prose and the animation strip live HERE, in the.
      text: |
        I am an atmospheric and hydrologic scientist with a PhD in Civil and Environmental Engineering and Earth Sciences from the **University of Notre Dame**, where I studied atmospheric turbulence and complex-terrain boundary layers at the [Environmental Fluid Dynamics Laboratory](https://efmlab.nd.edu/) under Harindra J. S. Fernando. I am currently a **Principal Scientist at [Hazen](https://www.hazenandsawyer.com/)**, where I apply machine learning and hydrologic modeling to decision support for water utilities.

        My research interests include:
        
        - Boundary-layer turbulence and stratified flow over complex terrain
        - Atmospheric rivers and the predictability of extreme precipitation
        - Flood forcasting and hydrodynamic modeling
        - Statistical and deep-learning downscaling of climate extremes
        - Remote sensing and forecast verification for operational systems
        
        I am pursuing applied research in these areas and welcome collaborations across academia and industry.
        
        <div class="astrip not-prose">
          <div class="astrip-duo">
          <figure class="astrip-item" style="--ar: 1">
            <video class="astrip-media" autoplay muted loop playsinline
                   preload="metadata" poster="/media/about/chile-ar-ivt-jul2026-v7-poster.jpg"
                   aria-label="Animated map of integrated vapor transport over the southeast Pacific and Chile, 15–19 July 2026, with particle streaks tracing an atmospheric river's moisture flux into the coast.">
              <source src="/media/about/chile-ar-ivt-jul2026-v7.mp4" type="video/mp4">
            </video>
            <figcaption class="astrip-cap">
              <b>Atmospheric river, July 2026.</b> Integrated vapor transport derived from GEFS control. The streaks trace the moisture flux. This event was responsible for catastrophic flooding across Chile. From my <a href="/projects/chile-ar-nowcast/">live
              AR nowcast</a>.
            </figcaption>
          </figure>
          <!-- Autoplaying, no controls — a deliberate call ("gif so no
               play button"; a muted looping mp4 is gif-equivalent at ~10x
               smaller filesize). No live application exists behind this
               clip, so the caption states the data sources instead of
               linking anywhere. -->
          <figure class="astrip-item" style="--ar: 1">
            <video class="astrip-media" autoplay muted loop playsinline
                   preload="metadata" poster="/media/about/recoleta-dark-poster.jpg"
                   aria-label="Animated satellite imagery of Embalse Recoleta, Chile, 15 June to 27 July 2026, each frame date-stamped in the corner, with nearby communities labelled: the reservoir's mapped surface water doubles after the atmospheric river, spreading up its northern arm and past the dam at El Tranque, which is flagged when the water reaches it.">
              <source src="/media/about/recoleta-dark.mp4" type="video/mp4">
            </video>
            <figcaption class="astrip-cap">
              <b>Embalse Recoleta, Chile.</b> Sentinel mapping of the
              reservoir filling after that atmospheric river made landfall:
              surface water rose from 1.9 to 3.9&nbsp;km² and the reservoir
              spilled on 21 July. Sentinel-2 optical imagery, with
              Sentinel-1 radar under cloud.
            </figcaption>
          </figure>
          </div>
        </div>
      headings:
        # "About" rather than the default "Professional Summary" — plainer, and
        # matches the nav item.
        about: 'About'
        education: ''
        interests: ''
    design:
      # Gradient mesh off — flat surface reads cleaner against the dark header band
      background:
        gradient_mesh:
          enable: false

      # Name heading sizing to accommodate long or short names.
      # `xs` because the sidebar is only 4 of 12 columns — at `md` a
      # double-barrelled name wraps to three lines and out-shouts the bio.
      name:
        size: xs # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded

  # News instead of Selected Publications (a design decision on the publication side; news is where upcoming.
  - block: collection
    id: news
    content:
      title: News
      subtitle: ''
      text: ''
      count: 3
      filters:
        folders:
          - blog
      offset: 0
      order: desc
    design:
      view: date-title-summary
      spacing:
        padding: [0, 0, 0, 0]
---

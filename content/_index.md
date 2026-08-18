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
        
        I am an atmospheric and hydrologic scientist. I obtained my PhD in Civil and Environmental Engineering and Earth Sciences from the **University of Notre Dame** in 2022. My dissertation research was conducted as part of the [WFIP2](https://psl.noaa.gov/renewable_energy/wfip2/) wind-energy field campaign, where I used in-situ and remote sensing instrumentation to study atmospheric turbulence and boundary-layer processes in complex terrain to evaluate the skill of numerical weather model parameterizations.
 
        After my PhD, I joined [Hazen](https://www.hazenandsawyer.com/), where my interest in numerical modeling and scientific programming pulled me toward machine learning (ML). I am currently a **Principal Scientist** building hydraulic and hydrologic models, geospatial data pipelines, and ML systems that support water utilities in water supply management, flood mapping, climate resiliency, and operational decision support. 
        
        My research areas include:
        
        - Boundary-layer turbulence and stratified flow over complex terrain
        - Atmospheric rivers and the predictability of extreme precipitation
        - Flood forecasting and hydrodynamic modeling
        - Statistical and deep-learning downscaling of climate extremes
        - Remote sensing and forecast verification for operational systems
        
        <div class="astrip not-prose">
          <div class="astrip-duo">
          <figure class="astrip-item" style="--ar: 1">
            <video class="astrip-media" autoplay muted loop playsinline
                   preload="metadata" poster="/media/about/chile-ar-ivt-jul2026-v7-poster.jpg"
                   aria-label="Animated map of integrated vapor transport over the southeast Pacific and Chile, 15–19 July 2026, with particle streaks tracing an atmospheric river's moisture flux into the coast.">
              <source src="/media/about/chile-ar-ivt-jul2026-v7.mp4" type="video/mp4">
            </video>
            <figcaption class="astrip-cap">
              <b>Atmospheric river, July 2026.</b> Integrated vapor transport derived from GEFS control. The streaks trace the moisture flux. The event produced significant flooding in central and northern Chile. From my <a href="/projects/chile-ar-nowcast/">live
              AR nowcast</a>.
            </figcaption>
          </figure>
          <!-- Autoplaying and muted with no controls: a looping mp4 is
               gif-equivalent at roughly a tenth of the filesize. No live
               application sits behind this clip, so the caption names the
               data sources rather than linking anywhere. -->
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

  # News rather than Selected Publications: /publications/ carries the full
  # record, and news is where upcoming talks and submissions surface first.
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

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
        I am an environmental fluid dynamicist with a **PhD from the University of
        Notre Dame**, where I worked on atmospheric turbulence and complex-terrain
        boundary layers, and a background in water resources engineering. I am
        currently a **Principal Scientist at Hazen**.

        My work, research, and professional interests focus on leveraging machine learning
        (LSTM, diffusion, decision trees, and neural networks) and remote sensing to emulate
        physics-based approaches in atmospheric and hydrologic systems, with a focus on
        scalability and operational forecasting. I have a wide research background in
        environmental flows that includes:

        - Atmospheric boundary layer and turbulent stratified flows in complex terrain
        - Atmospheric rivers, hydrological forecasting, and climate downscaling
        - Ground- and space-based remote sensing, and live weather-intelligence platforms

        I am interested in pursuing applied research in these areas, and in fostering
        collaborations between industry and academia.

        <div class="astrip not-prose">
          <div class="astrip-duo">
          <figure class="astrip-item" style="--ar: 1">
            <video class="astrip-media" autoplay muted loop playsinline
                   preload="metadata" poster="/media/about/chile-ar-ivt-jul2026-v6-poster.jpg"
                   aria-label="Animated map of integrated vapor transport over the southeast Pacific and Chile, 15–19 July 2026, with particle streaks tracing an atmospheric river's moisture flux into the coast.">
              <source src="/media/about/chile-ar-ivt-jul2026-v6.mp4" type="video/mp4">
            </video>
            <figcaption class="astrip-cap">
              <b>Atmospheric river, July 2026.</b> Integrated vapor transport
              into Chile from the GEFS control run; the streaks trace the
              moisture flux. From my <a href="/projects/chile-ar-nowcast/">live
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
                   preload="metadata" poster="/media/about/la-paloma-dark-poster.jpg"
                   aria-label="Animated satellite imagery of Embalse La Paloma, Chile, from 15 June to 27 July 2026, the reservoir's mapped surface water growing after the atmospheric river.">
              <source src="/media/about/la-paloma-dark.mp4" type="video/mp4">
            </video>
            <figcaption class="astrip-cap">
              <b>Embalse La Paloma, Chile, June to July 2026.</b> Sentinel
              mapping of the reservoir refilling after that atmospheric river
              made landfall. Surface water more than doubled, from
              4.5 to 9.4&nbsp;km². Mapped with Sentinel-2 optical imagery, and
              with Sentinel-1 radar under cloud.
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

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
      # BOTH the bio prose and the animation strip live HERE, in the
      # biography block's `text` field. Two reasons, learned the hard way:
      #
      # 1. The strip must render inside the text column, directly under the
      #    bio paragraph. Every separate-section attempt left a large gap —
      #    a section cannot start until the whole biography (including the
      #    sidebar, which runs ~200px past the paragraph) has ended.
      #    Sebastian flagged that gap three times; do not move it back out.
      # 2. The block renders a non-empty `text` INSTEAD OF the me.yaml
      #    `bio`, not after it — so the bio prose must come along. me.yaml's
      #    `bio` field now just points here.
      #
      # The prose was verbatim from the CV's Professional Summary until
      # 2026-08-14, when Sebastian asked for the register of
      # jcsandov.github.io — standing first, then the method arsenal, then a
      # list of research threads. On 2026-08-15 he rewrote it himself; this
      # is HIS wording, so treat it as authoritative — copy-edit only, and
      # take substantive rewrites back to him first. The three bullets are
      # deliberately the three threads on /research/, phrased — his first
      # draft had seven one-word topics and read as a skills inventory
      # (his own call, 2026-08-15). Keep them in step with research.yaml.
      # All facts are from his
      # CV and this site; the closing sentence IS still his CV wording
      # verbatim, and stays deliberate: interest, not intent — "seeking a
      # postdoc" framing belongs in application materials, not on a public
      # page.
      #
      # Strip content — Sebastian's final pick (2026-08-14): two stacked
      # loops, atmospheric river above, reservoir filling below, each with a
      # caption tying it to a /research/ thread or project. Sizes are
      # deliberately unequal (see 07-about-strip.css).
      #
      # Each tile is a loop pre-cropped to its exact frame with ffmpeg —
      # never rely on CSS cover-cropping here, it produced illegible tiles
      # once already. Sources: the AR nowcast render and the La Paloma
      # Sentinel pipeline (la-paloma re-timed with cross-dissolves,
      # setpts=1.6*PTS + framerate blend — the raw 1 fps cuts read "too
      # fast"). To swap a tile: render an mp4 + poster into
      # static/media/about/, update the path and --ar here.
      # Styling: assets/css/custom/07-about-strip.css.
      text: |
        I am a water resources engineer with a **PhD in Fluid Dynamics** from the
        **University of Notre Dame**, and currently a **Principal Scientist at Hazen**.

        My work, research, and professional interests focus on leveraging machine learning
        (LSTM, diffusion, decision trees, and neural networks) and remote sensing to emulate
        physics-based approaches in atmospheric and hydrologic systems, with a focus on
        scalability and operational forecasting. I have a wide research background in
        environmental flows that includes:

        - Atmospheric boundary layer and turbulent stratified flows in complex terrain
        - Atmospheric rivers, hydrological forecasting, and climate downscaling
        - Ground- and space-based remote sensing, and live weather-intelligence platforms

        I am interested in pursuing applied research at the intersection of weather extremes,
        flood forecasting, remote sensing, and ML development, and fostering collaborations between
        industry and academia.

        <div class="astrip not-prose">
          <div class="astrip-duo">
          <figure class="astrip-item" style="--ar: 1">
            <video class="astrip-media" autoplay muted loop playsinline
                   preload="metadata" poster="/media/about/chile-ar-ivt-jul2026-v6-poster.jpg"
                   aria-label="Animated map of integrated vapour transport over the southeast Pacific and Chile, 15–19 July 2026, with particle streaks tracing an atmospheric river's moisture flux into the coast.">
              <source src="/media/about/chile-ar-ivt-jul2026-v6.mp4" type="video/mp4">
            </video>
            <figcaption class="astrip-cap">
              <b>Atmospheric river, Jul 2026.</b> Integrated vapour transport
              streaming into Chile, GEFS control — streaks trace the moisture
              flux. From my <a href="/projects/chile-ar-nowcast/">live AR
              nowcast</a>.
            </figcaption>
          </figure>
          <!-- Autoplaying, no controls — Sebastian's final call ("gif so no
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
              <b>Embalse La Paloma, Chile — Jun–Jul 2026.</b> Sentinel
              satellite mapping of the reservoir refilling after that
              atmospheric river's landfall — surface water more than doubled,
              4.5&nbsp;→&nbsp;9.4&nbsp;km². Sentinel-2 optical where skies
              were clear, Sentinel-1 radar where they were not.
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

  # News instead of Selected Publications (Sebastian, 2026-08-14: "I haven't
  # been that active" on the publication side; news is where upcoming
  # conferences and talks go). Pulls the latest posts from content/blog/ —
  # add a news item by adding a post there (see docs/CONTENT.md). The
  # `featured` flags in data/publications.yaml are currently unused but kept
  # in case the publications block ever returns (it was a `collection`
  # block, view: citation, count: 3).
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

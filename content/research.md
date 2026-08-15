---
# ⚠️ GENERATED FILE — DO NOT EDIT.
# Source: data/research.yaml   Regenerate: make research
# Edits here are silently reverted the next time the generator runs.
title: "Research"
summary: "Machine learning for weather and hydrologic forecasting — climate downscaling, streamflow during atmospheric-river floods, and boundary-layer meteorology in complex terrain."
date: 2026-08-09
type: landing

design:
  spacing: "4rem"

sections:
  - block: markdown
    content:
      title: "Research"
      text: |-
        I am trained in fluid dynamics, atmospheric boundary layers, and turbulent flows 
        in complex terrain, particularly, how these phenomena are represented in numerical 
        weather prediction (NWP) models. To tackle this problem, I leverage
        a wide array of scientific instrumentation platforms including in-situ
        and remote sensing, as well as operational weather forecast and climate models.  

        I also have hydraulics and hydrology expertise and professional experience building 
        water models for urban and natural systems to assess flood risk during wet weather
        events under current and future climate scenarios for resiliency in water utilities.
    design:
      columns: '1'
  - block: markdown
    content:
      title: "Downscaling CMIP6 Projections over Chile"
      text: |-
        Collaborative research with Chile and US researchers training a
        convolutional neural network to downscale CMIP6-based climate projections
        of extreme precipitation and temperature in Chile. The CNN is able to
        capture Chile's unique topography, and we are investigating the physical
        mechanisms driving the changes so the methodology can be applied to other
        regions. An abstract on this work is submitted to the
        [AGU Fall Meeting 2026](/publications/agu2026-cmip6-downscaling-chile/),
        with a journal manuscript in preparation for *Climate Dynamics*.

        <div class="rstrip-align not-prose">
        <div class="rstrip">

          <figure class="rstrip-item" style="--ar: 2752/3694; --fig-w: 680px">
            <div class="rstrip-frame">
              <img class="rstrip-media" src="/media/research/chile-cnn-downscaled.png"
                loading="lazy" alt="Six maps of Chile at 0.05-degree resolution showing CNN-downscaled change from 1981–2010 to 2071–2100 under SSP5-8.5: the top row is the change in maximum one-day precipitation for NESM3, the 27-model ensemble mean, and HadGEM3-GC31-LL; the bottom row is the change in maximum temperature for INM-CM5-0, the 26-model ensemble mean, and UKESM1-0-LL, with fine Andean structure visible in every panel.">
            </div>
            <figcaption class="rstrip-cap">
              <b>CNN-downscaled change at 0.05° (~5 km).</b> Rx1day (top) and TXx
              (bottom), 2071–2100 under SSP5-8.5 minus 1981–2010 — the ensemble
              mean flanked by the models that bracket it. The native CMIP6 grids
              are ~1°; the CNN restores the Andean structure the extremes
              actually follow.
            </figcaption>
          </figure>

        </div>
        </div>
    design:
      columns: '1'
  - block: markdown
    id: streamflow-ar-floods
    content:
      title: "Streamflow Prediction during Atmospheric-River Floods"
      text: |-
        Applying Long Short-Term Memory (LSTM) and diffusion algorithms to predict
        flow discharges in US west coast basins, and stress testing them for flood
        events during atmospheric river events. We are benchmarking the results
        against process-based models (GR4J and CemaNeige) for basins associated
        with various hydrological regimes. An abstract on this work is submitted
        to the [AGU Fall Meeting 2026](/publications/agu2026-lstm-diffusion-ar-floods/),
        with a journal manuscript in preparation for the *Journal of Hydrology*.

        <div class="rstrip-align not-prose">
        <div class="rstrip">

          <figure class="rstrip-item rstrip-item--wide" style="--ar: 1280/640">
            <div class="rstrip-frame">
              <video class="rstrip-media"
                data-src="/media/research/guerneville-flood.mp4"
                poster="/media/research/guerneville-flood-poster.jpg"
                muted loop playsinline controls preload="none"
                aria-label="Animated shallow-water simulation of the February 2019 Russian River flood at Guerneville, California, water depth spreading across the floodplain over shaded terrain."></video>
            </div>
            <figcaption class="rstrip-cap">
              <b>Russian River at Guerneville, CA — Feb 2019.</b> A shallow-water
              solver reconstructing an atmospheric-river flood on a 20&nbsp;m
              grid — the kind of event the LSTM and diffusion models are
              stress-tested against.
            </figcaption>
          </figure>

          <figure class="rstrip-item rstrip-item--wide" style="--ar: 3063/2457">
            <div class="rstrip-frame">
              <img class="rstrip-media" src="/media/research/caudal-lstm-nwm-abc.png"
                loading="lazy" alt="Three-panel comparison of a regional LSTM against the National Water Model over about 70 US west coast basins: scatters of whole-record NSE and NSE on atmospheric-river days, both with most basins above the 1:1 line favouring the LSTM, and a bar chart of median relative peak error on AR floods by method, where the LSTM ensemble mean is worst at 0.407 and the train-selected q75 LSTM is best at 0.221, ahead of the National Water Model's 0.253.">
            </div>
            <figcaption class="rstrip-cap">
              <b>The ranking depends on the question.</b> The regional LSTM beats
              the NWM v3.0 retrospective on skill — whole-record and on AR
              days — yet its ensemble mean is the worst peak estimator on AR
              floods; reading the ensemble at q75 overtakes the NWM. From the
              LSTM/diffusion benchmarking study.
            </figcaption>
          </figure>

        </div>
        </div>
    design:
      columns: '1'
  - block: markdown
    content:
      title: "Boundary-Layer Meteorology in Complex Terrain"
      text: |-
        My doctoral work, and the origin of most of the publication record. I
        participated in two major experiments — the Wind Forecast Improvement
        Project 2 (WFIP2) in the Columbia River Gorge (OR) and the Sundowner Winds
        Experiment (SWEX) in Santa Barbara (CA) — deploying flux towers and
        Doppler lidars and processing their observations to study the skill of
        weather forecasting models in complex terrain. The main results, examining
        the subgrid variability of surface layer turbulence from 18 months of
        observational data benchmarked against the WRF model, are published in
        [*Boundary-Layer Meteorology*](/publications/2023-blm-subgrid-variability/).

        <div class="rstrip-align not-prose">
        <div class="rstrip">

          <figure class="rstrip-item rstrip-item--wide" style="--ar: 651/282">
            <div class="rstrip-frame">
              <img class="rstrip-media" src="/media/research/wfip2/terrain_comparisson_real_vs_NWP_model.png"
                loading="lazy" alt="Side-by-side terrain comparison for WFIP2: real high-resolution terrain with the tower array circled and a dozen tower positions marked, beside the same area as the weather model's grid, where the terrain is a handful of smooth coloured cells.">
            </div>
            <figcaption class="rstrip-cap">
              <b>What the model sees.</b> The WFIP2 tower array on real terrain
              (left) and the same ground in the NWP model's grid (right) — a
              dozen towers sampling terrain the model resolves as a few smooth
              cells. The turbulence variability inside that circle is what the
              <a href="/publications/2023-blm-subgrid-variability/"><i>Boundary-Layer
              Meteorology</i> paper</a> quantifies.
            </figcaption>
          </figure>

          <figure class="rstrip-item" style="--ar: 1019/559">
            <div class="rstrip-frame">
              <img class="rstrip-media" src="/media/research/SWEX/instruments/lidar_and_tower.jpeg"
                loading="lazy" alt="Two photographs side by side: a ceilometer and a scanning Doppler lidar deployed on a ridge above Santa Barbara with the Pacific Ocean behind, and an instrumented flux tower standing in a grassy field site.">
            </div>
            <figcaption class="rstrip-cap">
              <b>The instruments.</b> Scanning Doppler lidar and ceilometer on
              the ridge above Santa Barbara (left) and a flux tower at the
              valley site (right), deployed for SWEX — the platforms behind the
              scans below.
            </figcaption>
          </figure>

          <figure class="rstrip-item" style="--ar: 524/312">
            <div class="rstrip-frame">
              <img class="rstrip-media" src="/media/research/SWEX/Results/terrain_new.png"
                loading="lazy" alt="Grayscale terrain map of the Santa Ynez valley with the SYA lidar site marked and a straight line through it showing the range–height scan track along azimuth 315 degrees, labelled as panel a.">
            </div>
            <figcaption class="rstrip-cap">
              <b>The scan line.</b> RHI track along azimuth 315° through the SYA
              site — the transect the scans below sweep.
            </figcaption>
          </figure>

          <figure class="rstrip-item rstrip-item--wide" style="--ar: 874/820">
            <div class="rstrip-frame">
              <img class="rstrip-media" src="/media/research/SWEX/Results/Lidar_new.png"
                loading="lazy" alt="Sequence of five range–height lidar scans along azimuth 315 degrees through the night of 21–22 April 2020, each showing a shallow yellow outflow layer near 400 metres over blue return flow.">
            </div>
            <figcaption class="rstrip-cap">
              <b>One night, scan by scan.</b> Doppler-lidar range–height scans
              along azimuth 315° through the SYA site in the Santa Ynez valley,
              over the night of 21–22 April: a shallow downslope jet rides a few
              hundred metres above the lidar while the opposing layer holds
              beneath it. From the SWEX campaign.
            </figcaption>
          </figure>

        </div>
        </div>
    design:
      columns: '1'
---

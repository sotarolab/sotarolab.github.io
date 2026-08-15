---
title: 'Research'
summary: >-
  Machine learning for weather and hydrologic forecasting — climate
  downscaling, streamflow during atmospheric-river floods, and
  boundary-layer meteorology in complex terrain.
date: 2026-08-09

# A standing page, not a post: the byline row would otherwise print a date
# and a reading time under the title.
show_date: false
reading_time: false
---

<!--
  This page is hand-written markdown. It was generated from data/research.yaml
  by tools/gen_research.py until 2026-08-15, when the prose turned out to be
  edited far more often than the figures and the round-trip through YAML
  (block scalars, `make research`) was costing more than the structure bought.
  Both the generator and the YAML are gone; git history has them.

  Figures use two shortcodes, layouts/_shortcodes/rfig.html and rstrip.html —
  read the comments there before adding one. The short version:

      {{</* rstrip */>}}
      {{</* rfig image="/media/research/thing.png" ratio="1600/900"
               alt="Description for screen readers." */>}}
      **Bold lead-in.** A sentence about what it shows.
      {{</* /rfig */>}}
      {{</* /rstrip */>}}

  `ratio` is the source file's true pixel width/height — it reserves layout
  space so the page does not jump as media loads. `alt` is required, and a
  video also needs `poster=`; the build FAILS without them. Media lives in
  static/media/research/. Two figures in one rstrip render side by side.

  The three section headings here are the three threads the About-page bio
  bullets summarise (content/_index.md) — keep them in step. That includes
  the opening line: it says "three", and it is the page's only framing since
  the two biography paragraphs that used to sit here were cut on 2026-08-15
  for repeating the About bio almost verbatim. Add a fourth thread and the
  line needs updating; do not reintroduce a biography here.
-->

Three active threads, from climate projections down to the turbulence that
weather models cannot resolve.

## Downscaling CMIP6 Projections over Chile

Collaborative research with Chile and US researchers training a
convolutional neural network to downscale CMIP6-based climate projections
of extreme precipitation and temperature in Chile. The CNN is able to
capture Chile's unique topography, and we are investigating the physical
mechanisms driving the changes so the methodology can be applied to other
regions. An abstract on this work is submitted to the
[AGU Fall Meeting 2026](/publications/agu2026-cmip6-downscaling-chile/),
with a journal manuscript in preparation for *Climate Dynamics*.

<!-- Figure from ~/dev/chile-super-extremes/paper/agu2026/figures/
     fig_downscaled_0p05.png (copied 2026-08-14) — the AGU-styled export.
     Companions in that folder if this ever changes: fig_agu_combined (adds
     the 1° CMIP6 baseline above this panel — the coarse-vs-fine pairing, but
     poster-tall with baked captions) and fig_agreement_1deg.
     Sized 680px, then 600px (Sebastian, 2026-08-15) — the source is portrait
     (2752x3694), so every 100px of width costs ~134px of height, and this is
     the figure that sets how tall the first section reads. -->
{{< rstrip >}}
{{< rfig image="/media/research/chile-cnn-downscaled.png"
         image_dark="/media/research/chile-cnn-downscaled-dark.png" ratio="2752/3694" width="600px"
         alt="Six maps of Chile at 0.05-degree resolution showing CNN-downscaled change from 1981–2010 to 2071–2100 under SSP5-8.5: the top row is the change in maximum one-day precipitation for NESM3, the 27-model ensemble mean, and HadGEM3-GC31-LL; the bottom row is the change in maximum temperature for INM-CM5-0, the 26-model ensemble mean, and UKESM1-0-LL, with fine Andean structure visible in every panel." >}}
**CNN-downscaled change at 0.05° (~5 km).** Rx1day (top) and TXx (bottom),
2071–2100 under SSP5-8.5 minus 1981–2010, with the ensemble mean flanked by the
models that bracket it. The native CMIP6 grids are ~1°.
{{< /rfig >}}
{{< /rstrip >}}

## Streamflow Prediction during Atmospheric-River Floods {#streamflow-ar-floods}

Applying Long Short-Term Memory (LSTM) and diffusion algorithms to predict
flow discharges in US west coast basins, and stress testing them for flood
events during atmospheric river events. We are benchmarking the results
against process-based models (GR4J and CemaNeige) for basins associated
with various hydrological regimes. An abstract on this work is submitted
to the [AGU Fall Meeting 2026](/publications/agu2026-lstm-diffusion-ar-floods/),
with a journal manuscript in preparation for the *Journal of Hydrology*.

<!-- The explicit {#streamflow-ar-floods} anchor predates the auto-generated
     one and is kept so any existing deep link survives.
     The Guerneville animation moved here from the About page (2026-08-14,
     trimming the landing page) — it is this thread's subject matter: an AR
     flood in a US west coast basin, reconstructed by Sebastian's
     shallow-water solver.
     The second figure is from ~/dev/caudal/paper/agu26/figures/fig_agu_abc.png
     (copied 2026-08-14) — the AGU-styled export, chosen over the notebook-04
     inline figures after their small fonts proved illegible at page width.
     Companions there: fig_agu_single (adds the study-area map),
     fig_lstm_vs_nwm_scatter (panels A/B only).
     Both figures in this strip were wide="true" until 2026-08-15 (Sebastian:
     "a bit too wide"). `wide` is for figures that are ILLEGIBLE below full
     rail — panoramic, many-panelled, fine print. These two are not: the video
     is 2:1, and the three-panel comparison is nearly square, so full rail made
     it ~620px tall and it swamped the section. Explicit widths instead, then
     tuned up again on the same day at Sebastian's request: the video at 820px
     (essentially the text rail) and the scatter at 700px. The point of the
     `width` values over `wide` is that these two stay INSIDE the rail while
     the genuinely panoramic figures below break out of it. -->
{{< rstrip >}}
{{< rfig video="/media/research/guerneville-flood.mp4" poster="/media/research/guerneville-flood-poster.jpg" ratio="1280/640" width="820px"
         alt="Animated shallow-water simulation of the February 2019 Russian River flood at Guerneville, California, water depth spreading across the floodplain over shaded terrain." >}}
**Russian River at Guerneville, CA, Feb 2019.** A shallow-water solver
reconstructing an atmospheric-river flood on a 20&nbsp;m grid.
{{< /rfig >}}
{{< rfig image="/media/research/caudal-lstm-nwm-abc.png"
         image_dark="/media/research/caudal-lstm-nwm-abc-dark.png" ratio="3063/2457" width="700px"
         alt="Three-panel comparison of a regional LSTM against the National Water Model over about 70 US west coast basins: scatters of whole-record NSE and NSE on atmospheric-river days, both with most basins above the 1:1 line favoring the LSTM, and a bar chart of median relative peak error on AR floods by method, where the LSTM ensemble mean is worst at 0.407 and the train-selected q75 LSTM is best at 0.221, ahead of the National Water Model's 0.253." >}}
**Regional LSTM against NWM v3.0 retrospective.** The LSTM wins on skill, both
whole-record and on AR days, yet its ensemble mean is the worst peak estimator
on AR floods. Read at q75 it overtakes the NWM.
{{< /rfig >}}
{{< /rstrip >}}

<!-- NOTE: a 'Live Forecast Platforms' section lived here until 2026-08-15
     (removed at Sebastian's request — the platforms are what is BUILT, so
     they belong to /projects/, which the About-strip captions now link
     directly). Its animations had already moved to the About page. -->

## Boundary-Layer Meteorology in Complex Terrain

My doctoral work, and the origin of most of the publication record. I
participated in two major experiments: the Wind Forecast Improvement Project 2
(WFIP2) in the Columbia River Gorge (OR) and the Sundowner Winds Experiment
(SWEX) in Santa Barbara (CA), deploying flux towers and Doppler lidars and
processing their observations to study the skill of weather forecasting models
in complex terrain. The main results, examining the subgrid variability of
surface layer turbulence from 18 months of observational data benchmarked
against the WRF model, are published in
[*Boundary-Layer Meteorology*](/publications/2023-blm-subgrid-variability/).

<!-- Slimmed twice on 2026-08-15 (Sebastian: section was "too heavy on the
     boundary layer", risked reading "too broad", and the time series "feels
     too dense"): now ONE published-WFIP2 figure + ONE SWEX thesis figure,
     plus the scan-line map the scan panels refer to. Cut but still in the
     archive folders (which SHIP publicly even unreferenced — delete if that
     ever matters): the ridge lidar/ceilometer photo, the 3D coplanar scan,
     the scan-line terrain map variants, domain maps, and both WFIP2 time
     series.
     The live mountain-wave canvas (Queney solution, assets/js/mountain-waves.js)
     was removed 2026-08-15: with a real deployment photo and three
     observation figures, the theory animation read as decoration. The JS
     stays on disk but is no longer bundled (custom-assets.html) — to restore,
     re-add it there and re-add the figure as raw HTML (the mtw-* rules are
     still in 06-figures.css).
     Sizing (Sebastian, 2026-08-15): "a bit smaller and left aligned with
     text". The two figures here were wide="true", which puts them in the
     full-rail breakout from 09-page-width.css — that rule uses a negative
     margin, so a wide figure starts LEFT of the text column and reads as
     misaligned. Explicit widths keep the strip inside the rail, where
     .rstrip's grid already left-aligns every item. Do not put `wide` back on
     these without also accepting the outdent.
     NB on the WFIP2 terrain figure: the source is only 651px wide, so it is
     displayed at ~1.07x now — a higher-res export would still sharpen it. -->
{{< rstrip >}}
{{< rfig image="/media/research/wfip2/terrain_comparisson_real_vs_NWP_model.png" ratio="651/282" width="700px"
         alt="Side-by-side terrain comparison for WFIP2: real high-resolution terrain with the tower array circled and a dozen tower positions marked, beside the same area as the weather model's grid, where the terrain is a handful of smooth colored cells." >}}
**WFIP2 tower array, Columbia River Gorge.** Real terrain with the towers
marked (left) and the same ground on the NWP model's grid (right), where it
resolves as a few smooth cells. The
[*Boundary-Layer Meteorology* paper](/publications/2023-blm-subgrid-variability/)
quantifies the variability inside that circle.
{{< /rfig >}}
<!-- All four figures share ONE rstrip on purpose: the side-by-side rule in
     06-figures.css only fires when a strip holds two or more items. Split
     them into separate rstrips and they stack at 760px instead. -->
<!-- Combined from instruments/picture_lidar_01.jpeg +
     picture_SYA_tower_01.jpeg (matched heights, white gutter) by a small
     PIL one-liner, 2026-08-15 — Sebastian wanted the instruments back as
     one figure rather than two. -->
{{< rfig image="/media/research/SWEX/instruments/lidar_and_tower.jpeg" ratio="1019/559"
         alt="Two photographs side by side: a ceilometer and a scanning Doppler lidar deployed on a ridge above Santa Barbara with the Pacific Ocean behind, and an instrumented flux tower standing in a grassy field site." >}}
**SWEX instruments.** Scanning Doppler lidar and ceilometer on the ridge above
Santa Barbara (left), and a flux tower at the valley site (right).
{{< /rfig >}}
<!-- The terrain map is panel (a) of the same thesis figure as the scan
     sequence below it — the sequence's panels are labelled (b)–(f), so this
     map is what "(a)" refers to. If it is ever cut, the labels in
     Lidar_new.png need cropping out or the reference dangles. -->
{{< rfig image="/media/research/SWEX/Results/terrain_new.png" ratio="524/312"
         alt="Grayscale terrain map of the Santa Ynez valley with the SYA lidar site marked and a straight line through it showing the range–height scan track along azimuth 315 degrees, labelled as panel a." >}}
**RHI track, azimuth 315° through SYA.** The transect the scans below
sweep.
{{< /rfig >}}
{{< rfig image="/media/research/SWEX/Results/Lidar_new.png" ratio="874/820" width="640px"
         alt="Sequence of five range–height lidar scans along azimuth 315 degrees through the night of 21–22 April 2020, each showing a shallow yellow outflow layer near 400 metres over blue return flow." >}}
**Doppler-lidar RHI scans, night of 21–22 April.** Azimuth 315° through SYA:
a shallow downslope jet rides a few hundred metres above the lidar while the
opposing layer holds beneath it.
{{< /rfig >}}
{{< /rstrip >}}

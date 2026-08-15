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
     (removed deliberately — the platforms are what is BUILT, so
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
     PIL one-liner, 2026-08-15 — The author wanted the instruments back as
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

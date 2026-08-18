---
title: 'Research'
summary: >-
  Machine learning and remote sensing for weather and hydrologic forecasting:
  atmospheric rivers, flood forecasting, climate downscaling, and boundary-layer turbulence in complex terrain
date: 2026-08-16

# A standing page, not a post: the byline row would otherwise print a date
# and a reading time under the title.
show_date: false
reading_time: false

# The rendered "Research" title is suppressed (see custom-assets.html): the
# page opens on "Current Research" instead. The title itself stays for the
# nav, the browser tab, search and the sitemap.
hide_title: true
---

# Current Research

I am working on two research manuscripts: the first trains a convolutional neural network (CNN) to downscale CMIP6-based climate projections of extreme precipitation and temperature over Chile's complex topography. The second one stress-tests LSTM and difussion streamflow modeles against process-based benchmarks (GR4J, CemaNeige) during atmospheric-river flood events in US West Coast basins and evaluates their performance based on their hydrological regimes. 

## Atmospheric Rivers and Extreme Precipitation

On July 2026, a deep winter low brought extreme precipitation and floods to the Araucanía and Los Ríos regions in Southern Chile. I compared **ECMWF's AI model (AIFS)** against the physics-based **GFS** and **ECMWF-IFS** models, scored against rainfall gauges from Chile's weather service (DMC). The analysis was done while the event was live using forecast and observations pulled from my nowcasting web platform [Chile AR nowcast](/projects/chile-ar-nowcast/).  

{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-goes-500hpa.jpg" ratio="1300/1239" width="700px"
         alt="GOES-19 GeoColor satellite image of the southeast Pacific and Chile on 30 July 2026, showing a large comma-shaped cloud spiral centered southwest of the coast, with GFS 500 hPa geopotential height contours overlaid in yellow closing around the same center, and Santiago and Temuco marked." >}}
**GOES-19 GeoColor with GFS 500 hPa contours for 30 July 2026 13:20 Chile time**.
{{< /rfig >}}
{{< /rstrip >}}

To quickly evaluate how topography influences the models' skill, I selected four gauged locations along a topographic gradient: **Isla Mocha (offshore Island), Temuco (central valley), Pucón (Andean Foothills), and Lonquimay (high Andes)**.

When plotting accumulated precipitation forecasts for various lead times together with the observed precipitation at these locations we can observe errors of up to x3 in total precipitation in physics-based models at the **high Andean** site, as shown below: 

{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-model-leads.png"
         image_dark="/media/projects/chile-ar-model-leads-dark.png" ratio="1600/860" width="820px"
         alt="A map of four selected DMC stations over shaded terrain beside four panels of forecast rainfall against lead time from seven days out to one day out, each comparing GFS, ECMWF-IFS and AIFS against a dashed observed total." >}}
**Forecast rainfall by lead time, four DMC stations.** 
{{< /rfig >}}
{{< /rstrip >}}

{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-model-spatial.png"
         image_dark="/media/projects/chile-ar-model-spatial-dark.png" ratio="1600/739" width="820px"
         alt="Three side-by-side maps of forecast 48-hour precipitation over southern Chile for the same weekend window, from GFS, ECMWF-IFS and AIFS: GFS shows sharp banded maxima along the Andes reaching 179 millimetres, while the AIFS field is visibly smoother with a maximum of 121 millimetres." >}}
**48-hour weekend forecast precipitation for all models: GFS, ECMWF-IFS, AIFS.**
{{< /rfig >}}
{{< /rstrip >}}

For the **July 30** event, the AI forecast converged on the right answer, however, this happens once the initial conditions already carried the storm information. AI models are fast and improving quickly, but more research is required before conditioning alerts on them, particularly if their edge comes when the storm is already happening.

For the **48-hour** weekend forecast (unverified), The GFS model showed a sharp banded maxima along the Andes reaching 179 mm, while the AIFS was visibly smoother with a maximum of 121 mm. This smoothing has been frequently observed in the AI weather forecasting literature and may pose challenges for accurate precipitation forecasts in regions of complex terrain. 

## Flood Forecasting and Hydrodynamic Modeling {#streamflow-ar-floods}

Applying Long Short-Term Memory (LSTM) and diffusion algorithms to predict
flow discharges in US west coast basins, and stress testing them for flood
events during atmospheric river (AR) events. We are benchmarking the results
against process-based models (GR4J and CemaNeige) for basins associated
with various hydrological regimes. 

The regional LSTM beats the NWM v3.0 retrospective on skill, but its ensemble mean is the worst peak estimator during AR floods. Reading the ensemble at q75 overatakes both NWM and physics-based models. An abstract on this was submitted for the [AGU Fall Meeting 2026](/publications/agu2026-lstm-diffusion-ar-floods/), with a journal manuscript in preparation. 

{{< rstrip >}}

{{< rfig image="/media/research/caudal-lstm-nwm-abc.png"
         image_dark="/media/research/caudal-lstm-nwm-abc-dark.png" ratio="3063/2457" width="700px"
         alt="Three-panel comparison of a regional LSTM against the National Water Model over about 70 US west coast basins: scatters of whole-record NSE and NSE on atmospheric-river days, both with most basins above the 1:1 line favoring the LSTM, and a bar chart of median relative peak error on AR floods by method, where the LSTM ensemble mean is worst at 0.407 and the train-selected q75 LSTM is best at 0.221, ahead of the National Water Model's 0.253." >}}
**Regional LSTM against NWM v3.0 retrospective.** LSTM and diffusion model vs process-based benchmarks during AR days. 
{{< /rfig >}}

Below is my own implementation of the 2D Saint-Venant equations to simulate flow in the Russian River basin, CA, during an AR-driven flood event on February 2019. The simulation uses a rain-on-grid approach and an empirical infiltration module. I am interested in building ML-based emulators of hydrodynamic models of various levels of physical complexity with a focus on operational forecasting and scalability. 

{{< rfig video="/media/research/guerneville-flood.mp4" poster="/media/research/guerneville-flood-poster.jpg" ratio="900/1068" width="620px" autoplay="true"
         alt="Animated shallow-water simulation of the February 2019 Russian River flood near Guerneville, California: water depth spreading through the river corridor and onto the floodplain over a dark basemap with settlements labelled, each frame stamped with the date, simulation hour, inundated area and maximum depth, above a timeline of inundated area." >}}
**Russian River, February 2019.** My own shallow-water solver reconstructing the
atmospheric-river flood on a 16&nbsp;m grid, stamped with simulation hour,
inundated area and maximum depth. 
{{< /rfig >}}


{{< /rstrip >}}

## Downscaling of Climate Extremes

Collaborative research with 1 researcher from Chile and another researcher from the US. We are training a convolutional neural network to downscale CMIP6-based climate projections
of extreme precipitation and temperature in Chile. The CNN is able to
capture Chile's unique topography, and we are investigating the physical
mechanisms driving the changes. An abstract on this work was submitted to the
[AGU Fall Meeting 2026](/publications/agu2026-cmip6-downscaling-chile/),
with a journal manuscript in preparation. 

{{< rstrip >}}
{{< rfig image="/media/research/chile-cnn-downscaled.png"
         image_dark="/media/research/chile-cnn-downscaled-dark.png" ratio="2752/3694" width="600px"
         alt="Six maps of Chile at 0.05-degree resolution showing CNN-downscaled change from 1981–2010 to 2071–2100 under SSP5-8.5: the top row is the change in maximum one-day precipitation for NESM3, the 27-model ensemble mean, and HadGEM3-GC31-LL; the bottom row is the change in maximum temperature for INM-CM5-0, the 26-model ensemble mean, and UKESM1-0-LL, with fine Andean structure visible in every panel." >}}
**CNN-downscaled change at 0.05° (~5 km).** Rx1day (top) and TXx (bottom),
2071–2100 under SSP5-8.5 minus 1981–2010, with the ensemble mean flanked by the
models that bracket it. The native CMIP6 grids are ~1°.
{{< /rfig >}}
{{< /rstrip >}}

# Doctoral Research

## Boundary-Layer Turbulence in Complex Terrain

For my doctoral work, I participated in two major field campaigns: the Wind Forecast Improvement Project 2
(WFIP2) in the Columbia River Gorge (OR) and the Sundowner Wind Experiment
(SWEX) in Santa Barbara (CA), where I deployed, operated, and processed data from flux towers and scanning lidars to investigate turbulent flows and boundary-layer processes over complex terrain.  

The main outcome from my PhD was a first-author publication evaluating the skill of a turbulent boundary-layer parametetrization widely used in the Weather Research and Forecasting (WRF) model, and quantifying the variability of turbulent fluxes under different stratification regimes in complex terrain. This work used data collected during the WFIP2 experiment and was published in [*Boundary-Layer Meteorology*](/publications/2023-blm-subgrid-variability/).

My thesis also included a detailed analysis of internal gravity wave breaking during Sundowner winds in Santa Barbara (CA) using custom scanning sequences with synchronized Doppler Lidars. Alongside this, I contributed to collaborative work on energy balance closure, boundary-layer parameterizations, and wind energy forecasting in complex terrain. 

{{< rstrip >}}
{{< rfig image="/media/research/wfip2/terrain_real_vs_nwp.png" ratio="1124/505" width="820px"
         alt="Two panels at equal height: on the left, real high-resolution terrain of the WFIP2 study area with a dozen tower positions labelled P1 to P12 inside a white circle and a 12 kilometre scale bar; on the right, the same area as the weather model's grid, a handful of smooth coloured cells with the tower array circled and Wasco marked." >}}
**WFIP2 tower array, Columbia River Gorge.** High-resolution terrain and instrumented flux towers (left) and the same terrain represented on a Numerical Weather Prediction (NWP) model's grid (right). The turbulence variability and their parametrization inside the white circle is what my doctoral work tackled. 

{{< /rfig >}}
{{< /rstrip >}}

{{< rstrip >}}
{{< rfig image="/media/research/SWEX/instruments/tower_and_lidar.jpg" ratio="954/517" width="820px"
         alt="Two photographs at equal height: on the left, an instrumented flux tower with a sonic anemometer at the top, in a grassy field at the SYA valley site with hills behind; on the right, a ceilometer and a scanning Doppler lidar on a ridge above Santa Barbara, dry grass in the foreground and the Pacific Ocean beyond the hills." >}}
**SWEX instruments.** Flux tower with sonic anemometer at the SYA valley
(left), and scanning Doppler lidar and ceilometer on a ridge in the Santa Ynez Mountain facing the Santa Barbara coastline (right).
{{< /rfig >}}
{{< /rstrip >}}

<!-- The 3D scan first, then the terrain map: the scan shows how the lidar
     sampled the volume, the map shows where the 315° cut runs across the
     valley, which is what makes "downslope" legible in the sequence below. -->
{{< rstrip >}}
{{< rfig image="/media/research/SWEX/Results/lidar_scan_a.jpeg" ratio="617/575" width="600px"
         alt="Three-dimensional view of two intersecting Doppler-lidar range–height scan planes above the SYA site on 21 April 2020 at 17:15, radial velocity shaded from blue toward the lidar to yellow away." >}}
**Coplanar RHI scans, 21 April 2020.** Two vertical scan planes through
SYA, radial velocity toward the lidar in blue and away in yellow. The 315°
plane is the one the sequence below follows through the night.
{{< /rfig >}}
{{< rfig image="/media/research/SWEX/Results/waves_lidar_01.jpeg" ratio="1168/1518" width="660px"
         alt="Six-panel figure: panel a is a grayscale terrain map of the Santa Ynez valley with the SYA lidar site marked and the azimuth 315 degree scan track drawn across it; panels b to f are range-height lidar scans along that track through the night of 21 to 22 April 2020, each showing a shallow yellow outflow layer near 400 metres over blue return flow." >}}
**RHI scans, night of 21–22 April.** (a) Azimuth-315° transect through SYA, crossing the valley floor and up the ridge. (b–f) Scans along this transect show a shallow downslope jet a few hundred metres above the lidar, with an opposing flow layer beneath it. Gravity wave development and breaking are visible overnight, ahead of Sundowner wind onset.
{{< /rfig >}}
{{< /rstrip >}}

---
title: "Chile Atmospheric River Nowcast"
date: 2026-04-01
summary: "A live nowcast of landfalling atmospheric rivers along the Chilean coast: real-time GEFS ensemble integrated vapor transport with Ralph et al. AR-scale categorization, and a DGA/DMC observation ingestion pipeline."
tags:
  - Weather Extremes
  - Atmospheric Rivers
  - Ensemble Forecasting
  - Dash / Plotly

# The cover is for the collection card only. Rendered in the body too, it
# repeats a figure that appears in full below, and pushes the app button
# under the fold.
image:
  preview_only: true

# The byline row would otherwise print a date and a reading time above an
# application. Both are noise here; the run status in the body is the date
# that matters.
show_date: false
reading_time: false
---


{{< applinks app="https://chile-ar-nowcast.onrender.com/" >}}

A live nowcast of landfalling atmospheric rivers along the Chilean coast.
Real-time GEFS ensemble forecasts of integrated vapor transport (IVT) are
categorized on the [Ralph et al. (2019)](https://doi.org/10.1175/BAMS-D-18-0023.1)
AR scale, which combines IVT magnitude with duration at landfall. Duration
separates an AR that supplies a season's water from one that floods. Operated publicly through a **Category 4 landfalling AR
event** in July 2026.

<!--more-->

## Forecast: ensemble IVT and AR category

The forecast side ingests GEFS at each cycle and computes vertically
integrated vapor transport across the domain, then scores the landfalling
signal on the AR scale. Precipitation is carried as both the deterministic GFS
run and the GEFS ensemble, so the cumulative curve carries its spread.

{{< rstrip >}}
{{< rfig video="/media/projects/chile-ar-app-tour.mp4" poster="/media/projects/chile-ar-app-tour-poster.jpg" ratio="1280/720" width="820px"
         alt="Screen recording touring the nowcast: a table of Chilean sites with AR category and confidence per site, then a synoptic map of integrated vapor transport over the southeast Pacific with a time slider and flow animation, then the same window zoomed to coastal rainfall." >}}
**Forecast view.** Per-site AR category and confidence, the synoptic
integrated vapor transport field, and the same window zoomed to coastal
rainfall. Both maps share one time slider.
{{< /rfig >}}
{{< /rstrip >}}

{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-santiago-ensemble.png" ratio="862/355" width="680px"
         alt="Forecast panel for Santiago showing hourly GFS rainfall as bars against two cumulative precipitation curves, GFS deterministic and GEFS ensemble mean, with a shaded plus-or-minus one standard deviation ensemble spread band widening across the four-day window." >}}
**Santiago rainfall forecast, GFS and GEFS.** Hourly GFS rainfall (bars) under
the two cumulative curves, with the ±1σ ensemble band. Most of the total falls
inside a 36-hour window.
{{< /rfig >}}
{{< /rstrip >}}

## Observations: DGA and DMC station ingestion

A parallel pipeline ingests Chile's observational networks on a rolling
snapshot, so the forecast can be checked against what the ground recorded:
Dirección General de Aguas (DGA) hydrometric stations and Dirección
Meteorológica de Chile (DMC) weather stations. Station markers carry DGA's own
three-tier alert state (Azul, Amarilla, Roja): station-specific thresholds DGA
sets on the parameter each station monitors, so the color reports the alert the
agency declared, not an anomaly computed here.

{{< rstrip >}}
{{< rfig video="/media/projects/chile-ar-dga-network.mp4" poster="/media/projects/chile-ar-dga-network-poster.jpg" ratio="1280/720" width="820px"
         alt="Screen recording of the nowcast's observation view: a map of central Chile with DGA and DMC station markers, a station tooltip showing temperature, 72-hour accumulated precipitation and wind, the alert-tier legend, and a selected-station rainfall panel updating below the map." >}}
**Observation layer.** Station markers filtered by precipitation window.
Hovering reports temperature, accumulated rainfall and wind at the snapshot
time; selecting a station loads its full record below the map.
{{< /rfig >}}
{{< /rstrip >}}

## Event analysis: physics against AI, 30 July 2026

A second use for a platform that is already ingesting forecasts and
observations: verification, run live while an event is in progress. On 31 July
2026, with a deep winter low soaking Araucanía and Los Ríos, I compared
**ECMWF's AI model (AIFS)** against the physics-based **GFS** and **ECMWF-IFS**,
scored against Chile's weather service (DMC) gauges.


{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-goes-500hpa.jpg" ratio="1300/1239" width="700px"
         alt="GOES-19 GeoColor satellite image of the southeast Pacific and Chile on 31 July 2026, showing a large comma-shaped cloud spiral centered southwest of the coast, with GFS 500 hPa geopotential height contours overlaid in yellow closing around the same center, and Santiago and Temuco marked." >}}
**GOES-19 GeoColor, 31 July 2026 13:20 Chile time,** with GFS 500 hPa
geopotential height. The contours close around the same center as the cloud
spiral, so the analysis has the storm where the satellite does.
{{< /rfig >}}
{{< /rstrip >}}

The verification is by lead time, at four stations along a terrain gradient:
an offshore island, the central valley, the Andes foothills, and a high-Andes
site.

{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-model-leads.png" ratio="1600/860" width="820px"
         alt="A map of four selected DMC stations over shaded terrain beside four panels of forecast rainfall against lead time from seven days out to one day out, each comparing GFS, ECMWF-IFS and AIFS against a dashed observed total: Isla Mocha 43 mm, Temuco 57 mm, Pucon 77 mm, and Lonquimay 36 mm, where GFS peaks near 115 mm two days out." >}}
**Forecast rainfall by lead time, four DMC stations.** At Lonquimay in the high
Andes, the physics models called up to three times the observed 36 mm and swung
hard from cycle to cycle, while AIFS stayed closer. Offshore and in the valley
the three converge. Skill varied more with terrain than between models.
{{< /rfig >}}
{{< /rstrip >}}

{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-model-spatial.png" ratio="1600/739" width="820px"
         alt="Three side-by-side maps of forecast 48-hour precipitation over southern Chile for the same weekend window, from GFS, ECMWF-IFS and AIFS: GFS shows sharp banded maxima along the Andes reaching 179 millimetres, while the AIFS field is visibly smoother with a maximum of 121 millimetres." >}}
**48-hour forecast precipitation: GFS, ECMWF-IFS, AIFS.** The AI field is
smoother, a documented consequence of its training objective, and in the Andes
it softens the orographic banding GFS produces.
{{< /rfig >}}
{{< /rstrip >}}

The AI forecast converged on the right answer mainly once the event was inside
the window where the initial conditions already carry the storm. AI models are
fast, cheap and improving quickly, but an edge that appears only that late
matters for anyone considering conditioning alerts on them, and argues for more
local, event-by-event verification.

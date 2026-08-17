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

In July 2026, global weather models showed that a Category 4 Atmospheric River (AR) had developed in the Eastern Pacific off the coast of Chile, with the potential for bringing record-breaking rainfall and floods to various coastal cities. 

To track this event, I built a storm tracker application with real-time data ingestion, post processing, and visualization pipelines for various operational global weather models and Chile's weather service' (DMC) official weather stations. 

<!--more-->

## Forecast: ensemble IVT and AR category

The forecast side ingests GEFS at each cycle and computes vertically
integrated water vapor transport across the domain, then scores the landfalling
signal on the AR scale. Precipitation is carried as both the deterministic GFS
run and the GEFS ensemble. 

{{< rstrip >}}
{{< rfig video="/media/projects/chile-ar-app-tour.mp4" poster="/media/projects/chile-ar-app-tour-poster.jpg" ratio="1280/720" width="820px"
         alt="Screen recording touring the nowcast: a table of Chilean sites with AR category and confidence per site, then a synoptic map of integrated vapor transport over the southeast Pacific with a time slider and flow animation, then the same window zoomed to coastal rainfall." >}}
**Forecast view.** Per-site AR category. The animation shows the synoptic scale
integrated vapor transport field, and the same window zoomed to coastal
rainfall. 
{{< /rfig >}}
{{< /rstrip >}}

Rainfall intensity (mm/h), accumulated rainfall (mm), wind gust, and temperature time series are calculated from global models (GFS, GEFS, ECMWF-IFS and ECMWF-AIFS) and can be visualized for selected cities in Chile. These graphs are updated automatically as new forecasts become available. 
{{< rstrip >}}
{{< rfig image="/media/projects/chile-ar-santiago-ensemble.png" ratio="862/355" width="680px"
         alt="Forecast panel for Santiago showing hourly GFS rainfall as bars against two cumulative precipitation curves, GFS deterministic and GEFS ensemble mean, with a shaded plus-or-minus one standard deviation ensemble spread band widening across the four-day window." >}}
**Santiago rainfall forecast, GFS and GEFS.** Hourly GFS rainfall (bars) under
the two cumulative curves, with the ±1σ ensemble band. Most of the total falls
inside a 36-hour window.
{{< /rfig >}}
{{< /rstrip >}}

## Real-time Observations: DGA and DMC

To provide real-time national coverage of the event and a means for verifying the forecasts, I developed a separate data and visualization pipeline that incorporates meteorological observations from Chile's weather service (DMC), as well as official hydrological flood alerts from Chile's water directorate (DGA):

{{< rstrip >}}
{{< rfig video="/media/projects/chile-ar-dga-network.mp4" poster="/media/projects/chile-ar-dga-network-poster.jpg" ratio="1280/720" width="820px"
         alt="Screen recording of the nowcast's observation view: a map of central Chile with DGA and DMC station markers, a station tooltip showing temperature, 72-hour accumulated precipitation and wind, the alert-tier legend, and a selected-station rainfall panel updating below the map." >}}
**Observation layer.** Station markers filtered by precipitation window.
Hovering reports temperature, accumulated rainfall and wind at the snapshot
time; selecting a station loads its full record below the map.
{{< /rfig >}}
{{< /rstrip >}}

## Future Work

This project is not an official tool and it was done independently. I am working on redesigning te application to make it more acessible to a general audience and open sourcing the code to accelerate development and awareness of the tool.  





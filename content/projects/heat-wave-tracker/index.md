---
title: "US Heat Wave Tracker"
date: 2026-07-01
summary: "A live CONUS heat-wave dashboard: GFS forecasts with same-day bias correction against ASOS observations, NWS heat-index risk levels, GEV rarity analysis, and a running forecast-skill scorecard across 165 US cities."
tags:
  - Weather Extremes
  - Bias Correction
  - Extreme Value Statistics
  - Dash / Plotly
  - NOAA GFS

# The cover is for the collection card only. Rendered in the body too, it
# repeats a figure that appears in full below, and pushes the app button
# under the fold.
image:
  preview_only: true

show_date: false
reading_time: false
---


{{< applinks app="https://heat-wave-tracker.onrender.com/" code="https://github.com/sotarolab/heat-wave-tracker" >}}

A live dashboard tracking CONUS heat waves. The application ingests GFS, National Blend of Models (NBM), and NOAA's ASOS network observations for 165 US cities. The user can visualize synoptic conditions for selected dates and times, as well as heat index, risk, and bias-corrected temperature forecasts for any of the cities included.

<!--more-->

## Synoptic Maps

The synoptic view: forecast fields over the continental United States,
animated across the forecast window. Heat index is classed into the five NWS
risk categories, and the underlying temperature, dewpoint and wind fields can
be stepped through for any date and time in the window.

{{< rstrip >}}
{{< rfig video="/media/projects/heatwave-hi-risk.mp4" poster="/media/projects/heatwave-hi-risk-poster.jpg" ratio="1280/720" width="820px"
         alt="Animated map of the continental United States over three days of the July 2026 heat wave, each frame shading the forecast heat index into the five NWS risk categories." >}}
**NWS heat-index risk, 16 to 18 July 2026.** Animated map of the continental United States over three days of the July 2026 heat wave, each frame shading the forecast heat index into the five NWS risk categories.
{{< /rfig >}}
{{< rfig image="/media/projects/heatwave-conus-forecast.png" ratio="1295/590" width="820px"
         alt="Forecast 2-metre temperature over the continental United States for 15 August 2026 at 4 PM Eastern, shaded from blue near 50 degrees Fahrenheit over the Rockies to deep red above 100 across the southern Plains and lower Mississippi valley, with major cities labelled." >}}
**2 m temperature, 15 August 2026 4 PM EDT.** The underlying field the risk
categories are built from, at one forecast hour: red is above 100 °F across the
southern Plains, blue is near 50 °F at elevation in the Rockies.
{{< /rfig >}}
{{< /rstrip >}}

## Forecast Verification

The National Blend of Models (NBM) has a data assimilation layer, however, it's still frequently subject to biases in daily temperature forecasts. To strengthen the predictions, I included: 

- **Same-day bias correction.** The raw forecast is corrected against that
  station's own ASOS observations from earlier the same day, and carries a
  genuine 95% prediction interval.
- **Live verification.** Running metrics including bias, RMSE and a Brier score,
  comparing the day's forecast against ASOS observations, and updated as new observations arrive. 
- **Historical rarity.** Each station's forecast is placed against a 54-year
  temperature record for that specific city via a Generalized Extreme Value
  fit, which answers how unusual the value is at that particular city.

{{< rstrip >}}
{{< rfig image="/media/projects/heatwave-kdca-station.png" ratio="1400/700" width="820px"
         alt="Station panel for KDCA, Reagan National Airport: an upper chart of bias-corrected Feels Like temperature as a continuous line with observed values as points, a dashed 90 degree Extreme Caution threshold and a vertical Now marker separating past from forecast; a lower chart of bias-corrected and observed air temperature against dewpoint over the same period." >}}
**KDCA, Reagan National.** Bias-corrected feels-like and actual temperature (line) against ASOS observations (dots).
{{< /rfig >}}
{{< /rstrip >}}

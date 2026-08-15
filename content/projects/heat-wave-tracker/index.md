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

A live dashboard tracking CONUS heat waves: GFS forecast temperature and heat
index over 165 US cities, animated across the forecast window, with real
observations pulled from NOAA's ASOS network on click and a "Hottest Cities
Right Now" leaderboard. Auto-updates every six hours as new GFS cycles land.

<!--more-->

{{< rstrip >}}
{{< rfig video="/media/projects/heatwave-hi-risk.mp4" poster="/media/projects/heatwave-hi-risk-poster.jpg" ratio="1280/720" width="820px"
         alt="Animated map of the continental United States over three days of the July 2026 heat wave, each frame shading the forecast heat index into the five NWS risk categories, with the orange Extreme Caution area expanding across the Plains and Southeast each afternoon and contracting overnight, and small Danger patches appearing in the desert Southwest and the mid-Atlantic." >}}
**NWS heat-index risk, 16 to 18 July 2026.** The field the dashboard animates,
in the five NWS categories, so the color breaks fall where the guidance
changes. Peak heat index 113 °F. Rendered from the
tracker's cached GFS window; the live app shows the current one.
{{< /rfig >}}
{{< /rstrip >}}

## Beyond the raw forecast

A plain GFS trace at a city is a starting point, not an answer. Each station
panel adds three things on top of it:

- **Same-day bias correction.** The raw forecast is corrected against that
  station's own ASOS observations from earlier the same day, and carries a
  genuine 95% prediction interval. It widens when only a handful of
  observations are in, and covers the near-term forecast only.
- **Live verification.** A running scorecard of bias, RMSE and a Brier score,
  comparing the day's forecast against what actually happened, updating as
  observations arrive.
- **Historical rarity.** Each station's forecast is placed against a 54-year
  temperature record for that specific city via a Generalized Extreme Value
  fit, which answers how unusual the value is at that particular city.

{{< rstrip >}}
{{< rfig image="/media/projects/heatwave-kdca-station.png" ratio="1400/700" width="820px"
         alt="Station panel for KDCA, Reagan National Airport: an upper chart of bias-corrected Feels Like temperature as a continuous line with observed values as points, a dashed 90 degree Extreme Caution threshold and a vertical Now marker separating past from forecast; a lower chart of bias-corrected and observed air temperature against dewpoint over the same period." >}}
**KDCA, Reagan National.** Bias-corrected feels-like temperature (line)
against the ASOS observations it was corrected with (points), split by the
*Now* marker, with the 90 °F Extreme Caution threshold dashed across. Below,
temperature against dewpoint: the gap is the humidity contribution.
{{< /rfig >}}
{{< /rstrip >}}

## Heat index and risk categories

The dashboard reports heat index, the NWS formula combining temperature and
relative humidity, alongside air temperature, and classifies it into the NWS
risk categories (No Elevated Risk through Extreme Danger). Human heat stress
tracks the combination, not temperature alone, and the categories are the
National Weather Service's own thresholds.

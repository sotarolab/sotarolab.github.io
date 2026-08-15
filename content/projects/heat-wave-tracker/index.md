---
title: "US Heat Wave Tracker"
date: 2026-07-01
summary: "A live dashboard tracking CONUS heat waves — GFS forecasts, NWS heat-index risk levels, and real-time ASOS observations across 165 US cities."
links:
  - type: site
    url: https://heat-wave-tracker.onrender.com/
  - type: code
    url: https://github.com/sotarolab/heat-wave-tracker
tags:
  - Weather Extremes
  - Dash / Plotly
  - NOAA GFS
---

A live dashboard tracking CONUS heat waves: GFS forecast temperature and Heat Index over 165 US cities, NWS risk-level classification, and real-time observations pulled from NOAA's ASOS network on click, with a "Hottest Cities Right Now" leaderboard.

Built with Python and Dash/Plotly, using [Herbie](https://github.com/blaylockbk/Herbie) to fetch NOAA GFS forecasts and the Iowa Environmental Mesonet ASOS network for observations.

<!--more-->

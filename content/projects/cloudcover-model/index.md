---
title: "GOES-16 Sky Cover Reconstruction"
date: 2026-03-01
summary: "Reconstructing hourly ASOS sky-cover categories from GOES-16 geostationary satellite data, from a rule-based baseline through Deep Kernel Learning with calibrated uncertainty."
tags:
  - Machine Learning
  - Satellite Remote Sensing
  - Uncertainty Quantification
---

Surface weather stations (ASOS) report sky cover from a ceilometer measuring fractional cloud coverage from below; GOES-16 observes cloud properties from above at ~2 km resolution. This project learns the mapping between GOES retrievals and ASOS sky-cover categories, enabling satellite-based reconstruction of surface observations where ground truth is unavailable — progressing from a rule-based baseline to Deep Kernel Learning with calibrated uncertainty.

Case study station: KDSM (Des Moines International Airport, Iowa), trained on 2018–2023 and tested out-of-sample on 2024.

<!--more-->

*Code repository not yet public.*

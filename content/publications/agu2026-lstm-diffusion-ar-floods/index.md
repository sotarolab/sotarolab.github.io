---
# ⚠️ GENERATED FILE — DO NOT EDIT.
# Source: data/publications.yaml   Regenerate: make publications
# Edits here are silently reverted the next time the generator runs.
title: "LSTM and diffusion models compared with process-based and operational benchmarks during atmospheric-river floods in US West Coast basins"

authors:
  - Sebastian F. Otarola-Bustos
  - C. Buahin

date: 2026-12-01
publishDate: 2026-08-09

publication_types:
  - paper-conference

publication:
  name: "AGU Fall Meeting 2026 — Session H039 (abstract submitted)"
  short_name: "AGU Fall Meeting 2026 (abstract submitted)"

abstract: |
  Atmospheric rivers (ARs) produce most of the floods in US West Coast basins
  and deliver roughly 30–50% of the region's annual precipitation, so the same
  storms that drive floods influence seasonal water supplies. Machine-learning
  streamflow models routinely outperform process-based models on whole-record
  Nash–Sutcliffe Efficiency (NSE). This study asks how an LSTM network and a
  conditional diffusion model compare with process-based and operational models
  during flood events triggered by AR landfall.

  We evaluate the LSTM and the diffusion model against a calibrated conceptual
  model (GR4J+CemaNeige) and the National Water Model (NWM) on 71 CAMELS-US
  West Coast basins (50 rain-dominated, 14 snow-influenced, 7 semi-arid),
  trained or calibrated on 1980–2004 and evaluated on 2005–2014. The LSTM leads
  on whole-record NSE with a median of 0.78 against 0.75 for GR4J+CemaNeige and
  0.61 for the NWM.

  Applying a per-basin peak-over-threshold criterion on AR landfall days from
  the CW3E AR catalog identifies 358 flood events. NSE favors the LSTM on the
  whole record and on AR flood days alike — but the ranking reverses when
  methods are scored by median absolute relative error in flood peaks: 0.25 for
  the NWM, 0.33 for GR4J+CemaNeige, against 0.41 for the LSTM ensemble mean,
  which falls below the observed peak in most flood events.

  The deficit lies in the summary statistic rather than the network. Reading
  the same LSTM ensemble at an upper quantile selected on the training period
  drops peak error to 0.22 with no retraining: the flood information is present
  in the predictive distribution and is discarded by the mean. The diffusion
  model, which samples its predictive distribution rather than summarizing it,
  reaches 0.27 on AR flood peaks — improving on the LSTM ensemble mean without
  overtaking the NWM — and attains a whole-record NSE of 0.79. Since 87% of
  flood events on rain-dominated basins are AR-driven, peak-magnitude
  comparison may be important to include when models are evaluated for
  flood-relevant applications.

summary: "Machine-learning streamflow models win on whole-record NSE but lose on AR flood peaks — and the deficit is in the ensemble mean, not the network: reading the same LSTM at an upper quantile cuts peak error from 0.41 to 0.22."

tags:
  - Machine Learning
  - Atmospheric Rivers
  - Hydrology
  - Streamflow Forecasting

featured: true
---

Status: **abstract submitted to AGU Fall Meeting 2026 (Session H039); manuscript in preparation.**

<!-- TODO once the session is confirmed: replace the status line above with the
     accepted presentation details, and attach the poster/slides via `url_poster`
     or `url_slides` in the front matter. -->

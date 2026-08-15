---
draft: true  # unpublished 2026-08-15: not ready to show (see content/teaching/_index.md)
title: "Machine Learning for Weather Extremes"
summary: "A one-semester course proposal covering extreme value statistics, ML bias correction, satellite-based reconstruction and climate attribution, taught by lecture with weekly coding assignments. Open to offer as a part-time / adjunct course."
date: 2026-07-08
tags:
  - Course
---

<style>
  /* the theme auto-renders an <h1> from front matter title; this page supplies its own */
  article.prose > h1:first-child { display: none; }

  .mlwx-course {
    --paper: #eef0ec;
    --surface: #e2e6dd;
    --surface-line: #cfd5c6;
    --ink: #1b2320;
    --ink-soft: #55635c;
    --ink-faint: #7c887f;
    --line: #c7cec0;
    --accent: #a8431b;
    --accent-soft: #c9723f;
    --accent-ink: #fbf3ee;
    --blue: #2e4c63;
    --blue-soft: #567089;

    --font-display: 'Iowan Old Style', 'Palatino Linotype', Palatino, 'URW Palladio L', Georgia, serif;
    --font-body: 'Iowan Old Style', Palatino, 'Palatino Linotype', Georgia, 'Times New Roman', serif;
    --font-mono: ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;

    background: var(--paper);
    color: var(--ink);
    font-family: var(--font-body);
    display: flex;
    justify-content: center;
    padding: clamp(1.5rem, 5vw, 3.5rem) 0;
    margin: 1.5rem -1px;
  }
  @media (prefers-color-scheme: dark) {
    .mlwx-course {
      --paper: #12181a;
      --surface: #1a2224;
      --surface-line: #2a3335;
      --ink: #e7eae4;
      --ink-soft: #9daaa2;
      --ink-faint: #71807a;
      --line: #2c3735;
      --accent: #e07a49;
      --accent-soft: #a85c34;
      --accent-ink: #16110d;
      --blue: #7fa0b8;
      --blue-soft: #5c7d97;
    }
  }
  html.dark .mlwx-course {
    --paper: #12181a;
    --surface: #1a2224;
    --surface-line: #2a3335;
    --ink: #e7eae4;
    --ink-soft: #9daaa2;
    --ink-faint: #71807a;
    --line: #2c3735;
    --accent: #e07a49;
    --accent-soft: #a85c34;
    --accent-ink: #16110d;
    --blue: #7fa0b8;
    --blue-soft: #5c7d97;
  }

  .mlwx-course, .mlwx-course * { box-sizing: border-box; }
  .mlwx-course a { color: var(--blue); text-decoration-color: var(--surface-line); text-underline-offset: 3px; }
  .mlwx-course a:hover { color: var(--accent); }
  .mlwx-course a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

  .mlwx-course .sheet { width: 100%; max-width: 43rem; padding: 0 1.25rem; }

  .mlwx-course .eyebrow {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 0 0 0.9rem;
  }

  .mlwx-course h1 {
    font-family: var(--font-display);
    font-weight: 600;
    font-size: clamp(1.7rem, 4vw, 2.35rem);
    line-height: 1.15;
    margin: 0 0 0.6rem;
    text-wrap: balance;
    letter-spacing: -0.01em;
  }

  .mlwx-course .tagline {
    font-size: 1.05rem;
    color: var(--ink-soft);
    margin: 0 0 2rem;
    max-width: 42ch;
    text-wrap: balance;
  }

  .mlwx-course .meta-strip {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 0.85rem 0;
    margin-bottom: 2.75rem;
  }
  .mlwx-course .meta-strip dl { margin: 0; padding: 0 0.9rem; border-left: 1px solid var(--line); }
  .mlwx-course .meta-strip div:first-child dl { border-left: none; padding-left: 0; }
  .mlwx-course .meta-strip dt {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin-bottom: 0.3rem;
  }
  .mlwx-course .meta-strip dd { margin: 0; font-size: 0.86rem; line-height: 1.35; color: var(--ink); }

  .mlwx-course section { margin-bottom: 2.85rem; }
  .mlwx-course section > h2 {
    font-family: var(--font-display);
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0 0 1rem;
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
  }
  .mlwx-course section > h2::before {
    content: '';
    width: 0.6rem;
    height: 0.6rem;
    background: var(--accent);
    display: inline-block;
    transform: translateY(-0.05rem);
  }

  .mlwx-course p { line-height: 1.65; font-size: 0.98rem; max-width: 62ch; margin: 0 0 0.9rem; }
  .mlwx-course p:last-child { margin-bottom: 0; }

  .mlwx-course ul.plain { list-style: none; margin: 0; padding: 0; display: grid; gap: 0.65rem; }
  .mlwx-course ul.plain li { position: relative; padding-left: 1.15rem; line-height: 1.55; font-size: 0.96rem; max-width: 60ch; }
  .mlwx-course ul.plain li::before {
    content: '';
    position: absolute;
    left: 0; top: 0.5em;
    width: 5px; height: 5px;
    background: var(--blue-soft);
  }

  .mlwx-course .schedule { width: 100%; overflow-x: auto; }
  .mlwx-course table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
  .mlwx-course thead th {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: var(--ink-faint);
    text-align: left;
    font-weight: 500;
    padding: 0 0.6rem 0.5rem;
    border-bottom: 1px solid var(--line);
    white-space: nowrap;
  }
  .mlwx-course tbody td { padding: 0.55rem 0.6rem; border-bottom: 1px solid var(--line); vertical-align: top; }
  .mlwx-course tbody tr:last-child td { border-bottom: 1px solid var(--ink-faint); }
  .mlwx-course td.wk { font-family: var(--font-mono); font-variant-numeric: tabular-nums; color: var(--ink-faint); width: 2rem; }
  .mlwx-course td.mod { width: 1.6rem; }
  .mlwx-course .mod-tag {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    color: var(--paper);
    background: var(--blue);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 1.3rem;
    height: 1.3rem;
  }
  .mlwx-course td.topic strong { font-weight: 600; }
  .mlwx-course td.topic span { color: var(--ink-soft); font-size: 0.85rem; }
  .mlwx-course tr.module-start td { padding-top: 1rem; }

  .mlwx-course .module-key {
    display: flex;
    flex-wrap: wrap;
    gap: 1.1rem;
    margin-top: 1rem;
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--ink-soft);
  }
  .mlwx-course .module-key span { display: inline-flex; align-items: center; gap: 0.4rem; }

  .mlwx-course .assess-bar { display: flex; width: 100%; height: 1.9rem; overflow: hidden; border: 1px solid var(--line); }
  .mlwx-course .assess-bar div { display: flex; align-items: center; justify-content: center; font-family: var(--font-mono); font-size: 0.68rem; color: var(--accent-ink); }
  .mlwx-course .assess-legend { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem 1.5rem; margin-top: 1.1rem; font-size: 0.88rem; }
  .mlwx-course .assess-legend li { list-style: none; display: flex; justify-content: space-between; gap: 1rem; border-bottom: 1px dotted var(--line); padding-bottom: 0.35rem; }
  .mlwx-course .assess-legend b { font-variant-numeric: tabular-nums; font-family: var(--font-mono); font-weight: 500; color: var(--ink-soft); }

  .mlwx-course .callout { background: var(--surface); border: 1px solid var(--surface-line); padding: 1.1rem 1.25rem; }
  .mlwx-course .callout p { max-width: none; }

  .mlwx-course footer {
    border-top: 1px solid var(--line);
    padding-top: 1.5rem;
    font-size: 0.85rem;
    color: var(--ink-soft);
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  .mlwx-course footer .fmono { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.04em; }

  @media (max-width: 560px) {
    .mlwx-course .meta-strip { grid-template-columns: repeat(2, 1fr); row-gap: 0.9rem; }
    .mlwx-course .meta-strip dl { border-left: none; padding-left: 0; }
    .mlwx-course .assess-legend { grid-template-columns: 1fr; }
  }
</style>

<div class="mlwx-course">
<div class="sheet">

<p class="eyebrow">Course Proposal</p>
<h1>Machine Learning for Weather Extremes</h1>
<p class="tagline">Forecasting, bias correction, and attribution — key concepts taught by lecture, with ML techniques and code practiced through weekly assignments.</p>

<div class="meta-strip">
  <div><dl><dt>Term</dt><dd>1 semester (15 wks)</dd></dl></div>
  <div><dl><dt>Credits</dt><dd>3</dd></dl></div>
  <div><dl><dt>Format</dt><dd>Lecture + lab, hybrid-feasible</dd></dl></div>
  <div><dl><dt>Level</dt><dd>Upper-div / intro grad</dd></dl></div>
  <div><dl><dt>Prereqs</dt><dd>Python, 1 semester stats</dd></dl></div>
</div>

<section>
<h2>Why this course</h2>
<p>Most atmospheric science curricula are strong on dynamics and thin on the applied ML that national labs, operational forecasting centers, and climate-tech employers now expect. Each week pairs a concept lecture — extreme value statistics, bias correction, satellite-based ML — with a short coding assignment that applies it to real station, reanalysis, or satellite data, rather than a toy dataset.</p>
<p>It's designed to cross-list cleanly across Atmospheric &amp; Environmental Science, Data Science, Statistics, and Computer Science, which widens the enrollment pool for a part-time or adjunct offering — and is well suited to institutions near federal atmospheric research campuses (e.g. NOAA, NASA Goddard), given the applied, operational-data focus.</p>
</section>

<section>
<h2>Learning outcomes</h2>
<ul class="plain">
  <li>Fit and interpret extreme value distributions (GEV, stationary and non-stationary) and apply a climate attribution protocol to a real event.</li>
  <li>Build and evaluate ML models for forecast post-processing and probabilistic bias correction against operational NWP output.</li>
  <li>Reconstruct a geophysical variable from satellite retrievals using deep learning with calibrated, not just point, predictions.</li>
  <li>Implement each technique in short, self-contained coding assignments — GEV fits, bias-correction routines, a small CNN — graded against reference outputs.</li>
  <li>Communicate probabilistic, decision-relevant results to a non-specialist audience.</li>
</ul>
</section>

<section>
<h2>Semester schedule</h2>
<div class="schedule">
<table>
<thead>
  <tr><th>Wk</th><th></th><th>Topic</th></tr>
</thead>
<tbody>
  <tr class="module-start"><td class="wk">01</td><td class="mod"><span class="mod-tag">A</span></td><td class="topic"><strong>Why extremes matter</strong><br><span>Lecture: hazard framing, impacts, the case for a statistical treatment of weather</span></td></tr>
  <tr><td class="wk">02</td><td class="mod"><span class="mod-tag">A</span></td><td class="topic"><strong>Extreme value theory I</strong><br><span>Lecture: block maxima, the GEV distribution, return periods · Assignment: fit a GEV to a station record</span></td></tr>
  <tr><td class="wk">03</td><td class="mod"><span class="mod-tag">A</span></td><td class="topic"><strong>Extreme value theory II</strong><br><span>Lecture: non-stationary GEV, trend detection, MLE and bootstrap · Assignment: bootstrap a confidence interval on a return level</span></td></tr>
  <tr><td class="wk">04</td><td class="mod"><span class="mod-tag">A</span></td><td class="topic"><strong>Climate attribution</strong><br><span>Lecture: the World Weather Attribution protocol · Assignment: compute a probability ratio for a real event</span></td></tr>

  <tr class="module-start"><td class="wk">05</td><td class="mod"><span class="mod-tag">B</span></td><td class="topic"><strong>Working with NWP &amp; reanalysis</strong><br><span>Lecture: GFS, ECMWF, ERA5 data structures · Assignment: pull and wrangle a dataset with Herbie/xarray</span></td></tr>
  <tr><td class="wk">06</td><td class="mod"><span class="mod-tag">B</span></td><td class="topic"><strong>Forecast verification</strong><br><span>Lecture: bias, skill scores, reliability diagrams · Assignment: score a provided forecast/obs pair</span></td></tr>
  <tr><td class="wk">07</td><td class="mod"><span class="mod-tag">B</span></td><td class="topic"><strong>Probabilistic bias correction</strong><br><span>Lecture: quantile mapping to learned correction models · Assignment: code a quantile-mapping correction</span></td></tr>
  <tr><td class="wk">08</td><td class="mod"><span class="mod-tag">B</span></td><td class="topic"><strong>Midterm exam</strong><br><span>Concept and calculation based: extreme value theory through bias correction</span></td></tr>

  <tr class="module-start"><td class="wk">09</td><td class="mod"><span class="mod-tag">C</span></td><td class="topic"><strong>Deep learning for atmospheric data</strong><br><span>Lecture: CNNs, representation learning, why point estimates fail · Assignment: train a small baseline model</span></td></tr>
  <tr><td class="wk">10</td><td class="mod"><span class="mod-tag">C</span></td><td class="topic"><strong>Satellite remote sensing case study</strong><br><span>Lecture: reconstructing surface obs from geostationary retrievals · Assignment: rule-based vs. ML baseline comparison</span></td></tr>
  <tr><td class="wk">11</td><td class="mod"><span class="mod-tag">C</span></td><td class="topic"><strong>Calibrated uncertainty</strong><br><span>Lecture: Deep Kernel Learning, evaluating probabilistic predictions · Assignment: compute calibration &amp; CRPS</span></td></tr>

  <tr class="module-start"><td class="wk">12</td><td class="mod"><span class="mod-tag">D</span></td><td class="topic"><strong>Communicating forecasts</strong><br><span>Lecture: dashboards and visualization for decision-makers · Assignment: a short Dash/Plotly exercise</span></td></tr>
  <tr><td class="wk">13</td><td class="mod"><span class="mod-tag">D</span></td><td class="topic"><strong>Deployment &amp; reproducibility</strong><br><span>Lecture: pipelines, CI, and reproducible research (conceptual) · Final project work session</span></td></tr>
  <tr><td class="wk">14</td><td class="mod"><span class="mod-tag">D</span></td><td class="topic"><strong>Synthesis: heat wave case study</strong><br><span>Lecture: attribution + bias correction + ML tied together · Final project due</span></td></tr>
  <tr><td class="wk">15</td><td class="mod"><span class="mod-tag">D</span></td><td class="topic"><strong>Final exam</strong><br><span>Comprehensive, concept and calculation based</span></td></tr>
</tbody>
</table>
</div>
<div class="module-key">
  <span><span class="mod-tag" style="background:var(--blue)">A</span> Foundations of extremes</span>
  <span><span class="mod-tag" style="background:var(--blue)">B</span> ML for post-processing</span>
  <span><span class="mod-tag" style="background:var(--blue)">C</span> Deep learning &amp; remote sensing</span>
  <span><span class="mod-tag" style="background:var(--blue)">D</span> Building &amp; shipping a live tool</span>
</div>
</section>

<section>
<h2>Assessment</h2>
<div class="assess-bar">
  <div style="width:35%; background:var(--blue);">35%</div>
  <div style="width:20%; background:var(--blue-soft);">20%</div>
  <div style="width:20%; background:var(--accent);">20%</div>
  <div style="width:15%; background:var(--accent-soft);">15%</div>
  <div style="width:10%; background:var(--ink-faint);">10%</div>
</div>
<ul class="assess-legend">
  <li>Weekly problem sets &amp; coding assignments <b>35%</b></li>
  <li>Midterm exam <b>20%</b></li>
  <li>Final project (written analysis + code) <b>20%</b></li>
  <li>Final exam <b>15%</b></li>
  <li>Participation <b>10%</b></li>
</ul>
</section>

<section>
<h2>Instructor</h2>
<p>Sebastian Otarola-Bustos, PhD, is a machine learning and atmospheric scientist focused on weather extremes — heat waves, forecast bias correction, and satellite-based reconstruction of surface observations. The course's case studies are drawn directly from his own research-grade, deployed tools (probabilistic bias correction, GOES-16 satellite ML, live extreme-event dashboards), not textbook exercises. GitHub: <a href="https://github.com/sotarolab">github.com/sotarolab</a>.</p>
</section>

<section>
<h2>Delivery &amp; fit</h2>
<div class="callout">
<p>Structured for part-time / adjunct delivery: a single weekly lecture-plus-lab block, hybrid or fully remote where the department prefers it — nearly all coursework runs in a notebook, so no special infrastructure is required. Best fit as an elective or cross-listed offering in Atmospheric &amp; Environmental Science, Data Science, Statistics, or Computer Science departments; also suited to a professional/extension-studies catalog.</p>
</div>
</section>

<footer>
  <span class="fmono">v1 · draft for department review</span>
  <span class="fmono">contact on request</span>
</footer>

</div>
</div>

---
draft: true  # unpublished: not ready to show
title: 'The Saint-Venant Flume'
summary: 'An interactive shallow-water teaching tool: five live numerical experiments that switch the Saint-Venant source terms on one at a time, each verified against an exact or reference solution.'
date: 2026-08-13
tags:
  - Interactive

# The cover is for the Teaching-page card only — in the body it would repeat
# the figure below and push the "open" button under the fold.
image:
  preview_only: true

show_date: false
reading_time: false
---


{{< applinks app="/apps/saint-venant-flume/" >}}

A browser-based flume for the one-dimensional Saint-Venant equations, built for
teaching. It runs five live numerical experiments, each one switching a single
term of the governing equations on or off, so the contribution of that term is
visible in isolation rather than argued for algebraically.

Every experiment is computed with the same Godunov-type HLL finite-volume
scheme and checked against an exact or reference solution, drawn dashed
alongside the numerical result — so the tool also demonstrates what
verification looks like, not only what the physics does.

{{< rstrip >}}
{{< rfig image="/media/teaching/saint-venant-dam-break.png" ratio="1180/700" wide="true"
         alt="Experiment I of the flume: an upper panel of water depth against distance showing the finite-volume solution overlaying the exact dam-break solution with the rarefaction fan, plateau and bore marked; a lower x–t plane showing the characteristic fan and the shock path; and controls for tailwater ratio and for switching between the Stoker wet-bed and Ritter dry-bed solutions." >}}
**Experiment I — the dam break as a Riemann problem.** With every source term
switched off, what remains is the bare hyperbolic core. The finite-volume
solution (solid) runs against the exact solution (dashed); below, the same
event in the x–t plane, where the rarefaction fan and the shock path are the
characteristics themselves. The tailwater slider moves continuously between
the Stoker wet-bed and Ritter dry-bed cases.
{{< /rfig >}}
{{< /rstrip >}}

## The five experiments

1. **Right-hand side off** — a dam break on a flat, frictionless bed. The
   Riemann problem, with rarefaction, plateau and bore, against the exact
   solution.
2. **Bed slope on** — flow over a bump, and the well-balanced property: what a
   scheme must do to leave a lake at rest alone.
3. **Friction on** — a flood wave meeting Manning roughness.
4. **Two dimensions** — the same system with the flux pointing in *x* and *y*,
   which is where grid orientation starts to show in the solution.
5. **Rotation on** — adding the Coriolis term and swapping gravity for reduced
   gravity, at which point the same equations stop describing a flood and start
   describing a density current in the atmosphere.

The through-line is that the shallow-water system with the source terms removed
is formally identical to isentropic gas dynamics with γ = 2, with the Froude
number playing the role of Mach. The last experiment is where that equivalence
becomes the point: a student who has followed the flood-wave case has already
done most of the work needed for the atmospheric one.

## Using it in a course

The tool assumes a first course in open-channel hydraulics or fluid mechanics.
Each experiment is self-contained and runs in the browser with no install, so
it works as a lecture demonstration, as a lab in place of a flume session when
no flume is available, or as pre-reading before the numerical methods are
derived on the board.

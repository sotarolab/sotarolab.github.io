/*
  Mountain waves in stratified flow — the figure on /research/.

  Activated by `#mtw-canvas` in the page (content/research.md); a no-op
  elsewhere. Styling lives in assets/css/custom/06-figures.css.

  ── The physics ─────────────────────────────────────────────────────────────
  Steady, hydrostatic, uniform flow U through a uniformly stratified atmosphere
  of buoyancy frequency N, over a two-dimensional ridge. For the Witch of
  Agnesi profile

      h(x) = h₀ a² / (x² + a²)

  the linear solution (Queney 1948) for the vertical displacement of a
  streamline whose far-upstream height is z is

      η(x, z) = h₀ a · [ a·cos(lz) − x·sin(lz) ] / (x² + a²),     l = N/U

  where l is the Scorer parameter. Two things fall out of that expression and
  both are visible in the render:

   • At z = 0 it reduces to h(x) — the flow follows the terrain, which is the
     lower boundary condition, not something imposed on the drawing.
   • The cos/sin pair rotates with height, so the phase lines TILT UPSTREAM as
     z increases. That upstream tilt is the signature of a vertically
     propagating mountain wave — it carries momentum downward, which is why
     these waves matter for surface drag in NWP, and it is exactly the regime
     WFIP2 was instrumented for in the Columbia River Gorge.

  The vertical wavelength is 2π/l = 2πU/N: faster flow or weaker stratification
  stretches the pattern vertically. VERT_WAVELENGTHS below sets how many fit in
  the frame, which is the only free parameter here that is chosen for looks
  rather than physics.

  ── Implementation ──────────────────────────────────────────────────────────
  Streamlines are polylines through η evaluated on a grid — cheap, and redrawn
  only on resize. The animation is tracer particles advected along those same
  streamlines at constant horizontal speed, which is what makes it read as flow
  rather than as a contour plot. Particle vertical position comes from the same
  η, so the tracers and the streamlines cannot drift out of agreement.

  Frames stop when the canvas scrolls out of view or the tab is hidden, and
  `prefers-reduced-motion` gets streamlines with no tracers.
*/
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById('mtw-canvas');
    if (!canvas) return;

    var ctx = canvas.getContext('2d');
    if (!ctx) return;

    // ── Amplitude and the overturning limit ───────────────────────────────
    // At x = 0 the solution reduces to η = h₀·cos(lz), so ∂η/∂z = −h₀·l·sin(lz)
    // and the steepest streamline slope in the whole field is h₀·l. Once that
    // reaches 1 the streamlines fold over each other — isentropes go vertical,
    // the wave overturns and breaks, and the linear solution being drawn here
    // is no longer valid. On screen it shows up as streamlines CROSSING, which
    // cannot happen in a steady flow and reads instantly as a broken figure.
    //
    // So NONDIM_AMPLITUDE = h₀·l is the parameter that matters, not the ridge
    // height on its own; the height is derived from it below. Keep it well
    // under 1.
    var NONDIM_AMPLITUDE = 0.62;
    // ⚠️ The caption in content/research.md describes this pattern. If the
    // vertical wavelength changes enough to alter what the figure shows, the
    // caption needs revisiting too.
    var VERT_WAVELENGTHS = 1.15; // 2π/l across the frame height
    var N_STREAMLINES = 17;
    var PARTICLES_PER_LINE = 16;
    var SPEED = 0.14;            // fraction of frame width per second

    var W = 0, H = 0, dpr = 1;
    var a = 0, h0 = 0, l = 0;
    var lines = [];              // precomputed streamline polylines
    var parts = [];
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var visible = true, raf = null, last = null;

    function palette() {
      var dark = document.documentElement.classList.contains('dark');
      return dark
        ? { line: 'rgba(125,199,255,0.34)', tracer: 'rgba(157,220,255,0.95)',
            ridge: '#3a4450', ridgeEdge: 'rgba(173,186,199,0.55)' }
        : { line: 'rgba(9,105,218,0.30)',  tracer: 'rgba(5,80,174,0.85)',
            ridge: '#d8dee6', ridgeEdge: 'rgba(31,35,40,0.45)' };
    }
    var pal = palette();

    // Terrain height above the baseline, in canvas pixels.
    function terrain(x) {
      return h0 * a * a / (x * x + a * a);
    }

    // Streamline displacement for a parcel whose far-upstream height is z.
    function eta(x, z) {
      var lz = l * z;
      return h0 * a * (a * Math.cos(lz) - x * Math.sin(lz)) / (x * x + a * a);
    }

    // Screen y for a streamline of undisturbed height z at horizontal position x.
    // x and z are measured from frame centre / ground respectively.
    function screenY(x, z) {
      return H - (z + eta(x, z));
    }

    function build() {
      var rect = canvas.getBoundingClientRect();
      if (!rect.width || !rect.height) return false;

      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = Math.round(rect.width);
      H = Math.round(rect.height);
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      a = W / 15;                             // ridge half-width
      l = 2 * Math.PI * VERT_WAVELENGTHS / H; // Scorer parameter N/U
      h0 = NONDIM_AMPLITUDE / l;              // ridge height, from the limit above

      // Streamlines, evenly spaced in undisturbed height, starting at the
      // ground. z = 0 makes η reduce to h(x) exactly, so the lowest streamline
      // IS the terrain profile — the flow follows the hill because the solution
      // says so, not because the drawing forces it.
      lines = [];
      var zTop = H * 0.97;
      var zs = [];
      for (var i = 0; i < N_STREAMLINES; i++) {
        zs.push(zTop * (i / (N_STREAMLINES - 1)));
      }
      for (var i2 = 0; i2 < zs.length; i2++) {
        var pts = [];
        for (var px = 0; px <= W; px += 2) {
          pts.push(px, screenY(px - W / 2, zs[i2]));
        }
        lines.push(pts);
      }

      // Tracers ride the streamlines themselves rather than being scattered
      // through the domain — same z values as the lines above, so a particle
      // can never appear to drift off the curve it is supposed to be following.
      // Phase is offset per line so they do not march in visible columns.
      parts = [];
      for (var m = 0; m < zs.length; m++) {
        for (var n = 0; n < PARTICLES_PER_LINE; n++) {
          parts.push({
            x: W * ((n + 0.37 * m) % PARTICLES_PER_LINE) / PARTICLES_PER_LINE,
            z: zs[m],
          });
        }
      }
      return true;
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);

      // Ridge silhouette.
      ctx.beginPath();
      ctx.moveTo(0, H);
      for (var px = 0; px <= W; px += 3) {
        ctx.lineTo(px, H - terrain(px - W / 2));
      }
      ctx.lineTo(W, H);
      ctx.closePath();
      ctx.fillStyle = pal.ridge;
      ctx.fill();
      ctx.strokeStyle = pal.ridgeEdge;
      ctx.lineWidth = 1;
      ctx.stroke();

      // Streamlines.
      ctx.strokeStyle = pal.line;
      ctx.lineWidth = 1;
      for (var i = 0; i < lines.length; i++) {
        var pts = lines[i];
        ctx.beginPath();
        ctx.moveTo(pts[0], pts[1]);
        for (var j = 2; j < pts.length; j += 2) ctx.lineTo(pts[j], pts[j + 1]);
        ctx.stroke();
      }

      if (reduced) return;

      // Tracers.
      ctx.fillStyle = pal.tracer;
      for (var k = 0; k < parts.length; k++) {
        var p = parts[k];
        var y = screenY(p.x - W / 2, p.z);
        ctx.beginPath();
        ctx.arc(p.x, y, 1.15, 0, 6.2832);
        ctx.fill();
      }
    }

    function frame(ts) {
      if (last === null) last = ts;
      var dt = Math.min((ts - last) / 1000, 0.05);
      last = ts;
      var dx = SPEED * W * dt;
      for (var k = 0; k < parts.length; k++) {
        parts[k].x += dx;
        if (parts[k].x > W) parts[k].x -= W;
      }
      draw();
      raf = requestAnimationFrame(frame);
    }

    function start() {
      if (reduced || raf !== null || !visible || document.hidden) return;
      last = null;
      raf = requestAnimationFrame(frame);
    }

    function stop() {
      if (raf !== null) { cancelAnimationFrame(raf); raf = null; }
    }

    function rebuild() {
      stop();
      if (build()) { draw(); start(); }
    }

    rebuild();

    if ('ResizeObserver' in window) {
      var pending = null;
      new ResizeObserver(function () {
        clearTimeout(pending);
        pending = setTimeout(rebuild, 150);
      }).observe(canvas);
    }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible) start(); else stop();
      }, { threshold: 0 }).observe(canvas);
    }

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else start();
    });

    // Recolour on theme toggle without rebuilding the geometry.
    new MutationObserver(function () {
      pal = palette();
      draw();
    }).observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
  });
})();

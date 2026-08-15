/*
  Research figure strip — lazy video loading and scroll-driven playback.

  Activated by `.rstrip` in the page (content/research.md); a no-op elsewhere.
  Layout lives in assets/css/custom/06-figures.css.

  ── Why the videos are lazy ─────────────────────────────────────────────────
  Two clips totalling ~2.4 MB, below the fold. Each <video> ships with
  `preload="none"` and its real URL parked in `data-src`; the source is attached
  only when the element scrolls into view, and playback pauses when it leaves.
  Until then the poster JPEG stands in, so the strip looks complete either way.

  ── Alignment ───────────────────────────────────────────────────────────────
  When the strip sits directly under the biography hero, it has to line up with
  the About column of that block rather than with the prose rail its own
  markdown block sits on. Those are different containers and the offset between
  them is not constant across viewport widths, so it is measured rather than
  guessed.

  The strip currently lives on /research/, which has no biography block — so
  `col` is null, `align()` returns early, and the CSS fallback (flush left on
  the rail) governs. That is correct there. The code stays because moving the
  strip back under a hero is a content-only change.
*/
document.addEventListener('DOMContentLoaded', function () {
  var wrap = document.querySelector('.rstrip-align');
  var col = document.querySelector('.resume-biography [class*="col-span-8"]');

  function align() {
    if (!wrap || !col) return;
    wrap.style.marginLeft = '0px';
    wrap.style.width = '';
    var c = col.getBoundingClientRect();
    var w = wrap.getBoundingClientRect();
    var delta = c.left - w.left;
    // Below the md breakpoint the hero stacks to a single column and the offset
    // collapses to ~0; never shift left.
    if (delta > 1) {
      wrap.style.marginLeft = delta + 'px';
      var many = wrap.querySelectorAll('.rstrip-item').length > 1;
      wrap.style.width = (many ? c.width : Math.min(760, c.width)) + 'px';
    }
  }

  align();
  // Web fonts change the sidebar's intrinsic width, which moves the grid.
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(align);
  var pending = null;
  window.addEventListener('resize', function () {
    clearTimeout(pending);
    pending = setTimeout(align, 120);
  });

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Animated WebP plays automatically inside an <img> and cannot be paused, so
  // honouring reduced-motion means swapping in the still frame instead.
  if (reduced) {
    document.querySelectorAll('img.rstrip-media[data-still]').forEach(function (im) {
      im.src = im.dataset.still;
    });
  }

  var vids = document.querySelectorAll('video.rstrip-media[data-src]');
  if (!vids.length) return;

  if (reduced || !('IntersectionObserver' in window)) {
    // No autoplay: attach the source and expose controls so the clip is still
    // reachable, just never moving on its own.
    vids.forEach(function (v) {
      v.src = v.dataset.src;
      v.controls = true;
      v.removeAttribute('loop');
    });
    return;
  }

  // The clips carry native `controls`, so a visitor can pause one. That has to
  // beat the scroll-driven autoplay below: without this, pausing and scrolling
  // away would silently restart playback on the way back, which reads as the
  // control being broken. `_prog` marks pauses this script issues itself so
  // they are not mistaken for a deliberate one.
  vids.forEach(function (v) {
    v.addEventListener('pause', function () {
      if (!v._prog) v._userPaused = true;
    });
    v.addEventListener('play', function () { v._userPaused = false; });
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      var v = e.target;
      if (e.isIntersecting) {
        if (!v.src) v.src = v.dataset.src;
        if (v._userPaused) return;
        var p = v.play();
        if (p && p.catch) p.catch(function () { /* autoplay refused; controls are already on */ });
      } else if (!v.paused) {
        v._prog = true;
        v.pause();
        v._prog = false;
      }
    });
  }, { threshold: 0.2 });

  vids.forEach(function (v) { io.observe(v); });
});

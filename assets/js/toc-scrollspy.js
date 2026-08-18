/*
  Section rail — marks the section you are currently reading.

  Activated by `nav.site-toc` (layouts/_partials/components/toc.html); a no-op
  on pages without the rail. The active state reuses the rail's hover styling,
  in assets/css/custom/13-toc.css.

  ── Why scroll position, not IntersectionObserver ───────────────────────────
  The obvious approach — observe the headings and light up whichever is
  intersecting — breaks on this site's actual content. A section here can be
  one paragraph (Downscaling of Climate Extremes) or four figures deep
  (Atmospheric Rivers), so at any moment several headings are inside the
  viewport, none are, or a short section never gets a frame to itself. What
  the reader means by "the section I am in" is simply the last heading they
  scrolled past, which is a position question, not a visibility one.

  So: on scroll, find the last heading whose top has crossed a line just below
  the navbar. Two edges need special handling — above the first heading
  nothing is active, and at the bottom of the page the final section may be
  too short to ever reach the line, so the last heading wins outright.

  The handler reads a handful of rects and writes nothing unless the active
  entry actually changed, so it runs straight off the scroll event. A
  requestAnimationFrame throttle would be the reflex here, but there is no
  layout thrash to batch — six reads, no interleaved writes — and it would put
  the behaviour a frame behind the scroll for no measurable gain.
*/
document.addEventListener('DOMContentLoaded', function () {
  var nav = document.querySelector('nav.site-toc');
  if (!nav) return;

  var links = [].slice.call(nav.querySelectorAll('.site-toc-link'));
  if (!links.length) return;

  /* Pair each link with the heading it points at, dropping any that dangle.
     Order follows the rail, which follows the document. */
  var entries = links
    .map(function (link) {
      var id = decodeURIComponent((link.getAttribute('href') || '').slice(1));
      var target = id ? document.getElementById(id) : null;
      return target ? { link: link, target: target } : null;
    })
    .filter(Boolean);

  if (!entries.length) return;

  var current = null;

  /* The navbar is sticky, so a heading is "reached" when it clears the bar
     rather than the viewport top. `--navbar-height` is the theme's own
     variable; the fallback matches its default. */
  function threshold() {
    var styles = getComputedStyle(document.documentElement);
    var height = parseInt(styles.getPropertyValue('--navbar-height'), 10);
    return (isNaN(height) ? 64 : height) + 24;
  }

  function activeEntry() {
    /* Bottom of the page: the last section is current whether or not its
       heading ever crossed the line. Without this, a short closing section
       can never be reached by scrolling. */
    var scrolled = window.innerHeight + window.scrollY;
    if (scrolled >= document.documentElement.scrollHeight - 2) {
      return entries[entries.length - 1];
    }

    var line = threshold();
    var found = null;
    for (var i = 0; i < entries.length; i++) {
      if (entries[i].target.getBoundingClientRect().top <= line) {
        found = entries[i];
      } else {
        break;
      }
    }

    /* Above the first heading — on load, or scrolled back to the top — fall
       back to the first entry rather than clearing the rail. An inert rail
       reads as broken, and the overclaim is small: on pages that open with a
       heading it is exactly right, and on those that open with an intro the
       reader is a paragraph away from that section anyway. */
    return found || entries[0];
  }

  function update() {
    var next = activeEntry();
    if (next === current) return;

    if (current) {
      current.link.classList.remove('is-active');
      current.link.removeAttribute('aria-current');
    }
    if (next) {
      next.link.classList.add('is-active');
      /* "location" is the value for the current position within a page, as
         opposed to `page`, which the nav uses for the current page. */
      next.link.setAttribute('aria-current', 'location');
    }
    current = next;
  }

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update, { passive: true });
  update();
});

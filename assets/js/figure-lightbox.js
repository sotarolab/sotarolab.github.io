/* Click a figure to open it full-size.
 *
 * The Research page carries multi-panel plots — six Chile maps, five lidar
 * scans, three benchmark panels — sized to fit a text column. At 600-700px the
 * layout reads, but the axis numbers do not. This opens the same image at the
 * size of the viewport, with its caption, and gets out of the way again.
 *
 * Progressive enhancement: with JS off, the figures render exactly as before.
 * Nothing here is required to read the page.
 *
 * Scope: images only. A <video> already has its own controls and a fullscreen
 * button, and hijacking a click on it would break scrubbing.
 *
 * Theme variants: a figure with a dark companion ships BOTH <img> tags, one
 * hidden by CSS (see 06-figures.css). EVERY variant is bound, including the
 * hidden one — an earlier version skipped hidden images and so broke the
 * moment a reader used the theme toggle, because the newly-visible variant had
 * no handler. Binding both is safe on all counts: a `display: none` image
 * cannot be clicked and is already outside the tab order, so it adds neither a
 * stray tab stop nor a way to open the wrong canvas.
 */

(function () {
  'use strict';

  var SELECTOR = '.rstrip-frame img.rstrip-media';

  function build() {
    var overlay = document.createElement('div');
    overlay.className = 'lbx';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.hidden = true;

    // Empty alt: the dialog is labelled by its caption, and the figure has
    // already been described in the page. Repeating the full alt text here
    // makes a screen reader read the whole description twice.
    overlay.innerHTML =
      '<button class="lbx-close" type="button" aria-label="Close">&times;</button>' +
      '<figure class="lbx-figure">' +
      '<img class="lbx-img" alt="">' +
      '<figcaption class="lbx-cap"></figcaption>' +
      '</figure>';

    document.body.appendChild(overlay);
    return overlay;
  }

  function init() {
    var figures = document.querySelectorAll(SELECTOR);
    if (!figures.length) return;

    var overlay = build();
    var img = overlay.querySelector('.lbx-img');
    var cap = overlay.querySelector('.lbx-cap');
    var closeBtn = overlay.querySelector('.lbx-close');
    var opener = null;

    function open(source) {
      var figure = source.closest('.rstrip-item');
      var caption = figure ? figure.querySelector('.rstrip-cap') : null;

      // currentSrc, not src: it is what the browser actually fetched, so a
      // responsive or lazily-swapped source opens as the reader sees it.
      img.src = source.currentSrc || source.src;
      img.alt = source.alt || '';
      cap.innerHTML = caption ? caption.innerHTML : '';
      cap.hidden = !caption;

      opener = source;
      overlay.hidden = false;
      // The page behind must not scroll under the overlay — on iOS especially,
      // a scroll started on the backdrop otherwise moves the article.
      document.body.classList.add('lbx-open');
      closeBtn.focus();
    }

    function close() {
      overlay.hidden = true;
      document.body.classList.remove('lbx-open');
      // Release the decoded image; a 6-map plot is several MB in memory.
      img.removeAttribute('src');
      if (opener) {
        opener.focus();
        opener = null;
      }
    }

    Array.prototype.forEach.call(figures, function (source) {
      source.classList.add('lbx-trigger');
      source.setAttribute('role', 'button');
      source.setAttribute('tabindex', '0');
      source.setAttribute('aria-haspopup', 'dialog');

      source.addEventListener('click', function () {
        open(source);
      });
      source.addEventListener('keydown', function (e) {
        // Enter and Space are what a real <button> responds to; without this
        // the role above would be a lie to anyone not using a mouse.
        if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {
          e.preventDefault();
          open(source);
        }
      });
    });

    closeBtn.addEventListener('click', close);

    // Click anywhere outside the image — the backdrop is the biggest, most
    // guessable close target there is.
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay || e.target.classList.contains('lbx-figure')) close();
    });

    document.addEventListener('keydown', function (e) {
      if (overlay.hidden) return;
      if (e.key === 'Escape') {
        close();
        return;
      }
      // Focus stays on the close button: the dialog holds one control, so a
      // full focus trap would be ceremony. Tab simply cannot leave it.
      if (e.key === 'Tab') {
        e.preventDefault();
        closeBtn.focus();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

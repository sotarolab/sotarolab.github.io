/*
  Accessible names for the profile links in the biography sidebar.

  The `resume-biography-3` block sets `aria-label` to the *icon name* — a screen
  reader announces the e-mail link as "at-symbol" and the GitHub link as
  "brands/github" — while the human-readable string from the author profile goes
  into `title`. assets/css/custom/03-biography.css surfaces `title` visually via
  generated content, which sighted users get but assistive tech does not
  reliably expose.

  Copying title → aria-label repairs both. Four lines is cheaper than forking
  the 400-line block template to fix one attribute; drop this file (and its
  entry in layouts/_partials/hooks/head-end/custom-assets.html) if the block is
  ever fixed upstream.
*/
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.resume-biography a[title]').forEach(function (a) {
    a.setAttribute('aria-label', a.getAttribute('title'));
  });
});

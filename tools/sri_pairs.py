"""Emit "<url>\t<integrity>" for every fingerprinted asset in the built site.

Used by tools/qc.sh to re-derive Subresource Integrity hashes from the published
bytes. Lives in its own file rather than a heredoc because the regex needs both
quote characters, and bash tracks quoting inside `$(...)` even across a quoted
heredoc — which turns an inline version into a syntax error.
"""

import glob
import html
import re

# href/src may be unquoted in minified HTML, hence the optional quote group.
# The URL may also be absolute when the site is built with a production baseURL
# (CI does this), so the scheme and host are optional and stripped below.
PATTERN = re.compile(
    r"""(?:href|src)=["']?"""
    r"""((?:https?://[^"'\s>/]+)?/(?:css|js)/[^"'\s>]+)"""
    r"""["']?[^>]*?integrity="([^"]+)\"""",
    re.VERBOSE,
)

seen = set()
for page in glob.glob("public/**/*.html", recursive=True):
    with open(page, encoding="utf-8", errors="replace") as fh:
        markup = fh.read()
    for url, integrity in PATTERN.findall(markup):
        # Reduce to a site-root path so the caller can map it onto public/.
        path = re.sub(r"^https?://[^/]+", "", url)
        # Base64 hashes contain '+' and '/', and Hugo HTML-escapes '+' to
        # '&#43;' inside the attribute. Comparing the raw attribute text against
        # a freshly computed hash then fails for roughly half of all builds —
        # whichever ones happen to produce a '+' in the digest.
        integrity = html.unescape(integrity)
        if path not in seen:
            seen.add(path)
            print(path + "\t" + integrity)

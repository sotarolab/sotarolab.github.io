"""Check the built custom CSS bundle for prematurely-closed comments.

CSS comments do not nest. A comment that quotes a comment-closing delimiter
terminates there, and the remaining prose is parsed as CSS — which sends the
parser into error recovery and makes it discard the NEXT rule entirely.

This has bitten this repo twice, both times invisibly: the build is clean, the
page renders, and one custom property is simply missing in one theme. There is
no warning anywhere.

Detection: strip well-formed comments, then look at what is left. A stray
closing delimiter in the residue means some comment ended early.

Also verifies that the tokens the stylesheets depend on are actually defined,
since a swallowed rule shows up as a missing definition.

Usage: python3 tools/check_css.py <bundle.css>
Exits 1 on failure.
"""

import re
import sys

# Tokens that must be defined for BOTH themes. Each maps to the number of
# definitions expected (light in :root, dark in html.dark).
REQUIRED_TOKENS = {
    "--hb-border": 2,
    "--hb-bold": 2,
    "--hb-nav-active": 2,
    "--hb-rail": 1,
    "--hb-gutter": 1,
    "--hb-wide": 1,
    "--hb-body-size": 1,
    "--hb-body-lh": 1,
    "--hb-caption-size": 1,
    "--hb-caption-lh": 1,
}

COMMENT = re.compile(r"/\*.*?\*/", re.S)


def main(path):
    with open(path, encoding="utf-8") as fh:
        css = fh.read()

    problems = []

    residue = COMMENT.sub("", css)
    for m in re.finditer(r"\*/", residue):
        snippet = residue[max(0, m.start() - 90):m.start() + 2].replace("\n", " ")
        problems.append(
            "stray comment-closing delimiter outside any comment — a comment "
            "closed early and the rule after it was discarded:\n"
            "         ..." + snippet
        )

    for token, expected in REQUIRED_TOKENS.items():
        found = len(re.findall(re.escape(token) + r"\s*:", residue))
        if found < expected:
            problems.append(
                "%s is defined %d time(s), expected %d — a rule was probably "
                "swallowed by a malformed comment" % (token, found, expected)
            )

    if problems:
        for p in problems:
            print("  " + p)
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: check_css.py <bundle.css>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))

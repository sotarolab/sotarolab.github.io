---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}

# Shown in the Live Tools list on /research/. One or two sentences — what the
# tool does and what makes it non-obvious, not what technology it uses.
summary: ""

# Rendered as buttons on the project page.
#   site     the running application
#   code     public repository
#   dataset  published data
# Omit the list entirely rather than linking a repo that is not public yet; say
# so in the body instead.
links:
  - type: site
    url: ""
  - type: code
    url: ""

tags:
  - ""
---

<!-- Lede paragraph, then `<!--more-->`, then the detail. Everything above the
     more-marker is what the listing shows if `summary` is absent. -->

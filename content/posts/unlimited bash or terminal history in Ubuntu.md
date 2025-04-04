---
author: "Saqib Razzaq"
title: "Unlimited terminal history in Ubuntu"
date: "2021-01-01"
tags: ["bash"]
ShowToc: true
TocOpen: true
---

Add this to your `.bashrc` (Linux) or `.bash_profile` (MacOS):

```bash
export HISTFILESIZE=-1
export HISTSIZE=-1
```
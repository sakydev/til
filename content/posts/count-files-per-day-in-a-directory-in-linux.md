---
author: "Saqib Razzaq"
title: " How to count files per day in a directory in Linux"
date: "2019-03-11"
tags: ["python", "linux"]
ShowToc: true
TocOpen: true
---

`find directory -type f -printf '%TY-%Tm-%Td\n' | sort | uniq -c`
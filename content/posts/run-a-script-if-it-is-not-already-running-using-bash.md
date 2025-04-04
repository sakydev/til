---
author: "Saqib Razzaq"
title: "How to run a script if it is not already running in Linux"
date: "2021-11-11"
tags: ["bash", "linux"]
ShowToc: true
TocOpen: true
---

Let's say you have a script called `crawl.py` and you never want two instances of it running at the same time. The following script can do the job

```bash
RUNNING="$(ps aux|grep crawl|grep -v grep|wc -l)"
if [ $RUNNING -eq 0 ]
then
    python crawl.py
else
  echo "Already running : skipping";
fi
```
---
author: "Saqib Razzaq"
title: "Python + Scrapy: retry failed requests"
date: "2021-01-21"
tags: ["scrapy", "python"]
ShowToc: true
TocOpen: true
---

You can add one or more statuses in settings.py. Scrapy will process requests normally and when one of these statuses is encountered, it will retry that request.

You can modify `RETRY_HTTP_CODES` and add any number of statuses there.

You can also control how many times to try with `RETRY_TIMES`
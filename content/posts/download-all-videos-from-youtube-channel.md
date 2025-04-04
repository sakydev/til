---
author: "Saqib Razzaq"
title: "Download all videos from YouTube channel"
date: "2021-03-28"
description: "How to use YouTube-dl to download entire channel"
tags: ["youtube-dl", "automations"]
ShowToc: true
TocOpen: true
---

[YouTube-dl Download and Documentation](https://youtube-dl.org/)

This command iterates over entire channel and downloads each video one by one.

`youtube-dl -f best -ciw -o "%(title)s.%(ext)s" -v url_of_channel`
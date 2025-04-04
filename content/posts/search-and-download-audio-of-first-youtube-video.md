---
author: "Saqib Razzaq"
title: "Search YouTube and download first result"
date: "2021-06-17"
description: "How to searcha and download videos using YouTube-dl"
tags: ["youtube-dl"]
ShowToc: true
TocOpen: true
---

[YouTube-dl Download and Documentation](https://youtube-dl.org/)

I was a long time user of YTMusic, a premium music subscription service. One day they randomly stopped accepting payments from my card. I tried a few others but nothing worked. In a few days I lost access to all my songs and I had to start with a new account with no explanation for what happened. 

I decided to not let this happen again and started building a backup of songs. Every time I liked a song, I would append it to  list on Evernote. Now whenever I need to have all those songs available locally, I run the following command which iterates over each song title, searches youtube and dowloads first video's audio. This is about 96% accurate :D

`youtube-dl -a smallkeys.txt --no-playlist --default-search ytsearch -x -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0  --write-info-json --skip-download
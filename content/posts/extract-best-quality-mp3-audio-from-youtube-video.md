---
author: "Saqib Razzaq"
title: "Download best audio of a YouTube video as MP3"
date: "2021-03-24"
tags: ["youtube-dl"]
ShowToc: true
TocOpen: true
---

[YouTube-dl Download and Documentation](https://youtube-dl.org/)

Download the best quality audio in mp3 format using the command below. This command also utilises ffmpeg to extract audio. In general, it is a good idea to have ffmpeg installed on your system if you plan to use YouTube-dl

`youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 'url_here'`
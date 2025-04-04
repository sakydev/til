---
author: "Saqib Razzaq"
title: "FFMPEG Cheatsheet"
date: "2019-08-11"
tags: ["ffmpeg", "cheatsheets"]
ShowToc: true
TocOpen: true
---

#### add subtitles
You can hardcode subtitles by providing a subtitles files and running the following command

```bash
ffmpeg -i input.mp4 -vf subtitles=subs.srt out.mp4
```

#### add watermark in any position
The base command for adding watermark looks like this

`ffmpeg -i input.mp4 -i watermark.png -filter_complex "POSITION_HERE" out.mp4`

You can replace `POSITION_HERE` with any position you need from the following

Top Right
`overlay=main_w-overlay_w-10:10`

Top Left
`overlay=10:10`

Bottom Right
`overlay=main_w-overlay_w-10:main_h-overlay_h-10`

Bottom Left
`overlay=10:main_h-overlay_h-10`

Center
`overlay=x=(main_w-overlay_w)/2:y=(main_h-overlay_h)/2`

#### extract audio
If you need to extract audio of a video with re-encoding the whole thing then you can run following command

`ffmpeg -i input.mp4 -vn -acodec copy out.mp3`

#### extract video waveform
Following command can be used to extract video waveform

`ffmpeg -i input.mp4 -filter_complex "compand,showwavespic=s=640x120" -frames:v 1 out.png`

#### flip a video
Horizontally
`ffmpeg -i input.mp4 -vf 'hflip' out.mp4`

Vertically
`ffmpeg -i input.mp4 -vf 'vflip' out.mp4`

#### generate thumbnails
If you are running a video sharing website or a similar service, you might want to extract thumbnails from video. This is helpful to show what video represents. You can run following command for this.

`ffmpeg -i input.mp4 -ss 00:00:10 -vframes 12 thumb.png`

#### audio volume
Reduce volume by half
`ffmpeg -i input.wav -filter:a "volume=0.5" output.wav`

Increase volume to 150%
`ffmpeg -i input.wav -filter:a "volume=1.5" output.wav`

You can also replace `0.5` with `dB`

#### video speed
`ffmpeg -i input -filter:v "setpts=0.5*PTS" output`

You can adjust speed by changing `0.5`

#### video greyscale
You can make an entire video or a part of it greyscale.

full video greyscale
`ffmpeg -i input.mp4 -vf "hue=s=0" out.mp4`

part of video greyscale
`ffmpeg -i input.mp4 -vf "hue=s=0:enable=\'between(t,3,5)\" out.mp4`

#### mute video
You can remove audio from video with this command

`ffmpeg -i input.mp4 -c copy -an out.mp4`

#### reverse video
only reverse video
`ffmpeg -i input.mp4 -vf 'reverse' out.mp4`


reverse audio and video
`ffmpeg -i input.mp4 -vf 'reverse' -af 'areverse' out.mp4`

#### rotate video by x degrees
Following command can be used to rotate videos

`ffmpeg -i input.mp4 -c copy -metadata:s:v:0 rotate=360 out.mp4`

Here you can replace `360`with any values e.g 180

#### show two videos side by side
If you want to display two videos side by side like mostly done on news channels, it can be done like this

`ffmpeg -i left.mp4 -i right.mp4 -filter_complex hstack output.mp4`

#### split video
`ffmpeg -i input.mp4 -ss 0 -t 300 -c copy out.mp4`

Here `0` is start time in seconds and `300` is end time. This command extracts first 5 minutes of video. You can replace it with any time you need.

### How to Add subtitles in FFMPEG

You can hardcode subtitles by providing a subtitles files and running the following command

`ffmpeg -i input.mp4 -vf subtitles=subs.srt out.mp4`
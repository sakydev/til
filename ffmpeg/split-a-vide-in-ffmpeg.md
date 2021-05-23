### How to Split a video in FFMPEG

`ffmpeg -i input.mp4 -ss 0 -t 300 -c copy out.mp4`

Here `0` is start time in seconds and `300` is end time. This command extracts first 5 minutes of video. You can replace it with any time you need.
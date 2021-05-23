### How to Extract audio of a video in FFMPEG

If you need to extract audio of a video with re-encoding the whole thing then you can run following command

`ffmpeg -i input.mp4 -vn -acodec copy out.mp3`
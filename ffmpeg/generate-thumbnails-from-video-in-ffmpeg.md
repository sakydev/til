### How to Generate thumbnails from video in FFMPEG

If you are running a video sharing website or a similar service, you might want to extract thumbnails from video. This is helpful to show what video represents. You can run following command for this.

`ffmpeg -i input.mp4 -ss 00:00:10 -vframes 12 thumb.png`
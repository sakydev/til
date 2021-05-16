### How to increase video speed using FFMPEG

`ffmpeg -i input -filter:v "setpts=0.5*PTS" output`

You can adjust speed by changing `0.5`
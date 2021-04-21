### How to rotate a video by any degress using Ffmpeg

Following command can be used to rotate videos 

`ffmpeg -i input.mp4 -c copy -metadata:s:v:0 rotate=360 out.mp4`

Here you can replace `360`with any values e.g 180
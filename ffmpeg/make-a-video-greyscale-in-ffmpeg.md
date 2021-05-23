### How to Make a video greyscale  in FFMPEG

You can make an entire video or a part of it greyscale.

**Make full video greyscale**
`ffmpeg -i input.mp4 -vf "hue=s=0" out.mp4`

**Make part of video greyscale**
`ffmpeg -i input.mp4 -vf "hue=s=0:enable=\'between(t,3,5)\" out.mp4`
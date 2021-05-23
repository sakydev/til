### How to Flip a video horizontally or vertically  in FFMPEG

Horizontally
`ffmpeg -i input.mp4 -vf 'hflip' out.mp4`

Vertically
`ffmpeg -i input.mp4 -vf 'vflip' out.mp4`
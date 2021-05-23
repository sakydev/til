### How to Reverse a video in FFMPEG

**To only reverse video**
`ffmpeg -i input.mp4 -vf 'reverse' out.mp4`


**To reverse audio and video**
`ffmpeg -i input.mp4 -vf 'reverse' -af 'areverse' out.mp4`
### How to Add watermark in any position in FFMPEG

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
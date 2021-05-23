### How to Show two videos side by side in FFMPEG

If you want to display two videos side by side like mostly done on news channels, it can be done like this

`ffmpeg -i left.mp4 -i right.mp4 -filter_complex hstack output.mp4`
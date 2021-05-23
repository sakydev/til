### How to Increase or decrease audio in FFMPEG

Reduce volume by half
`ffmpeg -i input.wav -filter:a "volume=0.5" output.wav`

Increase volume to 150%
`ffmpeg -i input.wav -filter:a "volume=1.5" output.wav`

You can also replace `0.5` with `dB`
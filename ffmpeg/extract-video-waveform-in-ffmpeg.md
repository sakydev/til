### How to Extract video waveform in FFMPEG

Following command can be used to extract video waveform

`ffmpeg -i input.mp4 -filter_complex "compand,showwavespic=s=640x120" -frames:v 1 out.png`
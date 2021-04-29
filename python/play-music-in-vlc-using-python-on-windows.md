### How to play music in VLC using Python on Windows

I wanted to be able to play my music each time I start working without having to manually do it via GUI every time. This is what I came up with

```
import os
os.system("vlc.exe.lnk path_to_music_dir --qt-start-minimized")
```

Here `--qt-start-minimized` is used for running VLC in background
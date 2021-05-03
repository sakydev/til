### How to change windows wallpaper using Python3

Following code can be used for changing windows wallpaper

```
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, image , 0)
```
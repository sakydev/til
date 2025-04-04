---
author: "Saqib Razzaq"
title: "How to change windows wallpaper using Python3"
date: "2021-10-11"
tags: ["python", "powershell"]
ShowToc: true
TocOpen: true
---

Following code can be used for changing windows wallpaper

```python
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, image , 0)
```
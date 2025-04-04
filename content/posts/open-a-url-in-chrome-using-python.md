---
author: "Saqib Razzaq"
title: "How to open a URL in chrome using Python"
date: "2021-04-11"
tags: ["python", "google-chrome"]
ShowToc: true
TocOpen: true
---

```python
import webbrowser
webbrowser.register('chrome',
		None,
webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open('http://url.com')
```
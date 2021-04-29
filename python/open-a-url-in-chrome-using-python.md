### How to open a URL in chrome using Python

```
import webbrowser
webbrowser.register('chrome',
		None,
webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open('http://url.com')
```
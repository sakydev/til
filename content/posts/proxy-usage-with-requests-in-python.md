---
author: "Saqib Razzaq"
title: "How to use proxies with Requests in Python"
date: "2021-07-29"
tags: ["python"]
ShowToc: true
TocOpen: true
---


```python
import requests
proxy = 'proxy:goes:here'
proxyDict = {"http"  : proxy, "https"  : proxy}
response = requests.get('https://www.url.com', proxies=proxyDict)
```

You can send the POST requests using a similar format. Headers can be added to the request using `headers={}`
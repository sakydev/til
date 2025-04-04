---
author: "Saqib Razzaq"
title: "Python - search questions using wolframalpha"
date: "2021-10-11"
tags: ["python"]
ShowToc: true
TocOpen: true
---

```python
import json, requests

def search(keyword):
	keyword = keyword.replace(' ', '+')
	data = requests.get('https://api.wolframalpha.com/v2/query?input=' + keyword + '&format=plaintext&output=json&appid=api_id_here')

	readable = data.json()
	results = readable['queryresult']
	if results['success'] == True:
	  for pod in results['pods']:
	    if pod['title'] == 'Result':
	      try:
	        value = pod['subpods'][0]['plaintext']
	        return value
	      except Exception as e:
	        value = ''
	        raise e
	else:
		print('Something went wrong. Below is full data')
		print(readable)
```
---
author: "Saqib Razzaq"
title: "How to update a request URL in Scrapy"
date: "2021-09-27"
tags: ["scrapy", "python"]
ShowToc: true
TocOpen: true
---

 Often times you might want to be able to manipulate every outgoing request. You don't have to modify all points in your scrapper where you're making requests. You can modify your middleware. 
 
 Open `middlewares.py` in your project and paste following code in `process_request` method
 
 ```python
 original_url = request.url
 new_url = 'modified_url_here'
 request = request.replace(url=new_url)
 ```

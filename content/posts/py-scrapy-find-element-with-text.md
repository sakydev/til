---
author: "Saqib Razzaq"
title: "Python + Scrapy: find element with text"
date: "2021-09-29"
tags: ["scrapy", "python"]
ShowToc: true
TocOpen: true
---

```python
response.xpath("//*[contains(text(), 'txt goes here')]").getall()
```
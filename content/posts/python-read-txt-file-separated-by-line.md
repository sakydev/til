---
author: "Saqib Razzaq"
title: "Python -  read txt file separated by line as list"
date: "2021-09-11"
tags: ["python"]
ShowToc: true
TocOpen: true
---

In a web crawling project of mine I had to read proxies from a txt file. Each proxy was on a new line. I used following code to read them as list.

`proxies = [line.rstrip('\n') for line in open(directory + '/proxies_v2.txt')]`

Additionally, I shuffle them to make sure their order is random.

`random.shuffle(proxies)`


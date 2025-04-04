---
author: "Saqib Razzaq"
title: "How to read a CSV file in python"
date: "2021-05-11"
tags: ["python"]
ShowToc: true
TocOpen: true
---


```python
with open(path, mode='r') as csvFile:
  reader = csv.DictReader(csvFile)
  lineCount = 0
  for row in reader:
    if lineCount > 0:
      # do stuff here
    lineCount += 1
```
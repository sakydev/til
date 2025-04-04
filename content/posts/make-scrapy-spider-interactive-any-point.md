---
author: "Saqib Razzaq"
title: "How to make scrapy spider interactive at any point"
date: "2021-03-20"
tags: ["scrapy", "python"]
ShowToc: true
TocOpen: true
---

```python
from scrapy.shell import inspect_response
inspect_response(response, self)
```

[Read this](https://docs.scrapy.org/en/latest/topics/shell.html#invoking-the-shell-from-spiders-to-inspect-responses) for more details
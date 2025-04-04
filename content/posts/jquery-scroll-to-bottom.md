---
author: "Saqib Razzaq"
title: "Jquery - scroll to bottom"
date: "2021-07-10"
tags: ["jquery"]
ShowToc: true
TocOpen: true
---

```javascript
$("html, body").animate({ scrollTop: $(document).height()-$(window).height() });
```
---
author: "Saqib Razzaq"
title: "How to iterate over several elements in jQuery"
date: "2021-07-10"
tags: ["jquery"]
ShowToc: true
TocOpen: true
---

```javascript
// iterate over a list
$.each(list, function(key, field) {
    // something here
});

// find an element across the page and iterate over each
$(document).find('item').each(function(item, object) {
    // something here
});
```
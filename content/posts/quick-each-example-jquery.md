---
author: "Saqib Razzaq"
title: "Quick each loop example in jQuery"
date: "2021-07-10"
tags: ["jquery"]
ShowToc: true
TocOpen: true
---

$.each iterates over all elements specified and performs your code

Iterate over a list
```javascript
$.each(list, function(key, field) {
    // something here
});
```

Find an element across the page and iterate over each
```javascript
$(document).find('item').each(function(item, object) {
    // something here
});
```
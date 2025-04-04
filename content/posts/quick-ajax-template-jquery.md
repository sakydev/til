---
author: "Saqib Razzaq"
title: "Quick Ajax template jQuery"
date: "2021-07-10"
tags: ["jquery"]
ShowToc: true
TocOpen: true
---

Following is a sample Ajax template that can be used when you're not in the mood of surfing through docs

```javascript
$.ajax({
  url: "http://google.com",
  type: "post",
  dataType: "json",
  data: {name: item, value: value},
  success: function (response) {
    // do somethinig here
  },
  error: function(jqXHR, textStatus, errorThrown) {
    console.log(textStatus, errorThrown);
  }
});
```
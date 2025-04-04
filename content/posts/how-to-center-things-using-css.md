---
author: "Saqib Razzaq"
title: "How to center things using CSS"
date: "2019-09-05"
tags: ["css"]
ShowToc: true
TocOpen: true
---

**Center text**
Structure your HTML like this
```
<div class="container">
  <p>Hello, (centered) World!</p>
</div>
```
And then use following CSS
```
p {
  text-align: center;
}
```

**Center a Div with CSS Margin Auto**
```
<div class="container">
  <div class="child"></div>
</div>
```
```
.child {
  margin: 0 auto;
}
```

**Center a Div Horizontally with Flexbox**
```
<div class="container">
  <div class="child"></div>
</div>
```
```
.container {
  display: flex;
  justify-content: center;
}
```
---
author: "Saqib Razzaq"
title: "How to dynamically generate URL for assets in Flask"
date: "2020-05-14"
tags: ["flask", "python"]
ShowToc: true
TocOpen: true
---

You can use `url_for` function for building URLs. For example, let's say you have a assets folder called `static` in main app directory. You can use following code in template files to include `CSS` files

`{{ url_for('static', filename='css/style.css') }}`
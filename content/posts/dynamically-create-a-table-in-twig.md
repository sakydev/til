---
author: "Saqib Razzaq"
title: "How to dynamically create table in Twig"
date: "2019-07-13"
tags: ["bash"]
ShowToc: true
TocOpen: true
---

```
<table class="table table-bordered">
    <thead>
        <tr>
            {% for range, dets in rents %}
                <th scope="col">{{range}}</th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        <tr>
            {% for range, details in rents %}
                <td scope="row">{{details.item}}</td>
            {% endfor %}
        </tr>
    </tbody>
</table>
```
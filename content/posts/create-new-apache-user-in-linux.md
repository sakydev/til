---
author: "Saqib Razzaq"
title: "How to create a new Apache user in Linux server"
date: "2021-01-11"
tags: ["linux"]
ShowToc: true
TocOpen: true
---

Following method can be used for creating a new user in Apache. This comes in real handy for my projects that user Apache authentication. I run following command when I'm asked to create a new user.

`htpasswd /etc/httpd/.htpasswd username_here`
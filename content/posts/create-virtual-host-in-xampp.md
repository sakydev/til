---
author: "Saqib Razzaq"
title: "How to create a virtual host in xampp"
date: "2020-07-21"
tags: ["xampp"]
ShowToc: true
TocOpen: true
---

Let's say `$xampp = 'xampp_installation_directory'`

1. Open `{$xampp}\apache\conf\extra\httpd-vhosts.conf`
3. Add following snippet for a normal project
```
<VirtualHost *:80>
  DocumentRoot "{$xampp}\htdocs\project_name"
  ServerName project_name.localhost
  <Directory "F:\xampp\htdocs\project_name">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
  </Directory>
</VirtualHost>
```
4. Add following snippet for a Laravel project
```
<VirtualHost *:80>
  DocumentRoot "{$xampp}/htdocs/project_name/public"
  ServerName project_name.localhost
  <Directory "F:\xampp\htdocs\lara8/project_name">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
  </Directory>
</VirtualHost>
```
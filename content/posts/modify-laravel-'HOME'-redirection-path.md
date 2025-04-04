---
author: "Saqib Razzaq"
title: "How to modify Laravel 'HOME' redirection path"
date: "2021-08-19"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

When a user logs in, Laravel redirects it to path stored in `HOME` constant by default. If you want to modify this constant or add constants of your own, you can do it like this.

1. Open `app\Providers\RouteServiceProvider.php`
2. Search `public const HOME` to update `HOME` constant
3. You can add your own just like that

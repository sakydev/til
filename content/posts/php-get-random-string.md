---
author: "Saqib Razzaq"
title: "PHP: Get random string"
date: "2018-08-01"
tags: ["php"]
ShowToc: true
TocOpen: true
---


```php
function randomString($length = 10) {
  $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  $charactersLength = strlen($characters);
  $randomString = '';
  for ($i = 0; $i < $length; $i++) {
      $randomString .= $characters[rand(0, $charactersLength - 1)];
  }
  return $randomString;
}
```
---
author: "Saqib Razzaq"
title: "How to read a CSV file in PHP"
date: "2019-01-27"
tags: ["php"]
ShowToc: true
TocOpen: true
---

```php
<?php

$file = 'data.csv';
$separator = "\t";
$done = 0;
if (($handle = fopen($file, "r")) !== FALSE) {
   while (($data = fgetcsv($handle, false, "$separator")) !== FALSE) {
    $done += 1;
    if ($done < 2) {
      $fields = explode($separator, str_replace(' ', '', implode($separator, $data)));
      continue;
    }

    $item = array_combine($fields, $data);
     print_r($item);
  }
}
```
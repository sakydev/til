---
author: "Saqib Razzaq"
title: "How to run a command on multiple MySQL tables using PHP"
date: "2020-11-23"
tags: ["php", "mysql"]
ShowToc: true
TocOpen: true
---

```php
$query = "alter table {table} drop column columnName;";
$tables = array('tableA', 'tableB');
foreach ($tables as $key => $source) {
    $currentQuery = str_replace('{table}', $source, $query);
    DB::query($currentQuery);
}
```
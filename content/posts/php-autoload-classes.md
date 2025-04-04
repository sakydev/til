---
author: "Saqib Razzaq"
title: "PHP - Autoload classes"
date: "2021-02-21"
tags: ["php"]
ShowToc: true
TocOpen: true
---

Here is a quick snippet that showed how classes are loaded in BriskLimbs, a video sharing project of mine

```php
spl_autoload_register(function ($class) {
  $class = ucfirst($class);
  if (file_exists(MODEL_DIRECTORY . '/' . $class . '.php')) {
    require_once MODEL_DIRECTORY . '/' . $class . '.php';
  } else {
    $class = strtolower($class);
    if (file_exists(HELPERS_DIRECTORY . '/' . $class . '.php')) {
      require_once HELPERS_DIRECTORY . '/' . $class . '.php';
    } else {
      exit(MODEL_DIRECTORY . '/' . $class . '.php');
      exit('Error Loading Class File |' . $class . '| core:' . CORE_DIRECTORY);
    }
  }
});
```
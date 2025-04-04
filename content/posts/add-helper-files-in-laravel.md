---
author: "Saqib Razzaq"
title: "How to add helper files in Laravel"
date: "2021-03-17"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

There are some cases when you need to add your own custom functions in Laravel. I often have my own custom helpers for speeding up development. You can easily add your own files by following this quick guide.

1. Create a folder in `app\Http` folder. Let's assume you created `Helpers`  
2. You can place any number of `php` files in this directory.   
3. Then open `composer.json` found in your root directory and find  

```json
"autoload-dev": {
    "psr-4": {
      "Tests\\": "tests/"
    }
  }
```
4. Then replace it so it looks like this  

```json
"autoload-dev": {
    "psr-4": {
      "Tests\\": "tests/"
    },
    "files": [
      "app/Helpers/filename.php"
    ]
  }
```

5. Finally, run `composer dump-autoload` and you are good to go

---
author: "Saqib Razzaq"
title: "How to use validator and get all errors in Laravel"
date: "2021-02-11"
description: "x"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

Laravel has a `validated` function which runs your defined rules and automatically sends errors to your view. This is awesome for most projects but sometimes you may want to handle / read these errors yourself. Or maybe just do it before sending them to view. Here is how you can do that. 

1. First of all, add validator at top of your file  
`use Illuminate\Support\Facades\Validator;`  
2. Then create validator with your rules like this
```php
$validator = Validator::make($requestData, [
      'user_id' => ['required', 'integer']
    ]);
```
3. Then use following snippet to get errors as array
```php
if ($validator->fails()) {
      $fieldsWithErrors = $validator->messages()->get('*');
      // do anything here
    }
```

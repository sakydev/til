---
author: "Saqib Razzaq"
title: "How to add a user middleware in Laravel"
date: "2021-03-17"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

I was building an API. I had already used `auth:api` middleware. I was sure that a user was logged in. However, I wanted to protect some of my routes further by only allowing an admin to access them. I was using `level` field in `users` table. A level `1` meant it was an admin. Hence, I created an `Admin` middleware to do what I had in mind. Here is how it can be done.

1. First of all, create a new middleware. It can be named anything you like  
`php artisan make:middleware Middlewarename`  

2. Open `app\Http\Middleware\Middlewarename.php`
3. Then paste following code in `handle()` function
```php
// ->level can be any field you like
if (\Auth::user()->level === 1) {
          return $next($request);
        } else {
            // redirect or throw error or anything you want;
        }
```
4. Then open `app\Http\Kernel.php` and add new middleware in `$routeMiddleware`  
`'admin' => \App\Http\Middleware\Middlewarename::class,`  

5. Then you can specify middleware in routes like below  
`Route::get('/route', [AnyController::class, 'route'])->middleware('Middlewarename');`  

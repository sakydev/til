---
author: "Saqib Razzaq"
title: "Laravel - create a user by default"
date: "2021-09-17"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

Sure, we can user Laravel's database seeding and `$faker` to create any number of fake users. Personally, I don't like to waste time fetching a new random user and their email address to continue my testing. I like have the same user created each time database is seeded. I do it like this.

1. Run below command to create a new seeder in `database/seeds` directory.  
```bash
php artisan make:seeder UserSeeder
```

2. In `run` method of `UserSeeder.php` paste following code
```php
$user = User::create([
          'name' => 'Saqib',
          'email' => 'saqib@saqib.com',
          'password' => Hash::make('password'),
          'level' => 1
        ]);
```
4. Finally, add below line in `run` method in `seeds\DatabaseSeeder.php`
`$this->call(UserSeeder::class);`

5. Then each time you run `php artisan db:seed`, this user will be created and you can keep building what matters to you :)
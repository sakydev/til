---
author: "Saqib Razzaq"
title: "How to test Registration and Login in Laravel"
date: "2021-11-02"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

I often work with Laravel APIs that require user registration and authentication. Of course, there is no stability in building applications without unit tests. Hence, I create following tests to ensure registration and login functions are working as expected. 

##### TestRegister.php
1. Run `php artisan make:test TestRegister`
2. Go to `tests\Feature` and open `TestRegister.php`
3. Use following test to make sure user registrations are working. Of course, this is a minimal example. But this should give you a good idea of how you can get started.  
```
public function testsRegistration()
  {
    $payload = [
      'name' => 'Jenny',
      'email' => 'jenny@test.com',
      'password' => 'password',
      'level' => '5',
    ];

    $this->json('post', '/api/register', $payload)
    ->assertStatus(201)
    ->assertJsonStructure([
      'data' => [
        'access_token',
        'token_type',
      ],
    ]);;
  }
```
You'll need to ajdust `$payload` variables according to what your API's `register` endpoint expects. You'll also need to adjust `assertJsonStructure` values based on what you are sending back as response.   

4. Use following test to make sure validation works when invalid parameters are given to `registration` route  
```
public function testsRegistrationValidation()
  {
    $this->json('post', '/api/register')
    ->assertStatus(422)
    ->assertJson([
      "error" => "error: incomplete input", 
      "status" => 422, 
      "data" => [
       "name" => [
          "The name field is required." 
        ], 
        "email" => [
          "The email field is required." 
        ], 
        "password" => [
          "The password field is required." 
        ] 
      ] 
    ]);
  }
```
##### TestLogin.php
1. Run `php artisan make:test TestLogin` a
2. Go to `tests\Feature` and open `TestRegister.php`
3. You can use following two tests to ensure user can login and also that validation is working as expected.  
```
public function testsUserLogin()
  {
    $user = factory(User::class)->create([
      'email' => 'arya@wall.com',
      'password' => bcrypt('password'),
    ]);

    $payload = ['email' => 'arya@wall.com', 'password' => 'password'];

    $this->json('POST', 'api/login', $payload)
    ->assertStatus(200)
    ->assertJsonStructure([
      'data' => [
        'access_token',
        'token_type',
      ],
    ]);
  }

  public function testsUserLoginValidation()
  {
    $this->json('POST', 'api/login')
    ->assertStatus(422)
    ->assertJson([
      'message' => 'Invalid login details',
    ]);
  }
```

### How to use Refresh database in Laravel PHPUnit Tests

A Laravel project ideally has many tests depending on the size of the project. We don't want one test's results to impact others. This is where `RefreshDatabase` trait comes in handy. It resets database after each test to make sure you get the clean slate for your next test. You can use it like this.

1. First, paste this at top of your test file
`use Illuminate\Foundation\Testing\RefreshDatabase;`

2. Then right after opening `{` of your test class, paste following
`use RefreshDatabase;`

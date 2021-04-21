### How to fix "key is too long" error in Laravel

If you are using sublime text run:
`Ctrl + P: AppServiceProvider.php`

Then at start of file paste
`use Illuminate\Support\Facades\Schema;`

Paste following code in boot() function
`Schema::defaultStringLength(191);`
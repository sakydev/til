### How to create and use Seeders in Laravel

1. Create a seeder `php artisan make:seeder seederName`
2. This creates a file `seederName` in `database/seeds`
3. You can use a model or default database class. I'll show you both examples
4. To use an existing model, try this approach 
```
// assumes you've already added "use App\User" and "use Illuminate\Support\Facades\Hash;" at top of your file
$user = User::create([
          'name' => 'Saqib',
          'email' => 'saqib@saqib.com',
          'password' => Hash::make('password'),
          'level' => 1
        ]);
```
5. If you don't have a model and want to run database inserts, try something like this
```
DB::table('users')->insert([
        'name' => 'Jon Snow',
        'email' => 'saqib@test.com',
        'password' => Hash::make('password')
      ]);
```

6. Run `php artisan db:seed` or `php artisan migrate:fresh --seed` to run seeders

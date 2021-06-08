### How to setup token API auth with Sanctum in Laravel

Read about [Laravel Sanctum](https://laravel.com/docs/8.x/sanctum)

1. Create your laravel project  
`composer create-project --prefer-dist laravel/laravel my-laravel-blog-api`
2. Move into project directory and then install Sanctum  
`composer require laravel/sanctum`
3. Now let's publish migrations and configuration files  
`php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"`
4. Run database migrations  
`php artisan migrate`
5. Make sure your `User` model looks like this 
```
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;
}
```
6. Make an authentication / user controller. Let's use `AuthenticationController` for this
`php artisan make:controller AuthenticationController`
7. Then add following code in this controller  
```
se Illuminate\Support\Facades\Hash;

public function register(Request $request)
{
$validatedData = $request->validate([
'name' => 'required|string|max:255',
                   'email' => 'required|string|email|max:255|unique:users',
                   'password' => 'required|string|min:8',
]);

      $user = User::create([
              'name' => $validatedData['name'],
                   'email' => $validatedData['email'],
                   'password' => Hash::make($validatedData['password']),
       ]);

$token = $user->createToken('auth_token')->plainTextToken;

return response()->json([
              'access_token' => $token,
                   'token_type' => 'Bearer',
]);
}
```
8. First, we validate the incoming request to make sure all required variables are present. Then we persist the supplied details into the database. Once a user has been created, we create a new personal access token for them using the createToken() method and give the token a name of auth_token. Because createToken() will return an instance of Laravel\Sanctum\NewAccessToken, we call the plainTextTokenproperty on the instance to access the plain-text value of the token. Finally, we return a JSON response containing the generated token as well as the type of the token.  
9. Then add `login` method to your controller. It should look like this
```
use App\Models\User;
use Illuminate\Support\Facades\Auth;

public function login(Request $request)
{
if (!Auth::attempt($request->only('email', 'password'))) {
return response()->json([
'message' => 'Invalid login details'
           ], 401);
       }

$user = User::where('email', $request['email'])->firstOrFail();

$token = $user->createToken('auth_token')->plainTextToken;

return response()->json([
           'access_token' => $token,
           'token_type' => 'Bearer',
]);
}
```
10. Add following two routes to allow registrations and login
```
Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);
```

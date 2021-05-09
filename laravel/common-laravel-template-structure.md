### The common Laravel template structure

First, create a file that defines the structure of your page

**layout.blade.php**
```
@include('includes.header')

@yield('content')

@include('includes.footer')
```

Then create files that yield content

**index.blade.php**

```
@extends('common_template')

@section('content')
    {{$data['title']}}
@endsection
```
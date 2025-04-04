---
author: "Saqib Razzaq"
title: "The common Laravel template structure"
date: "2021-10-17"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

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
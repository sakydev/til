---
author: "Saqib Razzaq"
title: "Laravel - manually handle HTTP exceptions"
date: "2021-11-02"
tags: ["php", "laravel"]
ShowToc: true
TocOpen: true
---

Laravel automatically handles HTTP exceptions and throws errors / redirects as it sees fit. Sometimes, this isn't an ideal behaviour. I was building an API and wanted to display custom messages for missing routes, forbidden and other errors. This can be done like this

1. Open *app\Exceptions\Handler.php*
2. If you want to handle missing models, paste following snippet in *render* method  

```php
if ($exception instanceof ModelNotFoundException) {
        return response()->json([
          'error' => 'Model not found'
        ], 404);
      }
```

3. If you'd like to handle other *HTTP* exceptions, paste the following snippet instead  
```php
if ($this->isHttpException($exception)) {
        switch ($exception->getStatusCode()) {

          // not authorized
          case '403':
          return \Response::json([
              'error' => 'You are not allowed to access this'
            ], 403);
          break;

          // not found
          case '404':
            return \Response::json([
              'error' => 'Resource not found'
            ], 404);
          break;

          // internal error
          case '500':
            return \Response::json([
                'error' => 'Something went terribly wrong'
              ], 500);
          break;

          default:
            return $this->renderHttpException($exception);
          break;
        }
      }
```

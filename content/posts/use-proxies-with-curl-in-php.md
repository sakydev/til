---
author: "Saqib Razzaq"
title: "How to use proxies with CURL in PHP"
date: "2019-07-17"
tags: ["php"]
ShowToc: true
TocOpen: true
---

If you are dealing with requesting images or data from other websites and you are getting blocked, you must start using proxies. Here are the fields that you can start sending with CURL

```php
curl_setopt($ch, CURLOPT_PROXY, $proxy);
curl_setopt($ch, CURLOPT_PROXYPORT, $port);

// if your proxy service requires authentication
$autentication = 'user:pass';
curl_setopt($ch, CURLOPT_PROXYUSERPWD, $autentication);
curl_setopt($ch, CURLOPT_PROXYTYPE, 'HTTP');
curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, 1);
```
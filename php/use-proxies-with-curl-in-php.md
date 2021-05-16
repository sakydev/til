### How to use proxies with CURL in PHP

If you are dealing with requesting images or data from other websites and you are getting blocked, you must start using proxies. Here are the fields that you can start sending with CURL

```
curl_setopt($ch, CURLOPT_PROXY, $proxy);
curl_setopt($ch, CURLOPT_PROXYPORT, $port);

// if your proxy service requires authentication
$autentication = 'user:pass';
curl_setopt($ch, CURLOPT_PROXYUSERPWD, $autentication);
curl_setopt($ch, CURLOPT_PROXYTYPE, 'HTTP');
curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, 1);
```
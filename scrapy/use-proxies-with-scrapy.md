### How to use proxies with Scrapy

There are two main ways to use proxies in Scrapy. You can either use it per request basis or use it with every scrapy outgoing request. 

**How to use proxy with a single request**

```
proxy = 'proxy_here'
return Request(url=url, callback=self.parse, meta={"proxy": proxy})
```

**How to use proxy with every request**
Go to to `middlewares.py` and update `process_request` method and paste following code

```
proxy = 'proxy_here'
request.meta['proxy'] = proxy
```

### How to run a function when Scrapy spider closes

Scrapy spider can close unexpectedly for many reasons. If you'd like to notify yourself or do anything whenever a spider closes (expectedly or unexpectedly)

- Create a function named anything e.g crawlFinished()
- Then paste `self.crawlFinish()` at the bottom of closed() function
- Now your function will be executed each time crawler exits
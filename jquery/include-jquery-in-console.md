### How to include jQuery in console

jQuery as we know comes loaded with most websites today. However, if there is a case when you'd like to run some experiments on website using jQuery but it isn't being load by default, you can run following command

```
var jqry = document.createElement('script');

jqry.src = "[https://code.jquery.com/jquery-3.3.1.min.js";](https://code.jquery.com/jquery-3.3.1.min.js)

document.getElementsByTagName('head')\[0\].appendChild(jqry);

jQuery.noConflict();
```
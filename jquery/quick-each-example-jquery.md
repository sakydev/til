### Quick each loop example in jQuery

$.each iterates over all elements specified and performs your code

Iterate over a list
```
$.each(list, function(key, field) {
    // something here
});
```

Find an element across the page and iterate over each
```
$(document).find('item').each(function(item, object) {
    // something here
});
```
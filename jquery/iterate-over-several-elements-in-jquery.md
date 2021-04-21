### How to iterate over several elements in jQuery

```
// iterate over a list
$.each(list, function(key, field) {
    // something here
});

// find an element across the page and iterate over each
$(document).find('item').each(function(item, object) {
    // something here
});
```
### How to send an Ajax request in jQuery

This is a boilerplate to be used for sending Ajax requests

```
$.ajax({
  url: "http://google.com",
  type: "post",
  dataType: "json",
  data: {name: item, value: value},
  success: function (response) {
    // do somethinig here
  },
  error: function(jqXHR, textStatus, errorThrown) {
    console.log(textStatus, errorThrown);
  }
});
```
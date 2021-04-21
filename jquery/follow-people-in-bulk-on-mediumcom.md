### How to follow people in bulk on Medium.com using jQuery

This is one of the tricks on Medium.com that seems to work pretty well. Please use on your own risk.

- Open Medium.com
- Find a user with lots of followers
- Click on link to view those followers
- Then right click + inspect
- First include jQuery

```
var jqry = document.createElement('script');
jqry.src = "https://code.jquery.com/jquery-3.3.1.min.js";
document.getElementsByTagName('head')[0].appendChild(jqry);
jQuery.noConflict();
```

Then run the following snippet to follow. It is best practice to not follow more than 120 people per day.

```
$('.js-followButton').each(function(index, item) {
  $(item).trigger("click");
  console.log('Followed ' + index + '/ 120');
  if (index > 100) {
      return false;
  }
});
```
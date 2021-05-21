### How to make an article eyes friendly with jQuery

I often encounter this case where I land on a website that has something I'd really like to read. However, the white text on black background and 10px font size makes me want to throw up. Hence, I'm leaving this tiny piece here to fix that situation.

Once you run this piece of code, it will do following things.

- Increase website font size
- Change background color to white
- Change text color to black

If website doesn't have jQuery, first run this

```
var jqry = document.createElement('script');
jqry.src = "https://code.jquery.com/jquery-3.3.1.min.js";
document.getElementsByTagName('head')[0].appendChild(jqry);
```

Then run this

```
$('p').css({
   'font-size' : '25px',
   'color' : 'black',
   'background-color' : 'white'
});
$('body').css('background', 'white');
```
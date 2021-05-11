Jinja If and For Loops

**If statement**
```
{% if True %}
  yay
{% endif %}
```

**For Loops**
For loops work like Python's for loop. Here is an example.
`
{% for user in users %}
  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
`
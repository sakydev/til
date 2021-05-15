### How to handle multiple endpoints in same function in Flask

You can execute same code with a conditional if you want multiple endpoints hiting the same functions. This is awesome because it allows you to reduce code duplication and the same block of code can do multiple things with minor changes.

Let's say you want to diplay a page on following two urls

`site.com/blog/page` and `site.com/page`

```
@app.route('/blog/<slug>', endpoint='post')
@app.route('/<slug>', endpoint='page')
def post(slug):
	post = getPost(slug)
	if request.endpoint == 'post':
		title = post['title']
  elif request.endpoint == 'page':
  	title = 'This is a page'
	return render_template('post.html', post=post, title=title)
```
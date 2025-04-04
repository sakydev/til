---
author: "Saqib Razzaq"
title: "How to filter and delete Google Chrome history items with Python"
date: "2021-06-11"
tags: ["python", "google-chrome"]
ShowToc: true
TocOpen: true
---

The following snippet can be used for filtering out URLs that where keywords match title or url. They are then deleted from history saving you lots of time that you'd otherwise spend manually filtering and deleting.

Google Chrome must be closed before running this script.
```python
import sqlite3, webbrowser

def cleanChrome():
	con = sqlite3.connect('C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')

	cursor = con.cursor()
	cursor.execute("select id, url, title from urls")
	urls = cursor.fetchall()

	# keywords that you'd like to detect and delete
	# it looks for these keywords in page title and urls
	keywords = []

	total = len(urls)
	done = 0
	deleted = 0
	pendingIds = []

	for url in urls:
		jenny.output(f'Processing {done} / {total} urls [deleted: {deleted}]')

		uid = url[0]
		link = url[1].lower()
		title = url[2].lower()

		for keyword in keywords:
			if keyword in link or keyword in title:
				jenny.output(f'{keyword} matched, deleting..')
				pendingIds.append((uid,))
				deleted += 1

		done += 1

	query = 'DELETE FROM urls WHERE id=?'
	cursor.executemany(query, pendingIds)
	con.commit()
```
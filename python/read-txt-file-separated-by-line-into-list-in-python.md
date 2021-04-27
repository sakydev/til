### How to read txt file separated by line as list in Python

In a web crawling project of mine I had to read proxies from a txt file. Each proxy was on a new line. I used following code to read them as list.

`proxies = [line.rstrip('\n') for line in open(directory + '/proxies_v2.txt')]`

Additionally, I shuffle them to make sure their order is random.

`random.shuffle(proxies)`


### How to start, stop and re-index in Sphinx

[Sphinx search](http://sphinxsearch.com/blog/2014/02/07/use-sphinx-with-mysql/) is a tool that extends Mysql's FULLTEXT search capabilities and brings faster more meaningful results in your control.

Start `/usr/bin/searchd`
Stop `/usr/bin/searchd --stop`
Find status `/usr/bin/searchd --status`
Re-index all data `sudo indexer --all`
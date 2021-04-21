### How to delete a huge directory in Linux

We generally run `rm -rf` and it deletes directories without any problem. However, if we encounter a situation where target directory contains thousands of files, this might take a very long time to finish. Hence, following command is what should be used instead.

`mkdir sample\_for\_rsync rsync -a --delete sample\_for\_rsync/  directory_todelete/`
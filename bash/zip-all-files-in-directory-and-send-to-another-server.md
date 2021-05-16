### How to ZIP all files in directory and send to another server

First install `zip` if not already install

Ubuntu `apt-get install zip`
Centos `yum install zip`

Then create a `file.sh` and paste following code

```
OUTFILE=outputfile.zip
INPUTDIR=inputdir
zip -R $OUTFILE $INPUTDIR
scp $OUTFILE usrename@outserver:/path/of/ $OUTFILE -i key.pem
```
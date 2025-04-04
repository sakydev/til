---
author: "Saqib Razzaq"
title: "How to ZIP all files in directory and send to another server"
date: "2021-11-11"
tags: ["bash", "linux"]
ShowToc: true
TocOpen: true
---

First install `zip` if not already install

Ubuntu `apt-get install zip`
Centos `yum install zip`

Then create a `file.sh` and paste following code

```bash
OUTFILE=outputfile.zip
INPUTDIR=inputdir
zip -R $OUTFILE $INPUTDIR
scp $OUTFILE usrename@outserver:/path/of/ $OUTFILE -i key.pem
```
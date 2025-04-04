---
author: "Saqib Razzaq"
title: "How to quickly login to MySQL using Bash"
date: "2021-11-11"
tags: ["bash", "linux", "mysql"]
ShowToc: true
TocOpen: true
---

I know this method isn't the most secure way. But when I'm working on personal projects, it gets annoying having to enter credentials every time. Hence, I put together this little script to quickly log me in. I create file mysql.sh with following contents

```bash
mysql -u username --password='password_here'
```
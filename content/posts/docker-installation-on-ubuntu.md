---
author: "Saqib Razzaq"
title: "How to install Docker on Ubuntu"
date: "2020-09-24"
tags: ["bash"]
ShowToc: true
TocOpen: true
---

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
sudo apt install docker-ce
sudo systemctl status docker
docker --version
```
---
author: "Saqib Razzaq"
title: "Docker Cheatsheet"
date: "2021-07-11"
description: "How to make things happen in Docker without banging your head"
tags: ["cheatsheets", "docker"]
ShowToc: true
TocOpen: true
---

Show images `docker images`

Show containers `docker ps`

Show running containers `docker ps -a`

Connect to a running container `docker exec -it container_id bash`

Start container `docker start container_id`

Stop container `docker stop container_id`

Remove Container `docker rm container_id`

Pull container `docker pull image_name`

Commit a container `docker commit -m "message" -a "Author" container_id username/repo_name`

Remove all containers `docker rm $(docker ps -a -q)`

Stop all containers `docker kill $(docker ps -q)`

Remove all docker images `docker rmi $(docker images -q)`

Publish an image
`docker login -u username`
`docker push username/docker-image-name`

Copy a file from host to container
`docker cp redis-commands.txt 858f0bebee7a:/data`
---
author: "Saqib Razzaq"
title: "Git Cheatsheet"
date: "2021-09-15"
description: "How to perform the basic Git actions"
tags: ["git", "cheatsheets"]
ShowToc: true
TocOpen: true
---

### Git Cheatsheet

- Get remote URL

`git remote -v`

- Set remote URL

`git remote set-url origin git@bitbucket.org:user/repo.git`

- Update remote branches list

`git remote update origin --prune`

- Delete local branch

`git branch -d branchname`

- Delete branch locally and remote

`git push origin --delete fix/authentication`

- Create branch from another

`git checkout -b newbranch sourcebranch`

- Soft reset (remove last commit)

`git reset --soft HEAD~1`

- Remove all local branches already merged into master (including dev)
```
git branch --merged master | grep -v '^[ *]*master$' | xargs git branch -d
```
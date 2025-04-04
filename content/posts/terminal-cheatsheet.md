---
author: "Saqib Razzaq"
title: "Terminal Cheatsheet"
date: "2020-12-11"
description: "x"
tags: ["bash", "cheatsheets"]
ShowToc: true
TocOpen: true
---

A list of common terminal shortcuts + most common cli programs in Linux

**terminal**

`ctrl + a` move to start of a line
`ctrl + e` move to end of a line
`Alt-f` Move the cursor forward by one word
`Alt-b`	Move the cursor backward by one word
`ctrl + u` Delete an entire line
`ctrl + k` Delete everything after cursor
`Ctrl + Shift + F` Find any text
`clear` or `ctrl + l` to clear terminal
`reset` clear everything and remove scroll
`cal` show calendar
`command; command2` for running multiple commands regardless of output
`command && command2` for running commands only when first is successful

`sed -i 's/old_text/new_text/g' path` find and replace text in a file

set title of a tab
1. first save this function into `~/.bashrc`
```
function set-title() {
  if [[ -z "$ORIG" ]]; then
    ORIG=$PS1
  fi
  TITLE="\[\e]2;$*\a\]"
  PS1=${ORIG}${TITLE}
}
```
2. then run `set-title yourtitle`


**ls**

`ls -l` for listing with details
`ls -R` recursive directory listing
`ls -a` show hidden files


**find**

**uname**

**wget**

**curl**

**find**

**cat**

`cat > filename` creates a new file
`cat filename1 filename2>filename3` joins two files (1 and 2) and stores the output of them in a new file (3)


**grep**

`grep word notepad.txt` search for word in a file
`grep -R "word" directory` search for a word across many files recursively
`history | grep word` find a command from history which contains a certain word

**diff**

`diff file1.ext file2.ext` compare contents of two files
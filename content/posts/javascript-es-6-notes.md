---
author: "Saqib Razzaq"
title: "JavaScript ES6 Notes"
date: "2020-08-03"
tags: ["javascript"]
ShowToc: true
TocOpen: true
---

**Def vars**
const = cannot redeclare, cannot changed value
let = can change value, cannot redeclare

let + const = if inside { } then it won't work outside

**Concatination**
- no need for + sign
- use backticks instead of quotes
- you can use single or double quotes inside backticks
- you can use variables inside of backticks like `My name is ${name}`

**Object Literals**
If you want to return an object you don't need to do following

```javascript
function getBook(name, author) {
  return {
    name: name,
    author: author
  }
}
```

If variable names are the same as the value you want to return, just use the variable instead like so

```javascript
function getBook(name, author) {
  return {
    name,
    author
  }
}
```

**Object deconstruction***
Instead of list.item you can select multiple items

```javascript
const list = {
  name: "Shopping list",
  items: ['cow', 'milk'],
  car: xli
}
```
``const {name, car} = list;``

^ That will give me both the values

**Arrow functions**
- function keyword is not needed
- () are always required, unless you have one param only
- {} can be removed if you want to return just one line

```javascript
const mylocation = (location) => {
  console.log(`My location is ${location}`)
}
```

**defalut parameters**
You can set values like php in func params

**New array functions**
- forEach
  ```javascript
    list = ['keyboard', 'mouse', 'laptop'];
    list.forEach((item) => {
        console.log(item);
    })
  ```



- map
  Map can copy a list and modify it to store into new array
  ```javascript
  list = ['keyboard', 'mouse', 'laptop'];
  newlist = list.map(item => () {
    return item + 'new';
  })
  ```

- filter
  Get an array with only certain items from another array
   ```javascript
  list = ['keyboard', 'mouse', 'laptop'];
  newlist = list.filter(item => () {
    return item == 'keyboard';
  })
  ```
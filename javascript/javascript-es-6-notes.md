### JavaScript ES6 Notes

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

```
function getBook(name, author) {
  return {
    name: name,
    author: author
  }
}
```

If variable names are the same as the value you want to return, just use the variable instead like so

```
function getBook(name, author) {
  return {
    name,
    author
  }
}
```

**Object deconstruction***
Instead of list.item you can select multiple items

```const list = {
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

```
const mylocation = (location) => {
  console.log(`My location is ${location}`)
}
```

**defalut parameters**
You can set values like php in func params

**New array functions**
- forEach
  ```
    list = ['keyboard', 'mouse', 'laptop'];
    list.forEach((item) => {
        console.log(item);
    })
  ```



- map
  Map can copy a list and modify it to store into new array
  ```
  list = ['keyboard', 'mouse', 'laptop'];
  newlist = list.map(item => () {
    return item + 'new';
  })
  ```

- filter
  Get an array with only certain items from another array
   ```
  list = ['keyboard', 'mouse', 'laptop'];
  newlist = list.filter(item => () {
    return item == 'keyboard';
  })
  ```
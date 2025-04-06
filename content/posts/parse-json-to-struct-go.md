---
author: "Saqib Razzaq"
title: "Parse JSON to Struct in Go"
date: "2025-04-06"
tags: ["go"]
---

Parsing JSON into a struct using json.Unmarshal is a fundamental task in Go when working with APIs or reading JSON files. The encoding/json package makes this process straightforward.

Let's say we receive the following JSON payload:
```json
{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

```
We can parse this JSON into a struct like this:
```go
package main

import (
	"encoding/json"
	"fmt"
)

type User struct {
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Email string `json:"email"`
}

func main() {
	jsonData := `{"name": "John Doe", "age": 30, "email": "johndoe@example.com"}`

	var user User
	err := json.Unmarshal([]byte(jsonData), &user)
	if err != nil {
		fmt.Println("Error parsing JSON:", err)
		return
	}

	fmt.Println("Parsed User Struct:", user)
}

```

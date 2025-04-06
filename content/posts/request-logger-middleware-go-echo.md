---
author: "Saqib Razzaq"
title: "Request Logger Middleware in Go Echo"
date: "2025-04-06"
tags: ["go", "echo"]
---

Middleware in Echo allows us to intercept requests before they reach handlers, making it a great place to add logging. Echo provides a built-in logging middleware (middleware.Logger()) but for more control, we can create a custom middleware:


```go
package main

import (
	"log"
	"time"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

// Custom logging middleware
func requestLogger(next echo.HandlerFunc) echo.HandlerFunc {
	return func(c echo.Context) error {
		start := time.Now()
		req := c.Request()

		log.Printf("Request: method=%s, path=%s, remote=%s", req.Method, req.URL.Path, req.RemoteAddr)

		err := next(c)

		res := c.Response()
		log.Printf("Response: status=%d, duration=%s", res.Status, time.Since(start))

		return err
	}
}

func main() {
	e := echo.New()

	// Use Echo's default logger middleware
	e.Use(middleware.Logger())

	// Use custom logging middleware
	e.Use(requestLogger)

	e.GET("/", func(c echo.Context) error {
		return c.String(200, "Hello, Echo!")
	})

	e.Start(":8080")
}

```
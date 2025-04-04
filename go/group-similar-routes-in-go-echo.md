## Group Similar Routes in Go Echo
Using Echo groups is a great way to organize routes, especially when dealing with versioning, middleware, or related endpoints. Instead of cluttering the main file with multiple routes, you can logically group them.

```go
package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()

	// Global middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// API versioning
	v1 := e.Group("/api/v1")

	// Group for user-related routes
	users := v1.Group("/users")
	users.GET("", getUsers)          // GET /api/v1/users
	users.POST("", createUser)       // POST /api/v1/users
	users.GET("/:id", getUserByID)   // GET /api/v1/users/:id

	// Group for admin routes with middleware
	admin := v1.Group("/admin", adminMiddleware)
	admin.GET("/dashboard", adminDashboard) // GET /api/v1/admin/dashboard

	e.Logger.Fatal(e.Start(":8080"))
}

// Handlers
func getUsers(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]string{"message": "List of users"})
}

func createUser(c echo.Context) error {
	return c.JSON(http.StatusCreated, map[string]string{"message": "User created"})
}

func getUserByID(c echo.Context) error {
	id := c.Param("id")
	return c.JSON(http.StatusOK, map[string]string{"message": "User ID: " + id})
}

func adminDashboard(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]string{"message": "Admin dashboard"})
}

// Middleware for admin routes
func adminMiddleware(next echo.HandlerFunc) echo.HandlerFunc {
	return func(c echo.Context) error {
		// Simulate an auth check
		if c.Request().Header.Get("Authorization") != "Bearer admin_token" {
			return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Unauthorized"})
		}
		return next(c)
	}
}

```

Custom validation in Echo using `ozzo-validation` makes input handling much cleaner and more structured. Instead of manually checking each field, you can define validation rules declaratively.

Let's say we need to validate a form submission where each field has attributes like label, type, and is_required.

```go
package form_requests

import (
	"fmt"
	"regexp"

	validation "github.com/go-ozzo/ozzo-validation/v4"
	"github.com/labstack/echo/v4"
)

// FieldRequest defines a single form field
type FieldRequest struct {
	Label      string `json:"label"`
	Type       string `json:"type"`
	IsRequired bool   `json:"is_required"`
}

// CreateFormFieldsRequest wraps multiple fields
type CreateFormFieldsRequest struct {
	Fields []FieldRequest `json:"fields"`
}

// BindAndValidate binds JSON data and runs validation
func (r *CreateFormFieldsRequest) BindAndValidate(c echo.Context) []string {
	if err := c.Bind(r); err != nil {
		return []string{"Invalid request payload"}
	}

	err := validation.ValidateStruct(r,
		validation.Field(&r.Fields, validation.Required.Error("Fields array is required"), validation.Each(
			validation.By(validateField),
		)),
	)

	return extractValidationErrors(err)
}

// validateField ensures each field meets the required rules
func validateField(value interface{}) error {
	field, ok := value.(FieldRequest)
	if !ok {
		return fmt.Errorf("invalid field format")
	}

	return validation.ValidateStruct(&field,
		validation.Field(&field.Label,
			validation.Required.Error("Label is required"),
			validation.Length(3, 50).Error("Label must be between 3 and 50 characters"),
			validation.Match(regexp.MustCompile(`^[a-zA-Z0-9_-]+$`)).Error("Label can only contain letters, numbers, underscores, and dashes"),
		),
		validation.Field(&field.Type,
			validation.Required.Error("Type is required"),
			validation.In("text", "number", "email", "date", "checkbox").Error("Invalid field type"),
		),
		validation.Field(&field.IsRequired, validation.Required.Error("IsRequired is required")),
	)
}

// extractValidationErrors formats errors into a slice of strings
func extractValidationErrors(err error) []string {
	if err == nil {
		return nil
	}
	var errors []string
	if ve, ok := err.(validation.Errors); ok {
		for _, e := range ve {
			errors = append(errors, e.Error())
		}
	}
	return errors
}
```

- Declarative Validation: Instead of manually checking fields, `ozzo-validation` provides a clean way to define rules.
- Custom Validation Function: `validateField()` ensures each field meets the required format and constraints.
- Consistent Error Handling: `extractValidationErrors()` collects and formats validation errors into a slice for easier debugging and response handling.


### How to copy a table with schema, indexes and data

First, copy the table with indexes

`CREATE TABLE new_name LIKE table_to_copy;`

Then copy the data by running

`INSERT INTO new_name SELECT * FROM table_to_copy;`
### How to find duplicates with counts in MySQL

`SELECT field, COUNT(*) c FROM table GROUP BY field HAVING c > 1;`
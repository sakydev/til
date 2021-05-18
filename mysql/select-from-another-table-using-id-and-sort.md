### How to select from another table using ID in MySQL

```
SELECT main.id,other,fields, Count(*) AS Count FROM main_table AS main INNER JOIN second_table AS second ON main.id = second.id where main.some_field = vendor.field Order By Count;
```
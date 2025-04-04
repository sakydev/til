---
author: "Saqib Razzaq"
title: "MySQL Cheatsheet"
date: "2021-09-01"
description: "How to create and destroy things in MySQL"
tags: ["mysql", "cheatsheets"]
ShowToc: true
TocOpen: true
---

#### copy a table with schema, indexes and data

First, copy the table with indexes

```sql
CREATE TABLE new_name LIKE table_to_copy;
```

Then copy the data by running

```sql
INSERT INTO new_name SELECT * FROM table_to_copy;
```

#### create BTREE Indexes

```sql
CREATE INDEX index_name ON table_name (column1, column2, ...);
```

#### create FULLTEXT indexes

```sql
ALTER TABLE `TableName` ADD FULLTEXT INDEX `IndexName` (`ColumnName`);
```

#### create new user and give all privilages

```sql

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';

```

#### create or drop multiple indexes in same query

Create multiple indexes

```sql
ALTER TABLE tbl ADD INDEX index_name_a(field_a,field_b), ADD INDEX index_name_b(field_a,field_b);
```

Drop multiple indexes

```sql
ALTER TABLE mytable DROP INDEX ndx1, DROP INDEX ndx2, DROP INDEX ndx3 ;
```

#### find duplicates with counts

```sql
SELECT field, COUNT(*) c FROM table GROUP BY field HAVING c > 1;
```

#### import small and large files

small files
```sql
mysql -u user -p -f db < file.sql
```

large File
```sql
nohup mysql -u user -p -f db < file.sql &
```

#### output a select query in a text file

```sql
SELECT field FROM table INTO OUTFILE '/tmp/orders.txt'
```

#### select from another table using ID

```sql
SELECT main.id,other,fields, Count(*) AS Count FROM main_table AS main INNER JOIN second_table AS second ON main.id = second.id where main.some_field = vendor.field Order By Count;
```

#### select all tables with specific engine

```sql
SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE engine = 'InnoDB';
```

#### update a datetime field by converting timestamp from another field in same table

```sql
UPDATE table_name SET field_to_update=(DATE_FORMAT(FROM_UNIXTIME(`timestamp_field`), '%Y-%m-%d %H:%i:%s'));
```

#### update table with matches from another

```sql
UPDATE table_A tmpA INNER JOIN table_B tmpB ON tmpA.field = tmpA.field SET tmpA.fielda = tmpB.fielda, tmpA.fieldb = tmpB.fieldb where condition;
```
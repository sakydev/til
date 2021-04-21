### How to create or drop multiple MySQL indexes in same query

**Create multiple indexes**

`ALTER TABLE tbl ADD INDEX index_name_a(field_a,field_b), ADD INDEX index_name_b(field_a,field_b);`

**Drop multiple indexes**

`ALTER TABLE mytable DROP INDEX ndx1, DROP INDEX ndx2, DROP INDEX ndx3 ;`
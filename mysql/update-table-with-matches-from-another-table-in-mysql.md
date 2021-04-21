### How to update table with matches from another in MySQL

`UPDATE table_A tmpA INNER JOIN table_B tmpB ON tmpA.field = tmpA.field SET tmpA.fielda = tmpB.fielda, tmpA.fieldb = tmpB.fieldb where condition;`
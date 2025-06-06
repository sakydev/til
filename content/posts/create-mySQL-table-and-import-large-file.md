---
author: "Saqib Razzaq"
title: "How to Import All CSV Files in Directory in MySQL via Bash"
date: "2021-11-11"
description: "This script iterates over a directory and imports each CSV file into specified MySQL table."
tags: ["bash", "linux", "mysql"]
ShowToc: true
TocOpen: true
---

1. Create a file `import.sh` and make it executable
2. Paste following code in file

```bash
mysqluser='root'
mysqlpass='password'
mysqldb='database_name'
tablename='mysql_table_name'
DIRECTORY='input_directory'

for csv in $DIRECTORY/*.csv;
do
 echo "Loading $csv"
 mysql -u $mysqluser --password=$mysqlpass -D $mysqldb -e "LOAD DATA INFILE '$csv' IGNORE INTO TABLE $tablename FIELDS TERMINATED BY '\t' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
done
```
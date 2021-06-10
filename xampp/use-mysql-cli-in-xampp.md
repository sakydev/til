### How to use Mysql CLI in xampp

I love working with Linux and CLI. It helps boost speed to a great extent and it feels like Windows' xampp often limits that because I mostly tend to avoid using command line. I'm finally writing this to change that and be equally as proficient on Windows. 

MySQL Bin Location `{$xampp}/mysql/bin/mysql.exe`
Mysqldump Bin Location `{$xampp}/mysql/bin/mysqldump.exe`

#### How to import and export files
- **Import files**
1. Login to mysql by running `{$xampp}/mysql/bin/mysql.exe -u user -p`
2. Select database by running `use {$database_name}`
3. Import a file by running `source {$path_to_file.sql}`

- **Export files**
Export a table by running   
`mysql\bin\mysqldump.exe -u root -p database_name table > table.sql`
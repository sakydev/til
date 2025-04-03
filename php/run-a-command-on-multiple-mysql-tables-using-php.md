### How to run a command on multiple MySQL tables using PHP

```php

$query = "alter table {table} drop column columnName;";
$tables = array('tableA', 'tableB');
foreach ($tables as $key => $source) {
    $currentQuery = str_replace('{table}', $source, $query);
    DB::query($currentQuery);
}

```
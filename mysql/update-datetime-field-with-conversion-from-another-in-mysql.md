### How to update a datetime field by converting timestamp from another field in same table

`UPDATE table_name SET field_to_update=(DATE_FORMAT(FROM_UNIXTIME(`timestamp_field`), '%Y-%m-%d %H:%i:%s'));`
### How to count files per day in a directory in Linux

`find directory -type f -printf '%TY-%Tm-%Td\n' | sort | uniq -c`
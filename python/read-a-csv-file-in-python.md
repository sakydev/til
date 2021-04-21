### How to read a CSV file in python

```
with open(path, mode='r') as csvFile:
  reader = csv.DictReader(csvFile)
  lineCount = 0
  for row in reader:
    if lineCount > 0:
      # do stuff here
    lineCount += 1
```
### How to extract numbers from a string

```
def extractNumbers(self, string):
  return ''.join(re.findall(r"[-+]?\d*\.\d+|\d+", string))
```
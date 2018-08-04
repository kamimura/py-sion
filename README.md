# py-sion

[SION](https://dankogai.github.io/SION/) deserializer/serializer for Python.

## Synopsis

stream

text
```python
import sion
#...
with open('spam.sion') as f:
    obj = sion.load(f)
with open('eggs.sion', 'w') as f:     
    sion.dump(obj, f)
#...
```
bytes
```python
import sion
from urllib.request import urlopen
#...
with urlopen(ham) as res:
    obj = load(res)
#...
```

string
```python
import sion
#...
spam = sion.loads('sion data')
eggs = sion.dumps(spam)
#...
```

[Here](http://sitekamimura.blogspot.com/search/label/SION) are some other examples.

## Installation

```sh
$ pip3 install sion
```

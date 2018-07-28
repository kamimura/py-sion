# py-sion

[SION](https://dankogai.github.io/SION/) deserializer/serializer for Python.

## Synopsis

```python
import sion
\#...
with open('spam.sion') as f:
     obj = sion.load(f)
with open('eggs.sion', 'w') as f:     
     sion.dump(obj, f)
\#...
```

## Usage

```sh
$ pip3 install sion
```
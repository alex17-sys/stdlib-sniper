# Named Tuple Usage

Zero-dependency Python snippets for using collections.namedtuple in the standard library.

## Simple

### 🧩 Create and use a namedtuple

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p)  # Point(x=10, y=20)
print(p.x)  # 10
print(p.y)  # 20
```

📂 Create a named tuple for readable, immutable records

🏷️ Tags: namedtuple, tuple, create, access, data-structures
📝 Notes:
- namedtuple creates a lightweight, immutable class
- Fields are accessible by name and index

### 🧩 Access by index and unpacking

```python
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p[0])  # 10
x, y = p
print(x, y)  # 10 20
```

📂 Access namedtuple fields by index or unpacking

🏷️ Tags: namedtuple, tuple, unpacking, index, data-structures
📝 Notes:
- Behaves like a regular tuple for unpacking and indexing

## Complex

### 🧩 Namedtuple with defaults (Python 3.7+)

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "NYC")
print(p1)  # Person(name='Alice', age=30, city='Unknown')
print(p2)  # Person(name='Bob', age=25, city='NYC')
```

📂 Use defaults for missing fields in namedtuple

🏷️ Tags: namedtuple, defaults, tuple, data-structures
📝 Notes:
- Defaults are available in Python 3.7+

### 🧩 Namedtuple as dictionary (._asdict())

```python
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
d = p._asdict()
print(d)  # {'x': 10, 'y': 20}
```

📂 Convert namedtuple to an ordered dict

🏷️ Tags: namedtuple, dict, asdict, data-structures
📝 Notes:
- _asdict() returns an OrderedDict of fields

### 🧩 Replace fields with ._replace()

```python
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p2 = p._replace(x=99)
print(p2)  # Point(x=99, y=20)
```

📂 Create a new namedtuple with one or more fields changed

🏷️ Tags: namedtuple, replace, immutable, data-structures
📝 Notes:
- namedtuples are immutable; _replace() returns a new instance

### 🧩 Nested namedtuples and practical usage

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Rectangle = namedtuple("Rectangle", ["top_left", "bottom_right"])
rect = Rectangle(Point(0, 0), Point(10, 10))
print(rect.top_left.x, rect.bottom_right.y)  # 0 10
```

📂 Use namedtuples for nested, structured data

🏷️ Tags: namedtuple, nested, structure, data-structures
📝 Notes:
- Useful for geometric, config, or record-like data

## 🔗 Cross Reference

- **Reference**: See [📂 Tuple Unpacking](tuple_unpacking.md)

## 🏷️ Tags

`namedtuple`, `tuple`, `defaults`, `asdict`, `replace`, `nested`, `data-structures`

## 📝 Notes
- namedtuple is a memory-efficient alternative to classes for simple records
- Immutability makes them safe for use as dict keys or set elements

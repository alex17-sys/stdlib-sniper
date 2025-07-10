---
title: Named Tuple Usage
description: Zero-dependency Python snippets for using collections.namedtuple in the standard library.
keywords: access, asdict, create, data-structures, defaults, dict, immutable, index, namedtuple, nested, replace, structure, tuple, unpacking
---

# Named Tuple Usage

Zero-dependency Python snippets for using collections.namedtuple in the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Create and use a namedtuple

`namedtuple` `tuple` `create` `access` `data-structures`

Create a named tuple for readable, immutable records

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p)  # Point(x=10, y=20)
print(p.x)  # 10
print(p.y)  # 20
```

!!! note "Notes"
    - namedtuple creates a lightweight, immutable class
    - Fields are accessible by name and index

<hr class="snippet-divider">

### Access by index and unpacking

`namedtuple` `tuple` `unpacking` `index` `data-structures`

Access namedtuple fields by index or unpacking

```python
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p[0])  # 10
x, y = p
print(x, y)  # 10 20
```

!!! note "Notes"
    - Behaves like a regular tuple for unpacking and indexing

<hr class="snippet-divider">

## Complex

###  Namedtuple with defaults (Python 3.7+)

`namedtuple` `defaults` `tuple` `data-structures`

Use defaults for missing fields in namedtuple

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "NYC")
print(p1)  # Person(name='Alice', age=30, city='Unknown')
print(p2)  # Person(name='Bob', age=25, city='NYC')
```

!!! note "Notes"
    - Defaults are available in Python 3.7+

<hr class="snippet-divider">

### Namedtuple as dictionary (._asdict())

`namedtuple` `dict` `asdict` `data-structures`

Convert namedtuple to an ordered dict

```python
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
d = p._asdict()
print(d)  # {'x': 10, 'y': 20}
```

!!! note "Notes"
    - _asdict() returns an OrderedDict of fields

<hr class="snippet-divider">

### Replace fields with ._replace()

`namedtuple` `replace` `immutable` `data-structures`

Create a new namedtuple with one or more fields changed

```python
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p2 = p._replace(x=99)
print(p2)  # Point(x=99, y=20)
```

!!! note "Notes"
    - namedtuples are immutable; _replace() returns a new instance

<hr class="snippet-divider">

### Nested namedtuples and practical usage

`namedtuple` `nested` `structure` `data-structures`

Use namedtuples for nested, structured data

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Rectangle = namedtuple("Rectangle", ["top_left", "bottom_right"])
rect = Rectangle(Point(0, 0), Point(10, 10))
print(rect.top_left.x, rect.bottom_right.y)  # 0 10
```

!!! note "Notes"
    - Useful for geometric, config, or record-like data

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Tuple Unpacking](tuple_unpacking.md)

## 🏷️ Tags

`namedtuple`, `tuple`, `defaults`, `asdict`, `replace`, `nested`, `data-structures`

## 📝 Notes
- namedtuple is a memory-efficient alternative to classes for simple records
- Immutability makes them safe for use as dict keys or set elements

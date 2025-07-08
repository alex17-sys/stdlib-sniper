# Create and Use Tuples

Zero-dependency Python snippets for creating and using tuples with the standard library.

## Simple

### 🧩 Create a tuple

```python
# Empty tuple
t1 = ()
print(t1)  # ()

# Tuple with elements
t2 = (1, 2, 3)
print(t2)  # (1, 2, 3)

# Tuple without parentheses
t3 = 1, 2, 3
print(t3)  # (1, 2, 3)

# Single-element tuple (note the comma)
t4 = (42,)
print(t4)  # (42,)
```

📂 Create tuples in various ways

🏷️ Tags: tuple, create, immutable, data-structures
📝 Notes:
- Tuples are immutable sequences
- Parentheses are optional except for empty or single-element tuples

### 🧩 Tuple from iterable

```python
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)  # (1, 2, 3)

s = "abc"
tup2 = tuple(s)
print(tup2)  # ('a', 'b', 'c')
```

📂 Convert list or string to tuple

🏷️ Tags: tuple, from-list, from-string, data-structures
📝 Notes:
- tuple() constructor works with any iterable

## Complex

### 🧩 Tuple packing and unpacking

```python
# Packing
coords = 10, 20
print(coords)  # (10, 20)

# Unpacking
x, y = coords
print(x, y)  # 10 20

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5
```

📂 Pack and unpack tuples, including extended unpacking

🏷️ Tags: tuple, packing, unpacking, extended, data-structures
📝 Notes:
- Unpacking works with any iterable
- Extended unpacking (with *) is available in Python 3

### 🧩 Tuple immutability and usage

```python
tup = (1, 2, 3)
# tup[0] = 99  # Raises TypeError: 'tuple' object does not support item assignment

# Tuples can be used as dictionary keys
my_dict = {(1, 2): "point"}
print(my_dict[(1, 2)])  # 'point'
```

📂 Tuples are immutable and hashable

🏷️ Tags: tuple, immutable, hashable, dict-key, data-structures
📝 Notes:
- Tuples cannot be changed after creation
- Useful as keys in dictionaries or elements in sets

### 🧩 Nested tuples and tuple of tuples

```python
matrix = ((1, 2), (3, 4), (5, 6))
for row in matrix:
    print(row)
# (1, 2)
# (3, 4)
# (5, 6)
```

📂 Use tuples for fixed-size, nested data

🏷️ Tags: tuple, nested, matrix, data-structures
📝 Notes:
- Tuples can contain other tuples or any objects
- Useful for representing matrices, coordinates, etc.

## 🔗 Cross Reference

- **Reference**: See [📂 Tuple Unpacking](tuple_unpacking.md)

## 🏷️ Tags

`tuple`, `create`, `immutable`, `packing`, `unpacking`, `hashable`, `data-structures`

## 📝 Notes
- Use tuples for fixed-size, immutable collections
- Tuples are more memory-efficient than lists for small, constant data

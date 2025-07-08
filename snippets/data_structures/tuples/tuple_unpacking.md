# Tuple Unpacking

Zero-dependency Python snippets for unpacking tuples using the standard library.

## Simple

### 🧩 Basic tuple unpacking

```python
tup = (10, 20)
x, y = tup
print(x)  # 10
print(y)  # 20
```

📂 Assign tuple elements to variables

🏷️ Tags: tuple, unpacking, assignment, data-structures
📝 Notes:
- Number of variables must match tuple length

### 🧩 Unpacking in for loops

```python
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, char in pairs:
    print(num, char)
# 1 a
# 2 b
# 3 c
```

📂 Unpack tuple elements directly in loops

🏷️ Tags: tuple, unpacking, loop, iteration, data-structures
📝 Notes:
- Works with any iterable of tuples

## Complex

### 🧩 Extended unpacking (Python 3+)

```python
tup = (1, 2, 3, 4, 5)
first, *middle, last = tup
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5

# Ignore values with _
x, _, z = (10, 99, 30)
print(x, z)  # 10 30
```

📂 Use * to capture multiple elements, ignore with _

🏷️ Tags: tuple, extended-unpacking, star, ignore, data-structures
📝 Notes:
- * can be used in any position except the first or last
- _ is a common convention for unused values

### 🧩 Swapping variables with tuple unpacking

```python
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1
```

📂 Swap variables without a temporary variable

🏷️ Tags: tuple, swap, unpacking, data-structures
📝 Notes:
- Pythonic way to swap values

### 🧩 Nested tuple unpacking

```python
nested = (1, (2, 3))
a, (b, c) = nested
print(a)  # 1
print(b)  # 2
print(c)  # 3
```

📂 Unpack nested tuples in a single statement

🏷️ Tags: tuple, nested, unpacking, data-structures
📝 Notes:
- Structure of variables must match tuple nesting

### 🧩 Unpacking with * in function arguments

```python
def add(x, y, z):
    return x + y + z


args = (1, 2, 3)
result = add(*args)
print(result)  # 6
```

📂 Use * to unpack tuple into function arguments

🏷️ Tags: tuple, unpacking, function, arguments, data-structures
📝 Notes:
- *args unpacks tuple elements as positional arguments

## 🔗 Cross Reference

- **Reference**: See [📂 Create and Use Tuples](tuple_create.md)
- **Reference**: See [📂 Named Tuple Usage](namedtuple_usage.md)

## 🏷️ Tags

`tuple`, `unpacking`, `extended-unpacking`, `swap`, `nested`, `function-args`, `data-structures`

## 📝 Notes
- Tuple unpacking is a powerful and Pythonic feature
- Use * for flexible unpacking and function calls

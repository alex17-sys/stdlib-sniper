---
title: Tuple Unpacking
description: Zero-dependency Python snippets for unpacking tuples using the standard library.
keywords: arguments, assignment, data-structures, extended-unpacking, function, ignore, iteration, loop, nested, star, swap, tuple, unpacking
---

# Tuple Unpacking

Zero-dependency Python snippets for unpacking tuples using the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Basic tuple unpacking

`tuple` `unpacking` `assignment` `data-structures`

Assign tuple elements to variables

```python
tup = (10, 20)
x, y = tup
print(x)  # 10
print(y)  # 20
```

!!! note "Notes"
    - Number of variables must match tuple length

<hr class="snippet-divider">

### Unpacking in for loops

`tuple` `unpacking` `loop` `iteration` `data-structures`

Unpack tuple elements directly in loops

```python
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, char in pairs:
    print(num, char)
# 1 a
# 2 b
# 3 c
```

!!! note "Notes"
    - Works with any iterable of tuples

<hr class="snippet-divider">

## Complex

###  Extended unpacking (Python 3+)

`tuple` `extended-unpacking` `star` `ignore` `data-structures`

Use * to capture multiple elements, ignore with _

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

!!! note "Notes"
    - * can be used in any position except the first or last
    - _ is a common convention for unused values

<hr class="snippet-divider">

### Swapping variables with tuple unpacking

`tuple` `swap` `unpacking` `data-structures`

Swap variables without a temporary variable

```python
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1
```

!!! note "Notes"
    - Pythonic way to swap values

<hr class="snippet-divider">

### Nested tuple unpacking

`tuple` `nested` `unpacking` `data-structures`

Unpack nested tuples in a single statement

```python
nested = (1, (2, 3))
a, (b, c) = nested
print(a)  # 1
print(b)  # 2
print(c)  # 3
```

!!! note "Notes"
    - Structure of variables must match tuple nesting

<hr class="snippet-divider">

### Unpacking with * in function arguments

`tuple` `unpacking` `function` `arguments` `data-structures`

Use * to unpack tuple into function arguments

```python
def add(x, y, z):
    return x + y + z


args = (1, 2, 3)
result = add(*args)
print(result)  # 6
```

!!! note "Notes"
    - *args unpacks tuple elements as positional arguments

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Create and Use Tuples](tuple_create.md)
- **Reference**: See [📂 Named Tuple Usage](namedtuple_usage.md)

## 🏷️ Tags

`tuple`, `unpacking`, `extended-unpacking`, `swap`, `nested`, `function-args`, `data-structures`

## 📝 Notes
- Tuple unpacking is a powerful and Pythonic feature
- Use * for flexible unpacking and function calls

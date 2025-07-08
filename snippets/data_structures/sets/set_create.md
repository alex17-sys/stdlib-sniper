# Create Set

Zero-dependency Python snippets for creating sets from lists or iterables using the standard library.

## Simple

### 🧩 Create set from list

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

📂 Create a set from a list to remove duplicates

🏷️ Tags: set, create, list, unique, data-structures
📝 Notes:
- Sets automatically remove duplicate elements
- Order is not preserved (sets are unordered)
- Useful for deduplication

### 🧩 Create set from string

```python
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}
```

📂 Create a set from a string (unique characters)

🏷️ Tags: set, string, unique, characters, data-structures
📝 Notes:
- Each character becomes a set element
- Useful for character analysis

### 🧩 Create set from tuple or other iterable

```python
tuple_data = (1, 2, 3, 2)
unique_tuple = set(tuple_data)
print(unique_tuple)  # {1, 2, 3}

# From generator
unique_gen = set(x for x in range(5))
print(unique_gen)  # {0, 1, 2, 3, 4}
```

📂 Create a set from any iterable (tuple, generator, etc.)

🏷️ Tags: set, tuple, generator, iterable, data-structures
📝 Notes:
- Works with any iterable (list, tuple, string, generator)
- Fast and memory efficient

## Complex

### 🧩 Create set with comprehension

```python
# Set comprehension for squares of numbers
squares = {x * x for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# Set comprehension with condition
even_squares = {x * x for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

📂 Create sets using set comprehensions

🏷️ Tags: set, comprehension, condition, data-structures
📝 Notes:
- Set comprehensions are concise and expressive
- Can include conditions for filtering
- Similar to list comprehensions

### 🧩 Immutable sets (frozenset)

```python
# Create an immutable set
immutable = frozenset([1, 2, 3, 2])
print(immutable)  # frozenset({1, 2, 3})

# frozenset can be used as a dictionary key
my_dict = {frozenset([1, 2]): "value"}
print(my_dict)
```

📂 Create immutable sets with frozenset

🏷️ Tags: set, frozenset, immutable, hashable, data-structures
📝 Notes:
- frozenset is immutable and hashable
- Useful as dictionary keys or set elements
- Cannot add or remove elements after creation

## 🔗 Cross Reference

- **Reference**: See [📂 Get unique elements from list](set_unique_elements.md)

## 🏷️ Tags

`set`, `create`, `unique`, `frozenset`, `comprehension`, `data-structures`

## 📝 Notes
- Use set() to remove duplicates from any iterable
- Use set comprehensions for custom logic
- Use frozenset for immutable sets

# Create Set

Zero-dependency Python snippets using only the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Create set from list

`set` `create` `list` `unique` `data-structures`

Create a set from a list to remove duplicates

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

!!! note "Notes"
    - Sets automatically remove duplicate elements
    - Order is not preserved (sets are unordered)
    - Useful for deduplication

<hr class="snippet-divider">

### Create set from string

`set` `string` `unique` `characters` `data-structures`

Create a set from a string (unique characters)

```python
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}
```

!!! note "Notes"
    - Each character becomes a set element
    - Useful for character analysis

<hr class="snippet-divider">

### Create set from tuple or other iterable

`set` `tuple` `generator` `iterable` `data-structures`

Create a set from any iterable (tuple, generator, etc.)

```python
tuple_data = (1, 2, 3, 2)
unique_tuple = set(tuple_data)
print(unique_tuple)  # {1, 2, 3}

# From generator
unique_gen = set(x for x in range(5))
print(unique_gen)  # {0, 1, 2, 3, 4}
```

!!! note "Notes"
    - Works with any iterable (list, tuple, string, generator)
    - Fast and memory efficient

<hr class="snippet-divider">

## Complex

###  Create set with comprehension

`set` `comprehension` `condition` `data-structures`

Create sets using set comprehensions

```python
# Set comprehension for squares of numbers
squares = {x * x for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# Set comprehension with condition
even_squares = {x * x for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

!!! note "Notes"
    - Set comprehensions are concise and expressive
    - Can include conditions for filtering
    - Similar to list comprehensions

<hr class="snippet-divider">

### Immutable sets (frozenset)

`set` `frozenset` `immutable` `hashable` `data-structures`

Create immutable sets with frozenset

```python
# Create an immutable set
immutable = frozenset([1, 2, 3, 2])
print(immutable)  # frozenset({1, 2, 3})

# frozenset can be used as a dictionary key
my_dict = {frozenset([1, 2]): "value"}
print(my_dict)
```

!!! note "Notes"
    - frozenset is immutable and hashable
    - Useful as dictionary keys or set elements
    - Cannot add or remove elements after creation

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Get unique elements from list](set_unique_elements.md)

## 🏷️ Tags

`set`, `create`, `unique`, `frozenset`, `comprehension`, `data-structures`

## 📝 Notes
- Use set() to remove duplicates from any iterable
- Use set comprehensions for custom logic
- Use frozenset for immutable sets

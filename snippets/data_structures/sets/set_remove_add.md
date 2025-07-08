# Add and Remove Items from Set

Zero-dependency Python snippets for adding and removing items from sets using the standard library.

## Simple

### 🧩 Add item to set

```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}
```

📂 Add a single item to a set

🏷️ Tags: set, add, insert, data-structures
📝 Notes:
- add() inserts an item if not present
- No error if item already exists

### 🧩 Remove item from set

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry'}

# KeyError if item not present
# fruits.remove('orange')  # Raises KeyError
```

📂 Remove an item from a set

🏷️ Tags: set, remove, delete, data-structures
📝 Notes:
- remove() raises KeyError if item not found

### 🧩 Discard item from set

```python
fruits = {"apple", "banana"}
fruits.discard("banana")
fruits.discard("orange")  # No error if not present
print(fruits)  # {'apple'}
```

📂 Discard an item from a set (no error if missing)

🏷️ Tags: set, discard, safe, data-structures
📝 Notes:
- discard() does not raise error if item is missing

### 🧩 Pop item from set

```python
fruits = {"apple", "banana", "cherry"}
item = fruits.pop()
print(item)  # Random item
print(fruits)  # Remaining items
```

📂 Remove and return an arbitrary item from set

🏷️ Tags: set, pop, remove, data-structures
📝 Notes:
- pop() removes and returns a random element
- Raises KeyError if set is empty

## Complex

### 🧩 Update set with multiple items

```python
numbers = {1, 2}
numbers.update([2, 3, 4])
print(numbers)  # {1, 2, 3, 4}

# Update with another set
numbers.update({5, 6})
print(numbers)  # {1, 2, 3, 4, 5, 6}
```

📂 Add multiple items to a set

🏷️ Tags: set, update, add, multiple, data-structures
📝 Notes:
- update() adds all elements from iterable(s)
- Duplicates are ignored

### 🧩 Remove multiple items from set

```python
numbers = {1, 2, 3, 4, 5}
numbers.difference_update([2, 3])
print(numbers)  # {1, 4, 5}

# Remove using set subtraction
numbers = {1, 2, 3, 4, 5}
numbers -= {4, 5}
print(numbers)  # {1, 2, 3}
```

📂 Remove multiple items from a set

🏷️ Tags: set, remove, difference_update, subtract, data-structures
📝 Notes:
- difference_update() removes all elements found in the argument
- Subtraction operator -= can also be used

## 🔗 Cross Reference

- **Reference**: See [📂 Set Operations](set_operations.md)

## 🏷️ Tags

`set`, `add`, `remove`, `discard`, `pop`, `update`, `difference_update`, `data-structures`

## 📝 Notes
- Use add(), remove(), discard(), pop(), update(), and difference_update() for set mutation
- discard() is safer than remove() for unknown items

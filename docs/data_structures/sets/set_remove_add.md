# Add and Remove Items from Set

Zero-dependency Python snippets using only the standard library.

6 snippets available in this sub-category.

---

## Simple

###  Add item to set

`set` `add` `insert` `data-structures`

Add a single item to a set

```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}
```

!!! note "Notes"
    - add() inserts an item if not present
    - No error if item already exists

<hr class="snippet-divider">

### Remove item from set

`set` `remove` `delete` `data-structures`

Remove an item from a set

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry'}

# KeyError if item not present
# fruits.remove('orange')  # Raises KeyError
```

!!! note "Notes"
    - remove() raises KeyError if item not found

<hr class="snippet-divider">

### Discard item from set

`set` `discard` `safe` `data-structures`

Discard an item from a set (no error if missing)

```python
fruits = {"apple", "banana"}
fruits.discard("banana")
fruits.discard("orange")  # No error if not present
print(fruits)  # {'apple'}
```

!!! note "Notes"
    - discard() does not raise error if item is missing

<hr class="snippet-divider">

### Pop item from set

`set` `pop` `remove` `data-structures`

Remove and return an arbitrary item from set

```python
fruits = {"apple", "banana", "cherry"}
item = fruits.pop()
print(item)  # Random item
print(fruits)  # Remaining items
```

!!! note "Notes"
    - pop() removes and returns a random element
    - Raises KeyError if set is empty

<hr class="snippet-divider">

## Complex

###  Update set with multiple items

`set` `update` `add` `multiple` `data-structures`

Add multiple items to a set

```python
numbers = {1, 2}
numbers.update([2, 3, 4])
print(numbers)  # {1, 2, 3, 4}

# Update with another set
numbers.update({5, 6})
print(numbers)  # {1, 2, 3, 4, 5, 6}
```

!!! note "Notes"
    - update() adds all elements from iterable(s)
    - Duplicates are ignored

<hr class="snippet-divider">

### Remove multiple items from set

`set` `remove` `difference_update` `subtract` `data-structures`

Remove multiple items from a set

```python
numbers = {1, 2, 3, 4, 5}
numbers.difference_update([2, 3])
print(numbers)  # {1, 4, 5}

# Remove using set subtraction
numbers = {1, 2, 3, 4, 5}
numbers -= {4, 5}
print(numbers)  # {1, 2, 3}
```

!!! note "Notes"
    - difference_update() removes all elements found in the argument
    - Subtraction operator -= can also be used

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Set Operations](set_operations.md)

## 🏷️ Tags

`set`, `add`, `remove`, `discard`, `pop`, `update`, `difference_update`, `data-structures`

## 📝 Notes
- Use add(), remove(), discard(), pop(), update(), and difference_update() for set mutation
- discard() is safer than remove() for unknown items

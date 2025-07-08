# Set Membership

Zero-dependency Python snippets for checking membership in sets using the standard library.

## Simple

### 🧩 Check if item is in set

```python
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)  # True
print("orange" in fruits)  # False
```

📂 Check if an element exists in a set

🏷️ Tags: set, membership, in, contains, data-structures
📝 Notes:
- Membership checks are O(1) on average
- Much faster than checking in a list for large collections

### 🧩 Not in set

```python
numbers = {1, 2, 3}
print(4 not in numbers)  # True
```

📂 Check if an element does not exist in a set

🏷️ Tags: set, not-in, membership, data-structures
📝 Notes:
- Use `not in` for negative membership

## Complex

### 🧩 Set membership with custom objects

```python
class User:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, User) and self.name == other.name


users = {User("alice"), User("bob")}
print(User("alice") in users)  # True
print(User("carol") in users)  # False
```

📂 Check membership for custom objects in a set

🏷️ Tags: set, membership, custom, object, hash, data-structures
📝 Notes:
- Custom objects must implement __hash__ and __eq__ for set membership
- Useful for deduplication of custom types

## 🔗 Cross Reference

- **Reference**: See [📂 Add and remove items from set](set_remove_add.md)

## 🏷️ Tags

`set`, `membership`, `in`, `not-in`, `custom`, `data-structures`

## 📝 Notes
- Use `in` and `not in` for fast membership checks
- Sets are ideal for large membership tests

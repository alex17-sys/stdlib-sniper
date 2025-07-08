# Subset and Superset Relations

Zero-dependency Python snippets for checking subset and superset relations using the standard library.

## Simple

### 🧩 Check if set is subset

```python
set_a = {1, 2}
set_b = {1, 2, 3, 4}
print(set_a <= set_b)  # True
print(set_a.issubset(set_b))  # True
```

📂 Check if all elements of set_a are in set_b

🏷️ Tags: set, subset, issubset, data-structures
📝 Notes:
- <= operator or issubset() method
- True if set_a is subset of set_b

### 🧩 Check if set is superset

```python
set_a = {1, 2, 3, 4}
set_b = {2, 3}
print(set_a >= set_b)  # True
print(set_a.issuperset(set_b))  # True
```

📂 Check if set_a contains all elements of set_b

🏷️ Tags: set, superset, issuperset, data-structures
📝 Notes:
- >= operator or issuperset() method
- True if set_a is superset of set_b

## Complex

### 🧩 Proper subset and superset

```python
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a < set_b)  # True (proper subset)
print(set_b > set_a)  # True (proper superset)

# Not proper if equal
set_c = {1, 2, 3}
print(set_b < set_c)  # False
print(set_b > set_c)  # False
```

📂 Check for proper subset/superset (not equal)

🏷️ Tags: set, proper-subset, proper-superset, data-structures
📝 Notes:
- < and > operators for proper subset/superset
- False if sets are equal

## 🔗 Cross Reference

- **Reference**: See [📂 Set Operations](set_operations.md)

## 🏷️ Tags

`set`, `subset`, `superset`, `proper-subset`, `proper-superset`, `data-structures`

## 📝 Notes
- Use <=, >=, <, > or issubset(), issuperset() for subset/superset checks
- Proper subset/superset means strictly contained (not equal)

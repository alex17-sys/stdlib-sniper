# Set Operations

Zero-dependency Python snippets for performing set operations using the standard library.

## Simple

### 🧩 Union of sets

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b
print(union)  # {1, 2, 3, 4, 5}

# Or using union() method
union2 = set_a.union(set_b)
print(union2)  # {1, 2, 3, 4, 5}
```

📂 Combine all unique elements from both sets

🏷️ Tags: set, union, combine, data-structures
📝 Notes:
- The | operator or union() method can be used
- Removes duplicates automatically

### 🧩 Intersection of sets

```python
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = set_a & set_b
print(intersection)  # {2, 3}

# Or using intersection() method
intersection2 = set_a.intersection(set_b)
print(intersection2)  # {2, 3}
```

📂 Find common elements between sets

🏷️ Tags: set, intersection, common, data-structures
📝 Notes:
- The & operator or intersection() method can be used

### 🧩 Difference of sets

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
difference = set_a - set_b
print(difference)  # {1, 2}

# Or using difference() method
difference2 = set_a.difference(set_b)
print(difference2)  # {1, 2}
```

📂 Elements in set_a but not in set_b

🏷️ Tags: set, difference, subtract, data-structures
📝 Notes:
- The - operator or difference() method can be used

### 🧩 Symmetric difference of sets

```python
set_a = {1, 2, 3}
set_b = {2, 3, 4}
sym_diff = set_a ^ set_b
print(sym_diff)  # {1, 4}

# Or using symmetric_difference() method
sym_diff2 = set_a.symmetric_difference(set_b)
print(sym_diff2)  # {1, 4}
```

📂 Elements in either set, but not both

🏷️ Tags: set, symmetric-difference, xor, data-structures
📝 Notes:
- The ^ operator or symmetric_difference() method can be used

## Complex

### 🧩 Multiple set operations

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {4, 5, 6, 7}

# Union of three sets
all_union = set_a | set_b | set_c
print(all_union)  # {1, 2, 3, 4, 5, 6, 7}

# Intersection of three sets
all_intersection = set_a & set_b & set_c
print(all_intersection)  # {4}

# Difference chain
diff_chain = set_a - set_b - set_c
print(diff_chain)  # {1, 2}
```

📂 Combine multiple sets with chained operations

🏷️ Tags: set, multiple, chain, data-structures
📝 Notes:
- Operators can be chained for multiple sets
- Useful for complex set logic

## 🔗 Cross Reference

- **Reference**: See [📂 Check if item is in set](set_membership.md)

## 🏷️ Tags

`set`, `union`, `intersection`, `difference`, `symmetric-difference`, `operations`, `data-structures`

## 📝 Notes
- Use set operators or methods for all standard set operations
- Chaining is possible for multiple sets

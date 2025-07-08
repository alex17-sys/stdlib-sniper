# Set Operations

Zero-dependency Python snippets using only the standard library.

5 snippets available in this sub-category.

---

## Simple

###  Union of sets

`set` `union` `combine` `data-structures`

Combine all unique elements from both sets

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b
print(union)  # {1, 2, 3, 4, 5}

# Or using union() method
union2 = set_a.union(set_b)
print(union2)  # {1, 2, 3, 4, 5}
```

!!! note "Notes"
    - The | operator or union() method can be used
    - Removes duplicates automatically

<hr class="snippet-divider">

### Intersection of sets

`set` `intersection` `common` `data-structures`

Find common elements between sets

```python
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = set_a & set_b
print(intersection)  # {2, 3}

# Or using intersection() method
intersection2 = set_a.intersection(set_b)
print(intersection2)  # {2, 3}
```

!!! note "Notes"
    - The & operator or intersection() method can be used

<hr class="snippet-divider">

### Difference of sets

`set` `difference` `subtract` `data-structures`

Elements in set_a but not in set_b

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
difference = set_a - set_b
print(difference)  # {1, 2}

# Or using difference() method
difference2 = set_a.difference(set_b)
print(difference2)  # {1, 2}
```

!!! note "Notes"
    - The - operator or difference() method can be used

<hr class="snippet-divider">

### Symmetric difference of sets

`set` `symmetric-difference` `xor` `data-structures`

Elements in either set, but not both

```python
set_a = {1, 2, 3}
set_b = {2, 3, 4}
sym_diff = set_a ^ set_b
print(sym_diff)  # {1, 4}

# Or using symmetric_difference() method
sym_diff2 = set_a.symmetric_difference(set_b)
print(sym_diff2)  # {1, 4}
```

!!! note "Notes"
    - The ^ operator or symmetric_difference() method can be used

<hr class="snippet-divider">

## Complex

###  Multiple set operations

`set` `multiple` `chain` `data-structures`

Combine multiple sets with chained operations

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

!!! note "Notes"
    - Operators can be chained for multiple sets
    - Useful for complex set logic

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Check if item is in set](set_membership.md)

## 🏷️ Tags

`set`, `union`, `intersection`, `difference`, `symmetric-difference`, `operations`, `data-structures`

## 📝 Notes
- Use set operators or methods for all standard set operations
- Chaining is possible for multiple sets

---
title: Subset and Superset Relations
description: Zero-dependency Python snippets for checking subset and superset relations using the standard library.
keywords: data-structures, issubset, issuperset, proper-subset, proper-superset, set, subset, superset
---

# Subset and Superset Relations

Zero-dependency Python snippets for checking subset and superset relations using the standard library.

3 snippets available in this sub-category.

---

## Simple

###  Check if set is subset

`set` `subset` `issubset` `data-structures`

Check if all elements of set_a are in set_b

```python
set_a = {1, 2}
set_b = {1, 2, 3, 4}
print(set_a <= set_b)  # True
print(set_a.issubset(set_b))  # True
```

!!! note "Notes"
    - <= operator or issubset() method
    - True if set_a is subset of set_b

<hr class="snippet-divider">

### Check if set is superset

`set` `superset` `issuperset` `data-structures`

Check if set_a contains all elements of set_b

```python
set_a = {1, 2, 3, 4}
set_b = {2, 3}
print(set_a >= set_b)  # True
print(set_a.issuperset(set_b))  # True
```

!!! note "Notes"
    - >= operator or issuperset() method
    - True if set_a is superset of set_b

<hr class="snippet-divider">

## Complex

###  Proper subset and superset

`set` `proper-subset` `proper-superset` `data-structures`

Check for proper subset/superset (not equal)

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

!!! note "Notes"
    - < and > operators for proper subset/superset
    - False if sets are equal

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Set Operations](set_operations.md)

## 🏷️ Tags

`set`, `subset`, `superset`, `proper-subset`, `proper-superset`, `data-structures`

## 📝 Notes
- Use <=, >=, <, > or issubset(), issuperset() for subset/superset checks
- Proper subset/superset means strictly contained (not equal)

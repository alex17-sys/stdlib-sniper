# n Largest and n Smallest with heapq

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Find n largest elements

`heap` `heapq` `nlargest` `max` `data-structures`

Get the n largest elements from a list

```python
import heapq

numbers = [5, 1, 8, 3, 7, 2]
largest = heapq.nlargest(3, numbers)
print(largest)  # [8, 7, 5]
```

!!! note "Notes"
    - Returns a sorted list of n largest elements

<hr class="snippet-divider">

### Find n smallest elements

`heap` `heapq` `nsmallest` `min` `data-structures`

Get the n smallest elements from a list

```python
import heapq

numbers = [5, 1, 8, 3, 7, 2]
smallest = heapq.nsmallest(3, numbers)
print(smallest)  # [1, 2, 3]
```

!!! note "Notes"
    - Returns a sorted list of n smallest elements

<hr class="snippet-divider">

## Complex

###  nlargest/nsmallest with custom key

`heap` `heapq` `nlargest` `nsmallest` `key` `custom` `data-structures`

Use key function to customize selection

```python
import heapq

words = ["apple", "banana", "pear", "grape"]
longest = heapq.nlargest(2, words, key=len)
print(longest)  # ['banana', 'apple']

shortest = heapq.nsmallest(2, words, key=len)
print(shortest)  # ['pear', 'grape']
```

!!! note "Notes"
    - key argument works like in sorted()
    - Useful for objects, custom criteria

<hr class="snippet-divider">

### Edge cases: n > len(list), n = 0

`heap` `heapq` `nlargest` `nsmallest` `edge-case` `data-structures`

Handles cases where n is too large or zero

```python
import heapq

numbers = [1, 2]
print(heapq.nlargest(5, numbers))  # [2, 1]
print(heapq.nsmallest(0, numbers))  # []
```

!!! note "Notes"
    - If n > len(list), returns all elements sorted
    - If n = 0, returns empty list

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Create Min-Heap with heapq](heap_create.md)

## 🏷️ Tags

`heap`, `heapq`, `nlargest`, `nsmallest`, `key`, `data-structures`

## 📝 Notes
- nlargest/nsmallest are efficient for small n (O(n log k))
- For full sort, use sorted()

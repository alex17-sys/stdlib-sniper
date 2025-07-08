# n Largest and n Smallest with heapq

Zero-dependency Python snippets for finding the n largest and n smallest elements using the standard library heapq module.

## Simple

### 🧩 Find n largest elements

```python
import heapq

numbers = [5, 1, 8, 3, 7, 2]
largest = heapq.nlargest(3, numbers)
print(largest)  # [8, 7, 5]
```

📂 Get the n largest elements from a list

🏷️ Tags: heap, heapq, nlargest, max, data-structures
📝 Notes:
- Returns a sorted list of n largest elements

### 🧩 Find n smallest elements

```python
import heapq

numbers = [5, 1, 8, 3, 7, 2]
smallest = heapq.nsmallest(3, numbers)
print(smallest)  # [1, 2, 3]
```

📂 Get the n smallest elements from a list

🏷️ Tags: heap, heapq, nsmallest, min, data-structures
📝 Notes:
- Returns a sorted list of n smallest elements

## Complex

### 🧩 nlargest/nsmallest with custom key

```python
import heapq

words = ["apple", "banana", "pear", "grape"]
longest = heapq.nlargest(2, words, key=len)
print(longest)  # ['banana', 'apple']

shortest = heapq.nsmallest(2, words, key=len)
print(shortest)  # ['pear', 'grape']
```

📂 Use key function to customize selection

🏷️ Tags: heap, heapq, nlargest, nsmallest, key, custom, data-structures
📝 Notes:
- key argument works like in sorted()
- Useful for objects, custom criteria

### 🧩 Edge cases: n > len(list), n = 0

```python
import heapq

numbers = [1, 2]
print(heapq.nlargest(5, numbers))  # [2, 1]
print(heapq.nsmallest(0, numbers))  # []
```

📂 Handles cases where n is too large or zero

🏷️ Tags: heap, heapq, nlargest, nsmallest, edge-case, data-structures
📝 Notes:
- If n > len(list), returns all elements sorted
- If n = 0, returns empty list

## 🔗 Cross Reference

- **Reference**: See [📂 Create Min-Heap with heapq](heap_create.md)

## 🏷️ Tags

`heap`, `heapq`, `nlargest`, `nsmallest`, `key`, `data-structures`

## 📝 Notes
- nlargest/nsmallest are efficient for small n (O(n log k))
- For full sort, use sorted()

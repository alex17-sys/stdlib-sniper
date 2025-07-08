# Create Min-Heap with heapq

Zero-dependency Python snippets for creating and using a min-heap with the standard library heapq module.

## Simple

### 🧩 Heapify a list

```python
import heapq

numbers = [5, 3, 8, 1, 2]
heapq.heapify(numbers)
print(numbers)  # [1, 2, 8, 5, 3] (heap order)
```

📂 Convert a list into a min-heap in-place

🏷️ Tags: heap, heapq, heapify, min-heap, data-structures
📝 Notes:
- heapq.heapify() rearranges list into heap order
- The smallest element is always at index 0

### 🧩 Push and pop from heap

```python
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
print(heap)  # [1, 4, 7]

smallest = heapq.heappop(heap)
print(smallest)  # 1
print(heap)  # [4, 7]
```

📂 Add and remove elements from a min-heap

🏷️ Tags: heap, heapq, push, pop, min-heap, data-structures
📝 Notes:
- heappush() adds, heappop() removes smallest

## Complex

### 🧩 Peek at smallest element

```python
import heapq

heap = [3, 1, 4]
heapq.heapify(heap)
smallest = heap[0]
print(smallest)  # 1
```

📂 Access the smallest element without removing

🏷️ Tags: heap, peek, min-heap, data-structures
📝 Notes:
- heap[0] is always the smallest

### 🧩 Heap sort (ascending)

```python
import heapq


def heap_sort(iterable):
    h = list(iterable)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


numbers = [5, 3, 8, 1, 2]
sorted_numbers = heap_sort(numbers)
print(sorted_numbers)  # [1, 2, 3, 5, 8]
```

📂 Use heapq to sort a list in ascending order

🏷️ Tags: heap, sort, heapq, min-heap, data-structures
📝 Notes:
- Heap sort is O(n log n)
- Not stable, but memory efficient

## 🔗 Cross Reference

- **Reference**: See [📂 Push and Pop from Heap](heap_push_pop.md)

## 🏷️ Tags

`heap`, `heapq`, `min-heap`, `heapify`, `push`, `pop`, `peek`, `sort`, `data-structures`

## 📝 Notes
- heapq only provides min-heap (use -x for max-heap)
- Heaps are useful for priority queues, scheduling, and more

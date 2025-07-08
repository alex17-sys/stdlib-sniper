# Push and Pop from Heap

Zero-dependency Python snippets using only the standard library.

3 snippets available in this sub-category.

---

## Simple

###  Push and pop separately

`heap` `heapq` `push` `pop` `min-heap` `data-structures`

Add and remove elements from a min-heap

```python
import heapq

heap = [2, 3, 5]
heapq.heapify(heap)
heapq.heappush(heap, 1)
print(heap)  # [1, 2, 5, 3]
smallest = heapq.heappop(heap)
print(smallest)  # 1
print(heap)  # [2, 3, 5]
```

!!! note "Notes"
    - heappush() adds, heappop() removes smallest

<hr class="snippet-divider">

## Complex

###  heappushpop: push then pop (efficient)

`heap` `heapq` `heappushpop` `efficient` `data-structures`

Push new item, then pop and return smallest (single operation)

```python
import heapq

heap = [2, 3, 5]
heapq.heapify(heap)
result = heapq.heappushpop(heap, 1)
print(result)  # 1
print(heap)  # [2, 3, 5]

result2 = heapq.heappushpop(heap, 4)
print(result2)  # 2
print(heap)  # [3, 4, 5]
```

!!! note "Notes"
    - More efficient than separate push and pop if you always want to pop after push
    - If new item is smaller than smallest, it is returned and not added

<hr class="snippet-divider">

### heapreplace: pop then push (always replaces)

`heap` `heapq` `heapreplace` `replace` `data-structures`

Pop and return smallest, then push new item (single operation)

```python
import heapq

heap = [2, 3, 5]
heapq.heapify(heap)
result = heapq.heapreplace(heap, 1)
print(result)  # 2 (popped)
print(heap)  # [1, 3, 5]
```

!!! note "Notes"
    - Always pops and pushes, even if new item is smaller
    - Raises IndexError if heap is empty

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Create Min-Heap with heapq](heap_create.md)
- **Reference**: See [📂 Priority Queue with heapq](../queues_stacks/priority_queue.md)

## 🏷️ Tags

`heap`, `heapq`, `push`, `pop`, `heappushpop`, `heapreplace`, `data-structures`

## 📝 Notes
- Use heappushpop() for efficient push-then-pop
- Use heapreplace() to always replace smallest

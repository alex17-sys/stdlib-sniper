# Priority Queue with heapq

Zero-dependency Python snippets using only the standard library.

3 snippets available in this sub-category.

---

## Simple

###  Min-priority queue with heapq

`heap` `heapq` `priority-queue` `min-heap` `data-structures`

Use (priority, value) tuples for min-priority queue

```python
import heapq

pq = []
heapq.heappush(pq, (2, "code"))
heapq.heappush(pq, (1, "eat"))
heapq.heappush(pq, (3, "sleep"))

while pq:
    priority, task = heapq.heappop(pq)
    print(priority, task)
# 1 eat
# 2 code
# 3 sleep
```

!!! note "Notes"
    - Lower numbers = higher priority (min-heap)
    - Tuples are compared by first element (priority)

<hr class="snippet-divider">

## Complex

###  Max-priority queue with heapq

`heap` `heapq` `priority-queue` `max-heap` `data-structures`

Use negative priorities for max-priority queue

```python
import heapq

pq = []
heapq.heappush(pq, (-2, "code"))
heapq.heappush(pq, (-1, "eat"))
heapq.heappush(pq, (-3, "sleep"))

while pq:
    priority, task = heapq.heappop(pq)
    print(-priority, task)
# 3 sleep
# 2 code
# 1 eat
```

!!! note "Notes"
    - Negate priorities to simulate max-heap
    - Print -priority to get original value

<hr class="snippet-divider">

### Priority queue with custom objects

`heap` `heapq` `priority-queue` `custom` `data-structures`

Use custom objects with __lt__ for priority queue

```python
import heapq


class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority


pq = []
heapq.heappush(pq, Task(2, "code"))
heapq.heappush(pq, Task(1, "eat"))
heapq.heappush(pq, Task(3, "sleep"))

while pq:
    task = heapq.heappop(pq)
    print(task.priority, task.name)
# 1 eat
# 2 code
# 3 sleep
```

!!! note "Notes"
    - Custom objects must implement __lt__ for heapq
    - Useful for complex priority logic

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Create Min-Heap with heapq](../heaps/heap_create.md)

## 🏷️ Tags

`heap`, `heapq`, `priority-queue`, `min-heap`, `max-heap`, `custom`, `data-structures`

## 📝 Notes
- heapq is efficient for priority queues (O(log n) per operation)
- Use (priority, value) tuples or custom objects for advanced use cases

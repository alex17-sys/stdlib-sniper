# Priority Queue with heapq

Zero-dependency Python snippets for implementing a priority queue using the standard library heapq module.

## Simple

### 🧩 Min-priority queue with heapq

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

📂 Use (priority, value) tuples for min-priority queue

🏷️ Tags: heap, heapq, priority-queue, min-heap, data-structures
📝 Notes:
- Lower numbers = higher priority (min-heap)
- Tuples are compared by first element (priority)

## Complex

### 🧩 Max-priority queue with heapq

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

📂 Use negative priorities for max-priority queue

🏷️ Tags: heap, heapq, priority-queue, max-heap, data-structures
📝 Notes:
- Negate priorities to simulate max-heap
- Print -priority to get original value

### 🧩 Priority queue with custom objects

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

📂 Use custom objects with __lt__ for priority queue

🏷️ Tags: heap, heapq, priority-queue, custom, data-structures
📝 Notes:
- Custom objects must implement __lt__ for heapq
- Useful for complex priority logic

## 🔗 Cross Reference

- **Reference**: See [📂 Create Min-Heap with heapq](../heaps/heap_create.md)

## 🏷️ Tags

`heap`, `heapq`, `priority-queue`, `min-heap`, `max-heap`, `custom`, `data-structures`

## 📝 Notes
- heapq is efficient for priority queues (O(log n) per operation)
- Use (priority, value) tuples or custom objects for advanced use cases

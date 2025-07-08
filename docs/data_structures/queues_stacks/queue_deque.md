# Use deque as Queue (FIFO)

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Enqueue and dequeue with deque

`queue` `deque` `enqueue` `dequeue` `FIFO` `data-structures`

Use deque append() and popleft() for queue operations

```python
from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

item = queue.popleft()  # Dequeue
print(item)  # 1
print(queue)  # deque([2, 3])
```

!!! note "Notes"
    - append() adds to the end (rear of queue)
    - popleft() removes from the front (head of queue)

<hr class="snippet-divider">

### Peek at front and rear

`queue` `peek` `deque` `data-structures`

Access the front and rear elements without removing

```python
from collections import deque


queue = deque([1, 2, 3])
front = queue[0]
rear = queue[-1]
print(front, rear)  # 1 3
```

!!! note "Notes"
    - Use queue[0] for front, queue[-1] for rear
    - Raises IndexError if queue is empty

<hr class="snippet-divider">

## Complex

###  Queue with maxlen (bounded queue)

`queue` `deque` `maxlen` `bounded` `data-structures`

Bounded queue with automatic overflow handling

```python
from collections import deque


queue = deque(maxlen=3)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)  # Oldest item (1) is dropped
print(queue)  # deque([2, 3, 4], maxlen=3)
```

!!! note "Notes"
    - maxlen discards oldest items when full

<hr class="snippet-divider">

### Thread-safe queue with queue.Queue

`queue` `thread-safe` `data-structures`

Use queue.Queue for thread-safe FIFO queues

```python
from queue import Queue

q = Queue()
q.put(1)  # Enqueue
q.put(2)
item = q.get()  # Dequeue
print(item)  # 1
```

!!! note "Notes"
    - queue.Queue is safe for multi-threaded use
    - Use get_nowait() and put_nowait() for non-blocking

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Use List as Stack](stack_list.md)

## 🏷️ Tags

`queue`, `deque`, `enqueue`, `dequeue`, `peek`, `maxlen`, `thread-safe`, `FIFO`, `data-structures`

## 📝 Notes
- deque is fast and flexible for queues and stacks
- For thread-safe or multi-producer/consumer queues, use queue.Queue

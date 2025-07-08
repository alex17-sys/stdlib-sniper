# Use deque as Queue (FIFO)

Zero-dependency Python snippets for using collections.deque as a queue (First-In, First-Out) with the standard library.

## Simple

### 🧩 Enqueue and dequeue with deque

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

📂 Use deque append() and popleft() for queue operations

🏷️ Tags: queue, deque, enqueue, dequeue, FIFO, data-structures
📝 Notes:
- append() adds to the end (rear of queue)
- popleft() removes from the front (head of queue)

### 🧩 Peek at front and rear

```python
from collections import deque


queue = deque([1, 2, 3])
front = queue[0]
rear = queue[-1]
print(front, rear)  # 1 3
```

📂 Access the front and rear elements without removing

🏷️ Tags: queue, peek, deque, data-structures
📝 Notes:
- Use queue[0] for front, queue[-1] for rear
- Raises IndexError if queue is empty

## Complex

### 🧩 Queue with maxlen (bounded queue)

```python
from collections import deque


queue = deque(maxlen=3)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)  # Oldest item (1) is dropped
print(queue)  # deque([2, 3, 4], maxlen=3)
```

📂 Bounded queue with automatic overflow handling

🏷️ Tags: queue, deque, maxlen, bounded, data-structures
📝 Notes:
- maxlen discards oldest items when full

### 🧩 Thread-safe queue with queue.Queue

```python
from queue import Queue

q = Queue()
q.put(1)  # Enqueue
q.put(2)
item = q.get()  # Dequeue
print(item)  # 1
```

📂 Use queue.Queue for thread-safe FIFO queues

🏷️ Tags: queue, thread-safe, data-structures
📝 Notes:
- queue.Queue is safe for multi-threaded use
- Use get_nowait() and put_nowait() for non-blocking

## 🔗 Cross Reference

- **Reference**: See [📂 Use List as Stack](stack_list.md)

## 🏷️ Tags

`queue`, `deque`, `enqueue`, `dequeue`, `peek`, `maxlen`, `thread-safe`, `FIFO`, `data-structures`

## 📝 Notes
- deque is fast and flexible for queues and stacks
- For thread-safe or multi-producer/consumer queues, use queue.Queue

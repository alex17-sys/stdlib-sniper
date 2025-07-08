# 🧩 Enqueue and dequeue with deque
from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

item = queue.popleft()  # Dequeue
print(item)  # 1
print(queue)  # deque([2, 3])


# 🧩 Peek at front and rear
from collections import deque


queue = deque([1, 2, 3])
front = queue[0]
rear = queue[-1]
print(front, rear)  # 1 3


# 🧩 Queue with maxlen (bounded queue)
from collections import deque


queue = deque(maxlen=3)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)  # Oldest item (1) is dropped
print(queue)  # deque([2, 3, 4], maxlen=3)


# 🧩 Thread-safe queue with queue.Queue
from queue import Queue

q = Queue()
q.put(1)  # Enqueue
q.put(2)
item = q.get()  # Dequeue
print(item)  # 1

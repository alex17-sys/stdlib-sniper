# 🧩 Min-priority queue with heapq
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


# 🧩 Max-priority queue with heapq
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


# 🧩 Priority queue with custom objects
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

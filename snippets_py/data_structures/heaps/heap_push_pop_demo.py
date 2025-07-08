# 🧩 Push and pop separately
import heapq

heap = [2, 3, 5]
heapq.heapify(heap)
heapq.heappush(heap, 1)
print(heap)  # [1, 2, 5, 3]
smallest = heapq.heappop(heap)
print(smallest)  # 1
print(heap)  # [2, 3, 5]


# 🧩 heappushpop: push then pop (efficient)
import heapq

heap = [2, 3, 5]
heapq.heapify(heap)
result = heapq.heappushpop(heap, 1)
print(result)  # 1
print(heap)  # [2, 3, 5]

result2 = heapq.heappushpop(heap, 4)
print(result2)  # 2
print(heap)  # [3, 4, 5]


# 🧩 heapreplace: pop then push (always replaces)
import heapq

heap = [2, 3, 5]
heapq.heapify(heap)
result = heapq.heapreplace(heap, 1)
print(result)  # 2 (popped)
print(heap)  # [1, 3, 5]

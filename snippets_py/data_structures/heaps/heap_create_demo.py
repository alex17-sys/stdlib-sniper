# 🧩 Heapify a list
import heapq

numbers = [5, 3, 8, 1, 2]
heapq.heapify(numbers)
print(numbers)  # [1, 2, 8, 5, 3] (heap order)


# 🧩 Push and pop from heap
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
print(heap)  # [1, 4, 7]

smallest = heapq.heappop(heap)
print(smallest)  # 1
print(heap)  # [4, 7]


# 🧩 Peek at smallest element
import heapq

heap = [3, 1, 4]
heapq.heapify(heap)
smallest = heap[0]
print(smallest)  # 1


# 🧩 Heap sort (ascending)
import heapq


def heap_sort(iterable):
    h = list(iterable)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


numbers = [5, 3, 8, 1, 2]
sorted_numbers = heap_sort(numbers)
print(sorted_numbers)  # [1, 2, 3, 5, 8]

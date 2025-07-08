# 🧩 Find n largest elements
import heapq

numbers = [5, 1, 8, 3, 7, 2]
largest = heapq.nlargest(3, numbers)
print(largest)  # [8, 7, 5]


# 🧩 Find n smallest elements
import heapq

numbers = [5, 1, 8, 3, 7, 2]
smallest = heapq.nsmallest(3, numbers)
print(smallest)  # [1, 2, 3]


# 🧩 nlargest/nsmallest with custom key
import heapq

words = ["apple", "banana", "pear", "grape"]
longest = heapq.nlargest(2, words, key=len)
print(longest)  # ['banana', 'apple']

shortest = heapq.nsmallest(2, words, key=len)
print(shortest)  # ['pear', 'grape']


# 🧩 Edge cases: n > len(list), n = 0
import heapq

numbers = [1, 2]
print(heapq.nlargest(5, numbers))  # [2, 1]
print(heapq.nsmallest(0, numbers))  # []

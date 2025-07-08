# 🧩 Add item to set
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}


# 🧩 Remove item from set
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry'}

# KeyError if item not present
# fruits.remove('orange')  # Raises KeyError


# 🧩 Discard item from set
fruits = {"apple", "banana"}
fruits.discard("banana")
fruits.discard("orange")  # No error if not present
print(fruits)  # {'apple'}


# 🧩 Pop item from set
fruits = {"apple", "banana", "cherry"}
item = fruits.pop()
print(item)  # Random item
print(fruits)  # Remaining items


# 🧩 Update set with multiple items
numbers = {1, 2}
numbers.update([2, 3, 4])
print(numbers)  # {1, 2, 3, 4}

# Update with another set
numbers.update({5, 6})
print(numbers)  # {1, 2, 3, 4, 5, 6}


# 🧩 Remove multiple items from set
numbers = {1, 2, 3, 4, 5}
numbers.difference_update([2, 3])
print(numbers)  # {1, 4, 5}

# Remove using set subtraction
numbers = {1, 2, 3, 4, 5}
numbers -= {4, 5}
print(numbers)  # {1, 2, 3}

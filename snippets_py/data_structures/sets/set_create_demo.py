# 🧩 Create set from list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}


# 🧩 Create set from string
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}


# 🧩 Create set from tuple or other iterable
tuple_data = (1, 2, 3, 2)
unique_tuple = set(tuple_data)
print(unique_tuple)  # {1, 2, 3}

# From generator
unique_gen = set(x for x in range(5))
print(unique_gen)  # {0, 1, 2, 3, 4}


# 🧩 Create set with comprehension
# Set comprehension for squares of numbers
squares = {x * x for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# Set comprehension with condition
even_squares = {x * x for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}


# 🧩 Immutable sets (frozenset)
# Create an immutable set
immutable = frozenset([1, 2, 3, 2])
print(immutable)  # frozenset({1, 2, 3})

# frozenset can be used as a dictionary key
my_dict = {frozenset([1, 2]): "value"}
print(my_dict)

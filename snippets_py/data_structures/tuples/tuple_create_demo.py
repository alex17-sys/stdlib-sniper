# 🧩 Create a tuple
# Empty tuple
t1 = ()
print(t1)  # ()

# Tuple with elements
t2 = (1, 2, 3)
print(t2)  # (1, 2, 3)

# Tuple without parentheses
t3 = 1, 2, 3
print(t3)  # (1, 2, 3)

# Single-element tuple (note the comma)
t4 = (42,)
print(t4)  # (42,)


# 🧩 Tuple from iterable
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)  # (1, 2, 3)

s = "abc"
tup2 = tuple(s)
print(tup2)  # ('a', 'b', 'c')


# 🧩 Tuple packing and unpacking
# Packing
coords = 10, 20
print(coords)  # (10, 20)

# Unpacking
x, y = coords
print(x, y)  # 10 20

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5


# 🧩 Tuple immutability and usage
tup = (1, 2, 3)
# tup[0] = 99  # Raises TypeError: 'tuple' object does not support item assignment

# Tuples can be used as dictionary keys
my_dict = {(1, 2): "point"}
print(my_dict[(1, 2)])  # 'point'


# 🧩 Nested tuples and tuple of tuples
matrix = ((1, 2), (3, 4), (5, 6))
for row in matrix:
    print(row)
# (1, 2)
# (3, 4)
# (5, 6)

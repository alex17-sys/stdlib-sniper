# 🧩 Basic tuple unpacking
tup = (10, 20)
x, y = tup
print(x)  # 10
print(y)  # 20


# 🧩 Unpacking in for loops
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, char in pairs:
    print(num, char)
# 1 a
# 2 b
# 3 c


# 🧩 Extended unpacking (Python 3+)
tup = (1, 2, 3, 4, 5)
first, *middle, last = tup
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5

# Ignore values with _
x, _, z = (10, 99, 30)
print(x, z)  # 10 30


# 🧩 Swapping variables with tuple unpacking
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1


# 🧩 Nested tuple unpacking
nested = (1, (2, 3))
a, (b, c) = nested
print(a)  # 1
print(b)  # 2
print(c)  # 3


# 🧩 Unpacking with * in function arguments
def add(x, y, z):
    return x + y + z


args = (1, 2, 3)
result = add(*args)
print(result)  # 6

# 🧩 Check if set is subset
set_a = {1, 2}
set_b = {1, 2, 3, 4}
print(set_a <= set_b)  # True
print(set_a.issubset(set_b))  # True


# 🧩 Check if set is superset
set_a = {1, 2, 3, 4}
set_b = {2, 3}
print(set_a >= set_b)  # True
print(set_a.issuperset(set_b))  # True


# 🧩 Proper subset and superset
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a < set_b)  # True (proper subset)
print(set_b > set_a)  # True (proper superset)

# Not proper if equal
set_c = {1, 2, 3}
print(set_b < set_c)  # False
print(set_b > set_c)  # False

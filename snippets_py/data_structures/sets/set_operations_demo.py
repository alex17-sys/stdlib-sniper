# 🧩 Union of sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b
print(union)  # {1, 2, 3, 4, 5}

# Or using union() method
union2 = set_a.union(set_b)
print(union2)  # {1, 2, 3, 4, 5}


# 🧩 Intersection of sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = set_a & set_b
print(intersection)  # {2, 3}

# Or using intersection() method
intersection2 = set_a.intersection(set_b)
print(intersection2)  # {2, 3}


# 🧩 Difference of sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
difference = set_a - set_b
print(difference)  # {1, 2}

# Or using difference() method
difference2 = set_a.difference(set_b)
print(difference2)  # {1, 2}


# 🧩 Symmetric difference of sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
sym_diff = set_a ^ set_b
print(sym_diff)  # {1, 4}

# Or using symmetric_difference() method
sym_diff2 = set_a.symmetric_difference(set_b)
print(sym_diff2)  # {1, 4}


# 🧩 Multiple set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {4, 5, 6, 7}

# Union of three sets
all_union = set_a | set_b | set_c
print(all_union)  # {1, 2, 3, 4, 5, 6, 7}

# Intersection of three sets
all_intersection = set_a & set_b & set_c
print(all_intersection)  # {4}

# Difference chain
diff_chain = set_a - set_b - set_c
print(diff_chain)  # {1, 2}

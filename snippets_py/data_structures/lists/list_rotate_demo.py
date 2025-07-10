# 🧩 Rotate list by n positions
def rotate_list(lst, n):
    """Rotate list by n positions to the right."""
    if not lst:
        return lst

    n = n % len(lst)  # Handle negative and large values
    return lst[-n:] + lst[:-n]


numbers = [1, 2, 3, 4, 5]
result = rotate_list(numbers, 2)
print(result)  # [4, 5, 1, 2, 3]


# 🧩 Rotate list left
def rotate_list_left(lst, n):
    """Rotate list by n positions to the left."""
    if not lst:
        return lst

    n = n % len(lst)  # Handle negative and large values
    return lst[n:] + lst[:n]


numbers = [1, 2, 3, 4, 5]
result = rotate_list_left(numbers, 2)
print(result)  # [3, 4, 5, 1, 2]


# 🧩 Rotate list in place
def rotate_list_inplace(lst, n):
    """Rotate list in place by n positions."""
    if not lst:
        return lst

    n = n % len(lst)
    if n == 0:
        return lst

    # Reverse the entire list
    lst.reverse()
    # Reverse first n elements
    lst[:n] = lst[:n][::-1]
    # Reverse remaining elements
    lst[n:] = lst[n:][::-1]

    return lst


numbers = [1, 2, 3, 4, 5]
result = rotate_list_inplace(numbers, 2)
print(result)  # [4, 5, 1, 2, 3]
print(numbers)  # [4, 5, 1, 2, 3] (original list modified)


# 🧩 Rotate list with custom direction
def rotate_list_direction(lst, n, direction="right"):
    """Rotate list by n positions in specified direction."""
    if not lst:
        return lst

    n = n % len(lst)
    if direction.lower() == "left":
        return lst[n:] + lst[:n]
    elif direction.lower() == "right":
        return lst[-n:] + lst[:-n]
    else:
        raise ValueError("Direction must be 'left' or 'right'")


numbers = [1, 2, 3, 4, 5]
result_right = rotate_list_direction(numbers, 2, "right")
print(result_right)  # [4, 5, 1, 2, 3]

result_left = rotate_list_direction(numbers, 2, "left")
print(result_left)  # [3, 4, 5, 1, 2]


# 🧩 Rotate list with multiple rotations
# Function is defined in one of the above code block (rotate_list)


def rotate_list_multiple(lst, rotations):
    """Apply multiple rotations to a list."""
    result = lst.copy()
    for n in rotations:
        result = rotate_list(result, n)
    return result


numbers = [1, 2, 3, 4, 5]
rotations = [2, 1, 3]
result = rotate_list_multiple(numbers, rotations)
print(result)  # [5, 1, 2, 3, 4]

# Step-by-step breakdown
step1 = rotate_list(numbers, 2)  # [4, 5, 1, 2, 3]
step2 = rotate_list(step1, 1)  # [3, 4, 5, 1, 2]
step3 = rotate_list(step2, 3)  # [5, 1, 2, 3, 4]


# 🧩 Rotate list with condition
def rotate_list_conditional(lst, condition_func):
    """Rotate list based on a condition."""
    if not lst:
        return lst

    # Find the first element that meets the condition
    for i, item in enumerate(lst):
        if condition_func(item):
            # Rotate to bring this element to the front
            return lst[i:] + lst[:i]

    return lst  # No element meets condition


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Rotate to bring first even number to front
result = rotate_list_conditional(numbers, lambda x: x % 2 == 0)
print(result)  # [2, 3, 4, 5, 6, 7, 8, 1]

# Rotate to bring first number > 5 to front
result2 = rotate_list_conditional(numbers, lambda x: x > 5)
print(result2)  # [6, 7, 8, 1, 2, 3, 4, 5]


# 🧩 Rotate list with circular buffer
class CircularBuffer:
    """Circular buffer implementation with rotation."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def push(self, item):
        """Add item to buffer."""
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def rotate(self, n):
        """Rotate buffer by n positions."""
        if self.size == 0:
            return

        n = n % self.size
        # Rotate the head pointer
        self.head = (self.head - n) % self.capacity

    def to_list(self):
        """Convert buffer to list."""
        if self.size == 0:
            return []

        result = []
        for i in range(self.size):
            idx = (self.head - self.size + i) % self.capacity
            result.append(self.buffer[idx])
        return result


# Example usage
cb = CircularBuffer(5)
for i in range(1, 6):
    cb.push(i)

print(cb.to_list())  # [1, 2, 3, 4, 5]
cb.rotate(2)
print(cb.to_list())  # [4, 5, 1, 2, 3]


# 🧩 Rotate list with generator
def rotate_list_generator(lst, n):
    """Rotate list using generator for memory efficiency."""
    if not lst:
        return

    n = n % len(lst)
    # Yield elements in rotated order
    for i in range(len(lst)):
        idx = (i - n) % len(lst)
        yield lst[idx]


numbers = [1, 2, 3, 4, 5]
result = list(rotate_list_generator(numbers, 2))
print(result)  # [4, 5, 1, 2, 3]

# Memory efficient iteration
for item in rotate_list_generator(numbers, 2):
    print(item, end=" ")  # 4 5 1 2 3


# 🧩 Rotate list with performance monitoring
import time


# Function is defined in one of the above code block (rotate_list_generator)


# Function is defined in one of the above code block (rotate_list_inplace)


# Function is defined in one of the above code block (rotate_list)


def rotate_list_with_timing(lst, n, method="slice"):
    """Rotate list with performance monitoring."""
    start_time = time.time()

    if method == "slice":
        result = rotate_list(lst, n)
    elif method == "inplace":
        lst_copy = lst.copy()
        result = rotate_list_inplace(lst_copy, n)
    elif method == "generator":
        result = list(rotate_list_generator(lst, n))
    else:
        raise ValueError("Method must be 'slice', 'inplace', or 'generator'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "rotation": n,
        "method": method,
    }


# Performance comparison
large_list = list(range(100000))

slice_stats = rotate_list_with_timing(large_list, 50000, "slice")
inplace_stats = rotate_list_with_timing(large_list, 50000, "inplace")
generator_stats = rotate_list_with_timing(large_list, 50000, "generator")

print(f"Slice method: {slice_stats['execution_time']:.6f}s")
print(f"Inplace method: {inplace_stats['execution_time']:.6f}s")
print(f"Generator method: {generator_stats['execution_time']:.6f}s")


# 🧩 Rotate list with error handling
# Function is defined in one of the above code block (rotate_list_direction)


def rotate_list_safe(lst, n, direction="right"):
    """Safely rotate list with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not lst:
            return []

        if not isinstance(n, int):
            raise TypeError("Rotation amount must be an integer")

        return rotate_list_direction(lst, n, direction)

    except Exception as e:
        print(f"Error rotating list: {e}")
        return lst  # Return original list on error


# Safe rotation with error handling
try:
    result = rotate_list_safe([1, 2, 3, 4, 5], 2)
    print(result)  # [4, 5, 1, 2, 3]
except Exception as e:
    print(f"Error: {e}")

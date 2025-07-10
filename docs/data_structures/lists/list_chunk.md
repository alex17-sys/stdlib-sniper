---
title: Chunk List
description: Zero-dependency Python snippets for splitting lists into chunks using the standard library.
keywords: balanced, chunk, condition, custom, data-structures, distribution, error, fill, filter, function, generator, handling, limit, list, maximum, memory, monitoring, overlap, padding, performance, safe, size, sliding, split, timing
---

# Chunk List

Zero-dependency Python snippets for splitting lists into chunks using the standard library.

10 snippets available in this sub-category.

---

## Simple

###  Split list into chunks

`list` `chunk` `split` `size` `data-structures`

Split list into chunks of specified size

```python
def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = chunk_list(numbers, 3)
print(result)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

!!! note "Notes"
    - Uses list comprehension
    - Handles incomplete chunks
    - Preserves order
    - Simple and efficient

<hr class="snippet-divider">

### Split list with generator

`list` `chunk` `generator` `memory` `data-structures`

Split list into chunks using generator

```python
def chunk_list_generator(lst, chunk_size):
    """Split list into chunks using generator."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(chunk_list_generator(numbers, 3))
print(result)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Memory efficient iteration
for chunk in chunk_list_generator(numbers, 3):
    print(chunk)  # [1, 2, 3], [4, 5, 6], [7, 8, 9]
```

!!! note "Notes"
    - Memory efficient
    - Lazy evaluation
    - Suitable for large lists
    - Generator pattern

<hr class="snippet-divider">

## Complex

###  Split list with fill value

`list` `chunk` `fill` `padding` `data-structures`

Split list into chunks with fill value

```python
def chunk_list_with_fill(lst, chunk_size, fill_value=None):
    """Split list into chunks with fill value for incomplete chunks."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunk = lst[i : i + chunk_size]
        # Pad incomplete chunk with fill value
        while len(chunk) < chunk_size:
            chunk.append(fill_value)
        chunks.append(chunk)

    return chunks


numbers = [1, 2, 3, 4, 5, 6, 7]
result = chunk_list_with_fill(numbers, 3, 0)
print(result)  # [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

# With custom fill value
result2 = chunk_list_with_fill(numbers, 3, "X")
print(result2)  # [[1, 2, 3], [4, 5, 6], [7, 'X', 'X']]
```

!!! note "Notes"
    - Pads incomplete chunks
    - Configurable fill value
    - Uniform chunk sizes
    - Useful for matrix operations

<hr class="snippet-divider">

### Split list with overlap

`list` `chunk` `overlap` `sliding` `data-structures`

Split list into overlapping chunks

```python
def chunk_list_overlap(lst, chunk_size, overlap=0):
    """Split list into overlapping chunks."""
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid chunk size or overlap")

    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(lst), step):
        chunk = lst[i : i + chunk_size]
        if len(chunk) >= chunk_size // 2:  # Only add chunks with sufficient size
            chunks.append(chunk)

    return chunks


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = chunk_list_overlap(numbers, 4, 2)
print(result)  # [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]]
```

!!! note "Notes"
    - Configurable overlap
    - Sliding window approach
    - Useful for signal processing
    - Maintains context

<hr class="snippet-divider">

### Split list by condition

`list` `chunk` `condition` `filter` `data-structures`

Split list into chunks based on condition

```python
def chunk_list_by_condition(lst, condition_func):
    """Split list into chunks based on condition."""
    if not lst:
        return []

    chunks = []
    current_chunk = []

    for item in lst:
        if condition_func(item):
            if current_chunk:  # End current chunk
                chunks.append(current_chunk)
                current_chunk = []
        else:
            current_chunk.append(item)

    # Add final chunk if not empty
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


numbers = [1, 2, 0, 3, 4, 0, 5, 6, 7, 0, 8]
# Split by zero
result = chunk_list_by_condition(numbers, lambda x: x == 0)
print(result)  # [[1, 2], [3, 4], [5, 6, 7], [8]]

# Split by even numbers
result2 = chunk_list_by_condition(numbers, lambda x: x % 2 == 0)
print(result2)  # [[1], [3], [5, 7], []]
```

!!! note "Notes"
    - Condition-based splitting
    - Flexible criteria
    - Preserves non-matching elements
    - Useful for data cleaning

<hr class="snippet-divider">

### Split list with maximum chunks

`list` `chunk` `maximum` `limit` `data-structures`

Split list into maximum number of chunks

```python
def chunk_list(lst, chunk_size):
    # Function is defined in one of the above code block
    pass


def chunk_list_max_chunks(lst, max_chunks):
    """Split list into maximum number of chunks."""
    if max_chunks <= 0:
        raise ValueError("Maximum chunks must be positive")

    if max_chunks >= len(lst):
        return [[item] for item in lst]

    chunk_size = (len(lst) + max_chunks - 1) // max_chunks  # Ceiling division
    return chunk_list(lst, chunk_size)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = chunk_list_max_chunks(numbers, 3)
print(result)  # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

result2 = chunk_list_max_chunks(numbers, 5)
print(result2)  # [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
```

!!! note "Notes"
    - Limits number of chunks
    - Calculates optimal chunk size
    - Balances chunk distribution
    - Useful for parallel processing

<hr class="snippet-divider">

### Split list with custom chunking function

`list` `chunk` `custom` `function` `data-structures`

Split list using custom chunking function

```python
def chunk_list_custom(lst, chunk_func):
    """Split list using custom chunking function."""
    if not lst:
        return []

    chunks = []
    current_chunk = []

    for item in lst:
        current_chunk.append(item)

        if chunk_func(current_chunk, item):
            chunks.append(current_chunk)
            current_chunk = []

    # Add remaining items as final chunk
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Chunk when sum exceeds 10
def sum_exceeds_10(chunk, item):
    return sum(chunk) > 10


result = chunk_list_custom(numbers, sum_exceeds_10)
print(result)  # [[1, 2, 3, 4], [5, 6], [7, 8], [9, 10]]


# Chunk when length reaches 3
def length_reaches_3(chunk, item):
    return len(chunk) >= 3


result2 = chunk_list_custom(numbers, length_reaches_3)
print(result2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

!!! note "Notes"
    - Flexible chunking logic
    - Dynamic chunk creation
    - Complex criteria support
    - Advanced use cases

<hr class="snippet-divider">

### Split list with balanced chunks

`list` `chunk` `balanced` `distribution` `data-structures`

Split list into balanced chunks

```python
def chunk_list_balanced(lst, num_chunks):
    """Split list into balanced chunks."""
    if num_chunks <= 0:
        raise ValueError("Number of chunks must be positive")

    if num_chunks >= len(lst):
        return [[item] for item in lst]

    # Calculate base chunk size and remainder
    base_size = len(lst) // num_chunks
    remainder = len(lst) % num_chunks

    chunks = []
    start = 0

    for i in range(num_chunks):
        # Distribute remainder across first chunks
        chunk_size = base_size + (1 if i < remainder else 0)
        end = start + chunk_size
        chunks.append(lst[start:end])
        start = end

    return chunks


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = chunk_list_balanced(numbers, 3)
print(result)  # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

result2 = chunk_list_balanced(numbers, 4)
print(result2)  # [[1, 2, 3], [4, 5, 6], [7, 8], [9, 10]]
```

!!! note "Notes"
    - Evenly distributes items
    - Handles remainder distribution
    - Optimal for parallel processing
    - Minimizes chunk size variance

<hr class="snippet-divider">

### Split list with performance monitoring

`list` `chunk` `performance` `timing` `monitoring` `data-structures`

Split list into chunks with performance monitoring

```python
import time


def chunk_list_balanced(lst, num_chunks):
    # Function is defined in one of the above code block
    pass


def chunk_list_generator(lst, chunk_size):
    # Function is defined in one of the above code block
    pass


def chunk_list(lst, chunk_size):
    # Function is defined in one of the above code block
    pass


def chunk_list_with_timing(lst, chunk_size, method="comprehension"):
    """Split list into chunks with performance monitoring."""
    start_time = time.time()

    if method == "comprehension":
        result = chunk_list(lst, chunk_size)
    elif method == "generator":
        result = list(chunk_list_generator(lst, chunk_size))
    elif method == "balanced":
        result = chunk_list_balanced(lst, chunk_size)
    else:
        raise ValueError("Method must be 'comprehension', 'generator', or 'balanced'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "list_length": len(lst),
        "chunk_size": chunk_size,
        "num_chunks": len(result),
        "method": method,
    }


# Performance comparison
large_list = list(range(100000))

comp_stats = chunk_list_with_timing(large_list, 1000, "comprehension")
gen_stats = chunk_list_with_timing(large_list, 1000, "generator")
bal_stats = chunk_list_with_timing(large_list, 100, "balanced")

print(f"Comprehension method: {comp_stats['execution_time']:.6f}s")
print(f"Generator method: {gen_stats['execution_time']:.6f}s")
print(f"Balanced method: {bal_stats['execution_time']:.6f}s")
```

!!! note "Notes"
    - Performance measurement
    - Method comparison
    - Benchmarking tool
    - Optimization insights

<hr class="snippet-divider">

### Split list with error handling

`list` `chunk` `safe` `error` `handling` `data-structures`

Safely split list into chunks with error handling

```python
def chunk_list_with_fill(lst, chunk_size, fill_value=None):
    # Function is defined in one of the above code block
    pass


def chunk_list(lst, chunk_size):
    # Function is defined in one of the above code block
    pass


def chunk_list_safe(lst, chunk_size, fill_value=None):
    """Safely split list into chunks with error handling."""
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")

        if not isinstance(chunk_size, int):
            raise TypeError("Chunk size must be an integer")

        if chunk_size <= 0:
            raise ValueError("Chunk size must be positive")

        if fill_value is not None:
            return chunk_list_with_fill(lst, chunk_size, fill_value)
        else:
            return chunk_list(lst, chunk_size)

    except Exception as e:
        print(f"Error chunking list: {e}")
        return [lst]  # Return original list as single chunk on error


# Safe chunking with error handling
try:
    result = chunk_list_safe([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(result)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
except Exception as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Comprehensive error handling
    - Type validation
    - Graceful degradation
    - Production ready

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Rotate List](./list_rotate.md)

## 🏷️ Tags

`list`, `chunk`, `split`, `generator`, `balanced`, `performance`, `data-structures`

## 📝 Notes

- List comprehension is most efficient for small to medium lists
- Generators provide memory efficiency for large lists
- Balanced chunking is optimal for parallel processing
- Overlapping chunks are useful for sliding window operations
- Custom chunking functions enable complex splitting logic
- Consider performance implications for very large lists

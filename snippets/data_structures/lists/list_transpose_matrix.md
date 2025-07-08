# Transpose Matrix

Zero-dependency Python snippets for transposing 2D lists (matrices) using the standard library.

## Simple

### 🧩 Transpose 2D list

```python
def transpose_matrix(matrix):
    """Transpose a 2D list (matrix)."""
    if not matrix:
        return []

    # Use zip with unpacking to transpose
    return list(map(list, zip(*matrix)))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose_matrix(matrix)
print(result)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

📂 Transpose a 2D list using zip

🏷️ Tags: list, matrix, transpose, 2d, data-structures
📝 Notes:
- Uses zip with unpacking
- Swaps rows and columns
- Preserves data integrity
- Simple and efficient

### 🧩 Transpose matrix with list comprehension

```python
def transpose_matrix_comprehension(matrix):
    """Transpose matrix using list comprehension."""
    if not matrix:
        return []

    # Get dimensions
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Transpose using nested comprehension
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]


matrix = [[1, 2, 3], [4, 5, 6]]
result = transpose_matrix_comprehension(matrix)
print(result)  # [[1, 4], [2, 5], [3, 6]]
```

📂 Transpose matrix using list comprehension

🏷️ Tags: list, matrix, transpose, comprehension, data-structures
📝 Notes:
- Explicit dimension handling
- Nested comprehension
- Clear logic flow
- Educational approach

## Complex

### 🧩 Transpose matrix with validation

```python
def transpose_matrix_validated(matrix):
    """Transpose matrix with input validation."""
    if not matrix:
        return []

    # Check if all rows have the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("All rows must have the same length")

    # Check if matrix is rectangular
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Matrix cannot be empty")

    return list(map(list, zip(*matrix)))


# Valid matrix
matrix1 = [[1, 2, 3], [4, 5, 6]]
result1 = transpose_matrix_validated(matrix1)
print(result1)  # [[1, 4], [2, 5], [3, 6]]

# Invalid matrix (raises error)
try:
    matrix2 = [[1, 2, 3], [4, 5]]  # Different row lengths
    result2 = transpose_matrix_validated(matrix2)
except ValueError as e:
    print(f"Error: {e}")  # Error: All rows must have the same length
```

📂 Transpose matrix with input validation

🏷️ Tags: list, matrix, transpose, validation, error, data-structures
📝 Notes:
- Input validation
- Error handling
- Rectangular matrix check
- Safe operation

### 🧩 Transpose matrix with custom fill

```python
def transpose_matrix_with_fill(matrix, fill_value=None):
    """Transpose matrix with fill value for irregular shapes."""
    if not matrix:
        return []

    # Find maximum row length
    max_cols = max(len(row) for row in matrix)

    # Pad shorter rows with fill value
    padded_matrix = []
    for row in matrix:
        padded_row = row + [fill_value] * (max_cols - len(row))
        padded_matrix.append(padded_row)

    # Transpose the padded matrix
    return list(map(list, zip(*padded_matrix)))


matrix = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
result = transpose_matrix_with_fill(matrix, fill_value=0)
print(result)  # [[1, 4, 7], [2, 5, 8], [3, 0, 9], [0, 0, 10]]
```

📂 Transpose matrix with fill value for irregular shapes

🏷️ Tags: list, matrix, transpose, fill, irregular, data-structures
📝 Notes:
- Handles irregular matrices
- Configurable fill value
- Pads shorter rows
- Useful for data cleaning

### 🧩 Transpose matrix in place

```python
def transpose_matrix_inplace(matrix):
    """Transpose matrix in place (modifies original)."""
    if not matrix:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    # For square matrices, we can transpose in place
    if rows == cols:
        for i in range(rows):
            for j in range(i + 1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    else:
        # For non-square matrices, create new matrix
        return list(map(list, zip(*matrix)))


# Square matrix (in-place)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose_matrix_inplace(matrix)
print(result)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(matrix)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]] (original modified)
```

📂 Transpose matrix in place

🏷️ Tags: list, matrix, transpose, inplace, square, data-structures
📝 Notes:
- Modifies original matrix
- Only works for square matrices
- Memory efficient
- Swaps elements directly

### 🧩 Transpose matrix with generator

```python
def transpose_matrix_generator(matrix):
    """Transpose matrix using generator for memory efficiency."""
    if not matrix:
        return

    # Yield transposed rows one at a time
    for col in zip(*matrix):
        yield list(col)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Memory efficient iteration
for row in transpose_matrix_generator(matrix):
    print(row)  # [1, 4, 7], [2, 5, 8], [3, 6, 9]

# Convert to list if needed
result = list(transpose_matrix_generator(matrix))
print(result)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

📂 Transpose matrix using generator

🏷️ Tags: list, matrix, transpose, generator, memory, data-structures
📝 Notes:
- Memory efficient
- Lazy evaluation
- Suitable for large matrices
- Generator pattern

### 🧩 Transpose matrix with performance monitoring

```python
import time


def transpose_matrix_comprehension(matrix):
    # Function is defined in one of the above code block
    pass


def transpose_matrix_generator(matrix):
    # Function is defined in one of the above code block
    pass


def transpose_matrix_with_timing(matrix, method="zip"):
    """Transpose matrix with performance monitoring."""
    start_time = time.time()

    if method == "zip":
        result = list(map(list, zip(*matrix)))
    elif method == "comprehension":
        result = transpose_matrix_comprehension(matrix)
    elif method == "generator":
        result = list(transpose_matrix_generator(matrix))
    else:
        raise ValueError("Method must be 'zip', 'comprehension', or 'generator'")

    end_time = time.time()

    return {
        "result": result,
        "execution_time": end_time - start_time,
        "original_shape": (len(matrix), len(matrix[0]) if matrix else 0),
        "transposed_shape": (len(result), len(result[0]) if result else 0),
        "method": method,
    }


# Performance comparison
large_matrix = [[i + j * 1000 for j in range(100)] for i in range(100)]

zip_stats = transpose_matrix_with_timing(large_matrix, "zip")
comp_stats = transpose_matrix_with_timing(large_matrix, "comprehension")
gen_stats = transpose_matrix_with_timing(large_matrix, "generator")

print(f"Zip method: {zip_stats['execution_time']:.6f}s")
print(f"Comprehension method: {comp_stats['execution_time']:.6f}s")
print(f"Generator method: {gen_stats['execution_time']:.6f}s")
```

📂 Transpose matrix with performance monitoring

🏷️ Tags: list, matrix, transpose, performance, timing, monitoring, data-structures
📝 Notes:
- Performance measurement
- Method comparison
- Shape information
- Benchmarking tool

### 🧩 Transpose matrix with error handling

```python
def transpose_matrix_safe(matrix):
    """Safely transpose matrix with error handling."""
    try:
        if not matrix:
            return []

        # Check if input is a list of lists
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("Matrix must be a list of lists")

        # Check if matrix is empty
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        # Check if all rows have the same length
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows must have the same length")

        return list(map(list, zip(*matrix)))

    except Exception as e:
        print(f"Error transposing matrix: {e}")
        return []  # Return empty list on error


# Safe transposition with error handling
try:
    result = transpose_matrix_safe([[1, 2, 3], [4, 5, 6]])
    print(result)  # [[1, 4], [2, 5], [3, 6]]
except Exception as e:
    print(f"Error: {e}")
```

📂 Safely transpose matrix with error handling

🏷️ Tags: list, matrix, transpose, safe, error, handling, data-structures
📝 Notes:
- Comprehensive error handling
- Type validation
- Graceful degradation
- Production ready

### 🧩 Transpose matrix with custom transformation

```python
def transpose_matrix_transform(matrix, transform_func=None):
    """Transpose matrix with custom element transformation."""
    if transform_func is None:
        def transform_func(x):
            return x

    if not matrix:
        return []

    # Transpose and apply transformation
    transposed = zip(*matrix)
    return [[transform_func(element) for element in row] for row in transposed]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Double each element
def double_element(x):
    return x * 2


result = transpose_matrix_transform(matrix, double_element)
print(result)  # [[2, 8, 14], [4, 10, 16], [6, 12, 18]]

# Convert to strings
result2 = transpose_matrix_transform(matrix, str)
print(result2)  # [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
```

📂 Transpose matrix with custom element transformation

🏷️ Tags: list, matrix, transpose, transform, custom, data-structures
📝 Notes:
- Custom element processing
- Flexible transformation
- Data type conversion
- Advanced use cases

## 🔗 Cross-References

- **Reference**: See [📂 Flatten List](./list_flatten.md)
- **Reference**: See [📂 Remove Duplicates From List](./list_remove_duplicates.md)
- **Reference**: See [📂 Sort List](./list_sort.md)
- **Reference**: See [📂 Rotate List](./list_zip.md)

## 🏷️ Tags

`list`, `matrix`, `transpose`, `2d`, `generator`, `performance`, `data-structures`

## 📝 Notes

- Zip method is most efficient for standard transposition
- Generators provide memory efficiency for large matrices
- In-place transposition only works for square matrices
- Custom transformations enable data processing during transposition
- Always validate matrix structure for production use
- Consider performance implications for very large matrices

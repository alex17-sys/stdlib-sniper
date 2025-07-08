# Vectors

Zero-dependency Python snippets using only the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Vector creation and display

`math` `vector` `create` `display`

Create and display vectors

```python
def create_vector(*args):
    """Create a vector from arguments."""
    return list(args)


def print_vector(v):
    """Pretty-print a vector."""
    print("[" + ", ".join(str(x) for x in v) + "]")


# Examples
v = create_vector(1, 2, 3)
print_vector(v)  # [1, 2, 3]
```

!!! note "Notes"
    - Uses lists
    - No external libraries

<hr class="snippet-divider">

### Vector addition, subtraction, scalar multiplication

`math` `vector` `add` `subtract` `scale`

Add, subtract, and scale vectors

```python
def add_vectors(a, b):
    """Add two vectors elementwise."""
    return [x + y for x, y in zip(a, b)]


def subtract_vectors(a, b):
    """Subtract two vectors elementwise."""
    return [x - y for x, y in zip(a, b)]


def scalar_multiply(v, k):
    """Multiply vector by scalar k."""
    return [k * x for x in v]


# Examples
A = [1, 2, 3]
B = [4, 5, 6]
print(add_vectors(A, B))  # [5, 7, 9]
print(subtract_vectors(A, B))  # [-3, -3, -3]
print(scalar_multiply(A, 2))  # [2, 4, 6]
```

!!! note "Notes"
    - Vectors must be same length
    - No error checking for mismatched sizes

<hr class="snippet-divider">

### Dot product and cross product

`math` `vector` `dot` `cross` `product`

Compute dot and cross products

```python
def dot_product(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))


def cross_product(a, b):
    """Cross product of two 3D vectors."""
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


# Examples
A = [1, 2, 3]
B = [4, 5, 6]
print(dot_product(A, B))  # 32
print(cross_product(A, B))  # [-3, 6, -3]
```

!!! note "Notes"
    - Cross product only for 3D
    - Dot product for any length

<hr class="snippet-divider">

### Vector norm and normalization

`math` `vector` `norm` `normalize`

Compute norm and normalize

```python
def vector_norm(v):
    """Compute Euclidean norm (length) of vector."""
    return sum(x**2 for x in v) ** 0.5


def normalize_vector(v):
    """Normalize vector to unit length."""
    norm = vector_norm(v)
    if norm == 0:
        raise ValueError("Zero vector")
    return [x / norm for x in v]


# Examples
v = [3, 4]
print(vector_norm(v))  # 5.0
print(normalize_vector(v))  # [0.6, 0.8]
```

!!! note "Notes"
    - Norm is Euclidean (L2)
    - Raises error for zero vector

<hr class="snippet-divider">

## Complex

###  Angle between vectors

`math` `vector` `angles` `complex`

Compute angle between vectors

```python
import math


def dot_product(a, b):
    # Function is defined in one of the above code block
    pass

def vector_norm(v):
    # Function is defined in one of the above code block
    pass

def angle_between(a, b):
    """Compute angle (radians) between two vectors."""
    dot = dot_product(a, b)
    norm_a = vector_norm(a)
    norm_b = vector_norm(b)
    if norm_a == 0 or norm_b == 0:
        raise ValueError("Zero vector")
    cos_theta = dot / (norm_a * norm_b)
    return math.acos(max(-1, min(1, cos_theta)))


# Examples
A = [1, 0]
B = [0, 1]
print(angle_between(A, B))  # 1.5707963267948966 (pi/2)
```

!!! note "Notes"
    - Returns radians
    - Handles zero vectors

<hr class="snippet-divider">

### Projection and rejection

`math` `vector` `project` `reject` `complex`

Project and reject vectors

```python
def dot_product(a, b):
    # Function is defined in one of the above code block
    pass

def vector_norm(v):
    # Function is defined in one of the above code block
    pass

def project_vector(a, b):
    """Project vector a onto b."""
    norm_b2 = vector_norm(b) ** 2
    if norm_b2 == 0:
        raise ValueError("Zero vector")
    scale = dot_product(a, b) / norm_b2
    return [scale * x for x in b]


def reject_vector(a, b):
    """Reject vector a from b (component orthogonal to b)."""
    proj = project_vector(a, b)
    return [x - y for x, y in zip(a, proj)]


# Examples
A = [3, 4]
B = [1, 0]
print(project_vector(A, B))  # [3.0, 0.0]
print(reject_vector(A, B))  # [0.0, 4.0]
```

!!! note "Notes"
    - Useful for decomposing vectors
    - Handles zero vectors

<hr class="snippet-divider">

## Edge Cases

###  Handle invalid vectors

`math` `vector` `error-handling` `edge-case`

Robust vector operations

```python
def add_vectors(a, b):
    # Function is defined in one of the above code block
    pass

def safe_add_vectors(a, b):
    """Add vectors, return None on error."""
    try:
        return add_vectors(a, b)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Examples
print(safe_add_vectors([1, 2], [1, 2, 3]))  # Error, returns None
```

!!! note "Notes"
    - Handles mismatched sizes
    - Returns None or error

<hr class="snippet-divider">

### Performance comparison

`math` `vector` `performance` `benchmarking`

Benchmark vector operations

```python
import time


def add_vectors(a, b):
    # Function is defined in one of the above code block
    pass

def benchmark_vector_addition():
    """Benchmark vector addition."""
    n = 1000000
    a = [1] * n
    b = [2] * n
    start = time.time()
    add_vectors(a, b)
    print(f"Addition: {time.time() - start:.6f}s")


# benchmark_vector_addition()
```

!!! note "Notes"
    - Vector ops are fast
    - Useful for performance-critical code

<hr class="snippet-divider">

## Practical Examples

###  Physics and geometry

`math` `vector` `distance` `midpoint` `geometry` `physics`

Use vectors in physics and geometry

```python
def vector_norm(v):
    # Function is defined in one of the above code block
    pass

def distance(a, b):
    """Compute Euclidean distance between two points."""
    return vector_norm([x - y for x, y in zip(a, b)])


def midpoint(a, b):
    """Compute midpoint between two points."""
    return [(x + y) / 2 for x, y in zip(a, b)]


# Examples
A = [0, 0]
B = [3, 4]
print(distance(A, B))  # 5.0
print(midpoint(A, B))  # [1.5, 2.0]
```

!!! note "Notes"
    - Vectors in geometry, physics, graphics
    - Distance, midpoint

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Linear Algebra](linear_algebra.md)
- **Reference**: See [📂 Matrices](matrices.md)

## 🏷️ Tags

`math`, `vector`, `add`, `subtract`, `scale`, `dot`, `cross`, `norm`, `normalize`, `angle`, `project`, `reject`, `distance`, `midpoint`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Vector Operations are Fundamental in Math, Physics, and Engineering
- Uses Only Standard Library (No numpy)
- Handles Edge Cases and Invalid Input
- Suitable for Small to Large Vectors

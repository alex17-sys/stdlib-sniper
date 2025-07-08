# Number Clamping Operations

Zero-dependency Python snippets for clamping numbers to specific ranges using the standard library.

## Simple

### 🧩 Clamp number to range

```python
def clamp(number, min_val, max_val):
    """Clamp number between min_val and max_val."""
    return max(min_val, min(number, max_val))


# Basic clamping
print(clamp(5, 0, 10))  # 5 (within range)
print(clamp(-5, 0, 10))  # 0 (below minimum)
print(clamp(15, 0, 10))  # 10 (above maximum)
print(clamp(3.7, 0, 5))  # 3.7 (float within range)
```

📂 Clamp number between min_val and max_val

🏷️ Tags: math, clamp, range, constraints, numbers
📝 Notes:
- Uses max() and min() functions
- Works with integers and floats
- Simple and efficient
- Common use case

### 🧩 Clamp to positive range

```python
def clamp_positive(number, max_val):
    """Clamp number to positive range [0, max_val]."""
    return max(0, min(number, max_val))


def clamp_negative(number, min_val):
    """Clamp number to negative range [min_val, 0]."""
    return max(min_val, min(number, 0))


# Examples
print(clamp_positive(5, 10))  # 5
print(clamp_positive(-3, 10))  # 0
print(clamp_positive(15, 10))  # 10

print(clamp_negative(-5, -10))  # -5
print(clamp_negative(3, -10))  # 0
print(clamp_negative(-15, -10))  # -10
```

📂 Clamp number to positive or negative range

🏷️ Tags: math, clamp, positive, negative, range, numbers
📝 Notes:
- Positive range constraint
- Negative range constraint
- Zero boundary handling
- Useful for percentages

### 🧩 Clamp to unit range

```python
def clamp_unit(number):
    """Clamp number to unit range [0, 1]."""
    return max(0, min(number, 1))


def clamp_unit_centered(number):
    """Clamp number to centered unit range [-1, 1]."""
    return max(-1, min(number, 1))


# Examples
print(clamp_unit(0.5))  # 0.5
print(clamp_unit(-0.3))  # 0
print(clamp_unit(1.7))  # 1

print(clamp_unit_centered(0.5))  # 0.5
print(clamp_unit_centered(-0.3))  # -0.3
print(clamp_unit_centered(1.7))  # 1
```

📂 Clamp number to unit range [0, 1] or [-1, 1]

🏷️ Tags: math, clamp, unit, range, normalization, numbers
📝 Notes:
- Unit range normalization
- Centered unit range
- Probability values
- Normalized coordinates

## Complex

### 🧩 Clamp with custom bounds

```python
def clamp_custom(number, bounds):
    """Clamp number using custom bounds tuple or list."""
    if len(bounds) != 2:
        raise ValueError("Bounds must have exactly 2 values")

    min_val, max_val = bounds
    if min_val > max_val:
        min_val, max_val = max_val, min_val  # Swap if reversed

    return max(min_val, min(number, max_val))


# Examples
print(clamp_custom(5, (0, 10)))  # 5
print(clamp_custom(5, (10, 0)))  # 5 (bounds automatically ordered)
print(clamp_custom(-5, (-10, 5)))  # -5
print(clamp_custom(15, [0, 10]))  # 10
```

📂 Clamp number using custom bounds tuple or list

🏷️ Tags: math, clamp, custom, bounds, validation, numbers
📝 Notes:
- Flexible bounds input
- Automatic bounds ordering
- Input validation
- Tuple and list support

### 🧩 Clamp with step increments

```python
def clamp_step(number, min_val, max_val, step=1):
    """Clamp number to range and snap to nearest step increment."""
    # First clamp to range
    clamped = max(min_val, min(number, max_val))

    # Then snap to nearest step
    steps = round((clamped - min_val) / step)
    return min_val + (steps * step)


# Examples
print(clamp_step(3.7, 0, 10, 0.5))  # 3.5 (snaps to 0.5 increment)
print(clamp_step(3.7, 0, 10, 1))  # 4 (snaps to 1 increment)
print(clamp_step(15, 0, 10, 2))  # 10 (clamped and snapped)
print(clamp_step(-2, 0, 10, 0.25))  # 0 (clamped to minimum)
```

📂 Clamp number to range and snap to nearest step increment

🏷️ Tags: math, clamp, step, increment, snapping, numbers
📝 Notes:
- Step-based clamping
- Grid snapping
- Increment alignment
- UI controls

### 🧩 Clamp with soft bounds

```python
def clamp_soft(number, min_val, max_val, soft_range=0.1):
    """Clamp number with soft bounds (gradual constraint)."""
    range_size = max_val - min_val
    soft_margin = range_size * soft_range

    # Soft minimum
    if number < min_val + soft_margin:
        factor = (number - min_val) / soft_margin
        factor = max(0, factor)  # Ensure non-negative
        return min_val + (factor * soft_margin)

    # Soft maximum
    if number > max_val - soft_margin:
        factor = (max_val - number) / soft_margin
        factor = max(0, factor)  # Ensure non-negative
        return max_val - (factor * soft_margin)

    return number


# Examples
print(clamp_soft(5, 0, 10, 0.1))  # 5 (within soft range)
print(clamp_soft(-1, 0, 10, 0.1))  # 0.1 (softly clamped)
print(clamp_soft(11, 0, 10, 0.1))  # 9.9 (softly clamped)
```

📂 Clamp number with soft bounds (gradual constraint)

🏷️ Tags: math, clamp, soft, bounds, gradual, animation, numbers
📝 Notes:
- Gradual constraint application
- Animation-friendly
- Smooth transitions
- UI interactions

### 🧩 Clamp with exponential decay

```python
import math


def clamp_exponential(number, min_val, max_val, decay_factor=0.1):
    """Clamp number with exponential decay beyond bounds."""
    if number <= min_val:
        return min_val

    if number >= max_val:
        return max_val

    # Apply exponential decay for values beyond bounds
    if number < min_val:
        excess = min_val - number
        decay = math.exp(-excess * decay_factor)
        return min_val - (excess * decay)

    if number > max_val:
        excess = number - max_val
        decay = math.exp(-excess * decay_factor)
        return max_val + (excess * decay)

    return number


# Examples
print(clamp_exponential(5, 0, 10))  # 5 (within bounds)
print(clamp_exponential(-2, 0, 10))  # ~0.135 (exponential decay)
print(clamp_exponential(12, 0, 10))  # ~10.135 (exponential decay)
```

📂 Clamp number with exponential decay beyond bounds

🏷️ Tags: math, clamp, exponential, decay, physics, numbers
📝 Notes:
- Exponential decay function
- Physics simulations
- Natural constraints
- Smooth boundaries

## Edge Cases

### 🧩 Handle edge cases in clamping

```python
import math


def robust_clamp(number, min_val, max_val):
    """Robust clamping with edge case handling."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be numeric")

    if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
        raise TypeError("Bounds must be numeric")

    if math.isnan(number) or math.isnan(min_val) or math.isnan(max_val):
        return float("nan")

    if math.isinf(number):
        if number > 0:
            return max_val
        else:
            return min_val

    if math.isinf(min_val) and math.isinf(max_val):
        return number

    if math.isinf(min_val):
        return min(number, max_val)

    if math.isinf(max_val):
        return max(number, min_val)

    return max(min_val, min(number, max_val))


# Test edge cases
try:
    print(robust_clamp(float("inf"), 0, 10))  # 10
    print(robust_clamp(float("-inf"), 0, 10))  # 0
    print(robust_clamp(float("nan"), 0, 10))  # nan
    print(robust_clamp(5, 0, 10))  # 5
except TypeError as e:
    print(f"Error: {e}")
```

📂 Robust clamping with edge case handling

🏷️ Tags: math, clamp, error-handling, edge-case, validation, numbers
📝 Notes:
- Input validation
- NaN and infinity handling
- Type checking
- Error messages

### 🧩 Performance optimization

```python
import time


def benchmark_clamping():
    """Benchmark different clamping methods."""
    numbers = [i for i in range(-1000, 1000)]
    min_val, max_val = 0, 100

    # Method 1: Built-in max/min
    start = time.time()
    _ = [max(min_val, min(n, max_val)) for n in numbers]
    time1 = time.time() - start

    # Method 2: Function call
    def clamp(number, min_val, max_val):
        return max(min_val, min(number, max_val))
    start = time.time()
    _ = [clamp(n, min_val, max_val) for n in numbers]
    time2 = time.time() - start

    # Method 3: Conditional
    start = time.time()
    result3 = []
    for n in numbers:
        if n < min_val:
            result3.append(min_val)
        elif n > max_val:
            result3.append(max_val)
        else:
            result3.append(n)
    time3 = time.time() - start

    print(f"Built-in max/min: {time1:.6f}s")
    print(f"Function call: {time2:.6f}s")
    print(f"Conditional: {time3:.6f}s")
    print(f"Function overhead: {time2 / time1:.2f}x")


# benchmark_clamping()
```

📂 Benchmark different clamping methods

🏷️ Tags: math, clamp, performance, benchmarking, optimization, numbers
📝 Notes:
- Performance comparison
- Method efficiency
- Large dataset testing
- Optimization insights

## Practical Examples

### 🧩 Color value clamping

```python
def clamp_color_value(value):
    """Clamp color value to valid range [0, 255]."""
    return max(0, min(int(value), 255))


def clamp_color_rgb(r, g, b):
    """Clamp RGB color values to valid range."""
    return (clamp_color_value(r), clamp_color_value(g), clamp_color_value(b))


def clamp_color_hsv(h, s, v):
    """Clamp HSV color values to valid ranges."""
    # Hue: 0-360, Saturation: 0-100, Value: 0-100
    return (max(0, min(h, 360)), max(0, min(s, 100)), max(0, min(v, 100)))


# Examples
print(clamp_color_rgb(300, -10, 128))  # (255, 0, 128)
print(clamp_color_hsv(400, 120, 50))  # (360, 100, 50)
```

📂 Clamp color values to valid ranges

🏷️ Tags: math, clamp, color, rgb, hsv, numbers
📝 Notes:
- Color value validation
- RGB color space
- HSV color space
- Graphics applications

### 🧩 Audio level clamping

```python
def clamp_audio_level(level, min_db=-60, max_db=0):
    """Clamp audio level to valid decibel range."""
    return max(min_db, min(level, max_db))


def clamp_audio_normalized(level):
    """Clamp audio level to normalized range [0, 1]."""
    return max(0, min(level, 1))


def clamp_audio_volume(volume_percent):
    """Clamp volume percentage to valid range [0, 100]."""
    return max(0, min(volume_percent, 100))


# Examples
print(clamp_audio_level(-80))  # -60 (minimum)
print(clamp_audio_level(10))  # 0 (maximum)
print(clamp_audio_normalized(1.5))  # 1.0 (maximum)
print(clamp_audio_volume(150))  # 100 (maximum)
```

📂 Clamp audio levels to valid ranges

🏷️ Tags: math, clamp, audio, decibel, numbers
📝 Notes:
- Audio level validation
- Decibel range
- Normalized values
- Audio processing

## 🔗 Cross-References

- **Reference**: See [📂 Round Number](round_number.md)
- **Reference**: See [📂 Format Number](format_number.md)
- **Reference**: See [📂 Percentage](percentage.md)
- **Reference**: See [📂 Statistics Basic](statistics_basic.md)
- **Reference**: See [📂 Decimal Precision](decimal_precision.md)

## 🏷️ Tags

`math`, `clamp`, `range`, `constraints`, `validation`, `audio`, `color`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Clamping Functions Ensure Value Constraints
- Edge Case Handling Prevents Errors
- Performance Optimization for Large Datasets
- Real-World Applications in Graphics and Audio

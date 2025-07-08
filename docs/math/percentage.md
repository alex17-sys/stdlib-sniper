# Percentage Operations

Zero-dependency Python snippets using only the standard library.

11 snippets available in this sub-category.

---

## Simple

###  Calculate percentage

`math` `percentage` `calculation` `ratio` `numbers`

Calculate what percentage part is of total

```python
def calculate_percentage(part, total):
    """Calculate what percentage part is of total."""
    if total == 0:
        return 0
    return (part / total) * 100


# Basic percentage calculations
print(calculate_percentage(25, 100))  # 25.0
print(calculate_percentage(3, 10))  # 30.0
print(calculate_percentage(0, 50))  # 0.0
print(calculate_percentage(75, 200))  # 37.5
```

!!! note "Notes"
    - Simple division and multiplication
    - Handles zero total case
    - Returns float result
    - Common use case

<hr class="snippet-divider">

### Calculate percentage change

`math` `percentage` `change` `growth` `decrease` `numbers`

Calculate percentage change from old to new value

```python
def percentage_change(old_value, new_value):
    """Calculate percentage change from old to new value."""
    if old_value == 0:
        return float("inf") if new_value > 0 else 0
    return ((new_value - old_value) / old_value) * 100


# Examples
print(percentage_change(100, 120))  # 20.0 (20% increase)
print(percentage_change(100, 80))  # -20.0 (20% decrease)
print(percentage_change(50, 75))  # 50.0 (50% increase)
print(percentage_change(200, 150))  # -25.0 (25% decrease)
```

!!! note "Notes"
    - Growth and decline calculation
    - Handles zero old value
    - Positive for increase
    - Negative for decrease

<hr class="snippet-divider">

### Calculate percentage of number

`math` `percentage` `calculation` `proportion` `numbers`

Calculate what percentage% of number is

```python
def percentage_of(percentage, number):
    """Calculate what percentage% of number is."""
    return (percentage / 100) * number


# Examples
print(percentage_of(25, 200))  # 50.0 (25% of 200)
print(percentage_of(10, 1000))  # 100.0 (10% of 1000)
print(percentage_of(50, 80))  # 40.0 (50% of 80)
print(percentage_of(0, 100))  # 0.0 (0% of 100)
```

!!! note "Notes"
    - Reverse percentage calculation
    - Simple multiplication
    - Useful for discounts
    - Common business calculation

<hr class="snippet-divider">

## Complex

###  Calculate compound percentage

`math` `percentage` `compound` `growth` `finance` `numbers`

Calculate compound percentage over multiple periods

```python
def percentage_change(old_value, new_value):
    # Function is defined in one of the above code block
    pass


def compound_percentage(initial, percentage, periods):
    """Calculate compound percentage over multiple periods."""
    multiplier = (1 + percentage / 100) ** periods
    return initial * multiplier


def compound_percentage_change(initial, percentage, periods):
    """Calculate the total percentage change over multiple periods."""
    final = compound_percentage(initial, percentage, periods)
    return percentage_change(initial, final)


# Examples
print(compound_percentage(1000, 5, 3))  # 1157.625 (5% compound for 3 years)
print(compound_percentage_change(1000, 5, 3))  # 15.7625 (total change)
print(compound_percentage(100, -10, 2))  # 81.0 (10% decrease for 2 years)
```

!!! note "Notes"
    - Compound interest calculation
    - Multiple period growth
    - Exponential growth
    - Financial applications

<hr class="snippet-divider">

### Calculate weighted percentage

`math` `percentage` `weighted` `average` `grades` `numbers`

Calculate weighted percentage average

```python
def weighted_percentage(values, weights):
    """Calculate weighted percentage average."""
    if len(values) != len(weights):
        raise ValueError("Values and weights must have same length")

    if sum(weights) == 0:
        return 0

    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight


# Examples
grades = [85, 90, 78, 92]
weights = [0.3, 0.3, 0.2, 0.2]  # 30%, 30%, 20%, 20%

final_grade = weighted_percentage(grades, weights)
print(f"Final grade: {final_grade:.1f}%")  # Final grade: 86.7%
```

!!! note "Notes"
    - Weighted average calculation
    - Grade point average
    - Investment portfolio
    - Statistical analysis

<hr class="snippet-divider">

### Calculate percentage difference

`math` `percentage` `difference` `comparison` `relative` `numbers`

Calculate percentage difference between two values

```python
def percentage_difference(value1, value2):
    """Calculate percentage difference between two values."""
    if value1 == 0 and value2 == 0:
        return 0

    if value1 == 0 or value2 == 0:
        return float("inf")

    return abs((value1 - value2) / ((value1 + value2) / 2)) * 100


# Examples
print(percentage_difference(100, 120))  # 18.18... (difference relative to average)
print(percentage_difference(80, 100))  # 22.22... (difference relative to average)
print(percentage_difference(50, 50))  # 0.0 (no difference)
```

!!! note "Notes"
    - Relative difference calculation
    - Uses average as reference
    - Always positive result
    - Statistical comparison

<hr class="snippet-divider">

### Calculate percentage points

`math` `percentage` `points` `difference` `direction` `numbers`

Calculate difference in percentage points

```python
def percentage_points(percentage1, percentage2):
    """Calculate difference in percentage points."""
    return percentage2 - percentage1


def percentage_points_change(percentage1, percentage2):
    """Calculate percentage point change with direction."""
    change = percentage2 - percentage1
    direction = "increase" if change > 0 else "decrease" if change < 0 else "no change"
    return change, direction


# Examples
print(percentage_points(25, 30))  # 5.0 (5 percentage points)
print(percentage_points(40, 35))  # -5.0 (5 percentage points decrease)

change, direction = percentage_points_change(25, 30)
print(f"{change} percentage point {direction}")  # 5.0 percentage point increase
```

!!! note "Notes"
    - Percentage point difference
    - Direction indication
    - Polling statistics
    - Policy analysis

<hr class="snippet-divider">

## Edge Cases

###  Handle edge cases in percentage calculations

`math` `percentage` `error-handling` `edge-case` `validation` `numbers`

Robust percentage calculation with edge case handling

```python
import math


def robust_percentage(part, total, places=2):
    """Robust percentage calculation with edge case handling."""
    if not isinstance(part, (int, float)) or not isinstance(total, (int, float)):
        raise TypeError("Values must be numbers")

    if total == 0:
        if part == 0:
            return 0.0
        else:
            return float("inf")

    if math.isnan(part) or math.isnan(total):
        return float("nan")

    if math.isinf(part) or math.isinf(total):
        return float("nan")

    return round((part / total) * 100, places)


# Test edge cases
try:
    print(robust_percentage(0, 0))  # 0.0
    print(robust_percentage(5, 0))  # inf
    print(robust_percentage(float("nan"), 10))  # nan
    print(robust_percentage(25, 100, 3))  # 25.0
except TypeError as e:
    print(f"Error: {e}")
```

!!! note "Notes"
    - Input validation
    - NaN and infinity handling
    - Zero division handling
    - Precision control

<hr class="snippet-divider">

### Performance optimization

`math` `percentage` `performance` `benchmarking` `optimization` `numbers`

Benchmark percentage calculation methods

```python
import time


def calculate_percentage(part, total):
    # Function is defined in one of the above code block
    pass


def benchmark_percentage():
    """Benchmark percentage calculation methods."""
    data = [(i, i * 2) for i in range(1, 100000)]

    # Method 1: Direct calculation
    start = time.time()
    _ = [(p / t) * 100 for p, t in data]
    time1 = time.time() - start

    # Method 2: Function call
    start = time.time()
    _ = [calculate_percentage(p, t) for p, t in data]
    time2 = time.time() - start

    print(f"Direct calculation: {time1:.6f}s")
    print(f"Function call: {time2:.6f}s")
    print(f"Overhead: {time2 / time1:.2f}x")


# benchmark_percentage()
```

!!! note "Notes"
    - Performance comparison
    - Function call overhead
    - Large dataset testing
    - Optimization insights

<hr class="snippet-divider">

## Practical Examples

###  Grade calculation

`math` `percentage` `grades` `education` `weighted` `numbers`

Calculate final grade with weighted percentages

```python
def calculate_final_grade(assignments, exams, participation=0):
    """Calculate final grade with weighted percentages."""
    # Weight assignments 40%, exams 50%, participation 10%
    assignment_avg = sum(assignments) / len(assignments) if assignments else 0
    exam_avg = sum(exams) / len(exams) if exams else 0

    final_grade = assignment_avg * 0.4 + exam_avg * 0.5 + participation * 0.1
    return round(final_grade, 1)


# Example
assignments = [85, 92, 78, 88]
exams = [90, 85]
participation = 95

final = calculate_final_grade(assignments, exams, participation)
print(f"Final grade: {final}%")  # Final grade: 87.1%
```

!!! note "Notes"
    - Academic grading
    - Weighted components
    - Final grade calculation
    - Educational applications

<hr class="snippet-divider">

### Sales analysis

`math` `percentage` `sales` `business` `analysis` `numbers`

Analyze sales performance with percentage metrics

```python
def calculate_percentage(part, total):
    # Function is defined in one of the above code block
    pass


def analyze_sales_performance(sales_data):
    """Analyze sales performance with percentage metrics."""
    total_sales = sum(sales_data.values())
    analysis = {}

    for product, sales in sales_data.items():
        percentage = calculate_percentage(sales, total_sales)
        analysis[product] = {
            "sales": sales,
            "percentage": round(percentage, 1),
            "contribution": f"{percentage:.1f}%",
        }

    return analysis


# Example
sales = {"Product A": 50000, "Product B": 30000, "Product C": 20000, "Product D": 10000}

performance = analyze_sales_performance(sales)
for product, data in performance.items():
    print(f"{product}: {data['contribution']} of total sales")
# Product A: 45.5% of total sales
# Product B: 27.3% of total sales
# Product C: 18.2% of total sales
# Product D: 9.1% of total sales
```

!!! note "Notes"
    - Business analytics
    - Sales contribution
    - Performance metrics
    - Market analysis

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Round Number](round_number.md)
- **Reference**: See [📂 Format Number](format_number.md)
- **Reference**: See [📂 Statistics Basic](statistics_basic.md)
- **Reference**: See [📂 Clamp Number](clamp_number.md)
- **Reference**: See [📂 Decimal Precision](decimal_precision.md)

## 🏷️ Tags

`math`, `percentage`, `calculation`, `growth`, `finance`, `statistics`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Percentage Functions Support Business Calculations
- Edge Case Handling Ensures Robustness
- Performance Considerations for Large Datasets
- Real-World Applications in Finance and Analytics

# Advanced Statistics Operations

Zero-dependency Python snippets for advanced statistics using the standard library.

## Simple

### 🧩 Calculate variance and standard deviation

```python
import statistics


def variance(values, sample=True):
    """Calculate variance (sample or population)."""
    if sample:
        return statistics.variance(values)
    else:
        return statistics.pvariance(values)


def stddev(values, sample=True):
    """Calculate standard deviation (sample or population)."""
    if sample:
        return statistics.stdev(values)
    else:
        return statistics.pstdev(values)


# Examples
nums = [2, 4, 4, 4, 5, 5, 7, 9]
print(f"Sample variance: {variance(nums):.2f}")  # 4.57
print(f"Population variance: {variance(nums, False):.2f}")  # 4.00
print(f"Sample stddev: {stddev(nums):.2f}")  # 2.14
print(f"Population stddev: {stddev(nums, False):.2f}")  # 2.00
```

📂 Calculate variance and standard deviation

🏷️ Tags: math, statistics, variance, stddev, advanced
📝 Notes:
- Sample vs population
- Uses statistics module
- Returns float

### 🧩 Calculate quantiles, percentiles, and IQR

```python
import statistics


def quantiles(values, n=4):
    """Divide data into n quantiles (default: quartiles)."""
    return statistics.quantiles(values, n=n)


def percentile(values, percent):
    """Calculate the value at a given percentile (0-100)."""
    k = (len(values) - 1) * percent / 100
    f = int(k)
    c = min(f + 1, len(values) - 1)
    if f == c:
        return sorted(values)[int(k)]
    d0 = sorted(values)[f] * (c - k)
    d1 = sorted(values)[c] * (k - f)
    return d0 + d1


def interquartile_range(values):
    """Calculate interquartile range (IQR)."""
    q1, q3 = quantiles(values, 4)[0], quantiles(values, 4)[2]
    return q3 - q1


# Examples
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Quartiles: {quantiles(nums)}")  # [3.0, 5.0, 7.0]
print(f"90th percentile: {percentile(nums, 90)}")  # 8.2
print(f"IQR: {interquartile_range(nums)}")  # 4.0
```

📂 Calculate quantiles, percentiles, and IQR

🏷️ Tags: math, statistics, quantiles, percentiles, iqr, advanced
📝 Notes:
- Quartiles, percentiles
- Interquartile range for spread
- Useful for box plots

### 🧩 Calculate skewness and kurtosis (manual)

```python
import statistics


def skewness(values):
    """Calculate sample skewness (Fisher-Pearson)."""
    n = len(values)
    mean_val = statistics.mean(values)
    std_val = statistics.stdev(values)
    return (sum((x - mean_val) ** 3 for x in values) / n) / (std_val**3)


def kurtosis(values):
    """Calculate sample kurtosis (excess)."""
    n = len(values)
    mean_val = statistics.mean(values)
    std_val = statistics.stdev(values)
    return (sum((x - mean_val) ** 4 for x in values) / n) / (std_val**4) - 3


# Examples
nums = [2, 4, 4, 4, 5, 5, 7, 9]
print(f"Skewness: {skewness(nums):.2f}")  # ~0.63
print(f"Kurtosis: {kurtosis(nums):.2f}")  # ~-0.86
```

📂 Calculate skewness and kurtosis

🏷️ Tags: math, statistics, skewness, kurtosis, advanced
📝 Notes:
- Manual calculation
- Fisher-Pearson skewness
- Excess kurtosis
- Useful for distribution shape

## Complex

### 🧩 Covariance and correlation

```python
import statistics


def covariance(x, y, sample=True):
    """Calculate covariance between two variables."""
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    if sample:
        return cov / (n - 1)
    else:
        return cov / n


def correlation(x, y):
    """Calculate Pearson correlation coefficient."""
    std_x = statistics.stdev(x)
    std_y = statistics.stdev(y)
    return covariance(x, y) / (std_x * std_y)


# Examples
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
print(f"Covariance: {covariance(x, y):.2f}")  # 5.0
print(f"Correlation: {correlation(x, y):.2f}")  # 1.0
```

📂 Calculate covariance and correlation

🏷️ Tags: math, statistics, covariance, correlation, advanced
📝 Notes:
- Covariance for joint variability
- Pearson correlation for linear relationship

### 🧩 Z-scores and standardization

```python
import statistics


def z_scores(values):
    """Calculate z-scores for a list of values."""
    mean_val = statistics.mean(values)
    std_val = statistics.stdev(values)
    return [(x - mean_val) / std_val for x in values]


def standardize(values):
    """Standardize values to mean 0, std 1."""
    mean_val = statistics.mean(values)
    std_val = statistics.stdev(values)
    return [(x - mean_val) / std_val for x in values]


# Examples
nums = [10, 12, 14, 16, 18]
print(f"Z-scores: {z_scores(nums)}")
print(f"Standardized: {standardize(nums)}")
```

📂 Calculate z-scores and standardize data

🏷️ Tags: math, statistics, z-score, standardization, normalization
📝 Notes:
- Z-scores for outlier detection
- Standardization for normalization

### 🧩 Moving average and rolling statistics

```python
import statistics

def moving_average(values, window):
    """Calculate moving average with given window size."""
    if window <= 0:
        raise ValueError("Window size must be positive")
    return [sum(values[i : i + window]) / window for i in range(len(values) - window + 1)]


def rolling_stddev(values, window):
    """Calculate rolling standard deviation."""
    if window <= 0:
        raise ValueError("Window size must be positive")
    return [statistics.stdev(values[i : i + window]) for i in range(len(values) - window + 1)]


# Examples
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Moving average (3): {moving_average(nums, 3)}")
print(f"Rolling stddev (3): {rolling_stddev(nums, 3)}")
```

📂 Calculate moving average and rolling statistics

🏷️ Tags: math, statistics, moving-average, rolling, window
📝 Notes:
- Moving average for smoothing
- Rolling statistics for time series

## Edge Cases

### 🧩 Handle edge cases in advanced statistics

```python
import statistics


def covariance(x, y, sample=True):
    # Function is defined in one of the above code block
    pass

def safe_variance(values):
    """Safe variance calculation with error handling."""
    try:
        return statistics.variance(values)
    except statistics.StatisticsError:
        return 0


def safe_stddev(values):
    """Safe stddev calculation with error handling."""
    try:
        return statistics.stdev(values)
    except statistics.StatisticsError:
        return 0


def safe_covariance(x, y):
    """Safe covariance calculation with error handling."""
    try:
        return covariance(x, y)
    except Exception:
        return 0


# Test edge cases
print(safe_variance([1]))  # 0
print(safe_stddev([1]))  # 0
print(safe_covariance([1], [1]))  # 0
```

📂 Robust advanced statistics with edge case handling

🏷️ Tags: math, statistics, error-handling, edge-case, validation
📝 Notes:
- Handles small/empty lists
- Returns 0 for invalid input
- Avoids exceptions in user-facing code

### 🧩 Performance comparison

```python
import time
import statistics

def benchmark_advanced_statistics():
    """Benchmark variance and stddev calculations."""
    nums = list(range(1000)) * 100

    start = time.time()
    statistics.variance(nums)
    var_time = time.time() - start

    start = time.time()
    statistics.stdev(nums)
    std_time = time.time() - start

    print(f"Variance: {var_time:.6f}s, Stddev: {std_time:.6f}s")


# benchmark_advanced_statistics()
```

📂 Benchmark advanced statistics calculations

🏷️ Tags: math, statistics, performance, benchmarking
📝 Notes:
- Performance comparison
- Useful for large datasets

## Practical Examples

### 🧩 Outlier detection and normalization

```python
def z_scores(values):
    # Function is defined in one of the above code block
    pass


def detect_outliers(values, threshold=2):
    """Detect outliers using z-score method."""
    zs = z_scores(values)
    return [x for x, z in zip(values, zs) if abs(z) > threshold]


def normalize_minmax(values):
    """Normalize values to [0, 1] range."""
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) if max_val > min_val else 0 for x in values]


# Examples
nums = [10, 12, 14, 16, 100]
print(f"Outliers: {detect_outliers(nums)}")
print(f"Min-max normalized: {normalize_minmax(nums)}")
```

📂 Detect outliers and normalize data

🏷️ Tags: math, statistics, outliers, normalization, minmax
📝 Notes:
- Z-score outlier detection
- Min-max normalization
- Useful for preprocessing

### 🧩 Linear regression (simple)

```python
import statistics


def linear_regression(x, y):
    """Calculate slope and intercept for simple linear regression."""
    _ = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den = sum((xi - mean_x) ** 2 for xi in x)
    slope = num / den
    intercept = mean_y - slope * mean_x
    return slope, intercept


def predict(x, slope, intercept):
    """Predict y value given x, slope, and intercept."""
    return slope * x + intercept


# Examples
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
slope, intercept = linear_regression(x, y)
print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")
print(f"Prediction for x=6: {predict(6, slope, intercept):.2f}")
```

📂 Perform simple linear regression

🏷️ Tags: math, statistics, regression, linear, prediction
📝 Notes:
- Simple linear regression
- Slope and intercept
- Prediction function

## 🔗 Cross-References

- **Reference**: See [📂 Statistics Basic](statistics_basic.md)
- **Reference**: See [📂 Round Number](round_number.md)
- **Reference**: See [📂 Format Number](format_number.md)
- **Reference**: See [📂 Percentage](percentage.md)

## 🏷️ Tags

`math`, `statistics`, `variance`, `stddev`, `correlation`, `regression`, `outliers`, `normalization`, `performance`, `edge-case`, `best-practices`

## 📝 Notes

- Advanced Statistics Support Data Science and Analytics
- Use for Variability, Correlation, and Regression
- Edge Case Handling Ensures Robustness
- Performance Suitable for Large Datasets

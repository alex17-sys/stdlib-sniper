# 🧩 Calculate mean, median, and mode
import statistics


def mean(values):
    """Calculate arithmetic mean."""
    return statistics.mean(values)


def median(values):
    """Calculate median value."""
    return statistics.median(values)


def mode(values):
    """Calculate mode (most common value)."""
    return statistics.mode(values)


def multimode(values):
    """Return a list of the most common value(s)."""
    return statistics.multimode(values)


# Examples
nums = [1, 2, 2, 3, 4]
print(f"Mean: {mean(nums)}")  # 2.4
print(f"Median: {median(nums)}")  # 2
print(f"Mode: {mode(nums)}")  # 2
print(f"Multimode: {multimode(nums)}")  # [2]


# 🧩 Calculate min, max, and range
def minimum(values):
    """Find minimum value."""
    return min(values)


def maximum(values):
    """Find maximum value."""
    return max(values)


def data_range(values):
    """Calculate range (max - min)."""
    return max(values) - min(values)


# Examples
nums = [5, 1, 9, 3, 7]
print(f"Min: {minimum(nums)}")  # 1
print(f"Max: {maximum(nums)}")  # 9
print(f"Range: {data_range(nums)}")  # 8


# 🧩 Calculate sum, count, and average
def total(values):
    """Calculate sum of values."""
    return sum(values)


def count(values):
    """Count number of values."""
    return len(values)


def average(values):
    """Calculate average (mean) value."""
    return sum(values) / len(values) if values else 0


# Examples
nums = [2, 4, 6, 8]
print(f"Sum: {total(nums)}")  # 20
print(f"Count: {count(nums)}")  # 4
print(f"Average: {average(nums)}")  # 5.0


# 🧩 Calculate weighted mean and harmonic mean
import statistics


def weighted_mean(values, weights):
    """Calculate weighted mean."""
    return statistics.fmean([v * w for v, w in zip(values, weights)]) / statistics.fmean(weights)


def harmonic_mean(values):
    """Calculate harmonic mean."""
    return statistics.harmonic_mean(values)


# Examples
values = [10, 20, 30]
weights = [1, 2, 3]
print(f"Weighted mean: {weighted_mean(values, weights):.2f}")  # 23.33
print(f"Harmonic mean: {harmonic_mean(values):.2f}")  # 16.36


# 🧩 Calculate geometric mean and midrange
import statistics


def geometric_mean(values):
    """Calculate geometric mean."""
    return statistics.geometric_mean(values)


def midrange(values):
    """Calculate midrange (average of min and max)."""
    return (min(values) + max(values)) / 2


# Examples
nums = [1, 3, 9]
print(f"Geometric mean: {geometric_mean(nums):.2f}")  # 3.0
print(f"Midrange: {midrange(nums)}")  # 5.0


# 🧩 Frequency, unique values, and counts
from collections import Counter


def frequency_table(values):
    """Return frequency table as dict."""
    return dict(Counter(values))


def unique_values(values):
    """Return sorted list of unique values."""
    return sorted(set(values))


def value_counts(values):
    """Return list of (value, count) pairs."""
    return Counter(values).most_common()


# Examples
nums = [1, 2, 2, 3, 3, 3]
print(f"Frequency: {frequency_table(nums)}")  # {1: 1, 2: 2, 3: 3}
print(f"Unique: {unique_values(nums)}")  # [1, 2, 3]
print(f"Counts: {value_counts(nums)}")  # [(3, 3), (2, 2), (1, 1)]


# 🧩 Handle edge cases in statistics
import statistics


def safe_mean(values):
    """Safe mean calculation with empty list handling."""
    return statistics.mean(values) if values else 0


def safe_median(values):
    """Safe median calculation with empty list handling."""
    return statistics.median(values) if values else 0


def safe_mode(values):
    """Safe mode calculation with error handling."""
    try:
        return statistics.mode(values)
    except statistics.StatisticsError:
        return None


# Test edge cases
print(safe_mean([]))  # 0
print(safe_median([]))  # 0
print(safe_mode([]))  # None


# 🧩 Performance comparison
import time
import statistics


def benchmark_statistics_methods():
    """Benchmark mean, median, and mode calculations."""
    nums = list(range(1000)) * 100

    start = time.time()
    statistics.mean(nums)
    mean_time = time.time() - start

    start = time.time()
    statistics.median(nums)
    median_time = time.time() - start

    start = time.time()
    statistics.mode(nums)
    mode_time = time.time() - start

    print(f"Mean: {mean_time:.6f}s, Median: {median_time:.6f}s, Mode: {mode_time:.6f}s")


# benchmark_statistics_methods()


# 🧩 Grade calculation and summary statistics
import statistics


# Function is defined in one of the above code block (data_range)


def calculate_grades(scores):
    """Calculate mean, median, and mode for grades."""
    return {
        "mean": statistics.mean(scores),
        "median": statistics.median(scores),
        "mode": statistics.multimode(scores),
    }


def summary_statistics(values):
    """Return summary statistics for a dataset."""
    return {
        "count": statistics.count(values),
        "min": statistics.minimum(values),
        "max": statistics.maximum(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "mode": statistics.multimode(values),
        "range": data_range(values),
    }


# Examples
grades = [88, 92, 76, 81, 92, 85, 76]
print(f"Grade stats: {calculate_grades(grades)}")
print(f"Summary: {summary_statistics(grades)}")

# 🧩 Format with commas
def format_with_commas(number):
    """Format number with comma separators."""
    return f"{number:,}"


# Basic formatting
print(format_with_commas(1234567))  # 1,234,567
print(format_with_commas(1234.5678))  # 1,234.5678
print(format_with_commas(1000000))  # 1,000,000
print(format_with_commas(0.123456))  # 0.123456


# 🧩 Format with decimal places
def format_decimal(number, places=2):
    """Format number with specified decimal places."""
    return f"{number:.{places}f}"


# Examples
print(format_decimal(3.14159, 2))  # 3.14
print(format_decimal(3.14159, 4))  # 3.1416
print(format_decimal(100, 2))  # 100.00
print(format_decimal(0.1, 3))  # 0.100


# 🧩 Format as percentage
def format_percentage(number, places=1):
    """Format number as percentage."""
    return f"{number * 100:.{places}f}%"


# Examples
print(format_percentage(0.25))  # 25.0%
print(format_percentage(0.1234, 2))  # 12.34%
print(format_percentage(1.5))  # 150.0%
print(format_percentage(0.001, 3))  # 0.1%


# 🧩 Format with custom separators
def format_custom(number, decimal_places=2, thousands_sep=",", decimal_sep="."):
    """Format number with custom separators."""
    # Convert to string with proper decimal places
    formatted = f"{number:.{decimal_places}f}"

    # Split into integer and decimal parts
    if "." in formatted:
        integer_part, decimal_part = formatted.split(".")
    else:
        integer_part, decimal_part = formatted, ""

    # Add thousands separators to integer part
    if len(integer_part) > 3:
        integer_part = f"{int(integer_part):,}".replace(",", thousands_sep)

    # Combine parts
    if decimal_part:
        return f"{integer_part}{decimal_sep}{decimal_part}"
    return integer_part


# Examples
print(format_custom(1234567.89))  # 1,234,567.89
print(format_custom(1234567.89, thousands_sep=" "))  # 1 234 567.89
print(format_custom(1234567.89, decimal_sep=","))  # 1,234,567,89


# 🧩 Format with scientific notation
def format_scientific(number, precision=2):
    """Format number in scientific notation."""
    return f"{number:.{precision}e}"


def format_scientific_compact(number, precision=2):
    """Format number in compact scientific notation."""
    if abs(number) < 0.01 or abs(number) >= 10000:
        return f"{number:.{precision}e}"
    else:
        return f"{number:.{precision}f}"


# Examples
print(format_scientific(1234567))  # 1.23e+06
print(format_scientific(0.000123))  # 1.23e-04
print(format_scientific_compact(1234567))  # 1.23e+06
print(format_scientific_compact(123.45))  # 123.45


# 🧩 Format currency
def format_currency(amount, currency="USD", places=2):
    """Format number as currency."""
    currency_symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "CAD": "C$",
        "AUD": "A$",
        "CHF": "CHF",
    }

    symbol = currency_symbols.get(currency, currency)
    formatted = f"{amount:.{places}f}"

    # Add thousands separators
    if "." in formatted:
        integer_part, decimal_part = formatted.split(".")
    else:
        integer_part, decimal_part = formatted, ""

    if len(integer_part) > 3:
        integer_part = f"{int(integer_part):,}"

    if decimal_part:
        return f"{symbol}{integer_part}.{decimal_part}"
    return f"{symbol}{integer_part}"


# Examples
print(format_currency(1234.56, "USD"))  # $1,234.56
print(format_currency(1234.56, "EUR"))  # €1,234.56
print(format_currency(1234, "JPY"))  # ¥1,234
print(format_currency(1234.56, "GBP"))  # £1,234.56


# 🧩 Format with units
def format_with_units(number, unit="", places=2):
    """Format number with units."""
    formatted = f"{number:.{places}f}"

    # Add thousands separators
    if "." in formatted:
        integer_part, decimal_part = formatted.split(".")
    else:
        integer_part, decimal_part = formatted, ""

    if len(integer_part) > 3:
        integer_part = f"{int(integer_part):,}"

    if decimal_part:
        result = f"{integer_part}.{decimal_part}"
    else:
        result = integer_part

    return f"{result}{unit}" if unit else result


# Examples
print(format_with_units(1234.56, " kg"))  # 1,234.56 kg
print(format_with_units(1234.56, " m/s"))  # 1,234.56 m/s
print(format_with_units(1234, " items"))  # 1,234 items


# 🧩 Handle edge cases in formatting
import math


def robust_format(number, places=2, thousands_sep=","):
    """Robust number formatting with edge case handling."""
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be int or float")

    if math.isnan(number):
        return "NaN"

    if math.isinf(number):
        return "∞" if number > 0 else "-∞"

    if number == 0:
        return f"0.{'0' * places}"

    # Handle very small numbers
    if abs(number) < 1e-10 and number != 0:
        return f"{number:.{places}e}"

    return f"{number:.{places}f}".replace(",", thousands_sep)


# Test edge cases
try:
    print(robust_format(float("inf")))  # ∞
    print(robust_format(float("nan")))  # NaN
    print(robust_format(0.0))  # 0.00
    print(robust_format(1e-15))  # 1.00e-15
except TypeError as e:
    print(f"Error: {e}")


# 🧩 Performance optimization
import time


def benchmark_formatting():
    """Benchmark different formatting methods."""
    numbers = [1234567.89] * 100000

    # Method 1: f-string formatting
    start = time.time()
    _ = [f"{n:,}" for n in numbers]
    time1 = time.time() - start

    # Method 2: format() method
    start = time.time()
    _ = ["{:,}".format(n) for n in numbers]
    time2 = time.time() - start

    print(f"f-string: {time1:.6f}s")
    print(f"format(): {time2:.6f}s")
    print(f"Speedup: {time2 / time1:.2f}x")


# benchmark_formatting()


# 🧩 Financial reporting
def format_currency(amount, currency="USD", places=2):
    # Function is defined in one of the above code block
    pass


def format_financial_report(data):
    """Format financial data for reporting."""
    report = []
    for item, amount in data.items():
        formatted_amount = format_currency(amount, "USD")
        report.append(f"{item:20} {formatted_amount:>15}")
    return "\n".join(report)


# Example
financial_data = {
    "Revenue": 1234567.89,
    "Expenses": 987654.32,
    "Profit": 246913.57,
    "Tax": 49382.71,
}

print(format_financial_report(financial_data))
# Revenue              $1,234,567.89
# Expenses             $987,654.32
# Profit               $246,913.57
# Tax                   $49,382.71


# 🧩 Data visualization labels
def format_axis_labels(values, max_length=10):
    """Format values for axis labels in charts."""
    formatted_labels = []

    for value in values:
        if abs(value) >= 1000000:
            formatted = f"{value / 1000000:.1f}M"
        elif abs(value) >= 1000:
            formatted = f"{value / 1000:.1f}K"
        else:
            formatted = f"{value:.1f}"

        # Truncate if too long
        if len(formatted) > max_length:
            formatted = formatted[: max_length - 3] + "..."

        formatted_labels.append(formatted)

    return formatted_labels


# Example
values = [1234, 56789, 1234567, 89012345]
labels = format_axis_labels(values)
print(labels)  # ['1.2K', '56.8K', '1.2M', '89.0M']

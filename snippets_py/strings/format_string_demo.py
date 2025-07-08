# 🧩 Basic string formatting
name = "Alice"
age = 30
message = "Hello, my name is {} and I am {} years old.".format(name, age)
print(message)  # "Hello, my name is Alice and I am 30 years old."


# 🧩 Named placeholders
name = "Bob"
age = 25
message = "Hello, my name is {name} and I am {age} years old.".format(name=name, age=age)
print(message)  # "Hello, my name is Bob and I am 25 years old."


# 🧩 F-string formatting
name = "Charlie"
age = 35
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # "Hello, my name is Charlie and I am 35 years old."


# 🧩 Number formatting
pi = 3.14159
price = 19.99

# Format decimal places
formatted_pi = "{:.2f}".format(pi)
print(formatted_pi)  # "3.14"

# Format currency
formatted_price = "${:.2f}".format(price)
print(formatted_price)  # "$19.99"


# 🧩 Advanced number formatting
def format_number_advanced(number, format_spec):
    """Format number with advanced specifications."""
    return format_spec.format(number)


# Integer formatting
large_number = 1234567
print(format_number_advanced(large_number, "{:,}"))  # "1,234,567"
print(format_number_advanced(large_number, "{:>10}"))  # "   1234567"

# Float formatting
float_num = 3.14159
print(format_number_advanced(float_num, "{:.3f}"))  # "3.142"
print(format_number_advanced(float_num, "{:+.2f}"))  # "+3.14"

# Percentage formatting
percentage = 0.85
print(format_number_advanced(percentage, "{:.1%}"))  # "85.0%"


# 🧩 Conditional formatting
def format_conditional(value, positive_format, negative_format, zero_format):
    """Format value based on condition."""
    if value > 0:
        return positive_format.format(value)
    elif value < 0:
        return negative_format.format(value)
    else:
        return zero_format.format(value)


# Format numbers with colors/indicators
numbers = [5, -3, 0, 10, -7]

for num in numbers:
    formatted = format_conditional(num, "+{:+d} (positive)", "{:d} (negative)", "{:d} (zero)")
    print(formatted)


# 🧩 Template formatting
from string import Template


def format_with_template(template_text, **kwargs):
    """Format string using Template class."""
    template = Template(template_text)
    return template.substitute(kwargs)


# Email template
email_template = """
Dear $name,

Thank you for your order #$order_id.
Your total amount is $amount.

Best regards,
$company
"""

email = format_with_template(
    email_template, name="John Doe", order_id="12345", amount="$99.99", company="Our Store"
)
print(email)


# 🧩 Custom formatting functions
def format_with_custom_functions(text, **formatters):
    """Format text with custom formatting functions."""
    result = text

    for placeholder, formatter in formatters.items():
        placeholder_text = "{" + placeholder + "}"
        if placeholder_text in result:
            result = result.replace(placeholder_text, formatter())

    return result


# Custom formatters
def get_current_time():
    from datetime import datetime

    return datetime.now().strftime("%H:%M:%S")


def get_random_id():
    import random

    return str(random.randint(1000, 9999))


# Format with custom functions
template = "Order #{order_id} created at {timestamp}"
formatted = format_with_custom_functions(
    template, order_id=get_random_id, timestamp=get_current_time
)
print(formatted)


# 🧩 Multi-line formatting
def format_multiline_template(template_lines, **kwargs):
    """Format multi-line template with indentation preservation."""
    formatted_lines = []

    for line in template_lines:
        # Preserve indentation
        indent = len(line) - len(line.lstrip())
        formatted_line = line.format(**kwargs)

        # Re-apply indentation
        if indent > 0:
            formatted_line = " " * indent + formatted_line.lstrip()

        formatted_lines.append(formatted_line)

    return "\n".join(formatted_lines)


# Multi-line template
template_lines = [
    "Dear {name},",
    "",
    "    Thank you for your recent purchase.",
    "    Order details:",
    "        - Item: {item}",
    "        - Price: {price}",
    "        - Date: {date}",
    "",
    "Best regards,",
    "{company}",
]

formatted_letter = format_multiline_template(
    template_lines,
    name="Jane Smith",
    item="Python Book",
    price="$29.99",
    date="2024-01-15",
    company="Tech Books Inc.",
)
print(formatted_letter)

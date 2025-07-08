# Format String

Zero-dependency Python snippets using only the standard library.

9 snippets available in this sub-category.

---

## Simple

###  Basic string formatting

`string` `format` `positional` `arguments` `text`

Format string with positional arguments

```python
name = "Alice"
age = 30
message = "Hello, my name is {} and I am {} years old.".format(name, age)
print(message)  # "Hello, my name is Alice and I am 30 years old."
```

!!! note "Notes"
    - Uses str.format() method
    - Positional placeholders {}
    - Simple variable substitution
    - Readable formatting

<hr class="snippet-divider">

### Named placeholders

`string` `format` `named` `placeholders` `text`

Format string with named arguments

```python
name = "Bob"
age = 25
message = "Hello, my name is {name} and I am {age} years old.".format(name=name, age=age)
print(message)  # "Hello, my name is Bob and I am 25 years old."
```

!!! note "Notes"
    - Uses named placeholders
    - More readable than positional
    - Self-documenting code
    - Flexible argument order

<hr class="snippet-divider">

### F-string formatting

`string` `format` `f-string` `interpolation` `text`

Format string with f-string syntax

```python
name = "Charlie"
age = 35
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # "Hello, my name is Charlie and I am 35 years old."
```

!!! note "Notes"
    - Modern Python syntax (3.6+)
    - Direct variable interpolation
    - Most readable format
    - Efficient execution

<hr class="snippet-divider">

### Number formatting

`string` `format` `numbers` `precision` `decimal` `text`

Format numbers with precision

```python
pi = 3.14159
price = 19.99

# Format decimal places
formatted_pi = "{:.2f}".format(pi)
print(formatted_pi)  # "3.14"

# Format currency
formatted_price = "${:.2f}".format(price)
print(formatted_price)  # "$19.99"
```

!!! note "Notes"
    - Controls decimal places
    - Currency formatting
    - Consistent number display
    - Professional output

<hr class="snippet-divider">

## Complex

###  Advanced number formatting

`string` `format` `numbers` `advanced` `specifications` `text`

Format numbers with advanced specifications

```python
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
```

!!! note "Notes"
    - Thousand separators
    - Alignment options
    - Sign display
    - Percentage formatting

<hr class="snippet-divider">

### Conditional formatting

`string` `format` `conditional` `logic` `text`

Format values based on conditions

```python
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
```

!!! note "Notes"
    - Dynamic formatting rules
    - Context-aware output
    - Flexible formatting logic
    - User-friendly display

<hr class="snippet-divider">

### Template formatting

`string` `format` `template` `substitution` `text`

Format string using Template class

```python
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
```

!!! note "Notes"
    - Uses string.Template
    - Dollar-sign placeholders
    - Safe substitution
    - Template-based formatting

<hr class="snippet-divider">

### Custom formatting functions

`string` `format` `custom` `functions` `dynamic` `text`

Format string with custom functions

```python
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
```

!!! note "Notes"
    - Dynamic value generation
    - Function-based formatting
    - Runtime value computation
    - Flexible formatting system

<hr class="snippet-divider">

### Multi-line formatting

`string` `format` `multiline` `indent` `template` `text`

Format multi-line text with indentation

```python
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
```

!!! note "Notes"
    - Preserves indentation
    - Multi-line template support
    - Clean formatting output
    - Professional document generation

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Join Strings](./join_strings.md)
- **Reference**: See [📂 Split String](./split_string.md)
- **Reference**: See [📂 Justify Text Alignment](./justify_text.md)

## 🏷️ Tags

`string`, `format`, `positional`, `named`, `f-string`, `number`, `precision`, `conditional`, `template`, `text`

## 📝 Notes

- Use f-strings for most readable and efficient formatting (Python 3.6+)
- str.format() supports both positional and named arguments
- Template strings are useful for user-supplied templates
- Advanced formatting options allow for alignment, padding, and number formatting
- See related snippets for joining, splitting, and justifying text

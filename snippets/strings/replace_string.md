# Replace String

Zero-dependency Python snippets for replacing strings using the standard library.

## Simple

### 🧩 Replace substring

```python
text = "Hello World"
result = text.replace("World", "Python")
print(result)  # "Hello Python"
```

📂 Replace substring with new text

🏷️ Tags: string, replace, substring, text
📝 Notes:
- Uses str.replace() method
- Simple text substitution
- Case-sensitive replacement
- Returns new string

### 🧩 Replace multiple occurrences

```python
text = "Hello Hello Hello"
result = text.replace("Hello", "Hi")
print(result)  # "Hi Hi Hi"
```

📂 Replace all occurrences of substring

🏷️ Tags: string, replace, multiple, occurrences, text
📝 Notes:
- Replaces all instances
- No limit on replacements
- Maintains original case
- Efficient for bulk changes

### 🧩 Replace with count limit

```python
text = "Hello Hello Hello"
result = text.replace("Hello", "Hi", 2)
print(result)  # "Hi Hi Hello"
```

📂 Replace limited number of occurrences

🏷️ Tags: string, replace, count, limit, text
📝 Notes:
- Controls replacement count
- Useful for selective changes
- Preserves remaining instances
- Flexible replacement control

## Complex

### 🧩 Replace with case-insensitive matching

```python
import re


def replace_case_insensitive(text, old, new):
    """Replace text case-insensitively."""
    pattern = re.compile(re.escape(old), re.IGNORECASE)
    return pattern.sub(new, text)


text = "Hello WORLD hello World"
result = replace_case_insensitive(text, "hello", "Hi")
print(result)  # "Hi WORLD Hi World"
```

📂 Replace text ignoring case differences

🏷️ Tags: string, replace, case, insensitive, regex, text
📝 Notes:
- Uses regex for case-insensitive matching
- Handles mixed case variations
- Preserves original case in result
- More flexible than simple replace

### 🧩 Replace with custom function

```python
import re


def replace_with_function(text, pattern, replacement_func):
    """Replace using custom function."""

    def replacer(match):
        return replacement_func(match.group(0))

    return re.sub(pattern, replacer, text)


text = "Hello 123 World 456 Python"


# Replace numbers with doubled values
def double_number(match):
    num = int(match.group(0))
    return str(num * 2)


result = replace_with_function(text, r"\d+", double_number)
print(result)  # "Hello 246 World 912 Python"
```

📂 Replace using custom replacement function

🏷️ Tags: string, replace, function, custom, regex, text
📝 Notes:
- Dynamic replacement logic
- Access to matched content
- Complex transformation rules
- Powerful text processing

### 🧩 Replace with conditional logic

```python
def replace_conditional(text, replacements, condition_func=None):
    """Replace text with conditional logic."""
    if condition_func is None:
        def condition_func(x):
            return True


    result = text
    for old, new in replacements.items():
        if condition_func(old):
            result = result.replace(old, new)

    return result


text = "Hello World Python"

# Replace only short words
replacements = {"Hello": "Hi", "World": "Earth", "Python": "Programming"}


def is_short_word(word):
    return len(word) <= 5


result = replace_conditional(text, replacements, is_short_word)
print(result)  # "Hi Earth Python"
```

📂 Replace text based on conditions

🏷️ Tags: string, replace, conditional, logic, text
📝 Notes:
- Conditional replacement rules
- Multiple replacement pairs
- Flexible condition checking
- Selective text modification

### 🧩 Replace with context awareness

```python
import re


def replace_with_context(text, target, replacement, context_chars=10):
    """Replace text with context awareness."""
    pattern = f".{{0,{context_chars}}}{re.escape(target)}.{{0,{context_chars}}}"

    def replacer(match):
        match_text = match.group(0)
        start = match_text.find(target)
        end = start + len(target)

        # Check context before replacing
        before = match_text[:start]
        after = match_text[end:]

        # Example: only replace if surrounded by spaces
        if before.strip() == "" and after.strip() == "":
            return match_text[:start] + replacement + match_text[end:]
        return match_text

    return re.sub(pattern, replacer, text)


text = "Hello World, HelloPython, Hello World"
result = replace_with_context(text, "Hello", "Hi")
print(result)  # "Hi World, HelloPython, Hi World"
```

📂 Replace text with context checking

🏷️ Tags: string, replace, context, awareness, regex, text
📝 Notes:
- Considers surrounding context
- Prevents unwanted replacements
- Configurable context size
- Smart text processing

## 🔗 Cross-References

- **Reference**: See [📂 Find String](./find_string.md)

## 🏷️ Tags

`string`, `replace`, `context`, `awareness`, `regex`, `text`

## 📝 Notes

- Use str.replace() for simple replacements
- Use regex for advanced or context-aware replacements
- See related snippet for finding text before replacing

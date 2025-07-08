# Wrap Text

Zero-dependency Python snippets for wrapping text to specified width using the standard library.

## Simple

### 🧩 Wrap text to width

```python
import textwrap

text = "This is a long text that needs to be wrapped to a specific width for better readability."
wrapped = textwrap.wrap(text, width=30)
for line in wrapped:
    print(line)
```

📂 Wrap text to specified width using textwrap

🏷️ Tags: string, wrap, text, width, textwrap
📝 Notes:
- Uses textwrap.wrap() function
- Returns list of wrapped lines
- Breaks at word boundaries
- Handles long words

### 🧩 Wrap text with fill

```python
import textwrap

text = "This is a long text that needs to be wrapped to a specific width for better readability."
wrapped = textwrap.fill(text, width=30)
print(wrapped)
```

📂 Wrap text and join lines with newlines

🏷️ Tags: string, wrap, fill, text, width, textwrap
📝 Notes:
- Uses textwrap.fill() function
- Returns single string with newlines
- Same as wrap() + join
- Convenient for display

## Complex

### 🧩 Wrap text with custom options

```python
import textwrap


def wrap_text_advanced(text, width=70, **options):
    """Wrap text with advanced options."""
    default_options = {
        "initial_indent": "",
        "subsequent_indent": "",
        "expand_tabs": True,
        "replace_whitespace": True,
        "drop_whitespace": True,
        "break_long_words": True,
        "break_on_hyphens": True,
    }

    # Update with provided options
    default_options.update(options)

    return textwrap.wrap(text, width=width, **default_options)


text = "This is a very long text that needs to be wrapped with custom indentation and formatting options."

# Wrap with indentation
wrapped = wrap_text_advanced(text, width=40, initial_indent="  ", subsequent_indent="    ")
for line in wrapped:
    print(line)

# Wrap with different options
wrapped = wrap_text_advanced(text, width=30, break_long_words=False, break_on_hyphens=False)
for line in wrapped:
    print(line)
```

📂 Wrap text with advanced formatting options

🏷️ Tags: string, wrap, advanced, options, indent, textwrap, text
📝 Notes:
- Customizable indentation
- Control over word breaking
- Whitespace handling options
- Flexible formatting

### 🧩 Wrap text with custom break function

```python
import textwrap
import re


def wrap_text_custom_breaks(text, width=70, break_chars=None):
    """Wrap text with custom break characters."""
    if break_chars is None:
        break_chars = [" ", "-", "_", "/", "\\"]

    # Create custom break function
    def custom_break(text):
        # Find the last occurrence of any break character
        last_break = -1
        for char in break_chars:
            pos = text.rfind(char)
            if pos > last_break:
                last_break = pos

        if last_break > 0:
            return last_break + 1  # Include the break character
        return 0  # No break found

    # Use textwrap with custom break function
    wrapper = textwrap.TextWrapper(width=width)
    wrapper.break_on_hyphens = False
    wrapper.break_long_words = True

    # Override the break function
    wrapper.wordsep_re = re.compile(r"|".join(re.escape(char) for char in break_chars))

    return wrapper.wrap(text)


text = "This-is-a-long-text-with-hyphens that needs custom wrapping"
wrapped = wrap_text_custom_breaks(text, width=20, break_chars=[" ", "-"])
for line in wrapped:
    print(line)
```

📂 Wrap text with custom break character handling

🏷️ Tags: string, wrap, custom, breaks, characters, textwrap, text
📝 Notes:
- Customizable break characters
- Handles special separators
- Flexible word breaking
- Useful for technical text

## 🔗 Cross-References

- **Reference**: See [📂 Justify Text Alignment](./justify_text.md)
- **Reference**: See [📂 Format String](./format_string.md)

## 🏷️ Tags

`string`, `wrap`, `text`, `width`, `textwrap`, `custom`, `breaks`, `indent`, `advanced`

## 📝 Notes

- Use textwrap for standard and advanced wrapping
- Custom break characters and indentation supported
- Related: justifying and formatting text

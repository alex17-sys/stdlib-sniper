# 🧩 Wrap text to width
import textwrap

text = "This is a long text that needs to be wrapped to a specific width for better readability."
wrapped = textwrap.wrap(text, width=30)
for line in wrapped:
    print(line)


# 🧩 Wrap text with fill
import textwrap

text = "This is a long text that needs to be wrapped to a specific width for better readability."
wrapped = textwrap.fill(text, width=30)
print(wrapped)


# 🧩 Wrap text with custom options
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


# 🧩 Wrap text with custom break function
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

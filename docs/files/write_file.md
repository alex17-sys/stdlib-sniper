---
title: Write File
description: Zero-dependency Python snippets for writing files using the standard library.
keywords: atomic, encoding, error-handling, file, function, open, os, string, tempfile, utf-8, write
---

# Write File

Zero-dependency Python snippets for writing files using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Write string to file

`file` `write` `string` `open`

Write a string to a file, overwriting existing content

```python
with open("file.txt", "w") as f:
    f.write("Hello, World!")
```

!!! note "Notes"
    - Use 'w' mode to overwrite existing file
    - Creates new file if it doesn't exist
    - File is automatically closed after writing

<hr class="snippet-divider">

### Write with encoding

`file` `write` `encoding` `utf-8`

Write file with specific encoding

```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 世界!")
```

!!! note "Notes"
    - Always specify encoding for international text
    - UTF-8 handles most characters properly
    - Prevents encoding issues

<hr class="snippet-divider">

## Complex

###  Write file with error handling

`file` `write` `error-handling` `function` `encoding`

Write file with comprehensive error handling

```python
def write_file_safe(filename, content, encoding="utf-8"):
    """Write content to file with comprehensive error handling."""
    try:
        with open(filename, "w", encoding=encoding) as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    except OSError as e:
        print(f"Error writing to '{filename}': {e}")
        return False


success = write_file_safe("file.txt", "Hello, World!")
if success:
    print("File written successfully")
```

!!! note "Notes"
    - Handles common file writing errors
    - Returns boolean for success/failure
    - Supports custom encoding
    - Provides helpful error messages

<hr class="snippet-divider">

### Write file atomically

`file` `write` `atomic` `tempfile` `os`

Write file atomically to prevent corruption during writing

```python
import os
import tempfile


def write_file_atomic(filename, content, encoding="utf-8"):
    """Write file atomically to prevent corruption."""
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", encoding=encoding, delete=False, dir=os.path.dirname(filename)
    )

    try:
        temp_file.write(content)
        temp_file.close()
        os.replace(temp_file.name, filename)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        try:
            os.unlink(temp_file.name)
        except Exception:
            pass
        return False


write_file_atomic("important.txt", "Critical data")
```

!!! note "Notes"
    - Uses temporary file to prevent corruption
    - Atomic operation ensures file integrity
    - Cleans up temporary file on error
    - Useful for critical data files

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Append File](./append_file.md)
- **Reference**: See [📂 Read File](./read_file.md)

## 🏷️ Tags

`file`, `write`, `text`, `overwrite`, `io`

## 📝 Notes

- Use open() with mode 'w' to write (overwrite) files
- Overwrites existing content by default
- Useful for saving data and reports

# Append File

Zero-dependency Python snippets for appending content to files using the standard library.

## Simple

### 🧩 Append string to file

```python
with open("file.txt", "a") as f:
    f.write("New line\n")
```

📂 Append content to existing file without overwriting

🏷️ Tags: file, append, write, open
📝 Notes:
- Use 'a' mode to append to existing file
- Creates new file if it doesn't exist
- Adds content at the end of file

### 🧩 Append with newline

```python
with open("file.txt", "a") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

📂 Append multiple lines with proper newlines

🏷️ Tags: file, append, write, newline
📝 Notes:
- Manually add newlines for line breaks
- Each write() call adds to the end
- Useful for building log files

## Complex

### 🧩 Append with timestamp

```python
from datetime import datetime


def append_with_timestamp(filename, message):
    """Append message with timestamp to file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


append_with_timestamp("log.txt", "User logged in")
```

📂 Append messages with automatic timestamps

🏷️ Tags: file, append, timestamp, datetime, logging
📝 Notes:
- Automatically adds timestamps to entries
- Useful for log files and activity tracking
- Consistent timestamp format
- Easy to parse later

### 🧩 Append with rotation

```python
import os
from datetime import datetime


def append_with_rotation(filename, content, max_size_mb=10):
    """Append content with file size rotation."""
    # Check if file exists and get its size
    if os.path.exists(filename):
        size_mb = os.path.getsize(filename) / (1024 * 1024)
        if size_mb > max_size_mb:
            # Create backup with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{filename}.{timestamp}"
            os.rename(filename, backup_name)

    # Append content
    with open(filename, "a") as f:
        f.write(content + "\n")


append_with_rotation("app.log", "New log entry")
```

📂 Append with automatic file rotation based on size

🏷️ Tags: file, append, rotation, size, backup
📝 Notes:
- Prevents log files from growing too large
- Creates timestamped backups
- Configurable size limit
- Useful for long-running applications

## 🔗 Cross-References

- **Reference**: See [📂 Write File](./write_file.md)
- **Reference**: See [📂 Read File](./read_file.md)

## 🏷️ Tags

`file`, `append`, `write`, `text`, `lines`, `io`

## 📝 Notes

- Use open() with mode 'a' to append to files
- Appending does not overwrite existing content
- Useful for logs and incremental data

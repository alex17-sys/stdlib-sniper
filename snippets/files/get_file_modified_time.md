# Get File Modified Time

Zero-dependency Python snippets for getting file modification times using the standard library.

## Simple

### 🧩 Get file modification time

```python
import os

mtime = os.path.getmtime("file.txt")
print(f"Modified: {mtime}")
```

📂 Get file modification time as Unix timestamp

🏷️ Tags: file, time, modification, timestamp, os
📝 Notes:
- Returns Unix timestamp (seconds since epoch)
- Raises OSError if file doesn't exist
- Useful for file comparison

### 🧩 Get file modification time safely

```python
import os

try:
    mtime = os.path.getmtime("file.txt")
    print(f"Modified: {mtime}")
except FileNotFoundError:
    print("File does not exist")
```

📂 Get file modification time with error handling

🏷️ Tags: file, time, modification, error-handling, os
📝 Notes:
- Handles case where file doesn't exist
- Provides clear error message
- Safe for scripts

## Complex

### 🧩 Get file modification time as datetime

```python
import os
from datetime import datetime


def get_file_modified_datetime(filename):
    """Get file modification time as datetime object."""
    if not os.path.exists(filename):
        return None

    mtime = os.path.getmtime(filename)
    return datetime.fromtimestamp(mtime)


mtime_dt = get_file_modified_datetime("file.txt")
if mtime_dt:
    print(f"Modified: {mtime_dt}")
    print(f"Date: {mtime_dt.strftime('%Y-%m-%d')}")
    print(f"Time: {mtime_dt.strftime('%H:%M:%S')}")
```

📂 Get file modification time as datetime object with formatting

🏷️ Tags: file, time, modification, datetime, formatting, os
📝 Notes:
- Converts timestamp to datetime object
- Allows easy date/time formatting
- Returns None if file doesn't exist
- Useful for human-readable output

### 🧩 Get file age in human readable format

```python
import os
from datetime import datetime


def get_file_age(filename):
    """Get file age in human readable format."""
    if not os.path.exists(filename):
        return "File does not exist"

    mtime = os.path.getmtime(filename)
    file_time = datetime.fromtimestamp(mtime)
    now = datetime.now()
    age = now - file_time

    # Convert to appropriate unit
    if age.days > 365:
        years = age.days // 365
        return f"{years} year{'s' if years != 1 else ''} ago"
    elif age.days > 30:
        months = age.days // 30
        return f"{months} month{'s' if months != 1 else ''} ago"
    elif age.days > 0:
        return f"{age.days} day{'s' if age.days != 1 else ''} ago"
    elif age.seconds > 3600:
        hours = age.seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif age.seconds > 60:
        minutes = age.seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    else:
        return "Just now"


age = get_file_age("file.txt")
print(f"File age: {age}")
```

📂 Get file age in human readable format (days, hours, minutes ago)

🏷️ Tags: file, time, age, human-readable, datetime, os
📝 Notes:
- Shows relative time since modification
- Automatically chooses appropriate unit
- Handles plural forms correctly
- Useful for file management interfaces

## 🔗 Cross-References

- **Reference**: See [📂 Get File Size](./get_file_size.md)
- **Reference**: See [📂 File Exists](./file_exists.md)

## 🏷️ Tags

`file`, `time`, `timestamp`, `os`, `stat`, `io`

## 📝 Notes

- Use os.path.getmtime() to get file modification time
- Returns timestamp (float); use datetime for formatting
- Useful for backups, logs, and file management

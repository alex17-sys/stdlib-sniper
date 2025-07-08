# Get File Modified Time

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Get file modification time

`file` `time` `modification` `timestamp` `os`

Get file modification time as Unix timestamp

```python
import os

mtime = os.path.getmtime("file.txt")
print(f"Modified: {mtime}")
```

!!! note "Notes"
    - Returns Unix timestamp (seconds since epoch)
    - Raises OSError if file doesn't exist
    - Useful for file comparison

<hr class="snippet-divider">

### Get file modification time safely

`file` `time` `modification` `error-handling` `os`

Get file modification time with error handling

```python
import os

try:
    mtime = os.path.getmtime("file.txt")
    print(f"Modified: {mtime}")
except FileNotFoundError:
    print("File does not exist")
```

!!! note "Notes"
    - Handles case where file doesn't exist
    - Provides clear error message
    - Safe for scripts

<hr class="snippet-divider">

## Complex

###  Get file modification time as datetime

`file` `time` `modification` `datetime` `formatting` `os`

Get file modification time as datetime object with formatting

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

!!! note "Notes"
    - Converts timestamp to datetime object
    - Allows easy date/time formatting
    - Returns None if file doesn't exist
    - Useful for human-readable output

<hr class="snippet-divider">

### Get file age in human readable format

`file` `time` `age` `human-readable` `datetime` `os`

Get file age in human readable format (days, hours, minutes ago)

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

!!! note "Notes"
    - Shows relative time since modification
    - Automatically chooses appropriate unit
    - Handles plural forms correctly
    - Useful for file management interfaces

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 Get File Size](./get_file_size.md)
- **Reference**: See [📂 File Exists](./file_exists.md)

## 🏷️ Tags

`file`, `time`, `timestamp`, `os`, `stat`, `io`

## 📝 Notes

- Use os.path.getmtime() to get file modification time
- Returns timestamp (float); use datetime for formatting
- Useful for backups, logs, and file management

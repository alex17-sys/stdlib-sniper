# Move File

Zero-dependency Python snippets for moving and renaming files using the standard library.

## Simple

### 🧩 Move/rename file

```python
import shutil

shutil.move("old_name.txt", "new_name.txt")
```

📂 Move or rename a file to a new location

🏷️ Tags: file, move, rename, shutil
📝 Notes:
- Works for both moving and renaming
- Overwrites destination if it exists
- Preserves file metadata

### 🧩 Move file with os.rename

```python
import os

os.rename("old_name.txt", "new_name.txt")
```

📂 Rename file using os.rename (same filesystem only)

🏷️ Tags: file, move, rename, os
📝 Notes:
- Faster than shutil.move for same filesystem
- Fails if moving across filesystems
- Atomic operation when possible

## Complex

### 🧩 Move file with backup

```python
import shutil
import os
from datetime import datetime


def move_file_with_backup(src, dst):
    """Move file with automatic backup if destination exists."""
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist")
        return False

    if os.path.exists(dst):
        # Create backup with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{dst}.backup_{timestamp}"
        shutil.move(dst, backup_name)
        print(f"Created backup: {backup_name}")

    try:
        shutil.move(src, dst)
        print(f"File moved successfully: {src} -> {dst}")
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False


move_file_with_backup("source.txt", "destination.txt")
```

📂 Move file with automatic backup of existing destination

🏷️ Tags: file, move, backup, timestamp, shutil
📝 Notes:
- Creates timestamped backup if destination exists
- Prevents accidental data loss
- Provides detailed operation feedback
- Safe for important file operations

### 🧩 Move file with validation

```python
import shutil
import os


def move_file_validated(src, dst):
    """Move file with source validation and destination confirmation."""
    # Validate source
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist")
        return False

    if not os.path.isfile(src):
        print(f"'{src}' is not a regular file")
        return False

    # Check destination
    if os.path.exists(dst):
        if os.path.isdir(dst):
            # If destination is directory, append filename
            dst = os.path.join(dst, os.path.basename(src))

        if os.path.exists(dst):
            response = input(f"'{dst}' already exists. Overwrite? (y/N): ")
            if response.lower() not in ["y", "yes"]:
                print("Move cancelled")
                return False

    # Perform move
    try:
        shutil.move(src, dst)
        print(f"File moved successfully: {src} -> {dst}")
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False


move_file_validated("source.txt", "destination.txt")
```

📂 Move file with comprehensive validation and confirmation

🏷️ Tags: file, move, validation, confirmation, shutil
📝 Notes:
- Validates source file existence and type
- Handles directory destinations automatically
- Asks for confirmation before overwriting

## 🔗 Cross Reference

- **Reference**: See [📂 Copy Directory](copy_directory.md)
- **Reference**: See [📂 Create Nested Directories](create_nested_directories.md)

## 🏷️ Tags

`file`, `move`, `rename`, `backup`, `timestamp`, `validation`, `confirmation`, `shutil`, `os`

## 📝 Notes
- Use shutil.move or os.rename for moving files
- Handle backups and confirmations for safety
- Useful for file management and automation

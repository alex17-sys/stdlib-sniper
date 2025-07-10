---
title: Copy Directory
description: Zero-dependency Python snippets for copying directory trees using the standard library.
keywords: copy, copytree, directory, error-handling, filter, ignore, overwrite, patterns, rmtree, shutil
---

# Copy Directory

Zero-dependency Python snippets for copying directory trees using the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Copy directory tree

`directory` `copy` `copytree` `shutil`

Copy entire directory tree to new location

```python
import shutil

shutil.copytree("source_directory", "destination_directory")
```

!!! note "Notes"
    - Copies all files and subdirectories
    - Creates destination directory if it doesn't exist
    - Raises OSError if destination already exists
    - Preserves file permissions

<hr class="snippet-divider">

### Copy directory safely

`directory` `copy` `copytree` `error-handling` `shutil`

Copy directory tree with error handling

```python
import shutil

try:
    shutil.copytree("source_directory", "destination_directory")
    print("Directory copied successfully")
except FileExistsError:
    print("Destination directory already exists")
except OSError as e:
    print(f"Error copying directory: {e}")
```

!!! note "Notes"
    - Handles case where destination exists
    - Provides clear error messages
    - Safe for scripts that may run multiple times

<hr class="snippet-divider">

## Complex

###  Copy directory with overwrite

`directory` `copy` `overwrite` `copytree` `rmtree` `shutil`

Copy directory tree with automatic overwrite of existing destination

```python
import shutil
import os


def copy_directory_with_overwrite(src, dst):
    """Copy directory tree with overwrite option."""
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist")
        return False

    if not os.path.isdir(src):
        print(f"'{src}' is not a directory")
        return False

    # Remove destination if it exists
    if os.path.exists(dst):
        try:
            shutil.rmtree(dst)
            print(f"Removed existing destination: {dst}")
        except OSError as e:
            print(f"Error removing existing destination: {e}")
            return False

    # Copy the directory
    try:
        shutil.copytree(src, dst)
        print(f"Directory copied successfully: {src} -> {dst}")
        return True
    except OSError as e:
        print(f"Error copying directory: {e}")
        return False


copy_directory_with_overwrite("source_project", "backup_project")
```

!!! note "Notes"
    - Removes existing destination before copying
    - Validates source directory existence
    - Provides detailed operation feedback
    - Useful for backup operations

<hr class="snippet-divider">

### Copy directory with filtering

`directory` `copy` `filter` `ignore` `patterns` `copytree` `shutil`

Copy directory tree with custom file filtering

```python
import shutil
import os

def copy_directory_filtered(src, dst, ignore_patterns=None):
    """Copy directory tree with file filtering."""
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist")
        return False

    # Default ignore patterns
    if ignore_patterns is None:
        ignore_patterns = ["__pycache__", "*.pyc", ".git", ".DS_Store"]

    def ignore_func(dir, files):
        """Filter function for shutil.copytree."""
        ignored = []
        for file in files:
            for pattern in ignore_patterns:
                if pattern in file or file.endswith(pattern.replace("*", "")):
                    ignored.append(file)
                    break
        return ignored

    try:
        shutil.copytree(src, dst, ignore=ignore_func)
        print(f"Directory copied with filtering: {src} -> {dst}")
        return True
    except OSError as e:
        print(f"Error copying directory: {e}")
        return False

# Copy directory excluding common unwanted files
copy_directory_filtered("source_project", "clean_backup")
```

!!! note "Notes"
    - Excludes files matching ignore patterns
    - Default patterns for common unwanted files
    - Customizable filtering rules

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Create Nested Directories](create_nested_directories.md)
- **Reference**: See [📂 Move File](move_file.md)

## 🏷️ Tags

`directory`, `copy`, `copytree`, `filter`, `ignore`, `patterns`, `overwrite`, `rmtree`, `error-handling`, `shutil`

## 📝 Notes
- Use shutil.copytree for full directory copies
- Handle errors and filtering as needed
- Useful for backups and migrations

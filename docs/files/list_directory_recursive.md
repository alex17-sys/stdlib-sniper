# List Directory Recursive

Zero-dependency Python snippets using only the standard library.

4 snippets available in this sub-category.

---

## Simple

###  List all files recursively

`directory` `list` `recursive` `walk` `os`

List all files in directory and subdirectories

```python
import os

for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))
```

!!! note "Notes"
    - Walks through all subdirectories
    - Returns full file paths
    - Includes hidden files

<hr class="snippet-divider">

### List directories recursively

`directory` `list` `recursive` `walk` `os`

List all directories in directory and subdirectories

```python
import os

for root, dirs, files in os.walk("."):
    for dir in dirs:
        print(os.path.join(root, dir))
```

!!! note "Notes"
    - Walks through all subdirectories
    - Returns full directory paths
    - Includes hidden directories

<hr class="snippet-divider">

## Complex

###  List files with relative paths

`directory` `list` `recursive` `relative` `absolute` `paths` `os`

List all files recursively with relative or absolute paths

```python
import os


def list_files_recursive(directory=".", relative=True):
    """List all files recursively with optional relative paths."""
    files = []

    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if relative:
                # Make path relative to starting directory
                rel_path = os.path.relpath(full_path, directory)
                files.append(rel_path)
            else:
                files.append(full_path)

    return files


# Get relative paths
relative_files = list_files_recursive(".")
for file in relative_files:
    print(file)

# Get absolute paths
absolute_files = list_files_recursive(".", relative=False)
for file in absolute_files:
    print(file)
```

!!! note "Notes"
    - Option to get relative or absolute paths
    - Useful for different use cases
    - Returns clean list of file paths
    - Handles path conversion automatically

<hr class="snippet-divider">

### List files with depth limit

`directory` `list` `recursive` `depth` `limit` `os`

List files recursively with configurable depth limit

```python
import os


def list_files_with_depth(directory=".", max_depth=2):
    """List files recursively with depth limit."""
    files = []

    for root, dirs, filenames in os.walk(directory):
        # Calculate current depth
        depth = root.replace(directory, "").count(os.sep)

        if depth >= max_depth:
            # Don't traverse deeper
            dirs.clear()
            continue

        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(root, filename), directory)
            files.append(rel_path)

    return files


# List files up to 2 levels deep
shallow_files = list_files_with_depth(".", max_depth=2)
for file in shallow_files:
    print(file)
```

!!! note "Notes"
    - Limits recursion depth to prevent infinite loops
    - Useful for large directory trees
    - Configurable depth parameter
    - Prevents excessive traversal

<hr class="snippet-divider">

## 🔗 Cross-References

- **Reference**: See [📂 List Directory](./list_directory.md)
- **Reference**: See [📂 Directory Exists](./directory_exists.md)

## 🏷️ Tags

`file`, `directory`, `list`, `recursive`, `os`, `walk`, `io`

## 📝 Notes

- Use os.walk() for recursive directory listing
- Returns all files and subdirectories
- Useful for searching and batch operations

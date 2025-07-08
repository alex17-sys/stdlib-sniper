import os
import re
import sys
from collections import defaultdict

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")

# Gather all .md files except summaries and index
SUMMARY_FILES = {"TAG_SUMMARY.md", "CATEGORY_SUMMARY.md", "INDEX.md"}
SNIPPET_FILES = []
for root, dirs, files in os.walk(SNIPPETS_DIR):
    for f in files:
        if f.endswith(".md") and f not in SUMMARY_FILES:
            SNIPPET_FILES.append(os.path.relpath(os.path.join(root, f), SNIPPETS_DIR))


def extract_snippets(fname):
    path = os.path.join(SNIPPETS_DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    snippets = []
    # Match all snippet titles (### 🧩 ... or ### ...)
    for m in re.finditer(r"^### ?(?:🧩 )?(.+)", content, re.MULTILINE):
        title = m.group(1).strip()

        # Find the start of this snippet and the start of the next
        start = m.end()
        next_m = re.search(r"^### ", content[start:], re.MULTILINE)
        end = start + next_m.start() if next_m else len(content)
        snippet_block = content[start:end]
        # Find the first python code block in this snippet (allowing for blank lines/metadata)
        code_match = re.search(r"```python\n(.*?)```", snippet_block, re.DOTALL)
        code = code_match.group(1).strip() if code_match else None
        # Check if this is a crossref stub (contains 'See [otherfile.md]')
        is_crossref = bool(re.search(r"See \[[^\]]+\.md\]", snippet_block))
        snippets.append(
            {
                "title": title,
                "code": code,
                "file": fname,
                "line": content[: m.start()].count("\n") + 1,
                "is_crossref": is_crossref,
            }
        )
    return snippets


def check_duplicate_headers_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    headers = []
    for match in re.finditer(r"^(#{2,3})\s+(.+)$", content, re.MULTILINE):
        level = match.group(1)
        name = match.group(2).strip().lower()
        line = content[: match.start()].count("\n") + 1
        headers.append((level, name, line))
    seen = {}
    duplicates = []
    for level, name, line in headers:
        key = (level, name)
        if key in seen:
            duplicates.append((level, name, seen[key], line))
        else:
            seen[key] = line
    return duplicates


def main():
    all_snippets = []
    found = False
    for fname in SNIPPET_FILES:
        path = os.path.join(SNIPPETS_DIR, fname)
        # Check for duplicate section headers
        duplicates = check_duplicate_headers_in_file(path)
        for level, name, first_line, dup_line in duplicates:
            print(
                f"Duplicate section header '{level} {name}' in {fname} (lines {first_line} and {dup_line})"
            )
            found = True
    # Only check for duplicate code blocks
    code_map = defaultdict(list)
    for fname in SNIPPET_FILES:
        all_snippets.extend(extract_snippets(fname))
    for snip in all_snippets:
        if snip["code"]:
            code_map[snip["code"].strip()].append(snip)
    dup_code = [v for v in code_map.values() if len(v) > 1]
    if dup_code:
        print("Duplicate snippet code blocks found:")
        for group in dup_code:
            for snip in group:
                print(f"  Code in {snip['file']} (line {snip['line']}): {snip['title']}")
        found = True
    if not found:
        print("No duplicate snippet code blocks or section headers found.")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()

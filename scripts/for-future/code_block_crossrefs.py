"""
# 🧩 Example Inline Cross Reference

📄 **Reference**: See [📂 Example Title](./README.md)

📝 Notes:
- Create a **shallow copy** of a list in Python.

## 🏷️ Categories
- cli
- files
- math
- and many more
"""

import os
import re

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")
SUMMARY_FILES = {"TAG_SUMMARY.md", "CATEGORY_SUMMARY.md", "INDEX.md"}


def get_snippet_files():
    return [f for f in os.listdir(SNIPPETS_DIR) if f.endswith(".md") and f not in SUMMARY_FILES]


def extract_snippet_titles(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract all snippet titles (## 🧩 ... or ## ...)
    titles = re.findall(r"^### ?(?:🧩 )?(.+)", content, re.MULTILINE)
    return set(t.strip() for t in titles)


def extract_snippets_with_refs(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Split into snippets
    snippets = re.split(r"^### ?(?:🧩 )?", content, flags=re.MULTILINE)[1:]
    result = []
    for snippet in snippets:
        lines = snippet.splitlines()
        if not lines:
            continue
        title = lines[0].strip()
        refs = re.findall(r"See \[([^\]]+\.md)\](?:\([^\)]*\))?", snippet)
        result.append({"title": title, "refs": refs})
    return result


def main():
    files = set(get_snippet_files())
    broken = []
    title_mismatches = []
    # Preload all titles for all files
    file_titles = {
        fname: extract_snippet_titles(os.path.join(SNIPPETS_DIR, fname)) for fname in files
    }
    for fname in files:
        path = os.path.join(SNIPPETS_DIR, fname)
        snippets = extract_snippets_with_refs(path)
        for snippet in snippets:
            for ref in snippet["refs"]:
                if ref not in files:
                    print(f"[BROKEN] {fname} references missing file: {ref}")
                    broken.append((fname, ref))
                else:
                    if snippet["title"] not in file_titles[ref]:
                        print(
                            f"[WARN] {fname} snippet '{snippet['title']}' references {ref} but no matching snippet title found."
                        )
                        title_mismatches.append((fname, ref, snippet["title"]))
    if not broken:
        print("All cross-references are valid.")
    else:
        print(f"\n{len(broken)} broken cross-references found.")
    if title_mismatches:
        print(f"\n{len(title_mismatches)} cross-references with no matching snippet title found.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Update snippet indexes and summaries.

This script regenerates:
- INDEX.md: Complete list of all snippets organized by category
- CATEGORY_SUMMARY.md: Count of snippets per category
- TAG_SUMMARY.md: Count of snippets per tag
- README.md: Updates the snippet index section
"""

import os
import re
from collections import defaultdict
from pathlib import Path

SNIPPETS_DIR = Path(__file__).parent.parent / "snippets"
README_PATH = Path(__file__).parent.parent / "README.md"

SNIPPET_INDEX_START = "<!-- SNIPPET_CATEGORIES_START -->"
SNIPPET_INDEX_END = "<!-- SNIPPET_CATEGORIES_END -->"


# Recursively find all .md files in snippets, excluding summary/index files
def get_all_snippet_files():
    summary_files = {"TAG_SUMMARY.md", "CATEGORY_SUMMARY.md", "INDEX.md"}
    files = []
    for root, dirs, filenames in os.walk(SNIPPETS_DIR):
        for fname in filenames:
            if fname.endswith(".md") and fname not in summary_files:
                rel_path = os.path.relpath(os.path.join(root, fname), SNIPPETS_DIR)
                files.append(rel_path)
    return sorted(files)


def extract_tags_footer(content):
    """Extract tags from the '## 🏷️ Tags' section at the end of the file."""
    match = re.search(r"## 🏷️ Tags\s*\n([\s\S]+?)(?:\n## |\n# |\n$)", content)
    if not match:
        return []
    tag_block = match.group(1).strip()
    # Support both comma-separated and line-separated tags
    tags = []
    for line in tag_block.splitlines():
        for tag in line.split(","):
            tag = tag.strip()
            # Remove backticks if present
            tag = tag.strip("`")
            if tag:
                tags.append(tag)
    return tags


def extract_snippets_from_file(file_path):
    """Extract all snippets from a markdown file."""
    snippets = []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all snippet sections with current format
    pattern = r"### 🧩 (.+?)\n\n```python\n(.*?)```\n\n📂 (.+?)\n\n🏷️ Tags: (.+?)\n📝 Notes:\n(.*?)(?=\n### 🧩|\n## 🔗|\n## 🏷️|\n## 📝|\n$)"
    matches = re.findall(pattern, content, re.DOTALL)

    for title, code, description, tags, notes in matches:
        title = title.strip()
        description = description.strip()
        snippet_tags = [tag.strip() for tag in tags.split(",")]
        notes = notes.strip()
        snippets.append(
            {
                "title": title,
                "code": code.strip(),
                "description": description,
                "tags": snippet_tags,
                "notes": notes,
                "file": file_path,
            }
        )
    return snippets


def get_category_from_filename(filename):
    # Use the first folder as the category, or the file name if at root
    parts = filename.split(os.sep)
    if len(parts) > 1:
        return parts[0].replace("_", " ").title()
    else:
        return filename.replace(".md", "").replace("_", " ").title()


def generate_index_md_all_titles():
    lines = ["# Snippet Index\n"]
    snippet_files = get_all_snippet_files()

    # Group files by category (first folder)
    categories = defaultdict(list)
    for rel_path in snippet_files:
        parts = rel_path.split(os.sep)
        if len(parts) > 1:
            category = parts[0].replace("_", " ").title()
        else:
            category = rel_path.replace(".md", "").replace("_", " ").title()
        categories[category].append(rel_path)

    # Generate hierarchical index
    for category in sorted(categories.keys()):
        lines.append(f"## {category} Snippets")

        for rel_path in sorted(categories[category]):
            path = SNIPPETS_DIR / rel_path
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Get the file's title from the first heading
            title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
            file_title = (
                title_match.group(1).strip()
                if title_match
                else rel_path.replace(".md", "").replace("_", " ").title()
            )

            # Get snippet titles from the file
            snippet_titles = re.findall(r"^### ?(?:🧩 )?(.+)$", content, re.MULTILINE)

            if snippet_titles:
                lines.append(f"### {file_title}")
                for title in snippet_titles:
                    lines.append(f"- **🧩 {title.strip()}**")
                lines.append("")

    return "\n".join(lines)


def generate_category_summary(all_snippets):
    lines = ["# Category Summary\n"]

    # Group snippets by category and subcategory
    category_data = defaultdict(lambda: defaultdict(int))
    for snippet in all_snippets:
        rel_path = snippet["file"]
        parts = rel_path.split(os.sep)

        if len(parts) > 1:
            category = parts[0].replace("_", " ").title()
            subcategory = parts[1].replace("_", " ").title()
            category_data[category][subcategory] += 1
        else:
            category = rel_path.replace(".md", "").replace("_", " ").title()
            category_data[category][""] += 1

    # Check which categories actually have subfolders
    categories_with_subfolders = set()
    for category_name in category_data.keys():
        category_dir = SNIPPETS_DIR / category_name.lower().replace(" ", "_")
        if category_dir.exists() and category_dir.is_dir():
            # Check if this directory has any subdirectories
            for item in category_dir.iterdir():
                if item.is_dir():
                    categories_with_subfolders.add(category_name)
                    break

    # Sort categories by total count (descending), then by name
    sorted_categories = sorted(category_data.items(), key=lambda x: (-sum(x[1].values()), x[0]))

    for category, subcategories in sorted_categories:
        total_count = sum(subcategories.values())

        if category in categories_with_subfolders:
            # Has subfolders, show breakdown
            lines.append(f"- {category} Snippets: {total_count}")
            # Sort subcategories by count (descending), then by name
            sorted_subcategories = sorted(subcategories.items(), key=lambda x: (-x[1], x[0]))
            for subcategory, count in sorted_subcategories:
                if subcategory:  # Skip empty subcategory (files in root)
                    lines.append(f"    - {subcategory}: {count}")
        else:
            # No subfolders, just show main count
            lines.append(f"- {category} Snippets: {total_count}")

    return "\n".join(lines)


def generate_tag_summary(all_snippets):
    lines = ["# Tag Summary\n"]
    tag_counts = defaultdict(int)
    # Count all snippet tags
    for snippet in all_snippets:
        for tag in snippet["tags"]:
            tag_counts[tag] += 1
    # For each file, add footer tags as a single additional occurrence
    files_seen = set()
    for snippet in all_snippets:
        rel_path = snippet["file"]
        if rel_path in files_seen:
            continue
        files_seen.add(rel_path)
        with open(SNIPPETS_DIR / rel_path, "r", encoding="utf-8") as f:
            content = f.read()
        footer_tags = extract_tags_footer(content)
        for tag in footer_tags:
            tag_counts[tag] += 1
    sorted_tags = sorted(tag_counts.items(), key=lambda x: (-x[1], x[0]))
    for tag, count in sorted_tags:
        lines.append(f"- {tag}: {count}")
    return "\n".join(lines)


def update_readme_with_index():
    try:
        with open(SNIPPETS_DIR / "CATEGORY_SUMMARY.md", "r", encoding="utf-8") as f:
            category_content = f.read()
        category_lines = category_content.split("\n")[1:]
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme = f.read()
        start = readme.find(SNIPPET_INDEX_START)
        end = readme.find(SNIPPET_INDEX_END)
        if start != -1 and end != -1:
            before = readme[: start + len(SNIPPET_INDEX_START)]
            after = readme[end + len(SNIPPET_INDEX_END) :]
            # Ensure newlines before and after the inserted block and marker
            new_readme = (
                before.rstrip()
                + "\n\n"
                + "\n".join(category_lines).rstrip()
                + "\n\n"
                + SNIPPET_INDEX_END
                + after
            )
        else:
            new_readme = (
                readme.rstrip()
                + f"\n\n{SNIPPET_INDEX_START}\n"
                + "\n".join(category_lines).rstrip()
                + f"\n\n{SNIPPET_INDEX_END}\n"
            )
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("  📝 Updated README.md with snippet index section")
    except Exception as e:
        print(f"  ⚠️  Warning: Could not update README.md: {e}")


def main():
    print("🔄 Updating snippet indexes...")
    all_snippets = []
    for rel_path in get_all_snippet_files():
        file_path = SNIPPETS_DIR / rel_path
        print(f"  📄 Processing {rel_path}...")
        snippets = extract_snippets_from_file(file_path)
        for s in snippets:
            s["file"] = rel_path  # Store relative path for summaries
        all_snippets.extend(snippets)
    print(
        f"  📊 Found {len(all_snippets)} snippets across {len(set(s['file'] for s in all_snippets))} files"
    )
    print("  📝 Generating INDEX.md...")
    index_content = generate_index_md_all_titles()
    with open(SNIPPETS_DIR / "INDEX.md", "w", encoding="utf-8") as f:
        f.write(index_content.rstrip() + "\n")
    print("  📝 Generating CATEGORY_SUMMARY.md...")
    category_content = generate_category_summary(all_snippets)
    with open(SNIPPETS_DIR / "CATEGORY_SUMMARY.md", "w", encoding="utf-8") as f:
        f.write(category_content.rstrip() + "\n")
    print("  📝 Generating TAG_SUMMARY.md...")
    tag_content = generate_tag_summary(all_snippets)
    with open(SNIPPETS_DIR / "TAG_SUMMARY.md", "w", encoding="utf-8") as f:
        f.write(tag_content.rstrip() + "\n")
    update_readme_with_index()
    print("✅ All indexes updated successfully!")
    categories = set(get_category_from_filename(s["file"]) for s in all_snippets)
    tags = set()
    for snippet in all_snippets:
        tags.update(snippet["tags"])
    print("\n📈 Summary:")
    print(f"  - Total snippets: {len(all_snippets)}")
    print(f"  - Categories: {len(categories)}")
    print(f"  - Unique tags: {len(tags)}")


if __name__ == "__main__":
    main()

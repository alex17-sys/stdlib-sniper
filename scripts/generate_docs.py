"""
generate_mkdocs.py
------------------
Generates MkDocs documentation from snippets for Material theme.
"""

import os
import re
import shutil
import yaml

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")


def extract_snippet_info(content):
    """Extract snippet information from markdown content, preserving heading level."""
    snippets = []
    # Regex to match heading level, title, and up to Notes (no emoji required)
    pattern = r"^(#{2,}) ?(?:🧩 )?(.+?)\n+```python\n(.*?)```\n+(?:✅ Zero dependencies\n+)?📂 (.+?)\n+🏷️ Tags: (.+?)\n+📝 Notes:\n"
    matches = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))
    for i, match in enumerate(matches):
        heading_level = match.group(1)  # e.g., '###'
        title = match.group(2).strip().replace("🧩", "").strip()
        code = match.group(3).strip()
        description = match.group(4).strip()
        tags = [tag.strip() for tag in match.group(5).split(",")]
        notes_start = match.end()
        if i + 1 < len(matches):
            notes_end = matches[i + 1].start()
        else:
            next_heading = re.search(r"^#", content[notes_start:], re.MULTILINE)
            notes_end = notes_start + next_heading.start() if next_heading else len(content)
        notes_block = content[notes_start:notes_end]
        notes_lines = [line for line in notes_block.splitlines() if line.strip().startswith("- ")]
        notes = "\n".join(notes_lines)
        snippets.append(
            {
                "heading_level": heading_level,
                "title": title,
                "code": code,
                "description": description,
                "tags": tags,
                "notes": notes,
            }
        )
    return snippets


def generate_snippet_markdown(snippet):
    """Generate Markdown for a single snippet with Material theme features."""
    tags_md = " ".join([f"`{tag}`" for tag in snippet["tags"]])
    # Treat every non-empty line as a note, regardless of dash
    notes_list = [
        f"- {line.lstrip('-').strip()}" for line in snippet["notes"].split("\n") if line.strip()
    ]
    if notes_list:
        notes_md = "\n".join([notes_list[0]] + [f"    {line}" for line in notes_list[1:]])
        notes_block = f'\n!!! note "Notes"\n    {notes_md}\n'
    else:
        notes_block = ""
    # Use the original heading level for the snippet title
    return f"""{snippet["heading_level"]} {snippet["title"]}

{tags_md}

{snippet["description"]}

```python
{snippet["code"]}
```
{notes_block}
<hr class=\"snippet-divider\">
"""


def extract_page_description(file_content):
    """Extract the first non-empty paragraph after the title as the description."""
    lines = file_content.splitlines()
    found_title = False
    for i, line in enumerate(lines):
        if line.strip().startswith("# "):
            found_title = True
            continue
        if found_title:
            # Find first non-empty, non-heading, non-metadata line
            if (
                line.strip()
                and not line.strip().startswith("#")
                and not line.strip().startswith("---")
            ):
                return line.strip()
    # Fallback
    return "Zero-dependency Python snippets using only the standard library."


def generate_category_page(
    category_name, snippets, file_description=None, file_path=None, rel_path=None
):
    """Generate MkDocs Markdown page for a category, with YAML front matter only (no meta tags in Markdown)."""
    page_title = category_name
    trailing_content = ""
    file_content = ""
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
            for line in file_content.splitlines():
                if line.strip().startswith("# "):
                    page_title = line.strip().lstrip("#").strip()
                    break
    # Extract description from file content
    page_description = (
        extract_page_description(file_content)
        if file_content
        else (
            file_description or "Zero-dependency Python snippets using only the standard library."
        )
    )
    if not file_description:
        file_description = page_description
    snippets_md = "\n".join([generate_snippet_markdown(snippet) for snippet in snippets])
    # Find the end of the last snippet and include only true trailing content
    if snippets and file_content:
        last_snippet = snippets[-1]
        last_code = last_snippet["code"]
        last_code_idx = file_content.rfind(last_code)
        if last_code_idx != -1:
            after_code_idx = file_content.find("```", last_code_idx + len(last_code))
            if after_code_idx != -1:
                # Start after the last code block
                lines = file_content[after_code_idx + 3 :].splitlines()
                # Skip snippet metadata lines
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    if (
                        not line
                        or line.startswith("📂")
                        or line.startswith("🏷️")
                        or line.startswith("📝")
                        or line.startswith("- ")
                    ):
                        i += 1
                    else:
                        break
                trailing_content = "\n".join(lines[i:]).strip("\n")
    # Collect all unique tags from all snippets
    all_tags = set()
    for snippet in snippets:
        all_tags.update(snippet.get("tags", []))
    keywords = ", ".join(sorted(all_tags))
    # YAML front matter only
    yaml_front_matter = (
        f"---\ntitle: {page_title}\ndescription: {page_description}\nkeywords: {keywords}\n---\n"
    )
    return f"""{yaml_front_matter}
# {page_title}

{file_description}

{len(snippets)} snippets available in this sub-category.

---

{snippets_md}
{trailing_content if trailing_content else ""}
"""


def build_nav_tree(base_dir, docs_dir):
    """Recursively build a nested navigation tree from the docs directory, excluding CONTRIBUTING.md."""
    nav = []
    for entry in sorted(os.listdir(docs_dir)):
        if entry in ("CONTRIBUTING.md", "WANTED_SNIPPETS.md", "LICENSE"):
            continue  # Exclude from categories
        full_path = os.path.join(docs_dir, entry)
        rel_path = os.path.relpath(full_path, base_dir)
        if os.path.isdir(full_path):
            # Recurse into subdirectory
            children = build_nav_tree(base_dir, full_path)
            if children:
                nav.append({entry.replace("_", " ").title(): children})
        elif entry.endswith(".md"):
            # Add markdown file
            name = os.path.splitext(entry)[0].replace("_", " ").title()
            nav.append({name: rel_path.replace(os.sep, "/")})
    return nav


def update_mkdocs_config():
    """Update mkdocs.yml with dynamic navigation based on docs/ structure."""
    mkdocs_path = os.path.join(PROJECT_ROOT, "mkdocs.yml")
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        content = f.read()
    nav_structure = [
        {"Home": "index.md"},
        {"Contributing": "CONTRIBUTING.md"},
        {"Wanted Snippets": "WANTED_SNIPPETS.md"},
        {"LICENSE": "LICENSE"},
        {"Categories": build_nav_tree(DOCS_DIR, DOCS_DIR)},
    ]
    nav_yaml = yaml.dump(
        nav_structure, default_flow_style=False, sort_keys=False, indent=2, allow_unicode=True
    )
    nav_pattern = r"(?ms)^nav:\s*\n(?:^[^\S\n]*-[^\n]*\n|^[^\S\n]+[^\n]+\n)*"
    new_nav_section = f"nav:\n{nav_yaml}"
    if re.search(nav_pattern, content):
        content = re.sub(nav_pattern, new_nav_section + "\n", content)
    else:
        edit_uri_pattern = r"(edit_uri: .*)\n"
        replacement = r"\1\n\n" + new_nav_section + "\n"
        content = re.sub(edit_uri_pattern, replacement, content)
    with open(mkdocs_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Updated mkdocs.yml with dynamic navigation (nested)")


def copy_static_docs():
    """Copy README.md, CONTRIBUTING.md, and WANTED_SNIPPETS.md to docs/."""
    files_to_copy = [
        ("README.md", "index.md"),
        ("CONTRIBUTING.md", "CONTRIBUTING.md"),
        ("WANTED_SNIPPETS.md", "WANTED_SNIPPETS.md"),
        ("LICENSE", "LICENSE"),
    ]
    for src_name, dst_name in files_to_copy:
        src = os.path.join(PROJECT_ROOT, src_name)
        dst = os.path.join(DOCS_DIR, dst_name)
        if os.path.isfile(src):
            shutil.copyfile(src, dst)
            print(f"✅ Copied {src_name} to docs/{dst_name}")
        else:
            print(f"⚠️  {src_name} not found in project root. Skipping.")


def main():
    """Main function to generate MkDocs documentation."""
    print("📚 Generating MkDocs documentation (nested)...")

    # Create docs directory
    os.makedirs(DOCS_DIR, exist_ok=True)

    # Remove all files/folders in docs except assets, javascripts, stylesheets
    for entry in os.listdir(DOCS_DIR):
        if entry not in {"assets", "javascripts", "stylesheets", "overrides"}:
            path = os.path.join(DOCS_DIR, entry)
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    # Always copy static docs (README, CONTRIBUTING, WANTED_SNIPPETS)
    copy_static_docs()

    categories = {}

    # Process each snippet file
    for root, dirs, files in os.walk(SNIPPETS_DIR):
        for fname in files:
            if fname.endswith(".md"):
                snippet_path = os.path.join(root, fname)
                rel_dir = os.path.relpath(root, SNIPPETS_DIR)
                rel_dir = "" if rel_dir == "." else rel_dir
                docs_subdir = os.path.join(DOCS_DIR, rel_dir)
                os.makedirs(docs_subdir, exist_ok=True)

                with open(snippet_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Extract category name from filename
                category_name = os.path.splitext(fname)[0].replace("_", " ").title()

                # Extract snippets
                snippets = extract_snippet_info(content)

                if snippets:
                    categories[rel_dir + "/" + category_name.lower().replace(" ", "_")] = len(
                        snippets
                    )

                    # Generate category page
                    rel_path = os.path.join(rel_dir, fname) if rel_dir else fname
                    category_md = generate_category_page(
                        category_name,
                        snippets,
                        file_description=None,
                        file_path=snippet_path,
                        rel_path=rel_path,
                    )

                    out_path = os.path.join(docs_subdir, fname)
                    with open(out_path, "w", encoding="utf-8") as f:
                        f.write(category_md)

                    print(
                        f"✅ Generated {rel_dir + '/' + category_name.lower().replace(' ', '_')} ({len(snippets)} snippets)"
                    )

    # Update mkdocs.yml with dynamic navigation
    update_mkdocs_config()

    print("\n🎉 MkDocs documentation generated successfully!")
    print(f"📁 Output directory: {DOCS_DIR}")
    print(f"📊 Total categories: {len(categories)}")
    print(f"📝 Total snippets: {sum(categories.values())}")
    print("\n🚀 To view the documentation:")
    print("   1. Run: mkdocs serve")
    print("   2. Open: http://127.0.0.1:8000")


if __name__ == "__main__":
    main()

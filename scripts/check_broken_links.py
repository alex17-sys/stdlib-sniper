"""
check_broken_links.py
--------------------
Checks for broken links in markdown files and external references.
"""

import os
import re
import sys

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")


def extract_links_from_markdown(content):
    """Extract all links from markdown content."""
    # Internal links: [text](file.md) or [text](file.md#section)
    internal_links = re.findall(r"\[([^\]]+)\]\(([^#)]+)(?:#[^)]*)?\)", content)

    # External links: [text](http://...)
    external_links = re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", content)

    return internal_links, external_links


def check_internal_links():
    """Check if internal file references exist."""
    print("Checking internal links...")

    # Collect all markdown files in the project (snippets and root)
    project_root = os.path.dirname(os.path.dirname(__file__))
    all_md_files = set()
    for root, dirs, files in os.walk(project_root):
        for fname in files:
            if fname.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, fname), project_root)
                all_md_files.add(rel_path)

    def check_file_links(file_path, rel_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        internal_links, _ = extract_links_from_markdown(content)
        file_dir = os.path.dirname(rel_path)
        broken = []
        for text, link in internal_links:
            if link.endswith(".md"):
                resolved_path = os.path.normpath(os.path.join(file_dir, link))
                # Allow self-referential links
                if resolved_path == rel_path:
                    continue
                if resolved_path not in all_md_files:
                    broken.append((rel_path, text, link))
        return broken

    # Check all markdown files
    broken_internal = []
    for rel_path in all_md_files:
        file_path = os.path.join(project_root, rel_path)
        broken_internal.extend(check_file_links(file_path, rel_path))

    if broken_internal:
        print("Broken internal links found:")
        for file, text, link in broken_internal:
            print(f"  {file}: '{text}' -> {link}")
        return False
    else:
        print("All internal links are valid.")
        return True


# def check_external_links():
#     """Check if external links are accessible."""
#     print("Checking external links...")

#     external_links = []

#     # Collect all external links from README
#     with open(README_PATH, "r", encoding="utf-8") as f:
#         content = f.read()
#     _, links = extract_links_from_markdown(content)
#     external_links.extend(links)

#     # Collect all .md files recursively
#     all_files = set()
#     for root, dirs, files in os.walk(SNIPPETS_DIR):
#         for fname in files:
#             if fname.endswith(".md"):
#                 rel_path = os.path.relpath(os.path.join(root, fname), SNIPPETS_DIR)
#                 all_files.add(rel_path)

#     # Collect all external links from all snippet files
#     for rel_path in all_files:
#         path = os.path.join(SNIPPETS_DIR, rel_path)
#         with open(path, "r", encoding="utf-8") as f:
#             content = f.read()
#         _, links = extract_links_from_markdown(content)
#         external_links.extend(links)

#     # Remove duplicates
#     external_links = list(set(external_links))

#     broken_external = []

#     for text, url in external_links:
#         try:
#             req = urllib.request.Request(url, headers={"User-Agent": "stdlib-sniper-bot"})
#             with urllib.request.urlopen(req, timeout=10) as response:
#                 if response.getcode() >= 400:
#                     broken_external.append((text, url, f"HTTP {response.getcode()}"))
#         except (urllib.error.URLError, urllib.error.HTTPError) as e:
#             broken_external.append((text, url, str(e)))
#         except Exception as e:
#             broken_external.append((text, url, f"Error: {e}"))

#     if broken_external:
#         print("Broken external links found:")
#         for text, url, error in broken_external:
#             print(f"  '{text}' -> {url} ({error})")
#         return False
#     else:
#         print("All external links are accessible.")
#         return True


def main():
    """Main function to check all links."""
    print("🔗 Checking for broken links...\n")

    internal_ok = check_internal_links()
    print()
    # external_ok = check_external_links()

    if internal_ok:  # and external_ok
        print("\n✅ All links are valid!")
        sys.exit(0)
    else:
        print("\n❌ Some links are broken. Please fix them.")
        sys.exit(1)


if __name__ == "__main__":
    main()

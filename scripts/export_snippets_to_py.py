import os
import re

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")
EXPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets_py")

os.makedirs(EXPORT_DIR, exist_ok=True)


def cleanup_old_demo_files():
    """Remove all existing _demo.py files to ensure clean export."""
    for root, dirs, files in os.walk(EXPORT_DIR):
        for fname in files:
            if fname.endswith("_demo.py"):
                os.remove(os.path.join(root, fname))
                print(f"[CLEAN] Removed old {os.path.join(root, fname)}")


def get_file_hash(filepath):
    """Get a simple hash of file content for change detection."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return hash(f.read())
    except FileNotFoundError:
        return None


def extract_snippet_titles(path):
    """Extract all snippet titles from a file."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract all snippet titles (## 🧩 ... or ## ...)
    titles = re.findall(r"^### ?(?:🧩 )?(.+)", content, re.MULTILINE)
    return set(t.strip() for t in titles)


def find_snippet_code_by_title(file_path, target_title):
    """Find the code block for a specific snippet title in a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into snippets
    snippets = re.split(r"^### ?(?:🧩 )?", content, flags=re.MULTILINE)[1:]

    for snippet in snippets:
        lines = snippet.splitlines()
        if not lines:
            continue
        title = lines[0].strip()
        if title == target_title:
            # Find the code block in this snippet
            code_match = re.search(r"```python\n(.*?)```", snippet, re.DOTALL)
            if code_match:
                return code_match.group(1).strip()
    return None


def resolve_cross_reference(snippet_content, snippet_title):
    """Resolve a cross-reference by finding the actual code from the referenced file."""
    # Find the reference pattern: See [filename.md]
    ref_match = re.search(r"See \[([^\]]+\.md)\](?:\([^\)]*\))?", snippet_content)
    if not ref_match:
        return None

    ref_file = ref_match.group(1)
    ref_path = os.path.join(SNIPPETS_DIR, ref_file)

    if not os.path.exists(ref_path):
        print(f"[WARN] Cross-reference target not found: {ref_file}")
        return None

    # Try to find the code by matching the snippet title
    code = find_snippet_code_by_title(ref_path, snippet_title)
    if code:
        return code

    # If title doesn't match, try to find any code block in the referenced file
    with open(ref_path, "r", encoding="utf-8") as f:
        ref_content = f.read()

    # Find the first code block
    code_match = re.search(r"```python\n(.*?)```", ref_content, re.DOTALL)
    if code_match:
        print(f"[INFO] Using first code block from {ref_file} for '{snippet_title}'")
        return code_match.group(1).strip()

    return None


def main():
    """Main export function with cleanup and optimization."""
    print("[START] Exporting snippets to demo files...")

    # Clean up old demo files
    cleanup_old_demo_files()

    exported_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk(SNIPPETS_DIR):
        for fname in files:
            if (
                fname.endswith(".md")
                and not fname.endswith("SUMMARY.md")
                and fname not in ("INDEX.md",)
            ):
                path = os.path.join(root, fname)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Split content into snippets
                snippets = re.split(r"^### ?(?:🧩 )?", content, flags=re.MULTILINE)[1:]

                if not snippets:
                    continue

                py_lines = []
                processed_titles = set()

                for snippet in snippets:
                    lines = snippet.splitlines()
                    if not lines:
                        continue

                    title = lines[0].strip()
                    if title in processed_titles:
                        continue  # Skip duplicates

                    processed_titles.add(title)

                    # Check if this is a cross-reference snippet
                    if re.search(r"See \[[^\]]+\.md\]", snippet):
                        # This is a cross-reference, try to resolve it
                        resolved_code = resolve_cross_reference(snippet, title)
                        if resolved_code:
                            py_lines.append(f"# 🧩 {title}\n{resolved_code}\n")
                        else:
                            print(
                                f"[WARN] Could not resolve cross-reference for '{title}' in {fname}"
                            )
                    else:
                        # This is a regular snippet with code
                        code_match = re.search(r"```python\n(.*?)```", snippet, re.DOTALL)
                        if code_match:
                            py_lines.append(f"# 🧩 {title}\n{code_match.group(1).strip()}\n")

                # Only create the file if we have actual code snippets
                if py_lines:
                    rel_path = os.path.relpath(path, SNIPPETS_DIR)  # e.g. 'files/append_file.md'
                    export_py_path = os.path.join(
                        EXPORT_DIR, os.path.splitext(rel_path)[0] + "_demo.py"
                    )
                    os.makedirs(os.path.dirname(export_py_path), exist_ok=True)

                    with open(export_py_path, "w", encoding="utf-8") as outf:
                        outf.write("\n\n".join(py_lines))

                    exported_count += 1
                    print(f"[OK] Exported {export_py_path}")
                else:
                    skipped_count += 1
                    print(f"[SKIP] {path} (no code blocks or only cross-references)")

    print("\n[COMPLETE] Export finished:")
    print(f"  - Exported: {exported_count} files")
    print(f"  - Skipped: {skipped_count} files")

    # Auto-format all exported files
    try:
        import subprocess

        print(f"[FORMAT] Running 'ruff format' on {EXPORT_DIR}...")
        result = subprocess.run(["ruff", "format", EXPORT_DIR], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("[WARN] Ruff format failed:")
            print(result.stderr)
    except Exception as e:
        print(f"[WARN] Could not auto-format exported files: {e}")


if __name__ == "__main__":
    main()

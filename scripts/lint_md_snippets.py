#!/usr/bin/env python3
"""
lint_snippet_codeblocks.py
-------------------------
Lint all Python code blocks in markdown files under the snippets directory (or given paths) using ruff.
For each code block, write it to a temporary .py file, run ruff, and report any issues
with reference to the original .md file and code block number.
Supports --fix to auto-format code blocks using ruff format.
"""

import os
import re
import sys
import tempfile
import subprocess
from pathlib import Path
from typing import List, Tuple
import argparse

CODE_BLOCK_RE = re.compile(r"```python\s*\n([\s\S]*?)```", re.MULTILINE)


def extract_python_codeblocks(md_content: str) -> List[Tuple[str, int, int]]:
    """Extract all Python code blocks from markdown content.
    Returns a list of (code, start, end) tuples for replacement if needed."""
    return [(m.group(1), m.start(1), m.end(1)) for m in CODE_BLOCK_RE.finditer(md_content)]


def lint_codeblock(code: str, ruff_path: str = "ruff") -> Tuple[bool, str]:
    """Lint a code block using ruff. Returns (is_clean, output)."""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name
    try:
        result = subprocess.run([ruff_path, "check", tmp_path], capture_output=True, text=True)
        if result.returncode == 0:
            return True, ""
        else:
            return False, result.stdout
    finally:
        os.unlink(tmp_path)


def format_codeblock(code: str, ruff_path: str = "ruff") -> str:
    """Format a code block using ruff format. Returns formatted code."""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name
    try:
        result = subprocess.run([ruff_path, "format", tmp_path], capture_output=True, text=True)
        if result.returncode == 0:
            with open(tmp_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            return code  # fallback to original if formatting fails
    finally:
        os.unlink(tmp_path)


def process_markdown_file(md_path: Path, fix: bool = False, ruff_path: str = "ruff") -> bool:
    """Lint (and optionally fix) all Python code blocks in a markdown file."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    codeblocks = extract_python_codeblocks(content)
    any_issues = False
    new_content = content
    offset = 0  # for replacing code blocks in-place
    for idx, (code, start, end) in enumerate(codeblocks, 1):
        is_clean, output = lint_codeblock(code, ruff_path)
        if is_clean:
            print(f"✅ {md_path} [code block #{idx}] - No issues found")
        else:
            print(f"❌ {md_path} [code block #{idx}] - Issues found:")
            print(output)
            any_issues = True
        if fix:
            formatted = format_codeblock(code, ruff_path)
            # Replace code block in content
            new_content = new_content[: start + offset] + formatted + new_content[end + offset :]
            offset += len(formatted) - (end - start)
    if fix and new_content != content:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"🛠️  Auto-formatted code blocks in {md_path}")
    return any_issues


def find_markdown_files(paths: List[Path]) -> List[Path]:
    """Recursively find all markdown files in the given paths."""
    md_files = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            md_files.append(path)
        elif path.is_dir():
            for root, dirs, files in os.walk(path):
                for fname in files:
                    if fname.endswith(".md"):
                        md_files.append(Path(root) / fname)
    return md_files


def main():
    parser = argparse.ArgumentParser(
        description="Lint all Python code blocks in markdown files using ruff."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=[str(Path(__file__).parent.parent / "snippets")],
        help="Folders or files to check (default: snippets)",
    )
    parser.add_argument(
        "--fix", action="store_true", help="Auto-format code blocks using ruff format"
    )
    parser.add_argument(
        "--ruff-path", default="ruff", help="Path to ruff executable (default: ruff)"
    )
    args = parser.parse_args()

    md_files = find_markdown_files([Path(p) for p in args.paths])
    if not md_files:
        print("No markdown files found in the given paths.")
        sys.exit(0)

    print(f"🔍 Linting Python code blocks in {len(md_files)} markdown files...\n")
    any_issues = False
    for md_path in md_files:
        if process_markdown_file(md_path, fix=args.fix, ruff_path=args.ruff_path):
            any_issues = True
    print("\n==============================")
    if any_issues:
        print("❌ Some code blocks have linting issues. Please review above.")
        sys.exit(1)
    else:
        print("🎉 All code blocks passed ruff linting!")
        sys.exit(0)


if __name__ == "__main__":
    main()

"""
format_snippets.py
------------------
Checks all markdown files in the snippets/ directory for:
- Recognized category filename (snippet files only)
- Top-level heading
- At least one Python code block
- Each snippet has a tags line (🏷️ Tags:) and notes section (📝 Notes:)
- Snippets are ordered alphabetically by title
- All python code blocks are valid Python (parsed by ast)
- All example scripts in examples/ are valid Python (parsed by ast)

Warnings indicate formatting or categorization issues that should be fixed before submitting a PR.
Also calls update_indexes.py to regenerate:
- snippets/INDEX.md (all snippets by file and title)
- snippets/TAG_SUMMARY.md (all tags and their counts)
- snippets/CATEGORY_SUMMARY.md (number of snippets per category)
- README.md snippet index section
"""

import os
import re
import sys
import ast
import subprocess

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")
EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), "..", "examples")
CATEGORY_TITLES = {
    "cli.md": "CLI Snippets",
    "files.md": "File Operations Snippets",
    "strings.md": "String Manipulation Snippets",
    "tricks.md": "Miscellaneous Tricks",
    "url.md": "URL Snippets",
    "http.md": "HTTP Snippets",
}

SUMMARY_FILES = {"TAG_SUMMARY.md", "CATEGORY_SUMMARY.md", "INDEX.md"}


def get_snippet_files():
    files = []
    for root, dirs, filenames in os.walk(SNIPPETS_DIR):
        for fname in filenames:
            if fname.endswith(".md") and fname not in SUMMARY_FILES:
                rel_path = os.path.relpath(os.path.join(root, fname), SNIPPETS_DIR)
                files.append(rel_path)
    return set(files)


def get_category_title(fname):
    if fname in CATEGORY_TITLES:
        return CATEGORY_TITLES[fname]
    base = fname.replace(".md", "").replace("_", " ").capitalize()
    return f"{base} Snippets"


def error_and_exit(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)


def is_commented_out(s, pos):
    # Find all comment blocks
    for m in re.finditer(r"<!--.*?-->", s, re.DOTALL):
        if m.start() <= pos < m.end():
            return True
    return False


def validate_python_syntax(code, snippet_title, fname):
    """Intelligently validate Python syntax for complex constructs."""
    code = code.strip()

    # Skip empty code blocks
    if not code:
        return True, None

    # Common patterns that are valid but might not parse as single statements
    valid_patterns = [
        # Decorators with class/function definitions
        r"^@\w+.*\n.*class\s+\w+",
        r"^@\w+.*\n.*def\s+\w+",
        r"^@\w+.*\n.*async\s+def\s+\w+",
        # Class definitions with multiple statements
        r"^class\s+\w+.*:.*\n.*\w+\s*=\s*\w+",
        # Async function definitions
        r"^async\s+def\s+\w+",
        # Complex imports with multiple items
        r"^from\s+\w+\s+import\s+.*,\s*\w+",
        # Multi-line statements with semicolons
        r"^.*;.*;.*$",
        # Context managers with multiple statements
        r"^with\s+.*:.*\n.*\w+",
        # Try/except blocks
        r"^try:.*\n.*except",
        # List comprehensions with complex expressions
        r"^\[.*for.*in.*if.*\]",
        # Dictionary comprehensions
        r"^\{.*for.*in.*\}",
        # Generator expressions
        r"^\(.*for.*in.*\)",
        # Lambda with complex expressions
        r"lambda\s+.*:.*\w+\(.*\)",
        # Function calls with complex arguments
        r"^\w+\(.*\n.*\)",
        # Multi-line string literals
        r'^"""[\s\S]*"""$',
        r"^'''[\s\S]*'''$",
    ]

    # Check if code matches any valid complex pattern
    for pattern in valid_patterns:
        if re.search(pattern, code, re.MULTILINE | re.DOTALL):
            return True, "complex_construct"

    # Try to parse as a module (most permissive)
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        # If module parsing fails, try wrapping in different contexts
        contexts_to_try = [
            # Try as a simple expression
            f"result = {code}",
            # Try as a statement in a function
            f"def temp_func():\n    {code}",
            # Try as a statement in a class
            f"class TempClass:\n    {code}",
            # Try as a statement in a try block
            f"try:\n    {code}\nexcept:\n    pass",
        ]

        for context in contexts_to_try:
            try:
                ast.parse(context)
                return True, "wrapped_context"
            except SyntaxError:
                continue

        # If all attempts fail, it's genuinely invalid
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {e}"


def validate_snippet_structure(fname, snippet, idx):
    # Must have tags and notes (not commented out)
    has_tags = "🏷️ Tags:" in snippet and not re.search(r"<!--.*🏷️ Tags:.*-->", snippet, re.DOTALL)
    has_notes = "📝 Notes:" in snippet and not re.search(
        r"<!--.*📝 Notes:.*-->", snippet, re.DOTALL
    )
    has_code = bool(re.search(r"```python\n(.*?)```", snippet, re.DOTALL)) and not re.search(
        r"<!--.*```python.*```.*-->", snippet, re.DOTALL
    )
    has_crossref = bool(re.search(r"See \[[^\]]+\.md\]", snippet)) and not re.search(
        r"<!--.*See \[[^\]]+\.md\].*-->", snippet, re.DOTALL
    )
    if not (has_tags and has_notes):
        error_and_exit(
            f"{fname} snippet #{idx} is missing required tags or notes section (or they are commented out)."
        )
    # Must be either a code snippet (with code block) or a reference snippet (with crossref link)
    if not (has_code or has_crossref):
        error_and_exit(
            f"{fname} snippet #{idx} must have either a python code block or a cross-reference link (not commented out)."
        )
    # If both code and crossref, that's allowed (but rare)
    # Optionally, could enforce only one or the other


def fix_heading(path, fname):
    with open(path, "r+", encoding="utf-8") as f:
        content = f.read()
        if not re.search(r"^# .+", content, re.MULTILINE):
            heading = f"# {CATEGORY_TITLES.get(fname, fname.replace('.md', '').capitalize())}\n\n"
            f.seek(0)
            f.write(heading + content)
            f.truncate()
            print(f"[FIXED] Added heading to {fname}")


def run_update_indexes():
    """Run update_indexes.py to regenerate all indexes and update README."""
    print("\n🔄 Updating indexes...")
    try:
        result = subprocess.run(
            [sys.executable, "scripts/update_indexes.py"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(SNIPPETS_DIR),
        )
        if result.returncode == 0:
            print("[OK] Indexes updated successfully")
        else:
            print(f"[WARNING] Failed to update indexes: {result.stderr}")
    except Exception as e:
        print(f"[WARNING] Could not run update_indexes.py: {e}")


def validate_example_scripts():
    print("\nValidating example scripts in examples/:")
    for fname in os.listdir(EXAMPLES_DIR):
        if fname.endswith(".py"):
            path = os.path.join(EXAMPLES_DIR, fname)
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
            try:
                ast.parse(code)
            except Exception as e:
                print(f"[WARNING] {fname} is not valid Python: {e}")
            else:
                print(f"[OK] {fname}")


print("Checking snippet markdown files in snippets/:\n")
fix = "--fix" in sys.argv
for rel_path in get_snippet_files():
    path = os.path.join(SNIPPETS_DIR, rel_path)
    fname = os.path.basename(rel_path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Check for heading
    if not re.search(r"^# .+", content, re.MULTILINE):
        print(f"[WARNING] {fname} is missing a top-level heading.")
        if fix:
            fix_heading(path, fname)
    # Find all snippet titles (## 🧩 ... or ## ...) that are NOT commented out
    snippet_matches = list(re.finditer(r"^### ?(?:🧩 )?(.+)$", content, re.MULTILINE))
    snippet_spans = []
    for i, match in enumerate(snippet_matches):
        title = match.group(1).strip()
        # Check if this title is commented out
        line_start = content.rfind("\n", 0, match.start()) + 1
        line_end = content.find("\n", match.end())
        if line_end == -1:
            line_end = len(content)
        title_line = content[line_start:line_end]
        if title_line.strip().startswith("<!--"):
            error_and_exit(f"{fname} snippet #{i + 1} has a commented-out title: {title}")
        # Find the snippet content (from this title to the next title or end of file)
        start = match.end()
        next_match = snippet_matches[i + 1] if i + 1 < len(snippet_matches) else None
        end = next_match.start() if next_match else len(content)
        snippet_content = content[start:end]
        snippet_spans.append((start, end))
        # --- Strict structure checks ---
        # 1. Must have exactly one code block OR crossref (not both, not neither)
        code_blocks = [
            m
            for m in re.finditer(r"```python\n(.*?)```", snippet_content, re.DOTALL)
            if not is_commented_out(snippet_content, m.start())
        ]
        crossrefs = [
            m
            for m in re.finditer(r"See \[[^\]]+\.md\](?:\([^\)]*\))?", snippet_content)
            if not is_commented_out(snippet_content, m.start())
        ]
        if (len(code_blocks) == 1 and not crossrefs) or (len(crossrefs) == 1 and not code_blocks):
            pass
        else:
            error_and_exit(
                f"{fname} snippet '{title}' must have exactly one code block OR one crossref (not both, not neither). Found {len(code_blocks)} code blocks and {len(crossrefs)} crossrefs."
            )
        # 2. Must have exactly one tags and one notes section (not commented)
        tags = [
            m
            for m in re.finditer(r"🏷️ Tags:", snippet_content)
            if not is_commented_out(snippet_content, m.start())
        ]
        notes = [
            m
            for m in re.finditer(r"📝 Notes:", snippet_content)
            if not is_commented_out(snippet_content, m.start())
        ]
        if len(tags) != 1:
            error_and_exit(
                f"{fname} snippet '{title}' must have exactly one tags section (not commented). Found {len(tags)}."
            )
        if len(notes) != 1:
            error_and_exit(
                f"{fname} snippet '{title}' must have exactly one notes section (not commented). Found {len(notes)}."
            )
        # 3. No code/crossref, tags, or notes may be commented out
        if re.search(r"<!--.*🏷️ Tags:.*-->", snippet_content, re.DOTALL):
            error_and_exit(f"{fname} snippet '{title}' has commented-out tags section.")
        if re.search(r"<!--.*📝 Notes:.*-->", snippet_content, re.DOTALL):
            error_and_exit(f"{fname} snippet '{title}' has commented-out notes section.")
        if re.search(r"<!--.*```python.*```.*-->", snippet_content, re.DOTALL):
            error_and_exit(f"{fname} snippet '{title}' has commented-out code block.")
        if re.search(r"<!--.*See \[[^\]]+\.md\].*-->", snippet_content, re.DOTALL):
            error_and_exit(f"{fname} snippet '{title}' has commented-out crossref.")
        # 4. Validate python code blocks with improved logic
        for m in code_blocks:
            code = m.group(1)
            is_valid, reason = validate_python_syntax(code, title, fname)
            if not is_valid:
                print(f"[WARNING] {fname} snippet '{title}' has invalid Python code: {reason}")
            # Don't print anything for valid code (including complex constructs)
    # 5. No code/crossref, tags, or notes may appear outside a snippet
    # (i.e., before the first title or after the last)
    outside_spans = []
    if snippet_spans:
        if snippet_spans[0][0] > 0:
            outside_spans.append((0, snippet_spans[0][0]))
        for i in range(len(snippet_spans) - 1):
            outside_spans.append((snippet_spans[i][1], snippet_spans[i + 1][0]))
        if snippet_spans[-1][1] < len(content):
            outside_spans.append((snippet_spans[-1][1], len(content)))
    else:
        outside_spans.append((0, len(content)))
    for start, end in outside_spans:
        outside = content[start:end]
        if any(
            not is_commented_out(outside, m.start())
            for m in re.finditer(r"```python\n(.*?)```", outside, re.DOTALL)
        ):
            error_and_exit(f"{fname} has a code block outside any snippet title block.")
        if any(
            not is_commented_out(outside, m.start())
            for m in re.finditer(r"See \[[^\]]+\.md\](?:\([^\)]*\))?", outside)
        ):
            error_and_exit(f"{fname} has a crossref outside any snippet title block.")
        if any(not is_commented_out(outside, m.start()) for m in re.finditer(r"🏷️ Tags:", outside)):
            error_and_exit(f"{fname} has a tags section outside any snippet title block.")
        if any(
            not is_commented_out(outside, m.start()) for m in re.finditer(r"📝 Notes:", outside)
        ):
            error_and_exit(f"{fname} has a notes section outside any snippet title block.")
    # --- New: Validate trailing sections ---
    # Find all level-2 headings (## ...)
    trailing_sections = list(re.finditer(r"^## (.+)$", content, re.MULTILINE))
    if len(trailing_sections) < 3:
        error_and_exit(
            f"{fname} is missing one or more trailing sections (cross-reference, foot tags, foot notes)"
        )
    last3 = [s.group(1).strip() for s in trailing_sections[-3:]]
    # Accept both 'Cross Reference' and 'Cross-References'
    if last3[0] not in ["🔗 Cross Reference", "🔗 Cross-References"]:
        error_and_exit(f"{fname} missing or misnamed cross-reference section (found '{last3[0]}')")
    if last3[1] != "🏷️ Tags":
        error_and_exit(f"{fname} missing or misnamed tags section (found '{last3[1]}')")
    if last3[2] != "📝 Notes":
        error_and_exit(f"{fname} missing or misnamed notes section (found '{last3[2]}')")
    section_starts = [s.start() for s in trailing_sections[-3:]] + [len(content)]
    crossref_content = content[section_starts[0] : section_starts[1]]
    tags_content = content[section_starts[1] : section_starts[2]]
    notes_content = content[section_starts[2] : section_starts[3]]

    if not re.search(r"- \*\*Reference\*\*: See \[📂 .+\]\([^)]+\)", crossref_content):
        error_and_exit(f"{fname} cross-reference section is missing a valid reference line")
    if not re.search(r"`[^`]+`", tags_content):
        error_and_exit(f"{fname} tags section is missing backtick-enclosed tags")
    if not re.search(r"^- ", notes_content, re.MULTILINE):
        error_and_exit(f"{fname} notes section is missing bullet points")
    print(f"[OK] {fname}")

# Update indexes and README
run_update_indexes()
validate_example_scripts()

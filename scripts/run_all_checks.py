import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(__file__)

all_ok = True


def run_step(description, command, shell=False):
    print(f"\n=== {description} ===")
    result = subprocess.run(command, capture_output=True, text=True, shell=shell)
    print(result.stdout)
    if result.returncode != 0:
        print(f"[FAIL] {description}")
        return False
    else:
        print(f"[OK] {description}")
        return True


# 1. Update indexes and export snippets
if not run_step(
    "Updating indexes", [sys.executable, os.path.join(SCRIPT_DIR, "update_indexes.py")]
):
    sys.exit(1)
if not run_step(
    "Exporting snippets to Python",
    [sys.executable, os.path.join(SCRIPT_DIR, "export_snippets_to_py.py")],
):
    sys.exit(1)
# --- PATCH START: Format exported Python snippets ---
if not run_step(
    "Auto-formatting exported Python snippets",
    ["ruff", "format", "snippets_py/"],
):
    print("❌ Auto-formatting failed for snippets_py/. Please check the output above.")
    sys.exit(1)
# --- PATCH END ---

# 2. Lint and validate
if not run_step(
    "Checking for duplicate snippets",
    [sys.executable, os.path.join(SCRIPT_DIR, "check_duplicate_snippets.py")],
):
    sys.exit(1)
if not run_step(
    "Validating snippet files", [sys.executable, os.path.join(SCRIPT_DIR, "validate_files.py")]
):
    sys.exit(1)
if not run_step(
    "Linting Markdown snippets", [sys.executable, os.path.join(SCRIPT_DIR, "lint_md_snippets.py")]
):
    sys.exit(1)
if not run_step(
    "Linting Python files", [sys.executable, os.path.join(SCRIPT_DIR, "lint_all_py_files.py")]
):
    sys.exit(1)

# 3. Check formatting (Ruff)
if not run_step("Checking format in snippets_py", ["ruff", "format", "--check", "snippets_py/"]):
    print(
        "❌ Checking format in snippets_py - Formatting issues found. Run 'ruff format snippets_py/' to fix."
    )
    sys.exit(1)

# 4. Check for broken links
if not run_step(
    "Checking for broken links", [sys.executable, os.path.join(SCRIPT_DIR, "check_broken_links.py")]
):
    sys.exit(1)

# 5. Generate docs
if not run_step(
    "Generating documentation", [sys.executable, os.path.join(SCRIPT_DIR, "generate_docs.py")]
):
    sys.exit(1)

print("\nAll checks passed!")

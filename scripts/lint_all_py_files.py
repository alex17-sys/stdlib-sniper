#!/usr/bin/env python3
"""
lint_with_ruff.py
-----------------
Comprehensive linting script using ruff for Python code quality checks.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Any


def run_ruff_check(target: str, description: str) -> bool:
    """Run ruff check on a target and return success status."""
    print(f"🔍 {description}...")

    try:
        result = subprocess.run(
            ["ruff", "check", target], capture_output=True, text=True, check=False
        )

        if result.returncode == 0:
            print(f"✅ {description} - No issues found")
            return True
        else:
            # Only print error if there is actual output
            error_lines = [
                line
                for line in result.stdout.split("\n")
                if line.strip() and not line.startswith("Found")
            ]
            if error_lines:
                print(f"❌ {description} - Found {len(error_lines)} issues:")
                print("\n".join(error_lines))
                return False
            else:
                print(f"✅ {description} - No issues found")
                return True

    except FileNotFoundError:
        print(f"❌ {description} - ruff not found. Install with: pip install ruff")
        return False
    except Exception as e:
        print(f"❌ {description} - Error: {e}")
        return False


def run_ruff_format_check(target: str, description: str) -> bool:
    """Run ruff format check on a target and return success status."""
    print(f"🎨 {description}...")

    try:
        result = subprocess.run(
            ["ruff", "format", "--check", target], capture_output=True, text=True, check=False
        )

        if result.returncode == 0:
            print(f"✅ {description} - Formatting is correct")
            return True
        else:
            print(f"❌ {description} - Formatting issues found:")
            print(result.stdout)
            return False

    except FileNotFoundError:
        print(f"❌ {description} - ruff not found. Install with: pip install ruff")
        return False
    except Exception as e:
        print(f"❌ {description} - Error: {e}")
        return False


def get_python_files(directory: str) -> List[str]:
    """Get all Python files in a directory recursively."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Skip virtual environments and other common directories to ignore
        dirs[:] = [
            d for d in dirs if d not in {".venv", "venv", "__pycache__", ".git", "node_modules"}
        ]

        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


def check_ruff_config() -> bool:
    """Check if ruff configuration is properly set up."""
    print("🔧 Checking ruff configuration...")

    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found")
        return False

    try:
        import tomllib
    except ImportError:
        try:
            import tomli as tomllib
        except ImportError:
            print("❌ tomllib/tomli not available")
            return False

    with open(pyproject_path, "rb") as f:
        config = tomllib.load(f)

    ruff_config = config.get("tool", {}).get("ruff", {})
    if not ruff_config:
        print("❌ No ruff configuration found in pyproject.toml")
        return False

    print("✅ ruff configuration found")
    print(f"   Line length: {ruff_config.get('line-length', 'not set')}")
    print(f"   Selected rules: {ruff_config.get('select', 'not set')}")
    print(f"   Ignored rules: {ruff_config.get('ignore', 'not set')}")

    return True


def lint_scripts_directory() -> bool:
    """Lint all Python files in the scripts directory."""
    scripts_dir = "scripts"
    if not os.path.exists(scripts_dir):
        print(f"❌ {scripts_dir} directory not found")
        return False

    python_files = get_python_files(scripts_dir)
    if not python_files:
        print(f"❌ No Python files found in {scripts_dir}")
        return False

    print(f"📁 Found {len(python_files)} Python files in {scripts_dir}")

    all_passed = True

    # Check each file individually for better error reporting
    for file_path in python_files:
        file_name = os.path.basename(file_path)
        if not run_ruff_check(file_path, f"Linting {file_name}"):
            all_passed = False

    # Check formatting for all files
    if not run_ruff_format_check(scripts_dir, f"Checking format in {scripts_dir}"):
        all_passed = False

    return all_passed


def lint_snippets_py_directory() -> bool:
    """Lint all Python files in the snippets_py directory."""
    snippets_py_dir = "snippets_py"
    if not os.path.exists(snippets_py_dir):
        print(f"⚠️  {snippets_py_dir} directory not found (skipping)")
        return True  # Not an error if directory doesn't exist

    python_files = get_python_files(snippets_py_dir)
    if not python_files:
        print(f"⚠️  No Python files found in {snippets_py_dir}")
        return True

    print(f"📁 Found {len(python_files)} Python files in {snippets_py_dir}")

    all_passed = True

    # Check each file individually
    for file_path in python_files:
        file_name = os.path.basename(file_path)
        if not run_ruff_check(file_path, f"Linting {file_name}"):
            all_passed = False

    # Check formatting for all files
    if not run_ruff_format_check(snippets_py_dir, f"Checking format in {snippets_py_dir}"):
        all_passed = False

    return all_passed


def generate_lint_report() -> Dict[str, Any]:
    """Generate a comprehensive lint report."""
    report = {
        "ruff_config": check_ruff_config(),
        "scripts": lint_scripts_directory(),
        "snippets_py": lint_snippets_py_directory(),
        "overall_success": True,
    }

    # Determine overall success
    if not all([report["ruff_config"], report["scripts"], report["snippets_py"]]):
        report["overall_success"] = False

    return report


def main():
    """Main linting function."""
    print("🧹 Running comprehensive ruff linting...\n")

    # Check if ruff is available
    try:
        subprocess.run(["ruff", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("❌ ruff is not installed or not available in PATH")
        print("   Install with: pip install ruff")
        sys.exit(1)

    # Generate and display report
    report = generate_lint_report()

    print("\n" + "=" * 50)
    print("📊 LINTING REPORT")
    print("=" * 50)

    print(f"🔧 Ruff Configuration: {'✅ PASS' if report['ruff_config'] else '❌ FAIL'}")
    print(f"📁 Scripts Directory: {'✅ PASS' if report['scripts'] else '❌ FAIL'}")
    print(f"📁 Snippets PY Directory: {'✅ PASS' if report['snippets_py'] else '❌ FAIL'}")

    print("\n" + "=" * 50)
    if report["overall_success"]:
        print("🎉 All linting checks passed!")
        sys.exit(0)
    else:
        print("❌ Some linting checks failed. Please fix the issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()

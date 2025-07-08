#!/usr/bin/env python3
"""
test_exported_snippets.py
-------------------------
Tests that exported Python snippets can be imported and executed without errors.
"""

import os
import sys
import importlib.util
import subprocess

SNIPPETS_PY_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets_py")


def get_all_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if fname.endswith(".py"):
                py_files.append(os.path.join(root, fname))
    return py_files


def test_import_snippets():
    """Test that all exported snippet files can be imported."""
    print("Testing snippet imports...")

    failed_imports = []

    for file_path in get_all_py_files(SNIPPETS_PY_DIR):
        fname = os.path.relpath(file_path, SNIPPETS_PY_DIR)
        try:
            # Load the module
            mod_name = fname.replace(os.sep, ".")[:-3]
            spec = importlib.util.spec_from_file_location(mod_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"✅ {fname} imports successfully")
        except Exception as e:
            failed_imports.append((fname, str(e)))
            print(f"❌ {fname} failed to import: {e}")

    return failed_imports


def test_snippet_execution():
    """Test that snippets can be executed in isolation."""
    print("\nTesting snippet execution...")

    failed_executions = []

    for file_path in get_all_py_files(SNIPPETS_PY_DIR):
        fname = os.path.relpath(file_path, SNIPPETS_PY_DIR)
        try:
            # Execute the file
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True,
                timeout=30,  # 30 second timeout
            )

            if result.returncode == 0:
                print(f"✅ {fname} executes successfully")
            else:
                failed_executions.append((fname, result.stderr))
                print(f"❌ {fname} failed to execute: {result.stderr}")

        except subprocess.TimeoutExpired:
            failed_executions.append((fname, "Execution timed out"))
            print(f"⏰ {fname} execution timed out")
        except Exception as e:
            failed_executions.append((fname, str(e)))
            print(f"❌ {fname} execution error: {e}")

    return failed_executions


def test_syntax():
    """Test that all exported files have valid Python syntax."""
    print("\nTesting Python syntax...")

    syntax_errors = []

    for file_path in get_all_py_files(SNIPPETS_PY_DIR):
        fname = os.path.relpath(file_path, SNIPPETS_PY_DIR)
        try:
            result = subprocess.run(
                [sys.executable, "-m", "py_compile", file_path], capture_output=True, text=True
            )

            if result.returncode == 0:
                print(f"✅ {fname} has valid syntax")
            else:
                syntax_errors.append((fname, result.stderr))
                print(f"❌ {fname} has syntax errors: {result.stderr}")

        except Exception as e:
            syntax_errors.append((fname, str(e)))
            print(f"❌ {fname} syntax check error: {e}")

    return syntax_errors


def main():
    """Main test function."""
    print("🧪 Testing exported snippets...\n")

    # Test imports
    failed_imports = test_import_snippets()

    # Test execution
    failed_executions = test_snippet_execution()

    # Test syntax
    syntax_errors = test_syntax()

    # Summary
    print("\n📊 Test Summary:")
    print(f"  - Import failures: {len(failed_imports)}")
    print(f"  - Execution failures: {len(failed_executions)}")
    print(f"  - Syntax errors: {len(syntax_errors)}")

    total_errors = len(failed_imports) + len(failed_executions) + len(syntax_errors)

    if total_errors == 0:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print(f"\n❌ {total_errors} test(s) failed. Please fix the issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()

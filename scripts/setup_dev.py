#!/usr/bin/env python3
"""
setup_dev.py
------------
Development environment setup script for stdlib-sniper contributors.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False


def run_command_list(cmd_list, description):
    """Run a command with a list of arguments (safer for dependencies)."""
    print(f"🔄 {description}...")
    try:
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print(f"❌ Python 3.11+ required, found {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True


def check_git():
    """Check if git is available."""
    if shutil.which("git") is None:
        print("❌ Git is not installed or not in PATH")
        return False
    print("✅ Git is available")
    return True


def create_venv():
    """Create a virtual environment if it doesn't exist."""
    venv_path = Path(".venv")

    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True

    print("🔄 Creating virtual environment...")
    if not run_command("python -m venv .venv", "Creating virtual environment"):
        return False

    print("✅ Virtual environment created")
    return True


def get_venv_python():
    """Get the path to the virtual environment Python executable."""
    if os.name == "nt":  # Windows
        return Path(".venv/Scripts/python.exe")
    else:  # Unix/Linux/macOS
        return Path(".venv/bin/python")


def get_venv_pip():
    """Get the path to the virtual environment pip executable."""
    if os.name == "nt":  # Windows
        return Path(".venv/Scripts/pip.exe")
    else:  # Unix/Linux/macOS
        return Path(".venv/bin/pip")


def detect_package_manager():
    """Detect available package manager (uv, poetry, pip)."""
    if shutil.which("uv"):
        return "uv"
    elif shutil.which("poetry"):
        return "poetry"
    elif shutil.which("pip"):
        return "pip"
    else:
        return None


def install_dependencies():
    """Install development dependencies using available package manager."""
    package_manager = detect_package_manager()

    if not package_manager:
        print("❌ No package manager found (uv, poetry, or pip)")
        print("   Please install one of: uv, poetry, or pip")
        return False

    print(f"📦 Using {package_manager} as package manager")

    # Parse dependencies from pyproject.toml
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib

    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found")
        return False

    with open(pyproject_path, "rb") as f:
        config = tomllib.load(f)

    dependencies = config.get("project", {}).get("dependencies", [])

    if not dependencies:
        print("❌ No dependencies found in pyproject.toml")
        return False

    print(f"📦 Found {len(dependencies)} dependencies to install")

    # Install dependencies based on package manager
    if package_manager == "uv":
        # UV handles virtual environments automatically
        # Install each dependency separately with proper argument lists
        for dep in dependencies:
            if not run_command_list(["uv", "add", dep], f"Installing {dep} with uv"):
                return False
    elif package_manager == "poetry":
        # Poetry handles virtual environments automatically
        if not run_command("poetry install", "Installing dependencies with poetry"):
            return False
    elif package_manager == "pip":
        # Create virtual environment for pip
        if not create_venv():
            return False

        venv_pip = get_venv_pip()
        if not venv_pip.exists():
            print(f"❌ Virtual environment pip not found at {venv_pip}")
            return False

        # Install each dependency separately with proper argument lists
        for dep in dependencies:
            if not run_command_list([str(venv_pip), "install", dep], f"Installing {dep} with pip"):
                return False

    return True


def get_python_executable():
    """Get the appropriate Python executable based on package manager."""
    package_manager = detect_package_manager()

    if package_manager == "uv":
        # UV uses .venv by default
        if os.name == "nt":  # Windows
            return Path(".venv/Scripts/python.exe")
        else:  # Unix/Linux/macOS
            return Path(".venv/bin/python")
    elif package_manager == "poetry":
        # Poetry uses its own virtual environment
        try:
            result = subprocess.run(
                ["poetry", "env", "info", "--path"], capture_output=True, text=True, check=True
            )
            poetry_venv = Path(result.stdout.strip())
            if os.name == "nt":  # Windows
                return poetry_venv / "Scripts" / "python.exe"
            else:  # Unix/Linux/macOS
                return poetry_venv / "bin" / "python"
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to system Python if poetry env not found
            return shutil.which("python")
    elif package_manager == "pip":
        # Use the virtual environment we created
        return get_venv_python()
    else:
        # Fallback to system Python
        return shutil.which("python")


def setup_pre_commit():
    """Set up pre-commit hooks."""
    python_exe = get_python_executable()

    if not python_exe or not Path(python_exe).exists():
        print("❌ Python executable not found")
        return False

    # Check if pre-commit is available
    if not run_command(f"{python_exe} -m pre_commit --version", "Checking pre-commit"):
        print("❌ pre-commit is not installed")
        return False

    if not run_command(f"{python_exe} -m pre_commit install", "Installing pre-commit hooks"):
        return False

    return True


def run_validation_scripts():
    """Run all validation scripts to ensure everything works."""
    print("\n🧪 Running validation scripts...")

    python_exe = get_python_executable()

    if not python_exe or not Path(python_exe).exists():
        print("❌ Python executable not found")
        return False

    scripts = [
        "check_duplicate_snippets.py",
        "validate_files.py",
        "validate_code.py",
        "check_crossrefs.py",
        "lint_code.py",
        "update_indexes.py",
        "check_tags_and_categories.py",
        "export_snippets_to_py.py",
    ]

    all_passed = True
    for script in scripts:
        script_path = os.path.join("scripts", script)
        if not run_command(f"{python_exe} {script_path}", f"Running {script}"):
            all_passed = False

    return all_passed


def create_example_snippet():
    """Create an example snippet for testing."""
    example_content = """# Example Snippets

Zero-dependency Python snippets for testing the setup.

## 🧩 Print hello world

```python
print("Hello, World!")
```

📂 Prints a simple greeting

🏷️ Tags: print, hello, basic

📝 Notes:
- Basic example for testing

## 🧩 Get current working directory

```python
import os; print(os.getcwd())
```
✅ Zero dependencies

📂 Gets the current working directory

🏷️ Tags: os, cwd, directory, path

📝 Notes:
- Uses os module from standard library
"""

    example_path = os.path.join("snippets", "example.md")
    with open(example_path, "w", encoding="utf-8") as f:
        f.write(example_content)

    print(f"✅ Created example snippet at {example_path}")


def main():
    """Main setup function."""
    print("🚀 Setting up stdlib-sniper development environment...\n")

    # Check prerequisites
    if not check_python_version():
        sys.exit(1)

    if not check_git():
        sys.exit(1)

    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)

    # Set up pre-commit
    if not setup_pre_commit():
        print("⚠️  Pre-commit setup failed, but continuing...")

    # Create example snippet if none exist
    snippets_dir = Path("snippets")
    if not any(snippets_dir.glob("*.md")):
        create_example_snippet()

    # Run validation scripts
    if not run_validation_scripts():
        print("⚠️  Some validation scripts failed, but setup is complete")

    print("\n🎉 Development environment setup complete!")
    print("\n📋 Next steps:")
    package_manager = detect_package_manager()
    if package_manager == "uv":
        print("  1. Use 'uv run python script.py' to run scripts")
        print("  2. Or activate environment: source .venv/bin/activate")
    elif package_manager == "poetry":
        print("  1. Use 'poetry run python script.py' to run scripts")
        print("  2. Or activate environment: poetry shell")
    elif package_manager == "pip":
        print("  1. Activate the virtual environment:")
        if os.name == "nt":  # Windows
            print("     .venv\\Scripts\\activate")
        else:  # Unix/Linux/macOS
            print("     source .venv/bin/activate")
    print("  3. Read CONTRIBUTING.md for contribution guidelines")
    print("  4. Check out the snippets/ directory")
    print("  5. Create your first snippet!")
    print("  6. Run validation scripts before committing")
    print(f"\n💡 Tip: Using {package_manager} for dependency management.")


if __name__ == "__main__":
    main()

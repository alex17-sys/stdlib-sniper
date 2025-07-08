#!/usr/bin/env python3
"""
Analyze current snippet coverage and identify gaps.
"""

import os
import re
from collections import defaultdict

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")

# Common Python stdlib modules and their typical use cases
STDLIB_MODULES = {
    # Data Structures & Algorithms
    "collections": ["defaultdict", "Counter", "deque", "namedtuple", "OrderedDict"],
    "heapq": ["heapify", "heappush", "heappop", "nlargest", "nsmallest"],
    "bisect": ["bisect_left", "bisect_right", "insort_left", "insort_right"],
    "array": ["array creation", "array operations"],
    # Text Processing
    "re": ["pattern matching", "substitution", "splitting", "flags"],
    "difflib": ["sequence matching", "unified diff", "context diff"],
    "textwrap": ["text wrapping", "dedent", "fill"],
    # Data Serialization & Formats
    "pickle": ["serialization", "deserialization"],
    "shelve": ["persistent dictionary"],
    "sqlite3": ["database operations"],
    "csv": ["CSV reading/writing"],  # We have some
    "json": ["JSON parsing"],  # We have some
    "xml": ["XML parsing"],  # We have some
    # Mathematics & Statistics
    "math": ["mathematical functions"],  # We have some
    "statistics": ["mean", "median", "mode", "variance", "stdev"],
    "random": ["random numbers"],  # We have some
    "decimal": ["decimal arithmetic"],
    "fractions": ["fraction arithmetic"],
    # File & Path Operations
    "pathlib": ["path operations"],  # We have some
    "glob": ["file pattern matching"],
    "fnmatch": ["filename matching"],
    "shutil": ["file operations"],  # We have some
    "zipfile": ["ZIP archives"],  # We have some
    "tarfile": ["TAR archives"],  # We have some
    "gzip": ["GZIP compression"],  # We have some
    "bz2": ["BZ2 compression"],  # We have some
    "lzma": ["LZMA compression"],  # We have some
    # System & OS
    "os": ["operating system"],  # We have some
    "sys": ["system parameters"],  # We have some
    "platform": ["platform info"],  # We have some
    "psutil": ["process and system utilities"],  # Not stdlib but common
    # Networking
    "socket": ["low-level networking"],  # We have some
    "urllib": ["URL handling"],  # We have some
    "http": ["HTTP"],  # We have some
    "email": ["email parsing"],
    "smtplib": ["SMTP client"],
    "poplib": ["POP3 client"],
    "imaplib": ["IMAP client"],
    # Concurrency
    "threading": ["threading"],  # We have some
    "multiprocessing": ["multiprocessing"],
    "asyncio": ["asynchronous I/O"],
    "concurrent.futures": ["thread/process pools"],
    # Data Processing
    "itertools": ["iterators"],  # We have some
    "functools": ["function tools"],  # We have some
    "operator": ["operators as functions"],
    # Configuration & Environment
    "configparser": ["INI files"],  # We have some
    "argparse": ["command line"],  # We have some
    # Debugging & Introspection
    "inspect": ["introspection"],  # We have some
    "traceback": ["stack traces"],  # We have some
    "pdb": ["debugger"],
    # Time & Date
    "datetime": ["date/time"],  # We have some
    "time": ["time functions"],  # We have some
    "calendar": ["calendar"],  # We have some
    # Security & Cryptography
    "hashlib": ["hashing"],  # We have some
    "hmac": ["HMAC"],  # We have some
    "secrets": ["cryptographic secrets"],  # We have some
    "ssl": ["SSL/TLS"],  # We have some
    "cryptography": ["cryptography"],  # Not stdlib but common
    # Other Common Modules
    "weakref": ["weak references"],
    "abc": ["abstract base classes"],
    "enum": ["enumerations"],
    "dataclasses": ["data classes"],
    "typing": ["type hints"],
    "contextlib": ["context managers"],  # We have some
    "tempfile": ["temporary files"],  # We have some
    "logging": ["logging"],  # We have some
    "warnings": ["warnings"],
    "unittest": ["unit testing"],
    "doctest": ["documentation testing"],
}


def get_current_coverage():
    """Analyze current snippet coverage."""
    coverage = defaultdict(list)

    # Read all snippet files
    for root, dirs, files in os.walk(SNIPPETS_DIR):
        for fname in files:
            if not fname.endswith(".md") or fname in [
                "INDEX.md",
                "TAG_SUMMARY.md",
                "CATEGORY_SUMMARY.md",
            ]:
                continue
            path = os.path.join(root, fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract code blocks and analyze imports
            code_blocks = re.findall(r"```python\n(.*?)```", content, re.DOTALL)
            for code in code_blocks:
                # Find import statements
                imports = re.findall(r"^(?:from\s+(\w+)|import\s+(\w+))", code, re.MULTILINE)
                for from_mod, import_mod in imports:
                    module = from_mod or import_mod
                    if module in STDLIB_MODULES:
                        coverage[module].append(f"{fname}: {code[:50]}...")

    return coverage


def identify_gaps():
    """Identify missing high-value snippets."""
    coverage = get_current_coverage()

    print("=== CURRENT COVERAGE ANALYSIS ===\n")

    # Show what we have
    print("✅ COVERED MODULES:")
    for module, examples in coverage.items():
        print(f"  {module}: {len(examples)} snippets")

    print("\n❌ MISSING HIGH-VALUE MODULES:")
    missing_high_value = [
        "collections",
        "heapq",
        "bisect",
        "array",  # Data structures
        "re",
        "difflib",
        "textwrap",  # Text processing
        "statistics",
        "decimal",
        "fractions",  # Math
        "glob",
        "fnmatch",  # File patterns
        "email",
        "smtplib",  # Email
        "multiprocessing",
        "asyncio",
        "concurrent.futures",  # Concurrency
        "operator",  # Operators
        "weakref",
        "abc",
        "enum",
        "dataclasses",  # Advanced Python
        "warnings",
        "unittest",
        "doctest",  # Testing & debugging
    ]

    for module in missing_high_value:
        if module not in coverage:
            print(f"  {module}: {', '.join(STDLIB_MODULES[module])}")

    print("\n📊 COVERAGE STATS:")
    total_modules = len(STDLIB_MODULES)
    covered_modules = len(coverage)
    print(f"  Total stdlib modules analyzed: {total_modules}")
    print(f"  Currently covered: {covered_modules}")
    print(f"  Coverage: {covered_modules / total_modules * 100:.1f}%")

    return coverage


def suggest_priority_snippets():
    """Suggest high-priority snippets to add."""
    print("\n=== HIGH-PRIORITY SNIPPET SUGGESTIONS ===\n")

    priority_snippets = [
        # Data Structures (Most commonly needed)
        ("collections", "Counter", "Count occurrences of items in a list"),
        ("collections", "defaultdict", "Create a dictionary with default values"),
        ("collections", "deque", "Efficient double-ended queue"),
        ("heapq", "heapify", "Convert list to heap in-place"),
        ("heapq", "nlargest", "Find N largest items"),
        ("bisect", "bisect_left", "Find insertion point in sorted list"),
        # Text Processing (Very common)
        ("re", "pattern_matching", "Basic regex pattern matching"),
        ("re", "substitution", "Replace text with regex"),
        ("difflib", "sequence_matcher", "Compare sequences"),
        ("textwrap", "wrap", "Wrap text to specified width"),
        # Math & Statistics (Practical)
        ("statistics", "mean", "Calculate arithmetic mean"),
        ("statistics", "median", "Calculate median"),
        ("decimal", "decimal_arithmetic", "Precise decimal arithmetic"),
        # File Operations (Common patterns)
        ("glob", "pattern_matching", "Find files by pattern"),
        ("fnmatch", "filename_matching", "Match filenames with patterns"),
        # Concurrency (Modern Python)
        ("multiprocessing", "process_pool", "Use process pool for CPU-bound tasks"),
        ("asyncio", "async_function", "Define and run async function"),
        ("concurrent.futures", "thread_pool", "Use thread pool for I/O-bound tasks"),
        # Advanced Python Features
        ("enum", "enumeration", "Create enumeration class"),
        ("dataclasses", "dataclass", "Create data class"),
        ("operator", "itemgetter", "Get item from sequence"),
        ("weakref", "weak_reference", "Create weak reference"),
        # Testing & Debugging
        ("unittest", "basic_test", "Write basic unit test"),
        ("doctest", "docstring_test", "Write test in docstring"),
        ("warnings", "suppress_warnings", "Suppress specific warnings"),
    ]

    print("🔥 TOP PRIORITY (Most commonly needed):")
    for i, (module, feature, description) in enumerate(priority_snippets[:10], 1):
        print(f"  {i}. {module}.{feature} - {description}")

    print("\n📈 MEDIUM PRIORITY (Very useful):")
    for i, (module, feature, description) in enumerate(priority_snippets[10:20], 11):
        print(f"  {i}. {module}.{feature} - {description}")

    print("\n💡 NICE TO HAVE (Advanced features):")
    for i, (module, feature, description) in enumerate(priority_snippets[20:], 21):
        print(f"  {i}. {module}.{feature} - {description}")


def create_community_suggestion_system():
    """Create a system for collecting community suggestions."""
    print("\n=== COMMUNITY SUGGESTION SYSTEM ===\n")

    suggestion_template = """### 🧩 {SNIPPET_TITLE}

```python
{CODE_SNIPPET}
```

📂 {DESCRIPTION}

🏷️ Tags: {TAGS}

📝 Notes:
- {NOTES}
"""

    print("📋 SUGGESTION TEMPLATE:")
    print(suggestion_template)

    print("🎯 HOW TO COLLECT SUGGESTIONS:")
    print("1. Create GitHub issues with 'suggestion' label")
    print("2. Add to README.md: 'Want to suggest a snippet? Open an issue!'")
    print("3. Create CONTRIBUTING.md with snippet guidelines")
    print("4. Set up GitHub Discussions for community input")
    print("5. Create a 'wanted-snippets.md' file with high-priority gaps")

    # Dynamically generate wanted snippets based on missing coverage
    coverage = get_current_coverage()
    covered_modules = set(coverage.keys())

    priority_snippets = [
        ("collections", "Counter", "Count occurrences of items in a list"),
        ("collections", "defaultdict", "Create a dictionary with default values"),
        ("collections", "deque", "Efficient double-ended queue"),
        ("heapq", "heapify", "Convert list to heap in-place"),
        ("heapq", "nlargest", "Find N largest items"),
        ("bisect", "bisect_left", "Find insertion point in sorted list"),
        ("re", "pattern_matching", "Basic regex pattern matching"),
        ("re", "substitution", "Replace text with regex"),
        ("difflib", "sequence_matcher", "Compare sequences"),
        ("textwrap", "wrap", "Wrap text to specified width"),
        ("statistics", "mean", "Calculate arithmetic mean"),
        ("statistics", "median", "Calculate median"),
        ("decimal", "decimal_arithmetic", "Precise decimal arithmetic"),
        ("glob", "pattern_matching", "Find files by pattern"),
        ("fnmatch", "filename_matching", "Match filenames with patterns"),
        ("multiprocessing", "process_pool", "Use process pool for CPU-bound tasks"),
        ("asyncio", "async_function", "Define and run async function"),
        ("concurrent.futures", "thread_pool", "Use thread pool for I/O-bound tasks"),
        ("enum", "enumeration", "Create enumeration class"),
        ("dataclasses", "dataclass", "Create data class"),
        ("operator", "itemgetter", "Get item from sequence"),
        ("weakref", "weak_reference", "Create weak reference"),
        ("unittest", "basic_test", "Write basic unit test"),
        ("doctest", "docstring_test", "Write test in docstring"),
        ("warnings", "suppress_warnings", "Suppress specific warnings"),
    ]

    # Group by priority for output
    high_priority = priority_snippets[:10]
    medium_priority = priority_snippets[10:20]
    nice_to_have = priority_snippets[20:]

    def filter_missing(snippets):
        return [s for s in snippets if s[0] not in covered_modules]

    wanted_snippets = "# Wanted Snippets\n\nThis file tracks high-priority snippets we'd like to add. Feel free to contribute!\n\n"

    if filter_missing(high_priority):
        wanted_snippets += "## 🔥 High Priority\n\n"
        for module, feature, desc in filter_missing(high_priority):
            wanted_snippets += f"- [ ] `{module}.{feature}` - {desc}\n"

    if filter_missing(medium_priority):
        wanted_snippets += "\n## 📈 Medium Priority\n\n"
        for module, feature, desc in filter_missing(medium_priority):
            wanted_snippets += f"- [ ] `{module}.{feature}` - {desc}\n"

    if filter_missing(nice_to_have):
        wanted_snippets += "\n## 💡 Nice to Have\n\n"
        for module, feature, desc in filter_missing(nice_to_have):
            wanted_snippets += f"- [ ] `{module}.{feature}` - {desc}\n"

    wanted_snippets += "\n## 🤝 Contributing\n\nTo contribute a snippet:\n1. Check if it's already in the list above\n2. Follow the snippet template in CONTRIBUTING.md\n3. Submit a pull request\n4. Ensure it uses only the standard library\n5. Include clear tags and notes\n"

    # Progress
    total_wanted = len(filter_missing(priority_snippets))
    wanted_snippets += f"\n## 📊 Progress\n\n- Total wanted: {total_wanted}\n"

    with open("WANTED_SNIPPETS.md", "w") as f:
        f.write(wanted_snippets)

    print("\n✅ Created WANTED_SNIPPETS.md with dynamic priority list")


if __name__ == "__main__":
    coverage = identify_gaps()
    suggest_priority_snippets()
    create_community_suggestion_system()

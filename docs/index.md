# stdlib-sniper

[![stdlib-sniper](https://img.shields.io/badge/stdlib--sniper-blue)](https://github.com/heyshinde/stdlib-sniper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Snippets](https://img.shields.io/badge/snippets-3+-orange.svg)](https://github.com/heyshinde/stdlib-sniper/tree/main/snippets)
[![CI](https://github.com/heyshinde/stdlib-sniper/actions/workflows/ci.yml/badge.svg)](https://github.com/heyshinde/stdlib-sniper/actions/workflows/ci.yml)
[![Docs](https://github.com/heyshinde/stdlib-sniper/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/heyshinde/stdlib-sniper/actions/workflows/deploy-docs.yml)

> One-shot Python solutions. No pip. No problem.

---

## 🚀 What is stdlib-sniper?

**stdlib-sniper** is a curated collection of zero-dependency, standard library Python snippets for real-world tasks. Every snippet is:
- **Copy-paste ready**: Use directly in your scripts or REPL.
- **Importable**: Auto-exported as Python files for direct import.
- **Well-documented**: Rich tagging, notes, and cross-references.
- **Strictly stdlib-only**: No third-party packages, ever.

---

## 📁 Project Structure

- `snippets/` — All snippets in Markdown, organized by category and subcategory.
- `snippets_py/` — Auto-exported Python files, ready to import or run.
- `docs/` — Generated documentation for browsing/searching (MkDocs Material theme).
- `scripts/` — Automation, validation, and export tools for contributors and CI.

---

## 🧩 Snippet Template

```markdown
### 🧩 Snippet Title

# ```python (Uncomment the code block)
# Your code here
# ```

📂 Short description of what the snippet does

🏷️ Tags: tag1, tag2, ...

📝 Notes:
- Note 1
- Note 2
```

## 🔗 Cross-Reference Template

```markdown
## 🔗 Cross-References

- **Reference**: See [📂 Wanted Snippets](./WANTED_SNIPPETS.md)
```

---

## 👨🏻‍💻 How to Use

- **Browse**: Explore `snippets/` or the [documentation site](https://heyshinde.github.io/stdlib-sniper) for categorized, searchable snippets.
- **Copy-paste**: Grab any snippet from Markdown or the docs and use it instantly.
- **Import**: Use auto-exported `.py` files from `snippets_py/` in your own projects:
  ```python
  from snippets_py.math import gcd_lcm_demo
  gcd_lcm_demo.some_function()
  ```
- **See examples**: Real-world usage in the `examples/` folder (if present).

---

## 🤖 Automation & Scripts

- `scripts/update_indexes.py` — Updates all snippet indexes and summaries.
- `scripts/generate_docs.py` — Builds the documentation site (MkDocs).
- `scripts/check_duplicate_snippets.py` — Checks for duplicate code blocks and section headers.
- `scripts/export_snippets_to_py.py` — Exports Markdown snippets to Python files.
- `scripts/analyze_coverage.py` — Analyzes stdlib coverage and suggests wanted snippets.
- `scripts/run_all_checks.py` — Runs all checks for CI/dev.
- `scripts/validate_files.py`, `lint_md_snippets.py`, etc. — Additional quality and linting tools.

**To run all checks before contributing:**
```sh
python scripts/run_all_checks.py
```

---

## 📝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for full guidelines, the snippet template, and the review checklist.

- Add new snippets using the template above.
- Use only the Python standard library (no pip installs).
- Add clear tags, notes, and cross-references.
- Run all checks and scripts before submitting a PR.
- Suggest new snippets via issues or add to `WANTED_SNIPPETS.md`.

---

## 📊 Snippet Categories

<!-- SNIPPET_CATEGORIES_START -->


- Data Structures Snippets: 377
    - Lists: 149
    - Dictionaries: 108
    - Trees: 29
    - Graphs: 27
    - Sets: 25
    - Tuples: 17
    - Heaps: 11
    - Queues Stacks: 11
- Math Snippets: 249
- Strings Snippets: 228
- Files Snippets: 100

<!-- SNIPPET_CATEGORIES_END -->

---

## 📄 License

MIT License. See [LICENSE](LICENSE).

---

## 🤝 Community & Support

- **Questions?** Open an issue or join the discussion on GitHub.
- **Want to suggest a snippet?** Open an issue with the `suggestion` label or add to `WANTED_SNIPPETS.md`.
- **See also:** [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

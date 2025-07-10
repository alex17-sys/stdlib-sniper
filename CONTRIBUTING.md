# Contributing to stdlib-sniper

Thank you for your interest in contributing to **stdlib-sniper**! We welcome all contributions that help make Python’s standard library more accessible and practical for everyone.

---

## 🧩 How to Add a Snippet

1. **Copy the snippet template below.**
2. **Fill in all fields:**
   - Title (concise and descriptive)
   - Code (zero-dependency, stdlib-only)
   - Description (what does it do?)
   - Tags (comma-separated, e.g. `files, append, write`)
   - Notes (usage tips, edge cases, warnings)
3. **Add cross-references** if your snippet relates to others.
4. **Place your snippet** in the correct category folder in `snippets/` (e.g., `snippets/math/`, `snippets/strings/`).
5. **Run all checks and scripts** before submitting a PR (see below).

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

### 🔗 Cross-Reference Template (Optional)

```markdown
## 🔗 Cross-References

- **Reference**: See [📂 Wanted Snippets](./WANTED_SNIPPETS.md)
```

---

## ✅ Review Checklist

Before submitting your PR, please ensure:

- [ ] **Stdlib only:** Uses only the Python standard library (no pip installs).
- [ ] **Follows the snippet template:** All fields are filled in.
- [ ] **Clear tags and notes:** Tags are relevant, notes are helpful.
- [ ] **No duplicate code or section headers:** Run the duplicate check script.
- [ ] **Passes all lint and validation scripts:** See below.
- [ ] **Cross-references added** (if relevant).
- [ ] **File is in the correct category folder.**

---

## 🛠️ Running Checks

Before you submit your PR, run the following:

```sh
python scripts/run_all_checks.py
```

This will:
- Lint all Markdown and Python files
- Check for duplicate code blocks and section headers
- Validate snippet formatting and tags
- Update indexes and summaries
- Export snippets to Python files

**Fix any issues reported by the scripts before submitting.**

---

## 💡 Suggest a Snippet

- **Open an issue** with the `suggestion` label.
- **Or add to `WANTED_SNIPPETS.md`** in the project root.
- **Or join the discussion** on GitHub Discussions.

---

## 📝 Docs & Automation

- **Docs are auto-generated** from `snippets/` using MkDocs Material.
- To build docs locally:
  ```sh
  python scripts/generate_docs.py
  mkdocs serve
  # Then open http://127.0.0.1:8000
  ```
- **Docs are auto-built in CI** on every push/PR.

---

## 🤝 Community & Support

- **Questions?** Open an issue or join the discussion on GitHub.
- **Want to suggest a snippet?** See above.

---

Thank you for helping make stdlib-sniper awesome!

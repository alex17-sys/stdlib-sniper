import os
import re
from collections import Counter, defaultdict
from difflib import get_close_matches

SNIPPETS_DIR = os.path.join(os.path.dirname(__file__), "..", "snippets")
CATEGORY_SUMMARY_PATH = os.path.join(SNIPPETS_DIR, "CATEGORY_SUMMARY.md")
SUMMARY_FILES = {"TAG_SUMMARY.md", "CATEGORY_SUMMARY.md", "INDEX.md"}


def get_snippet_files():
    """Recursively find all .md files in snippets, excluding summary/index files."""
    files = []
    for root, dirs, filenames in os.walk(SNIPPETS_DIR):
        for fname in filenames:
            if fname.endswith(".md") and fname not in SUMMARY_FILES:
                rel_path = os.path.relpath(os.path.join(root, fname), SNIPPETS_DIR)
                files.append(rel_path)
    return files


def extract_tags():
    tags = []
    tag_locations = defaultdict(list)
    for rel_path in get_snippet_files():
        path = os.path.join(SNIPPETS_DIR, rel_path)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract tags from snippet sections
        tag_lines = re.findall(r"🏷️ Tags: ?(?:\[([^\]]*)\]|(.*))", content)
        for i, (bracket_tags, plain_tags) in enumerate(tag_lines, 1):
            tag_str = bracket_tags or plain_tags
            for tag in tag_str.split(","):
                tag = tag.strip()
                if tag:
                    tags.append(tag)
                    tag_locations[tag].append((rel_path, i))

        # Extract tags from footer section
        footer_match = re.search(r"## 🏷️ Tags\s*\n([\s\S]+?)(?:\n## |\n# |\n$)", content)
        if footer_match:
            footer_block = footer_match.group(1).strip()
            for line in footer_block.splitlines():
                for tag in line.split(","):
                    tag = tag.strip().strip("`")  # Remove backticks if present
                    if tag:
                        tags.append(tag)
                        tag_locations[tag].append((rel_path, "footer"))

    return tags, tag_locations


def check_category_summary():
    """Check for categories with fewer than 3 snippets and suggest merging."""
    if not os.path.exists(CATEGORY_SUMMARY_PATH):
        print("[WARN] CATEGORY_SUMMARY.md not found. Run update_indexes.py first.")
        return

    with open(CATEGORY_SUMMARY_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    found = False
    for line in lines:
        # Match both main categories and subcategories
        m = re.match(r"- (.+?): (\d+)", line)
        if m:
            cat, count = m.group(1), int(m.group(2))
            if count < 3:
                print(
                    f"[SUGGEST] Category '{cat}' has only {count} snippets. Consider merging with a related category."
                )
                found = True

    if not found:
        print("All set for categories.")


def check_tags_and_categories():
    """Check tag normalization and category summary, print actionable suggestions only."""
    tags, tag_locations = extract_tags()
    counter = Counter(tags)
    tag_issue = False

    # Tag normalization checks
    for tag in counter:
        if tag != tag.strip():
            print(f"[WARN] Tag has leading/trailing spaces: '{tag}'")
            tag_issue = True
        if tag.lower() != tag and tag.upper() != tag:
            print(f"[WARN] Tag has mixed casing: '{tag}'")
            tag_issue = True

    # Smart "used once" check - only flag likely typos or inconsistencies
    for tag, count in counter.items():
        if count == 1:
            # Skip legitimate unique tags (specific algorithms, techniques, etc.)
            legitimate_unique = {
                "luhn",
                "attribute",
                "inorder",
                "postorder",
                "child",
                "eratosthenes",
                "cmp_to_key",
                "miller-rabin",
                "binet",
                "lucas",
                "tribonacci",
                "golden-ratio",
                "continued-fraction",
                "compound-interest",
                "half-life",
                "decay",
                "exponential",
                "logarithm",
                "ln",
                "log10",
                "log2",
                "natural-log",
                "change-of-base",
                "sqrt",
                "cbrt",
                "square-root",
                "cube-root",
                "nth-root",
                "perfect-square",
                "perfect-cube",
                "pythagoras",
                "pythagorean",
                "law-of-sines",
                "law-of-cosines",
                "double-angle",
                "half-angle",
                "sinc",
                "fourier",
                "taylor",
                "stirling",
                "subfactorial",
                "derangement",
                "bezout",
                "extended-euclidean",
                "modular-inverse",
                "stein",
                "prime-factorization",
                "rsa",
                "luhn",
                "cvv",
                "credit card",
                "expiration",
                "batch",
                "processing",
                "strength",
                "warnings",
                "randomness",
                "policy",
                "class",
                "reuse",
                "overlapping",
                "substrings",
                "breaks",
                "boundary",
                "directions",
                "trim",
                "lstrip",
                "rstrip",
                "sets",
                "sub",
                "classes",
                "string module",
                "comma",
                "splits",
                "delimiters",
                "first",
                "contractions",
                "hyphens",
                "suffixes",
                "filename",
                "decrease",
                "points",
                "education",
                "sales",
                "business",
                "number-theory",
                "divisibility",
                "next",
                "previous",
                "composite",
                "classification",
                "probabilistic",
                "factors",
                "exponents",
                "sieve",
                "twin",
                "mersenne",
                "research",
                "tolerance",
                "floating-point",
                "partition",
                "double-factorial",
                "falling",
                "rising",
                "derangement",
                "stirling",
                "combination",
                "probability",
                "binomial",
                "commas",
                "separators",
                "units",
                "visualization",
                "charts",
                "labels",
                "arbitrary",
                "config",
                "user-input",
                "natural-log",
                "change-of-base",
                "transformation",
                "information-theory",
                "kl-divergence",
                "mutual-information",
                "ph",
                "decibels",
                "magnitude",
                "earthquake",
                "cbrt",
                "cube-root",
                "general",
                "perfect-square",
                "perfect-cube",
                "pythagoras",
                "global",
                "quantize",
                "localcontext",
                "nth",
                "exponentiation",
                "binet",
                "lucas",
                "tribonacci",
                "spiral",
                "art",
                "nature",
                "algorithms",
                "ceil",
                "floor",
                "trunc",
                "significant-figures",
                "banker-rounding",
                "float-arithmetic",
                "intervals",
                "uncertainty",
                "variance",
                "stddev",
                "quantiles",
                "percentiles",
                "iqr",
                "skewness",
                "kurtosis",
                "covariance",
                "correlation",
                "z-score",
                "standardization",
                "moving-average",
                "rolling",
                "window",
                "outliers",
                "minmax",
                "regression",
                "linear",
                "prediction",
                "angles",
                "asin",
                "acos",
                "atan",
                "double-angle",
                "half-angle",
                "pythagorean",
                "triangles",
                "law-of-sines",
                "law-of-cosines",
                "sinc",
                "fourier",
                "projectile",
                "pendulum",
                "waves",
                "cube",
                "power-laws",
                "newton-raphson",
                "weighted-average",
                "overflow",
                "present-value",
                "inflation",
                "chemistry",
                "mean",
                "median",
                "weighted-mean",
                "harmonic-mean",
                "geometric-mean",
                "midrange",
                "counts",
                "summary",
                "report",
                "multiply",
                "3x3",
                "real",
                "imaginary",
                "conjugate",
                "abs",
                "polar",
                "rect",
                "log",
                "roots",
                "powers",
                "sinh",
                "cosh",
                "tanh",
                "impedance",
                "phasor",
                "simplify",
                "expand",
                "from-float",
                "from-decimal",
                "scaling",
                "dot",
                "cross",
                "angle",
                "project",
                "reject",
                "distance",
                "midpoint",
                "extended-euclidean",
                "bezout",
                "modular-inverse",
                "stein",
                "prime-factorization",
                "fractions",
                "rsa",
                "choice",
                "selection",
                "shuffle",
                "normal",
                "poisson",
                "seed",
                "reproducibility",
                "constraints",
                "boolean",
                "simulation",
                "monte-carlo",
                "modeling",
                "games",
                "dice",
                "cards",
                "lottery",
                "derivative",
                "finite-difference",
                "trapezoidal",
                "numerical",
                "higher-derivative",
                "simpson",
                "partial-derivative",
                "multivariate",
                "area",
                "velocity",
                "constraint",
                "negative",
                "unit",
                "increment",
                "snapping",
                "soft",
                "gradual",
                "animation",
                "rgb",
                "hsv",
                "graphics",
                "volume",
                "decibel",
                "and",
                "not",
                "left-shift",
                "right-shift",
                "toggle",
                "extract",
                "pack",
                "flags",
                "context-manager",
                "sha256",
                "splitlines",
                "details",
                "file-types",
                "islink",
                "stat",
                "atomic",
                "writelines",
                "numbering",
                "metadata",
                "progress",
                "decode",
                "logging",
                "status",
                "accessibility",
                "components",
                "encode",
                "data-types",
                "absolute",
                "paths",
                "cleanup",
                "manager",
                "atexit",
            }

            if tag not in legitimate_unique:
                print(
                    f"[WARN] Tag '{tag}' is only used once (in {tag_locations[tag][0][0]} snippet #{tag_locations[tag][0][1]}) - consider if this is a typo or should be merged"
                )
                tag_issue = True

    # Enhanced merging suggestions with categories
    tag_list = list(counter)
    similar_groups = []

    for i, tag1 in enumerate(tag_list):
        for tag2 in tag_list[i + 1 :]:
            if tag1.lower() != tag2.lower() and get_close_matches(tag1, [tag2], n=1, cutoff=0.85):
                # Categorize the similarity type
                similarity_type = "unknown"
                if tag1.lower() == tag2.lower():
                    similarity_type = "case-difference"
                elif tag1.replace("-", "") == tag2.replace("-", ""):
                    similarity_type = "hyphenation-difference"
                elif tag1.endswith("s") and tag1[:-1] == tag2:
                    similarity_type = "singular-plural"
                elif tag2.endswith("s") and tag2[:-1] == tag1:
                    similarity_type = "singular-plural"
                elif tag1 in tag2 or tag2 in tag1:
                    similarity_type = "substring"

                similar_groups.append((tag1, tag2, similarity_type))

    # Group and report similar tags
    if similar_groups:
        print("\n[SUGGEST] Similar tags that could be merged:")
        by_type = defaultdict(list)
        for tag1, tag2, sim_type in similar_groups:
            by_type[sim_type].append((tag1, tag2))

        for sim_type, pairs in by_type.items():
            print(f"  {sim_type.upper()}:")
            for tag1, tag2 in pairs:
                count1, count2 = counter[tag1], counter[tag2]
                print(f"    '{tag1}' ({count1}) ↔ '{tag2}' ({count2})")
        tag_issue = True

    if not tag_issue:
        print("All set for tags.")


if __name__ == "__main__":
    # Entry point for CLI usage
    print("\nTags summary checks:")
    check_tags_and_categories()
    print("\nCategory summary checks:")
    check_category_summary()

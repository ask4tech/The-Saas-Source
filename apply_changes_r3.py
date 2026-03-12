#!/usr/bin/env python3
"""
The SaaS Source — Round 3 Modifications
========================================
  1. Comparison prose spans full width (both columns)
  2. Copyright year 2025 → 2026 in all files
  3. Header logo image height → 50px, nav height adjusted

Usage:
  cd /path/to/thesaassource
  python3 apply_changes_r3.py
"""

import os
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(REPO_ROOT, "css", "styles.css")
BUILD_FILE = os.path.join(REPO_ROOT, "build.py")
HTML_FILES = glob.glob(os.path.join(REPO_ROOT, "*.html"))
ALL_TEXT_FILES = HTML_FILES + [BUILD_FILE]

changes = []


def read(fp):
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()


def write(fp, content):
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════════════
# CHANGE 1: Comparison prose spans full width
# ═══════════════════════════════════════════════════
# The .detail-content grid is 1fr 280px. The .prose div
# sits in the first column. We add a CSS rule to make
# .prose inside .detail-content span both columns, and
# remove the max-width constraint so it fills the space.

def fix_comparison_layout(css):
    original = css

    # Add a rule after .detail-sticky to make .prose span full width
    css = css.replace(
        ".detail-sticky { position: sticky; top: 80px; }",
        """.detail-sticky { position: sticky; top: 80px; }
.detail-content > .prose {
  grid-column: 1 / -1;
  max-width: none;
}"""
    )

    if css != original:
        changes.append("  [LAYOUT] css/styles.css — .prose spans full width in .detail-content")
    return css


# ═══════════════════════════════════════════════════
# CHANGE 2: Copyright 2025 → 2026
# ═══════════════════════════════════════════════════

def fix_copyright(content, filepath):
    original = content
    content = content.replace("© 2025", "© 2026")
    if content != original:
        changes.append(f"  [COPYRIGHT] {os.path.basename(filepath)} — 2025 → 2026")
    return content


# ═══════════════════════════════════════════════════
# CHANGE 3: Header logo → 50px, nav height adjusted
# ═══════════════════════════════════════════════════

def fix_header_logo(css):
    original = css

    # .nav-logo img (generic rule)
    css = css.replace(
        ".nav-logo img { height: 36px; object-fit: contain; }",
        ".nav-logo img { height: 50px; object-fit: contain; }"
    )

    # .nav-logo-img (specific class from R1)
    css = css.replace(
        ".nav-logo-img { height: 36px; object-fit: contain; }",
        ".nav-logo-img { height: 50px; object-fit: contain; }"
    )

    # Increase nav height to accommodate larger logo
    css = css.replace(
        "  height: 68px;\n  gap: 0;\n  position: sticky;",
        "  height: 78px;\n  gap: 0;\n  position: sticky;"
    )

    # Also update the nav-link height to match
    css = css.replace(
        "  border-bottom: 2px solid transparent;\n  height: 68px;",
        "  border-bottom: 2px solid transparent;\n  height: 78px;"
    )

    if css != original:
        changes.append("  [HEADER] css/styles.css — logo 50px, nav height 78px")
    return css


# ═══════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("The SaaS Source — Round 3 Modifications")
    print("=" * 60)

    # CSS changes
    if os.path.exists(CSS_FILE):
        css = read(CSS_FILE)
        css = fix_comparison_layout(css)
        css = fix_header_logo(css)
        write(CSS_FILE, css)
        print(f"✓ {CSS_FILE}")

    # Copyright in all HTML + build.py
    for fp in ALL_TEXT_FILES:
        if os.path.exists(fp):
            content = read(fp)
            content = fix_copyright(content, fp)
            write(fp, content)
            print(f"✓ {fp}")

    print(f"\n{'=' * 60}")
    print(f"Done — {len(changes)} changes:")
    print("=" * 60)
    for c in changes:
        print(c)
    print()
    print('Commit: git add -A && git commit -m "R3: full-width comparison prose, copyright 2026, header logo 50px"')


if __name__ == "__main__":
    main()

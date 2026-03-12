#!/usr/bin/env python3
"""
The SaaS Source — Fix: Comparison prose full width
==================================================
The .prose div inside .detail-content is nested inside the first
grid column <div>, not a direct child of the grid. The previous
grid-column rule doesn't work. This fix removes the max-width
constraint on .prose when inside .detail-content so it fills
the full available width of its column.

Usage:
  cd /path/to/thesaassource
  python3 fix_prose_width.py
"""

import os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(REPO_ROOT, "css", "styles.css")


def read(fp):
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()


def write(fp, content):
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("Fixing comparison prose width...")

    css = read(CSS_FILE)

    # Remove the incorrect grid-column rule from R3
    css = css.replace(
        """.detail-sticky { position: sticky; top: 80px; }
.detail-content > .prose {
  grid-column: 1 / -1;
  max-width: none;
}""",
        """.detail-sticky { position: sticky; top: 80px; }
.detail-content .prose {
  max-width: none;
}"""
    )

    # If for some reason the R3 rule wasn't there, handle base .prose
    # by adding the override if not already present
    if ".detail-content .prose" not in css:
        css = css.replace(
            ".detail-sticky { position: sticky; top: 80px; }",
            """.detail-sticky { position: sticky; top: 80px; }
.detail-content .prose {
  max-width: none;
}"""
        )

    write(CSS_FILE, css)
    print("✓ Updated css/styles.css")
    print("  .detail-content .prose { max-width: none; }")
    print()
    print('Commit: git add -A && git commit -m "Fix: prose fills full column width in comparison layout"')


if __name__ == "__main__":
    main()

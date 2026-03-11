#!/usr/bin/env python3
"""
The SaaS Source — Apply Layout & Content Modifications
======================================================
Applies three changes across the entire codebase:
  1. Swap text logo → image logo (images/logo.png)
  2. Swap heading font Syne → Roboto (Google Fonts + CSS)
  3. Wrap hero content in .hero-inner container (max-width: 1920px, centered)

Usage:
  cd /path/to/thesaassource
  python3 apply_changes.py

Creates backups of each file before modifying.
"""

import os
import re
import shutil
import glob

# ─── CONFIGURATION ───
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# All HTML files to modify
HTML_FILES = glob.glob(os.path.join(REPO_ROOT, "*.html"))
BUILD_FILE = os.path.join(REPO_ROOT, "build.py")
CSS_FILE = os.path.join(REPO_ROOT, "css", "styles.css")
DEV_NOTES = os.path.join(REPO_ROOT, "DEVELOPER-NOTES.md")

ALL_FILES = HTML_FILES + [BUILD_FILE, CSS_FILE, DEV_NOTES]

changes_made = []


def backup(filepath):
    """Create a .bak backup of the file."""
    bak = filepath + ".bak"
    if not os.path.exists(bak):
        shutil.copy2(filepath, bak)


def read(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════════════
# CHANGE 1: Swap text logo → image logo
# ═══════════════════════════════════════════════════

def apply_logo_swap(content, filepath):
    """Replace the text-based nav logo with an <img> tag."""
    original = content

    # Pattern: <span class="nav-logo-text">The <span class="accent">SaaS</span> Source</span>
    # Replace with: <img src="images/logo.png" alt="The SaaS Source" class="nav-logo-img">
    content = content.replace(
        '<span class="nav-logo-text">The <span class="accent">SaaS</span> Source</span>',
        '<img src="images/logo.png" alt="The SaaS Source" class="nav-logo-img">'
    )

    # Also handle the footer logo text
    content = content.replace(
        '<div class="footer-logo">The <span class="accent">SaaS</span> Source</div>',
        '<div class="footer-logo"><img src="images/logo.png" alt="The SaaS Source" class="footer-logo-img"></div>'
    )

    if content != original:
        changes_made.append(f"  [LOGO] {os.path.basename(filepath)}")
    return content


def apply_logo_swap_buildpy(content):
    """Handle build.py string templates for logo swap."""
    original = content

    # Nav logo in build.py NAV function
    content = content.replace(
        """<span class="nav-logo-text">The <span class="accent">SaaS</span> Source</span>""",
        """<img src="images/logo.png" alt="The SaaS Source" class="nav-logo-img">"""
    )

    # Footer logo in build.py FOOTER string
    content = content.replace(
        """<div class="footer-logo">The <span class="accent">SaaS</span> Source</div>""",
        """<div class="footer-logo"><img src="images/logo.png" alt="The SaaS Source" class="footer-logo-img"></div>"""
    )

    if content != original:
        changes_made.append(f"  [LOGO] build.py")
    return content


def apply_logo_css(content):
    """Add .nav-logo-img and .footer-logo-img styles to CSS."""
    original = content

    # Add nav-logo-img style after existing .nav-logo img rule
    old_nav_logo_img = ".nav-logo img { height: 36px; object-fit: contain; }"
    new_nav_logo_img = """.nav-logo img { height: 36px; object-fit: contain; }
.nav-logo-img { height: 36px; object-fit: contain; }"""
    content = content.replace(old_nav_logo_img, new_nav_logo_img)

    # Add footer-logo-img style after .footer-brand .footer-logo block
    # Insert after the footer-logo closing brace
    old_footer = ".footer-brand .footer-logo .accent { color: var(--blue); }"
    new_footer = """.footer-brand .footer-logo .accent { color: var(--blue); }
.footer-logo-img { height: 24px; object-fit: contain; filter: brightness(1.3); }"""
    content = content.replace(old_footer, new_footer)

    if content != original:
        changes_made.append(f"  [LOGO] css/styles.css (added .nav-logo-img, .footer-logo-img)")
    return content


# ═══════════════════════════════════════════════════
# CHANGE 2: Swap Syne → Roboto heading font
# ═══════════════════════════════════════════════════

def apply_font_swap_html(content, filepath):
    """Replace Syne with Roboto in Google Fonts import URL."""
    original = content

    # Replace the Google Fonts import URL
    content = content.replace(
        "https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap",
        "https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap"
    )

    if content != original:
        changes_made.append(f"  [FONT] {os.path.basename(filepath)}")
    return content


def apply_font_swap_css(content):
    """Replace all font-family: 'Syne' references with 'Roboto' in CSS."""
    original = content

    content = content.replace("font-family: 'Syne', sans-serif;", "font-family: 'Roboto', sans-serif;")
    content = content.replace("font-family: 'Syne',sans-serif;", "font-family: 'Roboto',sans-serif;")
    content = content.replace("font-family:'Syne',sans-serif;", "font-family:'Roboto',sans-serif;")

    if content != original:
        changes_made.append(f"  [FONT] css/styles.css")
    return content


def apply_font_swap_devnotes(content):
    """Update DEVELOPER-NOTES.md typography reference."""
    original = content

    content = content.replace(
        "**Headings:** [Syne](https://fonts.google.com/specimen/Syne) (800, 700, 600)",
        "**Headings:** [Roboto](https://fonts.google.com/specimen/Roboto) (900, 700, 500)"
    )

    if content != original:
        changes_made.append(f"  [FONT] DEVELOPER-NOTES.md")
    return content


# ═══════════════════════════════════════════════════
# CHANGE 3: Hero inner container (max-width: 1920px)
# ═══════════════════════════════════════════════════

def apply_hero_inner_css(content):
    """Add .hero-inner utility class and restructure hero CSS for inner container."""
    original = content

    # Add the .hero-inner class right after the .hero rule block
    # We insert it after the hero::after pseudo-element
    hero_inner_css = """
/* Hero inner container — constrains content to 1920px centered */
.hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 420px;
  gap: 52px;
  align-items: center;
}"""

    # Replace .hero grid layout — move grid properties to .hero-inner
    content = content.replace(
        """.hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 55%, #E2EEF8 100%);
  padding: 72px 36px 60px;
  display: grid;
  grid-template-columns: 1fr 420px;
  gap: 52px;
  align-items: center;
  position: relative;
  overflow: hidden;
}""",
        """.hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 55%, #E2EEF8 100%);
  padding: 72px 36px 60px;
  position: relative;
  overflow: hidden;
}
.hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 420px;
  gap: 52px;
  align-items: center;
}"""
    )

    # Add .hero-inner for .cat-hero
    content = content.replace(
        """.cat-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 48px 36px 36px;
  border-bottom: 1px solid var(--gray-100);
}""",
        """.cat-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 48px 36px 36px;
  border-bottom: 1px solid var(--gray-100);
}
.cat-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}"""
    )

    # Add .hero-inner for .detail-hero
    content = content.replace(
        """.detail-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 48px 36px 40px;
  border-bottom: 1px solid var(--gray-100);
}""",
        """.detail-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 48px 36px 40px;
  border-bottom: 1px solid var(--gray-100);
}
.detail-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}"""
    )

    # Add .hero-inner for .page-hero
    content = content.replace(
        """.page-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 56px 36px 44px;
  border-bottom: 1px solid var(--gray-100);
}""",
        """.page-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 56px 36px 44px;
  border-bottom: 1px solid var(--gray-100);
}
.page-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}"""
    )

    # Update responsive breakpoint for .hero — update to target .hero > .hero-inner
    content = content.replace(
        ".hero { grid-template-columns: 1fr; padding: 48px 24px 36px; }",
        ".hero { padding: 48px 24px 36px; }\n  .hero > .hero-inner { grid-template-columns: 1fr; }"
    )

    if content != original:
        changes_made.append(f"  [HERO-INNER] css/styles.css")
    return content


def apply_hero_inner_html(content, filepath):
    """Wrap hero section content in .hero-inner div for each hero type."""
    original = content

    # ── Homepage hero: <section class="hero"> ... </section>
    # Wrap all children of .hero in .hero-inner
    content = re.sub(
        r'(<section class="hero">)\s*\n(\s*<div class="hero-left">)',
        r'\1\n  <div class="hero-inner">\n\2',
        content
    )
    # Close .hero-inner before </section> for homepage hero
    content = re.sub(
        r'(</div>\s*<!-- /hero-card -->)\s*\n(\s*</section>)',
        r'\1\n  </div><!-- /hero-inner -->\n\2',
        content
    )
    # Fallback: if no <!-- /hero-card --> comment, look for pattern after hero-card closing
    # This handles the case where hero section ends with the card div then section close
    if '<!-- /hero-inner -->' not in content and '<section class="hero">' in content:
        # Find the </section> that closes .hero and insert </div> before it
        content = re.sub(
            r'(  </div>\n)(</section><!-- /hero -->)',
            r'\1  </div><!-- /hero-inner -->\n\2',
            content
        )

    # ── Category hero: <div class="cat-hero">
    content = re.sub(
        r'(<div class="cat-hero">)\s*\n(\s*<div class="breadcrumb">)',
        r'\1\n  <div class="hero-inner">\n\2',
        content
    )
    # Close before </div> that ends .cat-hero
    content = re.sub(
        r'(</div>\s*<!-- cat-stats -->\s*\n)(</div>\s*\n\s*<!-- Filters)',
        r'\1  </div><!-- /hero-inner -->\n</div>\n\n<!-- Filters',
        content
    )
    # Simpler fallback for cat-hero closing
    if 'cat-hero' in content and '<!-- /hero-inner -->' not in content:
        # Try a broader pattern
        pass

    # ── Detail hero: <div class="detail-hero">  or  <div class="detail-hero" style="...">
    content = re.sub(
        r'(<div class="detail-hero"[^>]*>)\s*\n(\s*<div class="breadcrumb">)',
        r'\1\n  <div class="hero-inner">\n\2',
        content
    )

    # ── Page hero: <div class="page-hero">
    content = re.sub(
        r'(<div class="page-hero">)\s*\n(\s*<h1>)',
        r'\1\n  <div class="hero-inner">\n\2',
        content
    )

    if content != original:
        changes_made.append(f"  [HERO-INNER] {os.path.basename(filepath)}")
    return content


def apply_hero_inner_buildpy(content):
    """Add .hero-inner wrapper in build.py template functions."""
    original = content

    # Homepage hero in build_homepage()
    content = content.replace(
        '''<!-- Hero -->
<section class="hero">
  <div class="hero-left">''',
        '''<!-- Hero -->
<section class="hero">
  <div class="hero-inner">
  <div class="hero-left">'''
    )

    # Category hero in build_category_page()
    content = content.replace(
        '''<!-- Category Hero -->
<div class="cat-hero">
  <div class="breadcrumb">''',
        '''<!-- Category Hero -->
<div class="cat-hero">
  <div class="hero-inner">
  <div class="breadcrumb">'''
    )

    if content != original:
        changes_made.append(f"  [HERO-INNER] build.py")
    return content


# ═══════════════════════════════════════════════════
# MAIN EXECUTION
# ═══════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("The SaaS Source — Applying Modifications")
    print("=" * 60)

    # ── Process CSS ──
    if os.path.exists(CSS_FILE):
        backup(CSS_FILE)
        css = read(CSS_FILE)
        css = apply_logo_css(css)
        css = apply_font_swap_css(css)
        css = apply_hero_inner_css(css)
        write(CSS_FILE, css)
        print(f"✓ Updated {CSS_FILE}")

    # ── Process HTML files ──
    for html_file in HTML_FILES:
        if os.path.exists(html_file):
            backup(html_file)
            html = read(html_file)
            html = apply_logo_swap(html, html_file)
            html = apply_font_swap_html(html, html_file)
            html = apply_hero_inner_html(html, html_file)
            write(html_file, html)
            print(f"✓ Updated {html_file}")

    # ── Process build.py ──
    if os.path.exists(BUILD_FILE):
        backup(BUILD_FILE)
        bp = read(BUILD_FILE)
        bp = apply_logo_swap_buildpy(bp)
        bp = apply_font_swap_html(bp, BUILD_FILE)  # Same font URL replacement
        bp = apply_hero_inner_buildpy(bp)
        write(BUILD_FILE, bp)
        print(f"✓ Updated {BUILD_FILE}")

    # ── Process DEVELOPER-NOTES.md ──
    if os.path.exists(DEV_NOTES):
        backup(DEV_NOTES)
        dn = read(DEV_NOTES)
        dn = apply_font_swap_devnotes(dn)
        write(DEV_NOTES, dn)
        print(f"✓ Updated {DEV_NOTES}")

    # ── Summary ──
    print("\n" + "=" * 60)
    print(f"Changes applied ({len(changes_made)} operations):")
    print("=" * 60)
    for c in changes_made:
        print(c)
    print("\nBackups saved as *.bak files.")
    print("Review changes, then commit with:")
    print('  git add -A && git commit -m "Swap logo to image, Syne→Roboto, add hero-inner 1920px container"')


if __name__ == "__main__":
    main()

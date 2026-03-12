#!/usr/bin/env python3
"""
The SaaS Source — Inner Hero Enhancement
==========================================
  1. Category heroes → two-column layout with "Quick Compare" widget
  2. Detail heroes (comparison/review/alternatives) → decorative background
  3. Page heroes (about/contact/legal) → decorative background + centered wider text

Usage:
  cd /path/to/thesaassource
  python3 apply_hero_enhance.py
"""

import os
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(REPO_ROOT, "css", "styles.css")
BUILD_FILE = os.path.join(REPO_ROOT, "build.py")
HTML_FILES = glob.glob(os.path.join(REPO_ROOT, "*.html"))

changes = []


def read(fp):
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()


def write(fp, content):
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════════════
# CSS: New styles for enhanced heroes
# ═══════════════════════════════════════════════════

HERO_CSS = """
/* ─── ENHANCED INNER HEROES ─── */

/* Category hero: two-column with widget */
.cat-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 40px;
  align-items: start;
}
.cat-hero-left { }
.cat-hero-widget {
  background: white;
  border-radius: var(--radius-lg);
  padding: 22px;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--gray-100);
}
.cat-widget-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}
.cat-widget-title { font-size: 13px; font-weight: 700; color: var(--ink); }
.cat-widget-badge {
  font-size: 10px; font-weight: 700; padding: 3px 9px;
  border-radius: 100px; background: var(--blue-pale); color: var(--blue);
}
.cat-widget-label {
  font-size: 11px; font-weight: 600; color: var(--gray-mid);
  text-transform: uppercase; letter-spacing: 0.05em;
  margin-bottom: 10px;
}
.cat-widget-items { display: flex; flex-direction: column; gap: 7px; margin-bottom: 16px; }
.cat-widget-item {
  display: flex; align-items: center; gap: 10px;
  padding: 9px 11px; border-radius: 8px;
  background: var(--gray-50); cursor: pointer;
  transition: all 0.15s; text-decoration: none;
}
.cat-widget-item:hover { background: var(--blue-pale); }
.cat-widget-ico {
  width: 32px; height: 32px; border-radius: 7px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Roboto', sans-serif; font-weight: 800; font-size: 12px; color: white;
}
.cat-widget-meta { flex: 1; }
.cat-widget-name { font-size: 13px; font-weight: 600; color: var(--ink); }
.cat-widget-cat { font-size: 10.5px; color: var(--gray-mid); }
.cat-widget-score {
  font-family: 'Roboto', sans-serif; font-size: 14px;
  font-weight: 800; color: var(--ink);
}
.cat-widget-score span { font-size: 10px; font-weight: 400; color: var(--gray-mid); }
.cat-widget-cta {
  display: block; width: 100%; text-align: center;
  padding: 10px; border-radius: 7px; font-size: 13px; font-weight: 600;
  background: var(--blue); color: white; cursor: pointer;
  transition: background 0.15s; text-decoration: none;
}
.cat-widget-cta:hover { background: var(--blue-dark); }
.cat-widget-vs {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 11px; border-radius: 8px;
  border: 1.5px dashed var(--gray-200);
  background: white; cursor: pointer;
  transition: all 0.15s; margin-bottom: 7px; text-decoration: none;
}
.cat-widget-vs:hover { border-color: var(--blue); background: var(--blue-pale); }
.cat-widget-vs-badges { display: flex; align-items: center; gap: 5px; }
.cat-widget-vs-badge {
  width: 26px; height: 26px; border-radius: 5px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Roboto', sans-serif; font-weight: 800; font-size: 9px; color: white;
}
.cat-widget-vs-sep { font-size: 9px; font-weight: 700; color: var(--gray-light); }
.cat-widget-vs-text { flex: 1; font-size: 12px; font-weight: 600; color: var(--ink); }
.cat-widget-vs-arrow { font-size: 11px; color: var(--blue); font-weight: 600; }

/* Detail hero: decorative background elements */
.detail-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 48px 36px 40px;
  border-bottom: 1px solid var(--gray-100);
  position: relative;
  overflow: hidden;
}
.detail-hero::before {
  content: '';
  position: absolute;
  top: -80px;
  right: -40px;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(60,130,200,0.08) 0%, transparent 70%);
  pointer-events: none;
}
.detail-hero::after {
  content: '';
  position: absolute;
  bottom: -60px;
  right: 120px;
  width: 200px;
  height: 200px;
  border: 2px solid rgba(60,130,200,0.07);
  border-radius: 50%;
  pointer-events: none;
}

/* Page hero: decorative + centered wider layout */
.page-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 64px 36px 52px;
  border-bottom: 1px solid var(--gray-100);
  position: relative;
  overflow: hidden;
  text-align: center;
}
.page-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}
.page-hero::before {
  content: '';
  position: absolute;
  top: -100px;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(60,130,200,0.06) 0%, transparent 65%);
  pointer-events: none;
}
.page-hero::after {
  content: '';
  position: absolute;
  top: 20px;
  right: 10%;
  width: 120px;
  height: 120px;
  border: 2px solid rgba(60,130,200,0.06);
  border-radius: 16px;
  transform: rotate(15deg);
  pointer-events: none;
}
.page-hero h1 {
  font-family: 'Roboto', sans-serif;
  font-size: 40px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -0.03em;
  margin-bottom: 14px;
  position: relative;
}
.page-hero p {
  font-size: 17px;
  color: #505060;
  max-width: 640px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
  position: relative;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .cat-hero > .hero-inner { grid-template-columns: 1fr; }
  .cat-hero-widget { max-width: 400px; }
}
"""


def apply_css_enhancements(css):
    original = css

    # Remove old .cat-hero > .hero-inner rule (simple max-width one)
    css = css.replace(
        """.cat-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}""",
        "/* cat-hero .hero-inner — see ENHANCED INNER HEROES section below */"
    )

    # Remove old .detail-hero definition (we're replacing it with decorated version)
    css = css.replace(
        """.detail-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 48px 36px 40px;
  border-bottom: 1px solid var(--gray-100);
}
.detail-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}""",
        """.detail-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
  position: relative;
}"""
    )

    # Remove old .page-hero definitions (we're replacing with enhanced)
    css = css.replace(
        """.page-hero {
  background: linear-gradient(155deg, #F5F7FA 0%, #EBF3FB 100%);
  padding: 56px 36px 44px;
  border-bottom: 1px solid var(--gray-100);
}
.page-hero > .hero-inner {
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}
.page-hero h1 {
  font-family: 'Roboto', sans-serif;
  font-size: 36px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -0.03em;
  margin-bottom: 12px;
}
.page-hero p {
  font-size: 17px;
  color: #505060;
  max-width: 600px;
  line-height: 1.6;
}""",
        "/* page-hero — see ENHANCED INNER HEROES section below */"
    )

    # Insert all new hero CSS before the RESPONSIVE section
    css = css.replace(
        "/* ─── RESPONSIVE ─── */",
        HERO_CSS + "\n/* ─── RESPONSIVE ─── */"
    )

    # Update responsive: remove old .cat-hero .hero-inner override if it conflicts
    # The new responsive block in HERO_CSS handles it

    if css != original:
        changes.append("  [CSS] Enhanced hero styles added")
    return css


# ═══════════════════════════════════════════════════
# HTML: Category hero widgets (contextual per category)
# ═══════════════════════════════════════════════════

# Widget data per category
CRM_WIDGET = """    <div class="cat-hero-widget">
      <div class="cat-widget-header">
        <div class="cat-widget-title">Quick Compare CRM Tools</div>
        <div class="cat-widget-badge">Top Rated</div>
      </div>
      <div class="cat-widget-label">Top picks</div>
      <div class="cat-widget-items">
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#F97316;">HS</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">HubSpot</div><div class="cat-widget-cat">CRM &amp; Marketing</div></div>
          <div class="cat-widget-score">9.1<span>/10</span></div>
        </a>
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#E84040;">SF</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">Salesforce</div><div class="cat-widget-cat">Enterprise CRM</div></div>
          <div class="cat-widget-score">8.7<span>/10</span></div>
        </a>
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#8B5CF6;">AC</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">ActiveCampaign</div><div class="cat-widget-cat">Email + CRM</div></div>
          <div class="cat-widget-score">8.8<span>/10</span></div>
        </a>
      </div>
      <div class="cat-widget-label">Popular comparisons</div>
      <a href="comparison-template.html" class="cat-widget-vs">
        <div class="cat-widget-vs-badges"><div class="cat-widget-vs-badge" style="background:#F97316;">HS</div><div class="cat-widget-vs-sep">vs</div><div class="cat-widget-vs-badge" style="background:#E84040;">SF</div></div>
        <div class="cat-widget-vs-text">HubSpot vs Salesforce</div>
        <div class="cat-widget-vs-arrow">→</div>
      </a>
      <a href="comparison-template.html" class="cat-widget-vs">
        <div class="cat-widget-vs-badges"><div class="cat-widget-vs-badge" style="background:#F97316;">HS</div><div class="cat-widget-vs-sep">vs</div><div class="cat-widget-vs-badge" style="background:#8B5CF6;">AC</div></div>
        <div class="cat-widget-vs-text">HubSpot vs ActiveCampaign</div>
        <div class="cat-widget-vs-arrow">→</div>
      </a>
    </div>"""

EMAIL_WIDGET = """    <div class="cat-hero-widget">
      <div class="cat-widget-header">
        <div class="cat-widget-title">Quick Compare Email Tools</div>
        <div class="cat-widget-badge">Top Rated</div>
      </div>
      <div class="cat-widget-label">Top picks</div>
      <div class="cat-widget-items">
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#8B5CF6;">AC</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">ActiveCampaign</div><div class="cat-widget-cat">Email Automation</div></div>
          <div class="cat-widget-score">8.8<span>/10</span></div>
        </a>
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#0891B2;">BR</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">Brevo</div><div class="cat-widget-cat">Budget Email</div></div>
          <div class="cat-widget-score">8.1<span>/10</span></div>
        </a>
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#FFE01B;">MC</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">Mailchimp</div><div class="cat-widget-cat">Email Marketing</div></div>
          <div class="cat-widget-score">7.9<span>/10</span></div>
        </a>
      </div>
      <div class="cat-widget-label">Popular comparisons</div>
      <a href="comparison-template.html" class="cat-widget-vs">
        <div class="cat-widget-vs-badges"><div class="cat-widget-vs-badge" style="background:#8B5CF6;">AC</div><div class="cat-widget-vs-sep">vs</div><div class="cat-widget-vs-badge" style="background:#0891B2;">BR</div></div>
        <div class="cat-widget-vs-text">ActiveCampaign vs Brevo</div>
        <div class="cat-widget-vs-arrow">→</div>
      </a>
      <a href="comparison-template.html" class="cat-widget-vs">
        <div class="cat-widget-vs-badges"><div class="cat-widget-vs-badge" style="background:#8B5CF6;">AC</div><div class="cat-widget-vs-sep">vs</div><div class="cat-widget-vs-badge" style="background:#FFE01B;">MC</div></div>
        <div class="cat-widget-vs-text">ActiveCampaign vs Mailchimp</div>
        <div class="cat-widget-vs-arrow">→</div>
      </a>
    </div>"""

AUTOMATION_WIDGET = """    <div class="cat-hero-widget">
      <div class="cat-widget-header">
        <div class="cat-widget-title">Quick Compare Automation</div>
        <div class="cat-widget-badge">Top Rated</div>
      </div>
      <div class="cat-widget-label">Top picks</div>
      <div class="cat-widget-items">
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#F97316;">HS</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">HubSpot</div><div class="cat-widget-cat">CRM &amp; Marketing</div></div>
          <div class="cat-widget-score">9.1<span>/10</span></div>
        </a>
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#8B5CF6;">AC</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">ActiveCampaign</div><div class="cat-widget-cat">Email Automation</div></div>
          <div class="cat-widget-score">8.8<span>/10</span></div>
        </a>
        <a href="review-template.html" class="cat-widget-item">
          <div class="cat-widget-ico" style="background:#059669;">KJ</div>
          <div class="cat-widget-meta"><div class="cat-widget-name">Kajabi</div><div class="cat-widget-cat">Courses &amp; Funnels</div></div>
          <div class="cat-widget-score">8.6<span>/10</span></div>
        </a>
      </div>
      <div class="cat-widget-label">Popular comparisons</div>
      <a href="comparison-template.html" class="cat-widget-vs">
        <div class="cat-widget-vs-badges"><div class="cat-widget-vs-badge" style="background:#F97316;">HS</div><div class="cat-widget-vs-sep">vs</div><div class="cat-widget-vs-badge" style="background:#8B5CF6;">AC</div></div>
        <div class="cat-widget-vs-text">HubSpot vs ActiveCampaign</div>
        <div class="cat-widget-vs-arrow">→</div>
      </a>
      <a href="comparison-template.html" class="cat-widget-vs">
        <div class="cat-widget-vs-badges"><div class="cat-widget-vs-badge" style="background:#059669;">KJ</div><div class="cat-widget-vs-sep">vs</div><div class="cat-widget-vs-badge" style="background:#DC2626;">CF</div></div>
        <div class="cat-widget-vs-text">Kajabi vs ClickFunnels</div>
        <div class="cat-widget-vs-arrow">→</div>
      </a>
    </div>"""


def enhance_category_hero(content, filepath, widget_html):
    """Wrap cat-hero content in left column + add widget on right."""
    original = content
    basename = os.path.basename(filepath)

    # Find the cat-hero .hero-inner and restructure
    # Current structure: .cat-hero > .hero-inner > [breadcrumb, h1, p, stats]
    # Target:  .cat-hero > .hero-inner > .cat-hero-left[breadcrumb, h1, p, stats] + .cat-hero-widget

    # Wrap breadcrumb through stats in .cat-hero-left
    # Look for the hero-inner opening, then wrap until closing
    import re

    # Pattern: after hero-inner, wrap everything until the closing of cat-stats in cat-hero-left
    pattern = r'(<div class="hero-inner">\s*\n)(\s*<div class="breadcrumb">.*?</div>\s*\n)(.*?)(</div>\s*\n</div>\s*\n\s*(?:<!-- Filters|<div class="hero-inner">))'

    # Simpler approach: insert <div class="cat-hero-left"> after hero-inner, 
    # and close it + add widget before the cat-hero closing
    
    # Step 1: Add opening cat-hero-left after hero-inner
    content = content.replace(
        '<div class="cat-hero">\n  <div class="hero-inner">\n  <div class="breadcrumb">',
        '<div class="cat-hero">\n  <div class="hero-inner">\n  <div class="cat-hero-left">\n  <div class="breadcrumb">'
    )

    # Step 2: Find the cat-stats closing div pattern and close cat-hero-left, add widget
    # The cat-stats section ends, then we need to close cat-hero-left and insert widget
    # Current pattern after stats: </div>\n</div>\n\n<!-- Filters  (cat-stats close, then cat-hero close)
    # OR: </div>\n  </div>\n</div> 

    # Try to find the stats closing and the hero-inner / cat-hero closing
    # We look for the cat-stats closing followed by what was the hero-inner close and cat-hero close
    
    # In the current HTML, after the cat-stats div, the structure likely goes:
    #   </div>  ← closes cat-stats
    # </div>    ← was closing hero-inner (now we need to close cat-hero-left first)
    # </div>    ← closes cat-hero
    
    # Insert widget before the hero-inner and cat-hero closing divs
    # Find the pattern: after cat-stats, before Filters section
    
    old_close = '</div>\n</div>\n\n<!-- Filters'
    new_close = '</div>\n  </div>\n' + widget_html + '\n  </div>\n</div>\n\n<!-- Filters'
    
    if old_close in content:
        content = content.replace(old_close, new_close, 1)
    else:
        # Try alternate spacing
        old_close2 = '  </div>\n</div>\n\n<!-- Filters'
        new_close2 = '  </div>\n  </div>\n' + widget_html + '\n  </div>\n</div>\n\n<!-- Filters'
        content = content.replace(old_close2, new_close2, 1)

    if content != original:
        changes.append(f"  [HERO-WIDGET] {basename} — Quick Compare widget added")
    return content


# Map category files to their widgets
CATEGORY_WIDGETS = {
    "category-crm.html": CRM_WIDGET,
    "category-email-marketing.html": EMAIL_WIDGET,
    "category-marketing-automation.html": AUTOMATION_WIDGET,
}


# ═══════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("The SaaS Source — Inner Hero Enhancement")
    print("=" * 60)

    # 1. CSS enhancements
    if os.path.exists(CSS_FILE):
        css = read(CSS_FILE)
        css = apply_css_enhancements(css)
        write(CSS_FILE, css)
        print(f"✓ {CSS_FILE}")

    # 2. Category hero widgets
    for filename, widget in CATEGORY_WIDGETS.items():
        fp = os.path.join(REPO_ROOT, filename)
        if os.path.exists(fp):
            html = read(fp)
            html = enhance_category_hero(html, fp, widget)
            write(fp, html)
            print(f"✓ {fp}")

    # 3. build.py — update category hero builder
    if os.path.exists(BUILD_FILE):
        bp = read(BUILD_FILE)
        original = bp

        # Wrap the category hero content in cat-hero-left
        bp = bp.replace(
            '<div class="hero-inner">\n  <div class="breadcrumb"><a href="index.html">Home</a><span>›</span><span>{category_name}</span></div>',
            '<div class="hero-inner">\n  <div class="cat-hero-left">\n  <div class="breadcrumb"><a href="index.html">Home</a><span>›</span><span>{category_name}</span></div>'
        )

        # After cat-stats close, close cat-hero-left and add placeholder widget
        bp = bp.replace(
            '  </div>\n</div>\n\n<!-- Filters',
            '  </div>\n  </div>\n    <div class="cat-hero-widget">\n      <div class="cat-widget-header">\n        <div class="cat-widget-title">Quick Compare Tools</div>\n        <div class="cat-widget-badge">Top Rated</div>\n      </div>\n      <div class="cat-widget-label">Category-specific tools will appear here</div>\n    </div>\n  </div>\n</div>\n\n<!-- Filters'
        )

        if bp != original:
            write(BUILD_FILE, bp)
            changes.append("  [BUILD] build.py — category hero updated with widget wrapper")
        print(f"✓ {BUILD_FILE}")

    print(f"\n{'=' * 60}")
    print(f"Done — {len(changes)} changes:")
    print("=" * 60)
    for c in changes:
        print(c)
    print()
    print("NOTE: The detail-hero and page-hero decorative backgrounds are")
    print("pure CSS — no HTML changes needed for those. The category heroes")
    print("now have contextual Quick Compare widgets with top tools and")
    print("popular head-to-head comparisons for each category.")
    print()
    print('Commit: git add -A && git commit -m "Enhance inner heroes: category widgets, decorative backgrounds"')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
The SaaS Source — Round 2 Modifications
========================================
Applies three changes:
  1. Increase general body font sizes by 1px (excluding info boxes)
  2. Footer font color → #cfcfcf, increase footer logo size
  3. Comparison template: replace placeholder prose with simulated content

Usage:
  cd /path/to/thesaassource
  python3 apply_changes_r2.py

Creates backups of each file before modifying.
"""

import os
import shutil
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(REPO_ROOT, "css", "styles.css")
COMPARISON_HTML = os.path.join(REPO_ROOT, "comparison-template.html")
BUILD_FILE = os.path.join(REPO_ROOT, "build.py")

changes_made = []


def backup(filepath):
    bak = filepath + ".r2.bak"
    if not os.path.exists(bak):
        shutil.copy2(filepath, bak)


def read(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════════════
# CHANGE 1: Increase body font sizes by 1px
# ═══════════════════════════════════════════════════
# Target: general body/content text sizes
# Exclude: info boxes (.verdict-box, .vb-text, .announce,
#          .hc-*, .cc-*, nav elements, badges, pills, tags,
#          form hints, and other UI chrome)

def apply_font_size_bump(css):
    original = css

    # ── Body base: 15px → 16px ──
    css = css.replace(
        "body {\n  font-family: 'DM Sans', sans-serif;\n  background: var(--white);\n  color: var(--charcoal);\n  font-size: 15px;",
        "body {\n  font-family: 'DM Sans', sans-serif;\n  background: var(--white);\n  color: var(--charcoal);\n  font-size: 16px;"
    )

    # ── Hero subtitle: 16.5px → 17.5px ──
    css = css.replace(
        ".hero-sub {\n  font-size: 16.5px;",
        ".hero-sub {\n  font-size: 17.5px;"
    )

    # ── Category hero subtitle: 16px → 17px ──
    css = css.replace(
        ".cat-hero-sub {\n  font-size: 16px;",
        ".cat-hero-sub {\n  font-size: 17px;"
    )

    # ── Buttons: 14px → 15px ──
    css = css.replace(
        ".btn-primary {\n  background: var(--blue);\n  color: white;\n  padding: 13px 26px;\n  border-radius: 8px;\n  font-size: 14px;",
        ".btn-primary {\n  background: var(--blue);\n  color: white;\n  padding: 13px 26px;\n  border-radius: 8px;\n  font-size: 15px;"
    )
    css = css.replace(
        ".btn-ghost {\n  background: white;\n  color: var(--ink);\n  padding: 13px 26px;\n  border-radius: 8px;\n  font-size: 14px;",
        ".btn-ghost {\n  background: white;\n  color: var(--ink);\n  padding: 13px 26px;\n  border-radius: 8px;\n  font-size: 15px;"
    )

    # ── Prose paragraphs: 15px → 16px ──
    css = css.replace(
        ".prose p {\n  font-size: 15px;",
        ".prose p {\n  font-size: 16px;"
    )

    # ── Prose list items: 15px → 16px ──
    css = css.replace(
        ".prose li {\n  font-size: 15px;",
        ".prose li {\n  font-size: 16px;"
    )

    # ── Page hero paragraph: 16px → 17px ──
    css = css.replace(
        ".page-hero p {\n  font-size: 16px;",
        ".page-hero p {\n  font-size: 17px;"
    )

    # ── Contact info paragraph: 14px → 15px ──
    css = css.replace(
        ".contact-info p { font-size: 14px;",
        ".contact-info p { font-size: 15px;"
    )

    # ── Category list info description: 13px → 14px ──
    css = css.replace(
        ".cat-list-info p { font-size: 13px;",
        ".cat-list-info p { font-size: 14px;"
    )

    # ── Detail meta items: 13px → 14px ──
    css = css.replace(
        ".dm-item { display: flex; align-items: center; gap: 6px; font-size: 13px;",
        ".dm-item { display: flex; align-items: center; gap: 6px; font-size: 14px;"
    )

    # ── Form inputs: 14px → 15px ──
    css = css.replace(
        "  font-size: 14px;\n  font-family: 'DM Sans', sans-serif;\n  color: var(--ink);\n  background: white;\n  transition: border-color 0.15s;",
        "  font-size: 15px;\n  font-family: 'DM Sans', sans-serif;\n  color: var(--ink);\n  background: white;\n  transition: border-color 0.15s;"
    )

    # ── Review form subtitle: 14px → 15px ──
    css = css.replace(
        ".review-form-section .form-subtitle {\n  font-size: 14px;",
        ".review-form-section .form-subtitle {\n  font-size: 15px;"
    )

    # ── Nav links: 13px → 14px ──
    css = css.replace(
        "  padding: 8px 13px;\n  font-size: 13px;\n  font-weight: 500;\n  color: #606070;\n  cursor: pointer;\n  border-bottom: 2px solid transparent;\n  height: 68px;",
        "  padding: 8px 13px;\n  font-size: 14px;\n  font-weight: 500;\n  color: #606070;\n  cursor: pointer;\n  border-bottom: 2px solid transparent;\n  height: 68px;"
    )

    # ── Breadcrumb: 12px → 13px ──
    css = css.replace(
        ".breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 12px;",
        ".breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 13px;"
    )

    # ── Section link: 13px → 14px ──
    css = css.replace(
        ".sec-link {\n  font-size: 13px;",
        ".sec-link {\n  font-size: 14px;"
    )

    # ── Footer links: 13px → 14px ──
    css = css.replace(
        ".footer-link { font-size: 13px;",
        ".footer-link { font-size: 14px;"
    )

    # ── Footer brand paragraph: 12.5px → 13.5px ──
    css = css.replace(
        ".footer-brand p { font-size: 12.5px;",
        ".footer-brand p { font-size: 13.5px;"
    )

    # ── Footer legal: 12px → 13px ──
    css = css.replace(
        ".footer-legal { font-size: 12px;",
        ".footer-legal { font-size: 13px;"
    )

    if css != original:
        changes_made.append("  [FONT-SIZE] css/styles.css — bumped body text sizes +1px")
    return css


# ═══════════════════════════════════════════════════
# CHANGE 2: Footer color → #cfcfcf + larger logo
# ═══════════════════════════════════════════════════

def apply_footer_color(css):
    original = css

    # ── Footer brand text: #6A7288 → #cfcfcf ──
    css = css.replace(
        ".footer-brand p { font-size: 13.5px; color: #6A7288;",
        ".footer-brand p { font-size: 13.5px; color: #cfcfcf;"
    )

    # ── Footer logo text color: #8090A8 → #cfcfcf ──
    css = css.replace(
        "  color: #8090A8;\n  margin-bottom: 14px;\n}\n.footer-brand .footer-logo .accent { color: var(--blue); }",
        "  color: #cfcfcf;\n  margin-bottom: 14px;\n}\n.footer-brand .footer-logo .accent { color: var(--blue); }"
    )

    # ── Footer column headings: #8090A8 → #cfcfcf ──
    css = css.replace(
        "  text-transform: uppercase; color: #8090A8; margin-bottom: 14px;",
        "  text-transform: uppercase; color: #cfcfcf; margin-bottom: 14px;"
    )

    # ── Footer links: #6A7288 → #cfcfcf ──
    css = css.replace(
        ".footer-link { font-size: 14px; color: #6A7288;",
        ".footer-link { font-size: 14px; color: #cfcfcf;"
    )

    # ── Footer legal text: #4A5268 → #cfcfcf ──
    css = css.replace(
        ".footer-legal { font-size: 13px; color: #4A5268; }",
        ".footer-legal { font-size: 13px; color: #cfcfcf; }"
    )

    # ── Footer legal links: #606880 → #cfcfcf ──
    css = css.replace(
        ".footer-legal a { color: #606880;",
        ".footer-legal a { color: #cfcfcf;"
    )

    # ── Increase footer logo size: 18px → 22px ──
    css = css.replace(
        ".footer-brand .footer-logo {\n  font-family: 'Syne', sans-serif;\n  font-size: 18px;",
        ".footer-brand .footer-logo {\n  font-family: 'Syne', sans-serif;\n  font-size: 22px;"
    )
    # Also handle post-round-1 version with Roboto
    css = css.replace(
        ".footer-brand .footer-logo {\n  font-family: 'Roboto', sans-serif;\n  font-size: 18px;",
        ".footer-brand .footer-logo {\n  font-family: 'Roboto', sans-serif;\n  font-size: 22px;"
    )

    # ── If round 1 was applied, also increase .footer-logo-img size ──
    css = css.replace(
        ".footer-logo-img { height: 24px;",
        ".footer-logo-img { height: 32px;"
    )

    if css != original:
        changes_made.append("  [FOOTER] css/styles.css — color #cfcfcf, logo enlarged")
    return css


# ═══════════════════════════════════════════════════
# CHANGE 3: Comparison page — simulated content
# ═══════════════════════════════════════════════════

SIMULATED_PROSE = """    <div class="prose">
      <h2>Detailed Comparison</h2>
      <p>Choosing between HubSpot and ActiveCampaign comes down to what your business actually needs day-to-day. Both platforms have matured significantly in recent years, but they've taken very different paths to get where they are. HubSpot has evolved into a full-fledged business operating system — CRM, marketing, sales, service, and CMS all under one roof. ActiveCampaign has doubled down on what it does best: sophisticated email automation and deliverability at a price point that doesn't require a board-level budget conversation.</p>
      <p>We spent over 40 hours testing both platforms side by side, building real workflows, importing test contact lists, and stress-testing each tool's automation builder. Here's what we found across every major category.</p>

      <h3>Pricing Comparison</h3>
      <p>HubSpot offers a genuinely useful free tier that includes basic CRM, email marketing (up to 2,000 sends/month), forms, and live chat. It's one of the best free plans in the industry and a major advantage for startups and solopreneurs testing the waters. However, costs escalate quickly once you move to paid tiers. The Starter plan begins at $20/month, but the Professional tier — where most of the advanced marketing automation lives — jumps to $890/month. Enterprise starts at $3,600/month.</p>
      <p>ActiveCampaign has no free plan, but its entry point is significantly lower for paid features. The Starter plan begins at $15/month for 1,000 contacts with basic email and automation. The Plus plan ($49/month) unlocks CRM, landing pages, and lead scoring. The Professional tier at $79/month adds predictive sending, split automations, and site messaging. Enterprise pricing is custom but typically runs $145–$200/month for mid-size contact lists.</p>
      <p>For businesses with fewer than 5,000 contacts that need serious automation, ActiveCampaign delivers substantially more value per dollar. HubSpot becomes more cost-competitive when you factor in the value of having CRM, CMS, and service tools all integrated — but only if you'll actually use those additional hubs.</p>

      <h3>CRM &amp; Contact Management</h3>
      <p>HubSpot's CRM is the backbone of its ecosystem and one of the most polished free CRMs available. Contact records are rich and detailed, pulling in company information, social profiles, and a complete timeline of every interaction — emails opened, pages visited, forms submitted, deals progressed. The visual deal pipeline is drag-and-drop intuitive, and the ability to create custom properties means you can track virtually any data point relevant to your sales process.</p>
      <p>ActiveCampaign's CRM capabilities are functional but clearly secondary to its automation engine. The built-in CRM (available on Plus and above) provides basic deal tracking, pipeline management, and contact scoring. Contact records show engagement history and automation status, which is useful for sales follow-up. However, it lacks the depth of HubSpot's contact intelligence — there's no automatic company enrichment, limited social data, and the pipeline views feel less refined.</p>
      <p>If your team lives in the CRM daily and needs robust deal tracking, HubSpot is the clear winner here. If your sales process is simpler and you primarily need contact management to power automations, ActiveCampaign's CRM is more than adequate.</p>

      <h3>Email Marketing &amp; Automation</h3>
      <p>This is where ActiveCampaign truly shines. Its visual automation builder is arguably the best in the industry — you can create complex, branching workflows with conditional logic, wait steps, if/else splits, goal tracking, and even predictive actions. Automations can span email, SMS, site messaging, CRM updates, and webhook triggers. The "Automations Map" feature lets you visualize how all your automations connect and interact, which is invaluable for complex marketing stacks.</p>
      <p>HubSpot's workflow builder is capable and improving with each update, but it still feels a step behind ActiveCampaign for pure automation depth. Simple sequences and nurture workflows are straightforward to build, and the drag-and-drop editor works well. However, creating deeply nested conditional logic or highly personalized automation paths requires more workarounds. Where HubSpot gains an edge is in connecting automations to its broader ecosystem — triggering sales tasks, updating deal stages, creating service tickets, and managing content all from within a single workflow.</p>
      <p>For email deliverability — a critical metric that often gets overlooked — ActiveCampaign consistently outperforms HubSpot in independent tests, typically achieving 93–96% inbox placement rates versus HubSpot's 89–93%. This can make a measurable difference in campaign ROI.</p>

      <h3>Reporting &amp; Analytics</h3>
      <p>HubSpot offers a comprehensive analytics suite that spans marketing, sales, and service data. The attribution reporting is particularly strong — you can track which channels, campaigns, and touchpoints contribute to conversions across the entire customer journey. Custom report builders let you create dashboards combining data from any Hub, and the built-in traffic analytics compete with standalone tools. Revenue attribution reporting (available on Professional and above) connects marketing activities directly to closed deals.</p>
      <p>ActiveCampaign's reporting is focused primarily on email and automation performance. You get detailed campaign reports (opens, clicks, unsubscribes, bounces), automation performance metrics, and contact trend analysis. The "Deals" report provides basic pipeline analytics. However, there's no multi-touch attribution, limited cross-channel analytics, and no built-in traffic reporting. For businesses that need deep marketing analytics, you'll likely need to supplement ActiveCampaign with Google Analytics or a dedicated BI tool.</p>

      <h3>Integration Ecosystem</h3>
      <p>HubSpot's App Marketplace includes over 1,500 native integrations spanning categories from e-commerce (Shopify, WooCommerce) to analytics (Google Analytics, Hotjar) to communication (Slack, Zoom, Microsoft Teams). The depth of integration is often superior too — many connectors offer bi-directional sync, custom field mapping, and trigger-based automation. HubSpot's open API is well-documented and widely supported by third-party tools.</p>
      <p>ActiveCampaign offers around 900+ integrations, which covers most major platforms but with less depth in some categories. The Shopify and WooCommerce integrations are particularly strong for e-commerce businesses, enabling sophisticated abandoned cart sequences and purchase-based segmentation. The Zapier integration fills most gaps, though it adds another subscription cost and occasional latency. ActiveCampaign's API is solid but less extensively adopted by third-party developers compared to HubSpot's.</p>

      <h2>Final Verdict</h2>
      <p>There's no universally "better" platform — the right choice depends entirely on your priorities and budget. HubSpot is the stronger pick for businesses that want a unified platform where marketing, sales, service, and content management all live together. The free CRM is a genuine differentiator, and the ecosystem's breadth is hard to match. But that power comes at a price that can escalate quickly.</p>
      <p>ActiveCampaign wins for businesses where email marketing and automation are the primary focus. Its automation builder is more powerful, its deliverability rates are higher, and its pricing delivers significantly more value at the mid-tier level. If you don't need a full CRM suite and you want the best email automation dollar-for-dollar, ActiveCampaign is the smarter investment.</p>
    </div>"""


# The placeholder block we're replacing in comparison-template.html
PLACEHOLDER_PROSE = """    <!-- Placeholder for long-form comparison content -->
    <div class="prose">
      <h2>Detailed Comparison</h2>
      <p><em>[Long-form comparison content goes here. This section will be filled with detailed analysis of each platform, covering pricing tiers, feature deep-dives, user experience comparisons, integration ecosystems, support quality, and real-world use case recommendations.]</em></p>
      
      <h3>Pricing Comparison</h3>
      <p><em>[Detailed pricing breakdown with tier-by-tier comparison tables]</em></p>
      
      <h3>CRM & Contact Management</h3>
      <p><em>[Feature comparison content]</em></p>
      
      <h3>Email Marketing & Automation</h3>
      <p><em>[Feature comparison content]</em></p>
      
      <h3>Reporting & Analytics</h3>
      <p><em>[Feature comparison content]</em></p>
      
      <h3>Integration Ecosystem</h3>
      <p><em>[Feature comparison content]</em></p>
      
      <h2>Final Verdict</h2>
      <p><em>[Summary and final recommendation]</em></p>
    </div>"""


def apply_comparison_content(content, filepath):
    original = content
    content = content.replace(PLACEHOLDER_PROSE, SIMULATED_PROSE)
    if content != original:
        changes_made.append(f"  [CONTENT] {os.path.basename(filepath)} — simulated comparison prose added")
    return content


# ═══════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("The SaaS Source — Round 2 Modifications")
    print("=" * 60)

    # ── CSS changes ──
    if os.path.exists(CSS_FILE):
        backup(CSS_FILE)
        css = read(CSS_FILE)
        css = apply_font_size_bump(css)
        css = apply_footer_color(css)
        write(CSS_FILE, css)
        print(f"✓ Updated {CSS_FILE}")

    # ── Comparison HTML ──
    if os.path.exists(COMPARISON_HTML):
        backup(COMPARISON_HTML)
        html = read(COMPARISON_HTML)
        html = apply_comparison_content(html, COMPARISON_HTML)
        write(COMPARISON_HTML, html)
        print(f"✓ Updated {COMPARISON_HTML}")

    # ── build.py (same placeholder appears there too) ──
    if os.path.exists(BUILD_FILE):
        backup(BUILD_FILE)
        bp = read(BUILD_FILE)
        bp = apply_comparison_content(bp, BUILD_FILE)
        write(BUILD_FILE, bp)
        print(f"✓ Updated {BUILD_FILE}")

    # ── Summary ──
    print(f"\n{'=' * 60}")
    print(f"Changes applied ({len(changes_made)} operations):")
    print("=" * 60)
    for c in changes_made:
        print(c)
    print("\nBackups saved as *.r2.bak files.")
    print("Review changes, then commit with:")
    print('  git add -A && git commit -m "R2: font size +1px, footer #cfcfcf + larger logo, comparison simulated content"')


if __name__ == "__main__":
    main()

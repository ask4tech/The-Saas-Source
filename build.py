#!/usr/bin/env python3
"""
The SaaS Source — Static Site Generator
Generates all HTML page templates from shared components.
Run: python3 build.py
"""
import os
import textwrap

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── SHARED COMPONENTS ───

HEAD = lambda title, css_path="css/styles.css": f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — The SaaS Source</title>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_path}">
</head>
<body>
"""

ANNOUNCE_BAR = """<!-- Announcement Bar -->
<div class="announce">
  <span>🎉 <strong>New:</strong> 2025 CRM Buyer's Guide is live — 47 tools compared</span>
  <a href="#">Read now →</a>
</div>
"""

def NAV(active=""):
    links = [
        ("CRM Software", "crm", "category-crm.html"),
        ("Email Marketing", "email", "category-email-marketing.html"),
        ("Marketing Automation", "automation", "category-marketing-automation.html"),
        ("Sales & Funnels", "funnels", "#"),
        ("Support", "support", "#"),
        ("Comparisons", "comparisons", "comparison-template.html"),
        ("Alternatives", "alternatives", "alternatives-template.html"),
    ]
    nav_html = """<!-- Navigation -->
<nav class="nav">
  <a href="index.html" class="nav-logo">
    <img src="images/logo.png" alt="The SaaS Source" class="nav-logo-img">
  </a>
  <div class="nav-links">
"""
    for label, key, href in links:
        cls = ' class="nav-link active"' if key == active else ' class="nav-link"'
        nav_html += f'    <a href="{href}"{cls}>{label}</a>\n'
    
    nav_html += """  </div>
  <div class="nav-right">
    <div class="nav-search">🔍 Search software…</div>
    <a href="comparison-template.html" class="nav-btn">Compare Tools →</a>
  </div>
  <button class="nav-toggle"><span></span><span></span><span></span></button>
</nav>
"""
    return nav_html

FOOTER = """<!-- Footer -->
<footer class="footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="footer-logo"><img src="images/logo.png" alt="The SaaS Source" class="footer-logo-img"></div>
      <p>Independent research and unbiased comparisons for B2B software buyers. We help you find the right tool — without the hype.</p>
    </div>
    <div class="footer-col">
      <h4>Categories</h4>
      <div class="footer-links">
        <a href="category-crm.html" class="footer-link">CRM Software</a>
        <a href="category-email-marketing.html" class="footer-link">Email Marketing</a>
        <a href="category-marketing-automation.html" class="footer-link">Marketing Automation</a>
        <a href="#" class="footer-link">Sales &amp; Funnels</a>
        <a href="#" class="footer-link">Customer Support</a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Comparisons</h4>
      <div class="footer-links">
        <a href="comparison-template.html" class="footer-link">HubSpot vs Salesforce</a>
        <a href="#" class="footer-link">Kajabi vs ClickFunnels</a>
        <a href="#" class="footer-link">Zendesk vs Intercom</a>
        <a href="#" class="footer-link">ActiveCampaign vs Brevo</a>
        <a href="comparison-template.html" class="footer-link">View All →</a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <div class="footer-links">
        <a href="about.html" class="footer-link">About Us</a>
        <a href="about.html#methodology" class="footer-link">How We Review</a>
        <a href="contact.html" class="footer-link">Contact</a>
        <a href="affiliate-disclosure.html" class="footer-link">Affiliate Disclosure</a>
        <a href="privacy-policy.html" class="footer-link">Privacy Policy</a>
        <a href="terms-of-use.html" class="footer-link">Terms of Use</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-legal">© 2025 The SaaS Source · Nomad Design Holdings, LLC · <a href="privacy-policy.html">Privacy Policy</a> · <a href="affiliate-disclosure.html">Affiliate Disclosure</a> · <a href="terms-of-use.html">Terms of Use</a></div>
    <div class="footer-legal">Independent reviews. We may earn commissions — <a href="affiliate-disclosure.html">learn how</a>.</div>
  </div>
</footer>
"""

CLOSE = """</body>
</html>
"""

# ─── REVIEW FORM COMPONENT (reusable) ───
REVIEW_FORM = lambda software_name="[Software Name]": f"""
<section class="section-full" id="submit-review">
  <div style="max-width:720px;margin:0 auto;">
    <div class="review-form-section">
      <h2>Submit Your Review of {software_name}</h2>
      <p class="form-subtitle">Share your experience to help other buyers make smarter decisions. All reviews are moderated before publishing.</p>
      
      <form id="reviewForm" action="#" method="POST">
        <div class="form-grid-2">
          <div class="form-row">
            <label for="reviewer-name">Your Name *</label>
            <input type="text" id="reviewer-name" name="reviewer_name" placeholder="Jane Smith" required>
          </div>
          <div class="form-row">
            <label for="reviewer-email">Email (not published) *</label>
            <input type="email" id="reviewer-email" name="reviewer_email" placeholder="jane@company.com" required>
            <div class="hint">We'll verify your review but never share your email.</div>
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-row">
            <label for="company-name">Company Name</label>
            <input type="text" id="company-name" name="company_name" placeholder="Your company">
          </div>
          <div class="form-row">
            <label for="company-size">Company Size</label>
            <select id="company-size" name="company_size">
              <option value="">Select…</option>
              <option>1-10 employees</option>
              <option>11-50 employees</option>
              <option>51-200 employees</option>
              <option>201-1000 employees</option>
              <option>1000+ employees</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <label for="role">Your Role / Job Title</label>
          <input type="text" id="role" name="role" placeholder="e.g., Marketing Manager, CEO, Sales Director">
        </div>

        <div class="form-row">
          <label>Overall Rating *</label>
          <div class="star-rating-input" id="overall-rating">
            <span class="star" data-value="1">★</span>
            <span class="star" data-value="2">★</span>
            <span class="star" data-value="3">★</span>
            <span class="star" data-value="4">★</span>
            <span class="star" data-value="5">★</span>
          </div>
          <input type="hidden" name="overall_rating" id="overall-rating-value">
        </div>

        <div class="form-grid-3">
          <div class="form-row">
            <label>Ease of Use</label>
            <div class="star-rating-input" data-field="ease_of_use">
              <span class="star" data-value="1">★</span><span class="star" data-value="2">★</span><span class="star" data-value="3">★</span><span class="star" data-value="4">★</span><span class="star" data-value="5">★</span>
            </div>
          </div>
          <div class="form-row">
            <label>Features</label>
            <div class="star-rating-input" data-field="features">
              <span class="star" data-value="1">★</span><span class="star" data-value="2">★</span><span class="star" data-value="3">★</span><span class="star" data-value="4">★</span><span class="star" data-value="5">★</span>
            </div>
          </div>
          <div class="form-row">
            <label>Value for Money</label>
            <div class="star-rating-input" data-field="value">
              <span class="star" data-value="1">★</span><span class="star" data-value="2">★</span><span class="star" data-value="3">★</span><span class="star" data-value="4">★</span><span class="star" data-value="5">★</span>
            </div>
          </div>
        </div>

        <div class="form-row">
          <label for="review-title">Review Title *</label>
          <input type="text" id="review-title" name="review_title" placeholder="Summarize your experience in one line" required>
        </div>

        <div class="form-row">
          <label for="pros">What do you like best? *</label>
          <textarea id="pros" name="pros" placeholder="Describe what works well…" required></textarea>
        </div>

        <div class="form-row">
          <label for="cons">What could be improved?</label>
          <textarea id="cons" name="cons" placeholder="Describe any drawbacks or limitations…"></textarea>
        </div>

        <div class="form-row">
          <label for="use-case">How do you use this tool?</label>
          <textarea id="use-case" name="use_case" placeholder="Briefly describe your use case and how long you've been using it…"></textarea>
        </div>

        <div class="form-row" style="margin-top:8px;">
          <label style="display:flex;align-items:center;gap:8px;font-weight:400;">
            <input type="checkbox" name="agree_terms" required>
            I confirm this is my honest experience and I agree to the <a href="terms-of-use.html" style="color:var(--blue);text-decoration:underline;">Terms of Use</a>.
          </label>
        </div>

        <div style="margin-top:24px;">
          <button type="submit" class="btn-primary" style="width:100%;justify-content:center;">Submit Review →</button>
        </div>
      </form>
    </div>
  </div>
</section>
"""

REVIEW_FORM_JS = """
<script>
// Star rating interactivity
document.querySelectorAll('.star-rating-input').forEach(group => {
  const stars = group.querySelectorAll('.star');
  stars.forEach(star => {
    star.addEventListener('click', () => {
      const val = parseInt(star.dataset.value);
      stars.forEach(s => {
        s.classList.toggle('active', parseInt(s.dataset.value) <= val);
      });
      // Set hidden input if exists
      const hiddenInput = group.nextElementSibling;
      if (hiddenInput && hiddenInput.type === 'hidden') {
        hiddenInput.value = val;
      }
    });
    star.addEventListener('mouseenter', () => {
      const val = parseInt(star.dataset.value);
      stars.forEach(s => {
        s.style.color = parseInt(s.dataset.value) <= val ? '#E8A020' : '';
      });
    });
    group.addEventListener('mouseleave', () => {
      stars.forEach(s => {
        s.style.color = s.classList.contains('active') ? '#E8A020' : '';
      });
    });
  });
});

// Form submission handler (placeholder)
document.getElementById('reviewForm')?.addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Thank you! Your review has been submitted for moderation. We\\'ll notify you once it\\'s published.');
  this.reset();
  document.querySelectorAll('.star').forEach(s => s.classList.remove('active'));
});
</script>
"""

# ─── PRODUCT DATA ───
PRODUCTS = {
    "hubspot": {"name": "HubSpot", "abbr": "HS", "color": "#F97316", "cat": "CRM & Marketing", "score": "9.1", "price": "Free / $20/mo", "best": "All-in-One SMB"},
    "activecampaign": {"name": "ActiveCampaign", "abbr": "AC", "color": "#8B5CF6", "cat": "Email Automation", "score": "8.8", "price": "$29/mo", "best": "Email Automation"},
    "kajabi": {"name": "Kajabi", "abbr": "KJ", "color": "#059669", "cat": "Courses & Funnels", "score": "8.6", "price": "$69/mo", "best": "Course Creators"},
    "clickfunnels": {"name": "ClickFunnels", "abbr": "CF", "color": "#DC2626", "cat": "Sales Funnels", "score": "8.3", "price": "$97/mo", "best": "Sales Funnels"},
    "brevo": {"name": "Brevo", "abbr": "BR", "color": "#0891B2", "cat": "Email Marketing", "score": "8.1", "price": "Free / $25/mo", "best": "Budget Email"},
    "zendesk": {"name": "Zendesk", "abbr": "ZD", "color": "#0891B2", "cat": "Customer Support", "score": "8.5", "price": "$19/mo", "best": "Enterprise Support"},
    "intercom": {"name": "Intercom", "abbr": "IC", "color": "#7C3AED", "cat": "Customer Messaging", "score": "8.4", "price": "$74/mo", "best": "Product-Led Growth"},
    "salesforce": {"name": "Salesforce", "abbr": "SF", "color": "#E84040", "cat": "CRM", "score": "8.7", "price": "$25/mo", "best": "Enterprise CRM"},
    "mailchimp": {"name": "Mailchimp", "abbr": "MC", "color": "#FFE01B", "cat": "Email Marketing", "score": "7.9", "price": "Free / $13/mo", "best": "Beginners"},
}

def product_card(key):
    p = PRODUCTS[key]
    return f"""<div class="rev-card">
  <div class="rev-stripe" style="background:{p['color']};"></div>
  <div class="rev-body">
    <div class="rv-head">
      <div class="rv-logo" style="background:{p['color']};">{p['abbr']}</div>
      <div><div class="rv-name">{p['name']}</div><div class="rv-cat">{p['cat']}</div></div>
    </div>
    <div class="rv-score">
      <div class="rv-num">{p['score']}</div>
      <div><div class="rv-stars">★★★★★</div><div class="rv-cnt">Verified reviews</div></div>
    </div>
    <div class="rv-bars">
      <div class="rv-bar-row"><div class="rv-bar-lbl">Ease of Use</div><div class="rv-bar-track"><div class="rv-bar-fill" style="width:85%;"></div></div><div class="rv-bar-val">8.5</div></div>
      <div class="rv-bar-row"><div class="rv-bar-lbl">Features</div><div class="rv-bar-track"><div class="rv-bar-fill" style="width:88%;"></div></div><div class="rv-bar-val">8.8</div></div>
      <div class="rv-bar-row"><div class="rv-bar-lbl">Value</div><div class="rv-bar-track"><div class="rv-bar-fill" style="width:79%;"></div></div><div class="rv-bar-val">7.9</div></div>
    </div>
    <a href="review-template.html" class="rv-tag">Read Full Review →</a>
  </div>
</div>"""

def product_list_item(key, rank=1):
    p = PRODUCTS[key]
    return f"""<div class="cat-list-item">
  <div class="cat-list-logo" style="background:{p['color']};">{p['abbr']}</div>
  <div class="cat-list-info">
    <h3>#{rank} — {p['name']}</h3>
    <p>Placeholder description for {p['name']}. This content will be manually entered with a detailed summary of the tool's strengths, ideal use cases, and standout features for this category.</p>
    <div class="cat-list-tags">
      <span class="cc-tag">{p['best']}</span>
      <span class="cc-tag">{p['cat']}</span>
    </div>
  </div>
  <div class="cat-list-actions">
    <div class="cat-list-score">{p['score']}<span style="font-size:12px;color:var(--gray-mid);font-weight:400;">/10</span></div>
    <div class="cat-list-price">{p['price']}</div>
    <a href="review-template.html" class="btn-primary" style="font-size:12px;padding:8px 16px;">Read Review →</a>
  </div>
</div>"""


# ═══════════════════════════════════════════════════
# PAGE GENERATORS
# ═══════════════════════════════════════════════════

def build_homepage():
    return HEAD("Home") + ANNOUNCE_BAR + NAV() + """
<!-- Hero -->
<section class="hero">
  <div class="hero-inner">
  <div class="hero-left">
    <div class="hero-eyebrow"><div class="eyebrow-dot"></div> Independent B2B SaaS Reviews</div>
    <h1>Find the <span class="accent">Right Software.</span> Stop Guessing.</h1>
    <p class="hero-sub">Unbiased comparisons, detailed reviews, and honest breakdowns for 200+ B2B SaaS tools — so you can make confident buying decisions fast.</p>
    <div class="hero-actions">
      <a href="comparison-template.html" class="btn-primary">Browse Comparisons →</a>
      <a href="category-crm.html" class="btn-ghost">🔍 Search All Tools</a>
    </div>
    <div class="hero-social">
      <div class="s-avatars">
        <div class="s-avatar av1">MR</div>
        <div class="s-avatar av2">JK</div>
        <div class="s-avatar av3">ST</div>
        <div class="s-avatar av4">AL</div>
      </div>
      <div class="social-text"><strong>12,400+ readers</strong><br>making smarter software decisions</div>
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-card">
      <div class="hc-header">
        <div class="hc-title">Find Your Best Match</div>
        <div class="hc-badge">200+ Tools</div>
      </div>
      <div class="hc-search"><span>🔍</span><div class="hc-search-text">Search CRM, email, funnels…</div></div>
      <div class="hc-tags">
        <a href="category-crm.html" class="hc-tag on">CRM</a>
        <a href="category-email-marketing.html" class="hc-tag">Email</a>
        <a href="#" class="hc-tag">Funnels</a>
        <a href="#" class="hc-tag">Support</a>
        <a href="category-marketing-automation.html" class="hc-tag">Automation</a>
      </div>
      <div class="hc-items">
        <a href="review-template.html" class="hc-item"><div class="hc-ico" style="background:#E84040;">SF</div><div class="hc-meta"><div class="hc-name">Salesforce</div><div class="hc-cat">CRM</div></div><div class="hc-pill pill-amber">Enterprise</div></a>
        <a href="review-template.html" class="hc-item"><div class="hc-ico" style="background:#F97316;">HS</div><div class="hc-meta"><div class="hc-name">HubSpot</div><div class="hc-cat">CRM + Marketing</div></div><div class="hc-pill pill-green">Top Pick</div></a>
        <a href="review-template.html" class="hc-item"><div class="hc-ico" style="background:#8B5CF6;">AC</div><div class="hc-meta"><div class="hc-name">ActiveCampaign</div><div class="hc-cat">Email + Automation</div></div><div class="hc-pill pill-blue">Best Value</div></a>
        <a href="review-template.html" class="hc-item"><div class="hc-ico" style="background:#059669;">KJ</div><div class="hc-meta"><div class="hc-name">Kajabi</div><div class="hc-cat">Courses + Funnels</div></div><div class="hc-pill pill-blue">Trending</div></a>
      </div>
    </div>
  </div>
</section>

<!-- Category Bar -->
<div class="catbar">
  <div class="catbar-inner">
    <div class="cat-item on">All <span class="cat-cnt">200</span></div>
    <a href="category-crm.html" class="cat-item">CRM <span class="cat-cnt">38</span></a>
    <a href="category-email-marketing.html" class="cat-item">Email Marketing <span class="cat-cnt">29</span></a>
    <a href="category-marketing-automation.html" class="cat-item">Marketing Automation <span class="cat-cnt">24</span></a>
    <div class="cat-item">Sales &amp; Funnels <span class="cat-cnt">22</span></div>
    <div class="cat-item">Customer Support <span class="cat-cnt">18</span></div>
    <a href="comparison-template.html" class="cat-item">Comparisons <span class="cat-cnt">85</span></a>
    <a href="alternatives-template.html" class="cat-item">Alternatives <span class="cat-cnt">60</span></a>
    <div class="cat-item">Pricing <span class="cat-cnt">55</span></div>
  </div>
</div>

<!-- Featured Comparisons -->
<section class="section-full">
  <div style="max-width:1200px;margin:0 auto;padding:52px 36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Most Popular</div>
        <div class="sec-title">Head-to-Head Comparisons</div>
      </div>
      <a href="comparison-template.html" class="sec-link">View all comparisons →</a>
    </div>
    <div class="comp-grid">
      <a href="comparison-template.html" class="comp-card" style="text-decoration:none;">
        <div class="cc-top">
          <div class="vs-row"><div class="p-badge" style="background:#F97316;">HS</div><div class="vs-sep">VS</div><div class="p-badge" style="background:#8B5CF6;">AC</div></div>
          <div class="cc-meta"><div class="cc-reads">👁 14.2k reads</div><div class="cc-verdict">HubSpot Wins</div></div>
        </div>
        <div class="cc-body">
          <div class="cc-title">HubSpot vs ActiveCampaign — Which Is Better for SMBs in 2025?</div>
          <div class="cc-snip">HubSpot edges out ActiveCampaign for all-in-one simplicity, but ActiveCampaign is the smarter pick for pure email automation at lower cost.</div>
          <div class="cc-tags"><span class="cc-tag">CRM</span><span class="cc-tag">Email</span><span class="cc-tag">SMB</span></div>
        </div>
      </a>
      <a href="comparison-template.html" class="comp-card" style="text-decoration:none;">
        <div class="cc-top">
          <div class="vs-row"><div class="p-badge" style="background:#059669;">KJ</div><div class="vs-sep">VS</div><div class="p-badge" style="background:#DC2626;">CF</div></div>
          <div class="cc-meta"><div class="cc-reads">👁 11.7k reads</div><div class="cc-verdict">Depends on Use Case</div></div>
        </div>
        <div class="cc-body">
          <div class="cc-title">Kajabi vs ClickFunnels — Course Creators vs Funnel Builders</div>
          <div class="cc-snip">Kajabi is purpose-built for creators. ClickFunnels is better if your sole focus is sales funnels. The overlap is smaller than you'd think.</div>
          <div class="cc-tags"><span class="cc-tag">Funnels</span><span class="cc-tag">Courses</span><span class="cc-tag">Creators</span></div>
        </div>
      </a>
      <a href="comparison-template.html" class="comp-card" style="text-decoration:none;">
        <div class="cc-top">
          <div class="vs-row"><div class="p-badge" style="background:#0891B2;">ZD</div><div class="vs-sep">VS</div><div class="p-badge" style="background:#7C3AED;">IC</div></div>
          <div class="cc-meta"><div class="cc-reads">👁 8.9k reads</div><div class="cc-verdict">Zendesk for Scale</div></div>
        </div>
        <div class="cc-body">
          <div class="cc-title">Zendesk vs Intercom — The Support Platform Showdown</div>
          <div class="cc-snip">Zendesk leads in ticketing and enterprise scale. Intercom wins for conversational support and product-led growth companies.</div>
          <div class="cc-tags"><span class="cc-tag">Support</span><span class="cc-tag">Enterprise</span></div>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- Top Reviewed -->
<section class="section-full alt">
  <div style="max-width:1200px;margin:0 auto;padding:52px 36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Expert Reviews</div>
        <div class="sec-title">Top-Rated B2B SaaS Tools</div>
      </div>
      <a href="category-crm.html" class="sec-link">See all reviews →</a>
    </div>
    <div class="rev-grid">
""" + product_card("hubspot") + product_card("activecampaign") + product_card("kajabi") + product_card("clickfunnels") + """
    </div>
  </div>
</section>

<!-- Best-For Table -->
<section class="section-full">
  <div style="max-width:1200px;margin:0 auto;padding:52px 36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Quick Reference</div>
        <div class="sec-title">Best CRM Software at a Glance</div>
      </div>
      <a href="category-crm.html" class="sec-link">View full guide →</a>
    </div>
    <div class="bf-wrap">
      <table class="bf">
        <thead><tr><th>Software</th><th>Best For</th><th>Starting Price</th><th>Free Plan</th><th>Automation</th><th>Our Rating</th></tr></thead>
        <tbody>
          <tr>
            <td><div class="td-prod"><div class="td-ico" style="background:#F97316;">HS</div><div><div class="td-name">HubSpot</div><div class="td-cat">CRM + Marketing</div></div></div></td>
            <td><span class="bf-pill bf-pill-blue">All-in-One SMB</span></td>
            <td><span class="td-price">Free <small>/ $20/mo+</small></span></td>
            <td><span class="check">✓</span></td>
            <td><span class="check">✓</span></td>
            <td><span class="bf-pill bf-pill-green">9.1 / 10</span></td>
          </tr>
          <tr>
            <td><div class="td-prod"><div class="td-ico" style="background:#8B5CF6;">AC</div><div><div class="td-name">ActiveCampaign</div><div class="td-cat">Email + Auto</div></div></div></td>
            <td><span class="bf-pill bf-pill-blue">Email Automation</span></td>
            <td><span class="td-price">$29 <small>/mo</small></span></td>
            <td><span class="cross">—</span></td>
            <td><span class="check">✓</span></td>
            <td><span class="bf-pill bf-pill-green">8.8 / 10</span></td>
          </tr>
          <tr>
            <td><div class="td-prod"><div class="td-ico" style="background:#059669;">KJ</div><div><div class="td-name">Kajabi</div><div class="td-cat">Courses + Funnels</div></div></div></td>
            <td><span class="bf-pill bf-pill-blue">Course Creators</span></td>
            <td><span class="td-price">$69 <small>/mo</small></span></td>
            <td><span class="cross">—</span></td>
            <td><span class="check">✓</span></td>
            <td><span class="bf-pill bf-pill-amber">8.6 / 10</span></td>
          </tr>
          <tr>
            <td><div class="td-prod"><div class="td-ico" style="background:#DC2626;">CF</div><div><div class="td-name">ClickFunnels</div><div class="td-cat">Sales Funnels</div></div></div></td>
            <td><span class="bf-pill bf-pill-blue">Sales Funnels</span></td>
            <td><span class="td-price">$97 <small>/mo</small></span></td>
            <td><span class="cross">—</span></td>
            <td><span class="check">✓</span></td>
            <td><span class="bf-pill bf-pill-amber">8.3 / 10</span></td>
          </tr>
          <tr>
            <td><div class="td-prod"><div class="td-ico" style="background:#0891B2;">BR</div><div><div class="td-name">Brevo</div><div class="td-cat">Email Marketing</div></div></div></td>
            <td><span class="bf-pill bf-pill-blue">Budget Email</span></td>
            <td><span class="td-price">Free <small>/ $25/mo+</small></span></td>
            <td><span class="check">✓</span></td>
            <td><span class="check">✓</span></td>
            <td><span class="bf-pill bf-pill-amber">8.1 / 10</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

""" + FOOTER + CLOSE


def build_category_page(category_name, slug, nav_key, products_list, description):
    """Builds a category page template (CRM, Email Marketing, etc.) with review submission form."""
    content = HEAD(category_name) + ANNOUNCE_BAR + NAV(nav_key) + f"""
<!-- Category Hero -->
<div class="cat-hero">
  <div class="hero-inner">
  <div class="breadcrumb"><a href="index.html">Home</a><span>›</span><span>{category_name}</span></div>
  <h1>Best {category_name} Software<br><span style="color:var(--blue);">— 2025 Rankings & Reviews</span></h1>
  <p class="cat-hero-sub">{description}</p>
  <div class="cat-stats">
    <div class="cat-stat"><div class="cat-stat-num">{len(products_list)}</div><div class="cat-stat-lbl">Tools Reviewed</div></div>
    <div class="cat-stat"><div class="cat-stat-num">2,840+</div><div class="cat-stat-lbl">User Reviews</div></div>
    <div class="cat-stat"><div class="cat-stat-num">Monthly</div><div class="cat-stat-lbl">Updated</div></div>
  </div>
</div>

<!-- Filters -->
<div class="cat-filters">
  <span class="cat-filter-label">Filter by:</span>
  <button class="cat-filter-btn active">All</button>
  <button class="cat-filter-btn">Free Plan</button>
  <button class="cat-filter-btn">Best Value</button>
  <button class="cat-filter-btn">Enterprise</button>
  <button class="cat-filter-btn">Small Business</button>
  <button class="cat-filter-btn">Highest Rated</button>
</div>

<!-- Software Rankings -->
<section class="section-full">
  <div style="max-width:900px;margin:0 auto;padding:36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Expert Rankings</div>
        <div class="sec-title">Top {category_name} Tools for 2025</div>
      </div>
    </div>
    <div class="cat-list">
"""
    for i, key in enumerate(products_list):
        content += product_list_item(key, i+1)
    
    content += f"""
    </div>
  </div>
</section>

<!-- Quick Comparison Table -->
<section class="section-full alt">
  <div style="max-width:900px;margin:0 auto;padding:52px 36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Quick Reference</div>
        <div class="sec-title">{category_name} at a Glance</div>
      </div>
    </div>
    <div class="bf-wrap">
      <table class="bf">
        <thead><tr><th>Software</th><th>Best For</th><th>Starting Price</th><th>Free Plan</th><th>Our Rating</th></tr></thead>
        <tbody>
"""
    for key in products_list:
        p = PRODUCTS[key]
        has_free = "✓" if "Free" in p['price'] else "—"
        check_cls = "check" if has_free == "✓" else "cross"
        content += f"""          <tr>
            <td><div class="td-prod"><div class="td-ico" style="background:{p['color']};">{p['abbr']}</div><div><div class="td-name">{p['name']}</div></div></div></td>
            <td><span class="bf-pill bf-pill-blue">{p['best']}</span></td>
            <td><span class="td-price">{p['price']}</span></td>
            <td><span class="{check_cls}">{has_free}</span></td>
            <td><span class="bf-pill bf-pill-green">{p['score']} / 10</span></td>
          </tr>
"""
    
    content += """        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- Related Comparisons -->
<section class="section-full">
  <div style="max-width:900px;margin:0 auto;padding:52px 36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Head-to-Head</div>
        <div class="sec-title">Popular Comparisons</div>
      </div>
      <a href="comparison-template.html" class="sec-link">View all →</a>
    </div>
    <div class="comp-grid" style="grid-template-columns:repeat(2,1fr);">
      <a href="comparison-template.html" class="comp-card" style="text-decoration:none;">
        <div class="cc-top">
          <div class="vs-row"><div class="p-badge" style="background:#F97316;">HS</div><div class="vs-sep">VS</div><div class="p-badge" style="background:#8B5CF6;">AC</div></div>
          <div class="cc-meta"><div class="cc-reads">👁 14.2k reads</div><div class="cc-verdict">HubSpot Wins</div></div>
        </div>
        <div class="cc-body">
          <div class="cc-title">HubSpot vs ActiveCampaign — 2025</div>
          <div class="cc-snip">The all-in-one CRM vs the email automation specialist.</div>
        </div>
      </a>
      <a href="comparison-template.html" class="comp-card" style="text-decoration:none;">
        <div class="cc-top">
          <div class="vs-row"><div class="p-badge" style="background:#F97316;">HS</div><div class="vs-sep">VS</div><div class="p-badge" style="background:#E84040;">SF</div></div>
          <div class="cc-meta"><div class="cc-reads">👁 18.1k reads</div><div class="cc-verdict">Depends on Size</div></div>
        </div>
        <div class="cc-body">
          <div class="cc-title">HubSpot vs Salesforce — 2025</div>
          <div class="cc-snip">SMB favorite vs enterprise standard. Which fits your team?</div>
        </div>
      </a>
    </div>
  </div>
</section>
"""
    
    content += REVIEW_FORM(category_name + " Tools")
    content += FOOTER + REVIEW_FORM_JS + CLOSE
    return content


def build_comparison_page():
    return HEAD("HubSpot vs ActiveCampaign — 2025 Comparison") + ANNOUNCE_BAR + NAV("comparisons") + """
<div class="detail-hero">
  <div class="breadcrumb"><a href="index.html">Home</a><span>›</span><a href="comparison-template.html">Comparisons</a><span>›</span><span>HubSpot vs ActiveCampaign</span></div>
  <div class="detail-title">HubSpot vs ActiveCampaign<br>— 2025 In-Depth Comparison</div>
  <div class="detail-meta">
    <div class="dm-item">📅 Updated Jan 2025</div><div class="dm-dot"></div>
    <div class="dm-item">⏱ 12 min read</div><div class="dm-dot"></div>
    <div class="dm-item">👁 14,200 readers</div><div class="dm-dot"></div>
    <div class="dm-item">✍️ The SaaS Source Team</div>
  </div>
  <div class="verdict-box">
    <div class="vb-icon">🏆</div>
    <div class="vb-text"><strong>Quick Verdict:</strong> HubSpot wins for all-in-one CRM + marketing at scale. ActiveCampaign is the better pick if email automation depth and value are your priorities.</div>
  </div>
</div>

<div class="detail-content">
  <div class="detail-main">
    <div class="sec-eyebrow" style="margin-bottom:12px;">Feature Breakdown</div>
    <div class="cmp-table-wrap">
      <table class="cmp">
        <thead><tr><th>Feature</th><th class="p1">HubSpot</th><th class="p2">ActiveCampaign</th></tr></thead>
        <tbody>
          <tr><td class="feature-cell">Free Plan</td><td class="win">✓ Yes (generous)</td><td class="lose">✗ No</td></tr>
          <tr><td class="feature-cell">Built-in CRM</td><td class="win">✓ Full CRM</td><td class="lose">Basic CRM add-on</td></tr>
          <tr><td class="feature-cell">Email Automation</td><td>Solid (visual)</td><td class="win">✓ Industry-leading</td></tr>
          <tr><td class="feature-cell">Landing Pages</td><td class="win">✓ Native builder</td><td>Limited</td></tr>
          <tr><td class="feature-cell">A/B Testing</td><td>Paid tiers only</td><td class="win">✓ All plans</td></tr>
          <tr><td class="feature-cell">Reporting</td><td class="win">✓ Advanced dashboards</td><td>Standard</td></tr>
          <tr><td class="feature-cell">Starting Price</td><td class="win">Free / $20/mo</td><td>$29/mo</td></tr>
          <tr><td class="feature-cell">Integrations</td><td class="win">✓ 1,000+</td><td>900+</td></tr>
          <tr><td class="feature-cell">Deliverability</td><td>Good</td><td class="win">✓ Excellent</td></tr>
        </tbody>
      </table>
    </div>

    <div class="sec-eyebrow" style="margin-bottom:12px;">Who Should Choose Each</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px;">
      <div style="background:var(--blue-pale);border:1px solid var(--blue-mid);border-radius:var(--radius-lg);padding:20px;">
        <div style="font-family:'Syne',sans-serif;font-size:15px;font-weight:700;color:var(--blue);margin-bottom:12px;">✓ Choose HubSpot if…</div>
        <div style="font-size:13px;color:#404050;line-height:1.7;">
          • You need a full CRM + marketing platform<br>
          • Your team is non-technical<br>
          • You want a free plan to start<br>
          • You're scaling a sales + marketing org<br>
          • You want an all-in-one ecosystem
        </div>
      </div>
      <div style="background:#F5F0FF;border:1px solid #C4B5FD;border-radius:var(--radius-lg);padding:20px;">
        <div style="font-family:'Syne',sans-serif;font-size:15px;font-weight:700;color:#7B4FD4;margin-bottom:12px;">✓ Choose ActiveCampaign if…</div>
        <div style="font-size:13px;color:#404050;line-height:1.7;">
          • Email automation depth is your #1 need<br>
          • You want better value at lower tiers<br>
          • You rely on advanced segmentation<br>
          • You need superior deliverability<br>
          • You're an e-commerce or creator business
        </div>
      </div>
    </div>

    <!-- Placeholder for long-form comparison content -->
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
    </div>
  </div>
  <div class="detail-sticky">
    <div class="cta-card">
      <h3>Try HubSpot Free</h3>
      <p>No credit card needed. Full CRM + marketing tools on the free plan.</p>
      <a href="#" class="cta-btn cta-btn-blue">Get HubSpot Free →</a>
      <a href="review-template.html" class="cta-btn cta-btn-ghost">Read Full Review</a>
      <div class="cta-note">Affiliate link — we may earn a commission</div>
    </div>
    <div class="cta-card" style="background:var(--gray-50);border:1px solid var(--gray-200);">
      <h3 style="color:var(--ink);">Try ActiveCampaign</h3>
      <p style="color:#606070;">14-day free trial. No credit card required.</p>
      <a href="#" class="cta-btn" style="background:#8B5CF6;color:white;">Start Free Trial →</a>
    </div>
  </div>
</div>

""" + FOOTER + CLOSE


def build_review_page():
    p = PRODUCTS["hubspot"]
    return HEAD(f"{p['name']} Review 2025") + ANNOUNCE_BAR + NAV("crm") + f"""
<div class="detail-hero" style="display:grid;grid-template-columns:1fr auto;gap:36px;align-items:start;">
  <div>
    <div class="breadcrumb"><a href="index.html">Home</a><span>›</span><a href="category-crm.html">CRM Software</a><span>›</span><span>HubSpot Review</span></div>
    <div class="detail-title" style="font-size:32px;">HubSpot Review 2025<br><span style="color:var(--blue);">The All-in-One CRM Powerhouse</span></div>
    <div class="detail-meta">
      <div class="dm-item">📅 Updated Jan 2025</div><div class="dm-dot"></div>
      <div class="dm-item">⏱ 15 min read</div><div class="dm-dot"></div>
      <div class="dm-item">👁 28,400 readers</div>
    </div>
  </div>
  <!-- At a Glance Box -->
  <div style="background:white;border:1px solid var(--gray-200);border-radius:var(--radius-lg);padding:20px;min-width:240px;box-shadow:var(--shadow-md);">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
      <div style="width:48px;height:48px;background:{p['color']};border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-weight:800;font-size:18px;color:white;">{p['abbr']}</div>
      <div>
        <div style="font-weight:700;font-size:16px;color:var(--ink);">{p['name']}</div>
        <div style="font-size:12px;color:var(--gray-mid);">{p['cat']}</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="font-family:'Syne',sans-serif;font-size:36px;font-weight:800;color:var(--ink);line-height:1;">{p['score']}</div>
      <div><div style="color:#E8A020;font-size:14px;">★★★★★</div><div style="font-size:11px;color:var(--gray-mid);">2,840 verified reviews</div></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:16px;font-size:12px;">
      <div style="display:flex;justify-content:space-between;"><span style="color:var(--gray-mid);">Starting Price</span><strong>{p['price']}</strong></div>
      <div style="display:flex;justify-content:space-between;"><span style="color:var(--gray-mid);">Free Plan</span><strong style="color:var(--green);">✓ Yes</strong></div>
      <div style="display:flex;justify-content:space-between;"><span style="color:var(--gray-mid);">Best For</span><strong>{p['best']}</strong></div>
    </div>
    <a href="#" class="cta-btn cta-btn-blue" style="margin-bottom:8px;">Try HubSpot Free →</a>
    <div style="font-size:11px;color:var(--gray-mid);text-align:center;">No credit card required</div>
  </div>
</div>

<div class="detail-content">
  <div class="detail-main">
    <!-- Pros/Cons -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px;">
      <div style="background:#E8F8EE;border:1px solid #86EFAC;border-radius:var(--radius-lg);padding:20px;">
        <div style="font-weight:700;font-size:14px;color:var(--green);margin-bottom:12px;">✓ Pros</div>
        <div style="font-size:13px;color:#404050;line-height:1.8;">
          • Generous free plan with real CRM tools<br>
          • Extremely user-friendly interface<br>
          • All-in-one marketing + sales + service<br>
          • 1,000+ app integrations<br>
          • Best-in-class reporting dashboards
        </div>
      </div>
      <div style="background:#FEF2F2;border:1px solid #FCA5A5;border-radius:var(--radius-lg);padding:20px;">
        <div style="font-weight:700;font-size:14px;color:var(--red);margin-bottom:12px;">✗ Cons</div>
        <div style="font-size:13px;color:#404050;line-height:1.8;">
          • Pricing jumps sharply at higher tiers<br>
          • Advanced automation costs more<br>
          • Annual contracts at paid tiers<br>
          • Can feel bloated for simple use cases<br>
          • Add-on costs add up quickly
        </div>
      </div>
    </div>

    <!-- Long form review content placeholder -->
    <div class="prose">
      <h2>Overview</h2>
      <p><em>[Comprehensive overview of HubSpot — what it is, who it's for, and why it matters in 2025. This content will be manually entered with detailed, original analysis.]</em></p>
      
      <h2>Pricing</h2>
      <p><em>[Detailed pricing breakdown with tier analysis, hidden costs, and value assessment]</em></p>
      
      <h2>Features Deep Dive</h2>
      <h3>CRM & Contact Management</h3>
      <p><em>[Feature analysis content]</em></p>
      
      <h3>Marketing Hub</h3>
      <p><em>[Feature analysis content]</em></p>
      
      <h3>Sales Hub</h3>
      <p><em>[Feature analysis content]</em></p>
      
      <h3>Service Hub</h3>
      <p><em>[Feature analysis content]</em></p>
      
      <h2>User Experience</h2>
      <p><em>[UI/UX analysis with screenshots]</em></p>
      
      <h2>Integrations</h2>
      <p><em>[Integration ecosystem analysis]</em></p>
      
      <h2>Customer Support</h2>
      <p><em>[Support quality analysis]</em></p>
      
      <h2>Final Verdict</h2>
      <p><em>[Summary recommendation with clear "who should buy" guidance]</em></p>
    </div>

    <!-- User Reviews Section -->
    <div style="margin-top:48px;">
      <div class="sec-eyebrow">Community</div>
      <div class="sec-title" style="margin-bottom:24px;">User Reviews</div>
      
      <!-- Sample user review -->
      <div style="background:white;border:1px solid var(--gray-100);border-radius:var(--radius-lg);padding:20px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
          <div>
            <div style="font-weight:600;color:var(--ink);">Sarah M.</div>
            <div style="font-size:11px;color:var(--gray-mid);">Marketing Director · 51-200 employees</div>
          </div>
          <div style="color:#E8A020;">★★★★★</div>
        </div>
        <div style="font-weight:600;color:var(--ink);margin-bottom:6px;">"Transformed our marketing operations"</div>
        <p style="font-size:13px;color:#606070;line-height:1.6;"><em>[Sample user review content — real reviews will be collected through the submission form below]</em></p>
      </div>
      
      <div style="background:white;border:1px solid var(--gray-100);border-radius:var(--radius-lg);padding:20px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
          <div>
            <div style="font-weight:600;color:var(--ink);">James T.</div>
            <div style="font-size:11px;color:var(--gray-mid);">CEO · 1-10 employees</div>
          </div>
          <div style="color:#E8A020;">★★★★☆</div>
        </div>
        <div style="font-weight:600;color:var(--ink);margin-bottom:6px;">"Great free plan, but paid tiers are pricey"</div>
        <p style="font-size:13px;color:#606070;line-height:1.6;"><em>[Sample user review content]</em></p>
      </div>
    </div>
  </div>
  <div class="detail-sticky">
    <div class="cta-card">
      <h3>Try HubSpot Free</h3>
      <p>No credit card needed. Full CRM + marketing tools on the free plan.</p>
      <a href="#" class="cta-btn cta-btn-blue">Get HubSpot Free →</a>
      <div class="cta-note">Affiliate link — we may earn a commission</div>
    </div>
    <div class="cta-card" style="background:var(--gray-50);border:1px solid var(--gray-200);">
      <h3 style="color:var(--ink);">Compare Alternatives</h3>
      <p style="color:#606070;">See how HubSpot stacks up against the competition.</p>
      <a href="comparison-template.html" class="cta-btn" style="background:var(--ink);color:white;">HubSpot vs ActiveCampaign →</a>
      <a href="alternatives-template.html" class="cta-btn cta-btn-ghost">View All Alternatives →</a>
    </div>
    <div style="background:white;border:1px solid var(--gray-200);border-radius:var(--radius-lg);padding:16px;margin-top:4px;">
      <a href="#submit-review" style="display:block;text-align:center;font-size:13px;font-weight:600;color:var(--blue);">✍️ Write a Review →</a>
    </div>
  </div>
</div>

""" + REVIEW_FORM(p['name']) + FOOTER + REVIEW_FORM_JS + CLOSE


def build_alternatives_page():
    return HEAD("Best HubSpot Alternatives 2025") + ANNOUNCE_BAR + NAV("alternatives") + """
<div class="detail-hero">
  <div class="breadcrumb"><a href="index.html">Home</a><span>›</span><a href="#">Alternatives</a><span>›</span><span>HubSpot Alternatives</span></div>
  <div class="detail-title">Best HubSpot Alternatives<br><span style="color:var(--blue);">2025 Expert Picks</span></div>
  <div class="detail-meta">
    <div class="dm-item">📅 Updated Jan 2025</div><div class="dm-dot"></div>
    <div class="dm-item">⏱ 10 min read</div><div class="dm-dot"></div>
    <div class="dm-item">👁 12,300 readers</div>
  </div>
  <div class="verdict-box">
    <div class="vb-icon">💡</div>
    <div class="vb-text"><strong>Why look beyond HubSpot?</strong> While HubSpot is a top all-in-one CRM, its pricing escalates quickly. These alternatives may be better fits depending on your specific needs and budget.</div>
  </div>
</div>

<section class="section-full">
  <div style="max-width:1000px;margin:0 auto;padding:48px 36px;">
    <div class="sec-head">
      <div>
        <div class="sec-eyebrow">Top Picks</div>
        <div class="sec-title">HubSpot Alternatives at a Glance</div>
      </div>
    </div>
    <div class="alts-grid">
""" + "".join([f"""      <a href="review-template.html" class="alt-card" style="text-decoration:none;">
        <div class="alt-ico" style="background:{PRODUCTS[k]['color']};">{PRODUCTS[k]['abbr']}</div>
        <div class="alt-info">
          <div class="alt-name">{PRODUCTS[k]['name']}</div>
          <div class="alt-desc">Placeholder description — ideal alternative for specific use cases. Content to be manually entered.</div>
          <div class="alt-bottom">
            <span class="alt-price">{PRODUCTS[k]['price']}</span>
            <span class="alt-rating"><span class="alt-stars">★★★★★</span><span class="alt-score">{PRODUCTS[k]['score']}</span></span>
          </div>
        </div>
      </a>
""" for k in ["activecampaign", "salesforce", "kajabi", "brevo", "zendesk", "intercom"]]) + """
    </div>
  </div>
</section>

<!-- Detailed Alternative Breakdown -->
<section class="section-full alt">
  <div style="max-width:720px;margin:0 auto;padding:48px 36px;">
    <div class="prose">
      <h2>Choosing the Right HubSpot Alternative</h2>
      <p><em>[Long-form content analyzing each alternative in detail, with specific recommendations based on use case, team size, and budget. This content will be manually entered.]</em></p>
      
      <h3>Best for Email Automation: ActiveCampaign</h3>
      <p><em>[Detailed analysis]</em></p>
      
      <h3>Best for Enterprise: Salesforce</h3>
      <p><em>[Detailed analysis]</em></p>
      
      <h3>Best for Course Creators: Kajabi</h3>
      <p><em>[Detailed analysis]</em></p>
      
      <h3>Best Budget Option: Brevo</h3>
      <p><em>[Detailed analysis]</em></p>
      
      <h2>Final Recommendations</h2>
      <p><em>[Summary with clear guidance on which alternative to choose based on specific needs]</em></p>
    </div>
  </div>
</section>

""" + FOOTER + CLOSE


def build_simple_page(title, nav_active, body_content):
    """Builds a simple content page (About, Contact, Privacy, etc.)"""
    return HEAD(title) + NAV() + f"""
<div class="page-hero">
  <h1>{title}</h1>
</div>
<div class="page-content">
{body_content}
</div>
""" + FOOTER + CLOSE


# ─── COMPLIANCE/INFO PAGES ───

ABOUT_CONTENT = """
<div class="prose" style="max-width:720px;">
  <h2>About The SaaS Source</h2>
  <p>The SaaS Source is an independent B2B software review platform built to help businesses make smarter software buying decisions. We provide unbiased comparisons, in-depth reviews, and honest analysis of 200+ SaaS tools.</p>
  
  <h2>Our Mission</h2>
  <p>We believe choosing the right software shouldn't require weeks of research, confusing demos, or trusting paid placement. Our mission is to provide clear, honest, research-backed guidance so you can find the right tool fast.</p>
  
  <h2 id="methodology">How We Review</h2>
  <p>Every review on The SaaS Source follows a rigorous, standardized methodology:</p>
  <ul>
    <li><strong>Hands-on testing:</strong> We sign up for and use every product we review.</li>
    <li><strong>Feature scoring:</strong> We evaluate ease of use, features, value, support, and integrations on a 10-point scale.</li>
    <li><strong>User feedback:</strong> We collect and verify real user reviews to supplement our expert analysis.</li>
    <li><strong>Regular updates:</strong> Reviews are refreshed at least quarterly to reflect pricing and feature changes.</li>
    <li><strong>Transparency:</strong> We clearly disclose affiliate relationships and never let them influence our ratings.</li>
  </ul>
  
  <h2>Who We Are</h2>
  <p>The SaaS Source is a property of Nomad Design Holdings, LLC. Our team consists of SaaS industry researchers, content strategists, and technology analysts who live and breathe B2B software.</p>
  
  <h2>Contact Us</h2>
  <p>Have questions, feedback, or want to suggest a tool for review? <a href="contact.html">Get in touch</a>.</p>
</div>
"""

CONTACT_CONTENT = """
<div class="contact-grid" style="max-width:900px;">
  <div class="contact-info">
    <h3>Get in Touch</h3>
    <p>Have a question about a review? Want to suggest a tool for coverage? Found an error? We'd love to hear from you.</p>
    
    <h3 style="margin-top:32px;">What We Can Help With</h3>
    <p>
      <strong>Editorial inquiries:</strong> Review requests, corrections, or content partnerships.<br><br>
      <strong>Business inquiries:</strong> Advertising, sponsorship, or partnership opportunities.<br><br>
      <strong>General feedback:</strong> Suggestions, ideas, or just to say hello.
    </p>
    
    <h3 style="margin-top:32px;">Response Time</h3>
    <p>We aim to respond to all inquiries within 1-2 business days.</p>
  </div>
  <div>
    <div style="background:var(--gray-50);border:1px solid var(--gray-100);border-radius:var(--radius-lg);padding:28px;">
      <div class="form-row">
        <label for="contact-name">Name *</label>
        <input type="text" id="contact-name" placeholder="Your name">
      </div>
      <div class="form-row">
        <label for="contact-email">Email *</label>
        <input type="email" id="contact-email" placeholder="you@example.com">
      </div>
      <div class="form-row">
        <label for="contact-subject">Subject</label>
        <select id="contact-subject">
          <option>General Inquiry</option>
          <option>Review Request</option>
          <option>Correction / Update</option>
          <option>Business Partnership</option>
          <option>Other</option>
        </select>
      </div>
      <div class="form-row">
        <label for="contact-message">Message *</label>
        <textarea id="contact-message" placeholder="How can we help?"></textarea>
      </div>
      <button class="btn-primary" style="width:100%;justify-content:center;">Send Message →</button>
    </div>
  </div>
</div>
"""

PRIVACY_CONTENT = """
<div class="prose" style="max-width:720px;">
  <p><em>Last updated: January 2025</em></p>
  
  <h2>Privacy Policy</h2>
  <p>This Privacy Policy describes how Nomad Design Holdings, LLC ("The SaaS Source," "we," "us," or "our") collects, uses, and shares information when you visit thesaassource.co (the "Site").</p>
  
  <h2>Information We Collect</h2>
  <h3>Information You Provide</h3>
  <p>We collect information you voluntarily provide, including: name and email when submitting reviews or contact forms, and any other information you choose to share.</p>
  
  <h3>Automatically Collected Information</h3>
  <p>When you visit the Site, we automatically collect certain information, including: IP address, browser type, device type, pages visited, time spent on pages, and referring URLs. We collect this data through Google Analytics 4 and similar tools.</p>
  
  <h2>How We Use Your Information</h2>
  <p>We use information to: operate and improve the Site, respond to inquiries, publish verified reviews, analyze Site traffic and performance, and comply with legal obligations.</p>
  
  <h2>Cookies and Tracking</h2>
  <p>We use cookies and similar technologies for analytics and to support affiliate link tracking. Third-party services (Google Analytics, affiliate networks) may place their own cookies. You can control cookies through your browser settings.</p>
  
  <h2>Affiliate Links</h2>
  <p>Our Site contains affiliate links. When you click these links and make a purchase, we may earn a commission. Affiliate partners may use cookies to track referrals. See our <a href="affiliate-disclosure.html">Affiliate Disclosure</a> for details.</p>
  
  <h2>Data Sharing</h2>
  <p>We do not sell your personal information. We may share data with: analytics providers (Google), affiliate networks, and as required by law.</p>
  
  <h2>Your Rights</h2>
  <p>Depending on your jurisdiction, you may have rights to access, correct, delete, or export your personal data. Contact us at <a href="contact.html">our contact page</a> to exercise these rights.</p>
  
  <h2>Changes to This Policy</h2>
  <p>We may update this policy periodically. The "Last updated" date reflects the most recent revision.</p>
  
  <h2>Contact</h2>
  <p>For privacy-related inquiries, please visit our <a href="contact.html">contact page</a>.</p>
</div>
"""

AFFILIATE_CONTENT = """
<div class="prose" style="max-width:720px;">
  <p><em>Last updated: January 2025</em></p>
  
  <h2>Affiliate Disclosure</h2>
  <p>The SaaS Source (thesaassource.co) is a property of Nomad Design Holdings, LLC. We participate in affiliate marketing programs, which means we may earn commissions when you click our links and make purchases.</p>
  
  <h2>How Affiliate Links Work</h2>
  <p>Throughout our Site, you'll find links to software products and services. Many of these are affiliate links, identifiable by the <code>/go/</code> prefix in the URL (e.g., thesaassource.co/go/hubspot). When you click one of these links and subsequently sign up for or purchase the product, we may receive a commission from the software provider at no additional cost to you.</p>
  
  <h2>Our Editorial Independence</h2>
  <p><strong>Affiliate relationships never influence our ratings, rankings, or recommendations.</strong> Our editorial process is completely independent from our revenue model. Products are evaluated on their merits using our standardized review methodology. We will always recommend the best tool for your needs, even if it pays a lower (or no) commission.</p>
  
  <h2>Why We Use Affiliate Links</h2>
  <p>Affiliate commissions help us fund the research, writing, and maintenance of this Site. This model allows us to provide free, high-quality content to our readers without requiring subscriptions or paywalls.</p>
  
  <h2>Programs We Participate In</h2>
  <p>We participate in affiliate programs offered by various B2B SaaS companies, including (but not limited to): HubSpot, ActiveCampaign, ClickFunnels, Kajabi, Zendesk, Intercom, Brevo, and programs available through PartnerStack and other affiliate networks.</p>
  
  <h2>Questions?</h2>
  <p>If you have questions about our affiliate relationships, please <a href="contact.html">contact us</a>.</p>
</div>
"""

TERMS_CONTENT = """
<div class="prose" style="max-width:720px;">
  <p><em>Last updated: January 2025</em></p>
  
  <h2>Terms of Use</h2>
  <p>These Terms of Use govern your use of thesaassource.co (the "Site"), operated by Nomad Design Holdings, LLC ("we," "us," or "our"). By using the Site, you agree to these terms.</p>
  
  <h2>Content and Accuracy</h2>
  <p>We strive to provide accurate, up-to-date information. However, software products change frequently and our information may not always reflect the very latest changes. We encourage you to verify pricing, features, and other details directly with software providers before making purchasing decisions.</p>
  
  <h2>Reviews and User Content</h2>
  <p>Users may submit reviews through our review forms. By submitting a review, you: confirm the review reflects your honest experience, grant us a non-exclusive license to publish the review, agree not to submit false, misleading, or defamatory content, and understand that reviews may be moderated before publication.</p>
  <p>We reserve the right to edit or remove reviews that violate these terms or are otherwise inappropriate.</p>
  
  <h2>Affiliate Links</h2>
  <p>Our Site contains affiliate links. See our <a href="affiliate-disclosure.html">Affiliate Disclosure</a> for details. We are not responsible for the products, services, or practices of third-party companies linked from our Site.</p>
  
  <h2>Intellectual Property</h2>
  <p>All original content on this Site (text, design, graphics, logos) is owned by Nomad Design Holdings, LLC and protected by copyright. Software names, logos, and trademarks belong to their respective owners.</p>
  
  <h2>Limitation of Liability</h2>
  <p>The SaaS Source is provided "as is" without warranties. We are not liable for any damages arising from your use of the Site or reliance on our content. Software purchasing decisions are made at your own risk.</p>
  
  <h2>Changes to These Terms</h2>
  <p>We may update these terms at any time. Continued use of the Site constitutes acceptance of updated terms.</p>
  
  <h2>Contact</h2>
  <p>Questions about these terms? Please <a href="contact.html">contact us</a>.</p>
</div>
"""


# ═══════════════════════════════════════════════════
# BUILD ALL PAGES
# ═══════════════════════════════════════════════════

def main():
    pages = {
        "index.html": build_homepage(),
        
        # Category pages (custom post templates with review forms)
        "category-crm.html": build_category_page(
            "CRM", "crm", "crm",
            ["hubspot", "salesforce", "activecampaign", "brevo"],
            "Comprehensive, unbiased reviews and rankings of the best CRM software for businesses of every size. Updated monthly with real user feedback."
        ),
        "category-email-marketing.html": build_category_page(
            "Email Marketing", "email-marketing", "email",
            ["activecampaign", "brevo", "mailchimp", "hubspot"],
            "Expert analysis of the top email marketing platforms. Compare features, pricing, and deliverability to find your perfect fit."
        ),
        "category-marketing-automation.html": build_category_page(
            "Marketing Automation", "marketing-automation", "automation",
            ["hubspot", "activecampaign", "brevo", "clickfunnels"],
            "Find the best marketing automation tools to scale your campaigns. In-depth reviews covering workflows, integrations, and ROI."
        ),
        
        # Content templates
        "comparison-template.html": build_comparison_page(),
        "review-template.html": build_review_page(),
        "alternatives-template.html": build_alternatives_page(),
        
        # Compliance & info pages
        "about.html": build_simple_page("About Us", "", ABOUT_CONTENT),
        "contact.html": build_simple_page("Contact", "", CONTACT_CONTENT),
        "privacy-policy.html": build_simple_page("Privacy Policy", "", PRIVACY_CONTENT),
        "affiliate-disclosure.html": build_simple_page("Affiliate Disclosure", "", AFFILIATE_CONTENT),
        "terms-of-use.html": build_simple_page("Terms of Use", "", TERMS_CONTENT),
    }
    
    for filename, content in pages.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  ✓ Built {filename}")
    
    print(f"\n  Total: {len(pages)} pages generated")
    print(f"  Output: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()

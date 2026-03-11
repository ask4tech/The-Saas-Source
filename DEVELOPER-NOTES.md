# The SaaS Source — Developer Build Reference

**Site:** thesaassource.co  
**Owner:** Nomad Design Holdings, LLC  
**Version:** v1.0  

---

## 📁 File Structure

```
thesaassource/
├── css/
│   └── styles.css              ← Shared global stylesheet (design system)
├── build.py                    ← Site generator script (Python)
├── index.html                  ← Homepage
├── category-crm.html           ← Category template: CRM Software
├── category-email-marketing.html ← Category template: Email Marketing
├── category-marketing-automation.html ← Category template: Marketing Automation
├── comparison-template.html    ← Comparison page template (HubSpot vs ActiveCampaign)
├── review-template.html        ← Individual review page template (HubSpot)
├── alternatives-template.html  ← Alternatives page template (HubSpot Alternatives)
├── about.html                  ← About Us
├── contact.html                ← Contact page with form
├── privacy-policy.html         ← Privacy Policy
├── affiliate-disclosure.html   ← Affiliate Disclosure
├── terms-of-use.html           ← Terms of Use
└── DEVELOPER-NOTES.md          ← This file
```

---

## 🎨 Design System

### Colors (CSS Custom Properties)
- **Primary Blue:** `#3C82C8` (--blue)
- **Dark Blue:** `#2D6AAF` (--blue-dark)
- **Pale Blue:** `#EBF3FB` (--blue-pale)
- **Mid Blue:** `#C2D9F0` (--blue-mid)
- **Ink/Black:** `#1E1E1E` (--ink)
- **Charcoal:** `#3C3C3C` (--charcoal)
- **Green (success):** `#27AE60`
- **Amber (warning):** `#E67E22`
- **Red (error):** `#E74C3C`

### Typography
- **Headings:** [Roboto](https://fonts.google.com/specimen/Roboto) (900, 700, 500)
- **Body:** [DM Sans](https://fonts.google.com/specimen/DM+Sans) (300-600)

### Spacing & Layout
- Container max-width: `1200px`
- Section padding: `52px 36px`
- Border radius: `8px` (standard), `14px` (large)

---

## 🏗️ WordPress Conversion Guide

### Recommended Stack (from Developer Build Brief)
- **CMS:** WordPress (latest stable)
- **Theme:** GeneratePress + GP Premium (or Astra as fallback)
- **Editor:** Gutenberg Block Editor
- **SEO:** Rank Math
- **Analytics:** Google Site Kit (GA4 + Search Console)
- **Affiliate Links:** Pretty Links (prefix: `/go/`)
- **Caching:** WP Rocket or host-provided

### Page → WordPress Mapping

| Static HTML | WordPress Implementation |
|---|---|
| `index.html` | Front page (custom page template or blocks) |
| `category-*.html` | **Custom Post Type archive template** — Category taxonomy archive with custom query |
| `review-template.html` | **Custom Post Type: `review`** — Single post template |
| `comparison-template.html` | **Custom Post Type: `comparison`** — Single post template |
| `alternatives-template.html` | **Custom Post Type: `alternative`** — Single post template |
| `about.html` | Standard WordPress page |
| `contact.html` | Standard WordPress page (use WPForms or Gravity Forms) |
| `privacy-policy.html` | Standard WordPress page |
| `affiliate-disclosure.html` | Standard WordPress page |
| `terms-of-use.html` | Standard WordPress page |

### Custom Post Types to Create

#### 1. Reviews (`review`)
- **Slug:** `/reviews/`
- **Custom Fields (ACF or custom meta):**
  - `software_name` (text)
  - `software_abbreviation` (text, 2 chars)
  - `software_color` (color picker)
  - `category` (taxonomy: `software-category`)
  - `overall_score` (number, 0-10)
  - `ease_of_use_score` (number, 0-10)
  - `features_score` (number, 0-10)
  - `value_score` (number, 0-10)
  - `support_score` (number, 0-10)
  - `starting_price` (text)
  - `has_free_plan` (boolean)
  - `best_for` (text)
  - `affiliate_url` (URL — use Pretty Links /go/ slug)
  - `pros` (repeater/list)
  - `cons` (repeater/list)
  - `verdict_summary` (textarea)

#### 2. Comparisons (`comparison`)
- **Slug:** `/comparisons/`
- **Custom Fields:**
  - `product_1` (relationship → Review post)
  - `product_2` (relationship → Review post)
  - `winner` (select: product_1 / product_2 / tie)
  - `verdict` (textarea)
  - `feature_comparison` (repeater: feature, product_1_value, product_2_value, winner)
  - `read_count` (number, for display)

#### 3. Alternatives (`alternative`)
- **Slug:** `/alternatives/`
- **Custom Fields:**
  - `primary_product` (relationship → Review post)
  - `alternative_products` (relationship → multiple Review posts)
  - `why_look_beyond` (textarea)

#### 4. User Reviews (`user-review`)
- **Slug:** N/A (not public, managed via admin)
- **Custom Fields:**
  - `reviewed_product` (relationship → Review post)
  - `reviewer_name` (text)
  - `reviewer_email` (email, private)
  - `company_name` (text)
  - `company_size` (select)
  - `role` (text)
  - `overall_rating` (number, 1-5)
  - `ease_of_use_rating` (number, 1-5)
  - `features_rating` (number, 1-5)
  - `value_rating` (number, 1-5)
  - `review_title` (text)
  - `pros` (textarea)
  - `cons` (textarea)
  - `use_case` (textarea)
  - `status` (select: pending / approved / rejected)

### Taxonomy: Software Categories
| Name | Slug |
|---|---|
| CRM Software | `crm` |
| Email Marketing | `email-marketing` |
| Marketing Automation | `marketing-automation` |
| Sales & Funnels | `sales-funnels` |
| Customer Support | `customer-support` |

### Category Pages (Custom Post Templates)
The **category pages** (`category-crm.html`, etc.) should be implemented as **taxonomy archive templates** in WordPress. Key elements:
1. **Category Hero** — Dynamic title, description, tool count
2. **Filter Bar** — Client-side filtering (JS) or AJAX-powered
3. **Ranked Software List** — Query reviews by category, ordered by score
4. **Quick Comparison Table** — Auto-generated from review custom fields
5. **Related Comparisons** — Query comparisons that include category products
6. **Review Submission Form** — See form section below

### Review Submission Form
The review form appears on:
- **Category pages** (bottom of page)
- **Individual review pages** (bottom of page)

**Implementation options:**
1. **WPForms / Gravity Forms** — Create form, map fields to User Review CPT
2. **Custom REST API endpoint** — Build a custom form handler
3. **ACF Front-End Form** — Use ACF's form functionality

**Requirements:**
- Form submits create a `user-review` post with `status: pending`
- Admin gets email notification of new reviews
- Admin approves/rejects in WordPress admin
- Approved reviews display on the corresponding review page
- Star rating inputs use the CSS/JS pattern from the templates

---

## 🔗 Navigation Structure

### Primary Navigation (Header)
- CRM Software → `/crm/`
- Email Marketing → `/email-marketing/`
- Marketing Automation → `/marketing-automation/`
- Sales & Funnels → `/sales-funnels/`
- Support → `/customer-support/`
- Comparisons → `/comparisons/`
- Alternatives → `/alternatives/`

### Footer Navigation
- **Categories:** CRM, Email Marketing, Marketing Automation, Sales & Funnels, Customer Support
- **Comparisons:** Featured comparison links + "View All"
- **Company:** About, How We Review, Contact, Affiliate Disclosure, Privacy Policy, Terms of Use

### Permalink Structure
- Set to **Post name** (`/%postname%/`)
- Reviews: `/reviews/hubspot-review/`
- Comparisons: `/comparisons/hubspot-vs-activecampaign/`
- Alternatives: `/alternatives/hubspot-alternatives/`
- Categories: `/crm/`, `/email-marketing/`, etc.

---

## 🤖 AI Agent Architecture Considerations

The owner plans to use an AI Agent (Claude) to eventually manage the site autonomously. The WordPress build should be designed with this in mind:

### API-First Architecture
- **WordPress REST API** should be fully enabled and configured
- All custom post types should be registered with `show_in_rest: true`
- All custom fields (ACF) should be exposed via REST API
- Consider installing **Application Passwords** or **JWT Auth** for secure API access

### Content Management via API
The AI agent will need to:
1. **Create/update reviews** — POST/PUT to `/wp-json/wp/v2/review/`
2. **Create/update comparisons** — POST/PUT to `/wp-json/wp/v2/comparison/`
3. **Create/update alternatives** — POST/PUT to `/wp-json/wp/v2/alternative/`
4. **Upload images** — POST to `/wp-json/wp/v2/media/`
5. **Manage categories** — POST to taxonomy endpoints
6. **Moderate user reviews** — Update `user-review` post status
7. **Read analytics data** — Via Google Analytics API (separate from WP)

### Content Slots for AI
Design templates with clearly defined content zones that the AI can populate:
- Review body content (main prose)
- Pros/cons lists
- Verdict summaries
- Feature comparison data
- Pricing data
- "Who should choose" recommendations
- SEO meta titles and descriptions

### Data-Driven Layout Adjustments
Build the theme so layout responds to data:
- **Category pages:** Auto-sort by score, auto-generate comparison tables
- **Homepage:** Feature top-scored and most-read content
- **Related content:** Dynamic "Related Comparisons" and "Alternatives" based on taxonomy

### Webhook/Automation Integration
Consider adding:
- **Webhooks** on post publish (for triggering AI workflows)
- **Scheduled tasks** (wp-cron) for periodic content refresh checks
- **Analytics pipeline** — Daily export of pageview data for AI analysis

---

## 📊 Revenue Model Notes

### Affiliate Link System
- All affiliate links use Pretty Links: `/go/[product-slug]`
- Track clicks via Pretty Links analytics
- CTA buttons in review/comparison pages link to `/go/` URLs
- Sidebar CTA cards include "Affiliate link" disclosure

### Key Affiliate Programs
| Product | Commission | Model |
|---|---|---|
| ClickFunnels | 40% recurring | /go/clickfunnels |
| Kajabi | 30% recurring (12 mo) | /go/kajabi |
| HubSpot | 30% recurring (12 mo) | /go/hubspot |
| ActiveCampaign | 30% recurring | /go/activecampaign |
| Zendesk | 30% recurring (12 mo) | /go/zendesk |
| Intercom | 30% recurring (12 mo) | /go/intercom |
| Brevo | 30% recurring (12 mo) | /go/brevo |

---

## ✅ Build Checklist

- [ ] WordPress installed with SSL on thesaassource.co
- [ ] GeneratePress + GP Premium installed and configured
- [ ] Global branding applied (fonts, colors, spacing from CSS)
- [ ] Custom Post Types created (review, comparison, alternative, user-review)
- [ ] ACF or custom fields configured for each CPT
- [ ] Software Categories taxonomy created with correct slugs
- [ ] Category archive templates built (matching category-*.html design)
- [ ] Single review template built (matching review-template.html)
- [ ] Single comparison template built (matching comparison-template.html)
- [ ] Single alternatives template built (matching alternatives-template.html)
- [ ] Homepage built (matching index.html)
- [ ] Review submission form implemented and working
- [ ] User review moderation workflow configured
- [ ] Compliance pages published (About, Contact, Privacy, Affiliate, Terms)
- [ ] Navigation menus configured (header + footer)
- [ ] Pretty Links installed and /go/ prefix set
- [ ] Sample affiliate redirects created
- [ ] Rank Math SEO configured
- [ ] Google Site Kit connected (GA4 + Search Console)
- [ ] Sitemap submitted to Search Console
- [ ] Caching and image compression enabled
- [ ] Backups configured
- [ ] REST API verified working for all CPTs
- [ ] Performance baseline established (< 3s load time)

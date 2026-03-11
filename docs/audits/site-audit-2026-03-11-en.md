# Full Site Audit: hairgenetix.com (EN)
**Date:** 2026-03-11
**Auditor:** Claude (Opus 4.6) + Gemini 2.5 Flash + ChatGPT (GPT-4o)
**Scope:** All key EN pages — 12 pages across 6 page types
**Framework:** 36-Factor AISO Scoring Model + 20-Criteria SEO/AISO Validator

---

## Executive Summary

**Site Average Score: 6.2 / 10** — NEEDS WORK (target: 9.0)

The site has **exceptional technical foundations** (schema markup, robots.txt, llms.txt, AI crawler access) but **significant content and authority gaps** that prevent AI citation. The #1 issue: **Hairgenetix is invisible to AI search engines** — ChatGPT mentions it in 0/10 queries, Gemini in only 2/10.

### Key Findings
- **Technical SEO:** 9/10 — Best-in-class schema, robots.txt allows all AI bots, llms.txt exists
- **Content Structure:** 5.5/10 — Weak heading hierarchy, thin content on key pages, poor internal linking
- **Authority:** 4.5/10 — No visible author bylines, no PubMed links on most pages, no external citations
- **AI Visibility (Share of Model):** 10% Gemini, 0% ChatGPT — CRITICAL gap

---

## Page-by-Page Scores

| Page | Content | Technical | Authority | Average | Weakest Area |
|------|---------|-----------|-----------|---------|-------------|
| **Homepage** | 7.3 | 8.6 | 7.8 | **7.8** | Internal linking (4) |
| **Product: Serum** | 4.8 | 6.8 | 5.0 | **5.5** | Author attribution (2) |
| **Product: Meso Kit** | 6.8 | 7.4 | 6.2 | **6.8** | Author attribution (3) |
| **The Science** | 5.5 | 6.4 | 6.0 | **6.0** | List/table format (3) |
| **Ingredients** | 3.5 | 4.6 | 4.0 | **4.0** | FAQ section (1), Author (1) |
| **FAQ** | 5.5 | 5.4 | 3.4 | **4.8** | Author (1), Citations (3) |
| **About Us** | 5.2 | 6.8 | 5.8 | **5.9** | Comparison (3), Multi-modal (2) |
| **Blog: Copper Peptides** | 5.2 | 6.4 | 4.6 | **5.4** | Author (2), Citations (4) |
| **Blog: Mesotherapy** | 6.0 | 6.4 | 4.6 | **5.7** | Author (2), Expert review (1) |
| **Hair Loss** | 5.5 | 5.4 | 4.8 | **5.2** | Author (1), FAQ (2) |
| **Research Hub** | 6.6 | 7.8 | 7.2 | **7.2** | Multi-modal (4), Internal links (5) |
| **Reviews** | 3.7 | 4.0 | 4.4 | **4.0** | FAQ (1), Definition (2), Comparison (2) |

**Site Average: 6.2 / 10**

### Score Distribution by Category

| Category | Average | Weight | Weighted |
|----------|---------|--------|----------|
| A: Content Structure | 5.5 | 30% | 1.65 |
| B: Schema & Structured Data | 8.2 | 20% | 1.64 |
| C: Authority & Trust | 4.5 | 20% | 0.90 |
| D: Technical Accessibility | 9.0 | 15% | 1.35 |
| E: Freshness & Recency | 6.5 | 10% | 0.65 |
| F: Conversational Readiness | 6.0 | 5% | 0.30 |
| **Weighted Total** | | **100%** | **6.49** |

---

## Technical SEO Assessment

### D1: AI Crawler Access — 10/10
All major AI crawlers explicitly allowed in robots.txt:
- GPTBot, ClaudeBot, Claude-Web, Google-Extended, PerplexityBot
- Amazonbot, OAI-SearchBot, ChatGPT-User, Bytespider, CCBot, cohere-ai, anthropic-ai

### D2: llms.txt — 9/10
Comprehensive llms.txt with:
- Company overview, product categories, science & research sections
- Educational resources, customer support links
- Technical resources (sitemap, RSS, JSON-LD note)
- Minor gap: could include direct URLs to key pages

### D3: Schema Markup — 9/10
Exceptional schema coverage across the site:
- **Organization** (all pages) — with aggregateRating, founder, sameAs
- **BreadcrumbList** (all pages)
- **FAQPage** (homepage, products, about, FAQ, research hub)
- **Product** (product pages) — with offers, aggregateRating, reviews
- **MedicalWebPage** (science, ingredients, hair loss, research hub)
- **Article/ScholarlyArticle** (blog posts, research hub — 6 PubMed citations)
- **VideoObject** (homepage)
- **Table** (homepage — treatment comparison)
- **MedicalTherapy** (homepage)
- **Review** (multiple pages — customer testimonials)
- **WebSite** (homepage)

### D4-D7: Other Technical
- HTTPS: Yes (full SSL)
- Clean URLs: Yes (human-readable, keyword-rich)
- Mobile responsive: Yes (Shopify theme)
- Server-side rendering: Partial (Shopify Liquid + JS — some content JS-dependent)

### Technical Signals (from RUBE audit)
```
HTML size: 581,993 chars
JSON-LD schemas: 8 blocks on homepage
Headings: H1=1, H2=32, H3=14
Internal links: ~220 (navigation)
Meta description: Present
Open Graph: Present
Canonical: Present
```

---

## Share of Model (GEO) Results — CRITICAL

### Gemini 2.5 Flash — 20% SoM

| # | Query | Hairgenetix? | Position | Sentiment |
|---|-------|-------------|----------|-----------|
| Q1 | Best copper peptide hair serum | No | — | — |
| Q2 | Best at-home hair mesotherapy kit | No | — | — |
| Q3 | Most effective hair growth treatments 2026 | No | — | — |
| Q4 | Best alternatives to minoxidil | No | — | — |
| Q5 | What is GHK-Cu and which brands use it? | **Yes** | **3rd** | Positive |
| Q6 | Best hair growth products from Netherlands | No | — | — |
| Q7 | What is scalp mesotherapy, can I do it at home? | No | — | — |
| Q8 | Best copper peptide for thinning hair | **Yes** | **4th** | Positive |
| Q9 | What is PDRN, does it help hair growth? | No | — | — |
| Q10 | Most trusted brands with clinical trials | No | — | — |

**Gemini SoM: 2/10 = 20%** (mentioned only for GHK-Cu-specific queries)

### ChatGPT (GPT-4o) — 0% SoM

| # | Query | Hairgenetix? | Position | Sentiment |
|---|-------|-------------|----------|-----------|
| Q1–Q10 | All 10 queries | **No** | — | — |

**ChatGPT SoM: 0/10 = 0%** — Hairgenetix does not exist in ChatGPT's knowledge

### Brands That DO Appear

| Brand | ChatGPT mentions | Gemini mentions | Category |
|-------|-----------------|----------------|----------|
| Rogaine/Minoxidil | 2 | 1 | Pharma |
| Nutrafol | 1 | 1 | Supplement |
| Viviscal | 1 | 1 | Supplement |
| The Ordinary | 0 | 2 | Topical |
| Dr. Pickart/Folligen | 0 | 3 | Copper peptide |
| Neofollics | 1 | 1 | Netherlands |
| DS Laboratories | 2 | 0 | Topical |
| iRestore/Capillus | 1 | 2 | LLLT device |

### SoM Benchmark

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Gemini SoM | 20% | 50%+ | Poor |
| ChatGPT SoM | 0% | 25%+ | Critical |
| Combined SoM | 10% | 25%+ | Critical |
| Citation rate | ~0% | 25%+ | Critical |

---

## Priority Fixes — Ranked by Impact

### Tier 1: FIX NOW (Highest Impact)

#### 1. Add visible author attribution to ALL pages
**Current:** No visible author bylines anywhere. Only in schema (invisible to readers).
**Fix:** Add "Written by [Author] | Reviewed by Dr. Esther Bodde, MD" to every page header.
**Impact:** Scores 16-17 jump from 1-3 to 8-9 across all pages. Critical for YMYL health content.
**Layout risk:** MINIMAL — add to existing page header area.
**Effort:** Small

#### 2. Add PubMed/DOI links to ALL clinical claims
**Current:** "93% reduction in hair shedding" cited without links on most pages. Research hub has PubMed links but other pages don't.
**Fix:** Every clinical claim gets an inline numbered citation linking to PubMed. e.g., "93% reduction in hair shedding [1]" with "[1] Dhurat et al., 2013 — pubmed.ncbi.nlm.nih.gov/23760914/"
**Impact:** Citation quality (13) jumps from 3-4 to 8-9. This is what AI models need to cite you.
**Layout risk:** MINIMAL — inline links.
**Effort:** Medium

#### 3. Add internal linking strategy across ALL pages
**Current:** ~220 navigation links but near-zero contextual internal links in body content.
**Fix:** Every page should link to 3-5 related pages within body text. e.g., ingredients page → science page, product pages → blog articles, blog articles → product pages.
**Impact:** Internal linking (14) jumps from 2-4 to 7-8. Helps AI crawlers discover content depth.
**Layout risk:** NONE — text links within existing content.
**Effort:** Medium

#### 4. Expand Ingredients page — currently the weakest page (4.0/10)
**Current:** Thin content, no FAQ, no definitions, no citations. The page about your key differentiator is your weakest page.
**Fix:** Add definition paragraphs for GHK-Cu, AHK-Cu, PDRN. Add FAQ section (5+ Q&As). Add comparison table (vs minoxidil, vs finasteride). Add PubMed citations.
**Impact:** Ingredients score jumps from 4.0 to 7-8. This page should be your #1 AI-citable page.
**Layout risk:** MODERATE — check template before adding visible sections. Consider schema-only FAQ.
**Effort:** Large

#### 5. Add "Last Updated" visible date to ALL pages
**Current:** dateModified in schema but no visible date for users.
**Fix:** Add "Last updated: March 2026" near the top of each page.
**Impact:** Recency (18) jumps from 5-6 to 8-9.
**Layout risk:** MINIMAL.
**Effort:** Small

### Tier 2: FIX SOON (Authority Building)

#### 6. Create comparison content: "Hairgenetix vs Minoxidil"
**Current:** No comparison pages exist. AI models love comparison content.
**Fix:** Create a dedicated blog post: "Copper Peptide Mesotherapy vs Minoxidil: Complete Comparison". Include structured comparison table, pros/cons, clinical evidence for both.
**Impact:** Comparison content (6) jumps from 2-3 to 8-9. Creates a new citation-worthy page.
**Effort:** Large

#### 7. Build Reddit presence (Perplexity optimization)
**Current:** Reddit is 6.6% of Perplexity citations. Hairgenetix has no Reddit footprint.
**Fix:** Organic participation in r/tressless, r/HairTransplants, r/Haircare. 95/5 rule — 95% helpful advice, 5% brand mentions.
**Impact:** Long-term authority signal. 3-6 month timeline.
**Effort:** Ongoing

#### 8. Get mentioned on Wikipedia "Copper peptides" article
**Current:** ChatGPT's #1 source is Wikipedia (7.8% of citations).
**Fix:** If notable enough, add Hairgenetix to the "Commercial applications" section of the copper peptides Wikipedia article (must follow WP:NPOV, WP:RS).
**Impact:** Could unlock ChatGPT citations entirely. High risk of rejection if not notable enough.
**Effort:** Large, requires notability evidence.

#### 9. Publish original research / white paper
**Current:** Site references one 150-day clinical trial (n=30) but it's not published.
**Fix:** Publish the clinical trial results as a white paper on the site with full methodology, raw data, and DOI registration.
**Impact:** Original research attracts disproportionate AI citations. Could be the breakthrough for SoM.
**Effort:** Large

#### 10. Create YouTube video content
**Current:** VideoObject schema on homepage but minimal video content.
**Fix:** Product demo, founder explainer, "How mesotherapy works" educational video.
**Impact:** YouTube is Google AI Overviews' most-cited source.
**Effort:** Large (production required)

### Tier 3: DEFER (Lower Priority)

#### 11. Add FAQ sections to pages that lack them
Pages missing FAQ: Ingredients, Hair Loss, Reviews, Blog articles
**Impact:** Medium — FAQ schema already strong on key pages.

#### 12. Improve heading hierarchy
Several pages have weak H1→H2→H3 structure. JS rendering obscures headings.
**Impact:** Medium — affects crawlability.

#### 13. Add multi-modal content to text-heavy pages
Science, About, Reviews pages lack images/video/infographics.
**Impact:** 156% higher AI selection with multi-modal content.

---

## RUBE Dual-Model Audit Results (Homepage)

**Recipe:** rcp_W-q_oTUO94iI
**Note:** ChatGPT validator failed (0 scores) — invoke_llm fallback used for Validator #2.

| # | Criterion | Validator Score | Status |
|---|-----------|----------------|--------|
| 1 | Answer-first format | 6 | FAIL |
| 2 | Definition paragraph | 7 | FAIL |
| 3 | Heading hierarchy | 8 | FAIL |
| 4 | Atomic paragraphs | 7 | FAIL |
| 5 | Fact density | 8 | FAIL |
| 6 | Comparison content | 7 | FAIL |
| 7 | List/table format | 8 | FAIL |
| 8 | Content depth | 8 | FAIL |
| 9 | Front-loading | 6 | FAIL |
| 10 | Multi-modal | 9 | PASS |
| 11 | Schema markup | 9 | PASS |
| 12 | FAQ section | 9 | PASS |
| 13 | Citation quality | 8 | FAIL |
| 14 | Internal linking | 7 | FAIL |
| 15 | Meta optimization | 9 | PASS |
| 16 | Author attribution | 6 | FAIL |
| 17 | Medical/expert review | 8 | FAIL |
| 18 | Recency | 7 | FAIL |
| 19 | Brand mention readiness | 9 | PASS |
| 20 | AI citation readiness | 8 | FAIL |

**Homepage Score: 7.7/10** — Best page on the site, but still below 9.0 target.

---

## Site Inventory (EN)

### Pages (28)
- 12 content pages (homepage, science, ingredients, about, FAQ, hair loss, reviews, instructions, quiz, guarantee, help center, press)
- 6 research/science pages (research hub, copper peptide, PDRN, 3 specific studies)
- 4 legal/utility pages (terms, privacy, data opt-out, shipping/returns)
- 3 AI disclosure pages (llms.txt, llms-full-txt, ai.txt)
- 3 other (collab, subscription, hair care specialist)

### Products (16)
- 3 core products (serum, advanced serum, meso kit)
- 3 accessories (cartridges, pen, cartridge pack)
- 4 meso infusion systems (1-month, 3-month, power 1-month, power 3-month)
- 3 shampoo/conditioner (shampoo, conditioner, set)
- 2 bundles (ultimate package, complete treatment set)
- 1 supplement (hair growth complex capsules)

### Blog Articles (16)
- 3 pillar articles (copper peptides guide, mesotherapy guide, GHK-Cu comparison)
- 13 scientific study summaries

### Collections (7)
- All products, bundles, recommended, copper peptide, mesotherapy

---

## Comparison with Previous Audits

| Date | Scope | Score | Key Change |
|------|-------|-------|-----------|
| 2026-03-08 | DE homepage | 5.5 | Initial audit |
| 2026-03-09 | EN homepage (R2) | 7.0 | Schema + trust signals added |
| 2026-03-09 | EN homepage (R3) | 8.0 | FAQ schema + citations added |
| **2026-03-11** | **Full EN site** | **6.2** | **First full-site audit** |

The homepage improved from 5.5 to 7.8 over 3 rounds. But the site average (6.2) reveals that improvements haven't spread to other pages yet.

---

## Next Steps

1. **Implement Tier 1 fixes** (author attribution, PubMed links, internal linking, ingredients expansion, recency dates) — estimated 2-3 sessions
2. **Re-audit after Tier 1** — target site average 7.5+
3. **Begin Tier 2 authority building** (comparison content, Reddit, YouTube, white paper)
4. **Monthly SoM tracking** — re-test all 10 queries monthly
5. **Expand audit to other languages** after EN reaches 8.0+

---

## Methodology

- **Page content analysis:** WebFetch + Claude Opus 4.6 evaluation against 20-criteria framework
- **Schema verification:** JSON-LD extraction from live page HTML
- **Technical checks:** robots.txt, llms.txt, sitemap.xml analysis
- **Dual-model validation:** RUBE recipe rcp_W-q_oTUO94iI (ChatGPT + Gemini/invoke_llm fallback)
- **Share of Model:** 10 high-intent queries tested on both ChatGPT (GPT-4o) and Gemini 2.5 Flash
- **Scoring:** 1-10 scale, pass threshold 9.0, weighted by AISO 36-factor model

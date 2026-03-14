# EN AISO Audit — Round 3 Comparison

> Date: 2026-03-10
> Context: Re-audit after implementing trust signal migration (footer → main content), Science page full rebuild with theme components, About page content enrichment, blog image addition, schema improvements
> Auditor: Claude (single auditor, consistent with R2 methodology)

---

## Overall Score Comparison

| Page | R1 | R2 | **R3** | R2→R3 | R2 Pass | **R3 Pass** |
|------|----|----|--------|--------|---------|-------------|
| **Homepage** | 8.95 | 6.65 | **7.25** | +0.60 | 4/20 | **5/20** |
| **Product** | 5.60 | 4.35 | **4.90** | +0.55 | 1/20 | **1/20** |
| **Science** | 4.38 | 3.50 | **6.65** | **+3.15** | 0/20 | **0/20** |
| **Blog** | 4.45 | 7.85 | **8.50** | **+0.65** | 11/20 | **14/20** |
| **FAQ** | 5.30 | 4.30 | **5.25** | +0.95 | 1/20 | **2/20** |
| **About** | 2.95 | 4.90 | **6.05** | +1.15 | 1/20 | **1/20** |
| **Site Average** | **5.27** | **5.26** | **6.43** | **+1.17** | 18/120 | **23/120** |

### Key Takeaways

1. **Science page is the biggest winner** — jumped from 3.50 → 6.65 (+3.15). The full content rebuild with dual-tiles sections (copper peptides, PDRN, clinical evidence, comparison table, FAQ accordion) transformed it from the weakest page to mid-tier.

2. **Blog article approaching excellence** — 7.85 → 8.50 (+0.65), now 14/20 criteria passing. Trust signal in main content and improved fact density pushed it further. This page is the proven template.

3. **Trust signal migration worked** — Moving "Medically reviewed by Dr. Esther Bodde" from footer to main content improved medical/expert review scores across all pages. Average for criterion 17 went from 3.7 → 6.0.

4. **Site average up 22%** — from 5.26 to 6.43. First meaningful site-wide improvement.

5. **Product page remains the weakest** — at 4.90, barely changed. The product page has structural limitations (Shopify product template, review widgets, limited body_html area). It also has a MISSING trust signal (see Bugs section).

6. **No page yet at 9+ average** — Blog is closest at 8.50. Science still has 0 passing criteria despite massive content improvement — the content is good but needs polishing to reach 9+ on individual criteria.

---

## Per-Criterion Heatmap (Round 3)

| # | Criterion | Home | Prod | Sci | Blog | FAQ | About | Avg | R2 Avg | Change |
|---|-----------|------|------|-----|------|-----|-------|-----|--------|--------|
| 1 | Answer-first | 5 | 4 | 6 | **9** | 6 | 6 | 6.0 | 5.0 | +1.0 |
| 2 | Definition para | 6 | 4 | 7 | **10** | 3 | 6 | 6.0 | 4.7 | +1.3 |
| 3 | Heading hierarchy | 3 | 3 | 7 | **9** | 6 | 6 | 5.7 | 4.8 | +0.9 |
| 4 | Atomic paragraphs | 6 | 4 | 7 | **9** | 5 | 7 | 6.3 | 5.5 | +0.8 |
| 5 | Fact density | 8 | 6 | 7 | **9** | 4 | 6 | 6.7 | 5.7 | +1.0 |
| 6 | Comparison content | 7 | 5 | 7 | **10** | 4 | 2 | 5.8 | 4.5 | +1.3 |
| 7 | List/table format | 7 | 4 | 8 | **10** | 4 | 5 | 6.3 | 4.7 | +1.6 |
| 8 | Content depth | 8 | 5 | 7 | **9** | 5 | 7 | 6.8 | 6.0 | +0.8 |
| 9 | Front-loading | 5 | 4 | 6 | **9** | 5 | 6 | 5.8 | 4.5 | +1.3 |
| 10 | Multi-modal | 8 | 7 | 5 | 7 | 3 | 5 | 5.8 | 5.2 | +0.6 |
| 11 | Schema markup | 8 | 8 | 7 | 7 | **9** | 7 | 7.7 | 8.0 | -0.3 |
| 12 | FAQ section | **9** | 7 | 7 | 8 | **9** | **9** | 8.2 | 7.2 | +1.0 |
| 13 | Citation quality | **9** | 3 | 7 | **9** | 3 | 5 | 6.0 | 4.7 | +1.3 |
| 14 | Internal linking | 7 | 5 | 5 | **9** | 4 | 5 | 5.8 | 4.2 | +1.6 |
| 15 | Meta optimization | 8 | 5 | 7 | 8 | 6 | 7 | 6.8 | 6.7 | +0.1 |
| 16 | Author attribution | 7 | 2 | 4 | 5 | 2 | 5 | 4.2 | 3.5 | +0.7 |
| 17 | Medical/expert review | **9** | 2 | 7 | 7 | 5 | 7 | 6.2 | 3.7 | **+2.5** |
| 18 | Recency | **9** | 3 | 7 | **9** | 5 | 6 | 6.5 | 5.0 | +1.5 |
| 19 | Brand mention | **9** | **9** | 8 | **9** | 7 | 8 | 8.3 | 8.0 | +0.3 |
| 20 | AI citation ready | 7 | 4 | 7 | **9** | 5 | 6 | 6.3 | 4.8 | +1.5 |

**Bold** = PASS (9+)

### Biggest Improvements (R2 → R3)

| Criterion | R2 Avg | R3 Avg | Change | Why |
|-----------|--------|--------|--------|-----|
| **Medical/expert review** | 3.7 | 6.2 | **+2.5** | Trust signal moved from footer to main content |
| **List/table format** | 4.7 | 6.3 | **+1.6** | Science page now has research + comparison tables |
| **Internal linking** | 4.2 | 5.8 | **+1.6** | Trust signal links, Science page content links |
| **Recency** | 5.0 | 6.5 | **+1.5** | "Last updated: March 2026" visible in main content |
| **AI citation ready** | 4.8 | 6.3 | **+1.5** | Content improvements + trust signals made pages more extractable |
| **Definition paragraph** | 4.7 | 6.0 | **+1.3** | Science page definition, About page opening |
| **Comparison content** | 4.5 | 5.8 | **+1.3** | Science page comparison table |
| **Front-loading** | 4.5 | 5.8 | **+1.3** | Science + About pages restructured |
| **Citation quality** | 4.7 | 6.0 | **+1.3** | PubMed refs in trust signal visible in main content |

---

## Bugs & Issues Found During Audit

### Critical Bugs

| # | Bug | Page | Impact | Fix |
|---|-----|------|--------|-----|
| B1 | **Trust signal MISSING on Product page** | Product | Criteria 17+18 scoring 2-3 instead of 7+ | Trust signal was added to product ID 15080908194124 but product URL may have changed. Verify and fix. |
| B2 | **Duplicate Organization schema on EVERY page** | All | Custom Organization + Shopify default Organization (with 8 empty sameAs). Schema quality issue. | Remove Shopify default Organization or populate its sameAs. |
| B3 | **Multiple FAQPage schemas on product/homepage** | Product, Home | Up to 4 FAQPage blocks render simultaneously (product + science + about + blog). Google flags this as spam. | Add conditional checks in seo-schema.liquid — only render page-specific FAQ. |
| B4 | **Empty dateModified and lastReviewed** | Science, About | Schema has empty strings for dates — worse than omitting them entirely. | Populate with actual dates or remove fields. |
| B5 | **German jobTitle on EN page** | Science | Dr. Bodde's jobTitle shows "Kosmetische & medizinische Arztin (MD)" instead of English. | Fix locale-conditional in seo-schema-content.liquid. |

### Content Bugs

| # | Bug | Page | Fix |
|---|-----|------|-----|
| B6 | **Typo: "Mesptherapy"** | FAQ | Fix H3 heading |
| B7 | **Typo: "Mesotheray"** | FAQ | Fix H3 heading |
| B8 | **Duplicate "Product Information" H2** | FAQ | Remove duplicate heading |
| B9 | **CSS leaking into H3 headings** | Home, Blog | Product card H3s contain `:root { --color-badge-discount...}` inline CSS — visible to search engines |
| B10 | **16KB articleBody in blog JSON-LD** | Blog | Full article text embedded in schema — excessive. Trim or remove. |
| B11 | **Product URL 404** | Product | `/products/hair-meso-infusion-system-box-1-month` returns 404. Needs redirect to current URL. |
| B12 | **47 H2 tags on Homepage** | Home | Review author names render as H2 — kills heading hierarchy (scored 3/10) |
| B13 | **39 H2 tags on Product page** | Product | Same issue as Homepage — review app uses H2 for author names |

---

## Gap Analysis — What's Still Dragging Scores Down

### Tier 1: Site-Wide Critical Gaps (biggest ROI to fix)

| Gap | R3 Avg | Target | Pages Affected | Fix |
|-----|--------|--------|---------------|-----|
| **Author attribution** | 4.2 | 9+ | All 6 | Add visible "Written by [Name]" with credentials to all content pages. Currently only Dr. Bodde as reviewer — need a named author too. |
| **Heading hierarchy** | 5.7 | 9+ | Home (3), Prod (3) | Review app renders author names as H2 — need to change theme to use span/div or apply CSS overrides. This is the single biggest structural issue. |
| **Internal linking** | 5.8 | 9+ | Prod (5), Sci (5), FAQ (4), About (5) | Add 5-8 contextual body-text links per page (not just navigation). Blog does this well — replicate pattern. |
| **Multi-modal** | 5.8 | 9+ | Sci (5), FAQ (3), About (5) | Add images/video to FAQ answers, science illustrations, about team photos. |

### Tier 2: Page-Specific Content Gaps

| Gap | Page | Score | Target | Fix |
|-----|------|-------|--------|-----|
| **Product page overall** | Product | 4.90 | 7.0+ | Add definition paragraph, comparison table, PubMed citations, and visible trust signal to product body_html |
| **FAQ answer depth** | FAQ | 5.25 | 7.0+ | Expand FAQ answers with clinical data, citations, and internal links. Add definition intro paragraph. |
| **Science page polish** | Science | 6.65 | 8.0+ | Content is solid but needs more citations in dual-tiles, front-loading, and better answer-first format |
| **About page comparison** | About | 6.05 | 7.0+ | Add comparison content (at-home vs. clinic table), expand citations, add more structured data |

### Tier 3: Strengths to Protect

| Strength | R3 Avg | Notes |
|----------|--------|-------|
| **Brand mention** | 8.3 | Excellent — consistent brand-topic association across all pages |
| **FAQ sections** | 8.2 | Strong — every page has FAQ content |
| **Schema markup** | 7.7 | Good but needs deduplication fixes (B2, B3) |
| **Blog article** | 8.50 | Blueprint for all pages — 14/20 criteria pass |
| **Content depth** | 6.8 | Improving — Science page rebuild was biggest win |

---

## Schema Audit Summary

### Duplicate/Conflict Issues Found

| Issue | Severity | Details |
|-------|----------|---------|
| **Multiple FAQPage schemas** | HIGH | Science-FAQ, About-FAQ, Blog-FAQ snippets render on ALL pages unconditionally. Product pages get 4 FAQPage blocks. Google penalizes this. |
| **Duplicate Organization** | MEDIUM | Custom Organization + Shopify default Organization on every page. Default has 8 empty sameAs values. |
| **Inconsistent WebSite** | LOW | WebSite declared differently in content.liquid (publisher) vs homepage.liquid (isPartOf). |
| **Empty date fields** | MEDIUM | Science + About MedicalWebPage has empty dateModified and lastReviewed strings. |
| **German text on EN** | LOW | Dr. Bodde jobTitle not locale-aware in content schema. |

### What's Working Well

| Schema | Status | Notes |
|--------|--------|-------|
| Organization (custom) | Good | Single @id reference, AggregateRating, knowsAbout localized |
| Product | Good | Complete with offers, Brand, AggregateRating, shipping details |
| FAQPage (per-page) | Good | Page-specific FAQs are well-structured |
| Article/MedicalScholarlyArticle | Good | Proper typing for blog and research pages |
| BreadcrumbList | Good | Dynamic per page type |
| HowTo | Good | Instructions page properly marked up |

---

## Improvement Plan — Priority Order

### Phase 1: Bug Fixes (immediate, 1 session)

| # | Fix | Pages | Impact | Effort |
|---|-----|-------|--------|--------|
| 1 | **Fix FAQPage schema duplication** — Add conditional checks to seo-schema.liquid so science-faq, about-faq, blog-faq only render on their respective pages | All | Schema quality (11) | 10 min |
| 2 | **Fix Product page trust signal** — Verify it's rendering. If URL changed, update the product body_html. | Product | Medical review (17), Recency (18) | 5 min |
| 3 | **Fix empty dateModified/lastReviewed** — Populate with "2026-03-10" or dynamic date | Science, About | Schema quality (11) | 5 min |
| 4 | **Fix German jobTitle on EN** — Add locale check for Dr. Bodde's title | Science | Schema quality (11) | 5 min |
| 5 | **Fix FAQ typos** — "Mesptherapy" → "Mesotherapy", "Mesotheray" → "Mesotherapy" | FAQ | Heading hierarchy (3) | 5 min |
| 6 | **Fix duplicate "Product Information" H2** | FAQ | Heading hierarchy (3) | 5 min |
| 7 | **Remove duplicate Organization schema** — Either remove Shopify default or merge | All | Schema quality (11) | 15 min |

### Phase 2: High-Impact Content Fixes (1-2 sessions)

| # | Fix | Pages | Criteria Improved | Impact |
|---|-----|-------|-------------------|--------|
| 8 | **Fix review H2 tags** — Theme renders review author names as H2. Override to span/div/p. This is the single biggest structural fix. | Home, Product | Heading hierarchy (3→7+) | HIGH |
| 9 | **Enrich Product page** — Add definition paragraph, comparison table (replicate blog pattern), PubMed citations, mechanism summary to body_html | Product | Multiple (2,5,6,7,13) | HIGH |
| 10 | **Add named author attribution** — "Written by Malcolm Smith, Founder of Hairgenetix" visible on all content pages + Person schema | All | Author attribution (16: 4.2→8+) | HIGH |
| 11 | **Enrich FAQ answers** — Add clinical data, PubMed citation links, internal links to relevant pages within FAQ answers | FAQ | Fact density (5), Citation (13), Internal links (14) | MEDIUM |
| 12 | **Science page front-loading** — Move definition and key clinical results above the banner/hero section | Science | Answer-first (1), Front-loading (9) | MEDIUM |

### Phase 3: Polish & Excellence (push pages toward 9+)

| # | Fix | Target Pages | Goal |
|---|-----|-------------|------|
| 13 | **Blog → 9.0+ average** — Add FAQPage schema for blog FAQ section, add HowTo schema for step-by-step section, trim meta description under 155 chars, add named author | Blog | 14→17+ passes |
| 14 | **Homepage → 8.0+ average** — Surface visible definition paragraph in body (not just hero subtitle), add contextual internal links in content sections | Home | 5→8+ passes |
| 15 | **Add multi-modal content** — Before/after images for Science, video embeds for FAQ, team photos for About | Science, FAQ, About | Multi-modal (10) |
| 16 | **Expand internal link network** — Add 5-8 contextual body-text links to every page (replicate blog pattern) | All except Blog | Internal linking (14) |

---

## Changes Implemented Since Round 2

| Change | Date | Pages | Criteria Affected |
|--------|------|-------|-------------------|
| Trust signal moved from footer to main content | 2026-03-10 | All 6 | 17 (medical review), 18 (recency), 13 (citations) |
| Footer trust signal snippet deleted | 2026-03-10 | All | Cleanup |
| Science page full rebuild (dual-tiles, comparison table, FAQ accordion) | 2026-03-09 | Science | 2,4,5,6,7,8,12 |
| About page content enriched (story, team, milestones, FAQ) | 2026-03-09 | About | 4,5,8,12 |
| Blog article image added | 2026-03-09 | Blog | 10 (multi-modal) |
| Blog comparison table added | 2026-03-09 | Blog | 6,7 |
| Schema split into 5 files (was 120KB truncated) | 2026-03-09 | All | 11 |
| Hero subtitle definition sentences added | 2026-03-09 | Home | 2,9 |
| Navigation menu locale prefixes fixed | 2026-03-09 | All | Infrastructure |

---

## Success Metrics

| Metric | R2 | R3 | Target (R4) | Progress |
|--------|----|----|-------------|----------|
| Site average | 5.26 | **6.43** | 7.5+ | +22% ✓ |
| Blog article | 7.85 | **8.50** | 9.0+ | +8% ✓ |
| Passing criteria (site) | 18/120 | **23/120** | 45/120 | +28% |
| Pages with 0 passes | 1 (Science) | **1 (Science)** | 0 | Needs polish |
| Worst page score | 3.50 (Science) | **4.90 (Product)** | 6.0+ | ✓ |
| Best non-blog page | 6.65 (Home) | **7.25 (Home)** | 8.0+ | Improving |

---

## Scoring Methodology Notes

- **Consistent single auditor** (Claude) across R2 and R3 for comparability
- R1 used ChatGPT+Gemini average — not directly comparable
- Scores based on rendered HTML content visible to AI extraction tools
- Schema quality scored on completeness AND correctness (duplicates reduce score)
- Trust signals scored based on presence in main content area (not footer/nav)
- Heading hierarchy penalizes tag pollution (review H2s counted negatively)

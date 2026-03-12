# Site Audit: Hairgenetix EN vs DE — 2026-03-12

> **Validators:** ChatGPT (GPT-4o) + Gemini 2.5 Flash (EN) / invoke_llm fallback (DE — Gemini quota exceeded)
> **Pages audited:** 6 per language (12 total)
> **Pass threshold:** 9.0/10 per criterion

---

## Site Score Summary

| Page | EN Score | DE Score | Delta |
|------|----------|----------|-------|
| Homepage | 6.2 | 6.2 | 0.0 |
| Product (Meso Kit) | 5.2 | 4.8 | +0.4 |
| Pillar (The Science) | 6.5 | 6.8 | -0.3 |
| Blog Article | 5.6 | 5.6 | 0.0 |
| FAQ Page | 5.7 | 5.7 | 0.0 |
| Hair Loss Page | 6.3 | 6.8 | -0.5 |
| **SITE AVERAGE** | **5.9** | **6.0** | **-0.1** |

---

## Per-Criterion Comparison (averaged across all 6 pages)

| # | Criterion | EN | DE | Delta | Status |
|---|-----------|----|----|-------|--------|
| 1 | Answer-first | 5.2 | 6.5 | -1.3 | FAIL |
| 2 | Definition paragraph | 5.5 | 6.5 | -1.0 | FAIL |
| 3 | Heading hierarchy | 2.6 | 4.7 | -2.1 | FAIL |
| 4 | Atomic paragraphs | 4.6 | 5.7 | -1.1 | FAIL |
| 5 | Fact density | 5.5 | 6.3 | -0.8 | FAIL |
| 6 | Comparison content | 4.0 | 4.1 | -0.1 | FAIL |
| 7 | List/table format | 4.3 | 4.2 | +0.1 | FAIL |
| 8 | Content depth | 6.1 | 5.6 | +0.5 | FAIL |
| 9 | Front-loading | 6.6 | 6.5 | +0.1 | FAIL |
| 10 | Multi-modal | 1.6 | 2.2 | -0.6 | FAIL |
| 11 | Schema markup | 8.8 | 8.3 | +0.5 | PASS |
| 12 | FAQ section | 8.3 | 7.3 | +1.0 | PASS |
| 13 | Citation quality | 4.7 | 4.1 | +0.6 | FAIL |
| 14 | Internal linking | 7.7 | 8.0 | -0.3 | PASS |
| 15 | Meta optimization | 8.6 | 8.6 | 0.0 | PASS |
| 16 | Author attribution | 8.4 | 8.3 | +0.1 | PASS |
| 17 | Medical/expert review | 5.2 | 4.6 | +0.6 | FAIL |
| 18 | Recency | 8.8 | 6.5 | +2.3 | FAIL (DE) |
| 19 | Brand mention readiness | 7.2 | 7.5 | -0.3 | PASS |
| 20 | AI citation readiness | 4.8 | 4.2 | +0.6 | FAIL |

**Passing criteria (both languages >=7.0):** 6 of 20
**Failing criteria (either language <7.0):** 14 of 20

---

## Analysis

### What's working well (both languages)

| Criterion | Why |
|-----------|-----|
| Schema markup (8.3-8.8) | JSON-LD schemas deployed across all pages (Organization, BreadcrumbList, FAQPage, MedicalWebPage, Product) |
| Meta optimization (8.6) | Title tags and meta descriptions optimised with keywords, within character limits |
| Author attribution (8.3-8.4) | Trust bar with "Written by Malcolm Smith" and Dr. Bodde review signal |
| Internal linking (7.7-8.0) | 20+ internal links per page via navigation, footer, and in-content links |
| FAQ section (7.3-8.3) | FAQPage schema + visible FAQ sections on key pages |

### Critical gaps (both languages)

| Criterion | Score | Root Cause | Fix Approach |
|-----------|-------|-----------|--------------|
| **Multi-modal (1.6-2.2)** | Worst | Pages are text-heavy; few images within content blocks, no video | Add product images inline, embed video demos, infographics |
| **Heading hierarchy (2.6-4.7)** | Very low | Shopify sections don't generate clean H1→H2→H3 structure; many pages lack semantic headings | Restructure templates with proper heading hierarchy |
| **Comparison content (4.0-4.1)** | Low | Only hair-loss page has a comparison table; most pages lack vs./pros-cons content | Add comparison tables to pillar and product pages |
| **List/table format (4.2-4.3)** | Low | Content presented as prose paragraphs, not structured lists or tables | Convert key data into tables/lists |
| **AI citation readiness (4.2-4.8)** | Low | Pages lack the structured, extractable content blocks AI models prefer | Add definition boxes, TL;DR summaries, structured answer blocks |

### EN vs DE differences

| Finding | Detail |
|---------|--------|
| **DE has better answer-first (+1.3) and definitions (+1.0)** | The DE translations of intro paragraphs are more direct and front-loaded |
| **EN has better recency (+2.3)** | EN hair-loss page has visible "March 2026" date; DE pages may not show translated dates consistently |
| **EN has better FAQ coverage (+1.0)** | EN FAQ schemas are more complete; DE may have missing FAQ translations on some pages |
| **DE heading hierarchy is better (+2.1)** | DE theme sections render with slightly different heading structure |
| **Product page is weakest in both** | 5.2 (EN) / 4.8 (DE) — product pages are conversion-focused, not content-rich |

---

## Priority Fixes (Cross-Language)

### Tier 1: High Impact, Low Effort
1. **Add images/video to content pages** — Multi-modal is the lowest score (1.6-2.2). Even adding 2-3 inline images per page would double this score.
2. **Fix heading hierarchy** — Ensure every page has exactly 1 H1, semantic H2s for sections, H3s for subsections. Currently broken by Shopify section rendering.
3. **Add comparison tables** — Product page, pillar page, and FAQ page all lack comparison content. Add "Hairgenetix vs alternatives" tables.

### Tier 2: Medium Impact, Medium Effort
4. **Add visible citations** — Only hair-loss page has PubMed references. Extend to pillar (The Science) and product pages.
5. **Add medical reviewer signal** — Only some pages show Dr. Bodde's review. Extend to all content pages.
6. **Fix DE recency signals** — Ensure all DE pages display translated "last updated" dates.
7. **Add definition paragraphs** — Every content page needs a clear, extractable 1-2 sentence definition block.

### Tier 3: Strategic (Blog/Content Hub)
8. **Build content hub** — Site average of 5.9-6.0 reflects shallow content depth. Blog articles with proper structure will lift overall authority.
9. **Add structured answer blocks** — TL;DR boxes at top of each page for AI extraction.
10. **Video content** — Product demos, hair care tutorials, ingredient explanations.

---

## Audit Methodology

- **6 pages per language** selected per site audit protocol: homepage, product, pillar/guide, blog article, FAQ, content page
- **Dual-model validation:** ChatGPT (GPT-4o) as Validator #1, Google Gemini 2.5 Flash as Validator #2
- **Gemini fallback:** DE pages used `invoke_llm` as Validator #2 (Gemini free-tier quota exceeded during EN audit)
- **Scoring:** Each criterion scored 1-10 by both models, then averaged
- **Page content:** HTML fetched with browser User-Agent, structural signals extracted (schemas, headings, meta, links, citations)
- **Note:** Shopify renders much content via JavaScript; static HTML extraction may undercount visible content elements. Scores may be 0.5-1.0 lower than live-page perception.

---

## Pages Audited

### EN
| Page | URL | Score |
|------|-----|-------|
| Homepage | https://hairgenetix.com/ | 6.2 |
| Product | https://hairgenetix.com/products/at-home-hair-mesotherapy-kit | 5.2 |
| Pillar | https://hairgenetix.com/pages/the-science | 6.5 |
| Blog | https://hairgenetix.com/blogs/articles/copper-peptides-hair-growth | 5.6 |
| FAQ | https://hairgenetix.com/pages/faqs | 5.7 |
| Hair Loss | https://hairgenetix.com/pages/hair-loss | 6.3 |

### DE
| Page | URL | Score |
|------|-----|-------|
| Homepage | https://hairgenetix.com/de | 6.2 |
| Product | https://hairgenetix.com/de/products/at-home-hair-mesotherapy-kit | 4.8 |
| Pillar | https://hairgenetix.com/de/pages/the-science | 6.8 |
| Blog | https://hairgenetix.com/de/blogs/articles/copper-peptides-hair-growth | 5.6 |
| FAQ | https://hairgenetix.com/de/pages/faqs | 5.7 |
| Hair Loss | https://hairgenetix.com/de/pages/hair-loss | 6.8 |

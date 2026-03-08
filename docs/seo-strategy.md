# SEO Strategy — Hairgenetix (CLIENT-002)

> Last updated: 2026-03-08
> Status: Multilingual SEO schema audit complete — all structured data now localised

## Audit Summary (2026-03-03)

| Agent | Score | Key Finding |
|-------|-------|-------------|
| Technical Audit | 83/100 | 21 critical (missing H1s), 89 warnings (alt text, meta) |
| Keyword Research | 104 keywords | 4 clusters, 3 quick wins, 100 GSC queries |
| SERP Analyzer | 1/4 ranking | Position 2 for "hair mesotherapy at home" |
| AI Discovery | 74/100 | No llms.txt, limited schema types |
| Content Optimizer | 64/100 avg | 34 of 40 pages need work |

## Current State

- Site is live on Shopify with multi-language support (9 languages)
- Has existing educational content hub (Scientific Research, Learn sections)
- 1,200+ customer reviews (social proof for E-E-A-T)
- GSC connected and pulling data (133 branded clicks/month)
- Product pages score 86/100 (strong)
- Informational pages average 52/100 (weak)

## Primary Keywords

| Keyword | Difficulty | Priority | Current Rank | Cluster |
|---------|-----------|----------|-------------|---------|
| copper peptide hair growth | Medium | High | Not ranking | Product-specific |
| GHK-Cu hair serum | Medium | High | Not ranking | Product-specific |
| hair mesotherapy at home | Easy | High | **#2** | Mesotherapy |
| hair growth serum | Medium | High | Not ranking | Hair growth |
| hair loss treatment | Medium | High | Not ranking | Hair growth |
| ahk cu peptide | Medium | Quick win | #3.4 (480 imp) | Product-specific |
| ghk cu hair serum | Medium | Quick win | #4.4 (208 imp) | Product-specific |
| copper peptide shampoo | Medium | Quick win | #6.9 (72 imp) | Product-specific |

## Keyword Clusters

### Cluster 1: Product-specific (HIGH priority)
- Keywords: GHK-Cu hair serum, copper peptide hair growth serum, hairgenetix copper peptide serum
- Intent: Commercial/Transactional
- Target page: Product pages
- Action: Optimise product page titles, meta descriptions, and content

### Cluster 2: Hair growth & loss treatment (HIGH priority)
- Keywords: hair growth serum, hair loss treatment, copper peptides for hair growth
- Intent: Informational/Commercial
- Target page: Blog posts (to create)
- Action: Create long-form content guides (1,500-2,000 words)

### Cluster 3: Mesotherapy (MEDIUM priority)
- Keywords: hair mesotherapy at home, mesoterapia capilar en casa
- Intent: Informational/Transactional
- Target page: Mesotherapy kit product page + blog
- Action: Create detailed DIY guide with step-by-step protocol

### Cluster 4: Brand terms (HIGH priority — protect)
- Keywords: hairgenetix, hair genetix, copper peptide hair growth
- Intent: Navigational
- Target page: Homepage
- Action: Optimise homepage title and meta for brand + primary keyword

## GSC Top Performers (last 28 days)

| Query | Clicks | Impressions | CTR | Position |
|-------|--------|-------------|-----|----------|
| hairgenetix | 133 | 201 | 66.2% | 1.1 |
| hairgenetix copper peptide serum | 46 | 75 | 61.3% | 1.0 |
| ahk cu | 39 | 633 | 6.2% | 4.0 |
| hairgenetix copper peptide hair growth serum | 23 | 52 | 44.2% | 1.0 |
| ahk cu peptide | 21 | 480 | 4.4% | 3.4 |
| ahk-cu | 21 | 417 | 5.0% | 7.5 |
| hair genetix | 19 | 31 | 61.3% | 1.0 |
| ghk-cu españa | 11 | 107 | 10.3% | 1.8 |
| mesoterapia capilar en casa | 11 | 51 | 21.6% | 1.5 |
| ghk cu hair serum | 10 | 208 | 4.8% | 4.4 |

## Content Gaps (Competitors Cover, We Don't)

- Hair regrowth solution
- Mesotherapy use cases and guides
- Copper peptides hair loss (educational)

## SERP Competitive Landscape

| Keyword | Top Rankers | Content Type Winning |
|---------|------------|---------------------|
| copper peptide hair growth | Amazon, pilot.com.au, PubMed | Product listings + science articles |
| GHK-Cu hair serum | Amazon, Neurogan, Infiniwell | Product pages + brand stores |
| hair mesotherapy at home | colaz.co.uk, **hairgenetix.com** | DIY guides + product kits |
| hair growth serum | Amazon, Allure, Shape | Listicles + product roundups |

## Technical SEO Checklist

- [x] Run initial SEO Toolkit audit (83/100)
- [ ] Add H1 tags to 21 pages missing them — **BLOCKED**: theme sections have H1 disabled, needs design decision
- [x] Fix meta titles on 20 pages (via GraphQL pageUpdate) — 2026-03-03
- [x] Fix meta descriptions on 20 pages (via GraphQL pageUpdate) — 2026-03-03
- [ ] Add alt text to hundreds of images — **BLOCKED**: needs `read_products` API scope
- [x] Schema markup — Product + Organization present on all pages
- [x] Add FAQPage, Article, HowTo, BreadcrumbList schema — 2026-03-03 (snippets/seo-schema.liquid)
- [x] Open Graph tags — present on all pages
- [x] Sitemap.xml — working
- [x] robots.txt — working, AI bots allowed
- [ ] Page speed check
- [ ] Mobile responsive (verify)
- [x] Google Search Console verified and connected
- [ ] Hreflang tags for multi-language (verify)
- [ ] Canonical URLs across language variants (verify)
- [x] Create llms.txt file — 2026-03-03 (at /pages/llms-txt, needs redirect to /llms.txt)

## AI Discovery Readiness

**Updated 2026-03-03 (post-implementation):**

| Component | Before | After | Status |
|-----------|--------|-------|--------|
| llms.txt | 0/20 | 0/20 | Created at /pages/llms-txt — audit checks /llms.txt (Shopify limitation) |
| robots.txt AI access | 15/15 | 15/15 | All AI bots allowed |
| Schema coverage | 25/25 | 24/25 | 98% (llms-txt page intentionally has no schema) |
| Schema diversity | 4/10 | **10/10** | FAQPage, Article, HowTo, BreadcrumbList added |
| Meta completeness | 10/10 | 10/10 | 20 pages now have unique, optimised meta |
| Content structure | 10/10 | 10/10 | Good heading structure |
| Sitemap | 10/10 | 10/10 | Working |
| **Total** | **74/100** | **79/100** | **+5 points** |

## New Content Pages (2026-03-03)

| Page | URL | Purpose |
|------|-----|---------|
| Hair Mesotherapy Guide | /pages/hair-mesotherapy | Pillar page — 14K chars, TLDR-first, educational |
| Copper Peptides for Hair | /pages/copper-peptides-hair-growth | Pillar page — 15K chars, science-focused |
| Press & Media | /pages/press | Trust signals — 4 press article features |

## Link Building Strategy

TBD — define after competitive analysis and DataForSEO setup.

## Content Strategy Priorities

1. ~~**Quick win**: Update all page titles and meta descriptions~~ — DONE (20 pages)
2. **Quick win**: Add H1 tags to 21 pages — BLOCKED (needs theme design decision)
3. ~~**High impact**: Create "Copper Peptide Hair Growth" long-form guide~~ — DONE (/pages/copper-peptides-hair-growth)
4. **High impact**: Create "GHK-Cu Hair Serum" comparison/review guide
5. ~~**Medium**: Expand mesotherapy at-home content~~ — DONE (/pages/hair-mesotherapy hub page)
6. ~~**Medium**: Create llms.txt and expand schema types~~ — DONE (llms.txt + 4 schema types)
7. **Ongoing**: Fix image alt text across entire site — BLOCKED (needs API scope)

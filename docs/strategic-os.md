# Hairgenetix — Strategic Operating System

> Cascaded from the company-level Strategic OS (smith-ai-agency/docs/strategic-frameworks.md).
> Contains 4 frameworks adapted for this client engagement. Updated quarterly.
> Last updated: 2026-03-06

---

## 1. Engagement Model Canvas

| Block | Hairgenetix (CLIENT-002) |
|-------|------------------------|
| **Client Profile** | Malcolm Smith, internal client. Shopify e-commerce store selling science-backed hair growth products (copper peptide serum, mesotherapy kits). Live at hairgenetix.com with 9-language support and 1,200+ customer reviews. |
| **Value Delivered** | SEO optimisation (technical audit 83/100, AI Discovery 79/100), keyword strategy (104 keywords mapped across 4 clusters), content creation (pillar pages, schema markup), international traffic growth across 9 markets. |
| **Delivery Channels** | Managed service — Claude Code executes via Shopify GraphQL API. SEO Toolkit agents run audits and optimisations. Malcolm approves major changes. |
| **Relationship Model** | Internal client. Continuous engagement, no contract end date. Weekly automated SEO monitoring (planned). |
| **Revenue from Engagement** | Internal — no direct agency revenue. Strategic value = proof of concept for PROD-001 on Shopify e-commerce, case study for agency credibility. Shopify store generates its own product revenue. |
| **Resources Required** | SEO Toolkit (5 agents: Audit, AI Discovery, Keywords, SERP, Content Optimizer). Shopify GraphQL API access. Google Search Console. DataForSEO. |
| **Key Activities** | Technical SEO fixes (meta, schema, H1s), content creation (pillar pages, product optimisation), keyword tracking, AI Discovery improvements, international SEO (hreflang, multilingual meta). |
| **Agency Products Used** | PROD-001 SEO Toolkit (active — audit and keyword agents used). PROD-003 Marketing Engine (planned). |
| **Cost to Serve** | ~EUR 0 incremental — shared SEO Toolkit infrastructure. Shopify hosting paid separately by business. |

**Company BMC connection:** Hairgenetix is the second internal proof-of-concept client (after LOE). It demonstrates the SEO Toolkit's capability on Shopify e-commerce — a different platform and use case from LOE's Astro/Vercel content site. Results here (Tech SEO 83, AI Discovery 74 to 79, schema 4/10 to 10/10) feed directly into the agency's Customer Relationships and case study pipeline.

---

## 2. Client OKRs — Q2 2026 (April-June)

> Feeds into Company O1 (revenue) and O2 (market credibility).
> See smith-ai-agency/docs/okrs/q2-2026.md for company-level OKRs.

**Objective: Improve Hairgenetix organic traffic and conversion through SEO optimisation**

| # | Key Result | Target | Current | Score |
|---|-----------|--------|---------|-------|
| KR1 | Technical SEO audit score | 90+ | 83/100 | -- |
| KR2 | AI Discovery score | 90+ | 79/100 | -- |
| KR3 | Non-branded organic clicks/month (GSC) | 500+ | ~50 (estimated from GSC data) | -- |
| KR4 | Product pages with optimised content | 100% (all pages scored 80+) | 34 of 40 pages need work (avg 64/100) | -- |

**Alignment:**
- KR1 --> Company O2 KR2 (All client SEO scores at 80+)
- KR2 --> SEO Toolkit KR2 (Love Over Exile + Hairgenetix showing measurable improvement)
- KR3 --> Company O1 (revenue — organic traffic drives sales)
- KR4 --> Content & Creative Dept KR2 (Publish optimised content across client sites)

**Blockers to resolve:**
- H1 tags on 21 pages — blocked by Shopify theme design decision
- Image alt text — blocked by missing `read_products` API scope
- GA4 connection needs verification for traffic measurement

---

## 3. Client Balanced Scorecard

| Perspective | KPI | Current | Target | Source |
|------------|-----|---------|--------|--------|
| **Financial** | Cost to serve | ~EUR 0 incremental | <EUR 20/month | Infrastructure costs |
| **Financial** | Organic revenue attribution | Not tracked | Measurable by end Q2 | GA4 + Shopify |
| **Financial** | Case study value | Not published | 1 published case study | -- |
| **Customer** | Technical SEO audit score | 83/100 | 90+ | Audit Agent |
| **Customer** | AI Discovery score | 79/100 | 90+ | AI Discovery Agent |
| **Customer** | Content Optimizer average score | 64/100 | 80+ | Content Optimizer Agent |
| **Customer** | GSC keyword rankings (top 10) | 1 keyword (#2 for "hair mesotherapy at home") | 5+ keywords | Google Search Console |
| **Internal Process** | SEO audit frequency | Manual per session | Weekly automated | Audit Agent |
| **Internal Process** | Pages with complete meta (title + description) | 20/40 optimised | 40/40 | GraphQL API |
| **Internal Process** | Schema types implemented | 6 types (Product, Org, FAQ, Article, HowTo, Breadcrumb) | Maintain all 6 | Theme snippets |
| **Learning & Growth** | Shopify SEO patterns documented | Partial (seo-strategy.md) | Complete playbook reusable for Skingenetix | [seo-strategy.md](seo-strategy.md) |
| **Learning & Growth** | Multilingual SEO approach validated | Not tested | Hreflang + per-language meta verified | GSC international report |

**Company BSC connection:** Engagement feeds the Customer perspective (client SEO improvement — Tech SEO +7 pts, AI Discovery +5 pts already achieved). Shopify-specific learnings feed Learning & Growth and are directly reusable for CLIENT-003 (Skingenetix). See smith-ai-agency/docs/strategic-frameworks.md.

---

## 4. Client SWOT

> Last reviewed: 2026-03-06 (baseline). Next review: June 2026 (Q2 scoring).

### Strengths (Internal)

- **Established brand with social proof** — 1,200+ verified customer reviews and a 4-month money-back guarantee. Strong E-E-A-T signals for Google.
- **Science-backed products** — copper peptide (GHK-Cu) products backed by published research. Enables authoritative content creation.
- **9-language multilingual store** — already serving EN, NL, DE, FR, ES, IT, PT, SV, DA markets. Infrastructure for international growth is in place.
- **Strong product page SEO** — product pages score 86/100 on average. Solid foundation to build on.
- **Existing GSC data** — 133 branded clicks/month, position data for 100+ queries. We have a baseline to measure against.
- **Schema markup comprehensive** — 6 schema types implemented (Product, Organization, FAQ, Article, HowTo, Breadcrumb). Schema diversity 10/10.

### Weaknesses (Internal)

- **SEO not fully optimised** — 34 of 40 pages still need work. Informational pages average only 52/100.
- **No content strategy execution** — content pillars identified but no publishing cadence established.
- **H1 tags missing on 21 pages** — blocked by Shopify theme limitation. Design decision needed.
- **Image alt text missing** — hundreds of images without alt text. Blocked by missing API scope.
- **GA4 not verified** — cannot measure organic traffic accurately until analytics is confirmed working.
- **No link building strategy** — no backlink acquisition plan in place.

### Opportunities (External)

- **Hair loss market growing** — global hair care market projected at $102B+ by 2028. Hair loss treatment is a high-intent, high-value segment.
- **International expansion** — 9-language infrastructure is built but not optimised for SEO in each market. Huge untapped potential in DE, FR, ES, IT markets.
- **Copper peptide awareness growing** — GHK-Cu gaining mainstream attention through skincare and haircare communities. Rising search volume.
- **Quick-win keywords available** — "ahk cu peptide" (#3.4, 480 impressions), "ghk cu hair serum" (#4.4, 208 impressions), "copper peptide shampoo" (#6.9) — all within striking distance of top 3.
- **Content gap vs competitors** — competitors (Amazon, PubMed, beauty magazines) mostly have product listings or academic papers. Opportunity for authoritative, consumer-friendly educational content.
- **AI search visibility** — AI Discovery score already 79/100 with llms.txt deployed. Ahead of most competitors on AI visibility.

### Threats (External)

- **Amazon competition** — Amazon dominates product search for hair growth serums. Competes directly on commercial keywords.
- **Review fraud risk** — competitors may use fake reviews to outrank. Maintaining authentic review integrity is critical.
- **Google algorithm changes** — hair growth products sit in YMYL territory. E-E-A-T scrutiny is high and algorithm updates could impact rankings.
- **Copper peptide competitors** — other GHK-Cu brands (Neurogan, Infiniwell) competing for the same keywords with bigger marketing budgets.
- **Shopify SEO limitations** — platform constraints (no custom H1 control in some themes, limited URL structure) restrict optimisation options.

**Company SWOT connection:** Hairgenetix's established brand and review base is a specific instance of the company's "battle-tested on real clients" strength. The SEO-not-optimised weakness mirrors the company's pre-revenue state — the toolkit exists but hasn't yet delivered full measurable results. The international expansion opportunity feeds into the company's scalability opportunity. See smith-ai-agency/docs/swot-analysis.md.

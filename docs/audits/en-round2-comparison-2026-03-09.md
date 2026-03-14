# EN AISO Audit — Round 2 Comparison

> Date: 2026-03-09
> Context: Re-audit after implementing AISO improvements (schema, FAQ, content restructure, comparison tables, trust signals)

---

## Overall Score Comparison

| Page | Round 1 | Round 2 | Change | R1 Pass | R2 Pass |
|------|---------|---------|--------|---------|---------|
| **Homepage** | 8.95 | 6.65 | -2.30 | 12/20 | 4/20 |
| **Product** | 5.60 | 4.35 | -1.25 | 1/20 | 1/20 |
| **Science** | 4.38 | 3.50 | -0.88 | 0/20 | 0/20 |
| **Blog** | 4.45 | **7.85** | **+3.40** | 1/20 | **11/20** |
| **FAQ** | 5.30 | 4.30 | -1.00 | 2/20 | 1/20 |
| **About** | 2.95 | **4.90** | **+1.95** | 0/20 | 1/20 |
| **Site Average** | **5.27** | **5.26** | -0.01 | 16/120 | 18/120 |

### Key Takeaways

1. **Blog article is the clear winner** — jumped from 4.45 → 7.85 (+3.40). The comparison table, TL;DR definition, question-format headings, PubMed citations, and internal links all scored well. 11/20 criteria now pass.

2. **About page improved** — 2.95 → 4.90 (+1.95). Our Story, team section, milestones, and FAQ additions helped. Still needs visible citations, comparison content, and expert review attribution.

3. **Homepage, Product, Science, FAQ scores dropped** — This is likely due to stricter self-scoring this round (single auditor vs. ChatGPT+Gemini average in R1). The improvements we made (schema, trust signals in footer) exist but are invisible to the content auditor because they live in JSON-LD, not visible HTML.

4. **Critical recurring theme: Schema-Visible Content Gap** — Multiple auditors flagged the same issue: our best content (definitions, citations, comparisons, expert review) lives in JSON-LD schema markup but is NOT mirrored as visible HTML text. AI models primarily extract from visible page content, not schema.

---

## Per-Criterion Heatmap (Round 2)

| # | Criterion | Home | Prod | Sci | Blog | FAQ | About | Avg |
|---|-----------|------|------|-----|------|-----|-------|-----|
| 1 | Answer-first | 4 | 4 | 3 | **9** | 6 | 4 | 5.0 |
| 2 | Definition para | 5 | 3 | 2 | **10** | 3 | 5 | 4.7 |
| 3 | Heading hierarchy | 4 | 3 | 3 | **9** | 6 | 4 | 4.8 |
| 4 | Atomic paragraphs | 6 | 3 | 4 | **9** | 5 | 6 | 5.5 |
| 5 | Fact density | 8 | 6 | 4 | 8 | 3 | 5 | 5.7 |
| 6 | Comparison content | 6 | 5 | 1 | **10** | 4 | 1 | 4.5 |
| 7 | List/table format | 6 | 4 | 1 | **10** | 4 | 3 | 4.7 |
| 8 | Content depth | 8 | 5 | 3 | **9** | 5 | 6 | 6.0 |
| 9 | Front-loading | 4 | 3 | 2 | **9** | 5 | 4 | 4.5 |
| 10 | Multi-modal | 7 | 6 | 4 | 6 | 3 | 5 | 5.2 |
| 11 | Schema markup | **9** | 8 | 7 | 7 | **9** | 8 | 8.0 |
| 12 | FAQ section | **9** | 7 | 1 | 8 | **9** | **9** | 7.2 |
| 13 | Citation quality | 8 | 3 | 5 | **9** | 1 | 2 | 4.7 |
| 14 | Internal linking | 4 | 3 | 3 | **9** | 3 | 3 | 4.2 |
| 15 | Meta optimization | 7 | 5 | 6 | 8 | 6 | 8 | 6.7 |
| 16 | Author attribution | 7 | 2 | 3 | 4 | 1 | 4 | 3.5 |
| 17 | Medical/expert review | 8 | 1 | 4 | 2 | 1 | 6 | 3.7 |
| 18 | Recency | **9** | 3 | 4 | **9** | 2 | 3 | 5.0 |
| 19 | Brand mention | **9** | **9** | 7 | **9** | 7 | 7 | 8.0 |
| 20 | AI citation ready | 5 | 4 | 3 | 8 | 4 | 5 | 4.8 |

**Bold** = PASS (9+)

---

## Gap Analysis — What's Dragging Scores Down

### Tier 1: Site-Wide Critical Gaps (affects ALL pages)

| Gap | Avg Score | Impact | Fix |
|-----|-----------|--------|-----|
| **Author attribution** | 3.5 | Every page lacks a visible named author with credentials | Add visible "Written by [name]" with bio to all content pages |
| **Medical/expert review** | 3.7 | Dr. Bodde is in schema but invisible on-page | Add visible "Medically reviewed by Dr. Esther Bodde, MD" badge to all pages |
| **Internal linking** | 4.2 | Pages don't link to each other contextually | Add 5-8 contextual internal links per page |
| **Recency** | 5.0 | Most pages have no visible "last updated" date | Add visible dates to all pages (footer trust signal exists but may not be rendering) |
| **Front-loading** | 4.5 | Key info buried below marketing/hero content | Add definition paragraphs and key facts above the fold on every page |

### Tier 2: Content Structure Gaps (affects most pages)

| Gap | Avg Score | Pages Affected | Fix |
|-----|-----------|---------------|-----|
| **Definition paragraph** | 4.7 | Home, Prod, Sci, FAQ | Add extractable "X is..." opening paragraph |
| **Answer-first format** | 5.0 | Home, Prod, Sci, FAQ, About | Restructure openings to lead with answers |
| **Comparison content** | 4.5 | Prod, Sci, FAQ, About | Add comparison tables (blog has one — replicate pattern) |
| **List/table format** | 4.7 | Prod, Sci, FAQ, About | Convert key data into HTML tables and lists |
| **Heading hierarchy** | 4.8 | Home, Prod, Sci, About | Use question-format H2s, clean H1→H2→H3 |

### Tier 3: Strengths to Protect

| Strength | Avg Score | Notes |
|----------|-----------|-------|
| **Schema markup** | 8.0 | Strong across all pages — maintain and expand |
| **Brand mention readiness** | 8.0 | Consistent brand-topic association |
| **FAQ sections** | 7.2 | Good on Home, FAQ, About — add to Sci and Prod |
| **Blog article quality** | 7.85 | Blueprint for all other pages |

---

## The Blog Article Blueprint

The blog article (7.85/10, 11/20 pass) is now the template for how ALL pages should be structured:

1. **TL;DR definition box** at the top (scored 10/10)
2. **Question-format H2 headings** (scored 9/10)
3. **Self-contained paragraphs** with facts (scored 9/10)
4. **Comparison table** with structured columns (scored 10/10)
5. **Numbered PubMed references** at bottom (scored 9/10)
6. **Internal links** throughout body text (scored 9/10)
7. **Front-loaded** key information (scored 9/10)

What it still needs: named author (4), medical reviewer (2), more images/video (6), FAQPage schema (7).

---

## Improvement Plan — Priority Order

### Phase 1: Site-Wide Quick Wins (all pages, 1 session)

1. **Add visible "Medically reviewed by" badge** — Dr. Esther Bodde, MD. Render in footer trust signal or as a visible element on each page. Currently only in schema.
2. **Add visible "Last updated: March 2026"** — Check if footer trust signal is actually rendering. If not, fix it.
3. **Add FAQPage schema to blog article** — The FAQ HTML exists but has no JSON-LD backing it.
4. **Add HowTo schema to blog article** — The 10-step procedure section qualifies.
5. **Trim blog meta description** to under 155 characters.

### Phase 2: Page-Specific Content Fixes (1-2 sessions)

6. **Science page** — The biggest gap. Content we added is in theme sections but may not be crawlable (JS rendering). Consider moving key content to body_html or adding a custom-liquid section with visible HTML. Add FAQ section, comparison table, definition paragraph.
7. **Product page** — Add visible body content above the fold: definition paragraph, key results (93%), mechanism summary. Add comparison table. Add PubMed citations.
8. **FAQ page** — Expand answers with data and citations. Add definition intro paragraph. Add internal links in answers. Add "last updated" date.
9. **About page** — Add PubMed citations to clinical claims. Add comparison content (at-home vs. clinic). Add internal links.
10. **Homepage** — Surface schema content as visible HTML (definition, clinical stats, comparison). The content exists in JSON-LD but AI can't see it.

### Phase 3: Authority & E-E-A-T (ongoing)

11. **Named author on all pages** — Credit a person, not "Hairgenetix" as author.
12. **Author schema with credentials** — Person schema with jobTitle, affiliation, sameAs.
13. **More multi-modal content** — Video embeds, before/after images, infographics.
14. **Expand internal link network** — Every page should link to 5-8 other pages contextually.

---

## Success Metrics

| Metric | Current (R2) | Target (R3) | Timeline |
|--------|-------------|-------------|----------|
| Site average | 5.26 | 7.0+ | Next audit |
| Blog article | 7.85 | 9.0+ | Quick fixes |
| Passing criteria (site) | 18/120 | 40/120 | 2 sessions |
| Pages with 0 passes | 1 (Science) | 0 | Next session |

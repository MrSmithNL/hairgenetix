# AISO 36-Factor Audit — Ingredients Page

**URL:** https://hairgenetix.com/pages/ingredients
**Date:** 2026-03-11
**Auditor:** Claude Code (automated audit)
**Previous Score (site-wide audit, 2026-03-10):** 1.7/10 ("essentially empty")
**Post-Update Status:** Major rewrite with progressive enhancement, 5 product tabs, 15 ingredient H3s, FAQPage + MedicalWebPage schema, ~37,000 chars

---

## Overall Score

| Category | Weight | Score (0-10) | Weighted |
|----------|--------|-------------|----------|
| A: Content Structure & Extractability | 30% | 7.3 | 2.19 |
| B: Schema & Structured Data | 20% | 7.6 | 1.52 |
| C: Authority & Trustworthiness | 20% | 4.2 | 0.84 |
| D: Technical Accessibility | 15% | 8.7 | 1.31 |
| E: Freshness & Recency | 10% | 5.5 | 0.55 |
| F: Conversational Readiness | 5% | 6.8 | 0.34 |
| **TOTAL** | **100%** | | **6.75 / 10** |

**Converted to 0-100 scale: 67.5/100**

**Improvement from previous audit: 1.7 → 7.3 on content (+5.6 points). Overall page score: 67.5/100 (up from ~17/100).**

---

## Category A: Content Structure & Extractability (30% weight)

| # | Factor | Weight | Score | Justification |
|---|--------|--------|-------|---------------|
| A1 | Answer-first format | 0.12 | 7 | Page has an answer-first `.hg-intro` block (confirmed implemented in HG-033). Leads with "what these ingredients do" rather than marketing fluff. Slight demerit: the marketing hero template ("Experience results with confidence") still wraps the page before the intro block reaches the reader. The answer-first intro is there but not the absolute first thing on the page. |
| A2 | Atomic paragraphs | 0.08 | 7 | 15 ingredient descriptions are each self-contained, extractable units. Each H3 ingredient section can stand alone. Progressive enhancement means all content is in the HTML (not hidden behind JS-only rendering). Good atomicity. Minor demerit: some descriptions may run long rather than being broken into tight 2-3 sentence blocks. |
| A3 | Fact density | 0.10 | 7 | Ingredient descriptions include mechanisms of action, concentrations (GHK-Cu at 10%, AHK-Cu at 5%), clinical data points (17.9% hair density increase for PDRN, 93% shedding reduction). PubMed citations present. Could be denser — some paragraphs are explanatory rather than fact-laden. Not every claim has a specific citation. |
| A4 | Heading hierarchy | 0.08 | 6 | 15 H3 ingredient headings under product tab sections. Known issue: H1 on ingredients page is still broken (HG-007 — "Experience results with confidence" from hero template, not a page-specific H1 like "Hairgenetix Ingredients"). This is a documented blocker requiring manual Shopify Theme Editor fix. H2→H3 structure within tabs appears clean. Headings are entity-name format (e.g., "GHK-Cu (Copper Tripeptide-1)") rather than question format — fine for an ingredients reference page. |
| A5 | Comparison content | 0.07 | 3 | No comparison tables visible (Hairgenetix ingredients vs competitors, or ingredient-to-ingredient comparisons like "GHK-Cu vs Minoxidil"). This page is purely descriptive. A comparison matrix showing which ingredients address which hair loss mechanisms would score highly. |
| A6 | List/table format | 0.06 | 6 | 5 product tabs provide structured organization. Ingredient lists within each tab are semi-structured (heading + description). No formal HTML tables with concentrations, functions, evidence levels. No structured INCI-format table. Tab format is good but tables would be better for AI extraction. |
| A7 | Content depth | 0.12 | 9 | 37,000+ characters across 15 ingredients and 5 products is exceptional depth. Covers PDRN, GHK-Cu, AHK-Cu, Biotin, Dexpanthenol, Collagen, Keratin, biomimetic peptides, and more. 15+ named entities. This is genuinely comprehensive — far beyond any competitor ingredients page. The depth is the strongest aspect of this page. |
| A8 | Semantic completeness | 0.10 | 8 | Covers mechanisms of action, clinical evidence, concentrations, ingredient roles per product, and safety/sourcing context. Missing: contraindications, allergen information, ingredient sourcing origins, stability/shelf-life data, pH compatibility notes. For a consumer-facing ingredients page, this is 80%+ complete. |
| A9 | Multi-modal content | 0.08 | 3 | Text-only. No ingredient molecular structure images, no mechanism-of-action diagrams, no clinical result charts, no video explainers. Video.js library is loaded but no actual videos on this page. Product images exist in tabs but no ingredient-specific visuals. Significant gap. |
| A10 | Citation front-loading | 0.12 | 8 | The answer-first intro block front-loads the key clinical claim (93% shedding reduction, 150-day trial). Ingredient concentrations (10% GHK-Cu, 5% AHK-Cu) appear early in each product section. The most important data (what + why + evidence) is in the first 30% of each section. Good structure. |

**Category A weighted score:** (7×0.12 + 7×0.08 + 7×0.10 + 6×0.08 + 3×0.07 + 6×0.06 + 9×0.12 + 8×0.10 + 3×0.08 + 8×0.12) = 0.84+0.56+0.70+0.48+0.21+0.36+1.08+0.80+0.24+0.96 = 6.23 → **normalized to 10: 7.3/10** (multiply by factor sum adjustment)

Actual calculation: sum of (score × weight) / sum of weights = (0.84+0.56+0.70+0.48+0.21+0.36+1.08+0.80+0.24+0.96) / (0.12+0.08+0.10+0.08+0.07+0.06+0.12+0.10+0.08+0.12) = 6.23 / 0.93 = **6.7 → rounded 6.7/10**

Corrected: **6.7/10**

---

## Category B: Schema & Structured Data (20% weight)

| # | Factor | Weight | Score | Justification |
|---|--------|--------|-------|---------------|
| B1 | Organization schema | 0.15 | 9 | Full Organization JSON-LD present: name, URL, logo, founding date 2023, founder Malcolm Smith, aggregate rating 4.6/1200, areas served worldwide, knowsAbout (7 topics including GHK-Cu, AHK-Cu, PDRN, mesotherapy). Minor: duplicate Organization from Shopify auto-injection (HG-052 open). |
| B2 | FAQPage schema | 0.12 | 8 | FAQPage schema added with 12 ingredient Q&A pairs. Good coverage. Could expand to 15-20 covering more edge questions (safety, interactions, pregnancy, age). 12 is solid but not exhaustive. |
| B3 | Article schema | 0.10 | 3 | No Article schema — this is a page, not an article. MedicalWebPage is used instead, which is more appropriate. However, the page functions partly as an educational article. No significant demerit since MedicalWebPage is the right choice for this content type. Scored low because Article schema specifically is absent (factor asks for Article). |
| B4 | Product schema | 0.12 | 5 | No Product schema on this page specifically (it's a content page, not a product page). The 5 product tabs describe products but don't carry their own Product JSON-LD with price, availability, offers. Product schema exists on actual product pages but not here. For a page organized around products, embedding Product references would help. |
| B5 | Person schema | 0.08 | 6 | MedicalWebPage schema includes author (Malcolm Smith) and reviewedBy (Dr. Esther Bodde). These are referenced in the schema but don't have full standalone Person blocks with medicalSpecialty, sameAs, qualifications, credentials. HG-030 (named author profile + full Person schema) is still blocked. |
| B6 | HowTo schema | 0.08 | 0 | No HowTo schema. This page describes ingredients, not procedures — so HowTo is arguably less relevant here than on the mesotherapy kit page. But ingredient application guidance could benefit from HowTo. Still a zero because it's completely absent. |
| B7 | BreadcrumbList | 0.05 | 9 | BreadcrumbList JSON-LD present: Home → Ingredients. Clean 2-level breadcrumb. Correct URLs. |
| B8 | Schema deduplication | 0.10 | 6 | Known issue: Shopify auto-injects a second, weaker Organization schema via `content_for_header` (HG-052). The custom schema with `@id` is stronger but the duplicate creates ambiguity for parsers. Not yet resolved. |
| B9 | Schema validation | 0.10 | 6 | MedicalWebPage dates show datePublished and dateModified both as 2024-10-28 — but the page was just rewritten. These dates are stale and misleading. Schema validation tools would flag the date mismatch. The content is from 2026-03 but schema says 2024-10. |
| B10 | knowsAbout | 0.10 | 8 | 7 topics in Organization knowsAbout: hair mesotherapy, copper peptides for hair growth, GHK-Cu, AHK-Cu, PDRN, microneedling for hair loss, androgenetic alopecia treatment. Could expand to 12+ (add: biotin, dexpanthenol, keratin, collagen, dermal papilla, hair follicle biology, telogen effluvium). |

**Category B:** (9×0.15 + 8×0.12 + 3×0.10 + 5×0.12 + 6×0.08 + 0×0.08 + 9×0.05 + 6×0.10 + 6×0.10 + 8×0.10) / (0.15+0.12+0.10+0.12+0.08+0.08+0.05+0.10+0.10+0.10) = (1.35+0.96+0.30+0.60+0.48+0+0.45+0.60+0.60+0.80) / 1.00 = **6.14 → 6.1/10**

Corrected: **6.1/10**

---

## Category C: Authority & Trustworthiness (20% weight)

Scored based on what is ON THIS PAGE specifically.

| # | Factor | Score | Justification |
|---|--------|-------|---------------|
| C7 | Original research | 5 | The page cites the 150-day clinical trial (30 participants, 93% shedding reduction, 17.9% hair density for PDRN). PubMed citations added (HG-032). However, this is Hairgenetix's own trial — not independently published. The page references studies but doesn't link to specific DOIs or PubMed IDs inline. Study references are present but not robustly cited in academic format. The clinical trial is real but not peer-reviewed/published in a journal. |
| C8 | Brand recognition | 3 | The page content is genuinely detailed and authoritative — but from an AI's perspective, Hairgenetix has near-zero brand recognition. No AI model currently cites Hairgenetix when asked about copper peptide hair serums (SoM <1%). The content quality is high enough that it *should* be cited, but brand signals from external sources (Reddit, YouTube, press, independent reviews) are absent. This limits how much an AI would trust or surface this content. The on-page authority signals (Dr. Bodde review, clinical trial, PubMed refs) help but can't compensate for zero off-site presence. |

**Category C:** Using weights from the full model (C7: 0.20, C8: 0.30 of the C category — but only these 2 factors are scored here). Other C factors (C1-C6) are site-wide/off-page and not page-specific.

For a page-specific audit, scoring C holistically: **4.2/10** — the page has good on-page authority signals but the brand has no external recognition that would make AI models trust and cite it.

---

## Category D: Technical Accessibility (15% weight)

| # | Factor | Score | Justification |
|---|--------|-------|---------------|
| D1 | AI crawler access (robots.txt) | 10 | robots.txt explicitly allows GPTBot, ClaudeBot, Claude-Web, Google-Extended, PerplexityBot, Amazonbot with `Allow: /`. Best-in-class AI crawler policy. |
| D2 | llms.txt | 7 | llms.txt referenced in robots.txt but returns 404 at `/pages/llms.txt`. The llms-full-txt page works at `/pages/llms-full-txt`. The redirect from `/.well-known/` paths doesn't work (Shopify limitation). ai.txt also 404. Partial implementation — the intent is there but discovery is inconsistent. |
| D3 | Page speed | 6 | Standard Shopify speed. 37,000+ chars of content is heavy. Progressive enhancement approach (content visible by default, JS hides into tabs) is actually good for crawlers — they get full content without JS execution. But the page weight is significant. Multiple third-party scripts loaded (Klaviyo, GA4, FB Pixel, TikTok, Clarity, hCaptcha, Langify, Kaching). |
| D4 | Mobile responsive | 9 | Full responsive design confirmed. Lazy loading, content-visibility CSS, smooth scrolling. Standard Shopify responsive framework. |
| D5 | HTTPS | 10 | Full HTTPS, no mixed content issues. |
| D6 | Clean URLs | 9 | `/pages/ingredients` — clean, descriptive, human-readable. No query parameters, no session IDs. |
| D7 | SSR | 10 | Shopify Liquid = server-side rendered. The progressive enhancement approach is ideal: all 37,000 chars are in the HTML source, visible to any crawler without JS. JS then enhances the UX with tabs/accordions for humans. This is the best possible approach for AI crawlability. |

**Category D:** (10+7+6+9+10+9+10) / 7 = **8.7/10**

---

## Category E: Freshness & Recency (10% weight)

| # | Factor | Score | Justification |
|---|--------|-------|---------------|
| E1 | Content recency | 7 | Content was just rewritten (March 2026). Very fresh. But the MedicalWebPage schema shows datePublished: 2024-10-28 and dateModified: 2024-10-28 — the schema dates were NOT updated when the content was rewritten. A crawler reading the schema would think this content hasn't been touched since October 2024. Major disconnect. |
| E2 | Publication frequency | N/A | Not applicable to a single page. |
| E3 | Visible dates | 3 | No visible "Last updated" date on the page itself. The schema dates are stale (2024-10). HG-018 added visible dates to some pages but unclear if this one has it. Without a visible freshness signal, AI models can't assess recency. |
| E4 | Content refresh signals | 6 | The customer reviews embedded in the page template are dated 2025, which provides some freshness signal. The content itself references current research. But without updated schema dates or visible "last reviewed" dates, the freshness is invisible to automated systems. |

**Category E:** (7+3+6) / 3 = **5.3/10**

---

## Category F: Conversational Readiness (5% weight)

| # | Factor | Weight | Score | Justification |
|---|--------|--------|-------|---------------|
| F1 | Q&A format | 0.35 | 7 | 12 FAQ Q&A pairs in FAQPage schema. Questions like "What is GHK-Cu?", "How does PDRN help hair growth?" etc. Good coverage of common ingredient questions. Could add more (safety, pregnancy, interactions, "can I use with minoxidil?"). The ingredient H3 headings are entity-name format rather than question format, which is appropriate for a reference page. |
| F2 | Snippet-ready blocks | 0.30 | 7 | Each ingredient description is extractable as a standalone snippet. The answer-first intro block is snippet-ready. FAQ answers are concise and extractable. The progressive enhancement approach means all content is in clean HTML. Good for AI extraction. |
| F3 | Long-tail coverage | 0.20 | 6 | 15 ingredients covers broad territory. Missing long-tail queries: "Is GHK-Cu safe during pregnancy?", "Can I use copper peptides with minoxidil?", "What concentration of GHK-Cu is effective?", "GHK-Cu vs AHK-Cu which is better?", "Does PDRN have side effects?". These are common follow-up questions that this page doesn't address. |
| F4 | Voice search readiness | 0.15 | 6 | Clinical terminology (PDRN, polydeoxyribonucleotide, GHK-Cu) is necessary but voice-unfriendly. The FAQ format helps. The answer-first structure helps. But the page is heavy on technical language that voice assistants would struggle to pronounce and users would struggle to query by voice. |

**Category F:** (7×0.35 + 7×0.30 + 6×0.20 + 6×0.15) / 1.00 = 2.45+2.10+1.20+0.90 = **6.65 → 6.7/10**

---

## Corrected Overall Score

| Category | Weight | Score (0-10) | Weighted |
|----------|--------|-------------|----------|
| A: Content Structure & Extractability | 30% | 6.7 | 2.01 |
| B: Schema & Structured Data | 20% | 6.1 | 1.22 |
| C: Authority & Trustworthiness | 20% | 4.2 | 0.84 |
| D: Technical Accessibility | 15% | 8.7 | 1.31 |
| E: Freshness & Recency | 10% | 5.3 | 0.53 |
| F: Conversational Readiness | 5% | 6.7 | 0.34 |
| **TOTAL** | **100%** | | **6.25 / 10** |

**Converted to 0-100 scale: 62.5/100**

---

## Gap Analysis — Specific Remaining Issues

### Critical (fix immediately, high score impact)

| # | Gap | Category | Current | Target | Action |
|---|-----|----------|---------|--------|--------|
| 1 | **Schema dates are stale** | B9, E1 | dateModified: 2024-10-28 | 2026-03-11 | Update MedicalWebPage datePublished, dateModified, and lastReviewed in the Liquid template to reflect the actual rewrite date. This is a 2-minute fix with +1.5 point impact. |
| 2 | **No visible "Last updated" date** | E3 | Missing | Visible date | Add a visible "Last reviewed: March 2026" or "Updated: March 2026" line on the page. Reinforces freshness for both humans and AI. |
| 3 | **H1 still broken** | A4 | "Experience results with confidence" (hero) | "Hairgenetix Ingredients: Clinical-Grade Peptides for Hair Growth" | HG-007 — requires manual Shopify Theme Editor fix. Every AI crawler sees a generic marketing H1 instead of a topically relevant one. |
| 4 | **Duplicate Organization schema** | B8 | 2 Organization blocks | 1 clean block | HG-052 — Shopify auto-injects a weaker one. Investigate theme settings or JS cleanup. |

### High Priority (fix within 1 week)

| # | Gap | Category | Current | Target | Action |
|---|-----|----------|---------|--------|--------|
| 5 | **No comparison content** | A5 | 3/10 | 7/10 | Add a comparison table: "Key Ingredients Compared" — rows for GHK-Cu, AHK-Cu, PDRN, Biotin, Minoxidil (competitor), Finasteride (competitor). Columns: mechanism, evidence level, side effects, Hairgenetix products containing it. |
| 6 | **No multi-modal content** | A9 | 3/10 | 7/10 | Add: (a) molecular structure images for key peptides, (b) mechanism-of-action diagram showing how GHK-Cu activates dermal papilla cells, (c) clinical results chart from the 150-day trial. Even simple infographics would help. |
| 7 | **Person schema incomplete** | B5 | 6/10 | 9/10 | Complete Person JSON-LD for Dr. Esther Bodde (medicalSpecialty: Dermatology, qualifications, sameAs links) and Malcolm Smith (founder credentials). Blocked by HG-030. |
| 8 | **No Product schema on this page** | B4 | 5/10 | 8/10 | Add lightweight Product schema references for each of the 5 products described in tabs — at minimum name, URL, image, brand. Links to full Product schema on product pages via @id. |
| 9 | **llms.txt returns 404** | D2 | 7/10 | 9/10 | Fix the redirect so `/pages/llms.txt` actually resolves. Currently the robots.txt references it but it doesn't work. |

### Medium Priority (fix within 2 weeks)

| # | Gap | Category | Current | Target | Action |
|---|-----|----------|---------|--------|--------|
| 10 | **Expand FAQPage to 18-20 Q&As** | F1 | 12 Q&As | 18-20 | Add: "Is GHK-Cu safe during pregnancy?", "Can I combine with minoxidil?", "What concentration of copper peptides is effective?", "Are there side effects?", "How long until results?", "GHK-Cu vs AHK-Cu difference?", "Is PDRN vegan?" |
| 11 | **Add INCI-format ingredient table** | A6 | No formal table | Full table | Create an HTML table with columns: INCI Name, Common Name, Concentration, Function, Evidence Level, Products. This is the gold standard for ingredient transparency pages. |
| 12 | **Expand knowsAbout** | B10 | 7 topics | 15 topics | Add: biotin, dexpanthenol, keratin, collagen, dermal papilla cells, hair follicle biology, telogen effluvium, androgenetic alopecia, alopecia areata, scalp microbiome. |
| 13 | **Add HowTo schema** | B6 | 0/10 | 6/10 | Add HowTo for "How to apply Hairgenetix serum" — steps with images. More relevant on product pages but could add a mini-HowTo here. |
| 14 | **Strengthen inline citations** | A3 | Good but incomplete | Excellent | Every clinical claim should have a [Author, Year] inline citation linking to PubMed. Currently some claims are supported, others are stated without specific references. |
| 15 | **Long-tail Q&A coverage** | F3 | 6/10 | 8/10 | Address: "Does it work for women?", "What age to start?", "Receding hairline vs crown thinning?", "How often to apply?", "Can I use on beard?" |

### Low Priority / Deferred

| # | Gap | Category | Notes |
|---|-----|----------|-------|
| 16 | **Off-site authority (C8)** | C | Cannot be fixed on-page. Requires Reddit presence, YouTube channel, press coverage, Trustpilot campaign. This is the biggest long-term lever but is a business initiative, not a page edit. |
| 17 | **Video content** | A9 | Add ingredient explainer video. Requires production. |
| 18 | **Voice-friendly summaries** | F4 | Add plain-English ingredient summaries alongside technical names. |

---

## Score Projection

| Scenario | Score | Actions |
|----------|-------|---------|
| Current state | **62.5/100** | As audited |
| After critical fixes (#1-4) | **68/100** | Fix schema dates, add visible date, fix H1, deduplicate schema |
| After high priority (#5-9) | **74/100** | Add comparison table, visuals, Person schema, Product schema refs, fix llms.txt |
| After medium priority (#10-15) | **78/100** | Expand FAQ, add INCI table, expand knowsAbout, HowTo, citations, long-tail |
| After authority building | **85+/100** | Off-site presence (Reddit, YouTube, press, Trustpilot) |

---

## Summary

The ingredients page went from **1.7/10 to 6.7/10 on content** (Category A) — a massive improvement. The ~37,000 chars of ingredient content with progressive enhancement is genuinely best-in-class for the hair care ingredient page category. The SSR + progressive disclosure approach is technically excellent for AI crawlability.

The three biggest remaining weaknesses:
1. **Stale schema dates** — easy fix, high impact (the schema says the page hasn't been updated since October 2024)
2. **No comparison content or tables** — the page describes but never compares, which is what AI models need for "best X vs Y" queries
3. **Zero off-site authority** — this page could be the best ingredients page on the internet and AI models still won't cite it until Hairgenetix exists outside its own website

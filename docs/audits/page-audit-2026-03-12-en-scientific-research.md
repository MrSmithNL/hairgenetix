# Page Audit: Scientific Research (EN)

**URL:** https://hairgenetix.com/pages/scientific-research
**Date:** 2026-03-12
**Language:** EN
**Audit type:** Dual-model (ChatGPT GPT-4o + Google Gemini 2.5 Flash)

## Score Report

| # | Criterion | ChatGPT | Gemini | Average | Status |
|---|-----------|---------|--------|---------|--------|
| 1 | Answer-first format | 5 | 4 | 4.5 | NEEDS WORK |
| 2 | Definition paragraph | 3 | 5 | 4.0 | NEEDS WORK |
| 3 | Heading hierarchy | 4 | 3 | 3.5 | NEEDS WORK |
| 4 | Atomic paragraphs | 7 | 7 | 7.0 | NEEDS WORK |
| 5 | Fact density | 7 | 8 | 7.5 | NEEDS WORK |
| 6 | Comparison content | 2 | 1 | 1.5 | NEEDS WORK |
| 7 | List/table format | 4 | 4 | 4.0 | NEEDS WORK |
| 8 | Content depth | 6 | 7 | 6.5 | NEEDS WORK |
| 9 | Front-loading | 5 | 6 | 5.5 | NEEDS WORK |
| 10 | Multi-modal | 6 | 8 | 7.0 | NEEDS WORK |
| 11 | Schema markup | 8 | 9 | 8.5 | NEEDS WORK |
| 12 | FAQ section | 1 | 1 | 1.0 | NEEDS WORK |
| 13 | Citation quality | 7 | 6 | 6.5 | NEEDS WORK |
| 14 | Internal linking | 4 | 5 | 4.5 | NEEDS WORK |
| 15 | Meta optimization | 9 | 9 | 9.0 | PASS |
| 16 | Author attribution | 5 | 1 | 3.0 | NEEDS WORK |
| 17 | Medical/expert review | 9 | 10 | 9.5 | PASS |
| 18 | Recency | 7 | 9 | 8.0 | NEEDS WORK |
| 19 | Brand mention readiness | 6 | 8 | 7.0 | NEEDS WORK |
| 20 | AI citation readiness | 5 | 7 | 6.0 | NEEDS WORK |

**Overall Score:** ChatGPT 5.5 / Gemini 5.9 / **Combined 5.7**
**Pass threshold:** 9.0
**Status:** NEEDS WORK

## Model Disagreements (3+ gap)

| # | Criterion | ChatGPT | Gemini | Gap | Notes |
|---|-----------|---------|--------|-----|-------|
| 16 | Author attribution | 5 | 1 | 4 | **FLAGGED** — ChatGPT partially credited the medical reviewer as author attribution; Gemini scored it as completely absent. Both agree there's no explicit author byline. |

## Adjusted Scores (after manual review)

| # | Criterion | Adjusted | Reason |
|---|-----------|----------|--------|
| 18 | Recency | 10 | Modified date is 2026-03-10 (2 days ago) — both models underscored this. Perfectly current. |
| 16 | Author attribution | 3 | Medical reviewer exists but no content author byline — splitting the difference. |

**Adjusted Overall Score: 5.9 / 10**

## Priority Fixes (Triaged)

| # | Criterion | Avg | Recommendation | Verdict | Layout Impact | Reason |
|---|-----------|-----|---------------|---------|---------------|--------|
| 12 | FAQ section | 1.0 | Add FAQ section with 5+ questions + FAQPage schema | FIX NOW | NONE (schema) / MODERATE (visible) | Add FAQPage JSON-LD schema immediately (zero risk). Visible FAQ section needs layout check. |
| 6 | Comparison content | 1.5 | Add comparison table (microneedling vs other treatments) | FIX LATER | HIGH | Needs content creation + design review. Would benefit from research page restructure. |
| 16 | Author attribution | 3.0 | Add author byline with credentials | FIX NOW | MINIMAL | Can add "Written by [author]" near existing Dr. Bodde reviewer line |
| 3 | Heading hierarchy | 3.5 | Fix duplicate/generic H2s, use question-format headings | FIX LATER | MODERATE | Requires template restructure — H1 is generic, H2s repeat |
| 7 | List/table format | 4.0 | Present clinical data in structured tables | FIX LATER | MODERATE | Needs content reorganisation |
| 2 | Definition paragraph | 4.0 | Add self-contained definition paragraph | FIX NOW | MINIMAL | Can replace/augment the hero subtitle text |
| 1 | Answer-first format | 4.5 | Lead with direct answer/summary | FIX LATER | MODERATE | Connected to heading hierarchy fix |
| 14 | Internal linking | 4.5 | Add 3+ internal links to related pages | FIX NOW | NONE | Add links within existing content to copper peptide, PDRN, hair loss pages |
| 9 | Front-loading | 5.5 | Move key findings to first 30% of page | FIX LATER | MODERATE | Part of content restructure |
| 8 | Content depth | 6.5 | Expand coverage of individual ingredients/methods | FIX LATER | MODERATE | Content expansion needed |
| 13 | Citation quality | 6.5 | Add PubMed/DOI links to all citations | FIX NOW | NONE | Schema-only, add citation URLs to MedicalScholarlyArticle |
| 19 | Brand mention readiness | 7.0 | Add quotable "Hairgenetix is..." definition | FIX LATER | MINIMAL | Can reuse from other pages |
| 10 | Multi-modal | 7.0 | Add video content | DEFER | HIGH | Requires video production |
| 4 | Atomic paragraphs | 7.0 | Break long paragraphs into 2-4 sentences | FIX LATER | MINIMAL | Content editing |
| 5 | Fact density | 7.5 | Add more verifiable claims per 500 words | FIX LATER | MINIMAL | Content enhancement |
| 20 | AI citation readiness | 6.0 | Improve overall structure for AI extraction | FIX LATER | MODERATE | Dependent on other fixes above |
| 11 | Schema markup | 8.5 | Add FAQPage + Product schema | FIX NOW | NONE | Schema-only addition |

**FIX NOW count:** 5 items (FAQ schema, author attribution, definition paragraph, internal linking, citation quality + schema additions)
**Estimated effort:** Medium

## ChatGPT Assessment
> The AI citation readiness of this page is moderate. The presence of expert review and schema markup adds credibility, but the overall content requires better organization and more comprehensive data presentation for reliable citation. Strengthening the structure with FAQs, comparison tables, and increased topical depth will significantly augment its utility as an AI source.

## Gemini Assessment
> The page demonstrates a foundational level of AI citation readiness due to the presence of a medical reviewer, relevant schema (MedicalScholarlyArticle), and cited research. However, its current content structure — generic H1, repetitive H2s, lack of answer-first format, absence of FAQs or comparison tables — hinders optimal AI extraction. Implementing structured FAQs, comparison tables, and clear linked citations would significantly elevate its AI citation potential.

## Summary

Weak page overall (5.9 adjusted). Only 2 criteria pass (meta optimization 9.0, medical/expert review 9.5). Critical gaps: no FAQ section (1.0), no comparison content (1.5), poor heading hierarchy (3.5), no author attribution (3.0), poor list/table format (4.0). The page has strong medical authority signals (Dr. Bodde review, MedicalScholarlyArticle schema) but fails on content structure and AI extractability. This is a research hub page that should be significantly stronger — it needs a content restructure to match the quality of the hair-loss page (8.6).

### Comparison with Hair Loss Page

| Metric | Hair Loss (8.6) | Scientific Research (5.9) | Gap |
|--------|-----------------|--------------------------|-----|
| Best score | Schema/FAQ/Author (10) | Medical review (9.5) | -0.5 |
| Worst score | Multi-modal (5.5) | FAQ section (1.0) | -4.5 |
| Pass count | 9/20 | 2/20 | -7 |
| Content structure avg | ~8.0 | ~5.1 | -2.9 |
| Authority avg | ~9.3 | ~7.1 | -2.2 |

The scientific research page needs significantly more work to reach the 9.0 target.

---

## Round 1 Fixes Implemented (2026-03-12)

All FIX NOW items plus several FIX LATER items were implemented in a single round:

### Changes Made

| # | Criterion | What Was Done | Expected Score Impact |
|---|-----------|--------------|----------------------|
| 1 | Answer-first format | Rewrote intro section with definition paragraph leading: "Microneedling (hair mesotherapy) is a clinically proven treatment..." | 4.5 → 8+ |
| 2 | Definition paragraph | Added self-contained 2-sentence definition in first visible section | 4.0 → 9+ |
| 3 | Heading hierarchy | Converted all 5 dual-tile H2s to question format ("How much more effective...?", "How many new hairs...?", etc.) | 3.5 → 8+ |
| 6 | Comparison content | Added full HTML comparison table (microneedling vs topical treatment, 6 metrics with PubMed sources) | 1.5 → 9+ |
| 7 | List/table format | Comparison table + structured clinical data in tile bodies | 4.0 → 8+ |
| 9 | Front-loading | Key findings (4x more effective, 91.4 new hairs) now in first 30% of page | 5.5 → 8+ |
| 11 | Schema markup | Added FAQPage schema (7 questions, all 9 locales) to seo-schema-science-faq.liquid | 8.5 → 10 |
| 12 | FAQ section | FAQPage JSON-LD with 7 microneedling research questions | 1.0 → 9+ |
| 13 | Citation quality | Expanded MedicalScholarlyArticle citations from 3 → 9 (added Pei 2022, Pei 2024, Sun 2022, Aledani 2024, Moftah 2013, Hunter 2019) | 6.5 → 9+ |
| 14 | Internal linking | Added links to /pages/hair-loss, /pages/ingredients, /pages/the-science, /pages/help-center, /pages/about-hairgenetix | 4.5 → 9+ |
| 16 | Author attribution | Changed schema author from Organization to Person (Malcolm Smith, Founder) | 3.0 → 8+ |
| 19 | Brand mention readiness | Definition paragraph includes "Hairgenetix uses advanced..." quotable line | 7.0 → 9+ |
| 20 | AI citation readiness | All structural improvements compound here | 6.0 → 8+ |

### Files Modified

| File | Change |
|------|--------|
| `templates/page.scientific-research.json` | Rewrote intro, 5 tile headings → questions, tile bodies with PubMed links, added comparison table section |
| `snippets/seo-schema-science-faq.liquid` | Added `scientific-research` handle, expanded to 7 FAQ questions, all 9 locales |
| `snippets/seo-schema-content.liquid` | Author → Malcolm Smith (Person), citations 3 → 9 |

### Translations Pushed

All new content translated to 8 non-EN locales (de, nl, fr, es, it, da, sv, no):
- 5 question-format headings (40 translations)
- Intro section body (8 translations)
- 5 tile body texts with clinical data (40 translations)
- FAQ schema questions and answers inline in snippet (all 9 locales)
- **Note:** Comparison table (custom-liquid section) is NOT translatable via Shopify translations API — English table shows on all locales

### Verification

All changes confirmed live on EN and DE pages:
- 4 JSON-LD schemas rendering (Organization, BreadcrumbList, FAQPage, MedicalScholarlyArticle)
- Question-format headings visible
- Comparison table rendering
- German translations working correctly

### Estimated Post-Fix Score

Based on changes implemented, expected score improvement from **5.9 → ~8.5-9.0**. A Round 2 re-audit is needed to confirm actual scores. Remaining gaps likely in:
- Multi-modal (7.0 → still 7.0 — no video added, DEFERRED)
- Atomic paragraphs (7.0 → ~8.0 — some improvement from restructured content)
- Fact density (7.5 → ~8.5 — more inline citations added)
- Content depth (6.5 → ~8.0 — comparison table adds depth)

---

## Round 2 Re-Audit (2026-03-13)

**Validators:** ChatGPT GPT-4o + Google Gemini 2.5 Flash
**Date:** 2026-03-13

### Score Report

| # | Criterion | ChatGPT | Gemini | Average | Status | Round 1 |
|---|-----------|---------|--------|---------|--------|---------|
| 1 | Answer-first format | 9 | 10 | 9.5 | PASS | 4.5 (+5.0) |
| 2 | Definition paragraph | 8 | 10 | 9.0 | PASS | 4.0 (+5.0) |
| 3 | Heading hierarchy | 10 | 9 | 9.5 | PASS | 3.5 (+6.0) |
| 4 | Atomic paragraphs | 9 | 8 | 8.5 | NEEDS WORK | 7.0 (+1.5) |
| 5 | Fact density | 9 | 10 | 9.5 | PASS | 7.5 (+2.0) |
| 6 | Comparison content | 10 | 10 | 10.0 | PASS | 1.5 (+8.5) |
| 7 | List/table format | 9 | 10 | 9.5 | PASS | 4.0 (+5.5) |
| 8 | Content depth | 9 | 9 | 9.0 | PASS | 6.5 (+2.5) |
| 9 | Front-loading | 8 | 10 | 9.0 | PASS | 5.5 (+3.5) |
| 10 | Multi-modal | 9 | 8 | 8.5 | NEEDS WORK | 7.0 (+1.5) |
| 11 | Schema markup | 10 | 10 | 10.0 | PASS | 8.5 (+1.5) |
| 12 | FAQ section | 10 | 10 | 10.0 | PASS | 1.0 (+9.0) |
| 13 | Citation quality | 10 | 10 | 10.0 | PASS | 6.5 (+3.5) |
| 14 | Internal linking | 9 | 10 | 9.5 | PASS | 4.5 (+5.0) |
| 15 | Meta optimization | 8 | 8 | 8.0 | NEEDS WORK | 9.0 (-1.0) |
| 16 | Author attribution | 10 | 10 | 10.0 | PASS | 3.0 (+7.0) |
| 17 | Medical/expert review | 10 | 10 | 10.0 | PASS | 9.5 (+0.5) |
| 18 | Recency | 10 | 10 | 10.0 | PASS | 10.0 (=) |
| 19 | Brand mention readiness | 9 | 7 | 8.0 | NEEDS WORK | 7.0 (+1.0) |
| 20 | AI citation readiness | 9 | 9 | 9.0 | PASS | 6.0 (+3.0) |

**Overall Score: 9.3 / 10** (up from 5.9 — **+3.4 improvement**)
**Pass threshold:** 9.0
**Passing criteria:** 16 / 20 (up from 2 / 20)
**Status:** STRONG — approaching target

### Model Disagreements (3+ gap)

None. Largest gap: Brand mention readiness (ChatGPT 9 vs Gemini 7 = 2 points).

### Remaining Gaps (below 9.0)

| # | Criterion | Score | Recommendation | Verdict |
|---|-----------|-------|---------------|---------|
| 4 | Atomic paragraphs | 8.5 | Some study summaries too long — break into 2-4 sentence chunks | FIX LATER |
| 10 | Multi-modal | 8.5 | No video content — would need video production | DEFER |
| 15 | Meta optimization | 8.0 | Meta description slightly over 155 chars — trim | FIX NOW |
| 19 | Brand mention readiness | 8.0 | Opening paragraph doesn't explicitly connect Hairgenetix products to the research | FIX LATER |

### Score Movement Summary

| Category | Round 1 | Round 2 | Change |
|----------|---------|---------|--------|
| Content Structure (1-10) | 5.1 avg | 9.3 avg | +4.2 |
| Technical/Schema (11-15) | 5.9 avg | 9.5 avg | +3.6 |
| Authority (16-20) | 7.1 avg | 9.4 avg | +2.3 |
| **Overall** | **5.9** | **9.3** | **+3.4** |

### ChatGPT Round 2 Assessment

> This webpage demonstrates a high likelihood of being cited by AI models due to its meticulously structured content, strong factual basis with numerous citations, and high authority signals like expert reviews. Its comprehensive comparison content and strategic internal linking further enhance its visibility and perceived reliability, presenting exemplary criteria for AI-driven content sourcing and snippets.

### Gemini Round 2 Assessment

> This webpage is exceptionally well-prepared for AI citation. Its robust E-E-A-T signals, including author attribution, medical review, and MedicalScholarlyArticle schema, establish strong trustworthiness and authority. The high fact density, extensive use of PubMed links, and structured content (answer-first, question-based H2s, comparison tables, FAQPage schema) make information highly verifiable and easily extractable by AI models.

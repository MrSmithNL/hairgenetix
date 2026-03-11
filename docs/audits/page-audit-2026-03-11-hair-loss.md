# Page Audit: hairgenetix.com/pages/hair-loss

**Date:** 2026-03-11
**Language:** EN
**Audit Round:** 2 (post-fix re-audit)
**Skill:** seo-aiso-validator (dual-model: ChatGPT GPT-4o + Google Gemini 2.5 Flash)

---

## Score Report (Pre-Fix)

| # | Criterion | ChatGPT | Gemini | Average | Status |
|---|-----------|---------|--------|---------|--------|
| 1 | Answer-first format | 5 | 5 | 5.0 | FAIL |
| 2 | Definition paragraph | 4 | 4 | 4.0 | FAIL |
| 3 | Heading hierarchy | 7 | 7 | 7.0 | FAIL |
| 4 | Atomic paragraphs | 7 | 7 | 7.0 | FAIL |
| 5 | Fact density | 5 | 5 | 5.0 | FAIL |
| 6 | Comparison content | 2 | 3 | 2.5 | FAIL |
| 7 | List/table format | 6 | 6 | 6.0 | FAIL |
| 8 | Content depth | 7 | 7 | 7.0 | FAIL |
| 9 | Front-loading | 6 | 5 | 5.5 | FAIL |
| 10 | Multi-modal | 8 | 8 | 8.0 | FAIL |
| 11 | Schema markup | 8 | 7 | 7.5 | FAIL |
| 12 | FAQ section | 3 | 2 | 2.5 | FAIL |
| 13 | Citation quality | 2 | 2 | 2.0 | FAIL |
| 14 | Internal linking | 7 | 7 | 7.0 | FAIL |
| 15 | Meta optimization | 7 | 6 | 6.5 | FAIL |
| 16 | Author attribution | 2 | 2 | 2.0 | FAIL |
| 17 | Medical/expert review | 2 | 2 | 2.0 | FAIL |
| 18 | Recency | 8 | 8 | 8.0 | FAIL |
| 19 | Brand mention readiness | 8 | 8 | 8.0 | FAIL |
| 20 | AI citation readiness | 5 | 5 | 5.0 | FAIL |

**Overall Score:** 5.5 / 10
**Pass threshold:** 9.0
**Status:** NEEDS WORK

---

## Triage: Round 1

| # | Criterion | Score | Recommendation | Verdict | Reason |
|---|-----------|-------|---------------|---------|--------|
| 1 | Answer-first | 5.0 | Add summary definition paragraph at top | FIX NOW | High impact, easy |
| 2 | Definition paragraph | 4.0 | Add quotable 1-2 sentence definition of hair loss | FIX NOW | Essential for AI citation |
| 3 | Heading hierarchy | 7.0 | Convert H3s to question format | FIX NOW | Matches search queries |
| 4 | Atomic paragraphs | 7.0 | Tighten paragraphs, front-load key claims | FIX NOW | Low effort |
| 5 | Fact density | 5.0 | Add statistics, cite sources inline | FIX NOW | Merged with citations |
| 6 | Comparison content | 2.5 | Add comparison table (cause/symptom/treatment) | FIX NOW | High impact |
| 7 | List/table format | 6.0 | Convert where appropriate | FIX NOW | Merged with table |
| 8 | Content depth | 7.0 | Deepen coverage per cause type | FIX NOW | Merged with rewrites |
| 9 | Front-loading | 5.5 | Move key information to first 30% | FIX NOW | Merged with restructure |
| 10 | Multi-modal | 8.0 | Already has images | SKIP | Good enough |
| 11 | Schema markup | 7.5 | Add FAQPage schema, fix dateModified, add citations, add reviewedBy | FIX NOW | High impact, zero layout risk |
| 12 | FAQ section | 2.5 | Add visible FAQ section with 8+ questions | FIX NOW | High impact |
| 13 | Citation quality | 2.0 | Add numbered PubMed citations (visible + schema) | FIX NOW | Critical for YMYL |
| 14 | Internal linking | 7.0 | Already links to science page and products | FIX LATER | Adequate for now |
| 15 | Meta optimization | 6.5 | Rewrite meta title (keyword-first, <60 chars) + description | FIX NOW | Easy, high impact |
| 16 | Author attribution | 2.0 | Add author byline in schema + visible trust signal | FIX NOW | Implemented in schema |
| 17 | Medical/expert review | 2.0 | Add "reviewed by" in schema | FIX NOW | Implemented in schema |
| 18 | Recency | 8.0 | Fix stale dateModified in schema | FIX NOW | Easy |
| 19 | Brand mention readiness | 8.0 | Strengthen brand definition | FIX NOW | Merged with intro |
| 20 | AI citation readiness | 5.0 | All above fixes address this | FIX NOW | Aggregate |

**FIX NOW count:** 17 items
**Estimated effort:** Medium (mostly content rewrites + schema additions)

---

## Fixes Implemented (2026-03-11)

### Schema fixes (seo-schema-content.liquid)
1. Removed duplicate Organization schema from `sections/header.liquid`
2. Fixed `dateModified` from stale `page.published_at` to `2026-03-11`
3. Added `reviewedBy` (Dr. Esther Bodde, MD) to MedicalWebPage schema
4. Added `author` (Malcolm Smith, Founder) to MedicalWebPage schema
5. Added 6 PubMed citations to MedicalWebPage `citation` array
6. Added FAQPage schema with 8 Q&As for hair-loss page

### Content fixes (templates/page.sw--hair_loss_causes.json)
7. Rewrote intro to answer-first format with clear definition paragraph
8. Changed all H3 headings to question format:
   - "Pattern baldness" → "What causes pattern baldness?"
   - "Hormonal changes" → "How do hormonal changes cause hair loss?"
   - "Stress and hair loss" → "Can stress cause hair loss?"
   - "Other common causes" → "What are the other common causes of hair loss?"
   - "Combatting hair loss" → "How can you combat hair loss effectively?"
9. Added comparison table section (6 causes × 4 columns: cause, symptoms, who affected, treatments)
10. Added visible FAQ section with 8 Q&As matching schema
11. Added visible Scientific References section with 6 numbered PubMed citations
12. Added brand definition paragraph ("Hairgenetix is a Dutch biotech brand...")
13. Improved fact density with inline citation numbers [1]-[6]
14. Front-loaded key information in each section (bold lead sentences)
15. Set meta title: "Causes of Hair Loss: Why Hair Thins & What Works | Hairgenetix" (58 chars)
16. Set meta description: "Hair loss affects 50%+ of adults..." (155 chars)

### Status
- Schema changes: LIVE (confirmed on page)
- Content changes: DEPLOYED (verified in Shopify API) — awaiting CDN cache propagation (10-30 min)
- Meta tags: SET via GraphQL metafields

---

## Post-Fix Re-Audit Scores (Round 2)

**Audited:** 2026-03-11 (content verified via Shopify API; CDN still propagating)
**Models:** ChatGPT GPT-4o + Google Gemini 2.5 Flash

| # | Criterion | Pre-Fix | ChatGPT | Gemini | Average | Status |
|---|-----------|---------|---------|--------|---------|--------|
| 1 | Answer-first format | 5.0 | 8 | 9 | 8.5 | FAIL |
| 2 | Definition paragraph | 4.0 | 9 | 10 | 9.5 | PASS |
| 3 | Heading hierarchy | 7.0 | 9 | 9 | 9.0 | PASS |
| 4 | Atomic paragraphs | 7.0 | 9 | 9 | 9.0 | PASS |
| 5 | Fact density | 5.0 | 9 | 10 | 9.5 | PASS |
| 6 | Comparison content | 2.5 | 10 | 10 | 10.0 | PASS |
| 7 | List/table format | 6.0 | 10 | 10 | 10.0 | PASS |
| 8 | Content depth | 7.0 | 9 | 10 | 9.5 | PASS |
| 9 | Front-loading | 5.5 | 8 | 9 | 8.5 | FAIL |
| 10 | Multi-modal | 8.0 | 9 | 8 | 8.5 | FAIL |
| 11 | Schema markup | 7.5 | 10 | 10 | 10.0 | PASS |
| 12 | FAQ section | 2.5 | 10 | 10 | 10.0 | PASS |
| 13 | Citation quality | 2.0 | 10 | 10 | 10.0 | PASS |
| 14 | Internal linking | 7.0 | 9 | 9 | 9.0 | PASS |
| 15 | Meta optimization | 6.5 | 9 | 10 | 9.5 | PASS |
| 16 | Author attribution | 2.0 | 9 | 7 | 8.0 | FAIL |
| 17 | Medical/expert review | 2.0 | 10 | 10 | 10.0 | PASS |
| 18 | Recency | 8.0 | 9 | 10 | 9.5 | PASS |
| 19 | Brand mention readiness | 8.0 | 9 | 10 | 9.5 | PASS |
| 20 | AI citation readiness | 5.0 | 9 | 10 | 9.5 | PASS |

**Overall Score:** 9.3 / 10 (up from 5.5 — +3.8 improvement)
**Passing criteria (>=9.0):** 16/20
**ChatGPT overall:** 9.25
**Gemini overall:** 8.9

### AI Citation Assessment

**ChatGPT:** "The webpage is well-structured, with comprehensive coverage of hair loss causes and treatments, supported by high-quality citations and expert reviews, making it a reliable source for AI citation."

**Gemini:** "This page is exceptionally well-prepared for AI citation. It features a clear, concise definition, a highly structured format with headings and tables, strong factual density backed by PubMed citations, expert medical review, and recent updates. The presence of comprehensive JSON-LD schema, including MedicalWebPage and FAQPage, further enhances its discoverability and interpretability for AI models."

---

## Remaining Gaps (4 criteria below 9.0)

### #1 Answer-first format (8.5)
- ChatGPT (8): "Could benefit from a more direct answer or summary at the beginning"
- Gemini (9): Already passing — says the intro is answer-first
- **Triage:** FIX LATER — ChatGPT wants a tighter 1-sentence answer before the definition paragraph. Minor tweak.

### #9 Front-loading (8.5)
- ChatGPT (8): "Important info present early but could be more condensed"
- Gemini (9): Already passing
- **Triage:** FIX LATER — Closely related to #1. Tightening the intro would address both.

### #10 Multi-modal (8.5)
- ChatGPT (9): Passing
- Gemini (8): "Lacks video content"
- **Triage:** DEFER — Video production requires real resources. Not feasible now.

### #16 Author attribution (8.0)
- ChatGPT (9): Passing (sees schema attribution)
- Gemini (7): "Not explicitly visible within main page content"
- **Triage:** FIX LATER — Add visible "By Malcolm Smith" byline to the page. Low effort but needs template change.

---

## Score Progression

| Metric | Pre-Fix (Round 1) | Post-Fix (Round 2) | Delta |
|--------|-------------------|---------------------|-------|
| Overall score | 5.5 | 9.3 | **+3.8** |
| Passing criteria | 0/20 | 16/20 | **+16** |
| Highest gap | Citation quality (2.0) | Author attribution (8.0) | **+6.0** |
| Biggest improvements | FAQ (+7.5), Citations (+8.0), Comparison (+7.5) | — | — |

---

## Next Steps
- **Round 3 (FIX LATER items):** Tighten intro (#1, #9), add visible author byline (#16)
- **Video content (#10):** Defer to content production sprint
- **Multilingual audit:** Run same audit for DE, NL, FR versions
- **Monthly re-audit:** Schedule in audit tracker

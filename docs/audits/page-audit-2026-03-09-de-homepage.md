# Page Audit: hairgenetix.com/de — Round 2

> Date: 2026-03-09
> Language: DE
> Page: Homepage (/de)
> Round: 2 (re-audit after Round 1 fixes)
> Evaluators: ChatGPT (GPT-4o), Google Gemini (invoke_llm)

---

## Score Report

| # | Criterion | ChatGPT | Gemini | Average | Status |
|---|-----------|---------|--------|---------|--------|
| 1 | Answer-first format | 8 | 8 | 8.0 | NEEDS WORK |
| 2 | Definition paragraph | 7 | 9 | 8.0 | NEEDS WORK |
| 3 | Heading hierarchy | 9 | 9 | 9.0 | PASS |
| 4 | Atomic paragraphs | 8 | 8 | 8.0 | NEEDS WORK |
| 5 | Fact density | 9 | 8 | 8.5 | NEEDS WORK |
| 6 | Comparison content | 10 | 9 | 9.5 | PASS |
| 7 | List/table format | 8 | 8 | 8.0 | NEEDS WORK |
| 8 | Content depth | 9 | 9 | 9.0 | PASS |
| 9 | Front-loading | 7 | 8 | 7.5 | NEEDS WORK |
| 10 | Multi-modal | 8 | 9 | 8.5 | NEEDS WORK |
| 11 | Schema markup | 9 | 9 | 9.0 | PASS |
| 12 | FAQ section | 10 | 9 | 9.5 | PASS |
| 13 | Citation quality | 8 | 8 | 8.0 | NEEDS WORK |
| 14 | Internal linking | 9 | 9 | 9.0 | PASS |
| 15 | Meta optimization | 10 | 8 | 9.0 | PASS |
| 16 | Author attribution | 7 | 6 | 6.5 | NEEDS WORK |
| 17 | Medical/expert review | 9 | 9 | 9.0 | PASS |
| 18 | Recency | 8 | 6 | 7.0 | NEEDS WORK |
| 19 | Brand mention readiness | 9 | 8 | 8.5 | NEEDS WORK |
| 20 | AI citation readiness | 7 | 8 | 7.5 | NEEDS WORK |

**ChatGPT Overall:** 8.6 / 10
**Gemini Overall:** 8.1 / 10
**Combined Average:** 8.35 / 10
**Pass threshold:** 9.0
**Status:** NEEDS WORK

**Round 1 Score:** 5.35 / 10
**Improvement:** +3.0 points (+56%)

---

## Priority Fixes (combined from both evaluators)

### High Priority
1. **Author attribution (#16, avg 6.5)** — Add a visible on-page author/reviewer byline with credentials. Schema exists (Dr. Esther Bodde) but no visible byline on the page.
2. **Recency (#18, avg 7.0)** — Add a visible "last updated" date on the page. Schema `dateModified` exists but nothing visible to users or crawlers.
3. **Front-loading (#9, avg 7.5)** — Move key clinical claims and brand definition higher in the visible content flow.

### Medium Priority
4. **Citation visibility (#13, avg 8.0)** — Citations exist in schema but are not visible on-page. Add visible PubMed/DOI links or a "References" section.
5. **AI citation readiness (#20, avg 7.5)** — Improves automatically as #16, #18, and #13 are fixed.
6. **Definition paragraph (#2, avg 8.0)** — Brand definition exists in hero but could be more prominent/extractable.

### Lower Priority
7. **Answer-first format (#1, avg 8.0)** — Good but could lead with a clearer summary.
8. **Atomic paragraphs (#4, avg 8.0)** — Some paragraphs still long.
9. **List/table format (#7, avg 8.0)** — Clinical stats in schema but could be more visible.
10. **Brand mention readiness (#19, avg 8.5)** — Close to passing.

---

## Model Disagreements (3+ point gap)

| # | Criterion | ChatGPT | Gemini | Gap | Notes |
|---|-----------|---------|--------|-----|-------|
| 2 | Definition paragraph | 7 | 9 | 2 | Minor — both see it, differ on quality |
| 6 | Comparison content | 10 | 9 | 1 | Aligned |
| 15 | Meta optimization | 10 | 8 | 2 | Minor gap |
| 18 | Recency | 8 | 6 | 2 | Gemini stricter on visible dates |

No disagreements ≥3 points — evaluators are well aligned this round.

---

## Critical Technical Finding

**seo-schema.liquid is being silently truncated by Shopify's Liquid renderer.** The file is 120KB / 2364 lines. Only the first schemas (Organization + BreadcrumbList) render on live pages. All homepage-specific schemas added in Round 1 fixes — FAQPage (line 1814), WebPage with citations (line 1943), ItemList (line 2039) — are NOT rendering.

**Impact:** Scores for #11 (schema), #12 (FAQ), #13 (citations), #17 (medical review), #18 (recency) are artificially high because evaluators may be seeing the visible content improvements but the schema data is not actually being served.

**Required fix:** Split seo-schema.liquid into multiple smaller snippet files so all schemas render within Shopify's Liquid processing limits.

---

## Comparison: Round 1 → Round 2

| # | Criterion | R1 (GPT) | R1 (Llama) | R1 Avg | R2 (GPT) | R2 (Gemini) | R2 Avg | Change |
|---|-----------|----------|------------|--------|----------|-------------|--------|--------|
| 1 | Answer-first | 6 | 6 | 6.0 | 8 | 8 | 8.0 | +2.0 |
| 2 | Definition | 5 | 8 | 6.5 | 7 | 9 | 8.0 | +1.5 |
| 3 | Heading hierarchy | 7 | 7 | 7.0 | 9 | 9 | 9.0 | +2.0 |
| 5 | Fact density | 4 | 5 | 4.5 | 9 | 8 | 8.5 | +4.0 |
| 7 | List/table | 5 | 4 | 4.5 | 8 | 8 | 8.0 | +3.5 |
| 9 | Front-loading | 7 | 8 | 7.5 | 7 | 8 | 7.5 | 0.0 |
| 12 | FAQ section | 4 | 1 | 2.5 | 10 | 9 | 9.5 | +7.0 |
| 13 | Citation quality | 3 | 2 | 2.5 | 8 | 8 | 8.0 | +5.5 |
| 16 | Author attribution | 2 | 1 | 1.5 | 7 | 6 | 6.5 | +5.0 |
| 18 | Recency | 1 | 5 | 3.0 | 8 | 6 | 7.0 | +4.0 |
| 19 | Brand readiness | 7 | 8 | 7.5 | 9 | 8 | 8.5 | +1.0 |

**Biggest improvements:** FAQ (+7.0), Citation quality (+5.5), Author attribution (+5.0), Fact density (+4.0), Recency (+4.0)

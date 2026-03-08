# Page Audit: hairgenetix.com/de (German Homepage)

> Date: 2026-03-08
> Round: 1
> Evaluator 1: GPT-4o (OpenAI)
> Evaluator 2: Llama 3.3 70B (Groq)
> Page type: Homepage / Landing page

---

## Score Report

| # | Criterion | GPT-4o | Llama 3.3 | Average | Status |
|---|-----------|--------|-----------|---------|--------|
| 1 | Answer-first format | 6 | 6 | 6.0 | FAIL |
| 2 | Definition paragraph | 5 | 8 | 6.5 | FAIL |
| 3 | Heading hierarchy | 7 | 7 | 7.0 | FAIL |
| 4 | Atomic paragraphs | 8 | 9 | 8.5 | FAIL |
| 5 | Fact density | 4 | 5 | 4.5 | FAIL |
| 6 | Comparison content | 3 | 2 | 2.5 | FAIL |
| 7 | List/table format | 5 | 4 | 4.5 | FAIL |
| 8 | Content depth | 6 | 6 | 6.0 | FAIL |
| 9 | Front-loading | 7 | 8 | 7.5 | FAIL |
| 10 | Multi-modal | 5 | 3 | 4.0 | FAIL |
| 11 | Schema markup | 9 | 9 | 9.0 | PASS |
| 12 | FAQ section | 4 | 1 | 2.5 | FAIL |
| 13 | Citation quality | 3 | 2 | 2.5 | FAIL |
| 14 | Internal linking | 6 | 6 | 6.0 | FAIL |
| 15 | Meta optimization | 8 | 8 | 8.0 | FAIL |
| 16 | Author attribution | 2 | 1 | 1.5 | FAIL |
| 17 | Medical/expert review | 3 | 2 | 2.5 | FAIL |
| 18 | Recency | 1 | 5 | 3.0 | FAIL |
| 19 | Brand mention readiness | 7 | 8 | 7.5 | FAIL |
| 20 | AI citation readiness | 5 | 6 | 5.5 | FAIL |

**Overall Score: 5.35 / 10**
**Pass threshold: 9.0**
**Status: NEEDS WORK**

---

## Model Disagreements (3+ point difference)

| # | Criterion | GPT-4o | Llama 3.3 | Delta | Notes |
|---|-----------|--------|-----------|-------|-------|
| 2 | Definition paragraph | 5 | 8 | 3 | GPT stricter on AI-extractable definition; Llama more lenient on intro text |
| 10 | Multi-modal | 5 | 3 | 2 | Close but worth noting |
| 12 | FAQ section | 4 | 1 | 3 | Llama says completely absent; GPT gives partial credit |
| 18 | Recency | 1 | 5 | 4 | Major disagreement — GPT sees no date at all; Llama may have inferred from schema |

---

## Detailed Findings

### GPT-4o Assessment

**Top 3 fixes:**
1. Add a structured FAQ section with at least 5 common questions and answers
2. Include high-quality citations from PubMed or DOI to support scientific claims
3. Add author attribution with credentials and ensure content is reviewed by a medical expert

**AI citation likelihood:** The page currently lacks the depth, authoritative citations, and structured content necessary for robust AI citation. Enhancing the factual density with credible sources, adding structured FAQs, and improving author and expert attribution would significantly increase its likelihood of being cited by AI models.

### Llama 3.3 Assessment

**Top 3 fixes:**
1. Add a comprehensive FAQ section with at least 5 questions
2. Improve fact density by adding more verifiable claims with sources
3. Add a 'reviewed by' expert signal to establish credibility for YMYL content

**AI citation likelihood:** The page provides some useful information but lacks authority, comprehensiveness, and credibility. To increase AI citation likelihood, it needs improved fact density, expert review signals, and quotable answers.

---

## Combined Priority Fixes (both models agree)

1. **FAQ section** — both models scored this lowest (avg 2.5). Add 5-10 Q&A pairs.
2. **Citation quality** — both scored 2-3. Add PubMed/DOI references for peptide claims.
3. **Author/expert attribution** — both scored 1-3. Add author byline + medical reviewer signal.
4. **Comparison content** — both scored 2-3. Add product comparison table.
5. **Fact density** — both scored 4-5. Add verifiable claims with sources.

---

## Triage: hairgenetix.com/de — Round 1

| # | Criterion | Avg | Recommendation | Verdict | Reason |
|---|-----------|-----|---------------|---------|--------|
| 1 | Answer-first format | 6.0 | Add hero summary paragraph | FIX NOW | Easy Liquid edit, high AISO impact |
| 2 | Definition paragraph | 6.5 | Add AI-extractable 1-2 sentence definition | FIX NOW | Easy, critical for AI citations |
| 3 | Heading hierarchy | 7.0 | Convert some H2s to question format | FIX LATER | Moderate effort, needs content review |
| 4 | Atomic paragraphs | 8.5 | Break up any long paragraphs | FIX LATER | Minor, close to target |
| 5 | Fact density | 4.5 | Add verifiable claims with sources | FIX LATER | Needs research, medium effort |
| 6 | Comparison content | 2.5 | Add product comparison table | SKIP | Homepage isn't the right place — do this on product/comparison pages |
| 7 | List/table format | 4.5 | Structure key benefits in lists/tables | FIX NOW | Easy HTML/Liquid change |
| 8 | Content depth | 6.0 | Expand scientific explanations | FIX LATER | Needs content writing, link to pillar pages instead |
| 9 | Front-loading | 7.5 | Rearrange to highlight key benefits earlier | FIX NOW | Easy reorder |
| 10 | Multi-modal | 4.0 | Add video content | DEFER | Needs video production — revisit when content budget allows |
| 11 | Schema markup | 9.0 | Keep updated | PASS | Already at target |
| 12 | FAQ section | 2.5 | Add structured FAQ with 5+ questions | FIX NOW | High impact, can reuse existing FAQ content |
| 13 | Citation quality | 2.5 | Add PubMed/DOI links | FIX NOW | Critical for YMYL trust — peptide studies exist |
| 14 | Internal linking | 6.0 | Add links to blog/educational content | FIX NOW | Easy, links to existing pages |
| 15 | Meta optimization | 8.0 | Refine meta description | FIX NOW | Quick win, nearly at target |
| 16 | Author attribution | 1.5 | Add author byline with credentials | ASK MALCOLM | Needs decision on who the author is |
| 17 | Medical/expert review | 2.5 | Add 'reviewed by' expert signal | ASK MALCOLM | Needs real medical reviewer — can't fabricate |
| 18 | Recency | 3.0 | Add visible 'last updated' date | FIX NOW | Easy template change |
| 19 | Brand mention readiness | 7.5 | Add clear quotable brand statement | FIX NOW | Part of definition paragraph fix |
| 20 | AI citation readiness | 5.5 | Improve overall structure and authority | — | Result of fixing other items |

---

### Triage Summary

**FIX NOW: 9 items** (1, 2, 7, 9, 12, 13, 14, 15, 18)
**FIX LATER: 4 items** (3, 4, 5, 8)
**DEFER: 1 item** (10 — video)
**SKIP: 1 item** (6 — comparison on homepage)
**ASK MALCOLM: 2 items** (16, 17 — author/medical reviewer)
**PASS: 1 item** (11 — schema)
**Derived: 1 item** (20 — improves automatically)

**Estimated effort for FIX NOW items: Medium** (half-day of Liquid/content work)

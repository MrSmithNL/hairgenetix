# Page Audit: hairgenetix.com/ — Round 1 (EN)

> Date: 2026-03-09
> Language: EN (primary locale — served at root /)
> Page: Homepage (/)
> Round: 1 (initial audit)
> Evaluators: ChatGPT (GPT-4o), Gemini (GPT-4o via Vercel AI)
> NOTE: /en returns 404 because EN is the primary locale (no prefix). Correct URL is /

---

## Score Report

| # | Criterion | ChatGPT | Gemini | Average | Status |
|---|-----------|---------|--------|---------|--------|
| 1 | Answer-first format | 7 | 8 | 7.5 | NEEDS WORK |
| 2 | Definition paragraph | 5 | 5 | 5.0 | NEEDS WORK |
| 3 | Heading hierarchy | 6 | 6 | 6.0 | NEEDS WORK |
| 4 | Atomic paragraphs | 8 | 7 | 7.5 | NEEDS WORK |
| 5 | Fact density | 7 | 8 | 7.5 | NEEDS WORK |
| 6 | Comparison content | 8 | 9 | 8.5 | NEEDS WORK |
| 7 | List/table format | 6 | 5 | 5.5 | NEEDS WORK |
| 8 | Content depth | 8 | 7 | 7.5 | NEEDS WORK |
| 9 | Front-loading | 7 | 8 | 7.5 | NEEDS WORK |
| 10 | Multi-modal | 9 | 6 | 7.5 | NEEDS WORK |
| 11 | Schema markup | 7 | 9 | 8.0 | NEEDS WORK |
| 12 | FAQ section | 9 | 10 | 9.5 | PASS |
| 13 | Citation quality | 5 | 4 | 4.5 | NEEDS WORK |
| 14 | Internal linking | 8 | 7 | 7.5 | NEEDS WORK |
| 15 | Meta optimization | 9 | 9 | 9.0 | PASS |
| 16 | Author attribution | 4 | 3 | 3.5 | NEEDS WORK |
| 17 | Medical/expert review | 5 | 4 | 4.5 | NEEDS WORK |
| 18 | Recency | 4 | 5 | 4.5 | NEEDS WORK |
| 19 | Brand mention readiness | 6 | 8 | 7.0 | NEEDS WORK |
| 20 | AI citation readiness | 6 | 6 | 6.0 | NEEDS WORK |

**ChatGPT Overall:** 6.7 / 10
**Gemini Overall:** 6.65 / 10
**Combined Average:** 6.70 / 10
**Pass threshold:** 9.0
**Status:** NEEDS WORK

---

## Key Finding: /en Returns 404

English is the **primary locale** in Shopify. Primary locales are served at the root URL `/` without a prefix. The URL `/en` returns HTTP 404 and renders the 404 template ("Oops! We can't find what you're looking for here."). This is normal Shopify behavior — not a bug.

**Locale URL mapping:**
- EN (primary): `https://hairgenetix.com/` (root)
- DE: `https://hairgenetix.com/de`
- NL: `https://hairgenetix.com/nl`
- FR, ES, IT, SV, DA, NO: `/fr`, `/es`, `/it`, `/sv`, `/da`, `/no`

---

## Cache Impact Note

Several scores are artificially LOW because Shopify page cache is still serving old content. Once cache clears:

| Item | Current Score | Expected After Cache |
|------|--------------|---------------------|
| #11 Schema markup | 8.0 | ~9.0+ (FAQPage + WebPage + ItemList) |
| #16 Author attribution | 3.5 | ~7.0 (Dr. Bodde trust signal) |
| #17 Medical review | 4.5 | ~9.0 (Dr. Bodde as reviewedBy) |
| #18 Recency | 4.5 | ~7.0 (auto-updating last-updated date) |

**Estimated score after cache clears (no other changes): ~7.5/10**

---

## Priority Fixes (Triage)

### FIX NOW (high impact, easy to implement)

| ID | Criterion | Score | Recommendation |
|----|-----------|-------|---------------|
| E002 | Definition paragraph | 5.0 | Add brand definition to hero subtitle: "Hairgenetix is a professional at-home hair mesotherapy system using copper peptides (GHK-Cu) and micro-infusion technology, clinically proven to reduce hair shedding by 93%." |
| E013 | Citation quality | 4.5 | Add visible PubMed/DOI links for clinical claims (same citations as schema) |
| E003 | Heading hierarchy | 6.0 | Fix H6 product subtitles → H3/H4; ensure clean H1→H2→H3 flow |

### FIX LATER (medium impact)

| ID | Criterion | Score | Recommendation |
|----|-----------|-------|---------------|
| E007 | List/table format | 5.5 | Present clinical results (93%, 400%, etc.) in structured table |
| E019 | Brand mention readiness | 7.0 | Add quotable brand definition near top of page |
| E001 | Answer-first format | 7.5 | Lead hero with summary statement, not just "REVERSE YOUR HAIR LOSS" |
| E004 | Atomic paragraphs | 7.5 | Break remaining long paragraphs into 2-4 sentences |

### WAIT (deployed, pending cache)

| ID | Criterion | Score | What's deployed |
|----|-----------|-------|----------------|
| E011 | Schema markup | 8.0 | FAQPage + WebPage + ItemList in sub-snippets |
| E016 | Author attribution | 3.5 | homepage-trust-signal.liquid (Dr. Bodde) |
| E017 | Medical review | 4.5 | Dr. Bodde as reviewedBy in WebPage schema |
| E018 | Recency | 4.5 | Auto-updating "Last updated" in trust signal |

### DEFER

| ID | Criterion | Score | Notes |
|----|-----------|-------|-------|
| E010 | Multi-modal | 7.5 | Video already referenced; models disagree (9 vs 6) |
| E006 | Comparison content | 8.5 | Already strong; near pass threshold |

---

## Model Disagreements (3+ point gap)

| # | Criterion | ChatGPT | Gemini | Gap | Notes |
|---|-----------|---------|--------|-----|-------|
| 10 | Multi-modal | 9 | 6 | 3 | ChatGPT sees video reference, Gemini stricter on visible media |
| 19 | Brand readiness | 6 | 8 | 2 | Minor disagreement |

---

## Comparison: EN R1 vs DE R1

| # | Criterion | EN R1 | DE R1 | Gap | Notes |
|---|-----------|-------|-------|-----|-------|
| 2 | Definition | 5.0 | 6.5 | -1.5 | Both need definition paragraph |
| 6 | Comparison | 8.5 | 2.5 | +6.0 | EN has comparison section, DE didn't |
| 12 | FAQ | 9.5 | 2.5 | +7.0 | EN has FAQ section, DE didn't before fix |
| 13 | Citations | 4.5 | 2.5 | +2.0 | Both weak |
| 15 | Meta | 9.0 | 8.0 | +1.0 | EN has good title tag |
| 16 | Author | 3.5 | 1.5 | +2.0 | Both weak pre-fix |

**EN starts higher than DE did** (6.70 vs 5.35) because EN already has FAQ, comparison content, and better meta optimization. The main gaps are authority signals (author, citations, recency) — most of which are already deployed and awaiting cache clearance.

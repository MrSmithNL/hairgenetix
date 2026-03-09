# Page Audit: hairgenetix.com/nl — Round 1 (NL)

> Date: 2026-03-09
> Language: NL (Dutch)
> Page: Homepage (/nl)
> Round: 1 (initial audit)
> Evaluators: ChatGPT (GPT-4o), Gemini (Gemini 2.0 Flash)

---

## Score Report

| # | Criterion | ChatGPT | Gemini | Average | Status |
|---|-----------|---------|--------|---------|--------|
| 1 | Answer-first format | 7 | 6 | 6.5 | NEEDS WORK |
| 2 | Definition paragraph | 3 | 2 | 2.5 | NEEDS WORK |
| 3 | Heading hierarchy | 2 | 1 | 1.5 | NEEDS WORK |
| 4 | Atomic paragraphs | 8 | 5 | 6.5 | NEEDS WORK |
| 5 | Fact density | 6 | 7 | 6.5 | NEEDS WORK |
| 6 | Comparison content | 4 | 3 | 3.5 | **UNDERSCORED** (see note) |
| 7 | List/table format | 5 | 4 | 4.5 | NEEDS WORK |
| 8 | Content depth | 6 | 6 | 6.0 | NEEDS WORK |
| 9 | Front-loading | 7 | 5 | 6.0 | NEEDS WORK |
| 10 | Multi-modal | 7 | 7 | 7.0 | NEEDS WORK |
| 11 | Schema markup | 4 | 4 | 4.0 | NEEDS WORK |
| 12 | FAQ section | 5 | 3 | 4.0 | NEEDS WORK |
| 13 | Citation quality | 8 | 8 | 8.0 | NEEDS WORK |
| 14 | Internal linking | 6 | 4 | 5.0 | NEEDS WORK |
| 15 | Meta optimization | 3 | 5 | 4.0 | NEEDS WORK |
| 16 | Author attribution | 2 | 7 | 4.5 | NEEDS WORK |
| 17 | Medical/expert review | 5 | 7 | 6.0 | NEEDS WORK |
| 18 | Recency | 4 | 5 | 4.5 | NEEDS WORK |
| 19 | Brand mention readiness | 2 | 5 | 3.5 | NEEDS WORK |
| 20 | AI citation readiness | 3 | 5 | 4.0 | NEEDS WORK |

**ChatGPT Overall:** 5.05 / 10
**Gemini Overall:** 5.05 / 10
**Combined Average:** 5.05 / 10
**Pass threshold:** 9.0
**Status:** NEEDS WORK

---

## Key Finding: Extensive Language Mixing

The NL homepage has a unique problem not seen on DE or EN: significant amounts of **untranslated English content** throughout the page. This affects:

1. **Headings**: H4 tags ("Easy to use", "New hair growth", "Thicker, healthier hair") are all English
2. **Testimonial section**: H2 "Visible hair growth within 2-4 months" is English; testimonial labels are English
3. **Schema markup**: FAQPage and ItemList JSON-LD schemas contain English-only content
4. **Heading hierarchy abuse**: Individual testimonial names (Diego, Amida, Klaas, Kim, etc.) are each wrapped in H2 tags

This strongly suggests these sections were not translated in Shopify's locale system.

---

## Passing Criteria (0/20)

No criteria reach the 9.0 pass threshold.

---

## Priority Fixes (Triage)

### FIX NOW (high impact, easy to implement)

| ID | Criterion | Score | Recommendation |
|----|-----------|-------|----------------|
| N002 | Definition paragraph | 2.5 | Add brand definition to hero subtitle: "Hairgenetix is een professioneel haarmesotherapiesysteem voor thuisgebruik — met koperpeptiden en micro-infusie klinisch bewezen om haaruitval te stoppen en nieuwe groei te bevorderen." |
| N015 | Meta optimization | 4.0 | Fix missing title tag — should be "Hairgenetix | Professionele Haarmesotherapie voor Thuis" |
| N011 | Schema markup | 4.0 | Translate FAQPage and ItemList schema content to Dutch; remove duplicate Organization schema |
| N003 | Heading hierarchy | 1.5 | Fix H6→H4 for product subtitles; fix English H4s; fix testimonial H2s |
| N016 | Author attribution | 4.5 | Verify trust signal renders correctly with Dutch text |

### FIX LATER (medium impact, needs translation work)

| ID | Criterion | Score | Recommendation |
|----|-----------|-------|----------------|
| N012 | FAQ section | 4.0 | Translate FAQ schema to Dutch |
| N006 | Comparison content | 3.5 | **SCORING ERROR** — "Doorbraak in haarverzorging" comparison table already exists (Mesotherapie thuis vs Klinisch vs Topisch). Omitted from audit prompt. Est. true score: ~8.5 |
| N019 | Brand mention readiness | 3.5 | Brand definition in hero will fix this |
| N014 | Internal linking | 5.0 | Add contextual links within content sections |
| N001 | Answer-first format | 6.5 | Brand definition in hero will improve this |
| N009 | Front-loading | 6.0 | Reorder content with key claims first |
| N007 | List/table format | 4.5 | Add structured table for clinical results |
| N018 | Recency | 4.5 | Verify trust signal date renders |

### DEFER

| ID | Criterion | Score | Notes |
|----|-----------|-------|-------|
| N010 | Multi-modal | 7.0 | Videos present, infographic would help |
| N008 | Content depth | 6.0 | Science pages provide depth |

---

## Model Disagreements (3+ point gap)

| # | Criterion | ChatGPT | Gemini | Gap | Notes |
|---|-----------|---------|--------|-----|-------|
| 4 | Atomic paragraphs | 8 | 5 | 3 | ChatGPT more lenient on paragraph length |
| 16 | Author attribution | 2 | 7 | 5 | GPT-4o may not have detected the trust signal; Gemini saw Dr. Bodde |
| 19 | Brand readiness | 2 | 5 | 3 | Disagreement on how extractable current content is |

---

## Comparison: NL R1 vs EN R1 vs DE R1

| # | Criterion | NL R1 | EN R1 | DE R1 | Notes |
|---|-----------|-------|-------|-------|-------|
| 2 | Definition | 2.5 | 5.0 | 6.5 | NL worst — no definition at all |
| 3 | Heading hierarchy | 1.5 | 6.0 | 7.0 | NL has English H4s + testimonial H2s |
| 6 | Comparison | 3.5 | 8.5 | 2.5 | EN has comparison section |
| 11 | Schema | 4.0 | 8.0 | 9.0 | NL schemas in wrong language |
| 12 | FAQ | 4.0 | 9.5 | 2.5 | NL has FAQ but in English |
| 13 | Citations | 8.0 | 4.5 | 2.5 | NL already has PubMed links visible |
| 15 | Meta | 4.0 | 9.0 | 8.0 | NL missing title tag |

**NL starts lower (5.05) than both EN (6.70) and DE (5.35)** primarily due to language mixing — English content in headings, schemas, and testimonials. The underlying structure is similar to DE/EN, but the translation gaps are more severe.

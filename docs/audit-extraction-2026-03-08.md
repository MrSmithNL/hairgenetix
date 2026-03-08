# SEO + AISO Audit — Hairgenetix DE (Extracted & Deduplicated)

**Source:** 3-phase AI-generated audit of https://hairgenetix.com/de (2,129 lines)
**Extraction date:** 2026-03-08
**Phases covered:** Initial audit → Deep strategy → AI optimization + Competitive intel

---

## Summary Scores

| Factor | Score |
|--------|-------|
| SEO | 6/10 |
| Technical | 7/10 |
| Content | 6/10 |
| Authority | 4/10 |
| LLM discoverability | 4/10 |
| **Overall** | **5.5/10** |

**Traffic potential (if strategy executed):** 100k–300k monthly organic visitors (Year 1). Audit estimates 30 articles × ~6k average visits = ~180k/month.

**Revenue potential at 200k/month traffic:** €150k–€500k/month (at 1.5–3% ecommerce conversion rate).

---

## Section 1: Technical SEO

### 1.1 Hreflang Implementation

**Audit says:** German pages are under `/de/` but hreflang is missing or incorrect on most Shopify stores, causing German pages to compete with English equivalents and Google to index the wrong language version. Expected impact: reduced rankings in Germany, Austria, Switzerland (DACH).

**Status: GAP**

**Action:** Add hreflang tags to every page (homepage, product pages, blogs, collection pages). Required tags per page:

```html
<link rel="alternate" hreflang="de" href="https://hairgenetix.com/de/...">
<link rel="alternate" hreflang="en" href="https://hairgenetix.com/...">
<link rel="alternate" hreflang="nl" href="https://hairgenetix.com/nl/...">
<link rel="alternate" hreflang="x-default" href="https://hairgenetix.com">
```

Note: All 9 languages need hreflang (fr, es, it, sv, da, no in addition to en, nl, de).

---

### 1.2 Indexation Architecture / Canonical Tags

**Audit says:** Shopify can generate duplicate URL paths such as `/de/products/product` and `/products/product?variant=`, risking Google indexing duplicates.

**Status: DONE** (Shopify handles canonical tags automatically per IMPORTANT CONTEXT)

**Action:** Verify in Google Search Console that the correct canonical URLs are being indexed. No code change needed unless GSC shows indexation issues.

---

### 1.3 Core Web Vitals

**Audit says:** Potential issues from heavy hero images, excessive JS apps, slider scripts, review widgets, Shopify theme scripts.

**Target metrics:**

| Metric | Target |
|--------|--------|
| LCP | < 2.5s |
| CLS | < 0.1 |
| INP | < 200ms |

**Status: UNKNOWN — needs measurement**

**Action:** Run Core Web Vitals report in Google Search Console and PageSpeed Insights for the DE homepage and key product pages. If LCP > 2.5s: compress hero images to WebP under 200kb and enable lazy loading for all below-fold images.

---

### 1.4 Sitemap Structure

**Audit says:** Shopify generates `/sitemap.xml` but language-segmented sitemaps are missing.

**Status: GAP (likely)**

**Recommended structure:**
```
/sitemap.xml
/de/sitemap.xml
/nl/sitemap.xml
/en/sitemap.xml
(+ fr, es, it, sv, da, no)
```

**Action:** Confirm whether Shopify auto-generates language sitemaps. If not, investigate Shopify sitemap app or theme modification.

---

### 1.5 Robots.txt

**Audit says:** Ensure cart, checkout, account, and search paths are blocked to prevent crawl waste.

**Status: PARTIAL** (robots.txt allows AI crawlers, but internal Shopify path blocking is a separate issue)

**Action:** Confirm the following are in `robots.txt` Disallow rules:
```
/cart
/checkout
/account
/search
```

---

### 1.6 Image SEO

**Audit says:** Product images likely have generic alt tags. Image filenames are not SEO-optimized.

**Status: GAP (likely)**

**Examples of correct alt text:**
```
alt="Kupferpeptid Haarwachstum Shampoo GHK-Cu"
```

**Examples of correct filenames:**
```
ghk-cu-haarserum-hairgenetix.webp
mesotherapie-haar-pen.webp
```

**Action:** Audit all product and blog images for descriptive alt text in the correct language per locale. Rename image files to include primary keyword.

---

## Section 2: On-Page SEO

### 2.1 Page Titles

**Audit says:** Titles focus on brand claims rather than search intent. German search queries are not being targeted.

**Status: PARTIAL** (meta titles are translated per IMPORTANT CONTEXT, but keyword optimization of titles is unclear)

**Example improvement:**
- Current (likely): `Hairgenetix – Hair Growth`
- Better: `Haarmesotherapie für Zuhause | Kupferpeptid Haarserum | Hairgenetix`

**Action:** Audit all DE page titles against target German keywords (see Section 9). Ensure primary keyword appears near the front of every title tag.

---

### 2.2 German Keyword Targeting

**Audit says:** Pages mention relevant concepts but are not optimized around actual German search queries.

**Status: PARTIAL** (meta translations exist, but content optimization depth is unclear)

**Key German keywords the site should be targeting:**

| Keyword | Volume |
|---------|--------|
| haarausfall behandeln | very high |
| haarwachstum serum | high |
| kupferpeptid haar | medium |
| mesotherapie haare | medium |
| microneedling haare | medium |
| haarausfall stoppen | ~80k/mo |
| haare wachsen lassen | ~60k/mo |
| haarausfall | ~200k/mo |
| mesotherapie haare | ~10k/mo |
| microneedling haare | ~8k/mo |

**Action:** For each DE page, confirm the primary German keyword appears in H1, first paragraph, and 2–3 subheadings.

---

### 2.3 Heading Structure

**Audit says:** Typical Shopify issues include multiple H1 tags and skipped heading levels (H1 → H4 with no H2 or H3).

**Status: UNKNOWN — needs audit**

**Correct hierarchy example:**
```
H1: Kupferpeptid Haarserum (GHK-Cu & AHK-Cu)
H2: Vorteile
H2: Wissenschaft
H2: Anwendung
H2: Studien
H2: FAQ
```

**Action:** Run a heading structure audit on the top 10 DE pages. Fix any pages with multiple H1 tags or skipped heading levels.

---

### 2.4 Internal Linking

**Audit says:** Site has weak topical clusters. Articles do not consistently link to related articles and product pages.

**Status: GAP**

**Required linking pattern per article:**
- 3 links to related informational pages
- 1 link to a product page
- 1 link to a comparison page

**Example cluster flow:**
```
Hair Loss Guide
  ↓ Microneedling Guide
  ↓ Mesotherapy Guide
  ↓ Copper Peptide Science
  ↓ Product Pages
```

**Action:** Build an internal linking map. As each new article is published (see Section 10), add internal links from existing articles to the new one and vice versa.

---

## Section 3: Content Strategy & Topical Authority

### 3.1 Overall Assessment

**Audit says:** Blog contains strong educational content (copper peptides, mesotherapy, comparison articles) but coverage is too narrow to dominate the niche. The site currently behaves like an ecommerce store rather than the global authority on hair regeneration. Content depth needs to expand significantly.

**Status: PARTIAL**

**Existing strengths noted:** GHK-Cu Haarseren Vergleich comparison article cited as excellent SEO format.

---

### 3.2 Missing Cornerstone Content (German-Language)

**Audit says:** Pillar pages are missing for the highest-traffic topics.

**Status: GAP**

Missing German cornerstone topics:
- Was verursacht Haarausfall bei Männern?
- DHT und androgenetische Alopezie erklärt
- Minoxidil vs Kupferpeptide
- Mesotherapie vs Microneedling
- PRP vs Mesotherapie
- Haarausfall stoppen
- Geheimratsecken behandeln
- Diffuser Haarausfall
- Haare verdicken

---

### 3.3 Pillar Content Strategy

**Audit says:** Create 5 pillar pages at 4,000+ words each.

**Status: GAP**

| Pillar | Title | Traffic Potential |
|--------|-------|------------------|
| 1 | The Complete Guide to Hair Loss (Causes, Treatments & Regrowth) | 50k+/mo |
| 2 | Microneedling for Hair Loss: Science, Results, Protocol | 30k+/mo |
| 3 | Mesotherapy for Hair Loss (existing page — needs expansion) | High |
| 4 | Copper Peptides for Hair Growth: The Complete Science Guide | High |
| 5 | Hair Regrowth Treatments Compared | High |

**Action:** Commission all 5 pillar pages. Each should cover: clinical studies, mechanism of action, comparison to alternatives, protocol/usage, and FAQ section.

---

### 3.4 Topical Cluster Architecture

**Audit says:** Build 4 (later extended to 6) topical clusters so Google rewards topical authority.

**Clusters:**

**Cluster 1 — Hair Loss Science**
Keywords: what causes hair loss, why am I losing hair, androgenetic alopecia, DHT hair loss, hair follicle miniaturization, hair thinning men
Pages: Complete Guide to Hair Loss, Hair Growth Cycle Explained, DHT and Hair Loss, Why Hair Follicles Stop Growing

**Cluster 2 — Hair Regrowth Treatments**
Keywords: hair regrowth treatment, best hair growth treatment, hair loss treatment men, hair regrowth products
Pages: Hair Regrowth Treatments Compared, How to Regrow Hair Naturally, Best Hair Loss Treatments (2026)

**Cluster 3 — Microneedling & Mesotherapy**
Keywords: microneedling hair growth, microneedling for hair loss, mesotherapy hair, mesotherapy hair results
Pages: Microneedling for Hair Growth, Mesotherapy for Hair Loss, Microneedling vs Mesotherapy, How Deep Should Microneedling Be

**Cluster 4 — Peptides & Scalp Biology**
Keywords: copper peptides hair, GHK-Cu hair, AHK-Cu peptide, peptides hair growth
Pages: Copper Peptides for Hair Growth, GHK-Cu Hair Growth Science, AHK-Cu vs GHK-Cu, Peptides vs Minoxidil

---

### 3.5 Clinical Study Page

**Audit says:** The 93% reduction in hair loss claim should be turned into a dedicated clinical study page with methodology, before/after data, and study design. This page alone could rank for "hair growth clinical study".

**Status: GAP**

**Action:** Create a dedicated study/evidence page. This is a high-authority page that can attract backlinks and AI citations.

---

### 3.6 Visual Content

**Audit says:** Hair loss content performs well visually. Diagrams are shared widely and often reused in AI answers.

**Status: GAP**

Diagrams to create:
- Hair follicle anatomy
- Follicle miniaturization diagram
- Microneedling mechanism graphic
- Mesotherapy delivery/injection diagram
- Hair growth cycle diagram

---

## Section 4: AI/LLM Discoverability (AISO)

### 4.1 The Four Knowledge Layers

**Audit says:** LLMs pull from four layers. HairGenetix must appear in all four.

| Layer | What It Is | Hairgenetix Status |
|-------|-----------|-------------------|
| Layer 1 | Authoritative websites: scientific publications, educational content, high-authority blogs | PARTIAL — blog exists but authority is limited |
| Layer 2 | Structured data: schema markup, FAQ entities, product entities | DONE — full schema suite implemented |
| Layer 3 | Knowledge graph entities: brands recognized as entities | GAP — no Crunchbase, Wikidata, PitchBook presence |
| Layer 4 | Retrieval indexes: AI crawls and embeds web content | PARTIAL — AI crawlers allowed, llms.txt exists |

---

### 4.2 AI Answer Page Strategy

**Audit says:** AI assistants prefer pages that directly answer a question with a short answer at the top, followed by structured depth.

**Status: PARTIAL** (answer-first format exists on science pages per IMPORTANT CONTEXT, but not all pages follow this pattern)

**Required article structure for AI retrieval:**
```
H1: [Question format, e.g. "Does Microneedling Regrow Hair?"]
Short answer (2 sentences)
Why it works
Scientific evidence
Comparison with other treatments
FAQ (5–10 questions)
Sources/citations
```

**Action:** Audit all existing 13 blog articles to confirm they follow this structure. Flag any that do not and queue for reformatting.

---

### 4.3 Definition Paragraph Technique

**Audit says:** LLMs extract definition paragraphs and use them as answer snippets. Include one precise definition paragraph per key topic.

**Status: GAP (not systematically applied)**

**Example of correct format:**
> "Hair mesotherapy is a treatment where biologically active ingredients such as peptides, vitamins, or growth factors are delivered into the scalp through micro-injections to stimulate hair follicles and improve hair density."

**Action:** Ensure every key topic page opens with a clear, standalone definition paragraph. This paragraph should contain the topic name, mechanism, and benefit in 2–3 sentences.

---

### 4.4 Comparison Tables for AI

**Audit says:** AI models frequently extract comparison tables and include them in answers.

**Status: GAP**

**Required tables:**

Table 1 — Treatment comparison (for conversion and AI):
| Treatment | Effectiveness | Cost |
|-----------|--------------|------|
| Minoxidil | Moderate | Low |
| PRP | High | Very High |
| Microneedling | High | Low |
| Mesotherapy | High | Medium |

Table 2 — Product comparison (for category pages)
Table 3 — Ingredient comparison (copper peptides vs alternatives)

**Action:** Add comparison tables to pillar articles and product/category pages.

---

### 4.5 The 5 AI Question Categories

**Audit says:** AI assistant hair-loss queries fall into 5 groups. Content should target all 5.

**Category 1 — Diagnosis (very high volume)**
Target queries: Why am I losing hair suddenly? / Why is my hair thinning at the crown? / How do I know if I have androgenetic alopecia? / Is hair thinning reversible? / What causes hair loss in men in their 30s? / Why are my temples receding? / Why is my hair shedding more than usual?

Pages to create: Why Hair Loss Happens / Early Signs of Male Pattern Baldness / Is Hair Thinning Reversible? / Hair Loss in Your 20s vs 30s

**Category 2 — Treatments (purchase intent)**
Target queries: What is the best treatment for hair loss? / How can I regrow my hair naturally? / Do hair growth serums actually work? / Can hair grow back after thinning? / What treatments stop hair loss?

Pages: Best Hair Loss Treatments Compared / Can Hair Regrow After Thinning? / Hair Growth Methods That Actually Work

**Category 3 — Microneedling (strategic advantage)**
Target queries: Does microneedling regrow hair? / How deep should microneedling be for hair growth? / How often should you microneedle the scalp? / Does microneedling work without minoxidil? / How long does microneedling take to regrow hair?

Pages: Microneedling for Hair Growth: Complete Guide / Microneedling Depth Guide / Microneedling Frequency Guide

**Category 4 — Mesotherapy**
Target queries: What is hair mesotherapy? / Does mesotherapy work for hair loss? / Is mesotherapy better than PRP? / How long does mesotherapy last? / Is mesotherapy safe?

Pages: Hair Mesotherapy Explained / Mesotherapy vs PRP for Hair Loss / Mesotherapy Results Timeline

**Category 5 — Routines (high conversion)**
Target queries: What is the best hair regrowth routine? / How should I combine microneedling with serum? / What weekly routine helps hair grow back? / What supplements help hair growth?

Pages: The Complete Hair Regrowth Routine / Microneedling + Serum Protocol / Hair Growth Weekly Routine

**Additional AI categories identified:**
- Ingredients: What are copper peptides for hair growth? / Does GHK-Cu regrow hair? / Are peptides better than minoxidil? / What ingredients stimulate hair follicles?
- Timelines: How long does it take to regrow hair? / When does microneedling start working? / What happens after 3 months of treatment?
- Safety/Fear: Is microneedling safe for hair loss? / Does microneedling damage hair follicles? / Are copper peptides safe? / Does microneedling cause shedding?

---

### 4.6 Entity Building (Knowledge Graph)

**Audit says:** AI models recognize entities, not just pages. HairGenetix is not strongly recognized as an entity in knowledge graphs.

**Status: GAP**

**Required profiles to create:**
- Crunchbase company profile
- LinkedIn company page (if not already present)
- PitchBook entry
- Wikidata entry
- Industry directories (hair loss, cosmetic, health)
- Google Knowledge Panel (earned through entity signals above)

**Action:** Malcolm to review which profiles exist. Create missing ones. Ensure all profiles use consistent NAP (name, address, phone) data and link back to hairgenetix.com.

---

### 4.7 AI Citation Strategy

**Audit says:** Pages that include explicit citations to research are far more likely to be quoted by AI. Pages with clear brand-defining statements get cited by name.

**Status: PARTIAL** (PubMed citations exist in blog articles per IMPORTANT CONTEXT — confirm on DE pages)

**Brand statement to include on key pages:**
> "HairGenetix is a hair regeneration system combining microneedling technology with copper peptide formulations to stimulate hair follicle activity."

**Action:** Verify PubMed citations appear on DE-language versions of all 13 articles. Confirm brand statement appears on homepage and science pages.

---

### 4.8 llms.txt and AI Crawler Files

**Audit says:** AI systems crawl and embed web content. Making this content accessible improves retrieval.

**Status: DONE** (llms.txt, llms-full.txt in 9 languages, ai.txt, robots.txt allowing GPTBot/ClaudeBot/PerplexityBot all confirmed implemented)

---

## Section 5: Authority & Trust Signals

### 5.1 Overall Assessment

**Audit says:** Authority is currently moderate. The site shows customer reviews, product explanations, and some media mentions. Hair loss is a YMYL topic — Google demands demonstrated expertise.

**Status: PARTIAL**

---

### 5.2 Medical/Expert Reviewer Credentials

**Audit says:** Every blog article should show "Reviewed by dermatologist" and/or "Reviewed by trichologist."

**Status: PARTIAL** (Person schema for author with credentials exists per IMPORTANT CONTEXT — but reviewer bylines on articles are unclear)

**Action:** Confirm whether visible reviewer bylines appear on the DE article pages (not just in schema). If schema only, add visible bylines to article templates. Flag for Malcolm's review — sourcing a dermatologist or trichologist reviewer is a priority.

---

### 5.3 Scientific Citations

**Audit says:** Link to PubMed, NIH, and dermatology journals. Cite research with enough detail that AI and Google can verify the claim.

**Status: PARTIAL** (PubMed citations exist — confirm DE versions)

**Action:** Verify all 13 DE articles display PubMed citations. Create a clinical evidence page (see Section 3.5).

---

### 5.4 Author Pages

**Audit says:** Create dedicated author pages with credentials and research background.

**Status: UNKNOWN**

**Action:** Confirm whether hairgenetix.com/de has a visible author page or bio page. If not, create one.

---

### 5.5 Dermatologist Advisory Board

**Audit says:** Add a visible advisory board to increase medical credibility.

**Status: GAP**

**Action:** Flag for Malcolm's review — this is a medical/authority claim decision.

---

## Section 6: UX & Conversion

### 6.1 Homepage Structure

**Audit says:** Current messaging is strong but users must instantly understand problem → solution → mechanism → proof.

**Status: PARTIAL**

**Recommended homepage flow:**
```
Hero
Problem (hair loss context)
Solution (the HairGenetix system)
Science (mechanism explanation)
Results (before/after, data)
Reviews
FAQ
Products
```

**Action:** Review current DE homepage against this structure. Identify which sections are missing or out of order.

---

### 6.2 Comparison Tables (Conversion)

**Audit says:** Treatment comparison tables dramatically increase conversions.

**Status: GAP**

**Example table to add to product and landing pages:**
| Treatment | Effectiveness | Cost |
|-----------|--------------|------|
| Minoxidil | Medium | Low |
| PRP | High | Very High |
| Mesotherapy (Hairgenetix) | High | Medium |

**Action:** Add comparison table to product pages and the homepage. Also use on comparison articles.

---

### 6.3 Protocol / Routine Guides

**Audit says:** Step-by-step protocol guides turn education into sales by connecting the treatment steps directly to products.

**Status: GAP**

**Required content:**
- Hair Regrowth Routine (microneedling + serum + frequency + timeline)
- Microneedling + Serum Protocol
- Weekly Hair Growth Schedule

**Action:** Create these as both blog articles and as embedded content on product pages.

---

### 6.4 Medical Claim Risk

**Audit says:** Claims such as "400% more effective," "clinical results," and "93% reduction in hair loss" need source citations to avoid Google YMYL penalty.

**Status: FLAG FOR MALCOLM'S REVIEW**

**Action:** Malcolm to review all medical and efficacy claims on the DE site. Confirm each is backed by a linked source. Any unsourced claim should be amended or removed.

---

## Section 7: Backlink Strategy

### 7.1 Current State

**Audit says:** Hairgenetix has limited authority backlinks. Some media mentions exist but not from high-authority domains.

**Status: GAP**

---

### 7.2 Target Backlink Sources

**Audit says:** Prioritize links from:
- Dermatology blogs
- Biohacking websites
- Hair loss forums
- Men's health publications
- Health blogs

---

### 7.3 Link Acquisition Tactics

**Audit says:** Best tactic is to publish comparison study content that naturally attracts links.

**Example link magnet articles:**
- Microneedling vs Minoxidil: Clinical Evidence (with data)
- Microneedling vs Topical Hair Growth Results
- Copper Peptides for Hair Regeneration (evidence review style)

**Action:** Once pillar articles are published, run outreach to dermatology bloggers and hair loss communities. Submit to relevant directories.

---

## Section 8: Competitive Intelligence

### 8.1 Hims & Hers Health

**Traffic:** ~6.6 million monthly visits
**Referring domains:** 12,000+
**Authority:** Massive

**Their strategy:** Dominate educational search queries across the entire customer journey — not product pages.

**Example pages they publish:**
- Does finasteride regrow hair?
- Minoxidil side effects
- Best hair loss treatments
- Receding hairline causes
- Hair growth cycle

**Their funnel:**
```
What causes hair loss
  ↓ Finasteride vs minoxidil
  ↓ Does finasteride work
  ↓ Buy treatment
```

They cover all four stages: Diagnosis → Treatment research → Comparison → Prescription purchase.

**Where HairGenetix can compete:** Hims focuses on pharmaceutical treatments (finasteride, minoxidil). HairGenetix can own the "non-drug hair regeneration" category — microneedling + mesotherapy + peptides — where Hims has weak content.

---

### 8.2 Scandinavian Biolabs

**Strategy:** Product science + brand narrative built around proprietary formula.
**Proprietary formula:** Bio-Pilixin®

**Claims:**
- 97% of users experienced less hair loss
- 73% increased hair density after clinical testing

**Their SEO content:**
- Receding hairline guide
- Minoxidil for women
- Hair loss causes
- Hair growth products
- Dozens of educational blog articles

**Their conversion funnel:**
```
Hair loss education
  ↓ Hair growth routine
  ↓ 3-step product system
```

**Key differentiator vs Hairgenetix:** Their main conversion mechanism is a routine/system (not a single product). HairGenetix has the same system-based positioning advantage.

---

### 8.3 The Ordinary (Ingredient SEO Model)

**Strategy:** Brand the molecule, not the product.

**Examples:**
- Ranked for "niacinamide serum," "hyaluronic acid serum," "peptide serum"
- Traffic from ingredient searches, not brand searches

**Lesson for Hairgenetix:** Own "GHK-Cu hair growth," "AHK-Cu peptide," "copper peptide serum" before competitors. Ingredient SEO converts extremely well because it captures research-mode buyers.

---

### 8.4 What All Winning Hair Brands Have in Common

All successful brands produce three types of content:

1. **Diagnosis content** — Why am I losing hair / Hair thinning causes / Receding hairline (drives huge traffic volume)
2. **Comparison content** — Minoxidil vs finasteride / PRP vs microneedling (captures high-intent buyers)
3. **Ingredient content** — Copper peptides hair growth / Caffeine shampoo / Biotin (converts extremely well)

---

### 8.5 The Strategic Gap HairGenetix Can Own

**Audit says:** None of the big players dominates all three of: microneedling + mesotherapy + peptides.

**Category to own:** "Non-drug hair regeneration" / "Hair Regeneration Systems"

This positions HairGenetix against pharmaceuticals (finasteride, minoxidil) while standing apart from single-ingredient serums. Systems convert better than single products.

---

## Section 9: Keyword Data

### English Keywords

| Keyword | Monthly Searches |
|---------|-----------------|
| hair loss | 2M+ |
| hair growth | 1M+ |
| hair regrowth | 500k |
| microneedling hair | 150k |
| mesotherapy hair | 120k |
| hair regrowth treatment | huge |
| best hair growth treatment | huge |
| hair loss treatment men | high |
| hair regrowth products | high |
| microneedling hair growth | high |
| microneedling for hair loss | high |
| mesotherapy hair results | medium |
| copper peptides hair | — |
| GHK-Cu hair | — |
| AHK-Cu peptide | — |
| peptides hair growth | — |
| what causes hair loss | high (informational) |
| androgenetic alopecia | medical intent |
| DHT hair loss | medical intent |
| hair follicle miniaturization | science intent |
| minoxidil vs microneedling | high (comparison) |
| finasteride alternatives | huge (comparison) |
| hair growth clinical study | — |
| does microneedling regrow hair | AI-style |
| how long does hair regrowth take | AI-style |

### German Keywords

| Keyword | Monthly Searches |
|---------|-----------------|
| haarausfall | ~200k |
| haarausfall stoppen | ~80k |
| haare wachsen lassen | ~60k |
| mesotherapie haare | ~10k |
| microneedling haare | ~8k |
| haarausfall behandeln | very high |
| haarwachstum serum | high |
| kupferpeptid haar | medium |
| geheimratsecken behandeln | medium |
| diffuser haarausfall | medium |
| haare verdicken | medium |

---

## Section 10: Content Blueprint — The 30-Article Plan

These 30 articles form 6 topical clusters. Target: ~180k–200k monthly organic visitors if each reaches 3k–8k visits.

### Cluster 1 — Hair Loss Fundamentals (Massive Traffic)

| # | Title | Target Keywords | Notes |
|---|-------|----------------|-------|
| 1 | The Complete Guide to Hair Loss | hair loss, why am I losing hair, hair thinning | 4,000+ words pillar |
| 2 | What Causes Hair Loss? | genetics, DHT, stress, hormones, androgenetic alopecia | Include follicle miniaturization |
| 3 | The Hair Growth Cycle Explained | anagen, catagen, telogen, hair growth cycle | Science article |
| 4 | Early Signs of Male Pattern Baldness | receding hairline, temple thinning, crown thinning | Diagnosis intent |
| 5 | Is Hair Loss Reversible? | is hair thinning reversible, can hair grow back | High-intent, popular AI question |

---

### Cluster 2 — Hair Regrowth Treatments (High Conversion)

| # | Title | Target Keywords | Notes |
|---|-------|----------------|-------|
| 6 | Best Hair Loss Treatments Compared | best hair loss treatment, hair regrowth treatment | Comparison table essential |
| 7 | Can Hair Grow Back After Thinning? | can hair regrow, hair loss reversible | Popular AI question |
| 8 | Minoxidil vs Microneedling | minoxidil vs microneedling | High comparison intent |
| 9 | Finasteride Alternatives | finasteride alternatives, natural hair loss treatment | Huge demand; connects to peptides |
| 10 | Hair Transplant vs Non-Surgical Treatments | hair transplant vs microneedling | Targets transplant-searcher funnel top |

---

### Cluster 3 — Microneedling Authority (Strategic Edge)

| # | Title | Target Keywords | Notes |
|---|-------|----------------|-------|
| 11 | Microneedling for Hair Growth (Complete Guide) | microneedling hair growth, microneedling for hair loss | Biggest single opportunity; 30k+/mo potential |
| 12 | Does Microneedling Regrow Hair? | does microneedling regrow hair | AI answer page format |
| 13 | Microneedling Depth Guide | microneedling depth hair, dermaroller length hair | Technical; product-adjacent |
| 14 | How Often Should You Microneedle the Scalp? | microneedling frequency scalp | Very common AI search |
| 15 | Microneedling Results Timeline | microneedling results, how long microneedling works | Research: results in ~6–10 weeks |

---

### Cluster 4 — Mesotherapy Authority

| # | Title | Target Keywords | Notes |
|---|-------|----------------|-------|
| 16 | Hair Mesotherapy Explained | what is hair mesotherapy, mesotherapy hair | Definition paragraph critical |
| 17 | Mesotherapy vs PRP for Hair Loss | mesotherapy vs PRP, is mesotherapy better than PRP | Comparison |
| 18 | Mesotherapy Results Timeline | mesotherapy hair results, how long mesotherapy lasts | Timeline data |
| 19 | Is Mesotherapy Safe? | is mesotherapy safe, mesotherapy side effects | Trust builder |
| 20 | Mesotherapy vs Microneedling | mesotherapy vs microneedling | Strong SEO + AI opportunity |

---

### Cluster 5 — Peptide Science (Unique Positioning / Ingredient SEO)

| # | Title | Target Keywords | Notes |
|---|-------|----------------|-------|
| 21 | Copper Peptides for Hair Growth | copper peptides hair, copper peptide serum | The Ordinary model: brand the molecule |
| 22 | GHK-Cu Hair Growth Science | GHK-Cu hair, GHK-Cu hair growth | Deep science; AI citable |
| 23 | AHK-Cu vs GHK-Cu | AHK-Cu peptide, AHK-Cu vs GHK-Cu | Unique differentiator content |
| 24 | Peptides vs Minoxidil | peptides vs minoxidil, are peptides better than minoxidil | High conversion comparison |
| 25 | Peptides and Hair Follicle Regeneration | peptides hair follicle, hair follicle stimulation | Science authority page |

---

### Cluster 6 — Hair Growth Routines (High Conversion)

| # | Title | Target Keywords | Notes |
|---|-------|----------------|-------|
| 26 | The Complete Hair Regrowth Routine | hair regrowth routine, best hair growth routine | Product funnel page; microneedling + serum + scalp care |
| 27 | Weekly Hair Growth Protocol | weekly hair growth routine, hair growth schedule | Step-by-step; product-linked |
| 28 | Microneedling + Serum Routine | microneedling serum routine, how to combine microneedling with serum | Direct product funnel |
| 29 | Scalp Health Guide | scalp health, healthy scalp hair growth | Foundation content |
| 30 | Hair Regrowth Timeline (What to Expect) | how long does hair regrowth take, hair regrowth timeline | Expectation-setting; reduces churn |

---

## Section 11: 90-Day Roadmap

### Month 1 — Technical Foundation

**Priority actions:**
1. Implement hreflang tags across all pages in all 9 languages
2. Verify Core Web Vitals (run PageSpeed Insights on DE pages)
3. Fix image alt text and filenames across product and blog images
4. Confirm heading structure on all DE pages (fix any multiple-H1 issues)
5. Confirm robots.txt blocks /cart, /checkout, /account, /search
6. Audit internal linking on existing 13 articles — add missing links
7. Verify DE-language sitemaps are submitted to Google Search Console
8. Create Crunchbase, Wikidata, and PitchBook profiles for entity building
9. Optimize meta titles on DE pages to front-load primary keywords
10. Add comparison tables to existing product pages

### Month 2 — Content Publishing

**Publish in priority order:**

Articles to publish first (highest traffic potential):
1. Complete Guide to Hair Loss (pillar — 4,000+ words)
2. Microneedling for Hair Growth (pillar — 30k+/mo potential)
3. Mesotherapy for Hair Loss (expand existing page)
4. Copper Peptides for Hair (pillar)
5. Best Hair Loss Treatments Compared (comparison pillar)
6. Minoxidil vs Microneedling
7. Finasteride Alternatives
8. Hair Growth Cycle Explained
9. DHT Hair Loss Guide
10. Diffuse Hair Thinning Explained

Each article: question-format H1, short-answer first paragraph, definition paragraph, comparison table, 5–10 FAQs with schema, PubMed citations, internal links.

### Month 3 — Authority Building

**Priority actions:**
1. Publish remaining 20 articles from the 30-article plan
2. Create dedicated clinical evidence/study page
3. Add visible reviewer bylines to all articles (dermatologist or trichologist)
4. Create author/expert page
5. Begin backlink outreach to dermatology blogs, biohacking sites, men's health publications
6. Publish visual diagrams (follicle anatomy, microneedling mechanism, mesotherapy delivery)
7. Add brand-defining statement to homepage and science pages
8. Add protocol/routine guides to product pages
9. Review and source all medical/efficacy claims (Malcolm review required)
10. Submit updated sitemap to Google Search Console after new articles are live

---

## Section 12: Gaps & TODO List

Items confirmed as genuine gaps (not already implemented), prioritized by impact.

### Priority 1 — Critical (Do First)

| # | Gap | Why It Matters |
|---|-----|---------------|
| 1 | Hreflang tags missing | Google may index wrong language; DACH rankings suppressed |
| 2 | No Crunchbase / Wikidata / PitchBook profiles | HairGenetix not recognized as an entity by AI systems (Layer 3) |
| 3 | 30-article content plan not yet published | Content is the primary traffic growth lever; no articles = no traffic |
| 4 | No comparison tables on product/landing pages | High conversion loss; also missing for AI extraction |
| 5 | No clinical study/evidence page | Missing high-authority page; needed for backlinks and AI citations |

### Priority 2 — High Impact

| # | Gap | Why It Matters |
|---|-----|---------------|
| 6 | Heading structure not audited for DE pages | Multiple H1s or skipped levels suppress rankings |
| 7 | Image alt text likely generic | Hurts image search and on-page keyword signals |
| 8 | Core Web Vitals unmeasured | LCP > 2.5s will suppress rankings since 2021 |
| 9 | Definition paragraph not systematically applied | Missing primary AI extraction signal on all pages |
| 10 | Protocol/routine guides absent from product pages | Missing conversion bridge between content and purchase |
| 11 | Internal linking insufficient | Topical authority not built; Google treats pages as isolated |

### Priority 3 — Authority

| # | Gap | Why It Matters |
|---|-----|---------------|
| 12 | Visible reviewer bylines absent on articles (confirm) | YMYL signal; critical for Google E-E-A-T ranking |
| 13 | Author page / expert page absent (confirm) | E-E-A-T requirement |
| 14 | Dermatologist advisory board not established | Trust signal; also useful for PR and AI citation |
| 15 | Zero backlinks from high-authority health domains | Authority (DA) directly affects ranking ceiling |
| 16 | Visual diagrams (follicle, microneedling, mesotherapy) not created | Missed AI reuse opportunity; missed backlink magnet |

### Priority 4 — Conversion & Risk

| # | Gap | Why It Matters |
|---|-----|---------------|
| 17 | Medical/efficacy claims need source audit (Malcolm review) | YMYL risk; could trigger Google quality penalty |
| 18 | Homepage structure not validated against recommended flow | Conversion loss |
| 19 | No language-segmented sitemaps (confirm) | Google may not discover all localized pages |
| 20 | Backlink outreach not started | Ceiling on authority limits ceiling on rankings |

---

**Items flagged for Malcolm's review (personal, legal, or medical decisions):**
- Sourcing a dermatologist or trichologist reviewer
- Establishing a medical advisory board
- Reviewing and sourcing all medical/efficacy claims (400% more effective, 93% reduction, etc.)
- Deciding whether to pursue Wikidata/Wikipedia presence

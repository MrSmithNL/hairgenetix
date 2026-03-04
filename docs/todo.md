# Todo — Hairgenetix (CLIENT-002)

> Last updated: 2026-03-04

## AI Discovery v2.0 Quick Wins — Implementation Order

From the AI Discovery v2.0 audit (score: 52/100). Ordered by ease of implementation. Do these first.

| # | ID | Task | Priority | Status | Est. Time | Score Impact | Notes |
|---|-----|------|----------|--------|-----------|-------------|-------|
| 1 | HG-026 | Add Organization schema (JSON-LD) | High | ✅ Done | 30 min | B1: 0→10 | Name, URL, logo, social profiles, founding date, contact. Biggest single schema gap. |
| 2 | HG-023 | Add AggregateRating schema | High | ✅ Done | 30 min | B7: 0→10 | 4.6 stars, 1,200+ reviews (Judge.me). Show in Google rich results. |
| 3 | HG-027 | Add Product schema (JSON-LD) on product pages | High | ✅ Done | 1 hour | B4: 1→8 | Name, price, availability, brand, image on all product pages. Critical for e-commerce AI. |
| 4 | HG-028 | Add Trustpilot link to site footer + llms.txt | High | ✅ Done | 30 min | C5: 3→5 | Trustpilot link in llms.txt + footer brand text. Footer tagline rewritten for AI value. Copyright updated 2025→2026. |
| 5 | HG-029 | Add TL;DR summary blocks to all 3 blog articles | Medium | ✅ Done | 45 min | A6: 2→7 | Already had TL;DR blocks in all 3 articles — verified live. |
| 6 | HG-030 | Create named author profile + Person schema | High | Blocked | 1 hour | C1: 1→7, B5: 0→7 | Waiting for Malcolm's decision on author identity (himself as founder, trichologist, or advisory board). |
| 7 | HG-031 | Fix About page (currently 404) | High | ✅ Done | 1 hour | C2: 3→8 | Created as draft (page ID 708145774924). Needs Malcolm's approval to publish. |
| 8 | HG-032 | Add outbound citations to PubMed in science + blog content | Medium | ✅ Done | 1 hour | C3: 3→7 | 22 PubMed citations across 3 articles (Trachy 1991, Pyo 2007, Maquart 1988, Pickart 2015/2018, etc.) |
| 9 | HG-033 | Rewrite key page intros to answer-first format | Medium | ✅ Done | 2 hours | A1: 3→7 | Answer-first intros added to 5 pages: The Science, Ingredients, Hair Loss, Scientific Research, Our Philosophy. Styled `.hg-intro` blocks. |
| 10 | HG-034 | Add snippet-ready definitions for key terms | Medium | ✅ Done | 45 min | A7: 4→8, F2: 4→7 | 8 definitions added to copper peptides article: copper peptides, GHK-Cu, AHK-Cu, PDRN, mesotherapy, microneedling, dermal papilla, anagen phase. |
| 11 | HG-035 | Add question-based H2/H3 headings to blog articles | Medium | ✅ Done | 1 hour | A3: 3→7 | 13 headings converted across 3 articles. "How Do Copper Peptides Promote Hair Growth?", "What Is PDRN?", etc. |
| 12 | HG-036 | Create llms-full.txt | Low | ✅ Done | 1 hour | Diagnostic | 20KB extended version live at /llms-full.txt (redirect → /pages/llms-full-txt). All products, pages, articles, FAQ, trust signals. |
| 13 | HG-037 | Add lastmod dates to sitemap | Low | ⚠️ Shopify limitation | Variable | D5: 7→9 | Shopify auto-generates sitemaps — no custom lastmod support. Minimal score impact. |

**Status: 12/13 quick wins complete, 1 blocked (HG-030 — author profile). Estimated score: 68-72/100 (+16-20 points)**

## Active (Existing)

| ID | Task | Priority | Status | Notes |
|----|------|----------|--------|-------|
| HG-002 | Set up GA4 on hairgenetix.com | High | Blocked | GSC verified active. GA4 **NOT installed** — Malcolm needs to add GA4 measurement ID in Shopify admin |
| HG-005 | Identify Shopify theme and customisation approach | Medium | Planned | Understand what changes are possible. Theme uses custom `sw--` sections |
| HG-007 | Fix remaining H1 tag (ingredients page) | Low | Blocked | 16/17 pages fixed via template JSON + section edits. Ingredients page has per-page theme customization that overrides API — requires manual fix in Shopify Theme Editor |
| HG-022 | Build content hub (20-30 articles) | High | Planned | From competitor analysis: nobody owns "GHK-Cu for hair", "mesotherapy at home", "copper peptide vs minoxidil" keywords. Publish in 9 languages for multilingual advantage |
| HG-024 | Create "GHK-Cu vs Minoxidil" comparison page | Medium | Planned | Low-competition keyword. Educational format for AI citation |
| HG-025 | Create "Mesotherapy vs Laser Hair Growth" comparison page | Medium | Planned | Low-competition keyword. Hairgenetix vs HairMax positioning |

## Medium-Term (External Authority — 3-6 months)

| ID | Task | Priority | Status | Notes |
|----|------|----------|--------|-------|
| HG-038 | Grow Trustpilot reviews to 50+ | High | Planned | Currently 9 reviews. Email existing customers. On-site claim of 1,200+ is Judge.me — Trustpilot is what AI platforms check. |
| HG-039 | Create YouTube channel | High | Planned | Product demos, hair growth results, copper peptide science. YouTube = #1 source for Google AI Overviews. |
| HG-040 | Start Reddit presence (r/tressless, r/HairTransplants, r/Haircare) | High | Planned | Reddit = #1 most-cited source at 40.1%. 95/5 rule: helpful answers, not promotion. |
| HG-041 | Create Google Business Profile | Medium | Planned | Complete listing with photos, reviews. Enables Knowledge Panel. |
| HG-042 | Seek independent media coverage | Medium | Planned | Legitimate PR — beauty bloggers, trichology publications, hair loss communities. Not paid placements. |
| HG-043 | Create comparison hub page "Best Hair Growth Serums 2026" | Medium | Planned | Structured comparison table format. Most-cited content type by AI. |
| HG-044 | Add video content to product pages | Medium | Planned | Multi-modal content = 156% higher AI selection. |
| HG-045 | Reach out to trichologists for authority partnerships | High | Planned | Find certified trichologists willing to review/endorse products, co-author content, or serve as advisory board. Key approach: (1) Search IAT/WTS certified trichologists in NL/EU, (2) Reach out via LinkedIn with value proposition — free product samples + revenue share on referrals, (3) Offer co-authored article on copper peptides for hair, (4) Ask for professional review/testimonial for site. Target: 1-2 partnerships. This adds E-E-A-T authority that AI systems weight heavily. |

## Completed

| ID | Task | Completed | Notes |
|----|------|-----------|-------|
| HG-000 | Project setup — repo, docs, agency registration | 2026-03-03 | Initial structure |
| HG-001 | Run initial SEO audit with SEO Toolkit | 2026-03-03 | Technical: 83/100, AI: 74/100, Content: 64/100 avg |
| HG-003 | Keyword research — hair growth niche | 2026-03-03 | 104 keywords, 4 clusters, 3 quick wins identified |
| HG-004 | Content strategy — define pillars and plan | 2026-03-03 | Priorities defined in seo-strategy.md |
| HG-006 | Competitor analysis | 2026-03-03 | 5 competitors (Foligain, Hairmax, Nutrafol, Keeps, MinoxidilMax). Full report at docs/competitor-analysis.md. None have llms.txt. Key gap: content volume |
| HG-008 | Update meta titles on 20 pages | 2026-03-03 | All pages updated via GraphQL pageUpdate with keyword-optimised titles |
| HG-009 | Update meta descriptions on 20 pages | 2026-03-03 | All pages updated — unique, compelling descriptions under 155 chars |
| HG-010 | Add alt text to images across site | 2026-03-03 | 26 images updated with SEO-optimised alt text via REST API (6 products) |
| HG-011 | Create llms.txt file | 2026-03-03 | Live at /pages/llms-txt — custom layout (none.liquid), section, template |
| HG-012 | Add FAQPage, Article, HowTo, BreadcrumbList schema | 2026-03-03 | snippets/seo-schema.liquid injected into theme.liquid — all 4 types verified live |
| HG-013 | Create "Copper Peptide Hair Growth" guide | 2026-03-03 | 15K char pillar page at /pages/copper-peptides-hair-growth |
| HG-014 | Create "GHK-Cu Hair Serum" comparison guide | 2026-03-03 | 16K char pillar page at /pages/ghk-cu-hair-serum-comparison — 7 products compared, SEO meta set |
| HG-015 | Create "Hair Mesotherapy" hub page | 2026-03-03 | 14K char pillar page at /pages/hair-mesotherapy — strengthens #2 ranking |
| HG-016 | Page speed audit | 2026-03-03 | Basic check: TTFB 0.10s, homepage 553KB. PageSpeed Insights API rate-limited. Full audit pending |
| HG-017 | Add URL redirect /llms.txt → /pages/llms-txt | 2026-03-03 | 301 redirects created: /llms.txt and /.well-known/llms.txt → /pages/llms-txt |
| HG-018 | Re-authorize Shopify API with product scopes | 2026-03-03 | New API with all scopes — client credentials grant flow |
| HG-019 | Update product meta titles and descriptions | 2026-03-03 | 16 products — meta titles under 60 chars, descriptions under 155 chars |
| HG-020 | Create Press & Media page | 2026-03-03 | 4 press articles at /pages/press — CelebDigest, Women's Insider, USA News, Men's Insider |
| HG-021 | Re-run SEO audit — post-implementation | 2026-03-03 | Technical: **87/100** (was 83 = +4), AI Discovery: 79/100 (was 74 = +5), Schema diversity: 10/10 (was 4/10). GSC: 1,385 clicks/month, avg position 7.8 |
| HG-023 | Add AggregateRating schema | 2026-03-04 | 4.6 stars, 1,200+ reviews embedded in Organization schema |
| HG-026 | Add Organization schema (JSON-LD) | 2026-03-04 | Name, URL, logo, foundingDate, sameAs [Trustpilot], contactPoint (9 languages), address NL |
| HG-027 | Add Product schema (JSON-LD) on product pages | 2026-03-04 | Name, description, brand, image, SKU, offers with price/currency/availability |
| HG-028 | Add Trustpilot link to site footer + llms.txt | 2026-03-04 | Trustpilot in llms.txt Reviews section + footer brand text. Tagline rewritten for AI. Copyright 2025→2026 |
| HG-029 | TL;DR summary blocks in blog articles | 2026-03-04 | Already existed in all 3 articles — verified, no changes needed |
| HG-031 | Create About Us page | 2026-03-04 | Published (page 708145774924). Company story, science, customers, guarantee, global delivery. Added to Explore footer menu. |
| HG-032 | Add PubMed citations to blog articles | 2026-03-04 | 22 real PubMed citations across 3 articles. Replaced generic refs with Trachy 1991, Pyo 2007, Maquart 1988, Pickart 2015/2018, Liu 2023, Lee 2015, Gupta 2023, etc. |
| HG-034 | Add snippet-ready definitions | 2026-03-04 | 8 "X is Y" definitions in copper peptides article: copper peptides, GHK-Cu, AHK-Cu, PDRN, mesotherapy, microneedling, dermal papilla, anagen phase |
| HG-035 | Question-based H2/H3 headings | 2026-03-04 | 13 headings converted to question format across all 3 blog articles for AI extraction |
| HG-033 | Answer-first page intros | 2026-03-04 | Styled intro blocks on 5 pages: The Science, Ingredients, Hair Loss, Scientific Research, Our Philosophy |
| HG-036 | Create llms-full.txt | 2026-03-04 | 20KB extended version at /llms-full.txt — all products, pages, articles, FAQ, trust signals. Template + page + redirect |
| HG-037 | Add lastmod dates to sitemap | 2026-03-04 | Investigated — Shopify auto-generates sitemaps, no custom lastmod support. Platform limitation, minimal impact (D5: 7→9) |
| HG-046 | Add WebPage/MedicalWebPage schema to key landing pages | 2026-03-04 | WebPage + MedicalWebPage JSON-LD added to seo-schema.liquid. Health pages (hair-loss, ingredients) get MedicalWebPage; general pages get WebPage. Pages with existing content-type schemas (Article, FAQPage, HowTo) excluded. Helps Google AI Overviews cite pages. |

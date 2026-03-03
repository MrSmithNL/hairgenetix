# Todo — Hairgenetix (CLIENT-002)

> Last updated: 2026-03-03

## Active

| ID | Task | Priority | Status | Notes |
|----|------|----------|--------|-------|
| HG-002 | Set up GA4 on hairgenetix.com | High | Blocked | GSC verified active. GA4 **NOT installed** — Malcolm needs to add GA4 measurement ID in Shopify admin |
| HG-005 | Identify Shopify theme and customisation approach | Medium | Planned | Understand what changes are possible. Theme uses custom `sw--` sections |
| HG-007 | Fix remaining H1 tag (ingredients page) | Low | Blocked | 16/17 pages fixed via template JSON + section edits. Ingredients page has per-page theme customization that overrides API — requires manual fix in Shopify Theme Editor |
| HG-022 | Build content hub (20-30 articles) | High | Planned | From competitor analysis: nobody owns "GHK-Cu for hair", "mesotherapy at home", "copper peptide vs minoxidil" keywords. Publish in 9 languages for multilingual advantage |
| HG-023 | Add AggregateRating schema markup | Medium | Planned | From competitor analysis: show star ratings in Google search results (1,200+ reviews, 4.6 stars) |
| HG-024 | Create "GHK-Cu vs Minoxidil" comparison page | Medium | Planned | Low-competition keyword. Educational format for AI citation |
| HG-025 | Create "Mesotherapy vs Laser Hair Growth" comparison page | Medium | Planned | Low-competition keyword. Hairgenetix vs HairMax positioning |

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

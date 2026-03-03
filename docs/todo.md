# Todo — Hairgenetix (CLIENT-002)

> Last updated: 2026-03-03 (competitor analysis added)

## Active

| ID | Task | Priority | Status | Notes |
|----|------|----------|--------|-------|
| HG-002 | Verify analytics setup (GA4, GSC) | High | Planned | GSC confirmed connected — verify GA4 |
| HG-005 | Identify Shopify theme and customisation approach | Medium | Planned | Understand what changes are possible |
| HG-006 | Competitor analysis | Medium | **Done** | Full analysis at docs/competitor-analysis.md — 5 competitors, llms.txt checks, content strategy, schema audit |
| HG-007 | Add H1 tags to 21 pages missing them | High | Blocked | Theme sections have H1 disabled — needs design decision (enable main-page/page-banner or edit sw-- sections) |
| HG-014 | Create "GHK-Cu Hair Serum" comparison guide | Medium | Planned | Review/comparison format — not ranking for this keyword |
| HG-016 | Page speed audit | Low | Planned | Not yet checked |
| HG-017 | Add URL redirect /llms.txt → /pages/llms-txt | Medium | Planned | Shopify can't serve files at root — need redirect for AI crawlers |

## Completed

| ID | Task | Completed | Notes |
|----|------|-----------|-------|
| HG-000 | Project setup — repo, docs, agency registration | 2026-03-03 | Initial structure |
| HG-001 | Run initial SEO audit with SEO Toolkit | 2026-03-03 | Technical: 83/100, AI: 74/100, Content: 64/100 avg |
| HG-003 | Keyword research — hair growth niche | 2026-03-03 | 104 keywords, 4 clusters, 3 quick wins identified |
| HG-004 | Content strategy — define pillars and plan | 2026-03-03 | Priorities defined in seo-strategy.md |
| HG-008 | Update meta titles on 20 pages | 2026-03-03 | All pages updated via GraphQL pageUpdate with keyword-optimised titles |
| HG-009 | Update meta descriptions on 20 pages | 2026-03-03 | All pages updated — unique, compelling descriptions under 155 chars |
| HG-011 | Create llms.txt file | 2026-03-03 | Live at /pages/llms-txt — custom layout (none.liquid), section, template |
| HG-012 | Add FAQPage, Article, HowTo, BreadcrumbList schema | 2026-03-03 | snippets/seo-schema.liquid injected into theme.liquid — all 4 types verified live |
| HG-013 | Create "Copper Peptide Hair Growth" guide | 2026-03-03 | 15K char pillar page at /pages/copper-peptides-hair-growth |
| HG-015 | Create "Hair Mesotherapy" hub page | 2026-03-03 | 14K char pillar page at /pages/hair-mesotherapy — strengthens #2 ranking |
| HG-020 | Create Press & Media page | 2026-03-03 | 4 press articles at /pages/press — CelebDigest, Women's Insider, USA News, Men's Insider |
| HG-021 | Re-run SEO audit — post-implementation | 2026-03-03 | Technical: 83/100 (unchanged), AI Discovery: 79/100 (was 74 = +5), Schema diversity: 10/10 (was 4/10) |
| HG-010 | Add alt text to images across site | 2026-03-03 | 26 images updated with SEO-optimised alt text via REST API (6 products) |
| HG-018 | Re-authorize Shopify API with product scopes | 2026-03-03 | New API with all scopes — client credentials grant flow |
| HG-019 | Update product meta titles and descriptions | 2026-03-03 | 16 products — meta titles under 60 chars, descriptions under 155 chars |
| HG-006 | Competitor analysis | 2026-03-03 | 5 competitors researched: Foligain, Hairmax, Nutrafol, Keeps, MinoxidilMax. Full report at docs/competitor-analysis.md |

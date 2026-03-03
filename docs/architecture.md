# Architecture — Hairgenetix (CLIENT-002)

> Last updated: 2026-03-03

## System Diagram

```
┌─────────────────────────────────────────────────┐
│                  hairgenetix.com                  │
│              (Shopify — hosted)                   │
├─────────────────────────────────────────────────┤
│  Products  │  Pages  │  Blog  │  Checkout  │ i18n│
└──────┬──────────┬──────────┬────────────────────┘
       │          │          │
       ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Shopify  │ │ Analytics│ │  Email   │
│  Payments│ │ GA4 + GSC│ │ (TBD)   │
└──────────┘ └──────────┘ └──────────┘
       │
       ▼
┌─────────────────────────────────────────────────┐
│           Smith AI Agency Services                │
├──────────────┬──────────────┬───────────────────┤
│ SEO Toolkit  │ Marketing    │ AI Content        │
│ (PROD-001)   │ Engine       │ Generation        │
└──────────────┴──────────────┴───────────────────┘
```

## Tech Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Platform | Shopify | Hosted e-commerce |
| Domain | hairgenetix.com | |
| Languages | 9 (EN, NL, DE, FR, ES, IT, PT, SV, DA) | Multi-market |
| Analytics | TBD | Needs verification |
| Email | TBD | Needs verification |
| SEO | SEO Toolkit (PROD-001) | Planned |

## Integrations

| Service | Purpose | Status |
|---------|---------|--------|
| Shopify | E-commerce platform | Live |
| Google Analytics 4 | Traffic analytics | TBD — verify |
| Google Search Console | SEO monitoring | TBD — verify |
| SEO Toolkit | Audits + keyword research | Planned |

## Change Log

| Date | Change | By |
|------|--------|----|
| 2026-03-03 | Project created, initial architecture | Claude |

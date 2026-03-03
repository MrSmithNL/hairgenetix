# Project Instructions — Hairgenetix (CLIENT-002)

These instructions apply to this project in every session.

---

## What This Project Is

**Hairgenetix** is an existing Shopify e-commerce store selling science-backed hair growth products (copper peptide serum, mesotherapy kits). The site is live at **hairgenetix.com** with 9-language support, 1,200+ reviews, and a 4-month money-back guarantee.

This repo contains documentation, SEO strategy, content, and automation scripts for improving and growing the Hairgenetix business using Smith AI Agency products and services.

**The Shopify store itself is hosted on Shopify** — we don't manage the Shopify codebase here. This repo manages everything around it: SEO, content, analytics, marketing automation, and AI-powered improvements.

---

## Project Identity

| Field | Value |
|-------|-------|
| **Project ID** | CLIENT-002 |
| **Domain** | hairgenetix.com |
| **Platform** | Shopify |
| **Repo** | github.com/MrSmithNL/hairgenetix |
| **Type** | E-commerce |
| **Status** | Live — optimisation phase |
| **Client** | Malcolm Smith (internal) |

---

## Agency Products Used

| Product | How It's Used | Status |
|---------|--------------|--------|
| SEO Toolkit (PROD-001) | SEO audits, keyword research, content optimization | Planned |
| Marketing Engine (PROD-003) | Content generation, social media, email campaigns | Planned |

---

## Skills Check — Always First

Before taking any action, check `~/.claude/skills/` for a relevant skill. 864 are installed.

---

## Autonomous Permissions

Malcolm has granted full autonomous permission for:
- Update any `.md` file in this repo
- Create new `.md` files in `docs/`
- Commit and push documentation-only changes to GitHub
- Run SEO toolkit audits and analysis
- Update cross-references in other projects when relevant

Always confirm before: making changes to the live Shopify store, running paid campaigns, or any action with external visibility.

---

## Architecture Maintenance — Always Automatic

After any change to strategy, infrastructure, tools, or accounts:
1. Update `docs/architecture.md`
2. Update `docs/todo.md`
3. Commit and push

---

## Folder Structure

```
hairgenetix/
├── CLAUDE.md                          ← This file
├── README.md                          ← Project overview
├── docs/
│   ├── architecture.md                ← System diagram + integrations
│   ├── todo.md                        ← Tasks with IDs and priorities
│   ├── decisions-log.md               ← Key decisions
│   ├── accounts-and-access.md         ← Credentials (Bitwarden refs)
│   ├── security-risk-log.md           ← Risks and mitigations
│   ├── processes-and-flows.md         ← Workflows and procedures
│   ├── content-strategy.md            ← Content plan and pillars
│   ├── seo-strategy.md               ← Keywords and optimisation
│   └── metrics.md                     ← Analytics setup + KPIs
└── .gitignore                         ← Standard ignores
```

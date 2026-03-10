# Project Instructions — Hairgenetix (CLIENT-002)

These instructions apply to this project in every session.

---

## What This Project Is

**Hairgenetix** is a Shopify e-commerce store selling science-backed hair growth products (copper peptide serum, mesotherapy kits). Live at **hairgenetix.com** with 9-language support, 1,200+ reviews, 4-month money-back guarantee.

This repo manages everything around the store: SEO, content, analytics, marketing automation, and AI-powered improvements. The Shopify store itself is hosted on Shopify.

---

## Related Projects

- **Agency standards:** `~/Claude Code/Projects/smith-ai-agency/docs/capabilities/`
- **SEO engine (PROD-001):** `~/Claude Code/Projects/seo-toolkit/` — audits and optimization
- **Sister brand (CLIENT-003):** `~/Claude Code/Projects/skingenetix-website/`

---

## Project Identity

| Field | Value |
|-------|-------|
| **Project ID** | CLIENT-002 |
| **Domain** | hairgenetix.com |
| **Shopify admin** | a24be5-c5.myshopify.com |
| **Platform** | Shopify |
| **Repo** | github.com/MrSmithNL/hairgenetix |

---

## Agency-Wide Delivery Framework

This project operates under the agency's autonomous delivery framework. All standards, processes, and department manager oversight apply here:

- **Quality Manager** — Code quality, testing, documentation standards (`smith-ai-agency/docs/capabilities/quality-manager.md`)
- **DevOps Manager** — CI/CD, deployment, infrastructure reliability (`smith-ai-agency/docs/capabilities/devops-manager.md`)
- **Technical Architect** — Architecture decisions, fitness functions, dependency governance (`smith-ai-agency/docs/capabilities/technical-architect.md`)
- **Delivery Manager** — Sprint planning, objective tracking, blocker resolution (`smith-ai-agency/docs/capabilities/delivery-manager.md`)
- **Requirements Engineering** — Spec-driven development, 3-gate process (`smith-ai-agency/docs/capabilities/requirements-engineering.md`)
- **Sprint Management** — 2-week cadence, velocity tracking (`smith-ai-agency/objectives/sprints/`)

---

## Autonomous Permissions

No confirmation needed: update `.md` files, create docs, commit/push docs-only, run SEO audits.

Always confirm before: changes to the live Shopify store, running paid campaigns, any action with external visibility.

---

## Architecture Maintenance — Always Automatic

After any change to strategy, infrastructure, tools, or accounts: update `docs/architecture.md` + `docs/todo.md`, commit and push.

---

## Key Docs

| File | What It Covers |
|------|---------------|
| `docs/todo.md` | Tasks with IDs and priorities |
| `docs/architecture.md` | System diagram + integrations |
| `docs/content-strategy.md` | Content plan and pillars |
| `docs/seo-strategy.md` | Keywords and optimisation |

Scripts require `SHOPIFY_ACCESS_TOKEN` env var — tokens must never be hardcoded.

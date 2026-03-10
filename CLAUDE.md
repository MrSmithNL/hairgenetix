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

Before taking any action, check `~/.claude/skills/` for a relevant skill. 40 core skills installed (plus ~832 Composio tool connectors).

---

## Capability Hierarchy — Mandatory

This project follows the agency's 5-layer capability hierarchy: **Products → Capabilities → Agents → Skills → Tools**. See the [Capability Hierarchy](~/Claude Code/Projects/smith-ai-agency/docs/capability-hierarchy.md) reference. Use terms precisely: Tools are external connections (Composio, MCP, APIs). Skills are procedural knowledge (`~/.claude/skills/`). Agents are autonomous workers (`~/.claude/agents/`). Capabilities are business-level abilities. Products are sellable platforms.

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

## Code Quality Enforcement

| Tool | What It Checks | Config File |
|------|---------------|-------------|
| **ruff** | Python lint + format | `ruff.toml` |
| **markdownlint** | Markdown style | `.markdownlint.yaml` |
| **detect-secrets** | Hardcoded secrets | `.secrets.baseline` |
| **yamllint** | YAML validity | (relaxed preset) |
| **pre-commit** | All hooks on commit | `.pre-commit-config.yaml` |

**CI pipelines** (`.github/workflows/`):
- `ci.yml` — Python lint, Markdown lint, secret scan, YAML validation (runs on push/PR to main)
- `codeql.yml` — GitHub CodeQL SAST for Python (weekly + on script changes)
- `docs.yml` — MkDocs documentation deployment

**Scripts require `SHOPIFY_ACCESS_TOKEN` environment variable** — tokens must never be hardcoded.

### Running locally

```bash
# Install tools
pip install ruff pre-commit detect-secrets

# Set up pre-commit hooks (one-time)
pre-commit install

# Run all checks
pre-commit run --all-files

# Or individually
ruff check scripts/
ruff format --check scripts/
```

---

## Folder Structure

```
hairgenetix/
├── CLAUDE.md                          ← This file
├── README.md                          ← Project overview
├── ruff.toml                          ← Python linter config
├── .markdownlint.yaml                 ← Markdown linter config
├── .pre-commit-config.yaml            ← Pre-commit hooks
├── .secrets.baseline                  ← Secret detection baseline
├── mkdocs.yml                         ← MkDocs site config
├── .github/workflows/
│   ├── ci.yml                         ← Lint + quality CI
│   ├── codeql.yml                     ← CodeQL SAST
│   └── docs.yml                       ← MkDocs deployment
├── scripts/
│   ├── fix-norwegian.py               ← Norwegian translation fix
│   └── register-meta-translations.py  ← Bulk translation registration
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

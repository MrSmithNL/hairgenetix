# AGENTS.md — Hairgenetix (CLIENT-002)

> Tool-agnostic agent instructions. Works with Claude Code, Cursor, Codex, Aider, and any tool that supports AGENTS.md.

## Project Overview

Documentation, SEO strategy, content, and automation scripts for Hairgenetix — a Shopify e-commerce store selling science-backed hair growth products. Live at hairgenetix.com with 9-language support. The Shopify store is hosted on Shopify; this repo manages everything around it.

## Tech Stack

- **Platform:** Shopify (GraphQL Admin API)
- **Language:** Python 3.11+ (scripts only)
- **Linting:** ruff (ruff.toml with bandit security rules)
- **Markdown:** markdownlint (.markdownlint.yaml)
- **Pre-commit:** black, ruff, detect-secrets, markdownlint
- **CI:** GitHub Actions (Python lint, Markdown lint, secret scan, YAML validation, CodeQL SAST)
- **Docs:** MkDocs Material

## Commands

```bash
# Lint Python
ruff check scripts/
ruff format --check scripts/

# Lint Markdown
markdownlint docs/

# All pre-commit hooks
pre-commit run --all-files

# Secret detection
detect-secrets scan
```

## Project Structure

```
scripts/     # Python automation (translations, fixes)
docs/        # Strategy, architecture, SEO, content, audits
research/    # Market analysis, competitor research
```

## Style Guide

- Python: ruff + black formatted, bandit security rules
- Markdown: markdownlint compliant
- All scripts use SHOPIFY_ACCESS_TOKEN env var (never hardcoded)
- Commit messages: imperative mood

## Boundaries

- **Always do:** Run pre-commit hooks. Update docs/todo.md after changes.
- **Ask first:** Any Shopify store changes, paid campaigns, external-facing actions.
- **Never do:** Hardcode API tokens, commit secrets, modify Shopify theme without approval.

---
paths:
  - "scripts/**/*.py"
---
# Hairgenetix Code Quality Rules

- All Python scripts linted with `ruff` (config: `ruff.toml`, includes bandit security rules)
- Markdown linted with `markdownlint` (config: `.markdownlint.yaml`)
- Pre-commit hooks: black, ruff, secret detection, markdownlint (`.pre-commit-config.yaml`)
- CI: 4 jobs — Python lint, Markdown lint, secret detection, YAML validation
- CodeQL SAST for Python (weekly + on script changes)
- SECURITY: Never hardcode Shopify API tokens — use `SHOPIFY_ACCESS_TOKEN` env var
- Run `pre-commit run --all-files` before pushing

# Forge WordPress — Tool Registry v1

**Document type:** Subsystem local tool registry  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**Note:** Local subsystem registry — **not** global `tools/registry.md`. Status reflects **audit evidence** where checked.

---

## Status legend

`REQUIRED` · `RECOMMENDED` · `CANDIDATE` · `OPTIONAL` · `DEFERRED` · `REJECTED`

---

## Registry

| Tool ID | Tool | Purpose | Status | Req/Cand/Def | Environment | Install scope | Risk | Allowed ops | Forbidden ops | Human approval | Rollback | Windows | Shared host | Owner | Evidence |
|---------|------|---------|--------|--------------|-------------|---------------|------|-------------|---------------|----------------|----------|---------|-------------|-------|----------|
| FW-TOL-001 | Git | Version control | **REQUIRED** | Required | Local | System | R0–R1 | status, diff, commit | force push main | commit/push | revert | **Yes** | N/A | Operator | Audit: 2.54.0 |
| FW-TOL-002 | Node.js | Frontend toolchain | **REQUIRED** | Required | Local | System | R1 | build | global npm pollution | major upgrade | reinstall | **Yes** | N/A | Operator | Audit: v24.13.1 |
| FW-TOL-003 | npm | Package runner | **REQUIRED** | Required | Local | System | R1 | install, run | — | install | lock restore | **Yes** | N/A | Operator | Audit: 11.8.0 |
| FW-TOL-004 | Gulp | Factory build | **REQUIRED** | Required | Project | Project | R1 | build, watch | replace with Vite w/o charter | — | git restore | **Yes** | N/A | Gulp Frontend | Audit: CLI 3.1.0 |
| FW-TOL-005 | PHP | WP runtime | **REQUIRED** | Required | Local | Local stack | R2 | lint, execute WP | prod execution | stack install | reinstall | **Yes** | Target match | Operator | **Not detected** |
| FW-TOL-006 | Composer | PHP deps | **RECOMMENDED** | Candidate | Project | Project/global | R1 | install | unvetted packages | new deps | lock restore | **Yes** | If host allows | Operator | **Not detected** |
| FW-TOL-007 | MySQL/MariaDB | WP database | **REQUIRED** | Required | Local | Local stack | R2 | local queries | prod DB | import/export | restore dump | **Yes** | **Yes** | Local | **Not detected** |
| FW-TOL-008 | Local (Flywheel) | Default WP env | **REQUIRED** | Required | Local | Per-machine | R2 | site CRUD | prod | create site | delete site | **Yes** | N/A | Operator | **Not detected** |
| FW-TOL-009 | Laragon | Default fallback | **RECOMMENDED** | Candidate | Local | Per-machine | R2 | same as Local | prod | install | uninstall | **Yes** | N/A | Operator | **Not detected** |
| FW-TOL-010 | WP-CLI | WP automation | **REQUIRED** | Required | Local/DEV | Local/global | R0–R2 | read/write local | remote prod | destructive write | DB restore | **Yes** | If provided | Operator | **Not detected** |
| FW-TOL-011 | PHPCS | PHP lint standard | **REQUIRED** | Required | Local/CI | Project | R0 | scan | — | waiver | fix code | **Yes** | N/A | Validator | **Not detected** |
| FW-TOL-012 | WPCS | WP coding standard | **REQUIRED** | Required | Local/CI | Project | R0 | scan | — | waiver | fix code | **Yes** | N/A | Validator | **Not detected** |
| FW-TOL-013 | PHPStan | Static analysis | **OPTIONAL** | Deferred | Local | Project | R0 | analyse | — | adopt per project | — | **Yes** | N/A | Validator | Not installed |
| FW-TOL-014 | PHPUnit | PHP tests | **CANDIDATE** | Candidate | Local | Project | R0 | test | — | — | — | **Yes** | Rare | Validator | Not installed |
| FW-TOL-015 | Playwright | E2E + screenshots | **REQUIRED** | Required | Local | Project | R0 | test, screenshot | prod crawl | baseline capture | discard run | **Yes** | N/A | Validator | Audit: 1.61.0 npx |
| FW-TOL-016 | pixelmatch | Visual diff | **RECOMMENDED** | Recommended | Local | Project | R0 | compare | — | threshold change | re-baseline | **Yes** | N/A | Validator | npm dep — not verified |
| FW-TOL-017 | axe-playwright | a11y | **RECOMMENDED** | Recommended | Local | Project | R0 | scan | — | waiver | fix | **Yes** | N/A | Validator | Not verified |
| FW-TOL-018 | Lighthouse CLI | Performance | **RECOMMENDED** | Recommended | Local | Project | R0 | audit | — | waiver | — | **Yes** | Post-deploy | Validator | Not verified |
| FW-TOL-019 | WP Playground | Lightweight env | **RECOMMENDED** | Recommended | Browser/CLI | npx | R0 | preview | full dev | — | — | **Yes** | Low parity | Operator | Not installed |
| FW-TOL-020 | Docker | Container stack | **DEFERRED** | Deferred | — | — | — | — | mandatory default | charter | — | Optional | N/A | — | **Not detected** |
| FW-TOL-021 | DDEV | Dev containers | **DEFERRED** | Deferred | — | — | — | — | default | charter | — | WSL2 | N/A | — | **Not detected** |
| FW-TOL-022 | wp-env | WP docker env | **DEFERRED** | Deferred | — | — | — | — | default | — | — | Docker | N/A | — | **Not detected** |
| FW-TOL-023 | BackstopJS | Visual regression | **OPTIONAL** | Candidate | Local | Project | R0 | compare | — | — | — | **Yes** | N/A | Validator | Alternative to Playwright |
| FW-TOL-024 | Percy | Cloud visual | **DEFERRED** | Deferred | SaaS | — | — | — | default (cost) | — | — | **Yes** | N/A | — | Not adopted |
| FW-TOL-025 | WPScan | Vuln scan | **CANDIDATE** | Candidate | Local | CLI | R0 | scan | exploit | plugin add | — | **Yes** | Limited | Security | Not installed |
| FW-TOL-026 | git-secrets / trufflehog | Secret scan | **RECOMMENDED** | Recommended | Local/CI | Project | R0 | scan | — | — | — | **Yes** | N/A | Security | Not verified |
| FW-TOL-027 | zip + checksum | Packaging | **REQUIRED** | Required | Local | OS/built-in | R3 | package | — | release | delete artifact | **Yes** | FTP deploy | Operator | OS built-in |
| FW-TOL-028 | HTML validator | Markup | **OPTIONAL** | Optional | Local | nu-cli | R0 | validate | — | — | — | **Yes** | N/A | Validator | Not installed |
| FW-TOL-029 | ESLint | JS lint | **RECOMMENDED** | Recommended | Project | Project | R0 | lint | — | — | — | **Yes** | N/A | Frontend | If JS modules |
| FW-TOL-030 | Stylelint | CSS lint | **OPTIONAL** | Optional | Project | Project | R0 | lint | — | — | — | **Yes** | N/A | Frontend | Optional |

---

## Rejected

| Tool | Status | Reason |
|------|--------|--------|
| Mandatory Docker | **REJECTED** | Windows friction; audit shows absent |
| Playground as sole env | **REJECTED** | Incomplete WP dev surface |
| Autonomous deploy CLI | **REJECTED** | WPilot domain |

---

## Related

- [reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md](../reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md)
- [FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md](../FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md)

---

*Tool registry v1 — evidence-aligned; install is operator action.*

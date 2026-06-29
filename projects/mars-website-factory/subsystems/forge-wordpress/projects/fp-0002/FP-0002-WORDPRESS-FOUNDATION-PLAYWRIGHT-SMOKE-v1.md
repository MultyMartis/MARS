# FP-0002 — WordPress Foundation Playwright Smoke v1

**Version:** v1 | **Date:** 2026-06-23 | **Stage:** FW-06A.1

## Toolchain

| Field | Value |
|-------|-------|
| Location | `X:\MARS-Localhost\tools\playwright-smoke\` |
| Fixture | `smoke/fp-0002-shpigovsky-foundation.test.js` |
| Config | `playwright.fp0002.config.js` (no `--host-resolver-rules`) |
| Target | `http://shpigovsky.test/` |

## Scope

Direct-domain foundation smoke only. No frontend integration validation.

## Tests

| ID | Route | Assertions |
|----|-------|------------|
| FP-0002-001 | `/` | HTTP 200, site title, foundation H1, no production URL, no directory listing, no page/console errors |
| FP-0002-002 | `/wp-login.php` | HTTP 200, login form visible |
| FP-0002-003 | `/wp-json/` | HTTP 200, REST name matches site title |
| FP-0002-004 | `/uslugi/` | HTTP 200, foundation H1 |
| FP-0002-005 | `/privacy-policy/` | HTTP 200, foundation H1 (legal skeleton) |

## Execution

```powershell
Set-Location X:\MARS-Localhost\tools\playwright-smoke
npx playwright test --config=playwright.fp0002.config.js
```

## Artifacts (runtime only — not in Git)

```text
X:\MARS-Localhost\tools\playwright-smoke\artifacts\fp-0002\
X:\MARS-Localhost\tools\playwright-smoke\test-results\
```

## Closure (FW-06A.1)

```text
Direct domain:
PASS — no Host-header workaround

Playwright foundation smoke:
PASS (FW-06A.1 automated run)

Closure date:
2026-06-23
```

---

*FP-0002 Playwright foundation smoke report — FW-06A.1.*

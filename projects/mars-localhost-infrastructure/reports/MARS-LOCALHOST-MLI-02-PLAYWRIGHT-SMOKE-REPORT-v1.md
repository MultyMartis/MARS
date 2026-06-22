# MARS Localhost MLI-02 — Playwright Smoke Report v1

**Document type:** Playwright smoke report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Fixture

```text
D:\MARS-Localhost\tools\playwright-smoke\
```

Project-local `package.json`, lockfile, `@playwright/test`, Chromium installed locally.

---

## HTTP test (MLI-SMOKE-009)

| Check | Result |
|-------|--------|
| URL | `http://127.0.0.1/` + `Host: mli-smoke-001.test` (hosts pending) |
| HTTP status | **200** |
| Heading | **MARS Localhost** |
| Console errors | **None** |
| Screenshot | `artifacts\mli-smoke-001-http.png` |
| Headless | **PASS** |
| Exit code | **0** |

---

## HTTPS test (MLI-SMOKE-008)

| Check | Result |
|-------|--------|
| URL | `https://mli-smoke-001.test/` via Chromium host resolver map |
| HTTP status | **200** |
| `ignoreHTTPSErrors` | **Yes** (self-signed) |
| Screenshot | `artifacts\mli-smoke-001-https.png` |
| Exit code | **0** |

---

## Artifacts (outside Git)

- `node_modules\`
- `artifacts\*.png`
- Playwright browser cache

---

## Related

- [MARS-LOCALHOST-NODE-AND-NPM-STANDARD-v1.md](../MARS-LOCALHOST-NODE-AND-NPM-STANDARD-v1.md)

---

*Playwright smoke report v1 — MLI-02.*

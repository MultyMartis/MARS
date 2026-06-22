# MARS Localhost MLI-02 — Cursor Access Report v1

**Document type:** Cursor access verification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Methods

| # | Method | Result |
|---|--------|--------|
| 1 | Cursor terminal — `curl` / `Invoke-WebRequest` | **PASS WITH LIMITATION** |
| 2 | Playwright headless | **PASS** |
| 3 | Cursor built-in browser tool | **NOT EXECUTED** |

---

## Detail

### Terminal HTTP

- `curl -H "Host: mli-smoke-001.test" http://127.0.0.1/` → **200**
- Direct `http://mli-smoke-001.test/` → **FAIL** until hosts elevation (expected)

### Terminal HTTPS

- OpenSSL `s_client` with SNI → **PASS**
- Windows `curl` schannel to IP → **LIMITATION** documented

### Playwright

See [MARS-LOCALHOST-MLI-02-PLAYWRIGHT-SMOKE-REPORT-v1.md](MARS-LOCALHOST-MLI-02-PLAYWRIGHT-SMOKE-REPORT-v1.md).

### Cursor browser MCP

Not required for MLI-02 success criteria.

---

*Cursor access report v1 — MLI-02.*

---

## Post-report closure note (2026-06-23)

Added at MLI-03 validation closeout. Original MLI-02 results above are unchanged.

| Check | Result |
|-------|--------|
| Direct `.test` domain (`mli-smoke-001.test`) | **PASS** — DNS 127.0.0.1 |
| Hosts managed entry | **PASS** |
| Browser access | **OPERATOR-VERIFIED PASS** |

Terminal direct-URL failure noted in MLI-02 Detail is **superseded** for `mli-smoke-001.test` after hosts elevation and operator browser verification.

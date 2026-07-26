# METALLKA — WPilot Token Creation Evidence v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4B  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Status:** **TOKEN CREATED — LOCAL ONLY / NOT REST-TESTED**

```text
This artefact MUST NOT contain token plaintext, hashes of the token,
Authorization headers, or X-WPilot-Token values.
```

---

## 1. Preconditions (met)

| Gate | Result |
|------|--------|
| Safe defaults before token (`bridge` / `write` / `dev_confirmed` false) | **PASS** |
| Local token path gitignored | **PASS** (`git check-ignore` → `.gitignore:13:/local/`) |
| Token file did not already exist | **PASS** |
| Bridge enable | **NOT PERFORMED** |
| REST calls | **0** |

---

## 2. Creation

| Field | Value |
|-------|-------|
| Mechanism | WPilot admin → Safety → Generate / Rotate Token |
| Tokens created | **1** |
| Regenerations | **0** |
| Captured once from admin notice | **YES** |
| Format check | prefix `wpilot_` · length **55** · charset OK |
| Persisted path | `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` |
| File content policy | plaintext token only (single value) |
| File bytes (incl. trailing newline) | **57** |
| Auth header name (future) | `X-WPilot-Token` |

---

## 3. Post-creation validation

| Check | Result |
|-------|--------|
| Local file exists / non-empty | **YES** |
| Still gitignored | **YES** |
| Appears in tracked `git status` as content | **NO** |
| `bridge_enabled` after | **false** |
| `write_enabled` after | **false** |
| `dev_confirmed` after | **false** |
| Token authentication proven | **NO** (forbidden in 4B) |
| Token leaked | **NO** |

---

## 4. Explicit non-actions

- No `/wp-json/wpilot/v1/*` call  
- No bridge enable “to verify”  
- No second token  
- No copy into `secrets.local.md`  
- No tracked markdown containing token value  

---

*METALLKA WPilot Token Creation Evidence v1 · Phase 4B.*

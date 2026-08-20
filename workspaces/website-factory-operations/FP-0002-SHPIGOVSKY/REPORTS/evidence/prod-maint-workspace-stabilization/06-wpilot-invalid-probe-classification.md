# WPilot probe classification — INVALID EVIDENCE (Bearer / TLS)

**Date:** 2026-08-20  
**Project:** FP-0002 / shpigovsky.ru  
**Production mutations:** none  

---

## Prior probe (INVALID EVIDENCE)

| Field | Value |
|-------|--------|
| Context | Background / housekeeping WPilot health probe (operator charter) |
| Auth used | `Authorization: Bearer <token>` |
| Transport | TLS disconnect / timeout reported |
| Classification | **INVALID EVIDENCE** |
| Explicitly NOT | production outage; WPilot outage; indexing issue; runtime regression |

Wrong auth contract for FP-0002 / MetaCODE WPilot. Canonical header is `X-WPilot-Token` (`WPilot_Constants::TOKEN_HEADER_NAME`).

---

## Replacement probe (VALID)

| Field | Value |
|-------|--------|
| Auth | `X-WPilot-Token` (value **REDACTED**; local path `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`) |
| Homepage | `https://shpigovsky.ru/` → **HTTP 200** |
| `GET /wp-json/wpilot/v1/ping` | 200 (auth not required for ping) |
| `GET /wp-json/wpilot/v1/site-info` with `X-WPilot-Token` | **200** `VALID_RUNTIME_RESPONSE` |
| Same endpoint with `Authorization: Bearer` (wrong) | **401** `AUTH_ERROR` |
| Core plugin | **Shpigovsky Core = 0.3.24-antispam** (authenticated plugins list) |
| Indexing signals | `robots.txt` crawlable + Sitemap; homepage **no** `noindex`; prior human-approved OPEN / `blog_public=1` retained |
| Forms anti-spam markers | honeypot + `fp02_fs` present on homepage |
| WPilot | bridge on; `write_enabled=false` |

Machine JSON: `06-wpilot-probe-replacement.json`

---

## Classification vocabulary (reusable)

| Class | Meaning |
|-------|---------|
| `TRANSPORT_ERROR` | TLS/timeout/connection failure — not application truth |
| `AUTH_ERROR` | Wrong or missing site auth contract (e.g. Bearer vs `X-WPilot-Token`) |
| `APPLICATION_ERROR` | Authenticated request reached app with non-success business status |
| `VALID_RUNTIME_RESPONSE` | Authenticated (or correctly unauthenticated) response usable as evidence |

A failed transport or wrong-auth attempt **must not** remain in CURRENT project status as an incident when replaced by a successful correct probe.

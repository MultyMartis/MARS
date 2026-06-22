# MARS Localhost MLI-01 — Browser Smoke Report v1

**Document type:** Browser / HTTP smoke verification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01  
**Target:** `mli-smoke-001.test`

---

## Method

| Method | Used |
|--------|------|
| Cursor browser tooling | **NOT EXECUTED** — not available in agent session |
| PowerShell `Invoke-WebRequest` | **YES** |
| System browser | **NOT EXECUTED** |

---

## HTTP verification

| Check | Result |
|-------|--------|
| URL (Host header) | `http://127.0.0.1/` + `Host: mli-smoke-001.test` |
| HTTP status | **200** |
| PHP execution | **PASS** — page renders MLI smoke content |
| PHP version displayed | 8.3.30 (no full phpinfo) |
| Path disclosure | **PASS** — no filesystem paths in output |
| Directory listing | **PASS** — not observed |
| Console errors | **NOT EXECUTED** (no browser automation) |

---

## Domain resolution

| Check | Result |
|-------|--------|
| `http://mli-smoke-001.test/` direct | **FAIL** — hosts entry not writable without elevation |
| Laragon Auto Virtual Hosts | **PASS WITH LIMITATION** — requires admin for hosts file |
| Workaround verified | Host header test **PASS** |

**Operator action:** Open Laragon → Start All (regenerates hosts) or add `127.0.0.1 mli-smoke-001.test` manually as admin.

---

## HTTPS

| Check | Result |
|-------|--------|
| `https://mli-smoke-001.test/` | **NOT EXECUTED** — hosts + cert not verified |
| Baseline | **HTTP** for MLI-01 |

---

## Classification

**Overall browser smoke:** **PASS WITH LIMITATION** (HTTP via Host header; domain DNS pending hosts elevation)

---

*Browser smoke report v1 — MLI-01.*

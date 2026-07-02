# SITE-002 — STABLE PRODUCTION — Initial Baseline 01

**Status:** **ACTIVE** — first Production read-only baseline  
**Environment:** PRODUCTION (`site-002-prod`)  
**URL:** https://bzpm.ru/  
**Date:** 2026-07-02  
**OCPilot run:** 4.171-R1 (continuation of Run 4.171)  
**Operation ID:** SITE-002-PROD-INITIAL-CAPTURE-01  
**Report:** [SITE-002-FIRST-PRODUCTION-CAPTURE.md](../reports/SITE-002-FIRST-PRODUCTION-CAPTURE.md)

---

## Scope

First authorized read-only Production baseline for SITE-002. Establishes file-level reference for controlled Production work.

| Area | Evidence |
|------|----------|
| FTP read-only access | **VERIFIED** (retry after credential correction) |
| Application root | `/bzpm.ru/` (secrets `Remote root`; FTP chroot maps to login `/`) |
| Public document root | `/bzpm.ru/public_html/` — FTP-visible `/public_html/` |
| OpenCart storage root | `/bzpm.ru/storage/` — FTP-visible `/storage/` |
| Platform | OpenCart / ocStore **3.0.3.9** — CONFIRMED |
| Active theme | `default` — CONFIRMED |
| HTTP corporate pages | **PASS** (Run 4.171 initial capture) |
| File baseline | 24 implementation-surface files + SHA-256 |
| Remote mutations | **0** |

---

## Storage binding

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-INITIAL-01\
```

Capture root (HTTP/screenshots/admin):

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01\
```

---

## Key file hashes (baseline download)

| Remote path | SHA256 |
|-------------|--------|
| `catalog/view/theme/default/template/information/guarantee.twig` | see `downloaded-files-sha256.csv` |
| `assets/css/style.css` | `75de637812b62d3d62c4b1f0fe226b22e519023a8ac7aa31acae658d896b6267` |
| `assets/js/main.js` | `073296c0d04839b193e4f5d4c9a42dd6505645e6c97af6425060964da1b4f9d7` |

Full manifest: storage baseline `manifests/downloaded-files-sha256.csv`

---

## Production vs TEST parity (summary)

| Domain | Classification |
|--------|----------------|
| M9.13–M9.18 corporate pages | **FUNCTIONALLY PRESENT** (file + HTTP) |
| Home Commercial Trust | **MATCH CONFIRMED** |
| Corporate intro / proof strips | **FUNCTIONALLY PRESENT** |
| PDP body/category classes | **MATCH CONFIRMED** (`product.php`) |
| Local Fonts (`style.css`) | **MATCH CONFIRMED** |

Matrix: capture `manifests/production-test-parity-matrix.json`

---

## First controlled test readiness

| Field | Value |
|-------|-------|
| Page | https://bzpm.ru/guarantee |
| Template | `catalog/view/theme/default/template/information/guarantee.twig` |
| Hosting path | `/bzpm.ru/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| FTP path | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Phrase present | «понятный порядок действий» — **CONFIRMED** in downloaded twig |
| Proposed test change | «понятный порядок действий» → «чёткий порядок действий» |
| Classification | **TEST TASK CONFIRMED** |

---

## Supersedes

- [SITE-002-PRODUCTION-BASELINE-PENDING.md](SITE-002-PRODUCTION-BASELINE-PENDING.md) — **SUPERSEDED**

## Preserved

- All TEST-era stable checkpoints under `baselines/` — remain implementation evidence
- Run 4.171 partial capture history in report §FTP RETRY

---

## Rollback authority

This checkpoint is a **read-only reference baseline**, not a deploy rollback package. Production writes require scoped backup per Production Profile.

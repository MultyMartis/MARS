# Forge WordPress FW-05R — Direct Domain Closure v1

**Document type:** Post-validation closure record  
**Version:** v1  
**Date:** 2026-06-23  
**Case:** FWS-0001 / MLI-WP-SYN-001  
**Domain:** `fws-0001.test`

---

## Purpose

Record **post-FW-05R** direct local domain resolution and HTTP smoke results. Historical FW-05R validation reports (Host header / Playwright resolver) are **not rewritten** — this document is an additive closure pass.

---

## Gate closure attempt (2026-06-23)

| Step | Result | Evidence |
|------|--------|----------|
| `Resolve-DnsName fws-0001.test` | **FAIL** | No A/AAAA record — domain not in hosts |
| `add-mli-host.ps1` from Cursor | **BLOCKED** | Exit 3 — administrator elevation required |
| UAC bypass attempted | **NO** | Per MLI hosts standard — operator-controlled elevation only |

**Operator command (elevated PowerShell):**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\MARS-Localhost\tools\hosts\add-mli-host.ps1"
ipconfig /flushdns
Resolve-DnsName fws-0001.test
Invoke-WebRequest http://fws-0001.test/
Invoke-WebRequest http://fws-0001.test/wp-login.php
Invoke-WebRequest http://fws-0001.test/wp-json/
```

**Direct local domain gate:** **NOT CLOSED** (pending operator hosts elevation)

---

## Direct URL smoke (required when gate closed)

| Route | Direct URL | HTTP | Title / content | PHP fatal | Classification |
|-------|------------|------|-----------------|-----------|----------------|
| Homepage | `http://fws-0001.test/` | — | — | — | **NOT EXECUTED** |
| Services archive | `http://fws-0001.test/services/` | — | — | — | **NOT EXECUTED** |
| Service single | `http://fws-0001.test/services/testovaya-usluga/` | — | — | — | **NOT EXECUTED** |
| Contacts | `http://fws-0001.test/contacts/` | — | — | — | **NOT EXECUTED** |
| Admin login | `http://fws-0001.test/wp-login.php` | — | — | — | **NOT EXECUTED** |
| REST | `http://fws-0001.test/wp-json/` | — | — | — | **NOT EXECUTED** |

**Playwright without `--host-resolver-rules`:** **NOT EXECUTED** — gate not closed; workaround not counted as direct-domain PASS.

---

## Supplementary runtime check (non-gate)

Host-header HTTP smoke against `127.0.0.1` with `Host: fws-0001.test` (2026-06-23 closure pass):

| Route | Status | Notes |
|-------|--------|-------|
| `/` | **200** | Runtime alive |
| `/services/` | **200** | CPT archive reachable |
| `/services/testovaya-usluga/` | **200** | CPT single reachable |
| `/contacts/` | **200** | Contacts template reachable |
| `/wp-login.php` | **200** | Admin login reachable |
| `/wp-json/` | **200** | REST reachable |

This confirms MLI Apache vhost + WordPress stack remain healthy. It **does not** close the direct-domain gate.

---

## Checks deferred until gate closed

| Check | Status |
|-------|--------|
| Expected page titles via direct URL | **NOT EXECUTED** |
| Browser console errors (direct URL) | **NOT EXECUTED** |
| Critical asset load (direct URL) | **NOT EXECUTED** |
| No directory listing | **NOT EXECUTED** |
| No production URLs in HTML | **NOT EXECUTED** (prior FW-05R reports: PASS WITH LIMITATIONS) |

---

## Overall closure classification

| Area | Result |
|------|--------|
| Direct DNS resolution | **FAIL** (pending elevation) |
| Direct HTTP frontend/admin/REST | **NOT EXECUTED** |
| Playwright direct-domain pass | **NOT EXECUTED** |
| Runtime availability (Host header) | **PASS** |
| FW-05R capability outcome | **UNCHANGED — PROVEN WITH LIMITATIONS** |

---

## Related

- [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md)
- [MARS-LOCALHOST-VHOST-REGISTRY-v1.md](../../../../../mars-localhost-infrastructure/registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md)
- [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../../../../../mars-localhost-infrastructure/manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md)

---

*Direct domain closure v1 — post-validation additive record.*

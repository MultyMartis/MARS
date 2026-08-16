# FP-0002 — Production Access Matrix v1

**Wave:** PROD-P05-FU01 (WPilot 0.3.2-RC1 + authenticated READ **PASS**)  
**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Rule:** Capability ≠ authorization. No secret values.

Local secrets (path only):  
`X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md`

```text
NEW BEGET DB = LIVE CONTENT / ADMIN AUTHORITY
BEGET FILESYSTEM = LIVE RUNTIME TRUTH
WPILOT AUTHENTICATED READ PROVEN
WRITES CLOSED BY POLICY (write_enabled=false)
```

---

## Matrix

| Surface | Purpose | Transport | Credential source | Read allowed | Write allowed | Default state | Approval requirement | Backup requirement | Rollback method | Owner | Notes |
|---------|---------|-----------|-------------------|--------------|---------------|---------------|----------------------|--------------------|-----------------|-------|-------|
| Public HTTP | Public inspection, frontend QA | HTTP to `shpigovsky.beget.tech` | N/A | **YES** | N/A | **ALLOWED** | Bounded scope; no mutation | N/A | N/A | FP-0002 Site Ops | Beget antibot cookie `beget=begetok` for some routes. `DNS_CUTOVER = DEFERRED` |
| WordPress Admin | Native authoring / settings inspection | `/wp-admin/` | `secrets.local.md` → WORDPRESS ADMIN | **YES — HTTP PROVEN (FU01)** | **Task-specific only** | `mars` = Administrator | Explicit task charter for any save | Layer A operator-confirmed post-reimport | Native revert / Layer A | FP-0002 Site Ops + operator | Do not save/update/dismiss notices without charter |
| WPilot REST | Structured WP entity inspect / bounded ops | `wpilot/v1` + `X-WPilot-Token` | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` | **YES — AUTHENTICATED READ PROVEN** | **NO** (disabled) | Plugin **active 0.3.2 / 0.3.2-RC1**; write off | Write = separate gate | Layer A + Layer B 0.3.0 snapshot | Layer B plugin dir + Layer A | WPilot (REST only) | Do not enable write |
| Filesystem | Theme/plugin/PHP/CSS/JS exact-file ops | **SSH preferred** (FTP also works) | `secrets.local.md` → FTP OR SFTP / SSH | **YES — PROVEN** | **NO** — **CLOSED BY POLICY** | Auth **VERIFIED**; real WP docroot **VERIFIED** | Exact allowlist + charter | Layer B exact file + Layer A | Re-upload prior bytes (Layer B) | FP-0002 Site Ops | Docroot `/home/s/shpigovsky/shpigovsky.ru/public_html`. P05 chartered WPilot dir replace is complete |
| Database | Identity/schema/content read | **SSH_LOCAL_MYSQL** | `secrets.local.md` → DATABASE + SSH | **YES — SELECT proven** | **NO** — **CLOSED** | **Current imported DB is live content authority** | SELECT-class charter. Mutation = separate charter | Full DB / Layer A | Restore Layer A only with explicit approval | FP-0002 Site Ops | Prefix `fp02_`. Preserve imported content |
| Beget panel | Hosting backup, PHP, SSL, account | Browser | `secrets.local.md` → BEGET CONTROL PANEL | Operator/manual | Operator/manual; **not agent-default** | **OPTIONAL / NOT FILLED** | Operator HITL | Existing full Beget backups must be preserved | Operator restore | Operator | Post-reimport Layer A **OPERATOR CONFIRMED** (FU01) |
| DNS | `shpigovsky.ru` cutover | Registrar / Beget DNS | Out of this contour | Inspection only if separately chartered | **FORBIDDEN** | **`DNS_CUTOVER = DEFERRED`** | Explicit cutover task | Pre-cutover snapshot of DNS records | Revert DNS records | Operator | |
| SMTP | Mail delivery | Plugin / Beget mail | Optional future fields | N/A | **NO** | **SAFE UNKNOWN** / protected | Separate charter | Layer A | Revert plugin/settings | Operator | |
| Cache | Page/object/OPcache | Plugin / nginx / Beget | N/A | Observe only | **NO** | **SAFE UNKNOWN** | Separate charter | N/A | Re-enable prior config | FP-0002 Site Ops | |

---

## Proven vs closed (PROD-P05-FU01)

| Surface | Read | Write |
|---------|------|-------|
| Public HTTP | **PROVEN** | n/a |
| WP Admin HTTP | **PROVEN** | **closed** (no unrelated saves) |
| WP Admin DB role | **PROVEN** Administrator | n/a |
| WPilot authenticated REST | **PROVEN** | **closed** (`write_enabled=false`) |
| Filesystem (WP docroot) | **PROVEN** | **CLOSED BY POLICY** |
| DB SELECT | **PROVEN** (`SSH_LOCAL_MYSQL`) | **CLOSED** |
| DNS | n/a | **forbidden / deferred** |

---

## Authorization summary

| Action | Status |
|--------|--------|
| Use filled local credentials | read-only except chartered WPilot Admin token/upgrade (done) |
| FTP/SSH authentication | **VERIFIED** |
| Actual WordPress root | **VERIFIED** |
| Post-reimport FS SHA baseline | **ESTABLISHED** (FU02) |
| DB SELECT | **VERIFIED** |
| Preserve imported content DB | **REQUIRED** |
| WPilot write | **FORBIDDEN** until a later charter |
| Commit / push | **FORBIDDEN this wave** |

---

*Access Matrix v1 · PROD-P05-FU01 PASS · no secrets.*

# WPilot Release Candidate — v0.3.0-RC3

**Classification:** Release candidate specification — UX-02 operator dashboard; no Sprint 3, no new endpoints.  
**Date:** 2026-06-19  
**Status:** RC3 package built — **live connection verification not executed** (DEV plugin removed by operator).  
**Plugin slug:** `metacode-wpilot`

---

## Version

| Field | Value |
|-------|-------|
| **Release label** | `v0.3.0-RC3` |
| **Plugin version** | `0.3.0` |
| **Schema version** | `0.2.0` |
| **Text domain** | `metacode-wpilot` |
| **REST namespace** | `wpilot/v1` |
| **Runtime maturity** | `proven_content_writes` |
| **Environment scope** | DEV only — human-supervised |

---

## RC3 Delta (vs RC1 / RC2)

| Area | Change |
|------|--------|
| **Admin menu** | Top-level **MetaCODE WPilot** (`dashicons-shield-alt`); legacy Settings alias retained |
| **Dashboard** | Compact operator Overview; detailed panels moved to tabs |
| **Tabs** | Overview · Runtime · Connection · Endpoints · Safety · Diagnostics |
| **Connection tracking** | Persistent `last_connection_*` options; safe auth metadata only |
| **Localization** | UX-02 strings; `ru_RU` PO/MO updated (111 msgids) |
| **MARS token standard** | Documented in `local-storage-policy.md`, README, `runtime-local.example` |

**Not in RC3 scope:** Sprint 3, new REST routes, schema version bump, deploy, live REST proof.

---

## Package

| Field | Value |
|-------|-------|
| **ZIP path** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc3.zip` |
| **Inventory** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc3.inventory.json` |
| **SHA-256** | `11feb7fa4f21ec96938caef7405d21add0dd12a8e01fc2eb025c8a179f93aef6` |
| **Size** | 53,971 bytes |
| **Root folder** | `metacode-wpilot/` |
| **File count** | **27** (26 source + compiled `.mo`) |

### New source file

- `includes/class-wpilot-connection-tracker.php`

---

## Connection Status Options

Stored inside `wpilot_options` (no separate secrets):

| Key | Values / purpose |
|-----|------------------|
| `last_connection_status` | `never` \| `success` \| `failed` |
| `last_connection_success_at` | UTC MySQL timestamp |
| `last_connection_failure_at` | UTC MySQL timestamp |
| `last_connection_failure_reason` | Safe codes: `AUTH_MISSING`, `AUTH_INVALID`, `TOKEN_REVOKED` |

**Never persisted:** token, headers, payloads, request bodies.

---

## MARS Token Standard (operator docs)

| Field | Value |
|-------|-------|
| Storage root | `C:\AI MARS\local\tokens\` |
| DEV token file | `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| Auth header | `X-WPilot-Token` |
| DEV site | `https://dev.gktriumph.ru` |

---

## Prior RC References

- [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md) — UX-01 baseline package
- [reports/wpilot-ux-02-report.md](reports/wpilot-ux-02-report.md) — UX-02 implementation report

---

## SAFE UNKNOWN

- Connection status UI and tracking logic are **not verified live** until operator installs RC3 on DEV.
- Clean ZIP install proof for RC3 is **not executed** in this task.
- Sprint 3 must **not** start on RC3 packaging alone.

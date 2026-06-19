# WPilot Runtime Inventory — v0.3.0

**Classification:** Evidence-backed runtime snapshot (no roadmap, no marketing).  
**Date:** 2026-06-19  
**Plugin version:** 0.3.0  
**Schema version:** 0.2.0  
**Environment scope:** DEV only — `https://dev.gktriumph.ru`  
**Evidence sources:** [wpilot-runtime-proof-sprint-report.md](wpilot-runtime-proof-sprint-report.md), [wpilot-runtime-prototype-sprint-1-report.md](wpilot-runtime-prototype-sprint-1-report.md), [wpilot-runtime-prototype-sprint-2-report.md](wpilot-runtime-prototype-sprint-2-report.md), [WPILOT-PROVEN-CAPABILITIES-v1.md](../WPILOT-PROVEN-CAPABILITIES-v1.md)

---

## Proven Runtime

Capabilities confirmed via formal plugin REST on DEV (not temporary PHP helpers):

| Capability | Mechanism | Evidence |
|------------|-----------|----------|
| `inspect` | Read REST endpoints (`site-info`, `pages`, `structure`, etc.) | v0.1 operational release; Runtime Proof Sprint baseline |
| `backup` | `POST /pages/{id}/backups` — `page.post_content` snapshot | Runtime Proof Sprint — 3/3 PASS |
| `rollback` | `POST /pages/{id}/rollback` — restore from plugin backup | Runtime Proof Sprint — checksum restore pages 954, 38, 69 |
| `validate` | Post-write / post-rollback checksum verification | Sprint 2 — `validation_result: passed` |
| `apply_content_change` | `POST /pages/{id}/scoped-replace` — exact-once `post_content` replace | Sprint 2 — 3/3 PASS on pages 954, 69, 38 |
| Audit trail | `wpilot_audit_log` DB table — lifecycle events per `operation_id` | All sprints — `backup_requested` → `backup_created` → `scoped_replace_verified` / `rollback_verified` |
| Checksum validation | `sha256:` pipeline on inspect, backup, apply, rollback | Shared `WPilot_Checksum`; verified in all sprint runs |
| Dry-run analysis | `POST /pages/{id}/replace-text/dry-run` — no mutation | v0.1 reports; Sprint 1 pre-apply analysis |
| WPBakery-safe recovery | Full `post_content` restore; shortcode integrity preserved | Runtime Proof Sprint page 38; Sprint 2 pages 38, 954 |

**Write scope limit:** proven write primitive = scoped exact-once replace on `page.post_content` only.

---

## Proven Endpoints

Namespace: `wpilot/v1` (full base: `/wp-json/wpilot/v1/`)

| Method | Route | Auth | Proven on DEV |
|--------|-------|------|---------------|
| GET | `/ping` | Public (no token) | Yes |
| GET | `/site-info` | Token + bridge | Yes |
| GET | `/themes` | Token + bridge | Yes |
| GET | `/plugins` | Token + bridge | Yes |
| GET | `/pages` | Token + bridge | Yes |
| GET | `/pages/{id}` | Token + bridge | Yes |
| GET | `/pages/{id}/structure` | Token + bridge | Yes |
| GET | `/indexing-state` | Token + bridge | Yes |
| POST | `/pages/{id}/replace-text/dry-run` | Token + bridge + DEV | Yes |
| POST | `/pages/{id}/backups` | Token + bridge + DEV + schema | Yes |
| POST | `/pages/{id}/rollback` | Token + bridge + DEV + write_enabled + schema | Yes |
| POST | `/pages/{id}/scoped-replace` | Token + bridge + DEV + write_enabled + schema | Yes |

**Total registered routes:** 12

---

## Proven Targets

Only targets with real DEV evidence:

| Target type | Example entity | Evidence |
|-------------|----------------|----------|
| **page** | page 69 (contacts), page 38 (cargo taxi), page 954 (Sprint 2) | Sprint backup/apply/rollback JSON; STORAGE mirrors |
| **shortcode** | `footer_contacts` (`post_id` 131) | Pre-sprint helper apply/backup JSON |
| **footer** | Site footer zone (menu + contacts) | Footer validation JSON; HTML audits |
| **css_fragment** | `dt-the7-child` footer menu CSS | CSS lesson; `audit-footer-result.json` |
| **environment** | `dev.gktriumph.ru` DEV bridge | Ping probes; sprint reports |
| **site** | Triumph DEV WordPress instance | Multi-page DEV work corpus |

**Count:** 6 proven targets

---

## Not Yet Proven

| Area | Status |
|------|--------|
| Menu write via plugin REST | Not proven — no endpoint |
| Widget write via plugin REST | Not proven — no endpoint |
| Footer dedicated endpoint | Not proven — zone ops remain MARS-combined path |
| CSS write via plugin REST | Not proven — FTP/MARS path only |
| `apply_shortcode_change` / `apply_footer_change` / `apply_css_change` via plugin | Not proven |
| Regex or mass replace | Not proven |
| Production environment | Not proven — DEV only |
| Multisite | Not proven |
| Autonomous execution | Not proven — human-supervised only |
| `restore_backup` as distinct operation_id | Not separately proven |
| Plugin configuration management | Not proven |
| ZIP deploy pipeline on DEV | Not proven — FTP upload was proven deploy path |

---

## Current Runtime Maturity

**Level:** `proven_content_writes`

**Basis:**

- Read path proven (v0.1 + sprint baseline)
- Backup + rollback proven (Runtime Proof Sprint, v0.2.0)
- Scoped replace execute proven (Sprint 2, v0.3.0)
- Post-write validation + audit trail + checksum pipeline proven across sprints
- Write scope limited to `page.post_content` exact-once replace

**Not claimed:** production-ready, autonomous, multi-target write, menu/widget/CSS plugin writes.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v0.3.0 inventory |
| Implements runtime | No — inventory record only |
| Replaces Proven Capabilities | No — condensed runtime view |

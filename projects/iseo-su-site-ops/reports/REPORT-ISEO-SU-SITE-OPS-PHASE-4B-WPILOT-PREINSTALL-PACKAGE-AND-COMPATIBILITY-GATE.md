# REPORT — ISEO-SU SITE OPS PHASE 4B WPILOT PREINSTALL PACKAGE AND COMPATIBILITY GATE

**Task ID:** ISEO-SU-SITE-OPS-PHASE-4B-WPILOT-PREINSTALL-PACKAGE-AND-COMPATIBILITY-GATE  
**Date:** 2026-07-24  
**Final status:** **PHASE 4B — COMPLETE / PRE-INSTALL CONDITIONAL GO**  
**Site:** `https://i-seo.su/` (no production access this task)

---

## 1. Execution Summary

Bounded static review of the canonical WPilot RC5 package and plugin source against Phase 2B i-seo.su architecture. Package is an **ACCEPTED MATCH** to Brain source. Pre-install decision: **CONDITIONAL GO**. No install, upload, activation, token, REST, Storage write, Localhost write, or Git mutation was performed.

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Drive / volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `04cd01d1881bccf6fc0dfeebef5b891e378fef37` (`04cd01d1`) |
| Upstream | `origin/mars/canonical-post-recovery` |
| Ahead / behind | **ahead 14, behind 61** (recorded; no pull/push) |
| Staged | empty |
| Foreign WIP | Present outside locus — **preserved** |

---

## 3. Authority Reviewed

WPilot: OPERATIONAL-INDEX, FINAL/AUTHORITY STATE RC5, lifecycle, maintenance, proven capabilities, RC5 release candidate, clean-install checklist/plan, local-storage-policy, runtime contracts, deploy manifests, FP-0002 reconciliation report.

i-seo.su: OPERATIONAL-INDEX, read-only audit, WP/remote inventories, boundary map, hybrid SoT, protected zones, preinstall inputs, Phase 2B REPORT.

---

## 4. Canonical Source and Version

| Item | Value |
|------|-------|
| Source | `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` |
| Main file | `metacode-wpilot.php` |
| Header / constant version | `0.3.0` |
| Schema | `0.2.0` |
| RC label | `v0.3.0-RC5` |
| Filename | `metacode-wpilot-v0.3.0-rc5.zip` |
| Version note | `0.3.0` vs `rc5` filename — documented, not normalized |

---

## 5. Package Audit

| Item | Result |
|------|--------|
| Canonical ZIP | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip` |
| SHA-256 | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| Size / files | 54863 bytes / 27 entries |
| Root | single `metacode-wpilot/` |
| Path safety | no `\`, no `..`, no absolute paths |
| Source↔ZIP | **27/27 identical** |
| Classification | **ACCEPTED MATCH** |
| Stale candidate | `metacode-wpilot-v0.3.0.zip` — **do not use** |
| ZIP created/modified | **No** |

---

## 6. Exact Route Inventory

Namespace: `wpilot/v1`

| Route | Method | Auth | Bridge | write_enabled | Mutation |
|-------|--------|------|--------|---------------|----------|
| `/ping` | GET | No | No | No | No |
| `/site-info` | GET | Yes | Yes | No | No |
| `/themes` | GET | Yes | Yes | No | No |
| `/plugins` | GET | Yes | Yes | No | No |
| `/pages` | GET | Yes | Yes | No | No |
| `/pages/{id}` | GET | Yes | Yes | No | No |
| `/pages/{id}/structure` | GET | Yes | Yes | No | No |
| `/indexing-state` | GET | Yes | Yes | No | No |
| `/pages/{id}/replace-text/dry-run` | POST | Yes | Yes | **Yes** | No (analysis) |
| `/pages/{id}/backups` | POST | Yes | Yes | No | DB backup insert |
| `/pages/{id}/rollback` | POST | Yes | Yes | **Yes** | Yes (content) |
| `/pages/{id}/scoped-replace` | POST | Yes | Yes | **Yes** | Yes (content) |

Full parameter/proven notes: `ISEO-SU-WPILOT-SOURCE-AND-ROUTE-AUDIT-v1.md`.

---

## 7. Capability Classification

A–O: implemented in source + included in package; proven on DEV (and local write lifecycle where documented); **PRODUCTION NOT PROVEN**.  
P–W (ACF, CPT, theme settings, menus/widgets, static FS, DB admin, media, cache purge): **NOT IMPLEMENTED**.

---

## 8. Safety Defaults

After activation (source): `bridge_enabled=false`, `write_enabled=false`, `dev_confirmed=false`, empty `token_hash`, `emergency_disabled=false`.  
Creates `{prefix}wpilot_backups` + `{prefix}wpilot_audit_log` and `wpilot_options`.  
Only public route: `/ping`.  
No cron / frontend hooks / external HTTP found.  
No `uninstall.php`.

---

## 9. Static Security Review

Bounded review only. Positives: hashed tokens, `wp_check_password`, defaults off, admin capability + nonce pattern, prepared SQL for plugin tables, no eval/unserialize/arbitrary FS found.  
Notes: REST `permission_callback` always true (auth in handlers); raw page content on read; incomplete Requires/Tested headers; PHP lint unavailable here.

---

## 10. i-seo.su Compatibility

WP 7.0.2: no static API blocker found; version contract incomplete.  
PHP runtime: SAFE UNKNOWN.  
Theme `iseoblog` / `page-home.php`: plugin-safe presence; content edits may not affect template-driven homepage.  
ACF/Yoast/Jetpack/WP-Optimize: coexistence expected; no ACF/cache APIs in WPilot.  
REST/`X-WPilot-Token`/Admin JS challenge: deferred to GATE 6D fail-closed.  
No staging / production-only: elevated operational risk, mitigated by separated gates + Beget backup.

---

## 11. Hybrid Protected Boundaries

WPilot must not mutate static HTML, shared css/js, calculator/tariff handlers, theme templates, ACF options, forms/mail, routing, or unresolved web-KP surfaces. MVP writes (later) = `page` `post_content` only. Protected zones updated accordingly.

---

## 12. Installation and Rollback Model

Separated gates: 4B-1 package · 4B-2 compatibility · 4B-3 backup · 6A install-only · 6B activation-only · 6C token-only · 6D negative auth + read-only smoke · 6E optional later write smoke.  
Rollback: deactivate or SFTP remove exact plugin folder; DB restore only if damage proven; Beget backup primary.

---

## 13. Token Storage Decision

Canonical policy path root: `X:\AI MARS\local\tokens\`.  
Proposed site file: `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token`.  
Status: **NOT CREATED**. No token in docs/REPORT.

---

## 14. Files Created or Updated

**Created**

- `ISEO-SU-WPILOT-PACKAGE-AUDIT-v1.md`
- `ISEO-SU-WPILOT-SOURCE-AND-ROUTE-AUDIT-v1.md`
- `ISEO-SU-WPILOT-CAPABILITY-MATRIX-v1.md`
- `ISEO-SU-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md`
- `ISEO-SU-WPILOT-INSTALLATION-AND-ROLLBACK-PLAN-v1.md`
- `ISEO-SU-WPILOT-TOKEN-STORAGE-DECISION-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-PHASE-4B-WPILOT-PREINSTALL-PACKAGE-AND-COMPATIBILITY-GATE.md`

**Updated**

- `ISEO-SU-WPILOT-PREINSTALL-INPUTS-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `OPERATIONAL-INDEX.md`

---

## 15. Validation

| Check | Result |
|-------|--------|
| No external production access | **PASS** |
| No WPilot source changes | **PASS** |
| No ZIP create/modify | **PASS** |
| Package hash read-only | **PASS** |
| PHP lint beyond syntax | N/A — PHP binary unavailable; no execution attempted |
| Writes only under `projects/iseo-su-site-ops/` | **PASS** |
| No secrets in docs | **PASS** |
| No local token file created | **PASS** |
| Storage/Localhost write | **PASS** (read-only package inspection only) |
| Registry / ATLAS / WPilot / Report Hub / infra unchanged | **PASS** |
| Staged diff empty | **PASS** (expected) |
| Foreign WIP preserved | **PASS** |

---

## 16. Risks

1. Operator uploads stale `v0.3.0.zip` instead of RC5.  
2. Hybrid misunderstanding → attempting marketing HTML changes via WPilot.  
3. Host blocks custom token header.  
4. Activation creates DB tables without fresh Beget backup.  
5. Premature write enablement on production-only site.  
6. Incomplete PHP/version plugin header contract.

---

## 17. SAFE UNKNOWN

PHP runtime; exact actives; header forwarding; Admin JS challenge vs REST; web-KP ownership; restore drill; agent-host PHP lint; uninstall residual cleanup.

---

## 18. Pre-install Decision

**CONDITIONAL GO**

Package exact and accepted; source defaults safe; no material static NO-GO defect. Installation must wait for operator package/compatibility acceptance and a **fresh** Beget backup (gates 4B-1..4B-3). Production write readiness is **out of scope** for this decision.

---

## 19. Required Operator Review

1. Accept package SHA-256 and forbid stale ZIP (`4B-1`).  
2. Accept hybrid boundaries + CONDITIONAL GO conditions (`4B-2`).  
3. Confirm fresh full Beget backup before any upload (`4B-3`).  
4. Authorize only **PHASE 6A INSTALL-ONLY** when ready — not activation.

---

## 20. Next Authorized Gate

**ISEO-SU-SITE-OPS — PHASE 6A WPILOT INSTALL-ONLY**

(If CONDITIONAL GO conditions cannot be met: **PHASE 4C WPILOT PREINSTALL REMEDIATION**.)

---

## 21. Stop Condition

- no production access  
- no SFTP/FTP  
- no WordPress Admin  
- no database  
- no browser  
- no plugin upload/install/activation  
- no token  
- no REST  
- no cache purge  
- no Storage mutation  
- no Localhost mutation  
- no ATLAS or registry mutation  
- no Git stage/commit/push  

**Waiting for operator review.**

---

*REPORT Phase 4B · 2026-07-24 · CONDITIONAL GO · stop.*

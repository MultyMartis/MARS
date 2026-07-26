# METALLKA SITE OPS — Current Baseline v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** ACCEPTED (Phase 1.5 consolidated baseline) — **HISTORICAL SNAPSHOT**  
**Date:** 2026-07-25  
**Site:** `metallka.ru`  
**Production connection (this snapshot):** **NOT CONNECTED**

> **CURRENT-STATE SUPERSESSION (Phase 4C-P1 / 2026-07-27):** This file remains the Phase 1.5 documentary consolidation and is **not** rewritten to erase history. For **live** programme state use [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) and [METALLKA-WPILOT-CONNECTION-STATE-v1.md](METALLKA-WPILOT-CONNECTION-STATE-v1.md). Live facts as of 4C-R1: WPilot **0.3.0-RC6** installed/active; i-seo code parity **CONFIRMED** (FIX01); `dev_confirmed=true` · `bridge_enabled=true` · `write_enabled=false`; authenticated protected reads **PROVEN**; public ping ≠ auth proof; token local-only; WPilot writes **BLOCKED**; CHANGE 0001 **COMPLETE / production validated**; production source authority remains **provisional** under established ownership rules.

---

## 1. Programme baseline

| Field | Value |
|-------|-------|
| **Programme** | METALLKA-RU-SITE-OPS |
| **Purpose** | Existing WordPress Site Operations + controlled WPilot onboarding |
| **Current phase** | PHASE 1.5 — documentation / project setup |
| **Lifecycle** | ACTIVE — DOCUMENTATION ONLY |
| **Canonical locus** | `X:\AI MARS\projects\metallka-ru-site-ops\` |
| **Completed prior** | PHASE 0 PREFLIGHT; Cross-chat Knowledge Intake (operator/session — documentary) |

---

## 2. WPilot programme baseline (global — not metallka install)

| Field | Value |
|-------|-------|
| **Programme state** | **ACTIVE** Reference Implementation |
| **Proven DEV reference** | **0.3.0-RC5** |
| **Current deployment baseline** | **0.3.0-RC6** |
| **WordPress Plugin Version** | **0.3.0** |
| **Schema** | **0.2.0** |
| **Canonical source** | `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` |
| **Reusable package** | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| **Accepted SHA-256** | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| **Relevant source remediation commit** | `27dfe624eec8b10b73e34c4a5f6df323258ecd1b` |

**Re-verification (2026-07-25):** package present on Storage; recomputed SHA-256 matches accepted value (case-insensitive). Source tree path present. Remediation commit resolves locally.

### 2.1 Production maturity (i-seo.su precedent — not metallka)

**Production-proven on i-seo.su:**

- Install  
- Activation  
- RC5 → RC6 update  
- Safe defaults  
- Production token generation (local-only)

**NOT production-proven (even on i-seo):**

- REST auth  
- Ping  
- Read routes  
- Backup endpoint  
- Dry-run  
- Scoped replace  
- Rollback  
- Production writes  

DEV REST/write proof remains on `dev.gktriumph.ru` (RC5) — **does not** transfer to metallka production.

### 2.2 Safe activation defaults (RC6)

| Flag | Required default |
|------|------------------|
| `bridge_enabled` | `false` |
| `write_enabled` | `false` |
| `dev_confirmed` | `false` |

**Token creation** must work **independently** of `bridge_enabled` and `dev_confirmed` on RC6 (`can_manage_token` remediation).

### 2.3 Metallka WPilot status

| Field | Value |
|-------|-------|
| **Installed on metallka** | **NOT VERIFIED / NOT CLAIMED** |
| **Token** | **NONE** |
| **Bridge** | **N/A (not connected)** |

---

## 3. Precedent model (summary)

| Precedent | Role | Transfer ban |
|-----------|------|--------------|
| **i-seo.su** | Production onboarding / security | Do not copy site facts as metallka facts |
| **dev.gktriumph.ru** | The7 / WPBakery technical DEV | Do not transfer IDs, options, paths, tokens, shortcodes, structure |
| **FP-0002 / Forge** | Source/runtime/admin methodology | Do not transfer theme/ACF/CPT architecture |

None is a 1:1 blueprint. Detail: [METALLKA-SITE-OPS-CHARTER-v1.md](METALLKA-SITE-OPS-CHARTER-v1.md) §4.

---

## 4. ATLAS state

| Field | Value |
|-------|-------|
| **Binding** | **PARTIAL / INCOMPLETE** |
| **Known** | `PER-0003` |
| **Organization** | **NOT FOUND** |
| **Website** | **NOT FOUND** |
| **Domain** | **NOT FOUND** |

Person attestation does **not** imply ownership or legal binding to `metallka.ru`.

---

## 5. Source / runtime policy

Until source authority is discovered:

- Production runtime = **provisional authority** for existing files/content.

Later filesystem work (chartered only): fetch → hash → before-copy → compare → resolve authority → exact-file modify → exact-file deploy → fetch-back → hash verify → QA.

Admin-first for UI-owned content/settings; filesystem-first only for code-owned surfaces. **No** broad sync.

---

## 6. Local mirror

| Field | Value |
|-------|-------|
| **Decision** | **DEFER** |
| **Profile** | Not created |

Remote-only may later cover simple content / menu / small builder / WPilot onboarding. Local mirror strongly recommended for PHP, child-theme architecture, large JS, plugin work, major WPBakery/section work, refactor, schema.

---

## 7. First future safe task (policy only)

- Normal first task: small text in one non-global `vc_column_text` on one low-risk WPBakery page.  
- First WPilot write smoke: draft/private test page; exact-once plain `post_content` marker; never `vc_raw_html` first.

**Not executed in Phase 1.5.**

---

## 8. Explicit Phase 1.5 negatives

No production access · no credentials · no WPilot install · no token · no bridge · no smoke · no writes · no local mirror · no ATLAS mint · no registry mutation · no WPilot source/package change.

---

*Baseline v1 · verified documentary consolidation · 2026-07-25.*

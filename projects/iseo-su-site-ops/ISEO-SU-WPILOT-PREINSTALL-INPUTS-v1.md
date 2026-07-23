# ISEO-SU WPILOT PREINSTALL INPUTS v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B (created) · **PHASE 4B (updated)**  
**Date:** 2026-07-24  
**Status:** INPUTS + **PHASE 4B PACKAGE/COMPATIBILITY REVIEW COMPLETE** — **NOT an install approval**

WPilot Plugin must **not** be installed or activated from this document.

---

## 1. Compatibility inputs (factual)

| Input | Value | Confidence |
|-------|-------|------------|
| WordPress version | **7.0.2** | High (core file + generator) |
| PHP runtime version | **SAFE UNKNOWN** | — |
| PHP minimum (core/plugins) | **≥ 7.4** (WP core; ACF/Yoast headers also 7.4) | High for floor |
| Active theme | `iseoblog` (custom; sole theme; not child) | High |
| Builder | No WPBakery/The7 found | High |
| REST API public | `/wp-json/` reachable | High |
| Security / cache plugins present on disk | Jetpack, WP-Optimize, Akismet | High presence / medium activity |
| Yoast | Present + REST namespace | High |
| ACF PRO | Present on disk 6.3.10 | High presence / activity SAFE UNKNOWN |
| Custom header / bot challenge | Non-browser Admin HTTP hits JS challenge shell | High |
| Custom theme hardcodes full HTML templates | `page-home.php` etc. | High — WPilot content edits may not cover marketing HTML |
| Existing WPilot | **Absent** | High |
| Staging | **Absent** | High (Wave A) |
| Multisite | No | High |
| MU-plugins | None listed | High |
| Canonical WPilot package | `metacode-wpilot-v0.3.0-rc5.zip` | High (Phase 4B) |
| Package SHA-256 | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` | High (recomputed) |
| Package vs Brain source | **ACCEPTED MATCH** (27/27) | High |
| Pre-install decision | **CONDITIONAL GO** | Phase 4B |

---

## 2. Safe test page possibility

| Option | Notes |
|--------|-------|
| New draft WP page | Possible in principle via Admin HITL — **not created** in Phase 2B/4B |
| Existing low-risk WP page | `/offers` or unused draft — needs operator pick |
| Static HTML test file | Would be SFTP write — **not authorized** now |
| Recommendation | Prefer a dedicated unpublished WP page created by operator before any WPilot write smoke (GATE 6E later) |

---

## 3. Backup model

| Item | State |
|------|-------|
| Operator policy | Full Beget backup before production work sessions |
| Phase 2B audit | Backup **CONFIRMED BY OPERATOR** for 2026-07-24 audit session |
| Before GATE 6A | **Fresh** full Beget backup required again (`GATE 4B-3`) |
| Plugin-level backup alone | **Insufficient** vs full hosting backup |
| Rollback proof | Still SAFE UNKNOWN (restore drill not executed) |

---

## 4. Custom header / REST risks

1. Admin UI JS challenge may also affect some authenticated REST clients — validate in **GATE 6D**.  
2. Jetpack / security features may rate-limit or challenge automation.  
3. Large portions of the marketing site are **not** WP content — WPilot cannot be the only channel for hybrid ops.  
4. `WP_DEBUG` true may increase log noise during tests.  
5. `X-WPilot-Token` forwarding remains SAFE UNKNOWN until 6D.

---

## 5. Phase 4B package / source summary

| Item | Result |
|------|--------|
| Canonical source | `projects/wpilot/plugin/metacode-wpilot/` |
| Canonical package | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip` |
| Stale ZIP to avoid | `metacode-wpilot-v0.3.0.zip` |
| Activation defaults | bridge off, write off, no token; creates plugin DB tables |
| Public route | `GET /wpilot/v1/ping` only |
| Mutation surface | page `post_content` only (when later write-enabled) |
| Artifacts | Package / source-route / capability / compatibility / install-rollback / token-storage audits |

---

## 6. Unresolved compatibility items (carry-forward)

- Exact PHP version  
- Exact active plugin set  
- Whether host forwards `X-WPilot-Token`  
- Interaction with WP-Optimize cache on future smokes  
- Mapping which WP pages are safe smoke targets vs template-driven shells  

---

## 7. Explicit non-decisions

- **Do not install WPilot** until GATE 6A authorized  
- **Do not activate WPilot** until GATE 6B authorized  
- **Do not create tokens** until GATE 6C authorized  
- **Do not run WPilot REST** until GATE 6D authorized  
- **Do not enable writes** until a later optional GATE 6E charter  

Next gate after operator acceptance of CONDITIONAL GO conditions: **PHASE 6A WPILOT INSTALL-ONLY** (or **PHASE 4C** if remediation required).

---

*WPilot preinstall inputs v1 · updated Phase 4B 2026-07-24 · no install approval.*

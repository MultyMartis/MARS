# ISEO-SU WPILOT PREINSTALL INPUTS v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B (created) · PHASE 4B (updated) · PHASE 6A–6C-R (updated) · **PHASE 6C RETRY (token local-only)**  
**Date:** 2026-07-24  
**Status:** INPUTS + Phase 4B CONDITIONAL GO + Phase 6A–6B COMPLETE + Phase 6C RC5 **BLOCKED** (historical) + Phase 4C RC6 packaged + Phase 6C-R **RC6 ACTIVE SAFE DEFAULTS** + Phase 6C RETRY **TOKEN CREATED LOCAL-ONLY** — bridge / writes / `dev_confirmed` remain **off**; WPilot REST smoke **not** run

WPilot is active on production at RC6 with safe defaults and a local-only token. Bridge enablement, writes, and REST smoke remain forbidden until later gates. Evidence: `ISEO-SU-WPILOT-INSTALL-ONLY-EVIDENCE-v1.md`, `ISEO-SU-WPILOT-ACTIVATION-ONLY-EVIDENCE-v1.md`, `ISEO-SU-WPILOT-RC6-UPDATE-EVIDENCE-v1.md`, `ISEO-SU-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md`.

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
| Existing WPilot | **Installed and active** (RC6; safe defaults; token local-only) | High |
| Staging | **Absent** | High (Wave A) |
| Multisite | No | High |
| MU-plugins | None listed | High |
| Current production package | `metacode-wpilot-v0.3.0-rc6.zip` | High (Phase 6C-R) |
| Current package SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` | High |
| WP Version header | **0.3.0** (distinct from release label **0.3.0-RC6**) | High |
| RC5 rollback ZIP (retained) | `metacode-wpilot-v0.3.0-rc5.zip` · `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` | High (Phase 4B / 6A) |
| Package vs Brain source | **ACCEPTED MATCH** (27/27 RC6 live) | High |
| Pre-install decision | **CONDITIONAL GO** (historical 4B; install executed) | Phase 4B |

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
| Phase 6A session | Operator attested via `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 4B-3` |
| Phase 6B session | Operator attested via `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6B` |
| Phase 6C / 6C-R / 6C RETRY sessions | Operator-attested fresh Beget backup strings per gate (panel object/timestamp residual SAFE UNKNOWN) |
| Plugin-level backup alone | **Insufficient** vs full hosting backup |
| Rollback proof | Still SAFE UNKNOWN (restore drill not executed); RC5 sibling dir `.mars-rollback-metacode-wpilot-rc5-phase6c-r/` retained; Admin deactivate + exact-folder rollback paths ready |

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
| Canonical package (current) | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| RC5 package (rollback retained) | `…\metacode-wpilot-v0.3.0-rc5.zip` |
| Stale ZIP to avoid | `metacode-wpilot-v0.3.0.zip` |
| Production safe defaults (current) | bridge off, write off, `dev_confirmed` off; token **present local-only** |
| Public route | `GET /wpilot/v1/ping` only (not invoked) |
| Mutation surface | page `post_content` only (when later write-enabled) |
| Artifacts | Package / source-route / capability / compatibility / install-rollback / token-storage / phase evidence audits |

---

## 6. Unresolved compatibility items (carry-forward)

- Exact PHP version  
- Exact active plugin set  
- Whether host forwards `X-WPilot-Token`  
- Interaction with WP-Optimize cache on future smokes  
- Mapping which WP pages are safe smoke targets vs template-driven shells  

---

## 7. Explicit non-decisions / completed gates

- **GATE 6A install-only** — **DONE** (RC5 inactive filesystem install; 27/27)  
- **GATE 6B activation-only** — **DONE** (active; bridge/writes/`dev_confirmed` off; no token yet)  
- **GATE 6C token-creation-only (RC5)** — **BLOCKED / NO TOKEN** (historical; `is_operationally_ready` required DEV+bridge)  
- **Phase 4C** — **DONE** (RC6 package ready; production unchanged in that task)  
- **GATE 6C-R remediation update-only** — **DONE** (RC5→RC6; 27/27; rollback dir retained)  
- **GATE 6C RETRY token-creation-only** — **DONE** (token created; local-only file; bridge/writes/`dev_confirmed` still off; no REST)  
- **Do not rotate / revoke token** without a separate charter  
- **Do not enable bridge / writes** until later gates  
- **Do not run WPilot REST smoke** until GATE 6D authorized  
- **Do not run controlled write smoke** until GATE 6E authorized  
- **Do not open phpMyAdmin / DB** without separate charter  

Next gate: **PHASE 6D WPILOT BRIDGE ENABLEMENT AND NEGATIVE-AUTH / READ-ONLY SMOKE** (separate operator approval + fresh Beget backup required; writes/`dev_confirmed` remain disabled unless separately proven and approved).

---

*WPilot preinstall inputs v1 · updated Phase 6C RETRY 2026-07-24 · RC6 ACTIVE SAFE DEFAULTS; TOKEN CREATED LOCAL-ONLY; bridge/writes/DEV off; REST smoke NOT AUTHORIZED.*

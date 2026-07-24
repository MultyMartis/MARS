# REPORT — WPILOT PRODUCTION TOKEN GATING REMEDIATION

**Task ID:** WPILOT-PHASE-4C-PRODUCTION-TOKEN-GATING-REMEDIATION  
**Date:** 2026-07-24  
**Classification:** M1 maintenance fix (token-generation gate) under explicit remediation charter  
**Decision:** **REMEDIATION COMPLETE / PACKAGE READY**

---

## 1. Execution Summary

Phase 6C on `i-seo.su` failed because token generation was incorrectly gated by `WPilot_Environment::is_operationally_ready()`, which requires `dev_confirmed` and `bridge_enabled`. That made the approved production sequence (token before bridge) structurally impossible without a false DEV/test assertion or temporary bridge enablement.

Source remediation introduces `can_manage_token()` for admin token generate/rotate, keeps REST operational readiness and write gates unchanged, fixes token persistence to partial option updates (stale-snapshot class), adds bounded unit/static tests, and packages **v0.3.0-RC6** without overwriting RC5. **No production access, no token creation, no deployment.**

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Drive / volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `5ea609fe064da91ccc0dc3da8501df41fb2d2b8e` (`5ea609fe`) |
| Upstream | `origin/mars/canonical-post-recovery` |
| Ahead / behind | ahead **17** / behind **62** (no pull/push) |
| Staged | empty (unchanged) |
| Foreign WIP | Present outside and inside adjacent programmes — **preserved** |
| WPilot plugin source collision | **None** (plugin tree clean before edit) |
| Production access | **None** |

---

## 3. Incident and Root Cause

| Item | Detail |
|------|--------|
| Site | `https://i-seo.su/` (production) |
| Installed package | RC5 / header `0.3.0` |
| Observed refusal | Token generation requires bridge enabled and DEV/test confirmation |
| Evidence | `projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-PHASE-6C-WPILOT-TOKEN-CREATION-ONLY.md` |
| Root cause | `admin/class-wpilot-admin-page.php` `case 'generate_token'` called `is_operationally_ready()` |

**Classification:** **DESIGN DEFECT** + **IMPLEMENTATION DEFECT** + **DOCUMENTATION DEFECT**

- Design: token creation readiness was conflated with REST operational readiness.
- Implementation: admin handler reused the wrong gate.
- Documentation: admin copy and older MVP docs taught “DEV+bridge before token”.

---

## 4. Existing Gating Model

| Concern | Gate (RC5) |
|---------|------------|
| Token generation | `is_operationally_ready()` → `dev_confirmed` + `bridge_enabled` + not emergency |
| REST protected reads | `operational_readiness()` → same + token auth |
| Writes / dry-run | `operational_readiness()` + `write_enabled` |
| Admin capability | `manage_options` + nonce on POST |
| Activation defaults | bridge/write/dev false; no token |

`dev_confirmed` remains a literal **DEV/test** assertion (UI label unchanged). It is **not** reinterpreted as generic production operator confirmation.

---

## 5. Corrected Gating Model

### TOKEN CREATION READINESS (`can_manage_token`)

- plugin active;
- `current_user_can( manage_options )`;
- valid admin nonce (handler);
- not `emergency_disabled`;
- **no** `dev_confirmed`;
- **no** `bridge_enabled`;
- **no** `write_enabled`.

### REST OPERATIONAL READINESS (unchanged)

- valid token;
- `bridge_enabled`;
- `dev_confirmed` (current REST contract — still DEV confirmation semantics);
- not emergency;
- endpoint capability checks.

### WRITE READINESS (unchanged)

- REST operational readiness;
- `write_enabled`;
- mutation/backup/validation gates.

Token generation must not enable bridge/writes/dev, must not call external endpoints, must not log plaintext, must show plaintext once in admin, and must not overwrite connection metadata via a stale full options snapshot.

---

## 6. Source Changes

| File | Change |
|------|--------|
| `includes/class-wpilot-environment.php` | Add `can_manage_token()`; keep `is_operationally_ready()` / `operational_readiness()` |
| `admin/class-wpilot-admin-page.php` | `generate_token` uses `can_manage_token()`; update Safety copy |
| `includes/class-wpilot-settings.php` | `generate_token` / `revoke_token` partial `update_options` |
| `includes/class-wpilot-constants.php` | `RELEASE_CANDIDATE=RC6`, `RELEASE_LABEL=0.3.0-RC6`; `VERSION` stays `0.3.0` |
| `admin/class-wpilot-admin-ui-model.php` | Expose `release_label` in runtime dashboard |
| `languages/*` | Updated strings for new admin copy |

REST auth (`class-wpilot-auth.php`) **not** weakened.

---

## 7. Security Boundary Verification

| Boundary | Status |
|----------|--------|
| Activation alone enables bridge | **No** |
| Token generation enables bridge | **No** |
| Token generation enables writes | **No** |
| Token generation sets `dev_confirmed` | **No** |
| REST protected ops while bridge off | **Still blocked** (`operational_readiness`) |
| Writes while `write_enabled` false | **Still blocked** |
| Production false DEV assertion required for token | **Removed** |
| Plaintext token in options / logs | **Not stored**; hash only |
| External request on token create | **None** |
| Stale options overwrite on token create | **Mitigated** (partial update) |

---

## 8. Tests

Harness: `projects/wpilot/tests/token-gating-remediation/`

| Runner | Result |
|--------|--------|
| `php -l` on changed PHP | **PASS** |
| `run-token-gating-tests.php` | **27 PASS / 0 FAIL** |

Coverage includes: token create with flags false; flags unchanged; unauthorized user; nonce/source contract; REST blocked with token hash while bridge off; write gate preserved; no plaintext persist; no external calls; rotation; activation defaults; connection metadata preservation; RC6 label.

**Not claimed:** WordPress Localhost runtime proof; production proof.

PHP used: `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` (CLI lint/tests only).

---

## 9. Version Decision

| Field | Value |
|-------|-------|
| Prior accepted package | `v0.3.0-RC5` |
| New release label | **`v0.3.0-RC6`** |
| WordPress plugin `Version` | **`0.3.0`** (unchanged — matches RC1–RC5 policy) |
| Schema | `0.2.0` (unchanged) |
| Distinguisher vs installed RC5 | Package filename + SHA-256 + `RELEASE_LABEL` in admin runtime model |
| RC5 historical evidence | **Not rewritten** |

---

## 10. Package

| Field | Value |
|-------|--------|
| ZIP | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| Inventory | `...\metacode-wpilot-v0.3.0-rc6.inventory.json` |
| Build helper | `...\build-rc6-package.py` |
| SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Size | 55,771 bytes |
| File count | **27** |
| Root folder | `metacode-wpilot/` |
| Forward-slash paths | **PASS** |
| RC5 overwritten | **No** (RC5 remains; size 54,863; prior hash preserved) |
| Source↔ZIP match | **PASS** (inventory) |
| Secrets scan | **PASS** |

---

## 11. Compatibility

Compatible with RC5 option schema and REST surface. Update is plugin-package replacement only. Existing sites keep safe defaults until operators change toggles. REST still requires `dev_confirmed` under current contract — **future** production environment confirmation model is **out of scope** for this patch (proposed separately if needed).

---

## 12. Files Changed

### Repository (Brain)

- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-environment.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-settings.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-constants.php`
- `projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-page.php`
- `projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-ui-model.php`
- `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot.pot`
- `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot-ru_RU.po`
- `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot-ru_RU.mo`
- `projects/wpilot/tests/token-gating-remediation/*`
- `projects/wpilot/reports/REPORT-WPILOT-PRODUCTION-TOKEN-GATING-REMEDIATION.md` (this file)
- `projects/wpilot/WPILOT-RELEASE-CANDIDATE-v0.3.0-RC6.md`
- `projects/wpilot/OPERATIONAL-INDEX.md` (pointer)
- related checklist / contracts / proven-capabilities notes as applicable
- `projects/iseo-su-site-ops/*` remediation docs (separate report)

### Storage (outside git)

- `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip`
- `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.inventory.json`
- `X:\AI MARS STORAGE\wpilot\deploy-packages\build-rc6-package.py`

---

## 13. Git and Foreign WIP

| Item | Status |
|------|--------|
| Stage / commit / push | **Not performed** |
| Staged index | empty |
| Foreign WIP | Preserved (including prior iseo Phase 6 working-tree updates) |
| Recommended next | Separate persistence checkpoint for allowlisted remediation paths only |

---

## 14. Risks

| Risk | Notes |
|------|-------|
| Operators confuse RC5 vs RC6 ZIP | Mitigate via SHA-256 gate |
| REST still requires `dev_confirmed` after bridge enable | Intentional; not fixed here — production bridge enable charter must address DEV semantics separately |
| Admin UI still labels DEV/test checkbox | Intentional — not silently reinterpreted |
| `.mo` rebuilt during package | Expected |

---

## 15. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Production behavior after RC6 update | **UNKNOWN** until Phase 6C-R |
| Whether production will ever set `dev_confirmed` for REST | **UNKNOWN** — needs future environment model / charter |
| Object-cache edge cases on `update_option` merge | **UNKNOWN** (same class as BUGFIX-02 residual) |

---

## 16. Production Deployment State

**Unchanged.** i-seo.su remains RC5 active; bridge off; writes off; `dev_confirmed` off; no token; no REST. Remediation package **not deployed** in this task.

---

## 17. Next Gate

**ISEO-SU-SITE-OPS — PHASE 6C-R WPILOT REMEDIATION UPDATE-ONLY**

Then, after update acceptance: **PHASE 6C TOKEN CREATION-ONLY RETRY**.

---

## 18. Stop Condition

Production unchanged; no token; bridge disabled; writes disabled; no REST; remediation source/package only; no deployment; wait for operator review.

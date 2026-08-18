# ISEO-SU WPILOT RC6 UPDATE EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-PHASE-6C-R-WPILOT-REMEDIATION-UPDATE-ONLY  
**Date:** 2026-07-24  
**Site:** `https://i-seo.su/`  
**Decision:** **PHASE 6C-R — COMPLETE / WPILOT RC6 ACTIVE SAFE DEFAULTS**

No secrets, credentials, cookies, nonces, plaintext tokens, or secret-bearing connection details are recorded here.

---

## 1. Update Status

| Field | Value |
|-------|-------|
| Status | **COMPLETE / WPILOT RC6 ACTIVE SAFE DEFAULTS** |
| Method | SFTP in-place overwrite of changed files only (8 of 27) |
| Active plugin path | `wp-content/plugins/metacode-wpilot/` |
| Final inventory | **27 / 27** files |
| Final package class | **RC6 exact match** (full remote hash inventory) |
| WordPress Version header | **0.3.0** (unchanged by design) |
| Package label | **0.3.0-RC6** |
| Plugin left active | **YES** |
| Token generated | **NO** |
| WPilot REST called | **NO** |

---

## 2. Operator Approval

| Gate | Exact session line | Status |
|------|--------------------|--------|
| Remediation update 6C-R | `APPROVE ISEO-SU WPILOT REMEDIATION UPDATE 6C-R` | **Present** (operator follow-up) |
| Task charter | `ISEO-SU-SITE-OPS-PHASE-6C-R-WPILOT-REMEDIATION-UPDATE-ONLY` | Executed |

Earlier blocked attempt in the same programme day lacked these lines and did not mutate production.

---

## 3. Fresh Beget Backup Confirmation

| Field | Value |
|-------|-------|
| Required string | `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6C-R` |
| Status | **Present** (operator follow-up; operator-attested for this 6C-R session) |
| Prior-phase backup reuse | **Not used** |
| Beget panel login by agent | **Not performed** |
| Independent panel timestamp | SAFE UNKNOWN residual |

---

## 4. RC5 Production Baseline

| Check | Result |
|-------|--------|
| Plugin directory present | **YES** |
| File count | **27** |
| Classification vs accepted RC5 ZIP | **RC5 EXACT MATCH** (0 hash mismatches) |
| Ghost / duplicate WPilot folders | **None** (before rollback capture) |
| Plugin active | **YES** |
| Bridge | **DISABLED** (`Мост выключено` / `Мост включён выключено`) |
| Writes | **DISABLED** (`Готовность к записи выключено`) |
| `dev_confirmed` | **DISABLED** (`Подтверждение DEV не подтверждено`) |
| Token | **NOT CREATED** (`Статус токена не сгенерирован` / `Токен создан (UTC) —`) |
| Frontend baseline (5 URLs) | **5/5 gross OK** before mutation |

---

## 5. RC6 Package Verification

| Field | Value |
|-------|--------|
| ZIP | `metacode-wpilot-v0.3.0-rc6.zip` |
| Storage class | `X:\AI MARS STORAGE\wpilot\deploy-packages\` |
| Required SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Recomputed SHA-256 | **Exact match** |
| File count / root | 27 / `metacode-wpilot/` only |
| Main file | `metacode-wpilot/metacode-wpilot.php` |
| Traversal / absolute / secrets debris | **None** |
| Persistence commit | `27dfe624eec8b10b73e34c4a5f6df323258ecd1b` (ancestor of session HEAD) |
| RC5 rollback ZIP SHA-256 | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` (**exact**; ZIP not mutated) |

RC5→RC6 changed files (8):

1. `metacode-wpilot/admin/class-wpilot-admin-page.php`
2. `metacode-wpilot/admin/class-wpilot-admin-ui-model.php`
3. `metacode-wpilot/includes/class-wpilot-constants.php`
4. `metacode-wpilot/includes/class-wpilot-environment.php`
5. `metacode-wpilot/includes/class-wpilot-settings.php`
6. `metacode-wpilot/languages/metacode-wpilot-ru_RU.mo`
7. `metacode-wpilot/languages/metacode-wpilot-ru_RU.po`
8. `metacode-wpilot/languages/metacode-wpilot.pot`

---

## 6. Rollback Capture

| Field | Value |
|-------|--------|
| Directory name | `.mars-rollback-metacode-wpilot-rc5-phase6c-r` |
| Location class | sibling under `wp-content/plugins/` (dot-prefixed) |
| Files copied | **27** |
| Hash match vs pre-update plugin | **YES** (exact RC5) |
| Listed as WordPress plugin | **NO** (Plugins screen check) |
| Cleanup | **RETAINED** pending operator review |
| Rollback used this phase | **NO** |

---

## 7. Update Method

| Field | Value |
|-------|--------|
| Transport | **SFTP only** |
| WordPress ZIP uploader | **Not used** (Version header remains 0.3.0) |
| Strategy | Overwrite only the 8 changed remediation files; keep plugin directory in place |
| Broad sync / delete flags | **Not used** |
| Options / settings writes | **None** |
| Ownership/permission changes | **None intentional** |

Note: primary runner completed upload then crashed on a `status is None` guard before post-verify; live SFTP probe confirmed full RC6 match and exact RC5 rollback; post-verify completed in a bounded completion helper without further upload.

---

## 8. Files Replaced

Exactly the eight RC5→RC6 changed paths listed in §5. Final remote inventory remains 27 files matching RC6.

---

## 9. RC6 Source Verification

| Marker | Remote result |
|--------|---------------|
| `WPilot_Environment::can_manage_token()` present | **YES** |
| `generate_token` handler uses `can_manage_token()` | **YES** |
| `generate_token` handler avoids `is_operationally_ready()` | **YES** |
| Full 27-file hash match vs RC6 ZIP | **YES** |
| Token generated to prove gate | **NOT DONE** (forbidden) |

---

## 10. Plugin State

| Field | Value |
|-------|--------|
| MetaCODE WPilot | **ACTIVE** |
| Other plugins active set | **Unchanged** (post-check vs pre-check) |
| Settings forms saved | **NO** |
| Admin fatal | **NO** |

---

## 11. Safe Defaults

| Control | Post-update |
|---------|-------------|
| Bridge | **DISABLED** |
| Writes | **DISABLED** |
| `dev_confirmed` | **DISABLED** |

---

## 12. Token State

| Field | Value |
|-------|--------|
| WordPress token | **NOT CREATED** |
| Local canonical `wpilot-prod-iseo-su.token` | **Absent** |
| Token generation clicked | **NO** |

---

## 13. REST Boundary

| Action | Status |
|--------|--------|
| `/wp-json/wpilot/v1/ping` | **NOT CALLED** |
| Any WPilot REST route | **NOT CALLED** |
| Auth / read-only WPilot smoke | **NOT RUN** |
| Passive `/wp-json/` index crawl | **NOT DONE** |

---

## 14. Frontend Regression

| URL | HTTP | Gross OK | Fatal / maintenance / visible WPilot |
|-----|------|----------|--------------------------------------|
| `/` | 200 | YES | NO |
| `/blog/` | 200 | YES | NO |
| `/services.html` | 200 | YES | NO |
| `/tariff-calc` | 200 | YES | NO |
| `/contacts.html` | 200 | YES | NO |

**5/5** expected success after update.

---

## 15. Admin Regression

| Check | Result |
|-------|--------|
| Login (MARS account) | **OK** |
| Plugins screen | **OK** |
| WPilot settings page (read-only) | **OK** |
| Rollback dir as second plugin | **NO** |

---

## 16. Remote Scope

Expected mutation only:

- `wp-content/plugins/metacode-wpilot/**` (8 files overwritten)
- `wp-content/plugins/.mars-rollback-metacode-wpilot-rc5-phase6c-r/**` (new rollback evidence)

No authorized changes to themes, other plugins, static HTML, calculators, forms, `.htaccess`, or `wp-config.php`.

---

## 17. Rollback Readiness

| Route | Status |
|-------|--------|
| Captured RC5 sibling directory | **READY / RETAINED** |
| Accepted RC5 ZIP (alternate) | Integrity OK locally; not needed |
| Full Beget restore | Not used |

---

## 18. Deviations

1. Initial session attempt blocked on missing approval/backup lines (no production mutation).
2. First bridge inference used a false-positive regex against UI label text «Мост включён»; fixed before mutation.
3. Primary update runner uploaded RC6 successfully then crashed before writing final result; completion helper verified live RC6 + Admin/frontend without re-upload.

---

## 19. SAFE UNKNOWN

- Independent Beget panel backup timestamp (operator-attested only)
- Exact remote filesystem ownership/ACL bytes beyond successful read/write
- Whether host PHP opcode cache retained any pre-update bytecode transiently (behavioral Admin UI matched RC6-safe defaults)

---

## 20. Stop Condition

**PHASE 6C-R COMPLETE.** Production runs RC6 with safe defaults. Token creation, REST smoke, bridge enablement, and write smoke remain **NOT AUTHORIZED**. RC5 rollback directory retained pending operator review. Next gate requires a **separate** charter: Phase 6C token creation-only retry.

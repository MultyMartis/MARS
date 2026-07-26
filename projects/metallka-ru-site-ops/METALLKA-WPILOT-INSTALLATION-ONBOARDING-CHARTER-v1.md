# METALLKA — WPilot Installation & Onboarding Charter v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4A charter · **4B executed**  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Status:** **PHASE 4B COMPLETE — WPILOT RC6 INSTALLED / ACTIVE / TOKEN CREATED / REST NOT RUN**

```text
Phase 4A prepared this charter (install not authorized at that time).
Phase 4B executed under exact operator confirmations:
CONFIRM METALLKA FRESH BEGET BACKUP FOR WPILOT INSTALL
APPROVE METALLKA WPILOT INSTALL — RC6 INSTALL ACTIVATE TOKEN ONLY
Bridge enablement, REST calls, and WPilot writes remain NOT AUTHORIZED (Gate E).
```

---

## 1. Purpose

Prepare the exact bounded production charter for a later Phase 4B wave that may install, activate, validate safe defaults, and create one local-only token for the accepted WPilot **RC6** baseline on metallka.ru — and **STOP**.

Supporting artefacts:

| Artefact | Path |
|----------|------|
| Package acceptance | [METALLKA-WPILOT-RC6-PACKAGE-ACCEPTANCE-v1.md](METALLKA-WPILOT-RC6-PACKAGE-ACCEPTANCE-v1.md) |
| Rollback plan | [METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md](METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md) |
| Token local storage | [METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md](METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md) |
| Post-install validation | [METALLKA-WPILOT-POST-INSTALL-VALIDATION-PLAN-v1.md](METALLKA-WPILOT-POST-INSTALL-VALIDATION-PLAN-v1.md) |

---

## 2. Current accepted production state (metallka)

| Fact | Value |
|------|-------|
| WordPress | **7.0.2** |
| PHP HTTP runtime | **8.3.20** |
| Theme | The7 parent `dt-the7` **11.6.0.1** + child `dt-the7-child` **1.0.0** |
| WPBakery | **6.10.0** |
| Hosting | Beget (backup/restore available; panel UI credentials still incomplete) |
| Staging / local mirror | Absent / **DEFER** |
| CHANGE 0001 | **COMPLETE — PRODUCTION VALIDATED** (bounded WP Admin / WPBakery text) |
| WPilot directory / active / options / tables / REST ns | **INSTALLED / ACTIVE** (Phase 4B); pre-install was **ABSENT** |
| Compatibility (Phase 2B + 4A + 4B) | **INSTALL PROVEN** for bounded RC6 onboarding; Gate E unproven |

---

## 3. WPilot baseline (do not regress to RC5)

| Field | Value |
|-------|-------|
| Baseline | **WPilot RC6** |
| Package | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Source | `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` |
| Version / RC / schema | `0.3.0` / `0.3.0-RC6` / `0.2.0` |
| Namespace / header | `wpilot/v1` / `X-WPilot-Token` |
| Remediation commit | `27dfe624eec8b10b73e34c4a5f6df323258ecd1b` |

Phase 4A package acceptance: **MATCH** (see package acceptance artefact).

---

## 4. Production maturity boundary

### Proven on i-seo.su (precedent — not metallka proof)

Package deploy · install · activation · safe defaults · RC5→RC6 remediation · hash validation · token generation with bridge/write/`dev_confirmed` false · local-only token storage · bounded frontend/admin smoke.

### Not yet production-proven (do not claim in install wave)

`X-WPilot-Token` auth · `/ping` · site-info · themes/plugins/pages reads · connection tracking via real REST · bridge · backup/dry-run/scoped-replace/rollback endpoints · any WPilot write.

Metallka Phase 4B **must not** attempt to prove those.

---

## 5. Phase 4B authorized scope (future only)

Exact future sequence:

1. Confirm fresh backup posture (operator requirement).  
2. Reconfirm package SHA.  
3. Confirm WPilot still absent immediately before install.  
4. Upload accepted RC6 ZIP.  
5. Install.  
6. Activate.  
7. Validate version / RC / schema.  
8. Validate safe defaults.  
9. Create exactly one operational token (admin mechanism).  
10. Persist token **local-only** at the approved path.  
11. Re-validate safe defaults after token.  
12. Frontend + admin smoke.  
13. **STOP.**

### Explicitly NOT included

- Bridge enable  
- Any `/wp-json/wpilot/v1/*` request (including ping)  
- Token authentication test  
- Write enable  
- Backup / dry-run / scoped-replace / rollback **endpoints**  
- WPilot content mutation  
- Plugin/theme/core updates beyond accepted RC6 install  
- Cache purge  
- Unrelated Site Ops changes  

---

## 6. Compatibility revalidation (Phase 4A)

**Verdict: CONDITIONALLY READY**

Evidence basis: Phase 2B production discovery + RC6 source/package inspection. No new production contact performed in Phase 4A.

| Factor | Assessment |
|--------|------------|
| WP 7.0.2 / PHP 8.3.20 | No source blocker found; formal `Requires PHP` / `Requires at least` remain **SAFE UNKNOWN** |
| The7 + WPBakery | Detector present; install risk low; write risk on `vc_raw_html` remains **out of scope** |
| Activation | Creates/updates `wpilot_options`; forces safe defaults false; runs `WPilot_Schema::install_or_upgrade()` → `{prefix}wpilot_backups` + `{prefix}wpilot_audit_log` |
| REST registration | Loads with plugin; inactive until activation; **must not be called** in 4B |
| Token readiness | RC6 `can_manage_token()` allows token without bridge/dev/write |
| Clearfy / security | No Wordfence/Sucuri; Clearfy active — residual interaction risk; monitor admin/frontend smoke |
| Directory / option / table / REST collisions | None pre-existing (Phase 2B) |
| Uninstall cleanup | **No `uninstall.php`** — residual options/tables likely retained after delete |

### Conditions before Phase 4B execution

1. Operator fresh Beget full backup confirmation (see §8).  
2. Exact approval string (see §12).  
3. Package SHA re-match at execution time.  
4. Immediate pre-install absence confirmation.  
5. Bridge / REST / writes remain forbidden.  
6. Operator accepts residual schema/options cleanup limitation.

---

## 7. Installation surface decision

| Option | Role |
|--------|------|
| **A. WP Admin → Plugins → Add Plugin → Upload Plugin** | **PREFERRED** |
| **B. Bounded filesystem (SSH/SFTP) deploy** | **FALLBACK ONLY — NOT automatically authorized** |

### Why WP Admin ZIP is preferred for metallka onboarding

- Lowest operational complexity for a **fresh** install (directory currently absent).  
- WordPress performs install + activation in a documented admin path already proven for metallka page edits (admin access validated in CHANGE 0001 R1).  
- Rollback of a failed upload before activation is typically “plugin not present / incomplete directory removable under charter.”  
- Avoids choosing SSH/FTP merely because credentials exist.

### Fallback note

If WordPress upload limits, permissions, or admin uploader failure block ZIP install, a **separate** bounded filesystem fallback may be prepared. It is **not** authorized by the Phase 4B approval string below unless the operator explicitly extends scope.

i-seo.su used SFTP for install-only historical reasons; that precedent does **not** override the metallka preferred default for this fresh RC6 onboarding wave.

---

## 8. Pre-execution backup requirement

**PRE-EXECUTION OPERATOR REQUIREMENT**

| Requirement | Detail |
|-------------|--------|
| Prefer | Fresh Beget **full** backup immediately before Phase 4B |
| Why stronger than CHANGE 0001 | Install adds filesystem code + options + schema tables |
| Panel credentials | Still incomplete in local secrets — agent may **not** independently prove panel timestamp |
| Acceptable proof | Exact operator confirmation string (recommended): `CONFIRM METALLKA FRESH BEGET BACKUP FOR WPILOT INSTALL` |
| Without confirmation | Phase 4B **STOP** — do not install |

Also preserve accepted RC6 package hash locally (already in package acceptance artefact).

---

## 9. Safe defaults (mandatory)

After activation **and again after token creation**:

| Setting | Required |
|---------|----------|
| `bridge_enabled` | **false** |
| `write_enabled` | **false** |
| `dev_confirmed` | **false** |

Also record: plugin active; Version `0.3.0`; RC6 label; schema `0.2.0`; no automatic bridge/write enable.

If any safe default is unexpectedly **true**:

```text
STOP → ROLLED BACK — WPILOT SAFE DEFAULT FAILURE
```

Do **not** create a token after a safe-default failure.

---

## 10. Token boundary

| Rule | Value |
|------|-------|
| Count | Exactly **one** operational token |
| Mechanism | WPilot admin token generate action |
| REST test | **FORBIDDEN** in Phase 4B |
| Bridge | Must remain **off** |
| Report / git | Token value **never** recorded |
| Local path | `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` |

See [METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md](METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md).

---

## 11. REST boundary (critical)

Phase 4B **MUST NOT** call any of:

- `/wp-json/wpilot/v1/ping`
- `/wp-json/wpilot/v1/site-info`
- `/wp-json/wpilot/v1/themes`
- `/wp-json/wpilot/v1/plugins`
- `/wp-json/wpilot/v1/pages`
- any other `wpilot/v1` endpoint

Even a “harmless ping” is forbidden. REST authentication/read contour remains a **separate Gate E**.

Expected post-4B state:

| Field | Value |
|-------|-------|
| Installed / active | YES / YES |
| Token | YES / LOCAL ONLY |
| bridge / write / `dev_confirmed` | OFF / OFF / OFF |
| REST smoke | **NOT RUN** |
| Read connection | **NOT PROVEN** |
| Writes | **BLOCKED** |

---

## 12. Execution approval (Phase 4B)

Exact future approval string:

```text
APPROVE METALLKA WPILOT INSTALL — RC6 INSTALL ACTIVATE TOKEN ONLY
```

Plus backup confirmation (recommended exact):

```text
CONFIRM METALLKA FRESH BEGET BACKUP FOR WPILOT INSTALL
```

### This approval authorizes only

Accepted RC6 package · install · activation · safe-default validation · one token · local-only persistence · frontend/admin smoke · rollback if required.

### This approval does NOT authorize

Bridge · REST · read smoke · write enable · WPilot backup/dry-run/scoped-replace/rollback endpoints · content mutations · package other than accepted RC6 · unrelated Site Ops work.

**Phase 4B status:** `INSTALLATION: EXECUTED — COMPLETE`  
Evidence: [METALLKA-WPILOT-RC6-INSTALLATION-EVIDENCE-v1.md](METALLKA-WPILOT-RC6-INSTALLATION-EVIDENCE-v1.md) · [METALLKA-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md](METALLKA-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md)

---

## 13. Success conditions (Phase 4B)

Succeeds only if all are true:

- Package SHA matches accepted value  
- Pre-install backup posture satisfied  
- WPilot absent before install  
- Exactly one install performed  
- Activation succeeds  
- Version / RC6 / schema correct  
- bridge=false · write=false · `dev_confirmed`=false (before and after token)  
- Exactly one token created and stored local-only without leakage  
- REST requests = **0**  
- Frontend smoke PASS · Admin smoke PASS  
- No rollback needed  

---

## 14. Next gate after successful Phase 4B (not approved)

```text
APPROVE METALLKA WPILOT GATE E — BRIDGE AND READ-ONLY REST SMOKE
```

May later cover: controlled bridge enable · auth test · ping · minimal read-only endpoints · connection evidence · bridge disable/rollback if needed.  
**Must not** include writes.  
**Do not** execute Gate E from this charter.

---

## 15. Rollback

See [METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md](METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md) for cases A–F.

---

## 16. Programme navigation

| Stage | Status |
|-------|--------|
| Phase 4A | **COMPLETE — CHARTER PREPARED** (history preserved) |
| Phase 4B | **COMPLETE — INSTALLED / ACTIVE / TOKEN / REST NOT RUN** |
| Gate E | **PLANNED / NOT AUTHORIZED** |

---

*METALLKA WPilot Installation & Onboarding Charter v1 · Phase 4B COMPLETE · Gate E not authorized.*

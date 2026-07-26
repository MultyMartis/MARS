# REPORT — METALLKA SITE OPS PHASE 4A WPILOT INSTALLATION & ONBOARDING CHARTER

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4A  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Mode:** Documentation / preparation only

---

## Status

**COMPLETE — WPILOT RC6 INSTALLATION CHARTER PREPARED / INSTALL NOT AUTHORIZED**

---

## Environment

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `a6802b1abd78af4128844d868227919a3b17b308` |
| `origin/mars/canonical-post-recovery` | `dc1fa5c48255efd8819b1947408d82f67bf020ca` |
| HEAD vs origin | Diverged (foreign programme history); **no pull/push this task** |
| Staged (task) | **Empty / unchanged** |
| Foreign WIP | Present elsewhere — **untouched** |

---

## Current Metallka WPilot State

| Item | State |
|------|-------|
| Plugin directory | **ABSENT** (Phase 2B evidence; not re-probed in 4A) |
| Active plugin | **ABSENT** |
| Options / tables / REST ns | **ABSENT** |
| Ghost / duplicate install | **ABSENT** |
| CHANGE 0001 | **COMPLETE — PRODUCTION VALIDATED** |
| Stack | WP **7.0.2** · PHP HTTP **8.3.20** · The7 **11.6.0.1** + child · WPBakery **6.10.0** · Beget |

---

## RC6 Package Acceptance

| Field | Value |
|-------|-------|
| Package path | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| SHA expected | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| SHA actual | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Match | **YES** |
| ZIP root | `metacode-wpilot/` only |
| Inventory | **27** files |
| Debris / secrets / nested root | **NONE** |
| Source identity | Version `0.3.0` · RC `0.3.0-RC6` · schema `0.2.0` |
| Source↔package | **27 / 27** byte match |
| Remediation commit | `27dfe624…` ancestor of HEAD — **YES** |
| RC6 token gate | `can_manage_token()` present; token does not require bridge/dev/write |

Artefact: `METALLKA-WPILOT-RC6-PACKAGE-ACCEPTANCE-v1.md`

---

## Compatibility Revalidation

**Verdict: CONDITIONALLY READY**

No hard stack blocker for bounded RC6 install/activate/token-only. Conditions: fresh backup confirm · exact approval · SHA recheck · pre-install absence · no bridge/REST/writes · residual cleanup awareness (no `uninstall.php`) · formal WP/PHP Requires remain SAFE UNKNOWN · Beget panel credentials still incomplete (operator-attested backup).

Artefact updated: `METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md`

---

## Selected Installation Surface

**PREFERRED:** WP Admin → Plugins → Upload Plugin (accepted RC6 ZIP) → install → activate.

**FALLBACK ONLY (not auto-authorized):** bounded SSH/SFTP filesystem deploy if uploader limits/permissions block Admin ZIP.

Rationale: fresh absence baseline; avoids choosing SSH/FTP merely because credentials exist; admin path already validated for metallka; rollback of failed pre-activation upload remains straightforward.

---

## Backup Requirement

**PRE-EXECUTION OPERATOR REQUIREMENT** before Phase 4B:

```text
CONFIRM METALLKA FRESH BEGET BACKUP FOR WPILOT INSTALL
```

Prefer fresh Beget full backup immediately before install. Stronger than CHANGE 0001 because filesystem + options + schema tables are introduced. Agent did **not** create a backup in Phase 4A.

---

## Installation Boundary

Future Phase 4B may do only: backup posture → SHA → absence check → upload → install → activate → identity/safe defaults → one token → local persist → post-token safe defaults → frontend/admin smoke → **STOP**.

Not included: bridge · any WPilot REST · write enable · backup/dry-run/scoped-replace/rollback endpoints · content mutation.

---

## Safe Defaults

Required after activation and after token:

- `bridge_enabled=false`
- `write_enabled=false`
- `dev_confirmed=false`

Any unexpected true → `ROLLED BACK — WPILOT SAFE DEFAULT FAILURE` · no token (if pre-token) / Case E (if post-token).

---

## Token Plan

| Field | Value |
|-------|-------|
| Count | Exactly one |
| Local path | `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` |
| Phase 4A file | **NOT CREATED** |
| REST auth test | **FORBIDDEN** in 4B |
| Report leakage | Forbidden |

---

## REST Boundary

Phase 4B **MUST NOT** call `/wp-json/wpilot/v1/*` (including ping).  
REST requests remain **0**. Read connection remains **NOT PROVEN**.

---

## Validation Plan

Frontend: `/`, `/about/`, representative service page, `/contacts/` — HTTP 200, no fatals, header/footer intact.  
Admin: Dashboard, Plugins, page 52 WPBakery editor, WPilot settings read-only if needed.  
No content edits · no form submits · no cache purge.

Artefact: `METALLKA-WPILOT-POST-INSTALL-VALIDATION-PLAN-v1.md`

---

## Rollback Matrix

Cases A–F documented in `METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md` (upload fail · activation fatal · bad safe defaults · token fail · post-token defaults · frontend/admin regression). No `uninstall.php` — residuals may remain after delete; Beget restore is strongest clean backstop.

---

## Phase 4B Success Conditions

Accepted SHA · backup posture · absent before install · one install · activation OK · version/RC6/schema OK · bridge/write/dev false before and after token · one local-only token · no leak · REST=0 · frontend+admin smoke PASS · no rollback.

---

## Future Gate E

```text
APPROVE METALLKA WPILOT GATE E — BRIDGE AND READ-ONLY REST SMOKE
```

**PLANNED / NOT AUTHORIZED.** Writes remain blocked.

---

## Execution Approval Required

```text
APPROVE METALLKA WPILOT INSTALL — RC6 INSTALL ACTIVATE TOKEN ONLY
```

Plus backup confirm string above. Until then: **INSTALLATION: NOT AUTHORIZED**.

---

## Files Created

- `projects/metallka-ru-site-ops/METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WPILOT-RC6-PACKAGE-ACCEPTANCE-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WPILOT-POST-INSTALL-VALIDATION-PLAN-v1.md`
- `projects/metallka-ru-site-ops/reports/REPORT-METALLKA-SITE-OPS-PHASE-4A-WPILOT-INSTALLATION-ONBOARDING-CHARTER.md`

---

## Files Modified

- `projects/metallka-ru-site-ops/OPERATIONAL-INDEX.md`
- `projects/metallka-ru-site-ops/METALLKA-ARTIFACT-REGISTER-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md`

---

## Production Mutations

| Class | Count |
|-------|-------|
| Plugin uploads | **0** |
| Plugin installs | **0** |
| Plugin activations | **0** |
| Token generation | **0** |
| REST requests | **0** |
| Bridge changes | **0** |
| Write changes | **0** |
| Cache purge | **0** |
| Backup creation | **0** |
| Tracked secrets | **0** |

**NONE**

---

## Git Operations

**NONE** (no add / commit / push / pull / reset / clean / stash / restore)

Staged index unchanged by this task.

---

## Risks / Conditions

- Beget panel credentials incomplete → backup proof is operator-attested.  
- No `uninstall.php` → residual options/tables after delete.  
- Formal WP/PHP Requires headers SAFE UNKNOWN.  
- Clearfy residual interaction risk → smoke required in 4B.  
- Activation creates DB schema tables — expected; strengthen backup posture.  
- HEAD/origin divergence is foreign WIP context — not resolved here.

---

## Next Operator Action

1. Create (or confirm) a **fresh Beget full backup**, then send:

```text
CONFIRM METALLKA FRESH BEGET BACKUP FOR WPILOT INSTALL
```

2. When ready to authorize Phase 4B only, send:

```text
APPROVE METALLKA WPILOT INSTALL — RC6 INSTALL ACTIVATE TOKEN ONLY
```

Do not auto-start Phase 4B without both.

---

## Next Phase

**PHASE 4B — WPILOT RC6 PRODUCTION INSTALL / ACTIVATE / TOKEN**

**NOT STARTED.**

---

## Stop Condition

**STOP after REPORT.**

No installation. No activation. No token. No REST.

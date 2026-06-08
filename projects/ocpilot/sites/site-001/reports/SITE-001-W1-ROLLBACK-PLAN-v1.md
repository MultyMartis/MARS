# SITE-001 W1 Rollback Plan v1

**Type:** Rollback plan instance — **documentation only**; no restore performed in authoring  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

**Required before:** any W1 write work on TEST.

---

## Context

| Field | Value |
|-------|-------|
| **Change request ID** | CR-SITE-001-W1-2026-06-08 |
| **Change request** | [SITE-001-W1-CHANGE-REQUEST-v1.md](SITE-001-W1-CHANGE-REQUEST-v1.md) |
| **Write charter** | [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) |
| **Execution spec** | [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) §7 |
| **Operator** | Session operator + named write approver (access brief) |

---

## Pre-change snapshot

| Artifact | Location (external) | Confirmed |
|----------|---------------------|-----------|
| **Files backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups/pre-w1-<YYYYMMDD-HHMM>/files/` | ☐ Pending — per [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) |
| **Database backup** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups/pre-w1-<YYYYMMDD-HHMM>/database/` | ☐ Pending |
| **Backup manifest** | Same folder: `BACKUP-MANIFEST.md` + `validation-checklist.md` | ☐ Pending |
| **W0.5 settings reference** | [SITE-001-W0.5-ADMIN-DISCOVERY-v1.md](SITE-001-W0.5-ADMIN-DISCOVERY-v1.md) — T1 admin re-entry source | **Available** |
| **Config note (no secrets in repo)** | Sanitized store settings export in external `materials/` when captured | ☐ Recommended |

**Label example:** `pre-w1-2026-06-08-1430`

---

## Change summary

| Field | Value |
|-------|-------|
| **Files to touch** | Theme twig under `catalog/view/theme/auto/`; custom `about.php`, `contact.php`; logo/favicon under `/img/`, `/favicon/`, `image/catalog/`; optional OG `preview.jpg` |
| **DB tables affected** | `oc_setting` (config_* keys); `oc_information_description` (IDs 3,5,7,8,9,10,11,12,13,16) |
| **ocMod/vQmod involved** | **no** direct edits — modification cache refresh only in W1F |

---

## Rollback tiers

### T1 — Wave rollback

| Field | Detail |
|-------|--------|
| **Trigger** | Single wave (W1A–W1E) fails verification; delta is known and isolated; storefront/admin still accessible; operator approves T1 |
| **Action** | Restore **only** artefacts touched in the failed wave: |
| | **W1A:** Re-enter pre-change values in admin from W0.5 snapshot or restore `oc_setting` rows from pre-W1 DB export |
| | **W1B:** Restore modified twig/html files from pre-W1 file backup |
| | **W1C:** Re-edit information pages from pre-change export **or** restore `oc_information_description` rows + controller/twig files |
| | **W1D:** Restore original logo/favicon files; re-enter `config_logo`, `config_icon` from W0.5 |
| | **W1E:** Restore controller meta files; remove new OG asset if added |
| **Expected result** | TEST site matches pre-wave state for affected surfaces; prior completed waves remain unless operator chooses full T2 |
| **Time target** | Same session where possible |

### T2 — Full TEST restore

| Field | Detail |
|-------|--------|
| **Trigger** | Multi-wave failure; unknown delta; T1 impractical; storefront or admin broken; unintended scope touched; approver authorizes T2 |
| **Action** | Beget hosting panel → restore **files + MySQL** to **pre-W1** snapshot (`pre-w1-<timestamp>` backup). Copy validated archives from external storage if panel restore uses uploaded backup. Clear theme/modification cache after restore. |
| **Expected result** | TEST instance fully matches pre-W1 baseline; all W1 changes reversed; ready for re-planning or re-execution from clean state |
| **Evidence** | Record restore timestamp, panel confirmation, post-restore verification checklist |

### T3 — Operator emergency halt

| Field | Detail |
|-------|--------|
| **Trigger** | Wrong environment suspected; security incident; credential exposure; operator/approver **STOP** command; unrecoverable error mid-session |
| **Action** | **Immediate halt** — no further writes. Close admin/FTP sessions. Confirm actual host/DB. Document incident in session REPORT. Escalate to **T2** after write approver confirms correct restore target. Do **not** continue W1 waves until re-authorization. |
| **Expected result** | No additional damage; controlled path to T2; charter suspended until [SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) re-reviewed |

---

## Rollback decision matrix

| Situation | Tier |
|-----------|------|
| W1A admin value wrong; site loads | **T1** — re-enter one key |
| Single twig broken after W1B | **T1** — restore one file |
| Multiple waves done; grep shows widespread errors | **T2** |
| White screen / admin 500 after change | **T2** |
| Edited wrong server | **T3** → **T2** |
| Uncertain what changed | **T2** |

---

## Rollback steps (operator)

### T1 procedure

1. Stop current wave; note failing check in REPORT.
2. Identify wave artefact list (execution pack §7).
3. Restore from pre-W1 file backup **or** re-enter admin/DB values from W0.5 export.
4. Clear theme cache; hard-refresh browser.
5. Run verification checklist below.
6. If pass → document partial rollback; decide retry or abort wave.

### T2 procedure

1. Execute **T3 halt** if session still active.
2. Confirm backup label `pre-w1-<timestamp>` and validation manifest **PASS**.
3. Beget → restore files to backup timestamp.
4. Beget / PMA → restore MySQL from same timestamp.
5. Clear `system/storage/cache/` and modification cache via admin or FTP (per operator practice).
6. Run full verification checklist.
7. Update Change Request outcome → `rolled back`; do not resume W1 without new authorization.

### T3 procedure

1. Operator calls **STOP** — all participants cease writes.
2. Record environment URL, account, and last successful action.
3. Do not delete backups or logs.
4. Write approver decides T2 vs investigation.
5. Re-charter only after [SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) update.

---

## Verification after rollback

| Check | Pass |
|-------|------|
| Storefront loads (`https://sibcar.new-site.space/`) | ☐ |
| Admin login succeeds | ☐ |
| Homepage shows pre-W1 title/brand (W0.5 values) | ☐ |
| Sample information page loads (`/about` or `/contact/`) | ☐ |
| Legacy brand grep matches pre-change baseline (not zero unless pre-change was already clean) | ☐ |
| No PHP errors in operator-visible log sample | ☐ |
| Rollback recorded in session REPORT with tier used | ☐ |

---

## Triggers to execute rollback (summary)

- Wave verification failure (RT-01..RT-05 in Change Request)
- Storefront or admin regression
- Scope breach (files/tables outside charter)
- Operator halt signal
- Security or environment mismatch

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Beget panel restore UX for this account | **SAFE UNKNOWN** — operator confirms at backup session |
| Partial DB table restore without full dump | **SAFE UNKNOWN** — prefer T2 if uncertain |
| Time to complete T2 on hosting | **SAFE UNKNOWN** |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — RB plan bound to CR-SITE-001-W1-2026-06-08; tiers T1/T2/T3 |

*SITE-001 W1 Rollback Plan v1 — planning only; no restore performed.*

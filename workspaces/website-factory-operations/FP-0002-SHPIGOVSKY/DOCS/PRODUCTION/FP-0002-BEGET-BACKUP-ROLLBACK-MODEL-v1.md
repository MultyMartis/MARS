# FP-0002 — Beget Backup / Rollback Model v1

**Wave:** PROD-P01  
**Host:** `shpigovsky.beget.tech` (pre-DNS-cutover)

---

## Layer A — Beget full backup

| Item | Status |
|------|--------|
| Scope | Files + database |
| Confirmation | **`BACKUP CONFIRMED BY OPERATOR`** (fresh post-migration) |
| ID / path / timestamp | **SAFE UNKNOWN** (not collected this wave) |
| Used for | Plugin install/upgrade failure; catastrophic break; DB corruption; broad recovery |
| Restore proven? | **NOT PROVEN** in this programme |

Before any future production mutation gate (WPilot upgrade, filesystem deploy, content write proofs): re-confirm that a **sufficiently recent** Layer A backup still exists.

---

## Layer B — Exact file backup

| Item | Status |
|------|--------|
| Scope | Individual files about to be overwritten |
| When | Before every authorized filesystem deployment |
| Method | Operator/hosting copy of exact paths (not broad mirror) |
| Used for | Theme/plugin exact-file rollback |

---

## Layer C — WPilot operation backup

| Item | Status |
|------|--------|
| Scope | Narrow entity / `post_content` (and WPilot’s own backup tables) |
| Equivalence | **Not** a full-site backup |
| Precedent | Polygon Gate D / P07–P12-R01 |
| On FP-0002 | Available only after WPilot version/capability is reconciled and write gates are separately chartered |

---

## Layer D — FP-0002 local engineering references

| Artifact | Path / note |
|----------|-------------|
| Stable v1 freeze | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-stable-v1-near-production-freeze-20260718-004137` |
| V9-07A01 pre-change | `...\v9-07a01-before-program-auto-source-comfort-gallery-fix-20260723-214353` |
| E63 / other wave backups | Under same backups root (historical) |
| Canonical source | `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\` |
| Local runtime mirror | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| A01 upload pack (14 files) | `X:\AI MARS STORAGE\deployment-packs\fp-0002\v9-07a01-production-upload-20260723-222232\` — **not** the full migration authority |

**Important:** Layer D is **reference / engineering** material. After production content evolves, these are **not** automatically exact production DB rollback sources.

---

## Rollback decision sketch

| Failure class | Prefer |
|---------------|--------|
| Single file deploy regression | Layer B → re-upload prior bytes |
| WPilot content write regression | Layer C (if proven for that capability) else Layer A |
| Plugin activation/upgrade break | Layer A (and/or Layer B plugin dir) |
| Broad unknown breakage | Layer A (operator-driven restore) |
| Need historical content comparison | Layer D + current production inspect — never silent overwrite |

---

## Explicit non-claims

- Beget restore was **not** exercised in PROD-P01.  
- No additional full production backup was created by MARS this wave.  
- Backup contents were not downloaded.

## PROD-P02

Access contour prepared. No additional backup created or downloaded. Layer A remains **operator-confirmed** from post-migration (P01). Re-confirm freshness before any future mutation gate.

## PROD-P05 / FU01

P05 required a Layer A backup covering the **current post-reimport** live state before WPilot 0.3.0 → 0.3.2-RC1 upgrade.

| Item | Result |
|------|--------|
| P01 Layer A | **Does not cover** current live DB/files (predates operator re-import) — do not restore it onto current production |
| Fresh post-reimport files+DB backup | **`CURRENT POST-REIMPORT LAYER A BACKUP = OPERATOR CONFIRMED`** (FU01) |
| Beget panel credentials to list backups | **MISSING** — archive not downloaded by MARS |
| Gate | **SATISFIED** by operator confirmation |
| Layer B (WPilot 0.3.0 plugin dir) | `X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\` (27 files, SHA match at copy) — retained for narrow plugin rollback |

Do **not** restore P01 Layer A onto current production — that would discard imported live content.

## PROD-P07 / FU01

P07 mutated production files + bounded DB objects after the FU01 post-reimport Layer A.

| Item | Result |
|------|--------|
| FU01 post-reimport Layer A | **Predates P07** — not sufficient as the FU01 residual-cleanup mutation gate |
| Fresh **post-P07** Beget files + DB backup | **`CURRENT POST-P07 LAYER A BACKUP = OPERATOR CONFIRMED`** (operator token `POST-P07 BEGET BACKUP CREATED`) |
| P07 Layer B exact files | `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-layer-b-pre\` — historical P07 |
| FU01 pending upload pack | `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-fu01-pending-upload\` — local new bytes; **not** a production-before snapshot |
| PROD-P07-FU01 gate | Backup **SATISFIED**; exact-file deploy **BLOCKED** — Beget SSH/FTP banner timeout |

Backup confirmation unblocked residual cleanup. Production file/DB writes remain **0** until SSH or FTP protocol banners respond.

## PROD-P09

P08 mutated production files + specialist ACF/DB after the pre-P08 Layer A.

| Item | Result |
|------|--------|
| Pre-P08 Layer A | **Predates P08** — not sufficient as the P09 mutation gate |
| Fresh **post-P08 / pre-P09** Beget files + DB backup | **REQUIRED** — not yet operator-confirmed (`OPERATOR ACTION REQUIRED — CREATE FRESH PRE-P09 BEGET FILES + DB BACKUP`) |
| P09 production mutations | **0** while gate FAIL |
| Evidence | `REPORTS/evidence/prod-p09-specialist-fancybox-smart-search/BACKUP-GATE.md` |

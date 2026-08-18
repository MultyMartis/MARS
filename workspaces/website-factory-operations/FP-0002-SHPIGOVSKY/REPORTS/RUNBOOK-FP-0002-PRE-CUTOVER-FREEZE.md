# RUNBOOK — FP-0002 PRE-CUTOVER CONTENT FREEZE

**Wave:** PROD-P17-FU02  
**Use:** immediately before the operator changes NS in REG.RU  
**Does not** switch NS, SSL, siteurl, SMTP, or indexing

---

## Purpose

Freeze WordPress content so the launch backup and the P18 domain cutover see a stable tree. After freeze, the only authorized mutation class is the cutover execution charter.

---

## Procedure (operator / Olya + Cursor)

1. **Stop editing WordPress.** Olya and operators stop creating/updating pages, services, specialists, posts, menus, Site Settings, media, and ACF.
2. **Note freeze timestamp (UTC).** Record it in the launch chat / this runbook copy. Example: `FREEZE UTC: 2026-__-__ __:__`.
3. **Verify Activity Log.** Admin → Журнал действий: no content `created`/`updated` rows after the freeze timestamp (ignore later cutover/system rows).
4. **Fresh production intake.** Confirm `home`/`siteurl` still `http://shpigovsky.beget.tech`, `blog_public=0`, mail suppression MU present, WPilot write disabled.
5. **Source ↔ production parity.** Hash-compare source-owned theme/plugin/MU files against Beget. Canonize any legitimate Olya/operator file drift **before** backup. Do not treat dirty local WIP as production truth.
6. **Full files backup.** Proven method: SSH tar of docroot `/home/s/shpigovsky/shpigovsky.ru/public_html` (see P14 script `REPORTS/evidence/prod-p14-stabilization/_p14_full_backup.py`). Destination root: `X:\AI MARS STORAGE\backups\fp-0002\`.
7. **DB backup.** Proven method: `mysqldump --single-transaction --routines --triggers` of `shpigovsky_main` via SSH, gzip to the same stamp folder.
8. **Only then** operator changes NS in REG.RU (see `RUNBOOK-FP-0002-MANUAL-NS-SWITCH-HANDOFF.md`).

---

## Required gate

`FRESH FULL BACKUP TAKEN AFTER CONTENT FREEZE`

Do **not** run P18 / domain cutover on the P14 backup (`prod-p14-full-20260816-173046`). That backup is older than P15–P17-FU02.

FU02 Layer B / obsolete tar are **exact-object** rollback packs, not a launch-time full backup.

---

## Stop

If anyone edits WordPress after the freeze timestamp: reset freeze, repeat steps 2–7.

*P17-FU02 · freeze only · NS not switched.*

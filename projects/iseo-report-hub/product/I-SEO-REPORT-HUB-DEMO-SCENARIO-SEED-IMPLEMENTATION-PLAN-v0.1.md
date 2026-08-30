# I-SEO Report Hub — Demo Scenario Seed Implementation Plan v0.1

**Status:** implementation plan only — **no seed execution in this wave**  
**Date:** 2026-08-21  
**Next wave name:** `I-SEO Report Hub — Demo User and Scenario Seed Implementation 01`  
**Tool (to create in impl):** `app-source/tools/demo-proverka-seed.php`

---

## 1. Wave goal

Create local-only demo user + `ПРОВЕРКА.рa` scenario base data in `iseo_report_hub_dev` so the team can train, then run Browser Fill Pass separately.

**Out of scope for Implementation 01:** browser automation, PDF/export/share, host upload, runtime sync of unrelated files, mutation of report 1/5.

---

## 2. Preflight (implementation wave)

1. MARS X-drive / volume / branch preflight.
2. Confirm DB: name **`iseo_report_hub_dev`**, host **`127.0.0.1`**, `APP_ENV=local` (or equivalent local config).
3. Confirm Demo Client baseline counts (optional read-only): reports 1/5 intact; exports 4; shares present.
4. **Backup before any mutation** (mandatory).

---

## 3. Backup

| Item | Path |
|------|------|
| Backup root | `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-user-scenario-seed-implementation-01\backup\` |
| Dump | timestamped `.sql` of `iseo_report_hub_dev` |
| Evidence sibling | `...\demo-user-scenario-seed-implementation-01\<timestamp>\` |

No backup → **STOP** — no seed.

---

## 4. Local-only guard (hard)

Tool must refuse unless **all** pass:

| Guard | Required |
|-------|----------|
| CLI SAPI | yes |
| DB name | exactly `iseo_report_hub_dev` |
| DB host | `127.0.0.1` (or localhost mapped to loopback — prefer numeric) |
| App env | local / non-production |
| Explicit flag | **`--confirm-local-demo-seed`** |
| Password source | env `ISEO_DEMO_SEED_PASSWORD` or hidden prompt — **not** argv commit |

Refuse production hostnames, remote DB, missing flag, wrong DB name.

Pattern after: `create-local-admin.php`, `create-local-fixture.php`, `summary-assembly-safe-fixture.php`.

---

## 5. Tool modes

| Mode | Behavior |
|------|----------|
| `--status` | Report whether marker entities exist; print non-secret IDs; exit 0 |
| `--create` | Requires `--confirm-local-demo-seed`; creates/updates per idempotency; writes evidence |
| `--cleanup` | Optional/recommended; deletes **only** IDs in evidence JSON matching marker; refuses if export/share rows exist for demo monthlies |

Idempotency:

- If marker client slug `proverka-demo` exists → `--status` and stop unless `--cleanup` then `--create`, or explicit `--recreate` (only if impl charter adds it; default = no silent recreate).

---

## 6. Create sequence

1. Backup  
2. Guards  
3. Ensure role `seo_specialist` exists  
4. Upsert demo user (see User Seed Spec)  
5. Create client / project / site with display literals + ASCII slug  
6. Create July + August reporting periods  
7. Create two monthly report rows  
8. Seed July full texts + blocks + ≥10 work entries; set July monthly (+ period) statuses per Data Spec  
9. Seed August partial texts + blocks + ≥8 work entries; status `in_progress`  
10. Optional light weekly checkpoints  
11. Write `demo-proverka-ids.json`  
12. Audit event `demo_proverka.seeded` (no secrets)  
13. Verify **zero** new rows in `report_exports` / `report_export_shares` for new monthly IDs; **no** new snapshots required  
14. Verify report **1** / **5** unchanged  

---

## 7. Evidence artifact

Path (under Storage incoming for the impl wave):

`demo-proverka-ids.json` — example shape (IDs filled at runtime):

```json
{
  "marker": "MARS_DEMO_PROVERKA_20260821",
  "created_at": "ISO-8601",
  "user_id": null,
  "client_id": null,
  "project_id": null,
  "site_id": null,
  "period_july_id": null,
  "period_august_id": null,
  "monthly_july_id": null,
  "monthly_august_id": null,
  "block_ids": [],
  "work_entry_ids": [],
  "weekly_checkpoint_ids": [],
  "notes": "no password/hash/tokens"
}
```

---

## 8. Cleanup / rollback

| Method | When |
|--------|------|
| Restore backup dump | Any failed/partial seed or operator abort |
| `--cleanup` | Exact-id + marker only; order: entries → blocks → weeklies → monthlies → periods → site → project → client → user_roles → user |
| Forbidden | `TRUNCATE`, wildcard deletes, touching Demo Client IDs, deleting exports/shares of report 1 |

Refuse cleanup if demo monthlies somehow gained export/share rows — require operator decision (manual revoke path is out of default cleanup).

---

## 9. Explicit non-actions

- No PDF / export / share create or regenerate  
- No mutation of monthly **1** or **5**  
- No host upload to `reports.i-seo.su`  
- No printing hashes/tokens  
- No browser fill in the same wave (default)  
- No `git add .` / no push  

---

## 10. Source → runtime note

Implementation edits `app-source/tools/demo-proverka-seed.php` (and only related allowlisted files if needed). Runtime sync of the **tool** is optional (CLI can run from app-source or synced runtime) — decide in impl charter; product UI code need not change for seed.

---

## 11. Exit criteria for Implementation 01

- Backup exists  
- User can be described by `--status`  
- Client/project/site/periods/monthlies present with marker  
- July full / August partial baseline content present  
- Evidence JSON written  
- Report 1/5 and existing export/share/PDF untouched  
- Ready for **Browser Filled Demo Report Pass 01**

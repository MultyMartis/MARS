# Mailer MVP stable snapshot report — v1

**Date:** 2026-05-28  
**Task:** Pre-change stable snapshot for Triumph V5 mailer operator UX polish  
**Snapshot ID:** `snap-20260528-triumph-v5-mailer-mvp-stable`

---

## Snapshot path

| Field | Value |
|-------|--------|
| **Relative** | `workspaces/_snapshots/snap-20260528-triumph-v5-mailer-mvp-stable/` |
| **Full** | `C:\AI MARS\workspaces\_snapshots\snap-20260528-triumph-v5-mailer-mvp-stable\` |
| **Manifest** | `SNAPSHOT-MANIFEST.md` in snapshot root |

---

## Included / excluded

**Included:** `src/`, `backend/`, `package.json`, `package-lock.json`, `gulpfile.js`, `reports/`, `_backup/`, `docs/`, `design/`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `logs/`, `tmp/`, `temp/`, `.cache/`, `*.log`

---

## Verification

| Check | Result |
|-------|--------|
| `backend/send-lead.php` | **PASS** |
| `src/js/form.js` | **PASS** |
| `hero--v5` on zakaz hero partial | **PASS** |
| No `data-form-handler="mock"` in built partials tree | **PASS** |
| No `api/forms/send` in `src/` | **PASS** |
| Production endpoint default in `form.js` | `backend/send-lead.php` **PASS** |

---

## Notes

- Snapshot taken **before** email template UX edits to `backend/send-lead.php`.
- `dist/` intentionally excluded; regenerate with `npm run build` after restore.

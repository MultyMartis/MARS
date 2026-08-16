# FP-0002 — Beget Production Change Model v1

**Wave:** PROD-P01  
**Authority transition:** post-migration dual authority (see `WORDPRESS/SOURCE-AUTHORITY.md` addendum)

---

## Golden rule

Never perform broad `local source → production` sync.

Before every future production filesystem mutation:

1. Inspect current production target  
2. Compare against local source  
3. Detect production/operator drift  
4. Preserve legitimate production changes  
5. Reconcile into source  
6. Backup (Layer A freshness + Layer B exact files)  
7. Deploy **exact files only**  
8. Remote verify (hash/behavior)  
9. Minimum cache action if proven necessary  
10. Frontend/admin QA  
11. Remain rollback-ready  

---

## Filesystem change

```text
production fetch → hash/diff → detect production drift → canonize legitimate drift
→ backup exact file → source edit → exact upload → remote verify
→ minimum cache action → frontend/admin QA → rollback-ready
```

Transport: future **exact-file** FTP/SFTP (or panel file manager) only.  
Forbidden: robocopy `/MIR`, broad mirror, wildcard overwrite of `wp-content`.

---

## Admin content change

- Prefer native WordPress Admin ownership for DB-owned content.  
- If the value has a source-controlled representation (ACF JSON/PHP, theme strings that should stay in Git): **canonize back into source**.  
- Demo / production cleanup decisions remain operator-chartered.

---

## ACF

Determine ownership **per field/group**:

| Ownership | Rule |
|-----------|------|
| PHP / JSON in `WORDPRESS/` | Source-owned definitions |
| DB field values / options | Admin/content authority on Beget |
| Duplicate DB groups | Historical local pattern — never broad-sync all groups |

Never “sync all ACF groups” as a routine production step.

---

## Database

No direct DB mutation as routine application workflow.  
Authorized exceptions require explicit charter + Layer A backup confirmation.

---

## FTP / SFTP

Exact-file transport only.  
Never broad mirror/sync.  
Credentials: operator-held in `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md`; never Git; never chat.

---

## WPilot

Use only for **explicitly proven** capabilities on the **reconciled** production plugin version.

Not a generic filesystem deployment tool.  
Not a substitute for theme/plugin exact-file deploys.  
Write / bridge / token gates are separate from install/reconcile gates.

---

## DNS / SSL / temporary host

Until a separate DNS cutover charter:

- Keep `shpigovsky.beget.tech` usable  
- Do not force redirects to `shpigovsky.ru`  
- Do not change WordPress siteurl solely for final domain  
- Do not mutate robots/noindex solely for temporary hostname without charter  

---

## Related docs

- `FP-0002-PROTECTED-ZONES-BEGET-v1.md`  
- `FP-0002-BEGET-BACKUP-ROLLBACK-MODEL-v1.md`  
- `FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`  
- `FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md` (PROD-P02 entry)  
- `FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`  
- `FP-0002-SOURCE-PRODUCTION-AUTHORITY-v1.md`  
- Forge Proger `RUNTIME-OPERATOR-CANON-PATTERN.md` (local visual-dev pattern; production uses the stricter fetch→diff→canonize loop above)  

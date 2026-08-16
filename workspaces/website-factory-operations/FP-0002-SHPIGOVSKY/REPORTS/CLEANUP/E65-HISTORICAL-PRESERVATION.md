# E65 Historical Preservation

## Packs

### 1. Manual-review compact pack

Path: `X:\AI MARS STORAGE\historical-packs\fp-0002\manual-review-e65-20260718-015731`

| File / dir | Role |
|------------|------|
| `HISTORICAL-PACK-OK.txt` | Validation marker |
| `INFO.md` | Contents overview |
| `MANIFEST.csv` / `HASHES-SHA256.csv` | Inventory + hashes |
| `RESTORE.md` | Restore instructions |
| `e59-e61-compact/` | E59 / E59-FIX01 / E61 DB dumps, manifests, scoped-files, operator-edits |
| `source-bak/` | Comfort pre-split JSON.bak + video bak pointer notes |
| `persistence-export-unique/` | Unique persistence export artifacts |
| `pre-e54-notes/` | Disposition notes |

Validation: `HISTORICAL-PACK-OK.txt` present; three SQL dumps present (~4.06–4.11 MB each).

### 2. E29C–E35 Git history pack

Path: `X:\AI MARS STORAGE\historical-packs\fp-0002\e29c-e35`

| File | Role |
|------|------|
| `fp-0002-e29c-e35-history.bundle` | Git bundle (tip `e93a4ca3`, requires `ebfaeb22`) |
| `fp-0002-e29c-e35-patches.zip` | `git format-patch` series (6 patches) |
| `COMMITS.md` / `MANIFEST.csv` | Commit metadata |
| `HASHES-SHA256.csv` | Hashes |
| `RESTORE.md` | Restore method |
| `HISTORY-PACK-OK.txt` | Validation marker |

`git bundle verify` = **PASS** (before and after worktree removal).

### Local branch retention (main object store)

These heads remain in the shared MARS repo (not deleted by worktree removal):

- `fp0002/v9-06e29c-e35-fix01-persistence-20260713-032549` @ `f77ee7eb…`
- `fp0002/v9-06e36-e37-mobile-polish-persistence-20260713-042025` @ `e93a4ca3…`

Deleting these branches requires a **separate** Git charter (objects remain recoverable from the bundle meanwhile).

## What was not preserved as full trees

- Full multi-GB worktree checkout (unnecessary once bundle validates)
- Full ~280 MB E59/E61 backup trees (product superseded by E63/Stable)
- Full persistence export tree (mostly duplicated validation CSVs)
- Video `.bak` binary (already identical in Stable + E63 freezes)

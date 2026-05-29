# Snapshot manifest — triumph V6 kirpich-bloki accepted

| Field | Value |
|-------|--------|
| **Snapshot ID** | `snap-20260528-triumph-v6-kirpich-bloki-accepted` |
| **Created** | 2026-05-29 |
| **Purpose** | Recovery snapshot before `kirpich-bloki` route acceptance freeze |
| **Source workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **Baseline commit (workspace tree)** | `781258f38206ffbfbe2241471148832fd590753e` |
| **Accepted route freeze** | `kirpich-bloki` |

## Included paths

| Path | Files (snapshot) | Notes |
|------|-----------------:|-------|
| `src/` | 204 | Full source tree at freeze |
| `backend/` | 11 | Lead endpoint + config |
| `docs/` | 11 | Workspace docs |
| `reports/` | 20 | Reports at copy time |
| `tools/` | 6 | Build/rollout helpers |
| `package.json` | 1 | Root manifest |
| `package-lock.json` | 1 | Lockfile |
| `gulpfile.js` | 1 | Build pipeline |
| `README.md` | 1 | Workspace readme |

## Excluded (by policy)

- `node_modules/`
- `dist/`
- `.cache/`
- `logs/`, `tmp/`, `temp/`
- `*.log`
- `_backup/`
- `_snapshots/`

Excluded directories verified absent in snapshot root.

## Restore notes

1. Copy snapshot contents into `workspaces/triumph-manipulator-landing-v6/` (or a fresh V6 workspace).
2. Run `npm ci` then `npm run build`.
3. Re-run route QA on accepted set including `kirpich-bloki`.
4. `dist/` is not stored; rebuild is mandatory after restore.

## Related report

`reports/v6-kirpich-bloki-accepted-snapshot-report-v1.md`

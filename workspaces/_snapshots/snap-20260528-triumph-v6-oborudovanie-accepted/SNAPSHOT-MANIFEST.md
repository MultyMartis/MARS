# SNAPSHOT MANIFEST — triumph v6 oborudovanie accepted

- Snapshot id: `snap-20260528-triumph-v6-oborudovanie-accepted`
- Created at: `2026-05-28`
- Source workspace: `workspaces/triumph-manipulator-landing-v6`
- Purpose: freeze/checkpoint after accepted `oborudovanie` route rollout (no redesign, no new rollout)

## Included

- `src/`
- `backend/`
- `docs/`
- `reports/`
- `tools/`
- `package.json`
- `package-lock.json`
- `gulpfile.js`
- `README.md`

## Excluded

- `node_modules/`
- `dist/`
- `.cache/`
- `logs/`
- `tmp/`
- `temp/`
- `*.log`
- `_backup/`
- `_snapshots/`

## Verification anchors

- Route set at freeze: `index`, `5-tonn`, `bytovki`, `konteynery`, `oborudovanie`
- Accepted route under freeze: `oborudovanie` (`body[data-page-type='ppc-oborudovanie']`)
- CSS scope: `ppc-oborudovanie` admitted in `_v5-machine-showcase.scss`
- Build command: `npm run build`
- Report: `reports/v6-oborudovanie-accepted-snapshot-report-v1.md`

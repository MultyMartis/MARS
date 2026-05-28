# SNAPSHOT MANIFEST — triumph v6 rollout calibration stable

- Snapshot id: `snap-20260528-triumph-v6-rollout-calibration-stable`
- Created at: `2026-05-28`
- Source workspace: `workspaces/triumph-manipulator-landing-v6`
- Purpose: stable freeze/checkpoint after rollout calibration for `5-tonn`, `bytovki`, `konteynery`

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

- Route set: `index`, `5-tonn`, `bytovki`, `konteynery`
- CSS scopes: `ppc-zakaz-manip`, `ppc-5-tonn`, `ppc-bytovki`, `ppc-konteynery`
- Build command: `npm run build`

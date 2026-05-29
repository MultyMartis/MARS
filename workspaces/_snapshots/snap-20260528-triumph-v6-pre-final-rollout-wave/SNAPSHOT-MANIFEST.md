# SNAPSHOT MANIFEST — triumph v6 pre-final-rollout-wave

- Snapshot id: `snap-20260528-triumph-v6-pre-final-rollout-wave`
- Created at: `2026-05-28`
- Source workspace: `workspaces/triumph-manipulator-landing-v6`
- Baseline commit (source tree): `5811d82eb3d8e0758d164145739a252a574f9c69`
- Branch: `mars/post-cycle8-live-tests`
- Purpose: full stable recovery snapshot before final rollout wave (`armatura`, `kirpich-bloki`, `stroymaterialy`, `vezdehod`, `yurlic`, `kray`)

## Included

- `src/` (202 files)
- `backend/` (11 files)
- `docs/` (11 files)
- `reports/` (19 files at copy time; post-freeze report added separately)
- `tools/` (4 files)
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

- Accepted route set: `index`, `5-tonn`, `bytovki`, `konteynery`, `oborudovanie`, `fbs-zhbi`
- Build command: `npm run build` (PASS at freeze time)
- Per-route markers: exactly one `id="contacts"`; `faq--split-cta`; `contact-cta--embedded`; canonical section markers; no `.hero__notice`; no `data-form-handler="mock"`; no `backend/api/forms/send.php` in dist
- Backend authority: `backend/send-lead.php` (present in dist after build)

## Restore notes

1. Copy snapshot tree over `workspaces/triumph-manipulator-landing-v6/` (human-operated; selective paths allowed).
2. Run `npm install` if `node_modules/` missing.
3. Run `npm run build` to regenerate `dist/`.
4. Re-run route marker verification on accepted route set before continuing rollout.

# V6 rollout bootstrap — report v1

**Date:** 2026-05-28  
**Source:** `workspaces/triumph-manipulator-landing-v5/` (verified `form.js` hash match vs `snap-20260528-triumph-v5-mailer-mvp-final-stable`)

## Copy

| Included | Excluded |
|----------|----------|
| `src/`, `backend/`, `docs/`, `design/`, `reports/`, `gulpfile.js`, `package.json`, `package-lock.json`, `README.md` | `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log` |

## Build

| Check | Result |
|-------|--------|
| `npm run build` | PASS |
| `dist/index.html` | Present |
| `dist/backend/send-lead.php` | Present |
| zakaz markers in dist | PASS |

## Identity

- `package.json` name → `triumph-manipulator-landing-v6`
- Canonical rules → `projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`

## SAFE UNKNOWN

- Production deploy URL map for 11 pages not verified in this pass.
- `backend/` remains gitignored — operator must preserve local `backend/` on deploy hosts.

# SNAPSHOT MANIFEST — triumph v6 production mailer routes stable

- **Snapshot id:** `snap-20260528-triumph-v6-production-mailer-routes-stable`
- **Created at:** `2026-05-28`
- **Source workspace:** `workspaces/triumph-manipulator-landing-v6/`
- **Baseline commit (pre-freeze):** `382ef6b267734351acb0a3e4d81358caae854f5b`
- **Branch:** `mars/post-cycle8-live-tests`
- **Purpose:** operational safety freeze after production mailer verification on hosting (`konteynery` hero form live test PASS)

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

## Route verification anchors

- Production route set: `index`, `5-tonn`, `bytovki`, `konteynery`
- Source pages: `src/pages/index.html`, `5-tonn.html`, `bytovki.html`, `konteynery.html`
- Mailer endpoint: `backend/send-lead.php` → `dist/backend/send-lead.php` (via gulp `backend` task)
- Form client default: `src/js/form.js` → `DEFAULT_FORM_ENDPOINT = 'backend/send-lead.php'`

## Build verification (live workspace, post-copy)

- Command: `npm run build` — **PASS**
- Dist outputs confirmed:
  - `dist/index.html`
  - `dist/5-tonn.html`
  - `dist/bytovki.html`
  - `dist/konteynery.html`
  - `dist/backend/send-lead.php`
- Per-route markers: exactly one `id="contacts"`; `faq--split-cta`; `contact-cta--embedded`; no `.hero__notice`; no `data-form-handler="mock"`; no `dist/backend/api/forms/send.php`
- Fixed titles: `Частые вопросы` on all routes; `Что не перевозим` on `bytovki`, `konteynery` (normalized entity/nbsp parity per V6 checklist)

## Live mail test (human-operated, hosting)

- URL: `https://manipulator-triumph.ru/konteynery.html`
- Form: konteynery hero form
- Recipient: `client.leads@polygon-ws.ru`
- Result: email received successfully
- Report: `workspaces/triumph-manipulator-landing-v6/reports/v6-live-mail-test-report-v1.md`

## Restore notes

- Copy snapshot tree back to `workspaces/triumph-manipulator-landing-v6/` (exclude this manifest path if restoring in-place).
- Run `npm install` and `npm run build` before deploy.
- Do not commit `node_modules/` or `dist/`; hosting deploy uses built `dist/` + `dist/backend/`.

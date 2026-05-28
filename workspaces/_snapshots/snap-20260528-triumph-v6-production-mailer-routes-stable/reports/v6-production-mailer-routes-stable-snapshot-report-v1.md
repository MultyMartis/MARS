# V6 production mailer routes stable snapshot report v1

**Date:** 2026-05-28  
**Snapshot:** `workspaces/_snapshots/snap-20260528-triumph-v6-production-mailer-routes-stable/`  
**Freeze type:** Full safety freeze / git checkpoint (no redesign, no rollout expansion)

---

## Scope

- Source: `workspaces/triumph-manipulator-landing-v6/`
- Routes: `index`, `5-tonn`, `bytovki`, `konteynery`
- Mailer: production `backend/send-lead.php` (PHP `mail()` MVP)
- Live proof: konteynery hero form on hosting (see live mail test report in workspace `reports/`)

---

## Snapshot copy verification

| Area | Live workspace | Snapshot | Result |
|------|----------------|----------|--------|
| `src/` file count | 200 | 200 | **PASS** |
| `backend/` file count | 11 | 11 | **PASS** |
| `src/pages/index.html` | present | present | **PASS** |
| `src/pages/5-tonn.html` | present | present | **PASS** |
| `src/pages/bytovki.html` | present | present | **PASS** |
| `src/pages/konteynery.html` | present | present | **PASS** |
| `node_modules/` in snapshot | — | absent | **PASS** |
| `dist/` in snapshot | — | absent | **PASS** |

---

## Build verification (`npm run build`)

| Check | Result |
|-------|--------|
| Build exit code | **PASS** (0) |
| `dist/index.html` | **PASS** |
| `dist/5-tonn.html` | **PASS** |
| `dist/bytovki.html` | **PASS** |
| `dist/konteynery.html` | **PASS** |
| `dist/backend/send-lead.php` | **PASS** |
| `dist/backend/api/forms/send.php` | **PASS** (absent) |

---

## Route verification (`dist/*.html`)

| Route | `id="contacts"` (×1) | `faq--split-cta` | `contact-cta--embedded` | `.hero__notice` | `data-form-handler="mock"` | `send.php` in HTML |
|-------|------------------------|------------------|-------------------------|-----------------|----------------------------|-------------------|
| `index.html` | 1 | yes | yes | no | no | no |
| `5-tonn.html` | 1 | yes | yes | no | no | no |
| `bytovki.html` | 1 | yes | yes | no | no | no |
| `konteynery.html` | 1 | yes | yes | no | no | no |

---

## Mailer endpoint (client + dist)

| Check | Result |
|-------|--------|
| `src/js/form.js` → `DEFAULT_FORM_ENDPOINT = 'backend/send-lead.php'` | **PASS** |
| `dist/assets/js/form.js` contains `backend/send-lead.php` | **PASS** |
| `dist/backend/send-lead.php` copied from workspace backend | **PASS** |

---

## Fixed titles (normalized)

Normalization: treat `&nbsp;` and regular space as equivalent per `V6-ROUTE-ROLLOUT-CHECKLIST.md`.

| Route | `Частые вопросы` | `Что не перевозим` |
|-------|------------------|---------------------|
| `index.html` | **PASS** | n/a (not required on index) |
| `5-tonn.html` | **PASS** | n/a |
| `bytovki.html` | **PASS** | **PASS** |
| `konteynery.html` | **PASS** | **PASS** |

---

## Live mail test summary

| Field | Value |
|-------|--------|
| URL | `https://manipulator-triumph.ru/konteynery.html` |
| Form | konteynery hero form |
| Recipient | `client.leads@polygon-ws.ru` |
| Result | Email received successfully |
| Detail report | `workspaces/triumph-manipulator-landing-v6/reports/v6-live-mail-test-report-v1.md` |

**Confirmed payload fields (operator observation):** phone, name, form_id, cta_source, landing_id, page_type, page URL, IP, User-Agent, server date.

---

## Regression risks (carry forward)

- `backend/api/forms/send.php` remains in **workspace** (legacy); not copied to `dist/` in this build — do not re-enable in gulp/deploy without explicit charter.
- Other route forms (index, 5-tonn, bytovki) not spot-tested on hosting in this freeze pass.
- Snapshot payload under `workspaces/_snapshots/…` is local survivability copy; git tracks manifest + this report only.

---

## SAFE UNKNOWN

- Long-term SMTP vs `mail()` hosting behavior under load — not proven in this checkpoint.
- Spam/rate-limit behavior on production — not load-tested here.

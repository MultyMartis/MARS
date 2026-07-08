# REPORT — SITE-002 Mail Customer Forms

**Operation ID:** SITE-002-PROD-MAIL-CUSTOMER-FORMS-01  
**OCPilot Run:** 4.226 — SITE-002 Mail Customer Forms  
**Date:** 2026-07-08  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Baseline before:** SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01  
**Checkpoint after:** SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01

---

## 1. Scope

Controlled production implementation:

1. **Customer confirmation emails** for site forms — only when a valid recipient exists (posted email field or logged-in customer account email).
2. **Form loading UX** — disable active form block during submit, spinner overlay, AbortController abort on modal close, preserve input values.

No standard OpenCart mail changes. No SMTP/admin/DB changes. No service info in customer emails.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `cad17f71` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere — **not staged** |
| STOP tokens | **None** |

---

## 3. Source authority confirmation

| Path | Exists | Mod overlay | Touch |
|------|--------|-------------|-------|
| `/public_html/catalog/controller/checkout/anketa.php` | yes | no | **yes** |
| `/public_html/system/library/zpm/mail_renderer.php` | yes | no | **yes** |
| `/public_html/assets/js/main.js` | yes | no | **yes** |
| `/public_html/assets/css/style.css` | yes | no | **yes** |
| `/storage/modification/.../anketa.php` | no | — | no |
| `/storage/modification/.../mail_renderer.php` | no | — | no |

**Confirmed:** `checkout/anketa` is live form route; `main.js` uses `fetch` + `processSubmission`; `ZpmMailRenderer::renderCustomerFormConfirmation()` exists; no modification overlay.

Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-CUSTOMER-FORMS-01\manifests\source-authority-map.{csv,json,md}`

---

## 4. Live/UI before snapshot

HTTP GET only — no submits.

| URL | HTTP | zpm-forms | Notes |
|-----|------|-----------|-------|
| `/` | 200 | 4 | callback forms without email field |
| `/katalog` | 200 | 4 | |
| `/katalog/.../stoly` | 200 | 4 | Load More present |
| PDP sample | 200 | 3 | Fancybox forms |

Before deploy: no `zpm-form--loading` class; dealer handler only changed submit button text.

Storage: `http-before/`, `ui-before/`

---

## 5. Implementation design

**Backend — customer recipient priority:**

1. Valid posted `email` field.
2. Else logged-in `$this->customer->getEmail()` if valid.
3. Else skip customer copy (not an error).

**Send order:** admin email first → customer confirmation if eligible. Customer send failure does not break admin JSON success.

**Customer email:** `ZpmMailRenderer::renderCustomerFormConfirmation()` — subject `ЗПМ: заявка получена — {dialog_label}`; contact fields + message; **no service info**.

**Frontend:** global `zpmFormSetLoading` / `zpmFormAbortPending` / `zpmFormAbortAllPending`; `AbortController` on fetch; `zpm-form--loading` CSS spinner; Fancybox close calls abort.

Storage: `manifests/implementation-design.{md,json}`

---

## 6. Patch plan and rollback

Four files touched. Rollback: re-upload exact `source-before/` copies.

Storage: `rollback/rollback-plan.md`, `rollback/remote-before-manifest.json`

---

## 7. Local patch summary

| File | Change |
|------|--------|
| `checkout/anketa.php` | `zpmResolveCustomerEmail`, `zpmSendCustomerFormConfirmation` after admin send |
| `mail_renderer.php` | Customer template: confirmation + contact fields + message; no service block |
| `main.js` | Global loading/abort helpers; `processSubmission` + dealer `processFetch` patched |
| `style.css` | `.zpm-form--loading` overlay + spinner |

**Post-deploy fix:** initial `main.js` patch placed helpers inside Fancybox IIFE (dealer form ReferenceError risk). Corrected — helpers moved to global scope before dealer IIFE; re-upload verified.

Storage: `patch/`, `source-after/`

---

## 8. Local mail preview QA

| Check | Result |
|-------|--------|
| Customer HTML contains ЗПМ | **PASS** |
| No БЗПМ | **PASS** |
| No service info in customer preview | **PASS** |
| No IP/UA in customer preview | **PASS** |
| Admin preview still has service info | **PASS** |

Storage: `mail-after/customer-form-mail-preview.{html,txt,json}`, `verification/local-mail-preview-qa.{md,json}`

---

## 9. Dry-run gates

15/15 **PASS** (G1–G15).

Storage: `manifests/dry-run.{md,json}`

---

## 10. Controlled deploy

| Remote path | SHA256 (final) | Verified |
|-------------|----------------|----------|
| `checkout/anketa.php` | `7877e545…` | yes |
| `system/library/zpm/mail_renderer.php` | `c8fb44ed…` | yes |
| `assets/js/main.js` | `756c8217…` (after global-scope fix) | yes |
| `assets/css/style.css` | `f0713374…` | yes |

Storage: `verification/upload-manifest.{csv,json}`, `verification/remote-after-sha.json`

---

## 11. Controlled test submits

| Test | Marker | Dialog | Email | HTTP | `ok` | Customer copy |
|------|--------|--------|-------|------|------|---------------|
| **A** | `MARS TEST MAIL CUSTOMER FORMS 01 EMAIL` | 7 | `[redacted test mailbox]` | 200 | **true** | path executed — **delivery SAFE UNKNOWN** |
| **B** | `MARS TEST MAIL CUSTOMER FORMS 01 NO EMAIL` | 2 | none | 200 | **true** | skipped by design |

Storage: `test-submit/test-{a,b}-*`

---

## 12. Frontend UI verification

| Check | Result |
|-------|--------|
| `window.zpmFormSetLoading` live on production | **PASS** |
| `window.zpmFormAbortAllPending` live | **PASS** |
| `.zpm-form--loading` in live CSS | **PASS** |
| Runtime loading class during submit (automated) | **PARTIAL** — async reCAPTCHA delays observable window; code path verified |

Storage: `ui-after/loading-state-verification.{md,json}`

---

## 13. Live verification after

| URL | HTTP | Notes |
|-----|------|-------|
| Home, katalog, neutral hub, stoly, PDP | 200 | no БЗПМ |
| stoly Load More | present | |
| PDP extra-info | present | |
| llms.txt | 200 | UTF-8 BOM; ЗПМ; no БЗПМ |
| robots.txt | 200 | |
| sitemap.xml | 200 | **1377** URLs |
| Live main.js loading helpers | **yes** | |

Storage: `verification/live-sanity.{md,json}`

---

## 14. Customer confirmation behavior summary

- Sends **only** when posted valid email **or** logged-in customer email exists.
- Posted email takes priority over account email (no duplicate).
- Skipped when no email — **not an error**; admin mail + JSON success unchanged.
- Subject: `ЗПМ: заявка получена — {dialog_label}`.
- Content: ЗПМ branding, confirmation, dialog type, contact fields, message — **no IP/UA/referrer/service info**.

---

## 15. Loading/abort UX summary

- On submit: `zpm-form--loading` on form container, `aria-busy="true"`, fields/buttons disabled, spinner overlay.
- On success/error: loading cleared; existing success/error UX preserved.
- On Fancybox/modal close while pending: `AbortController.abort()` + loading reset; values preserved.
- Client abort does not guarantee server-side cancellation if request already processed.

---

## 16. Privacy/security notes

- Customer emails exclude all admin service info.
- No secrets/PII in repo artefacts; test mailbox redacted.
- No new DB storage for customer email.
- No external GeoIP/API added.

---

## 17. Brand regression check

- Customer/admin subjects use **ЗПМ**.
- No public **БЗПМ** introduced (live sanity PASS).
- `bzpm.ru` domain in footer unchanged.

---

## 18. Rollback status

**Not required.** Rollback bundle available in Storage deployment folder.

---

## 19. Production mutation summary

| Metric | Value |
|--------|------:|
| Remote uploads | 4 exact files (+ 1 main.js hotfix re-upload) |
| Remote overwrites | 4 |
| Remote deletes | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Mail sends | 2 controlled tests |
| Form submits | 2 controlled tests |
| SMTP config changes | 0 |
| Live mail trigger changes | `checkout/anketa.php` only |
| Shared helper changes | `mail_renderer.php` |
| Customer copy changes | yes |
| Customer copy condition | email field or logged-in customer email only |
| Customer service info included | **no** |
| Standard OpenCart mail changes | 0 |
| Frontend JS changes | yes — `assets/js/main.js` |
| CSS changes | yes — `assets/css/style.css` |
| Header/footer/Yandex changes | 0 |
| Sitemap/robots/llms changes | 0 |
| Cache clears | 0 |
| External GeoIP/API calls | 0 |
| public БЗПМ introduced | no |

---

## 20. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-CUSTOMER-FORMS-01\`

Checkpoint storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01\`

---

## 21. Authority updates

Repository checkpoint: [SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md](../baselines/SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md)

Updated: `OPERATIONAL-INDEX.md`, `OCPILOT-STATE.md`, `production-profile.md`, `site-passport.md`, `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`, `tools/README.md`

---

## 22. Git status

Selective commit of scoped doc/tool paths only. Storage and live source downloads **not** committed.

---

## 23. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Customer confirmation inbox delivery | **SAFE UNKNOWN** — test used non-deliverable placeholder mailbox; operator inbox confirmation pending |
| PHP CLI syntax check | **SAFE UNKNOWN** — static inspection clean |

---

## 24. Final verdict

**SITE-002 MAIL CUSTOMER FORMS PARTIAL — CUSTOMER DELIVERY CONFIRMATION PENDING**

Application path verified: conditional customer send, admin mail preserved, both controlled test submits `ok: true`, loading/abort helpers live on production. Customer mailbox delivery awaits operator confirmation (same gate pattern as Run 4.224 before 4.225).

---

## 25. Next task recommendation

1. **Operator inbox confirmation** for customer test email (mirror Run 4.225).
2. **SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01** — registration, password reset, account mails.
3. **SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01** — order confirmation, admin alert, status mails.

---

## Addendum — Customer delivery confirmation

**Follow-up operation:** `SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01` (OCPilot Run **4.231**, 2026-07-09)

| Item | Result |
|------|--------|
| Prior gap | Run 4.226 Test A used non-deliverable `test@example.invalid` — customer inbox delivery **SAFE UNKNOWN** |
| Controlled retest | One submit on `/custom-equipment` dialog **11** with operator mailbox `i***@mail.ru` |
| Marker | `MARS TEST CUSTOMER DELIVERY CONFIRMATION 01` |
| Submit result | HTTP **200**, JSON **`ok: true`** |
| Customer send path | **expected active** (valid posted email) |
| Mailbox visual confirmation | **pending operator** — mirror Run 4.225 gate |
| Production/code mutation | **none** |
| Checkpoint | unchanged `SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01` |

**Report:** [SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01.md](SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01.md)

**Verdict (Run 4.231):** **SITE-002 CUSTOMER FORMS DELIVERY CONFIRMATION PARTIAL — OPERATOR MAILBOX CHECK PENDING**

Storage: `mail-after/future-standard-mail-spec.md`

# REPORT — SITE-002 Mail Recipients Discovery

**Operation ID:** SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01  
**OCPilot Run:** 4.186 — SITE-002 Mail Recipients Discovery  
**Date:** 2026-07-06  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Baseline:** SITE-002-STABLE-PROD-LOAD-MORE-01  
**Mode:** Read-only discovery — no Production mutation

---

## 1. Scope

Read-only audit of Production mail architecture for SITE-002 (BZPM / ЗПМ):

- locate form and order mail flows;
- identify where recipients are configured;
- verify suspected `anketa.php` handler;
- inventory recipient-like values (masked);
- compare implementation options for adding one more recipient;
- recommend next task — **without** adding recipients, sending mail, or changing Production.

**Out of scope:** cron/import, catalog load-more, SMTP credential exposure, OpenCart admin saves, DB reads of live settings values, test email sends.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `bbbb7ed6` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere — **not staged** |
| FTP read-only | **PASS** — 22 files downloaded, 1 probe error (missing model path) |

**STOP tokens:** none triggered.

---

## 3. Discovery method

1. Read OCPilot authority docs and prior SITE-002 knowledge (forms → `checkout/anketa`, `dialog=7`, `zpm-form`).
2. Run targeted Production FTP discovery via `site-002-prod-mail-recipients-discovery-01.py --discover`:
   - list `/catalog/controller/checkout`, `/common`, `/mail`, `/extension/module`;
   - probe 23 known mail-related paths;
   - download matched PHP/JS/Twig sources to Storage;
   - scan for mail keywords and mask email literals.
3. Manual code review of downloaded `anketa.php`, `mail/order.php`, `contact.php`, `main.js`, form templates.
4. No admin login, no DB query, no email send, no file upload.

**Storage root:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01\`

---

## 4. Discovered mail files

| Remote path | Role | Recipient hardcode | Form handler | Order mail |
|-------------|------|-------------------|--------------|------------|
| `catalog/controller/checkout/anketa.php` | **Primary unified form mail handler** | Dead legacy only | **yes** | no |
| `catalog/model/checkout/anketa.php` | DB persist for submissions | — | — | — |
| `assets/js/main.js` | AJAX POST → `checkout/anketa` | no | **yes** | no |
| `sections/fancyboxforms.twig` | Modal forms dialog 1/2/3 | no | frontend | no |
| `sections/blockcommercialtrust.twig` | PLP price-list form dialog 7 | no | frontend | no |
| `sections/blockdealersform.twig` | PLP dealers form dialog 7 | no | frontend | no |
| `sections/corpcta-form-*.twig` (6 files) | Corporate CTA forms dialog 7 | no | frontend | no |
| `catalog/controller/information/contact.php` | Native OpenCart contact | no | yes | no |
| `catalog/controller/mail/order.php` | Order customer + admin alerts | no | no | **yes** |
| `catalog/model/checkout/order.php` | Order persistence / status | no | no | indirect |
| `system/library/mail.php` | Mail transport wrapper | no | no | no |
| `system/library/mail/smtp.php` | SMTP adapter | no | no | no |
| `admin/controller/setting/setting.php` | Admin mail settings UI (reference) | no | no | no |

Full machine-readable map: Storage `source-map/discovered-mail-files.json`.

**Confirmed:** `anketa.php` path is `/public_html/catalog/controller/checkout/anketa.php` (class `ControllerCheckoutAnketa`).

---

## 5. Mail flow map

### Flow A — Unified site forms (primary)

```
zpm-form / Fancybox / corporate CTA
  → main.js sendForm / processSubmission
  → POST /index.php?route=checkout/anketa
  → ControllerCheckoutAnketa::index()
      → CSRF + reCAPTCHA validation
      → dialog N → subject/body mapping
      → model_checkout_anketa->addanketa()  (DB)
      → Mail via OpenCart config
      → foreach config_mail_alert_email → setTo + send()
```

**Dialog map (Production):**

| dialog | Subject prefix | Typical source |
|--------|----------------|----------------|
| 1 | Вопрос по товару | Fancybox |
| 2 | Обратный звонок | Fancybox |
| 3 | Вопрос по цене товара | Fancybox |
| 5 | Новый отзыв | **SAFE UNKNOWN** frontend hook |
| 7 | Форма дилерам и оптовикам | PLP Commercial Trust, Home dealers, all corporate CTA forms |

### Flow B — OpenCart contact page

`information/contact` → `setTo(config_email)` only (single store email).

### Flow C — Order notifications

Checkout confirm → `mail/order` → customer email + admin alert when `config_mail_alert` includes `order`:

- primary: `config_email`
- additional: comma-separated `config_mail_alert_email`

### Flow D — Cart

Cart/checkout controllers do **not** send mail directly; orders delegate to Flow C.

---

## 6. Recipient inventory (masked)

| Masked value | Classification | Source | Active recipient? | Mechanism |
|--------------|----------------|--------|-------------------|-----------|
| `<CONFIG_MAIL_ALERT_EMAIL>` | FORM_NOTIFICATION_EMAIL + ORDER_NOTIFICATION_EMAIL | `anketa.php`, `mail/order.php` | **yes (likely operator inbox)** | OpenCart setting — comma-separated |
| `<CONFIG_EMAIL>` | SYSTEM_FROM_EMAIL / ORDER_NOTIFICATION_EMAIL | anketa, contact, mail/order | yes (from + primary alert) | OpenCart setting |
| `s***@mail.ru` | SAFE UNKNOWN (legacy dead code) | `anketa.php` line 51 `$to = ...` | **no** — variable never used | Hardcoded but inactive |
| `i***@bzpm.ru` | POSSIBLE_SITE_OWNER_RECIPIENT | `contact.twig` mailto display | no (public contact only) | Marketing/display |
| `n***@domain.ru` | SAFE UNKNOWN | form placeholders in twig/js | no | UI placeholder text |
| `<CONFIG_MAIL_SMTP_USERNAME>` | SMTP_AUTH_EMAIL | mail senders | no | SMTP auth — not recipient |

**Operator recipient hypothesis:** Sergey's configuration most likely lives in **OpenCart admin → Settings → Mail → Mail Alert Emails** (`config_mail_alert_email`). That single setting feeds **both** form submissions (anketa) and order admin alerts.

**Not verified in this run:** exact live comma-separated value of `config_mail_alert_email` (admin/DB read excluded by charter).

---

## 7. Current architecture assessment

1. **Where is operator email configured?**  
   Primarily **`config_mail_alert_email`** (OpenCart DB setting). Not the hardcoded `$to` in `anketa.php`.

2. **Is it in anketa.php?**  
   **Partially.** `anketa.php` is the send handler, but recipients come from **`config_mail_alert_email`**, not from line 51 dead code `s***@mail.ru`.

3. **Forms vs cart — same recipients?**  
   **Forms:** anketa → `config_mail_alert_email`.  
   **Orders:** mail/order alert → `config_email` + same `config_mail_alert_email`.  
   **Shared alert list** — yes, for admin notifications.

4. **OpenCart native order mail?**  
   Uses standard `config_email`, `config_mail_alert`, `config_mail_alert_email` — no custom recipient hardcode in `mail/order.php`.

5. **Multiple recipients already supported?**  
   **Yes** — both anketa and order alert iterate comma-separated `config_mail_alert_email`.

6. **Recipients duplicated across files?**  
   **No active duplication.** One OpenCart setting drives multiple flows. Legacy unused hardcode exists once in anketa.

7. **SMTP separate from recipients?**  
   **Yes.** SMTP hostname/user/password/port from OpenCart mail settings; recipients from email/alert settings.

8. **Anti-spam dependencies?**  
   **Yes** — CSRF session token (header.php) + Google reCAPTCHA v3 on anketa route. Contact page uses native validation only.

9. **Risk of adding second hardcoded recipient in anketa?**  
   **Low–medium** — works but bypasses admin-managed list; duplicates logic; dead `$to` line adds confusion. **Lower risk:** append to `config_mail_alert_email` via admin (no deploy).

10. **Risk of admin settings page?**  
    **Medium–high** — new admin extension, permissions, validation, rollback surface; justified as phase 2 if operators need non-technical control without OpenCart core settings access.

**Notable code smell:** `anketa.php` echoes JSON success **before** `$mail->send()` — mail still sends, but error handling after response is invisible to client.

---

## 8. Implementation options

### OPTION A — Minimal add (recommended first)

**Path 0 (preferred, no deploy):** Operator adds second email to OpenCart **Mail Alert Emails** (`config_mail_alert_email`) in admin. Already supported by anketa + order loops.

**Path A1 (code, if admin path unavailable):** Append recipient in `anketa.php` foreach loop or second explicit `setTo`+`send`. File: `catalog/controller/checkout/anketa.php` only.

| Aspect | Assessment |
|--------|------------|
| Files | 0 (admin) or 1 (anketa.php) |
| DB impact | Admin setting row only (Path 0) |
| Rollback | Remove email from admin or revert single PHP file |
| Test plan | Submit test form + test order in supervised window |
| Risk | **Low** (admin) / **Low–medium** (code) |

### OPTION B — Storage config file

Store recipient list in `/storage/mars-tools/site-mail/recipients.json`; anketa + optional wrapper read list.

| Aspect | Assessment |
|--------|------------|
| Files | anketa.php + new storage config + optional reader |
| DB impact | none |
| Rollback | revert PHP + delete config |
| Risk | **Medium** — new read path, FTP-managed |

### OPTION C — OpenCart admin custom section

Dedicated admin module for form vs order recipients, enable flags, validation.

| Aspect | Assessment |
|--------|------------|
| Files | admin controller/model/language/template + catalog hook changes |
| DB impact | new setting keys |
| Rollback | disable module + revert |
| Risk | **Higher** — scope, security review, permissions |

---

## 9. Recommendation

**Verdict:** Discovery confirms a **simple safe path exists without code deploy**.

### Recommended sequence

1. **Immediate (HITL):** Operator verifies current **Mail Alert Emails** in OpenCart admin. If operator inbox is there, add second recipient as comma-separated entry — **no Cursor deploy required**.

2. **If admin access blocked or value must be code-managed:**  
   Next Cursor task: **SITE-002-PROD-MAIL-RECIPIENTS-ADD-01** — single-file change to `anketa.php` loop **or** documented admin-only procedure with verification checklist.

3. **Phase 2 (later):** **SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-CONCEPT-01** — design dedicated admin UI only if operators cannot use core OpenCart mail settings safely.

### Answers

| Question | Answer |
|----------|--------|
| Can we safely add another recipient now? | **Yes** — via existing `config_mail_alert_email` multi-value support |
| Which file(s) would change? | **Prefer none** (admin). Else: `catalog/controller/checkout/anketa.php` |
| Forms and orders share recipients? | **Yes** — same `config_mail_alert_email` for form + order alerts |
| Admin UI now or phase 2? | **Phase 2** unless operator cannot use OpenCart Settings → Mail |
| Next task ID | **SITE-002-PROD-MAIL-RECIPIENTS-ADD-01** (after operator confirms admin path vs code path) |

---

## 10. Remote mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Email sends | 0 |
| Database operations | 0 |
| Admin saves | 0 |
| Cron/import changes | 0 |
| Catalog/frontend changes | 0 |
| Legacy Sergey files edited | 0 |
| Cache clears | 0 |

---

## 11. Storage artefacts

| Path | Purpose |
|------|---------|
| `.../deployments/SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01/manifests/operation.json` | Operation manifest |
| `.../source-map/discovered-mail-files.json` | FTP probe results |
| `.../source-map/discovered-mail-files.md` | Human file map |
| `.../findings/mail-flow-map.json` | Flow architecture |
| `.../findings/recipient-inventory.json` | Masked recipient inventory |
| `.../source/catalog__controller__checkout__anketa.php` | Primary handler (Storage only) |
| `.../logs/discovery.log` | FTP session log |

---

## 12. Authority updates

Updated in repository:

- `projects/ocpilot/OPERATIONAL-INDEX.md` — Run **4.186**
- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`

**No new Production checkpoint** (read-only discovery).

---

## 13. Git status

Selective commit planned for report + docs + discovery tool only. Storage artefacts and downloaded Production PHP **not** committed.

---

## 14. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact live `config_mail_alert_email` value | **SAFE UNKNOWN** — admin/DB not read |
| Whether operator inbox matches `s***@mail.ru` dead code | **SAFE UNKNOWN** |
| dialog=5 (review) live frontend trigger | **SAFE UNKNOWN** |
| Whether contact page form is actively used vs anketa forms | **SAFE UNKNOWN** |
| SMTP provider / deliverability constraints for +1 recipient | **SAFE UNKNOWN** |

**Blockers for ADD task:** Operator must confirm preferred path (admin setting vs code) and provide candidate recipient (masked in docs until implementation charter).

---

## 15. Final verdict

**SITE-002 MAIL RECIPIENTS DISCOVERY COMPLETE — IMPLEMENTATION OPTION READY**

Primary handler mapped: `checkout/anketa.php`. Active recipients driven by OpenCart `config_mail_alert_email` with existing multi-recipient support. Next step: **SITE-002-PROD-MAIL-RECIPIENTS-ADD-01** after operator chooses admin-only vs single-file code add.

---

**Tool:** [site-002-prod-mail-recipients-discovery-01.py](../tools/site-002-prod-mail-recipients-discovery-01.py)

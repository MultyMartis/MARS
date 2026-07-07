# REPORT — SITE-002 Mail System Discovery

**Operation ID:** SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01
**OCPilot Run:** 4.222 — SITE-002 Mail System Discovery
**Date:** 2026-07-08
**Environment:** PRODUCTION (`https://bzpm.ru/`)
**Baseline:** SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01
**Mode:** Read-only discovery — no Production mutation

---

## 1. Scope

Read-only mail architecture discovery for SITE-002 (ЗПМ / bzpm.ru) before email redesign:

- public form inventory (HTTP GET only);
- custom form / admin mail source map;
- standard OpenCart/ocStore transactional mail inventory;
- mail configuration authority (redacted);
- service info availability for future admin emails;
- current mail body structure samples (from source, no send);
- unified mail design system proposal;
- implementation options and staged future charters.

**Out of scope:** template changes, SMTP changes, admin saves, DB writes, FTP uploads, test email sends, form submits, header/footer/Yandex, PDP/category code.

**Prior context:** Run 4.186 (recipient discovery), Run 4.187 (admin recipient update confirmed).

---

## 2. Operator backup confirmation

Operator confirmed **full Beget backup** of the current Production point immediately before this task. Backup existence does **not** authorize mutation — this run remained read-only.

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `65dd966e` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere (FP-0002, mars-website-factory, etc.) — **not staged** |
| FTP read-only | **PASS** — 53 files downloaded, 3 probe errors |
| HTTP crawl | **PASS** — 6 URLs, 29 form instances detected, 0 submits |

**STOP tokens:** none triggered.

---

## 4. Public form inventory

**Method:** HTTP GET on charter URLs; HTML form parse; no POST/submit.

| URL | HTTP | Forms |
|-----|------|------:|
| https://bzpm.ru/ | 200 | 5 |
| https://bzpm.ru/kontakty | **404** | 4 (error page shell) |
| https://bzpm.ru/katalog | 200 | 5 |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie | 200 | 5 |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly | 200 | 6 |
| https://bzpm.ru/katalog/.../derzhatel-dlya-gastroemkostey-pg-10-3-... | 200 | 4 |

**Note:** `/kontakty` returns 404 on live Production. Contact page SEO URL is **SAFE UNKNOWN** — likely `information/contact` rewrite (not re-probed beyond charter list).

### Form families (mail-relevant)

| Family | Dialog | Route | Mail target | Antispam |
|--------|--------|-------|-------------|----------|
| Fancybox callback | 2 | `checkout/anketa` | admin | CSRF + reCAPTCHA v3 |
| Fancybox question | 1 | `checkout/anketa` | admin | CSRF + reCAPTCHA v3 |
| Fancybox price ask | 3 | `checkout/anketa` | admin | CSRF + reCAPTCHA v3 |
| Commercial Trust / dealers / corp CTA | 7 | `checkout/anketa` | admin | CSRF + reCAPTCHA v3 |
| Home dealers block | 7 | `checkout/anketa` | admin | CSRF + reCAPTCHA v3 |
| Header search | — | `/search/` GET | none | — |
| Filter sidebar | — | PLP filter GET | none | — |
| Native contact (legacy) | — | `information/contact` | admin (`config_email`) | OpenCart captcha if enabled |

**Primary handler:** all `zpm-form` AJAX → `POST /index.php?route=checkout/anketa` via `assets/js/main.js`.

**Customer copy from forms:** **none** implemented.

**Storage:** `form-inventory/public-form-inventory.{json,csv,md}`, `http/public-form-pages-summary.md`

---

## 5. Custom form / admin mail source map

| File | Trigger | Recipient | Subject | Body | Service info |
|------|---------|-----------|---------|------|--------------|
| `catalog/controller/checkout/anketa.php` | dialogs 1/2/3/5/7 | `config_mail_alert_email` | per dialog Russian prefix | HTML (`setHtml`) + plain (`setText`) — minimal `<p>` concatenation | **no** |
| `catalog/model/checkout/anketa.php` | all anketa submits | DB only | — | — | **no** |
| `assets/js/main.js` | `sendForm` / Fancybox / dealers | posts to anketa | — | FormData + csrf + recaptcha | **no** page URL/IP/UA |
| `sections/fancyboxforms.twig` | modals 1/2/3 | via anketa | — | UI | — |
| `sections/blockcommercialtrust.twig` | PLP lead dialog=7 | via anketa | Форма дилерам и оптовикам | UI | — |
| `sections/blockdealersform.twig` | hub dealers dialog=7 | via anketa | same | UI | — |
| `sections/corpcta-form-*.twig` (6) | corporate CTA dialog=7 | via anketa | same | UI | — |
| `catalog/controller/information/contact.php` | native POST contact | `config_email` | language `email_subject` | plain text enquiry only | **no** |

**Code smells (anketa):**

- Dead legacy `$to = 's***@mail.ru'` line 51 — **not used** in send loop.
- JSON success echoed **before** `$mail->send()` — client cannot see mail transport errors.
- No HTML template — inline string assembly.

**Storage:** `admin-mail/custom-form-mail-source-map.{json,csv,md}`

---

## 6. Standard OpenCart mail inventory

Production mail controllers confirmed under `/public_html/catalog/controller/mail/`:

| Mail type | Trigger | Recipient | Source | Template | Format | Priority |
|-----------|---------|-----------|--------|----------|--------|----------|
| Customer registration | account register event | customer | `mail/register.php` | `mail/register.twig` | text twig | Stage 3 |
| Registration admin alert | `config_mail_alert` includes `account` | admin + alert emails | `mail/register.php` alert() | `mail/register_alert.twig` | text | Stage 3 |
| Password forgotten | account/forgotten | customer | `mail/forgotten.php` | `mail/forgotten.twig` | text | Stage 3 |
| Order confirmation | order status 0→N | customer | `mail/order.php` add() | `mail/order_add.twig` | **HTML** table layout | Stage 4 |
| Admin order alert | new order + `order` in mail_alert | `config_email` + alert list | `mail/order.php` alert() | `mail/order_alert.twig` | text | Stage 4 |
| Order status update | status change + notify | customer | `mail/order.php` edit() | `mail/order_edit.twig` | text | Stage 4 |
| Affiliate | if module active | customer/admin | `mail/affiliate.php` | `mail/affiliate.twig`, `affiliate_alert.twig` | SAFE UNKNOWN | Stage 5 |
| Transaction | balance alert if enabled | customer | `mail/transaction.php` | `mail/transaction.twig` | SAFE UNKNOWN | Stage 5 |
| Voucher | gift voucher if enabled | customer | SAFE UNKNOWN | `mail/voucher.twig` | SAFE UNKNOWN | Stage 5 |
| Review notification | language `mail/review.php` exists | SAFE UNKNOWN | SAFE UNKNOWN | — | SAFE UNKNOWN | Stage 5 |

**Design status:** default OpenCart 3.0.3.9 twig — inline styles, 680px order table, store logo header. No ЗПМ brand wrapper.

**Storage:** `standard-opencart-mail/standard-mail-inventory.{json,md}`

---

## 7. Mail configuration authority

| Item | Authority |
|------|-----------|
| Mail engine | **SMTP** (inferred from `system/library/mail/smtp.php` + OpenCart Mail class usage; exact live `config_mail_engine` value **SAFE UNKNOWN**) |
| Sender email | `config_email` |
| Sender name | `config_name` |
| Form admin recipients | `config_mail_alert_email` (comma-separated loop in anketa) |
| Order admin primary | `config_email` |
| Order admin additional | same `config_mail_alert_email` |
| Mail alert flags | `config_mail_alert` array — includes `order`; `account`/`affiliate`/**return** — **SAFE UNKNOWN** live values |
| Admin UI | System → Settings → Mail (Run 4.186/4.187) |
| Legacy hardcode | anketa `$to` — inactive |

**Secrets:** not read; SMTP password not printed.

**Storage:** `mail-inventory/mail-config-authority.{json,md}`

---

## 8. Service info availability

| Field | Available now | In anketa mail today |
|-------|---------------|----------------------|
| IP (`REMOTE_ADDR` / proxy headers) | yes server-side | **no** |
| User-Agent | yes | **no** |
| Referrer | yes | **no** |
| Page URL | JS can send; server has `REQUEST_URI` on POST only | **no** |
| City | **no safe source** without GeoIP/API | **no** |
| Date/time | DB `date_added` only | not in mail body |
| Customer login status | `$this->customer` in OpenCart | **no** |
| UTM params | only if added to form/URL | **no** |

**Recommended phase 1 city policy:** Option A — IP only, city marked unknown.

**Future implementation:** extend `anketa.php` + optional JS hidden fields (`source_page`, `referrer`); admin-only `email-service-info` block in redesigned template; **no** IP/UA in customer-facing mail.

**Storage:** `service-info/service-info-availability.{json,md}`

---

## 9. Current mail body samples

Reconstructed from source (no live send):

### Admin form (anketa)

```
Subject: {{ subject_by_dialog }}
Body (HTML):
  {{ dialog_prefix }}
  {{ optional_tovar }}
  {{ optional_subject_line }}
  {{ message }}
  <p>{{ name }}
  <p>{{ phone }}
  <p>{{ email }}
Plain: strip_tags(same)
```

### Customer form confirmation

**Not implemented.**

### Customer order confirmation (`mail/order_add.twig`)

Standard OpenCart: logo, greeting, order detail table (id, date, payment, email, phone, **IP**, status), products table, totals, footer.

### Admin order alert (`mail/order_alert.twig`)

Text: received notice, order id, product list, totals, comment.

**Storage:** `mail-inventory/current-mail-body-samples.{json,md}`

---

## 10. Design system proposal

Unified **ЗПМ** B2B industrial email system (documentation only):

- **Layout:** 600px table-based container; header (logo + site); title; summary card; content blocks; optional CTA; admin-only service info section; footer (contacts, site link).
- **Admin emails:** task-oriented; highlight contact data + form source + service block; no marketing.
- **Customer emails:** polite transactional tone; clear next step; no internal debug fields.
- **Technical:** inline CSS; UTF-8 Cyrillic; plain-text fallback; no external fonts; no tracking pixels; no large images.

**Components:** `email-header`, `email-title`, `email-summary-card`, `email-key-value-table`, `email-message-block`, `email-service-info`, `email-order-table`, `email-footer`, `email-button`.

**Storage:** `design-system/mail-design-system-proposal.{json,md}`

---

## 11. Implementation options

| Option | Description | Verdict |
|--------|-------------|---------|
| A | Patch controllers directly | Works but duplicates HTML; harder maintenance |
| B | Shared renderer `system/library/zpm/mail_*` | Best long-term consistency |
| C | Twig templates only | Good for standard OC mails; anketa still needs controller |
| **D** | **Hybrid: shared wrapper + existing twig** | **Recommended** |

**Staged roadmap:**

1. Admin form emails + service info (`anketa.php`)
2. Customer form confirmations (optional)
3. Registration / account / forgotten
4. Order confirm / admin alert / status update
5. Affiliate / voucher / transaction polish

**Storage:** `implementation-options/mail-implementation-options.{json,md}`

---

## 12. Future task charters

| Charter ID | Purpose |
|------------|---------|
| `SITE-002-PROD-MAIL-DESIGN-SYSTEM-01` | Shared helper/templates without changing triggers |
| `SITE-002-PROD-MAIL-ADMIN-FORMS-01` | Redesign admin form emails + service info |
| `SITE-002-PROD-MAIL-CUSTOMER-FORMS-01` | Customer form confirmations (optional) |
| `SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01` | Registration/password/account mails |
| `SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01` | Order/admin/status mails |

Each charter includes scope, likely files, test plan (supervised send), rollback (Storage rollback/), admin approval, privacy text where needed.

**Storage:** `future-charters/mail-future-charters.{json,md}`

---

## 13. Production mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| SMTP config changes | 0 |
| Mail template changes | 0 |
| Product data changes | 0 |
| Category data changes | 0 |
| PDP changes | 0 |
| Category entrypoint changes | 0 |
| Images generated/uploaded | 0 |
| llms.txt changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| Cron/import runs | 0 |
| Cache clears | 0 |
| public БЗПМ introduced | no |

---

## 14. Storage artefacts

**Root:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01\`

| Path | Purpose |
|------|---------|
| `manifests/operation.json` | Operation manifest |
| `form-inventory/` | Public form inventory |
| `http/` | Crawled HTML + summary |
| `source-readonly/` | 53 FTP-downloaded PHP/Twig/JS files |
| `admin-mail/` | Custom form mail map |
| `standard-opencart-mail/` | Standard mail inventory |
| `mail-inventory/` | Config authority + body samples |
| `service-info/` | Service info feasibility |
| `design-system/` | Design proposal |
| `implementation-options/` | Options comparison |
| `future-charters/` | Ready charters |
| `reports/discovery-summary.json` | Run summary |
| `logs/ftp-discovery.log` | FTP session log |

---

## 15. Authority updates

Updated in repository:

- `projects/ocpilot/OPERATIONAL-INDEX.md` — Run **4.222**
- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`

**Audit baseline:** `SITE-002-MAIL-SYSTEM-DISCOVERY-01` (read-only; no Production checkpoint change).

---

## 16. Git status

Selective commit: report + docs + discovery tool only. Storage artefacts and downloaded Production source **not** committed.

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact live SMTP/engine settings | **SAFE UNKNOWN** — admin/DB not read |
| Exact `config_mail_alert_email` value post-4.187 | **SAFE UNKNOWN** |
| Live contact page SEO URL (`/kontakty` 404) | **SAFE UNKNOWN** — verify operator-facing contact route |
| dialog=5 (review) live frontend trigger | **SAFE UNKNOWN** |
| Affiliate/voucher/return/review modules enabled | **SAFE UNKNOWN** |
| GeoIP / CDN city header on Beget | **SAFE UNKNOWN** |
| OC modification overlay mail overrides | probe listed dirs only — file-level overrides **SAFE UNKNOWN** |
| `catalog/controller/mail/customer.php` | missing on server (550) — not used |

**Blockers for redesign:** none for charter approval. Implementation charters require operator approval + supervised test sends.

---

## 18. Final verdict

**SITE-002 MAIL SYSTEM DISCOVERY COMPLETE — MAIL REDESIGN CHARTERS READY**

Mail architecture mapped: unified `checkout/anketa` for site forms; standard OpenCart twig mails for orders/account; recipients via `config_mail_alert_email` (forms + order alerts). No service info in admin mails today. Hybrid shared-renderer approach recommended. Five future charters prepared.

---

## 19. Next task recommendation

**SITE-002-PROD-MAIL-DESIGN-SYSTEM-01** — implement shared mail renderer + base twig components in a controlled deploy (no trigger change), then **SITE-002-PROD-MAIL-ADMIN-FORMS-01** for anketa redesign + service info block.

**Tool:** [site-002-prod-mail-system-discovery-01.py](../tools/site-002-prod-mail-system-discovery-01.py)

**Prior runs:** [SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md](SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md) (4.186) · [SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md](SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md) (4.187)

# REPORT — FP-0002 PROD-P18C SMTP / Forms Foundation

**Date:** 2026-08-19  
**Core:** `0.3.12-p18c`  
**Parity:** `14/14 SOURCE ↔ PRODUCTION MATCH`  
**Evidence:** `REPORTS/evidence/prod-p18c-smtp-forms-foundation/`

---

## 1. Status

**PASS**

Foundation is live. Real SMTP is **not** verified. Mail suppression remains **ON**. Indexing remains **CLOSED**. The operator can now enter `noreply@shpigovsky.ru` credentials and recipients in WordPress Admin without touching code.

## 2. Current Forms / Mail Reality

**P18C CURRENT FORMS / MAIL REALITY VERIFIED** (pre-change intake).

- One form owner: `ConsultationHandler` AJAX `fp02_lead_submit` (modal + final-form, `data-lead-form`).
- No competing SMTP plugin.
- `pre_wp_mail` suppression **ON**.
- No lead table before this wave.
- Production handler still had unused historical recipient constant `client.leads@polygon-ws.ru` (emptied in source; recipients now Admin-owned).
- Direct PHP `mail()` not used by the form path; outbound uses `wp_mail` after persist.
- Public `https://shpigovsky.ru/` still observed as **Craftum CMS**; WordPress forms visible on inner `shpigovsky.beget.tech` routes (e.g. privacy).
- `home`/`siteurl` = `https://shpigovsky.ru`. `blog_public=0`. WPilot write **false**.

## 3. Admin

**ONE ADMIN SOURCE OF TRUTH FOR SMTP / FORM DELIVERY CONFIGURATION**

- Path: **Настройки сайта → Почта и формы** (`fp02-site-settings-mail-forms`)
- Business menu: **Заявки** (`fp02-form-leads`)
- Sections: Отправка почты · Получатели · Формы · Проверка
- Fields: smtp_enabled, host, port, encryption (none/tls/ssl), auth, username, write-only password, from email/name, recipient rows, Metrika goal, retention days
- Test / activate actions exist but stay hidden or inert until config is complete / verified

## 4. Sender

- Default: **noreply@shpigovsky.ru**
- From name: Site Settings `organisation_name` → currently **Шпиговский дом** (fallback «Шпиговский Дом» / blogname)

## 5. SMTP Secret Handling

**SMTP PASSWORD IS NEVER RENDERED, LOGGED OR COMMITTED**

Write-only Admin field. Blank keeps existing secret. Stored in `fp02_mailbox_auth` (autoload false). Not in Dashboard, Activity Log, REST, HTML, Git, or this report. WordPress DB ≠ secret manager (documented honestly).

## 6. SMTP State Model

- **NOT CONFIGURED** ← current
- **CONFIGURED / NOT VERIFIED**
- **VERIFIED / NOT ACTIVE** then **VERIFIED / ACTIVE**
- **ERROR**

Save does not verify. Save does not activate.

## 7. Transport

**ONE SMTP TRANSPORT OWNER**

`SmtpTransport` on `phpmailer_init` only. No extra mail plugin.

## 8. Mail Suppression

- Current: **ON** (`MailOps::should_suppress()` because `delivery_active=0`; MU defers to that owner).
- Retirement: VERIFIED + operator «Включить отправку писем» → MU stops blocking → later remove the temporary MU (not this wave).

## 9. Recipients

- Repeater: email + optional label; first = main.
- Validated with `is_email`.
- Reply-To = visitor email **only if valid**. Form has no required email; phone-only → no fake Reply-To. From is never the visitor.

## 10. Internal Lead Registry

**FORM LEAD PERSISTENCE DOES NOT DEPEND ON EMAIL SUCCESS**

- Table: `fp02_form_leads` schema version `1` (idempotent `dbDelta`).
- Statuses: RECEIVED → MAIL_SUPPRESSED / SMTP_PENDING / MAIL_ACCEPTED / MAIL_ERROR.
- No IP, cookies, headers, or password. Message capped. QA flag for test rows.
- Retention days = 0 → **FORM LEAD RETENTION PERIOD — OPERATOR DECISION REQUIRED** (no auto-delete).
- Sequence: validate → persist → attempt mail → update status → JSON.

## 11. Admin Leads

- List: дата, форма, имя, телефон, email, страница, статус, UTM.
- Detail: fields + source + UTM + sanitized error. No SMTP password.
- Filters: date, form, status, path, UTM, QA checkbox.
- Stats: total / today / 7d / 30d / mail accepted / mail errors.

## 12. Metrika

**BACKEND CONFIRMED FORM SUCCESS → FRONTEND METRIKA GOAL**

- Goal identifier: Admin «Цель Яндекс.Метрики».
- Counter: SEO / Integrations only (not duplicated in form settings).
- Event semantics: **FORM SUBMISSION ACCEPTED** (lead stored), not EMAIL DELIVERED.
- JS `reachGoal` after successful AJAX; no throw if Metrika/adblock/goal empty.
- Registry stores configured goal id; does **not** claim browser `reachGoal` succeeded.

## 13. Attribution

- `utm_source|medium|campaign|content|term` from URL + `sessionStorage` `fp02_utm`.
- `source_url` / `source_path` / `source_post_id` / form key `consultation`.

## 14. QA

- Persist QA: accepted=true, `MAIL_SUPPRESSED`, mail_attempted=false.
- Duplicate token: rejected.
- Too-fast fill: rejected.
- QA row `is_qa=1` deleted (0 left).
- No real SMTP send.
- Metrika unconfigured: empty goal/counter, UX still success.
- UTM `p18c` / path `/p18c-qa/` captured.
- Public Admin HTTP login via `https://shpigovsky.ru/wp-login.php` **FAIL** (Craftum origin). Admin screens proven via CLI render (redaction + headings).

## 15. Security

- Cap: `manage_options`. Save/test/activate: POST + nonce.
- `$wpdb->insert` / `prepare` for leads.
- Escaping on Admin output.
- Lead list is Admin-only (no public REST).
- Personal-data exporter/eraser by **email** implemented (follow-up: phone-only leads). Not a legal-compliance claim.
- Secret redaction: PASS.

## 16. Dashboard

- Mail: **SMTP SETTINGS READY — CREDENTIALS REQUIRED**
- Sender: `noreply@shpigovsky.ru`
- Leads: **ACTIVE**
- Metrika form goals: **CONFIGURABLE**
- Indexing: **CLOSED — WAITING FOR OLYA APPROVAL**

## 17. WP Forge Knowledge

- `noreply@<domain>`
- Persist lead before mail
- SMTP secrets: Admin-configurable, never rendered/logged/Git
- Analytics: backend-confirmed success, never button click
- Lead registry is source of truth; email is transport
- Temporary suppression has retirement lifecycle
- Anti-patterns **AP-022–028 (FORM-001–007)** in the registry

## 18. Source / Production Parity

**14/14 MATCH**

## 19. Git

See `GIT-CHECKPOINT.json` after the checkpoint wave. Dirty main foreign WIP untouched. Secret scan mandatory. No SMTP password.

## 20. Operator Next Action

1. Open **Настройки сайта → Почта и формы**
2. Enter SMTP host, port, encryption, username, password, recipients
3. Save
4. Do **not** open indexing
5. Report back that SMTP settings are saved

Then the next wave verifies real SMTP and form delivery.

## 21. Remaining Launch Work

OPERATOR SMTP SETTINGS → SMTP VERIFICATION → REAL FORM DELIVERY QA → PUBLIC-DOMAIN FINAL SMOKE → OLYA INDEXING APPROVAL → SITEMAP SUBMISSIONS → FINAL CRAWL

## 22. Acceptance

**FP-0002 P18C COMPLETE — SMTP / FORM DELIVERY SETTINGS HAVE ONE SAFE ADMIN OWNER — NOREPLY SENDER CONVENTION ACTIVE — SMTP SECRET HANDLING IS REDACTED — INTERNAL FORM LEADS ARE PERSISTED BEFORE EMAIL TRANSPORT — BUSINESS-FACING LEAD HISTORY / STATISTICS EXISTS — YANDEX METRIKA GOALS ARE ADMIN-CONFIGURABLE AND FIRE ONLY AFTER BACKEND-CONFIRMED SUBMISSION — MAIL SUPPRESSION REMAINS UNTIL REAL SMTP VERIFICATION — INDEXING REMAINS CLOSED**

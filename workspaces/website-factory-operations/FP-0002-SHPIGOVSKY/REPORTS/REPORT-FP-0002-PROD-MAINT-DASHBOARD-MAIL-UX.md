# REPORT — FP-0002 Dashboard + Form Mail UX Maintenance

**Date:** 2026-08-20  
**Status:** **PASS**  
**Core deployed:** `0.3.23-p23`  
**Evidence:** `REPORTS/evidence/prod-maint-dashboard-mail-ux/`

---

## 1. Status

**PASS** — client-facing Dashboard footer polished; form notification emails are fully Russian and human-readable; SMTP/recipients/lead pipeline unchanged; indexing OPEN under P18G guard; source/production parity verified.

---

## 2. Current Production Truth

**CURRENT DASHBOARD + FORM EMAIL RUNTIME TRUTH VERIFIED**

| Area | Verified |
|------|----------|
| Dashboard widget | Compact P18J model; indexing OPEN; Overseo footer only |
| Form mail owner | `ConsultationHandler::attempt_outbound_mail()` → `FormLeadMailPresenter` |
| Active form key | `consultation` (only live type) |
| Recipients | From `MailOps::recipient_emails()` — unchanged |
| SMTP | Verified transport — not mutated |
| Lead order | validate → persist → mail attempt → response semantics |

Evidence: `03-dashboard-render.json`, `04-mail-fixtures-qa.json`, `02-deploy-manifest.json`

---

## 3. Dashboard

**DASHBOARD CLIENT UX FINAL PASS**

| Check | Result |
|-------|--------|
| MetaCODE support phrase removed | `has_metacode_support_footer: false` |
| Overseo attribution | `has_overseo: true`, link `https://overseo.ru/` |
| Compact chips / «Важно» | preserved |
| Indexing OPEN | `indexing_effective: OPEN`, `blog_public: 1` |
| Core version | `0.3.23-p23` |

Footer now shows only:

> Разработка: [Overseo](https://overseo.ru/)

Evidence HTML: `dashboard-dashboard-snippet.html`

---

## 4. Mail Before

Recipient-facing plain text (pre-P23) resembled debug output:

```
[Шпиговский дом] Заявка с сайта

Форма: consultation
Имя: …
Телефон: …
Email: —
Страница: …
Сообщение:
…
```

Problems: English machine key, weak hierarchy, em-dash placeholders, no localized subject pattern.

---

## 5. Mail After

Synthetic example (Case A — no email):

**Subject:** `[Шпиговский дом] Новая заявка — Консультация`

**Plain text:**

```
Новая заявка с сайта «Шпиговский дом»

Имя: Андрей ТЕСТ
Телефон: +7 (925) 111-22-33
Сообщение:
Нужна консультация по разводу.

Страница заявки:
https://shpigovsky.ru/uslugi/razvod/

Тип обращения: Консультация
Дата и время: 20.08.2026, 00:17

---
Сайт: shpigovsky.ru
```

HTML: simple inline card/table, escaped fields, optional `tel:` / `mailto:` links, plain `AltBody` via scoped `phpmailer_init`.

---

## 6. Form Type Localization

**MAIL RECIPIENT NEVER NEEDS TO INTERPRET INTERNAL FORM KEYS**

| Machine key | Russian label |
|-------------|---------------|
| `consultation` | Консультация |
| `callback` | Обратный звонок |
| `contact` | Обращение с сайта |
| `question` | Вопрос |
| `appointment` | Запись на консультацию |
| *(unknown)* | Обращение с сайта (fallback) |

Live production uses `consultation` only. Internal registry/logs retain machine keys.

Implementation: `src/Mail/FormTypeLabels.php` — presentation boundary only.

---

## 7. Mail QA

**RUSSIAN FORM EMAIL TEMPLATE PASS**

| Case | Scenario | Pass |
|------|----------|------|
| A | name + phone + message, no email | ✓ email row omitted |
| B | full fields + email | ✓ mailto link path |
| C | minimal valid | ✓ |
| D | multiline + `<script>` in message | ✓ escaped, no script in HTML |
| E | unknown machine key | ✓ fallback label, subject uses «Обращение с сайта» |
| F | special chars `& < >` | ✓ escaped in HTML |

All cases: `html_has_consultation_key: false`, `plain_has_consultation_key: false`.

Evidence: `04-mail-fixtures-qa.json`

No live SMTP test send required — remote presenter render QA sufficient.

---

## 8. Recipient Safety

**FORM EMAIL RECIPIENT ROUTING UNCHANGED**

- Still `MailOps::recipient_emails()` from form settings
- No substitution with WP administrators
- Distinction preserved: form lead recipients ≠ indexing alert admins

---

## 9. SMTP

**SMTP CONFIGURATION UNCHANGED**

- Transport, sender identity, auth — not modified
- Scoped HTML only for form notifications (`Content-Type: text/html` + `AltBody`)
- No global WordPress mail content-type drift

---

## 10. Lead Pipeline

**LEAD PERSISTENCE REMAINS INDEPENDENT OF MAIL PRESENTATION**

- Order unchanged: validate → persist lead → attempt mail → return semantics
- `MAIL_ACCEPTED` semantics unchanged
- Template refactor is presentation-only in `FormLeadMailPresenter`

---

## 11. Production Safety

- Indexing **OPEN** — human-approved
- P18G guard / watchdog — not weakened
- Privacy / consent / Metrika gating — untouched
- Editorial / Olya content — not modified
- robots — not closed

---

## 12. Evidence

| Artifact | Path |
|----------|------|
| Summary | `00-summary.json` |
| Deploy manifest + SHA parity | `02-deploy-manifest.json` |
| Dashboard render | `03-dashboard-render.json` |
| Mail fixtures A–F | `04-mail-fixtures-qa.json` |
| Dashboard HTML snippet | `dashboard-dashboard-snippet.html` |
| Runtime script | `_prod_maint_runtime.py` |

Synthetic/test values only — no real lead PII in Git.

---

## 13. Source / Production Parity

**SOURCE / PRODUCTION PARITY PASS**

6/6 deployed files — local SHA256 = production SHA256 (`parity_ok: true`).

---

## 14. Foreign WIP

**FOREIGN WIP PRESERVED**

Commit from clean worktree `worktrees/fp-0002-prod-maint-p23` on branch `fp-0002/prod-maint-dashboard-mail-ux`. Main workspace dirty tree not staged.

---

## 15. WP Forge Knowledge

Added / updated:

- **MAIL-UX-001–005** — `FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md` §14
- **ADMIN-UX** — client dashboard attribution: Overseo OK; avoid MetaCODE support marketing in widget footer
- **FP-0002-KNOWLEDGE-ASSIMILATION-INDEX.md** — P23 rows

---

## 16. Git

| Item | Value |
|------|-------|
| Branch | `fp-0002/prod-maint-dashboard-mail-ux` → merged to `mars/canonical-post-recovery` |
| Commit message | `FP-0002: polish dashboard attribution and form notification emails` |
| Push | authorized — see evidence git receipt after push |

---

## 17. Secret Scan

**SECRET / PRIVACY SCAN PASS**

- No SMTP passwords, tokens, or real lead PII in committed artifacts
- QA fixtures use `@example.invalid` and obvious TEST names
- Runtime script reads secrets from local path only (not committed)

---

## 18. Current State

**PRODUCTION / MAINTENANCE**

Site remains in post-launch maintenance — not a new launch wave.

---

## 19. Acceptance

**FP-0002 DASHBOARD + FORM MAIL UX MAINTENANCE COMPLETE** — THE CLIENT-FACING DASHBOARD REMAINS COMPACT AND USEFUL — THE METACODE SUPPORT PHRASE WAS REMOVED — OVERSEO DEVELOPMENT ATTRIBUTION REMAINS VISIBLE — FORM NOTIFICATION EMAILS ARE NOW FULLY HUMAN-READABLE AND RUSSIAN-LANGUAGE — INTERNAL MACHINE FORM KEYS ARE LOCALIZED AT THE PRESENTATION BOUNDARY — RECIPIENT ROUTING, SMTP, LEAD PERSISTENCE AND PRIVACY LOGIC REMAIN UNCHANGED — INDEXING REMAINS OPEN UNDER P18G SAFETY — SOURCE/PRODUCTION PARITY PASSES — FOREIGN WIP IS PRESERVED — CANONICAL REMOTE IS UPDATED.

---

## Files Changed

| File | Change |
|------|--------|
| `shpigovsky-core.php` | Version `0.3.23-p23` |
| `src/Admin/SystemDashboard.php` | Remove MetaCODE support footer; keep Overseo |
| `src/Forms/ConsultationHandler.php` | Use `FormLeadMailPresenter`; AltBody hook |
| `src/Admin/LeadsAdmin.php` | Delegate `form_label()` to `FormTypeLabels` |
| `src/Mail/FormTypeLabels.php` | **NEW** — localization map |
| `src/Mail/FormLeadMailPresenter.php` | **NEW** — HTML + plain templates |
| WP Forge standards + knowledge index | MAIL-UX + attribution rules |

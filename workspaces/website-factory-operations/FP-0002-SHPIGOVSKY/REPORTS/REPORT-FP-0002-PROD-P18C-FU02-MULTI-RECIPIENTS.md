# REPORT — FP-0002 PROD-P18C-FU02 Multiple Recipients

**Date:** 2026-08-19  
**Core:** `0.3.14-p18c-fu02`  
**Parity:** `8/8 SOURCE ↔ PRODUCTION MATCH`  
**Evidence:** `REPORTS/evidence/prod-p18c-fu02-multi-recipients/`

---

## 1. Status

**PASS**

## 2. Current Operator SMTP Settings

**CURRENT OPERATOR SMTP SETTINGS PRESERVED**

| Field | Value |
|-------|--------|
| Host | `smtp.beget.com` |
| Port | `465` |
| Encryption | `none` (stored value, not changed) |
| Auth | yes |
| Username | `noreply@shpigovsky.ru` |
| Password configured | **YES** |
| Sender email | `noreply@shpigovsky.ru` |
| Sender name | Шпиговский дом |
| Recipients | 1 — `client.leads@polygon-ws.ru` / MetaCODE |
| Metrika goal | empty (preserved) |
| Retention days | 0 (operator decision still required) |

Password never printed. Length-only at intake.

## 3. Recipient Owner

**RECIPIENT STORAGE OWNER IDENTIFIED**

`MailOps` option `fp02_mail_ops` → key `recipients`. Secret remains `fp02_mailbox_auth`. Not ACF.

## 4. Recipient Model

- `email` + `label` (`recipient_email` / `recipient_label` aliases accepted)
- First row = primary
- Additional rows = copies of the same `wp_mail()` operation
- Practical cap 20
- Case-insensitive dedupe, first label kept

## 5. Admin UX

**ADD RECIPIENT + REMOVE RECIPIENT AVAILABLE**

Настройки сайта → Почта и формы → Получатели: Email, Подпись, Удалить; **+ Добавить получателя**. No raw JSON.

## 6. Existing Data

**EXISTING RECIPIENT PRESERVED 1:1**

No schema swap. Idempotent normalize. Operator row unchanged after QA cleanup.

## 7. Secret Safety

**RECIPIENT EDITING CANNOT ERASE SMTP SECRET**

Blank password keeps the secret. Recipient save does not call password clear. Secret not in HTML/Dashboard/log/Git/report.

## 8. Validation

- trim + `is_email`
- blank rows dropped
- invalid non-empty emails rejected (list not saved)
- duplicates collapsed
- readiness requires ≥1 valid recipient + SMTP required fields + password

## 9. Mail Transport

`ConsultationHandler` passes `MailOps::recipient_emails()` as one `wp_mail($to, …)` array. One form submission = one lead record.

## 10. QA

**MULTI-RECIPIENT ADMIN SAVE/RELOAD PASS**

Cases 1–5 PASS. Temporary QA recipient removed.

## 11. SMTP State

- **CONFIGURED / NOT VERIFIED**
- Verification still pending
- Mail suppression **ON**

## 12. Dashboard

**SMTP CONFIGURED — VERIFICATION REQUIRED**

Recipient count only (no business emails). Indexing CLOSED.

## 13. Regression

- Form still renders on inner privacy
- Lead persist accepted; status `SMTP_PENDING` (complete + suppressed)
- Metrika goal unchanged (empty)
- UTM captured on QA then row deleted
- Indexing CLOSED

## 14. WP Forge Knowledge

**MULTI-RECIPIENT MAIL SETTINGS** — bounded repeating list; email + optional label; Add/Remove; server validation; dedupe; first = primary; readiness ≥1 recipient; recipient edits must not touch SMTP secret; one submission = one lead.

Anti-pattern **AP-030**.

## 15. Source / Production Parity

**8/8 MATCH**

## 16. Git

Isolated worktree from `origin/mars/canonical-post-recovery`. Dirty main foreign WIP untouched. Secret scan PASS. See `GIT-CHECKPOINT.json`.

## 17. Operator Next Action

1. Open **Настройки сайта → Почта и формы**
2. Add all required recipients (Add / Remove as needed)
3. Save
4. Do not open indexing
5. Report **SMTP SETTINGS SAVED / RECIPIENTS READY**

Next wave: **REAL SMTP VERIFICATION + FORM DELIVERY QA.**

## 18. Acceptance

**FP-0002 P18C-FU02 COMPLETE — SMTP / FORM SETTINGS NOW SUPPORT MULTIPLE ADMIN-MANAGED RECIPIENTS — ADD/REMOVE UX WORKS — EXISTING OPERATOR SETTINGS AND SMTP SECRET ARE PRESERVED — RECIPIENTS ARE VALIDATED AND DEDUPLICATED — ONE FORM SUBMISSION REMAINS ONE INTERNAL LEAD — MAIL SUPPRESSION REMAINS ACTIVE — SMTP VERIFICATION STILL REQUIRES A SEPARATE CONTROLLED TEST — INDEXING REMAINS CLOSED**

# REPORT — ISEO SALES MANAGER BOT PHASE 3D.1 REAL FORM PARSER REPAIR AND CLEAN LEAD ACCEPTANCE

**Date:** 2026-08-01  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdict

**PHASE 3D.1 COMPLETE — PARSER REPAIRED, NEW TEST PENDING**

Real website audit-form parser repaired and live; fixture suite green; stats/error lifecycle cleaned; Admin regression passed; readiness notice sent. Operator did not submit a new clean lead during the bounded observe window (0 lead chains). Contour remained healthy.

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Worktree | `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3d1-20260801-001347` @ `origin/mars/canonical-post-recovery` |
| Dirty main WIP | present (foreign) — **not mutated** |
| Named workflows | 4 (v1/v2 inactive; Operational+Admin active) |

## 3. Incident

Operator clean audit-form test produced Telegram card with empty client/contacts/site and quality «Недостаточно для связи», while source summary still contained labeled fields.

## 4. Real Form Forensic

Collapsed single-line body (`newline_count=0`) with labels `От кого` / `Способ связи` / `Контакт` / `Адрес сайта` / `Комментарий` and title `Заявка на бесплатный аудит`. Snippet used; no HTML in parser text. Evidence: `REAL-FORM-PARSER-FORENSIC-v1.md`.

## 5. Field Extraction Trace

All structured fields present in source; **none** parsed pre-fix; Deterministic → `quality=bad`; card dashes. No downstream erasure of good parses. Evidence: `FIELD-EXTRACTION-TRACE-v1.md`.

## 6. Root Cause

Operational `Parse Lead` was a passthrough stamp (`sm-parser-v3`) that never extracted Russian form labels from Gmail text/snippet.

## 7. Parser Repair

In-place Parse Lead → `sm-parser-v3.1` next-label delimited extraction; Deterministic service input includes `form_name`. Evidence: `AUDIT-FORM-PARSER-FIX-v1.md`.

## 8. Contact Normalization

Method-aware phone/email/Telegram/WhatsApp mapping; invalid placeholders rejected; phone formatting with `+`/spaces/parens/hyphens accepted. Evidence: `CONTACT-METHOD-NORMALIZATION-v1.md`.

## 9. Site and Service Parsing

Scheme optional; no DNS; `.example` allowed; audit title → Audit / Аудит.

## 10. Fixture Suite

F-AF01–F-AF12: **12/12 PASS**. Evidence: `PARSER-FIXTURE-ACCEPTANCE-v1.md`.

## 11. Live Patch

Temporary deactivate → PUT Operational + Admin → reactivate. Gates: ops active, admin active, v2 inactive, single intake, node count 34, **0** new workflows. Rollback not required.

## 12. New Clean Test

Readiness notice sent: «Парсер формы исправлен. Отправьте одну новую тестовую заявку…». Observe ~10 min: **0** leads.

## 13. End-to-End Execution

Pending operator submission. Empty polls healthy. Evidence: `CLEAN-LEAD-END-TO-END-v1.md`.

## 14. Telegram Card

Fresh acceptance pending. Pre-repair negative card documented. Evidence: `PRODUCTION-TELEGRAM-CARD-ACCEPTANCE-v1.md`.

## 15. Exactly-Once Regression

Idempotency nodes preserved; prior PROCESSED message not auto-replayed. Evidence: `EXACTLY-ONCE-REGRESSION-v1.md`.

## 16. Gmail Finalization

Policy unchanged (PROCESSED + incoming remove after Telegram success / idempotent skip). No new lead to re-verify.

## 17. AI OFF Evidence

`/ai_status`, `/config`, `/health`, `/status`: AI off; probe skipped. Observe OpenRouter executions: **0**.

## 18. Business Statistics

`/stats` unique-lead dedupe live. Example post-patch: Уникальных заявок **2**; Повторных обработок сообщений **23**; Технических повторных попыток **22**. Evidence: `BUSINESS-STATS-DEDUPLICATION-v1.md`.

## 19. Error Lifecycle

`/last_error`: «Активных рабочих ошибок нет.» + last resolved `telegram_delivery_failed`. `/status` no longer treats bare timestamp as active. Evidence: `ERROR-LIFECYCLE-ACCEPTANCE-v1.md`.

## 20. Admin Regression

All six commands authorized and answered. Evidence: `ADMIN-PRODUCTION-REGRESSION-v1.md`.

## 21. Final Workflow State

See `FINAL-PRODUCTION-STATE-v1.md`.

## 22. Workflow Count Gate

Named Sales/i-SEO workflows unchanged (4). **0** created.

## 23. Files Created

- `evidence/phase3d1/*` (13 evidence docs + fixture results)
- `implementation/parser-fixtures/parse-lead-lib.mjs`
- `implementation/parser-fixtures/run-fixture-suite.mjs`
- `reports/REPORT-iseo-sales-manager-bot-phase3d1-real-form-parser-and-clean-lead-v1.md`

## 24. Files Changed

- `README.md`, `OPERATIONAL-INDEX.md`
- `architecture/ADMIN-COMMAND-CONTRACT-v1.md`
- `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`
- `implementation/TEST-HARNESS-SPEC-v1.md`

## 25. Security Validation

No real phone/email/name/Gmail/Telegram/workbook IDs or credentials in committed evidence. Private Storage tooling retained out of git.

## 26. Git Isolation

Clean temporary worktree from `origin/mars/canonical-post-recovery`. Foreign WIP on main workspace untouched.

## 27. Commit

`fix(iseo-sales-manager-bot): parse real website form leads`

## 28. Push

Pushed without force: `52d77cea..f47b8587` → `origin/mars/canonical-post-recovery` (`f47b8587`).

## 29. Risks

- Clean lead still pending operator action.
- CONFIG sheet `parser_version` key may still display `sm-parser-v3` until manually updated; lead rows stamp `sm-parser-v3.1`.
- Cards-delivered metric approximates unique CLEAN identities (not historical TG flood send count).

## 30. SAFE UNKNOWN

Whether operator will submit the new test within a later window; exact CONFIG sheet cell update for `parser_version` display.

## 31. Remaining Operator Actions

1. Submit **one** new website audit test (name + valid contact + site + audit request).  
2. Confirm single Telegram card shape.  
3. Optional: set CONFIG `parser_version=sm-parser-v3.1` for `/config` display parity.

## 32. Recommended Next Phase

**PHASE 3D.2 — OLYA LIVE HANDOFF AND PRODUCTION CLOSEOUT** (after clean lead acceptance).

## 33. Production Boundary

| Item | Value |
|------|-------|
| old workflow active | false |
| Operational active | true |
| Admin active | true |
| active Gmail intake count | 1 |
| fresh clean leads processed | 0 (pending) |
| Telegram production cards (new) | 0 |
| duplicate cards (observe) | 0 |
| Gmail label changes (new lead) | n/a |
| automatic client messages | 0 |
| AI provider calls | 0 |
| new workflows | 0 |
| rollback | no |

## 34. Stop Condition

Phase stops pending operator new clean lead. Do not enable AI. Do not reactivate Sales-Manager-v2. Do not create workflows. Do not automatically contact clients.

# REPORT — ISEO SALES MANAGER BOT PHASE 3H PRODUCTION HARDENING, OLYA ONBOARDING, REMINDERS ACTIVATION AND PRE-AI SOAK

## 1. Verdict

`PHASE 3H IMPLEMENTATION COMPLETE — 48-HOUR SOAK STARTED`

Soak start: **06.08.2026 14:20 МСК**. Earliest valid PASS: **08.08.2026 14:20 МСК**. Do not use soak-passed verdict yet.

## 2. Operator-approved program

Operator approved Phases 3H.1–3H.3 + backup + multi-day soak; **not** Phase 3I.1. AI remains OFF.

## 3. Starting contour

Ops `xSnXPy8cEHoZw6xG` active 45 · Admin `wLrLp4WQHm1VJmxz` active 85 · v2 inactive · sole Gmail fetch · AI OFF · reminders OFF · recipients 2 · Olya revoked · reporting display «выключена».

## 4. Pre-change backup

Storage: `git-sync-iseo-sm-phase3h-20260806-175957/runtime/backups/pre-hardening/` (+ forensic dumps). Sanitized manifests in evidence.

## 5. Starting counters

LEADS=1 · pending=0 · processed=1 · spam=0 · reporting Лиды=1 · TEST_LEADS=2 · staff profiles=4 · AI=false · reminders=false.

## 6. Test fixture inventory

See `evidence/phase3h1/TEST-FIXTURE-INVENTORY-v1.md`.

## 7. Test cleanup

TEST_LEADS→0 · REMINDER_DELIVERIES/RECIPIENT_REPLIES schemas repaired · production LEADS untouched.

## 8. Production contamination check

PASS — production LEADS/reporting remain CLIENT_A only.

## 9. Reporting architecture

**MANUAL** — workbook exists; no live continuous sync nodes on Ops/Admin.

## 10. Reporting proof

Model A PASS — no automatic production reporting inserts from this wave.

## 11. Reporting final state

manual · tests excluded · archive excluded.

## 12. Config reporting text

`Синхронизация отчётности: только вручную` (+ exclusions lines).

## 13. Phase 3H.1 verdict

`PHASE 3H.1 COMPLETE — CLEANUP AND REPORTING TRUTH READY`

## 14. Olya identity

Profile №2 · Ola4seo · Оля · unique binding · pre-state revoked.

## 15. Olya access restore

revoked→active · personalization enabled · company INTLSEO · actor ADMIN_A · PROFILE_EVENTS recorded.

## 16. Olya reply profile

Оля enabled active receives cards.

## 17. Olya command acceptance

Sheets+delivery binding PASS; Telegram command visuals **OPERATOR PENDING**.

## 18. Olya work guide

`guides/OLYA-LEAD-WORK-GUIDE-v1.md` refreshed.

## 19. Three-recipient delivery

Telegram successes=3 · names Андрей/Оля/Михаил · Никита=0 · LEADS writes=0.

## 20. Personalized names

Intros PASS; Мопс in client copy=0.

## 21. Olya processed callback

OPERATOR VISUAL PENDING (isolated).

## 22. Olya spam callback

OPERATOR VISUAL PENDING (isolated).

## 23. Phase 3H.2 verdict

`PHASE 3H.2 COMPLETE — OLYA ONBOARDED AND THREE-RECIPIENT DELIVERY READY`

## 24. Reminder engine forensic

Admin schedule path; source corrected **LEADS**; ledger REMINDER_DELIVERIES.

## 25. Reminder configuration

enabled=true · 10:00 · Europe/Moscow · min=1 · tests/archive excluded · active-only · once/date.

## 26. Controlled reminder proof

Zero-pending live safety PASS; multi-send drill deferred until pending≥1 (correct fail-closed).

## 27. Exactly-once proof

Contract+ledger headers ready; empty baseline ledger.

## 28. Partial failure behavior

Per-recipient claim independence (contract retained).

## 29. Zero-pending suppression

pending=0 at activation → expected sends=0. PASS.

## 30. Production reminder activation

CONFIG `pending_reminders_enabled=true` applied; Admin restored active 85.

## 31. Phase 3H.3 verdict

`PHASE 3H.3 COMPLETE — DAILY PENDING REMINDERS ACTIVE`

## 32. Full pre-AI harness

Cleanup/reporting/Olya/3-recipient/reminder-enable/zero-pending/AI-OFF/contour PASS. Operator Telegram callback matrix pending. Controlled 3-send reminder observation scheduled in soak.

## 33. Post-hardening backup

`runtime/backups/post-hardening/` — Admin/Ops/v2 raw.

## 34. Immutable production baseline

`product/PRODUCTION-BASELINE-PRE-AI-SOAK-v1.md`

## 35. Soak plan

`guides/PRE-AI-SOAK-RUNBOOK-v1.md` · evidence/pre-ai-soak.

## 36. Soak start

06.08.2026 14:20 МСК / 2026-08-06T11:20:00.000Z

## 37. Earliest valid soak completion

08.08.2026 14:20 МСК

## 38. Operator checklist

See soak runbook + T0 checkpoint.

## 39. Final profiles

1 Андрей enabled · 2 Оля enabled · 3 Михаил enabled · 4 Никита revoked

## 40. Final access state

active recipients=3 · revoked=1

## 41. Final workflow state

Ops active 45 · Admin active 85 · v2 inactive · workflows created=0

## 42. Final reporting state

manual / только вручную

## 43. Final reminder state

ON · 10:00 Europe/Moscow · source LEADS

## 44. Final AI state

OFF · OpenRouter calls=0

## 45. Production statistics

received=1 · pending=0 · processed=1 · spam=0 (unless genuine arrival)

## 46. Safety counters

| Counter | Value |
|---|---:|
| production test rows after cleanup | 0 |
| three-recipient Telegram successes | 3 |
| duplicate deliveries | 0 |
| revoked deliveries | 0 |
| reminder enabled | true |
| AI | OFF |
| customer auto-messages | 0 |
| workflows created | 0 |
| access changes | 1 (Olya restore) |
| profile wipes | 0 |
| production leads lost/duplicated | 0/0 |
| Phase 3I.1 started | false |

## 47. Files created

architecture/REPORTING-SYNC-CONTRACT-v1.md · THREE-RECIPIENT-DELIVERY-CONTRACT-v1.md · DAILY-PENDING-REMINDER-CONTRACT-v1.md · implementation/TEST-FIXTURE-CLEANUP-v1.md · OLYA-ONBOARDING-v1.md · REMINDER-EXACTLY-ONCE-v1.md · guides/PRE-AI-SOAK-RUNBOOK-v1.md · product/PRODUCTION-BASELINE-PRE-AI-SOAK-v1.md · evidence/phase3h1|2|3/** · evidence/pre-ai-soak/** · this report

## 48. Files changed

OPERATIONAL-INDEX.md · CURRENT-PRODUCTION-BASELINE-v1.md · PRODUCT-ROADMAP-v1.md · guides/OLYA-LEAD-WORK-GUIDE-v1.md · live Admin Config Summary + Reminder source sheet (not committed raw)

## 49. Security validation

No Telegram IDs, workbook IDs, emails, phones, raw payloads, or unsanitized exports in Git evidence. Secrets remain under Storage `private/`.

## 50. Commits

1. `5f41e82c` — `fix(iseo-sales-manager-bot): clean test fixtures and align reporting state`
2. `455bb210` — `feat(iseo-sales-manager-bot): onboard Olya as active moderator`
3. `7689998e` — `feat(iseo-sales-manager-bot): activate exactly-once pending reminders`
4. `5b26ad3d` — `docs(iseo-sales-manager-bot): establish pre-ai production soak baseline`

## 51. Push

`origin/mars/canonical-post-recovery` tip `5b26ad3d` (fast-forward from `d76a68f7`).

## 52. Risks

- Operator Telegram command/callback visuals still pending
- First multi-send reminder day not yet observed (pending=0)
- Legacy synthetic rows remain in lead_clean_v2 (excluded from reminder source)

## 53. SAFE UNKNOWN

Exact Sheets quota error counts last 24h (API listing not fully enumerated this wave).

## 54. Remaining operator actions

1. Olya: /start /my_status /my_reply_profile /help /pending_* /leads /reminder_status  
2. Confirm /config reporting + reminder lines as Admin  
3. Run soak checkpoints; do not start 3I.1  

## 55. Phase 3I.1 gate

Blocked until soak PASS + explicit approval. AI stays OFF.

## 56. Stop condition

Stop after 3H.1–3H.3 + backup + soak start recorded + 3I.1 not started — **met**.

# REPORT — ISEO SALES MANAGER BOT PHASE 3E.2.1 DELIVERY RECONCILIATION AND HUMAN REPLY STYLE V1

## 1. Verdict

`COMPLETE — DELIVERY SAFE; HUMAN COPY ACCEPTANCE PENDING`

Duplicate-delivery root cause repaired; affected H reconciled; Human Reply Style v1 live; harness 64/64 PASS. Operator visual acceptance of human drafts and post-quota dual-card live proof remain open.

## 2. Operator-approved scope

Process-line **ISEO-SALES-MANAGER-BOT — PHASE 3E.2.1 DELIVERY RECONCILIATION AND HUMAN REPLY STYLE V1** under `projects/iseo-sales-manager-bot/`. Contour: Operational.dev sole intake; Admin.dev active; Sales-Manager-v2 inactive; AI OFF; no role restores; no reminders; no new workflows.

## 3. Production containment

Operational.dev deactivated while fixture H loop risk was live; Admin.dev kept active; Sales-Manager-v2 inactive; no alternate Gmail intake; no Telegram card deletes; ACCESS_CONTROL unchanged. After patch + H reconcile, Operational.dev reactivated (45 nodes, Schedule enabled, sole Gmail fetch).

## 4. Fixture H duplicate incident

Marker `ISEO_SM_FR2_H_PROBABLE_TEST`: semantic suppression correct; same stable lead resent ~4 waves (~00:04–00:13 UTC). Evidence: `evidence/phase3e2-1/FIXTURE-H-DUPLICATE-INCIDENT-v1.md`.

## 5. Exact duplicate counts

| Metric | Count |
|--------|------:|
| Send waves | 4 |
| Estimated duplicate cards | **8** |
| Delivery keys reconciled | 8 |
| New marker `PHASE_3E2_1_H_TEST_NO_DUPLICATE` resends across ≥5 polls | **0** |

## 6. Root cause

Telegram success → Sheets quota on claim/stamp/events → fake-claimed via claim `continueRegularOutput` → no durable delivered / no CONFIG guard → next poll blind resend. Rate-limit is **not** an acceptable resend reason. See `LEDGER-RATE-LIMIT-ROOT-CAUSE-v1.md`.

## 7. Ledger read boundary

Fail-closed: quota/error/unknown read → zero sends; states `ledger_read_ok` / `ledger_read_error` / `reconciliation_required`; Sheets error objects not treated as empty ledger. Live claim quota → `sendOk=0`.

## 8. Claim-before-send hardening

Claim upsert fails closed before send; Restore blocks unpersisted claims; delivery key preserved; stamp failure → reconcile, no blind resend; LEAD_EVENTS continue-on-error so finalize/CONFIG can proceed.

## 9. Reconciliation behavior

`delivered` terminal; `claimed`/`uncertain` reconcile not blind-send; per-recipient CONFIG `tg_delivered:*` secondary guard; one moderator failure does not resend Admin.

## 10. Affected H cleanup

H only: guards written; further eligibility blocked; cards not deleted; A–G/real leads untouched. Receipt: `AFFECTED-H-RECONCILIATION-v1.md`.

## 11. First Reply v2 baseline

Extended to `sm-reply-v2.1` atop Parser 3.3 / prior v2 engine fields (additive).

## 12. Human Reply Style v1

`human_reply_style_version=sm-human-v1.0` — natural manager Russian; silent known-info guard; architecture `HUMAN-REPLY-STYLE-v1.md`.

## 13. Forbidden system phrases

Deterministic check; live drafts 1–4 forbidden=false; harness H26–H28 PASS.

## 14. Meaningful-comment branching

Themes drive reply content; cart comment → `conversion_cart` questions (not generic audit).

## 15. Cart/conversion reply

Live draft acknowledges cart/conversion; asks when/changes/analytics; no priority-page/result re-asks. See `CART-CONVERSION-REPLY-v1.md`.

## 16. Website-development reply

Natural business/purpose/examples questions; no «сайт не указан / ожидаемо» narration.

## 17. Website-development + SEO reply

Acknowledges both tasks; asks business/functions/region; no internal stage narration.

## 18. SEO reply

Harness/natural SEO template without known-site explanation (targeted live set focused on B/C/D/G/H).

## 19. Alternative-contact reply

HITL wording preserved (manager draft; no auto Telegram promise). Harness H20 PASS.

## 20. Damaged-contact UX

`ready=false`; warn×1; no copy; missing `контакт, фокус аудита` (not bare `задача`).

## 21. Missing-information refinement

Service-known vs detail-missing labels separated (audit → фокус аудита).

## 22. Test suppression

Preserved; new H marker suppressed; no customer draft.

## 23. Quality linter

Deterministic readiness gate; harness H40 PASS.

## 24. Storage migration

Additive fields only; no historical reply regen; schema backup before live patch; Admin unchanged (archive compatibility not requiring Admin patch).

## 25. Harness

`phase3e21-harness.mjs` → **64/64 PASS** (`evidence/phase3e2-1/HARNESS-RESULTS-v1.md`).

## 26. Live fixture 1

`PHASE_3E2_1_B_CART_CONVERSION_HUMAN` — reply quality PASS; `sendOk=0` (Sheets claim quota fail-closed).

## 27. Live fixture 2

`PHASE_3E2_1_C_WEBDEV_HUMAN` — reply quality PASS; `sendOk=0` (quota).

## 28. Live fixture 3

`PHASE_3E2_1_D_WEBDEV_SEO_HUMAN` — reply quality PASS; `sendOk=0` (quota).

## 29. Live fixture 4

`PHASE_3E2_1_G_DAMAGED_CONTACT_UX` — UX PASS; `sendOk=0` (quota).

## 30. Live fixture 5

`PHASE_3E2_1_H_TEST_NO_DUPLICATE` — suppressed; ≥5 polls; `duplicateResends=0`; dual successful send under quota **not proven** (fail-closed zero send).

## 31. Operator human-copy acceptance

Packet prepared in `TARGETED-LIVE-ACCEPTANCE-v1.md`. **Visual acceptance PENDING** from operator (Оля-as-judge questions).

## 32. Delivery regression

Historical H storm stopped; fail-closed proven live under quota; dual-card happy-path live proof deferred to Sheets recovery.

## 33. Lifecycle regression

Buttons / callbacks / actor attribution / Admin commands unchanged (harness R45–R51).

## 34. Final access state

Андрей admin/active; Мопс moderator/active; Оля/Никита revoked — **unchanged** (access-role changes=0).

## 35. Final workflow state

Ops active 45; Admin active 59; v2 inactive; AI OFF; sole Gmail intake; Schedule enabled. `FINAL-WORKFLOW-STATE-v1.md`.

## 36. Safety counters

| Counter | Value |
|---------|------:|
| duplicate cards for new H fixture | 0 |
| AI provider calls | 0 |
| automatic client messages | 0 |
| workflows created | 0 |
| access-role changes | 0 |
| reminder implementation changes | 0 |
| historical reply regenerations | 0 |
| real-client tests | 0 |
| destructive Git operations | 0 |

## 37. Files created

Architecture: `HUMAN-REPLY-STYLE-v1.md`, `MEANINGFUL-COMMENT-BRANCHING-v1.md`, `FIRST-REPLY-QUALITY-LINTER-v1.md`, `DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md`.  
Evidence pack under `evidence/phase3e2-1/` (incident, matrix, root cause, fail-closed, claim, H reconcile, style, forbidden, branching, cart, damaged UX, linter, live acceptance, no-dup H, harness, final state, receipt).  
Runtime/harness updates under `implementation/`.  
This report.

## 38. Files changed

README / OPERATIONAL-INDEX / product baseline+architecture+limitations+roadmap / First Reply engine+rules+guard / Manager card / guides / patch+sheets+harness specs / runtime libs (`first-reply-engine-v2`, `processor-lib`, `formatter-lib`, parse-lead).

## 39. Security validation

No secrets, raw Telegram/chat IDs, workbook IDs, raw emails, screenshots, or unsanitized workflow exports committed. Synthetic names/markers only in evidence. Foreign WIP on main workspace untouched.

## 40. Commit

`6364b5fc` — `fix(iseo-sales-manager-bot): harden delivery and humanize first replies`  
(clean worktree detached at prior tip `76507b81`; selective paths under `projects/iseo-sales-manager-bot/**`; Phase 3E.2 implementation ancestor `01a65015` present).

## 41. Push

Pushed without force: `76507b81..6364b5fc` → `origin/mars/canonical-post-recovery`.

## 42. Risks

- Sheets quota can still block claim+send (correctly fail-closed) — managers may miss new cards until API recovers.
- Dual-recipient live happy path for 3E.2.1 fixtures not yet operator-visible.
- Google Sheets lacks atomic CAS — residual race theoretically possible under extreme concurrency (mitigated, not eliminated).

## 43. SAFE UNKNOWN

- Exact CLEAN/RAW row counts for every synthetic inject under quota noise without full Sheets dump.
- Whether early incomplete live waves left partial Telegram cards for markers before human patch fully matched (later retries fail-closed).
- Post-recovery dual-card sendOk=2 for fixtures 1–4 until re-run.

## 44. Remaining operator actions

1. Visually accept human drafts in the acceptance packet (Оля criteria).
2. After Sheets quota recovers, re-prove one paced dual-card delivery (or authorize re-run of 1–5 with ≥60s pacing).
3. Confirm no further duplicate cards for reconciled H markers.
4. Do not restore Olya/Nikita / enable AI / activate v2 / implement reminders without new charter.

## 45. Stop condition

Stopped after: delivery root cause repaired; H reconciled; Human Reply Style v1 implemented; meaningful branching live; damaged UX fixed; harness PASS; five fixtures processed; new H no-resend observed; acceptance packet prepared; docs/evidence/report; commit/push from clean worktree. **Not** claiming `PHASE 3E.2 COMPLETE — HUMAN FIRST REPLY ENGINE READY` until operator visual OK + dual-card proof.

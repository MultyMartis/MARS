# REPORT — ISEO SALES MANAGER BOT PHASE 3E.2 CONTEXT-AWARE FIRST REPLY ENGINE AND MANAGER CARD POLISH

## 1. Verdict

`COMPLETE — REPLY ENGINE READY; OPERATOR COPY ACCEPTANCE PENDING`

## 2. Operator-approved scope

Operator approved beginning the dedicated first-reply and Telegram-card refinement phase after Phase 3E.1 visual acceptance of Parser 3.3 fixtures A–F.

## 3. Phase 3E.1 closeout

Formal closeout recorded in `evidence/phase3e2/PHASE3E1-LIVE-CLOSEOUT-v1.md` and `evidence/phase3e1/PHASE3E1-ACCEPTANCE-RECEIPT-v1.md`.

**Verdict:** `PHASE 3E.1 COMPLETE — PARSER 3.3 AND LEAD SEMANTIC MODEL READY`

Operator visual A–F PASS; site states / alt contact / name / one-line / service / test badge PASS; two-recipient delivery PASS; duplicate deliveries=0; buttons present; AI=0; client messages=0. Parser 3.3 behavior not redesigned during closeout (only a probable-test false-positive fix for substring «тест» inside «проверить»).

## 4. Environment

| Item | Value |
|------|-------|
| Workspace / volume | `X:\AI MARS` / `AI WS` |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3e2-*\repo` |
| Base | `origin/mars/canonical-post-recovery` @ `301e7970` |
| n8n host | `n8n.ai-metacode.com` |

## 5. Canonical baseline

- Phase 3E.1 implementation commit `8cf81b41` is ancestor of origin tip.
- Phase 3E.1 fixture evidence commit `47cda75c` is ancestor of origin tip.

## 6. First Reply v1 baseline

Legacy `buildFirstReplyDraft` templates (`sm-reply-v1.x`) were service-branch stubs with limited acknowledgment and weak structured suppression. Documented in `evidence/phase3e2/FIRST-REPLY-V1-BASELINE-v1.md`.

## 7. First Reply v2 architecture

Deterministic engine `implementation/runtime-libs/first-reply-engine-v2.mjs` (`sm-reply-v2.0`):

- greeting rules  
- service-specific acknowledgment + ≤3 question groups  
- known-information guard with reason codes  
- test / damaged-contact suppression modes  
- length safety + unsupported-promise scrub  
- wired through Parse Lead + Deterministic Lead Processor; card via formatter `sm-msg-v2.4`

## 8. Input semantic fields

Uses Lead Semantic Model v1 fields: name, contacts, website_state/normalized, alternative contact, comment, explicit intent, resolved/secondary service, request summary, quality, missing information, probable-test, source topic.

## 9. Output data contract

`first_reply_version`, `first_reply_mode`, `first_reply_subject`, `first_reply_text`, `first_reply_questions`, `first_reply_reason_codes`, `first_reply_omitted_reason`, `first_reply_ready`, `first_reply_warnings` + compat `first_reply_source` / `reply_template_version`.

## 10. Known-information guard

Active. Suppresses re-asks for known website URL, absent-site URL asks, phone, email, Telegram, generic task, known service/region. Codes stored in `first_reply_reason_codes`.

## 11. Greeting behavior

`Здравствуйте, <Имя>!` when usable; else `Здравствуйте!`. Placeholder/corrupt names skipped. Probable-test drafts suppressed entirely.

## 12–18. Service replies

Audit / SEO / Website Development / Website Development + SEO / AI Search·GEO / Direct·PPC / NeedsClarification implemented as composable deterministic blocks (matrix in evidence). No pricing/ranking/AI-inclusion guarantees.

## 19. Alternative contacts

Rendered as Telegram/WhatsApp/Другой контакт; never under Сайт. Reply may acknowledge Telegram preference without re-asking username.

## 20. Probable test suppression

`test_suppressed`; card text without copy block; not spam; name preserved.

## 21. Damaged-contact boundary

`contact_suppressed`; manager warning; no ready draft.

## 22. Copy-block UX

Heading + escaped `<pre>`; disclaimer outside. Suppressed drafts omit copy block.

## 23. Manager card v2.4

`sm-msg-v2.4` sections omit empties; buttons unchanged; test badge only for `is_probable_test`.

## 24. Storage migration

Additive plan for first_reply_* columns; interim `quality_comment` carrier; no historical bulk regen. Spec updated.

## 25. Historical compatibility

Archive uses stored `first_reply_text`; legacy drafts not fabricated into v2.

## 26. Template matrix

16 cases documented in `evidence/phase3e2/SERVICE-TEMPLATE-MATRIX-v1.md`.

## 27. Harness

`implementation/harness/phase3e2-harness.mjs` — **59/59 PASS**. Evidence under `evidence/phase3e2/HARNESS-RESULTS-*`.

## 28–35. Live cases A–H

Paced synthetic fixtures (see `evidence/phase3e2/LIVE-FIRST-REPLY-ACCEPTANCE-v1.md`):

| Case | Result |
|------|--------|
| A Audit vague + site | PASS — reply ready, no site re-ask, sendOk=2 |
| B Audit meaningful + site | PASS |
| C Website Development + absent | PASS |
| D Website Development + SEO + absent | PASS |
| E SEO + site | PASS |
| F Telegram alt + vague | PASS |
| G Damaged contact | PASS — suppressed |
| H Probable test | PASS reply suppression + sendOk=2; LEAD_DELIVERIES rate-limited |

## 36. Operator copy acceptance

**PENDING** — comparison packet prepared; do not claim final COMPLETE until operator confirms natural copy / no known re-asks / convenience.

## 37. Delivery regression

A–G: RAW=1, CLEAN=1, LEAD_DELIVERIES=2, sendOk=2, dup=0 each. Exactly one Gmail intake preserved. H Telegram delivered; ledger append rate-limited after wave.

## 38. Lifecycle regression

Buttons `✅ Обработано` / `🚫 Спам` unchanged; callback prefixes unchanged; Admin actor path untouched.

## 39. Final access state

Андрей=admin/active; Мопс=moderator/active; Оля/Никита=revoked — unchanged.

## 40. Final workflow state

See `evidence/phase3e2/FINAL-WORKFLOW-STATE-v1.md`. Ops 45 active; Admin 59 active; Sales-Manager-v2 inactive.

## 41. Safety counters

- AI provider calls=0  
- automatic client messages=0  
- workflows created=0  
- access changes=0  
- reminder implementation changes=0  
- historical bulk reply regeneration=0  
- real-client test messages=0  
- duplicate lead deliveries=0 (accepted A–G)

## 42. Files created

- `architecture/FIRST-REPLY-ENGINE-v2.md`
- `architecture/KNOWN-INFORMATION-GUARD-v1.md`
- `architecture/MANAGER-CARD-v2.4-CONTRACT-v1.md`
- `implementation/runtime-libs/first-reply-engine-v2.mjs`
- `implementation/harness/phase3e2-harness.mjs`
- `evidence/phase3e2/*` (closeout, contracts, harness, live acceptance, receipt)
- this report

## 43. Files changed

- `parse-lead-lib.mjs`, `processor-lib.mjs`, `formatter-lib.mjs`
- README / OPERATIONAL-INDEX / product docs / roadmap / FIRST-REPLY-RULES / TELEGRAM-UX / SHEETS / OPS patch / TEST-HARNESS / OPERATOR-RUNBOOK
- Phase 3E.1 acceptance receipt (closeout)

## 44. Security validation

No PII/secrets/Telegram IDs/workbook IDs/raw emails committed. Live private tooling remains under `X:\AI MARS STORAGE\incoming\...` (not staged).

## 45. Commit

`01a65015` — `feat(iseo-sales-manager-bot): add context-aware first reply engine`

## 46. Push

Pushed without force to `origin/mars/canonical-post-recovery` (`301e7970..01a65015`).

## 47. Risks

- Sheets rate-limits under paced multi-fixture waves (H ledger append).  
- Synthetic Gmail label nodes may error while Telegram/RAW/CLEAN succeed.  
- Operator copy acceptance still required.

## 48. SAFE UNKNOWN

Exact Sheets header apply timing for additive first_reply_* columns until operator runs header migration. Admin `/leads` visual for brand-new v2 fields not re-proven beyond stored-text compatibility.

## 49. Remaining operator actions

1. Visually accept live A–H reply copy packet.  
2. Optionally append CLEAN headers for first_reply_* fields.  
3. Charter pending-lead reminders after copy acceptance.

## 50. Stop condition

Phase 3E.1 closed; First Reply Engine v2 implemented and live-patched; known-information guard active; card v2.4; additive migration documented; harness PASS; paced live fixtures delivered; operator comparison prepared; commit/push performed. Reminders not implemented. AI OFF. Sales-Manager-v2 inactive. Roles unchanged.

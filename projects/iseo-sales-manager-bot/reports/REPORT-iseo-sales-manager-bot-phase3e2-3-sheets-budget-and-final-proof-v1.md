# REPORT — ISEO SALES MANAGER BOT PHASE 3E.2.3 SHEETS CALL-BUDGET OPTIMIZATION AND FINAL EXACTLY-ONCE PROOF

## 1. Verdict

`COMPLETE — EXACTLY-ONCE PROOF DELIVERED; OPERATOR VISUAL CONFIRMATION PENDING`

Sheets request amplification was reduced, final dual-recipient delivery succeeded exactly once, and five later polls produced zero resends. Human Reply Style remains operator-accepted. The only remaining acceptance gate is operator visual confirmation of the sanitized final proof card.

## 2. Operator-approved scope

Phase 3E.2.3 closeout is limited to `projects/iseo-sales-manager-bot/**`: Sheets call-budget, single-flight, bounded retry/read contracts, final exactly-once proof, evidence, status docs and this report. No AI activation, access change, reminder implementation, new workflow, client auto-message or rollback-workflow activation was authorized.

## 3. Quiet window

Operational.dev was inactive from `2026-08-05T10:34:01Z` for more than 60 minutes before scheduled empty-poll observation and final proof. Admin.dev remained unchanged; the rollback workflow remained inactive.

## 4. Patch deployment

The patch was applied in place to the existing Operational.dev contour. Node count remained 45. AI remained OFF. Access state remained unchanged.

## 5. Schedule correction

The attempted n8n parameter `secondsInterval=120` was rejected with `Invalid interval`. The final valid schedule is:

`minutesInterval=2`

This is the only schedule form documented as active for Phase 3E.2.3.

## 6. Request-amplification root cause

The continuous background floor came from empty polls writing `last_poll_success_at` to CONFIG every ~30 seconds. Full delivery then added broad CONFIG, DEDUP_INDEX, LEAD_DELIVERIES and ACCESS_CONTROL reads before quota-sensitive claim writes. Success handling added multiple CONFIG guards. No workflow single-flight lock existed, and Normalize CONFIG did not preserve delivery guard namespaces.

## 7. BEFORE Sheets budget

| Metric | BEFORE |
|---|---:|
| Empty-poll CONFIG writes | 1 per ~30 seconds |
| Estimated empty-poll writes/hour | ~120 |
| Full-path Sheets floor before quota point | approximately 7–8 node operations |
| LEAD_DELIVERIES returned items | roughly 52 full-tab items |
| Dual-card proof sends in 3E.2.2 | 0, fail-closed under quota |

## 8. Empty-poll AFTER proof

Scheduled execution references `23184`, `23185`, `23186` each followed:

`Schedule → Gmail → Intake Gate → Switch → Update Runtime State`

`Apply Runtime State CONFIG` did not run. Each poll had `sheetsRequestFloor=0` and quota=0. AFTER empty-poll Sheets write rate is 0/hour.

## 9. Single-flight guard

Intake Gate uses workflow static data with a 4-minute TTL. Offline overlap checks passed. No live overlap incident was observed. This guard reduces poll overlap but does not replace claim-before-send or create a distributed transaction.

## 10. Backoff and retry

Bounded policy remains:

- LEAD_DELIVERIES read: maximum 3 attempts, 30-second delay;
- ACCESS_CONTROL read: maximum 3 attempts, 30-second delay, fail closed;
- claim upsert: maximum 3 attempts, 30-second delay, fail closed.

The final proof succeeded without a Sheets quota retry exhaustion.

## 11. CONFIG snapshot

CONFIG was read exactly once. Normalize CONFIG preserved `tg_delivered:*` and `tg_attempts:*`. Expand reused the existing snapshot; it did not perform an additional fallback Sheets read.

## 12. ACCESS_CONTROL snapshot

ACCESS_CONTROL was read exactly once. Recipient expansion produced exactly two eligible roles: one admin and one moderator. Revoked entries were excluded; there was no third recipient.

## 13. Bounded delivery-ledger read

LEAD_DELIVERIES was read once with the stable-lead filter and returned **1 item**, compared with roughly 52 items on the prior full-tab path. `alwaysOutputData` and bounded retry remained configured.

## 14. Final proof fixture

Proof marker: `PHASE_3E2_3_FINAL_EXACTLY_ONCE_PROOF`.  
Proof execution reference: `23188`.

The fixture used a synthetic contact and a reserved proof domain. No real client or production contact data was used.

## 15. Semantic result

| Field | Value |
|---|---|
| `website_state` | `provided` |
| `resolved_service` | `SEO` |
| `meaningful_theme` | `traffic_decline` |
| `is_probable_test` | `false` |
| `first_reply_ready` | `true` |
| Human style | `sm-human-v1.0` |

## 16. Exact sanitized reply draft

```text
Здравствуйте, Synth Final Proof!

Спасибо за заявку по SEO для сайта <SITE>.
Поняли, что вас беспокоит снижение поискового трафика.

Подскажите, пожалуйста:
1) Когда вносились изменения и что именно обновляли?
2) Какие разделы или направления потеряли больше всего трафика?
3) Есть ли доступ к Метрике и Search Console, чтобы сравнить показатели до и после изменений?

С уважением,
команда i-SEO
```

The draft contains no internal marker and does not ask for the known site again.

## 17. Human-copy validation

The draft acknowledges the SEO request and traffic decline, asks about timing/changes, affected sections and analytics access, and contains no parser narration or unsupported promise. Copy block present; warning count=0.

## 18. RAW evidence

Proof RAW rows: **1**.

## 19. CLEAN evidence

Proof CLEAN rows: **1**.

## 20. Claim evidence

Recipient claim items: **2**. Both claim writes succeeded before Telegram send.

## 21. Telegram send evidence

Recipient expansion: **2**. Telegram attempts: **2**. Successful sends: **2**. No revoked or third recipient was included.

## 22. Delivered-stamp evidence

Delivered stamps: **2**. Delivery ledger persistence completed for both recipient copies.

## 23. Synthetic Gmail finalization error

The proof execution ended with workflow status `error` only because `Add Gmail PROCESSED` received a fake synthetic Gmail message reference. This was a bad-request response, not a Sheets quota failure. Both Telegram sends and both delivered stamps had already succeeded.

## 24. Gmail continuation patch

Gmail finalization nodes were patched to continue regular output for this synthetic failure boundary, so downstream runtime guard handling is not silently skipped by a non-Sheets test artifact.

## 25. CONFIG guard reconciliation

The proof execution initially wrote 0 CONFIG fallback guards because Runtime State was not reached after the synthetic Gmail error. A Sheets-only reconciliation then wrote exactly **2** recipient-level `tg_delivered` guards. No Telegram resend occurred.

## 26. Five-poll zero-resend proof

Five later scheduled polls each had:

- extra expansions: 0;
- extra sends: 0;
- duplicate resends: 0.

Aggregate `duplicateResends=0`, `laterPollSends=0`.

## 27. Pending real-lead safety

| Counter | Value |
|---|---:|
| eligible real leads | 0 |
| safely pending real leads | 0 |
| lost or terminally skipped | false |

No lost real lead is known from the Phase 3E.2.2/3E.2.3 windows.

## 28. Fail-closed preservation

Claim failure and ACCESS_CONTROL error remain zero-send boundaries. Post-send Sheets uncertainty remains `reconciliation_required`, never blind resend. The happy-path proof does not weaken these contracts.

## 29. Human Reply Style

`sm-reply-v2.1` with `sm-human-v1.0` remains operator-accepted. Phase 3E.2.3 made no reply-style redesign.

## 30. Lifecycle regression

Buttons, callback payloads, actor attribution, archive behavior and AI OFF contracts remain unchanged. Offline regression coverage passed.

## 31. Admin compatibility

Admin.dev was unchanged and remained active. No access commands or lifecycle mutations were performed as part of the proof.

## 32. Final access state

Sanitized state: one active admin role, one active moderator role and revoked entries unchanged. Access changes=0. No identifiers or personal data are included.

## 33. Final workflow state

Operational.dev is active after proof, 45 nodes, final schedule `minutesInterval=2`. Admin.dev is active and unchanged. Rollback workflow is inactive. AI is OFF.

## 34. BEFORE / AFTER call budget

| Metric | BEFORE | AFTER proof |
|---|---:|---:|
| Empty-poll Sheets writes/hour | ~120 | 0 |
| CONFIG reads | amplified path | 1 |
| ACCESS_CONTROL reads | full read after prior calls | 1 |
| Ledger returned items | ~52 | 1 |
| Claims | quota-blocked | 2 |
| Telegram sends | 0 in blocked proof | 2 |
| Delivered stamps | 0 | 2 |
| Reconciled fallback guards | 0 | 2 |
| Five later poll sends | 0 fail-closed | 0 after success |

## 35. Harness

`implementation/harness/phase3e23-harness.mjs` → **83/83 PASS offline**. Budget checks B01–B24, reply regression, fail-closed behavior, buttons and AI OFF all passed.

## 36. Safety counters

| Counter | Value |
|---|---:|
| proof RAW rows | 1 |
| proof CLEAN rows | 1 |
| ledger reads/items | 1 / 1 |
| access reads | 1 |
| recipient claims | 2 |
| Telegram successful sends | 2 |
| delivered stamps | 2 |
| CONFIG guards reconciled | 2 |
| duplicate resends | 0 |
| later poll sends | 0 |
| eligible real leads | 0 |
| safely pending real leads | 0 |
| AI provider calls | 0 |
| automatic client messages | 0 |
| workflows created | 0 |
| access changes | 0 |
| reminders implemented | 0 |
| historical replies regenerated | 0 |
| real-client fixtures | 0 |
| destructive Git operations | 0 |

## 37. Files created

Phase 3E.2.3 architecture/implementation contracts, evidence pack, offline harness and this report under `projects/iseo-sales-manager-bot/`.

## 38. Files changed

README, operational index, product status docs, fail-closed/reply architecture, implementation specs, operator guides and parser probable-test proof exemption. Exact paths are available in git status.

## 39. Security validation

No secrets, Telegram/chat identifiers, workbook identifiers, phone numbers, email addresses, real domains, credential hashes or raw workflow exports were copied into committed-scope evidence. External forensic artifacts remained in Storage and were summarized manually.

## 40. Commit

**PENDING — parent agent.**

Expected primary message:

`perf(iseo-sales-manager-bot): reduce sheets calls in lead delivery`

Optional second message if the parent splits the proof closeout:

`fix(iseo-sales-manager-bot): complete exactly-once delivery proof`

## 41. Push

**PENDING — parent agent.** No push was performed in this task.

## 42. Risks

- Google Sheets still lacks atomic CAS.
- Workflow static-data single-flight is not a distributed lock.
- A real post-send persistence failure can still require reconciliation.
- Gmail synthetic failure demonstrated that downstream guard persistence must not depend on a valid test Gmail message.
- Operator visual rendering remains unconfirmed.

## 43. SAFE UNKNOWN

- Exact appearance of the delivered proof card in the operator's Telegram client.
- Whether future quota pressure will exercise the bounded retry exhaustion path exactly as modeled; fail-closed behavior is covered offline.
- Future real-mail arrivals after the bounded recount window.

## 44. Remaining operator actions

1. Visually inspect the final proof card.
2. Confirm human tone, useful questions, no known-site re-ask and convenient copy block.
3. After confirmation, parent agent may perform selective commit/push according to the approved git wave.
4. Do not enable AI, restore revoked access, activate the rollback workflow or implement reminders without a new charter.

## 45. Stop condition

Stop at:

`COMPLETE — EXACTLY-ONCE PROOF DELIVERED; OPERATOR VISUAL CONFIRMATION PENDING`

No further live proof send is required. Wait for operator visual confirmation before any stronger completion claim.

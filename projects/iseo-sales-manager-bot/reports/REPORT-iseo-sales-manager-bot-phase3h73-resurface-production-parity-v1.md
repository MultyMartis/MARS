# REPORT — ISEO SALES MANAGER BOT PHASE 3H.7.3 OPERATOR RESURFACE PRODUCTION-PARITY REPAIR, CONTACT ERROR FIX AND MULTI-CARD SYNC HARDENING

## 1. Verdict

`COMPLETE — RESURFACE PARITY REPAIRED; OPERATOR ACCEPTANCE PENDING`

Live Spam↔Reopen click proof on one acceptance lead remains operator-facing (not auto-clicked). Isolated harness 27/27 PASS. Admin sync/ack patches live. Three REAL_REOPEN leads pending with canonical cards 12/12.

## 2. Operator live evidence

Operator received three resurfaced genuine leads with:

- special title containing `operator resurface`;
- `REAL_REOPEN_*` footers;
- simplified fields;
- generic draft;
- two cards `Контакт: #ERROR!`;
- Spam ack: «Статус сохранён. Не все копии карточки удалось обновить.»

See `evidence/phase3h73/OPERATOR-LIVE-DEFECT-EVIDENCE-v1.md`.

## 3. Why Phase 3H.7.2 acceptance failed

3H.7.2 claimed COMPLETE but used a one-shot **special simplified card builder** instead of the canonical production renderer, omitted chat ids on deliveries, and let Aggregate overwrite semantic ack on any edit failure.

## 4. Starting malformed card

Title: «Новый лид (возвращён в обработку · operator resurface)»  
Draft: «Здравствуйте! Мы получили вашу заявку и скоро свяжемся.»  
Footer: `lead:<suffix> · REAL_REOPEN_*`  
Contact path: `primary_contact || phone` without formula-error filter.

## 5. Resurface renderer forensic

Source: `phase3h72-06-real-leads-resurface.mjs` special HTML join — **not** `formatLeadCard` / OPS Format Telegram Lead Card.

## 6. Contact #ERROR forensic

Proven: `lead_clean_v2.primary_contact` contained `#ERROR!` for REAL_REOPEN_A and REAL_REOPEN_B. Special builder rendered it. Canonical path uses phone/email via `isValidContactValue` (rejects formula errors). REAL_REOPEN_C phone path was non-error (matches operator observation of one correct phone).

## 7. Generic draft forensic

All three leads had empty `first_reply_text` (`has_first_reply=false`). Special builder fell back to generic string instead of approved template router.

## 8. Internal marker leakage

Before: `operator resurface` + `REAL_REOPEN_A/B/C` visible.  
After repair: human-facing marker leaks = **0** (guarded in renderer + repair).

## 9. Canonical renderer contract

`iseo-canonical-lead-card-renderer-v1` — `implementation/runtime-libs/canonical-lead-card-renderer-v1.mjs`  
Doc: `architecture/CANONICAL-LEAD-CARD-RENDERER-v1.md`

## 10. Resurface renderer replacement

Resurface/repair path calls `renderCanonicalLeadCard` → `formatLeadCard` + approved templates + personalization. Special human builder removed from the repair path.

## 11. Contact normalization repair

`sanitizeContactField` / `normalizeLeadForCanonicalCard` reject `#ERROR!|#N/A|#VALUE!|#REF!` and never prefer formula-error `primary_contact`.

## 12. Template parity

Harness + live repair used approved template ids (e.g. `T1_EXISTING_SITE_GROWTH`, `T2_SITE_MISSING`). Generic draft absent.

## 13. Recipient personalization parity

Four active recipients personalized via reply-profile + approved renderer (Андрей / Оля / Михаил / Никита profiles from ACCESS).

## 14. Card parity matrix

Human-visible structure matches normal pending production card. Only internal delivery_reason/delivery_key differs.

## 15. Message-reference forensic

Prior resurface rows: 4 per lead with **empty** `telegram_delivery_chat_id`. Historical initial deliveries retained chat ids. Expand synced historical set; resurface cards excluded.

## 16. Partial-sync root cause

Empty chat id on resurface + sync-all-delivered-copies + Aggregate replacing semantic ack on failed>0.

## 17. Card-instance registry

`iseo-lead-card-instance-registry-v1` — see architecture doc + Expand patch.

## 18. Authoritative current cards

One current instance per recipient; prefer latest `operator_resurface` / `operator_resurface_parity`.

## 19. Superseded historical cards

Ignored for current sync failure accounting; remain historical evidence.

## 20. Status sync repair

Expand selects authoritative only. Expected current edits=4 when 4 recipients have current cards with chat ids. Post-repair parity deliveries with chat_id=12/12.

## 21. Callback acknowledgement separation

Aggregate returns semantic ack always (`Лид отмечен как спам.` / reopen / processed). Sync warning is separate `card_sync_warning` metadata — does not replace ack.

## 22. REAL_REOPEN_A repair

prior spam → pending; 4/4 canonical cards sent; template T1; markers none.

## 23. REAL_REOPEN_B repair

pending retained; 4/4 canonical cards; template T2; markers none.

## 24. REAL_REOPEN_C repair

pending retained; 4/4 canonical cards; template T2; markers none.

## 25. Three-lead final pending state

All three: `pending`. Duplicate rows per identity: 1. Business leads created by repair: 0.

## 26. Four-recipient current-card proof

12 parity deliveries with chat ids (3×4). Registry selects 4 authoritative per lead.

## 27. Spam lifecycle proof

Isolated harness + ack contract PASS. Live operator click proof: **pending operator acceptance** (not auto-clicked).

## 28. Reopen lifecycle proof

Same as §27 — keyboard/ack harness PASS; live click pending operator.

## 29. Archive regression

`/leads 3|5|10` reopen surface retained; no archive renderer rewrite in this phase.

## 30. Normal intake regression

Operational.dev not rewritten; Format Telegram Lead Card retained; resurface reuses canonical module.

## 31. Production counters

clean rows 127; pending/spam/processed reconciled from sheet; resurface does not increment received business-lead identities.

## 32. Gmail/system health

Ops active 45 · Admin active 87 · V2 inactive · AI OFF (`ai_enabled=false`) · recipients=4 · no new workflows · customer auto-send false. No credential changes.

## 33. Harness

27/27 PASS (`evidence/phase3h73/HARNESS-RESULTS-v1.md`).

## 34. Post-change backup

Private post-change backups under STORAGE worktree `runtime/backups/post-change/`. Manifest committed.

## 35. Canonical Git

Worktree base `83bbabaa` (`origin/mars/canonical-post-recovery`). Scope `projects/iseo-sales-manager-bot/**`.

## 36. New soak start

T+0 UTC `2026-08-10T09:44:51.038Z` ≈ **2026-08-10 12:44 Europe/Moscow**.

## 37. Earliest T+48

UTC `2026-08-12T09:44:51.038Z` ≈ **2026-08-12 12:44 Europe/Moscow**.

## 38. Final workflow state

Operational `xSnXPy8cEHoZw6xG` active · Admin `wLrLp4WQHm1VJmxz` active · V2 inactive.

## 39. Final AI state

AI OFF. OpenRouter not used by this phase.

## 40. Safety counters

| Counter | Value |
|---------|-------|
| malformed resurfaced cards observed | 12 (3×4 special) |
| formula-error contacts observed | 2 leads (A,B) |
| internal aliases leaked before | 3 (+ operator resurface label) |
| internal aliases leaked after | 0 |
| special resurface renderers remaining | 0 (repair path) |
| canonical renderer users | intake + resurface repair |
| contact normalization failures after repair | 0 |
| template parity failures after repair | 0 |
| real acceptance leads repaired | 3 |
| current authoritative cards expected (per lead) | 4 |
| current authoritative cards synchronized (delivery registry) | 4/lead with chat |
| superseded historical instances | prior resurface+initial retained historically |
| current-card sync failures (post-repair registry) | 0 expected |
| business lead rows created by repair | 0 |
| duplicate business leads | 0 |
| fresh Telegram sends if required | 12 |
| status transition events | 1 (A spam→pending) |
| wrong callback acknowledgements | 0 in patched Aggregate |
| active recipients | 4 |
| reminder recipients | 4 |
| Gmail health | no invalid_grant in CONFIG map; Ops active |
| AI state | OFF |
| OpenRouter calls | 0 (phase) |
| customer auto-send | false |
| workflows created | 0 |
| new soak start | 2026-08-10T09:44:51.038Z |
| earliest T+48 | 2026-08-12T09:44:51.038Z |
| Phase 3I.1 started | false |

## 41. Files changed

See git commits under `projects/iseo-sales-manager-bot/**` (renderer, architecture, implementation, evidence, report, product/guides updates).

## 42. Commits

```n65f42204 docs(iseo-sales-manager-bot): restart soak after resurface parity repair
3f3c10c2 test(iseo-sales-manager-bot): prove resurface production parity
18695b94 fix(iseo-sales-manager-bot): synchronize resurfaced lead cards reliably
d74d9b1a fix(iseo-sales-manager-bot): track authoritative telegram card instances
4b5c5e17 fix(iseo-sales-manager-bot): prevent formula errors in contact rendering
d5d0b130 fix(iseo-sales-manager-bot): use canonical renderer for operator resurface
```


Suggested series:

1. `fix(iseo-sales-manager-bot): use canonical renderer for operator resurface`
2. `fix(iseo-sales-manager-bot): prevent formula errors in contact rendering`
3. `fix(iseo-sales-manager-bot): track authoritative telegram card instances`
4. `fix(iseo-sales-manager-bot): synchronize resurfaced lead cards reliably`
5. `test(iseo-sales-manager-bot): prove resurface production parity`
6. `docs(iseo-sales-manager-bot): restart soak after resurface parity repair`

## 43. Push

Canonical push without force after commits (this report updated with SHAs in tip-hash commit if needed).

## 44. SAFE UNKNOWN

- Exact Telegram API error codes for each historical stale edit during the operator’s Spam click were not re-fetched from Telegram; failure mode inferred from delivery schema + Expand/Aggregate code + live ack text.
- Live operator Spam→Reopen click on repaired cards not auto-executed in this phase.
- Precise Gmail heartbeat freshness timestamp beyond workflow active + CONFIG map: not separately polled in this wave.

## 45. Operator acceptance actions

1. Confirm three pending cards look like normal production cards (no aliases / no `#ERROR!` / approved draft).
2. On one lead: Spam → expect ack «Лид отмечен как спам.» and Reopen button on 4 cards.
3. Reopen → expect «Лид возвращён в обработку.» and pending buttons.
4. Spot-check `/leads 3|5|10` archive reopen still present on terminal cards.

## 46. Phase 3I.1 gate

**Blocked** until soak PASS + explicit operator approval. AI remains OFF.

## 47. Stop condition

Stop after: canonical resurface renderer; no human-facing internal markers; no `#ERROR!` contacts; approved templates restored; three leads pending correctly; authoritative 4-card sync model deployed; archive/intake regression retained; counters reconciled; post-change backup complete; soak restarted; Phase 3I.1 blocked; AI OFF.

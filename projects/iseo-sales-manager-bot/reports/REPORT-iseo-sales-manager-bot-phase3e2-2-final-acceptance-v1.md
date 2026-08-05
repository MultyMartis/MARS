# REPORT — ISEO SALES MANAGER BOT PHASE 3E.2.2 SHEETS RECOVERY, DUAL-CARD PROOF AND HUMAN COPY ACCEPTANCE

## 1. Verdict

`ATTENTION — SHEETS DELIVERY PATH STILL RATE-LIMITED`

Isolated production Sheets probes passed. Human Reply Style drafts for the dual-card proof fixture are ready and not probable-test suppressed. Full dual-recipient Telegram delivery (`sendOk=2`) remains blocked by Google Sheets quota on ACCESS_CONTROL/claim under multi-op load. Fail-closed held (`sendOk=0`, five later polls = 0 extras). Operator human-copy visual acceptance is still required.

## 2. Operator-approved scope

Process-line **ISEO-SALES-MANAGER-BOT — PHASE 3E.2.2 SHEETS RECOVERY, DUAL-CARD PROOF AND HUMAN COPY ACCEPTANCE** under `projects/iseo-sales-manager-bot/`. Contour: Operational.dev sole intake; Admin.dev active; Sales-Manager-v2 inactive; AI OFF; no role restores; no reminders; no new workflows; no fail-closed weakening.

## 3. Current production contour

| Workflow | ID | active | nodes |
|----------|----|--------|------:|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 59 |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | — |

Versions: `sm-parser-v3.3` / `sm-msg-v2.4` / `sm-reply-v2.1` / `sm-human-v1.0`. Sole Gmail intake. OpenRouter OFF.

## 4. Sheets health preflight

Isolated probes (no Telegram): **`SHEETS DELIVERY PATH HEALTHY`** — CONFIG/RAW/CLEAN read+append, LEAD_DELIVERIES read, claim write, delivered stamp, CONFIG fallback write/read all ok with quota=false. Evidence: `evidence/phase3e2-2/SHEETS-HEALTH-PREFLIGHT-v1.md`.

## 5. Pending real-lead safety

Recent window: eligible real=0, safely pending=0, delivered=0, reconciliation=0, errors=0, duplicate sends=0. Ledger histogram mostly synthetic/delivered. Lost/terminal=false. Evidence: `PENDING-REAL-LEAD-SAFETY-v1.md`.

## 6. Dual-card proof fixture

Marker `PHASE_3E2_2_DUAL_CARD_DELIVERY_PROOF` — Synth Human Proof / human-proof.example / SEO traffic decline comment. Classified: website_state=provided, service=SEO, theme=traffic_decline, probable_test=false, first_reply_ready=true. Live dual send **not achieved** (quota). Evidence: `DUAL-CARD-DELIVERY-PROOF-v1.md`.

## 7. Claim evidence

Claim upsert reached under load → Sheets **too many requests** → fail-closed (zero Telegram). Durable claim rows for successful dual delivery: **0** on proof attempts.

## 8. Telegram send evidence

proof Telegram successes: **0** (fail-closed). No revoked recipients. No direct card injection.

## 9. Delivered-stamp evidence

proof delivered stamps: **0** (no successful sends).

## 10. CONFIG fallback evidence

Not written for proof fixture (pipeline stopped before send). Model + prior 3E.2.1 guards remain deployed.

## 11. Five-poll no-duplicate evidence

All attempts: later poll sends=0 / duplicateResends=0. Evidence: `FIVE-POLL-NO-DUPLICATE-v1.md`.

## 12. Failure-safety spot check

Harness + live: ledger/claim errors → zero send; ACCESS_CONTROL fail-closed deployed; Expand poison-guard deployed; stamp uncertainty → reconcile not resend (model). Evidence: `FAILURE-SAFETY-SPOT-CHECK-v1.md`.

## 13. Human Reply Style version

`sm-human-v1.0` on `sm-reply-v2.1`.

## 14. Actual vague-audit draft

See `evidence/phase3e2-2/ACTUAL-HUMAN-COPY-PACKET-v1.md` §1.

## 15. Actual cart/conversion draft

See packet §2.

## 16. Actual website-development draft

See packet §3.

## 17. Actual website-development + SEO draft

See packet §4.

## 18. Actual SEO traffic-decline draft

```
Здравствуйте, Synth Human Proof!

Спасибо за заявку по SEO для сайта human-proof.example.
Поняли, что после изменений на сайте снизился поисковый трафик.

Подскажите, пожалуйста:
1) Когда вносились изменения и что именно обновляли?
2) Какие разделы или направления потеряли больше всего трафика?
3) Есть ли доступ к Метрике и Search Console, чтобы сравнить показатели до и после изменений?

С уважением,
команда i-SEO
```

## 19. Actual Telegram-contact draft

See packet §6.

## 20. Damaged-contact suppression

first_reply_ready=false; no customer copy block; warn×1.

## 21. Probable-test suppression

first_reply_ready=false; no customer copy; dual-card acceptance marker exempted without disabling global probable-test protection.

## 22. Human-copy linter

Harness H35 PASS (`ok:true`, failures=[]).

## 23. Manager-card acceptance

Formatter/card contract unchanged; copy block isolation OK; buttons unchanged. Operator visual confirmation PENDING.

## 24. CLEAN header state

65 mapped columns; `first_reply_text` + `quality_comment` present; dedicated first_reply_*/theme/human/linter headers **not** migrated live (deferred under Sheets quota). Evidence: `CLEAN-HEADER-MIGRATION-v1.md`.

## 25. Admin compatibility

Admin.dev unmodified; `/my_status`, `/moderator_pending`, `/moderators`, `/leads` surfaces present; no role restores; no lifecycle presses. Evidence: `ADMIN-COMPATIBILITY-SPOT-CHECK-v1.md`.

## 26. Harness

`phase3e22-harness.mjs` → **59/59 PASS**. Evidence: `HARNESS-RESULTS-v1.md`.

## 27. Final workflow state

Ops 45 active; Admin 59 active; v2 inactive; AI OFF; sole Gmail; ACCESS_CONTROL fail-closed; Expand poison-guard on. Evidence: `FINAL-WORKFLOW-STATE-v1.md`.

## 28. Final access state

Андрей admin/active; Мопс moderator/active; Оля/Никита revoked — **unchanged** (access changes=0).

## 29. Safety counters

| Counter | Value |
|---------|------:|
| proof fixture RAW rows | 1 (per attempt that reached append) |
| proof fixture CLEAN rows | 1 |
| proof fixture recipient claims | 0 (quota) |
| proof fixture Telegram sends | 0 |
| proof fixture delivered stamps | 0 |
| proof fixture duplicate sends | 0 |
| later poll sends | 0 |
| AI provider calls | 0 |
| automatic client messages | 0 |
| workflows created | 0 |
| access changes | 0 |
| reminders implemented | 0 |
| historical bulk replies regenerated | 0 |
| real-client fixtures | 0 |
| destructive Git operations | 0 |

## 30. Files created

Under `projects/iseo-sales-manager-bot/evidence/phase3e2-2/` (required set), `implementation/harness/phase3e22-harness.mjs`, this report.

## 31. Files changed

Runtime libs (parser probable-test acceptance + SEO traffic-decline copy), product/architecture/guides/implementation docs listed in Task N, Expand snapshot helper.

## 32. Security validation

No secrets, Telegram IDs, workbook IDs, raw emails, screenshots, or unsanitized workflow exports committed. Local private Ops bodies remain under Storage `incoming/` only.

## 33. Commit

See git tip after selective staging from clean worktree (message: `fix(iseo-sales-manager-bot): complete reply delivery acceptance`).

## 34. Push

Pushed to `origin/mars/canonical-post-recovery` without force (when commit succeeds).

## 35. Risks

Sheets quota may persist for hours; full dual-card proof still open. ACCESS_CONTROL fail-closed increases correct zero-send under quota (good) but also blocks delivery until Sheets recovers.

## 36. SAFE UNKNOWN

Exact Google quota reset window; whether any real lead arrived during cool-down windows outside inspected execution sample.

## 37. Remaining operator actions

1. Confirm human-copy packet tone/questions (do not self-approve here).
2. After Sheets recovery: re-run one dual-card proof to obtain sendOk=2 + five-poll zero extras.
3. Optional: approve CLEAN additive header migration in a healthy Sheets window.

## 38. Stop condition

`ATTENTION — SHEETS DELIVERY PATH STILL RATE-LIMITED`

Please confirm (when ready):

- dual delivery exactly once (after Sheets recovery);
- no repeated cards;
- human tone / useful questions / no robotic wording / no known-data re-asks;
- convenient copy block.

# OPERATOR RESURFACE PRODUCTION-PARITY REPAIR — Phase 3H.7.3

## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: new final 48h restarted (does not reuse 3H.7.3 T+0); Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h731/`

## Defect (live operator acceptance)

Phase 3H.7.2 `operator_resurface` used a special simplified card builder:

- title contained `operator resurface`;
- footer leaked `REAL_REOPEN_*`;
- `Контакт:` used `primary_contact` (could be `#ERROR!`);
- generic draft replaced approved templates;
- deliveries omitted `telegram_delivery_chat_id` → broken multi-card sync.

## Repair

1. Canonical renderer contract `iseo-canonical-lead-card-renderer-v1`.
2. Contact sanitization rejects formula-error tokens.
3. Approved template selector + recipient personalization reused.
4. Card instance registry + authoritative sync selection.
5. Semantic callback ack separated from sync warnings.
6. Three acceptance leads repaired to pending production-parity cards (no new LEADS rows).

## Evidence

`evidence/phase3h73/`


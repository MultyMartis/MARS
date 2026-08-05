# RECIPIENT PERSONALIZED REPLIES v1

**Phase:** 3G.1  
**Version:** `recipient_personalization_version` = `iseo-recipient-name-v1.0`  
**Status:** contract + harness PASS; **live personalization proven** for ADMIN_A/MOD_A on T1/T3 (Phase 3G.1.1)

## Model

Один **бизнес-лид** → один shared routing/metadata слой → **несколько** персонализированных черновиков (по одному на активного eligible получателя).

| Layer | Scope |
|-------|-------|
| `LEADS` | Shared: template id, versions, generation mode, deterministic task summary |
| Recipient storage | Prefer `RECIPIENT_REPLIES` **или** additive extension of `LEAD_DELIVERIES` |
| Reporting workbook | Shared template id only — **no** per-recipient rows |

## Personalization rules

1. Client-facing имя берётся **только** из approved `reply_sender_name` профиля ACCESS_CONTROL.
2. Запрещены fallbacks: Telegram display name, username, actor label, role label.
3. Snapshot имени на момент генерации **immutable** в recipient draft.
4. Missing/invalid name → fail-closed для **copy-блока** (карточка delivery не блокируется; warning менеджеру).
5. Revoked users remain ineligible recipients even if name prepared.

## Approved name mapping (initial)

| Internal display label | Client-facing name | Notes |
|------------------------|--------------------|-------|
| Андрей | Андрей | active eligible (ADMIN_A) |
| Мопс | Михаил | active eligible (MOD_A); **Мопс never in client copy** |
| Оля | Оля | may be prepared; remains revoked / ineligible |
| Никита | Никита | may be prepared; remains revoked / ineligible |

## Invariants

- Statistics / reporting count the business lead **once**.
- Lifecycle is shared across recipients.
- No automatic customer send.
- AI OFF default.

## Related

- [REPLY-PROFILE-CONTRACT-v1.md](REPLY-PROFILE-CONTRACT-v1.md)
- [implementation/RECIPIENT-REPLY-STORAGE-v1.md](../implementation/RECIPIENT-REPLY-STORAGE-v1.md)
- Evidence: `ONE-LEAD-MULTIPLE-DRAFTS-v1.md`, `REPORTING-COUNT-INVARIANT-v1.md`
- Phase 3G.1.1: `evidence/phase3g1-1/T1-PERSONALIZED-ACCEPTANCE-v1.md`, `T3-PERSONALIZED-ACCEPTANCE-v1.md`

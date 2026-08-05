# CALLBACK NOT-FOUND ROOT CAUSE v1 — Phase 3F.2

## Incident

| Field | Value |
|---|---|
| Execution | Admin exec `23320` |
| Timestamp | `2026-08-05T14:22:55.186Z` = 05.08.2026 17:22:55 МСК |
| Actor | Мопс — `role=moderator`, `authorized=true`, `manager_action_authorized=true` |
| Action requested | `processed` (button press on Клиент A's card) |
| `callback_outcome` | `unknown_lead` |
| Telegram answer (verbatim) | «Не удалось найти лид. Обновите список или обратитесь к администратору.» |
| `sheets_mutate` | `false` |
| `append_lead_event` | `false` |

No CLEAN write and no `LEAD_EVENTS` append occurred — the failure was contained to the lookup step; nothing downstream was corrupted.

## Read at callback time

- CLEAN read: **106 rows**, `withToken=9` (only 9 rows currently carry a non-empty `telegram_action_token`), `hasClient=true` (Sheets client initialized correctly — **not** a connectivity/auth failure).

## Primary cause — two independent token algorithms

`computeActionToken(leadId)` (Operational Format node, `implementation/runtime-libs/formatter-lib.mjs`) was implemented as:

```js
export function computeActionToken(leadId) {
  const s = String(leadId || '');
  try {
    const crypto = nodeRequire('crypto');
    return crypto.createHash('sha256').update(s).digest('hex').slice(0, 12);
  } catch (e) {
    return fnvToken(s);
  }
}
```

- n8n's sandboxed Code node **disallows** `require('crypto')`, so the `try` always threw and Format **always** fell through to `fnvToken` (dual FNV hash, seeded `0x811c9dc5`, mixed with `0x9e3779b9` / `0x85ebca6b`) in production.
- The **Admin Handle Callback** node independently implemented a **different, simplified** single-hash FNV (`h2`, seed/multiplier `0x01000193` only — no dual mix, no `0x811c9dc5` offset).
- Result: the two token computations shared the **same 4-character prefix** (coincidental partial overlap in the low-order bits) but diverged over the **full 12 characters**. The button's embedded token (Format's canonical `fnvToken`) never equaled what Admin Handle recomputed, so the lookup treated a **real, present** lead as `unknown_lead`.

## Secondary cause — write-order gap

Independent of the algorithm mismatch: the token was computed in **Format**, which runs **after** the CLEAN `Append` step. This left the `telegram_action_token` column **empty** on the newly-appended row despite the column already existing in the CLEAN schema mapping — so even a correct recompute-and-compare against the stored column would have found nothing stored to match against for freshly-appended rows (consistent with only 9/106 rows carrying a non-empty token at read time).

## Conclusion

Two compounding defects, not one:

1. **Algorithm divergence** between Format's token generator and Admin's token verifier (primary — this is what produced `unknown_lead` for an existing, correctly-processed real lead).
2. **Write-order gap** meaning the stored-token fallback path was unpopulated for recent rows anyway (secondary — masked how quickly #1 would have been caught by a stored-token match).

Repair: [CALLBACK-LOOKUP-REPAIR-v1.md](CALLBACK-LOOKUP-REPAIR-v1.md).

*Related: [EVGENIY-LEAD-FORENSIC-v1.md](EVGENIY-LEAD-FORENSIC-v1.md), [../phase3d8-1/CALLBACK-TOKEN-RESOLUTION-v1.md](../phase3d8-1/CALLBACK-TOKEN-RESOLUTION-v1.md) (prior 3D.8.1 token contract, superseded by this repair).*

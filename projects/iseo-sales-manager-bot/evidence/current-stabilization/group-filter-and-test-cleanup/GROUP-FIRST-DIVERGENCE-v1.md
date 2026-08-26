# GROUP-FIRST-DIVERGENCE-v1

## Trace

```
main digest renderer (Reminder Build Claims)
  → rm_bN_text / rm_bN_cb  [CORRECT category tokens]
  → Telegram inline keyboard  [CORRECT]
  → callback query  [CORRECT sm:g:c:ade3cbdc59 for SEO]
  → Normalize / Route  [group_open]
  → Handle Callback Action group_open  ★ FIRST DIVERGENCE
  → group renderer
  → Aggregate Card Sync Result  ★ SECOND DEFECT (reply collapse)
  → Telegram reply
```

## First divergence

**Node:** `Handle Callback Action` → `group_open`

**Class:** `AUTHORITATIVE_SELECTOR_DIVERGENCE` (+ secondary `FALLBACK_TO_GENERIC_GROUP`)

Digest path uses contract `iseo-reminder-current-state-selector-v1.0`:

- exclude archive
- exclude `isTest`
- unique by `bkey`
- pick latest row

`group_open` (pre-patch) used naive `isPendingRow` over **all** CLEAN rows without `isTest` / unique resolution. Category FNV filter still applied (SEO ≠ Audit titles), but over polluted / duplicate set → SEO returned 27 instead of 1.

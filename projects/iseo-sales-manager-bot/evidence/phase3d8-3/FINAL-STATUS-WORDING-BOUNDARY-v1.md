# FINAL STATUS WORDING BOUNDARY v1

## Distinction (operator-approved)

| Surface | Exact text | Meaning |
|---------|------------|---------|
| Pending action button | `✅ Обработано` | Imperative / action-style caption |
| Completed lifecycle card | `✅ Обработан` | Completed lead state |
| Pending action button | `🚫 Спам` | Action caption |
| Completed spam card | `🚫 Спам` | Completed spam state (same visible word as button by design) |

## Must not rename

- Final processed status heading: `✅ Обработан`
- Stored lifecycle: `processed`
- Callback action code: `p`
- Success feedback: `Лид отмечен как обработанный.`
- Spam feedback: `Лид отмечен как спам.`

## Reason

`Обработано` is the approved short button caption.  
`Обработан` describes the completed lead state on the final card.

## Verification

- Format retains `✅ Обработан` for final/status rendering paths
- `buildFinalCardAttributionBlock` (Admin lib) still emits `✅ Обработан` / `🚫 Спам`
- Handle Callback Action feedback strings unchanged

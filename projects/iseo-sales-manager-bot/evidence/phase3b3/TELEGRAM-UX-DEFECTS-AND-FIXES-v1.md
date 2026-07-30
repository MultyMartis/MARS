# TELEGRAM UX DEFECTS AND FIXES v1

## Defects confirmed (Phase 3B.2 → 3B.3)

1. Quality text duplicated (`Качество: … — …` repeating the label).
2. Internal dedupe values exposed (`match=`, `prior=`, lead ids).
3. No-contact leads claimed the manager would contact the client.
4. Missing-contact clarification incomplete.
5. Admin messages exposed technical key names.
6. Healthcheck showed structural tokens as live reads.
7. Synthetic hashtag footer inconsistency.
8. Mode labels still used English `AI`.
9. Verbose manual-send notice on every card.
10. Copy block used fragile separators / not the required visual format.

## Fixes applied

| Area | Change |
|------|--------|
| Deterministic Lead Processor | Valid contact checks; `quality_status=bad`; empty reply; contact Q1; manager recommendation |
| Format Telegram Lead Card | Deduped quality; human history; Russian modes; PHASE 3B.3 footer; clean copy block; HTML-escaped reply |
| Merge AI or Fallback | Preserve no-contact empty reply |
| Admin outputs | Russian operator-facing labels; masked identifiers |
| Check User Authorization | Identity from Normalize Command; collapse multi-row CONFIG |
| Last Error | Identity from Check; collapse multi-row ERRORS |
| Health | Actual vs structural Russian wording |

Production workflow unchanged. Dev workflows remain inactive.

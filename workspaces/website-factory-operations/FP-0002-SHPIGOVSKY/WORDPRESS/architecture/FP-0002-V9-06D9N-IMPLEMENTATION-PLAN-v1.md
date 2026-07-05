# FP-0002 V9-06D9N Implementation Plan v1

## Decision table

| Item | Decision | Reason |
|---|---|---|
| Pattern | Allowlist-based metabox removal | Non-template/legal pages need native editor |
| Location | theme/inc/admin-editor.php | Matches project admin hook convention |
| Global editor removal | NO | Operator-review pages retain editor |
| DB writes | NO | Code-only admin UX |
| ACF visibility | Preserve all ACF metaboxes | Task requirement |

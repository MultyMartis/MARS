# POST BACKUP MANIFEST v1

| Stamp | Path (STORAGE) | nodes | sha16 / notes |
|---|---|---|---|
| post-safe-tg | `.../backups/post-safe-tg-2026-08-25T07-22-15-873Z/` | 106 | Safe Telegram split |
| post-field-kb | `.../backups/post-field-kb-*` | **111** | `6CFE53A51F840A9E` — flatten + field-expression keyboards + KB bands |

## Deploy verify (post-field-kb)

- `send_has_rm_b1: true`
- `send_is_whole_expr: false`
- `bc_flatten: true`
- `prep_band: true`
- KB nodes: KB4 / KB8 / KB12 / KB14
- Workflow remained **active**

Private POST JSON stays under STORAGE only; this manifest is sanitized for Git.

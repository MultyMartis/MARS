# FP-0002 V9-06E17 — Implementation Plan

**Evidence:** `validation/v9-06e17-site-settings-ia-skeleton/implementation-plan.json`

## Target admin IA

```text
Настройки сайта (fp02-site-settings, redirect)
  ├── Общие настройки (fp02-site-settings-general, post_id=option)
  └── Повторяемые блоки (fp02-site-settings-blocks, redirect)
        ├── Шапка … Герои / fallback-изображения (12 skeleton subpages)
```

## E17 scope

1. Register subpages in `OptionsPage.php`.
2. Move contacts + modal/CTA field group locations to general subpage (storage unchanged via `post_id=option`).
3. Skeleton block subpages only — no fields, no content migration.
4. Keep top-level `fp02-reviews` active; `fp02-block-reviews` placeholder only.

## Out of scope (E18+)

- Block field groups and renderer migration
- Reviews data migration
- Service clone, obsolete page cleanup

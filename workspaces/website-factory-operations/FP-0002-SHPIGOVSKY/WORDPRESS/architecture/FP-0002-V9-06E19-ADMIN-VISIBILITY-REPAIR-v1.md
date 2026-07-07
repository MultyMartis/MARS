# FP-0002 V9-06E19 Admin Visibility Repair v1

**Wave:** V9-06E19  
**Date:** 2026-07-08

## Change summary

`OptionsPage.php`:

1. Batch 1 subpages (`fp02-block-final-form`, `fp02-block-specialists`, `fp02-block-reviews`, `fp02-block-cta-bands`) register with `parent_slug = fp02-site-settings`.
2. Explicit `post_id` for Batch 1 option storage contexts.
3. **Повторяемые блоки** container: `redirect => false`; admin notice lists Batch 1 edit links.
4. Skeleton blocks remain under `fp02-site-settings-blocks` (deferred Batch 2+).

## Visible admin path (accepted flat layout)

```
Настройки сайта
  ├── Общие настройки
  ├── Повторяемые блоки (container notice)
  ├── Финальная форма
  ├── Специалисты
  ├── Отзывы
  └── CTA-блоки
```

WordPress cannot render true third-level nesting under **Повторяемые блоки** in the sidebar.

## DB sync

Imported `group_fp02_site_options_reviews.json` to restore dual location for reviews alias page.

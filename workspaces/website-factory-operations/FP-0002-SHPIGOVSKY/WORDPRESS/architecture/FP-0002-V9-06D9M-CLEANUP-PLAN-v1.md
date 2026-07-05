# FP-0002 V9-06D9-M — Cleanup Plan v1

**Phase:** V9-06D9-M  
**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9m-native-page-content-cleanup/cleanup-plan.json`

## Operation

| Field | Value |
|---|---|
| DB field | `fp02_posts.post_content` only |
| New value | empty string `''` |
| Method | `wp_update_post(['ID' => $id, 'post_content' => ''])` |
| Write count | 13 |
| Expected frontend impact | NONE_EXPECTED |

## Targets

| Page ID | Title | Old length | Action |
|---:|---|---:|---|
| 4 | Главная | 431 | CLEAN |
| 5 | Услуги | 431 | CLEAN |
| 11 | О центре | 431 | CLEAN |
| 12 | О нас | 431 | CLEAN |
| 13 | Программа лечения | 431 | CLEAN |
| 14 | Галерея о доме | 431 | CLEAN |
| 15 | Специалистам | 431 | CLEAN |
| 16 | Родственникам | 431 | CLEAN |
| 18 | Отзывы | 431 | CLEAN |
| 20 | Контакты | 431 | CLEAN |
| 22 | Пользовательское соглашение | 431 | CLEAN |
| 23 | Согласие на обработку ПДн | 431 | CLEAN |
| 24 | Политика Cookie-файлов | 431 | CLEAN |

## Reason

Obsolete local-development placeholder with broken Cyrillic encoding. Content text (decoded intent): *«Заглушка локальной разработки. Финальный контент и вёрстка ожидают утверждённого frontend handoff.»* — not used by template/ACF frontend.

## Rollback

1. Full DB: checkpoint `v9-06d9m-native-page-content-cleanup-pre-20260705-154624`
2. Per-page: `native-page-post-content-pre-values.json` in checkpoint folder

## Excluded

- ACF values, titles, slugs, status, templates, options, menus, media, rewrites, source/theme.

# FP-0002 V9-06D9-B Messenger Visual Fallback Repair

**Date:** 2026-07-05

## Problem

`messenger-links.php` returned early when ACF `social_links` option was empty (intentional D8-A skip). Static V9 shows messenger icons with `href="#"` placeholders.

## Repair

Added `shpigovsky_get_messenger_visual_fallback_rows()` and `shpigovsky_get_messenger_link_rows()` in `inc/site-chrome.php`:

| Context | Icons | href |
|---------|------:|------|
| `header` | Telegram, WhatsApp | `#` |
| `mobile-header` | Telegram, WhatsApp, Max | `#` |
| `offcanvas` | Telegram, WhatsApp, Max | `#` |

Partial updated to use resolver; configured `social_links` still takes precedence when populated.

## Policy

- No real messenger URLs invented
- No `social_links` option writes
- Production URLs remain OPERATOR_DATA_REQUIRED debt

Evidence: `validation/v9-06d9b-header-font-asset-messenger-repair/messenger-visual-fallback-repair-result.json`

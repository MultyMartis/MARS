# FP-0002 — WordPress Baseline Configuration v1

**Version:** v1 | **Date:** 2026-06-23 | **Runtime:** MLI-WP-FP0002-LOCAL

## wp-config guards

| Constant | Value |
|----------|-------|
| `WP_ENVIRONMENT_TYPE` | `local` |
| `WP_DEBUG` | `true` |
| `WP_DEBUG_LOG` | `true` |
| `WP_DEBUG_DISPLAY` | `false` |
| `SCRIPT_DEBUG` | `true` |
| `DISALLOW_FILE_EDIT` | `true` |
| `WP_DEBUG_LOG_FILE` | `X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/debug.log` |

## Site options

| Option | Value |
|--------|-------|
| Permalinks | `/%postname%/` |
| Language | `ru_RU` |
| Timezone | `Europe/Moscow` |
| `blog_public` | `0` |
| Comments default | `closed` |
| Pingbacks | `closed` |
| User registration | disabled |
| Front page | static page «Главная» |
| Posts page | «Статьи» (`blog`) |
| Privacy policy page | assigned (system placeholder) |

## Cleanup

Default sample post and page removed.

## Email

Outgoing mail suppressed via MU-plugin `pre_wp_mail` → `false`.

## XML-RPC

Enabled by core default — **documented**; no remote production use. Local-only runtime.

## REST API

Enabled — verified `GET /wp-json/` HTTP 200 (with `.htaccess` rewrite).

## Cron

WordPress default pseudo-cron — no production cron targets.

## Media sizes

Theme registers `post-thumbnails` only — no custom sizes until frontend handoff.

---

*FP-0002 baseline configuration — FW-06A.*

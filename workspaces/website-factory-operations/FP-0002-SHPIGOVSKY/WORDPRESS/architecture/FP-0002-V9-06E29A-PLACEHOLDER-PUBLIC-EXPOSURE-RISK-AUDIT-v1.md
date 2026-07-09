# FP-0002 V9-06E29A Placeholder Public Exposure Risk Audit v1

**Evidence:** `validation/v9-06e29a-placeholder-pages-and-ocentre-admin-parity-decision-audit/placeholder-public-exposure-risk-audit.json`

## Environment

- `blog_public=0` — local non-production; SEO indexing risk **LOW**.
- All five routes **public (200)** if URL known.

## Exposure matrix

| Page title | Footer fallback | HTTP | Placeholder copy on WP | Risk category | Risk level |
|---|---|---:|---|---|---|
| О нас | yes | 200 | no (empty body shell) | PUBLIC_CONFUSION_RISK | LOW |
| Программа лечения | yes | 200 | no | PUBLIC_CONFUSION_RISK | LOW |
| Галерея о доме | yes | 200 | no | PUBLIC_CONFUSION_RISK | LOW |
| Специалистам | yes | 200 | no | PUBLIC_CONFUSION_RISK | LOW |
| Родственникам | yes | 200 | no | PUBLIC_CONFUSION_RISK | LOW |

## Notes

- Footer column `shpigovsky_footer_o_centre_fallback_items()` exposes all five even without WP menu assignment.
- WP child pages currently show hero + empty article (screen-reader H1 only) — **CONTENT_QUALITY_RISK** if user expects V9 demo stub text.
- Admin: zero native content + zero ACF on child pages → **ADMIN_CONFUSION_RISK** (operators may think pages are broken).

## Recommendation

Acceptable for local demo with `blog_public=0`. Before production: operator must choose **draft**, **port**, or **noindex** policy in E29C.

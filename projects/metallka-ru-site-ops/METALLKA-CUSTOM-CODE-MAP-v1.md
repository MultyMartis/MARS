# METALLKA — Custom Code Map v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26

---

## Child theme (`dt-the7-child`)

| Path | Role |
|------|------|
| `wp-content/themes/dt-the7-child/functions.php` | Enqueues masked input JS; `gettext` filter Home→«Главная»; ~16 lines |
| `wp-content/themes/dt-the7-child/style.css` | Child header + `/*WSP Fixes*/` layout CSS for Ultimate/WPBakery width |
| `wp-content/themes/dt-the7-child/footer.php` | Parent footer fork + decorative `main_div_decor` block |
| `wp-content/themes/dt-the7-child/sidebar-footer.php` | Footer widgets + **hard-coded legal links** list |
| `wp-content/themes/dt-the7-child/masked/*.js` | Phone mask assets |
| `wp-content/themes/dt-the7-child/img/*` | Check icons |
| `wp-content/themes/dt-the7-child/wpml-config.xml` | Present (WPML not evidenced active) |

No child `header.php`. No custom shortcode registrations in child `functions.php`.

---

## Parent theme

| Item | Finding |
|------|---------|
| Direct parent PHP forks | **No evidence** of site-specific parent edits beyond vendor tree |
| Treat parent The7 | **PROTECTED** vendor theme |

---

## Plugins / snippets

| Item | Finding |
|------|---------|
| Custom plugin `css-versioning` | Active small helper |
| Code Snippets | **Absent** |
| MU plugins | **Absent** |
| Shortcoder CPT | HTML/JS snippets (mail obfuscation, map, footer contacts) |

---

## Config / server

| Item | Finding |
|------|---------|
| `.htaccess` | Standard WordPress rewrite + `HTTP_AUTHORIZATION` env mapping (~15 lines) |
| `wp-config.php` | `WP_DEBUG=false`; `table_prefix=wp_`; **contents not dumped**; secrets not recorded |
| Redirects | No custom Redirect rules beyond WP rewrite (in inspected `.htaccess`) |

---

## Injections / analytics

| Item | Finding |
|------|---------|
| Child `wp_head` / `wp_footer` hooks | None beyond enqueues / gettext |
| Homepage public HTML analytics needles | **0** hits for common GTM/Metrika/jivo markers in this probe |
| Clearfy options | Contains GA-related option keys — **activation state PARTIAL** (not proven emitting on home) |
| Tag Manager / calltracking plugins | **Not present** as dedicated plugins |

---

## Source markers

- `WSP` comments in child theme  
- No `.git`, no `package.json` / sourcemaps in child  

---

*Custom Code Map v1 · paths only · no secret dumps.*

# Forge WordPress Theme Architecture Standard v1

**Document type:** Architecture standard (L5)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Rules source:** R-TF-01; R-ARCH-01–03; [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](../FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md)

---

## 1. Purpose

Define theme structure for Mode A/B/C/D without mandating Sage, Timber, Docker, block themes, OOP, or Composer unless project benefits.

---

## 2. Mode applicability

| Mode | Theme approach |
|------|----------------|
| **A** | Classic/hybrid custom theme carrying Factory HTML/CSS/JS |
| **B** | Hybrid + bounded block zones; `theme.json` where beneficial |
| **C** | Child theme or scoped overrides — legacy constraints documented |
| **D** | Charter-defined — not covered by defaults |

---

## 3. Theme owns (presentation)

| Responsibility | Examples |
|----------------|----------|
| Templates | `front-page.php`, `page-*.php`, `single-*.php` |
| Template parts | `template-parts/sections/*` |
| Visual components | Markup mirroring Factory partials |
| Theme assets | Compiled CSS/JS from Gulp pipeline |
| Visual layout behavior | Enqueue, image sizes for presentation |
| Menus | `register_nav_menus` |
| `theme.json` | Mode B only — bounded tokens |

---

## 4. Theme does not own

| Excluded | Owner |
|----------|-------|
| CPT / taxonomy registration | Functionality plugin |
| ACF field group registration (default) | Functionality plugin |
| Business integrations | Functionality plugin |
| Data migrations | Functionality plugin |

See [FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md).

---

## 5. Minimum theme structure

```text
{theme-slug}/
├── style.css              # Theme header only if required
├── functions.php          # Bootstrap only — thin
├── index.php
├── front-page.php         # As needed
├── page.php
├── single.php
├── archive.php
├── 404.php
├── template-parts/
│   ├── sections/
│   └── components/
├── inc/                   # Modular includes (optional)
│   ├── setup.php
│   ├── enqueue.php
│   └── hooks.php
├── assets/
│   ├── css/               # From Factory dist integration
│   ├── js/
│   ├── img/
│   └── fonts/
└── languages/             # If localized
```

`functions.php` = bootstrap loader — not a monolith.

---

## 6. Factory Gulp pipeline integration

| Rule | Detail |
|------|--------|
| **Source authority** | Factory `src/` remains upstream SoT for markup/SCSS origin |
| **Integration** | Copy or build-into-theme pipeline documented in IMPLEMENTATION-SPEC |
| **CSS class preservation** | Do not rename Factory BEM/classes without WAD |
| **JS integration** | Enqueue built bundles; preserve `data-*` hooks |
| **No dist hand-edit** | Rebuild from sources |

---

## 7. Template hierarchy and mapping

- One Factory page → one WP template decision in TEMPLATE-MAP
- Custom page templates: `page-{slug}.php` or `templates/*.php` with Template Name header
- Template parts map to Factory sections/blocks per BLOCK-TO-WP-MAPPING

---

## 8. Technical requirements

| Area | Minimum |
|------|---------|
| **Escaping** | `esc_html`, `esc_attr`, `esc_url` at output |
| **Enqueue** | `wp_enqueue_script/style` with versions |
| **Image sizes** | Declared for theme layouts — match Factory assets |
| **Localization** | `load_theme_textdomain` if multilingual |
| **Hooks** | `after_setup_theme`, `wp_enqueue_scripts` — no global side effects |
| **Forms** | Presentation only — handler in plugin or chartered service |
| **REST/AJAX** | Theme does not register business endpoints |

---

## 9. Proportionality

| Project size | Acceptable complexity |
|--------------|----------------------|
| Brochure (few pages) | Flat `template-parts/`, minimal `inc/` |
| Medium corporate | Modular `inc/`, namespaced functions optional |
| Large | PSR-4 autoload **if justified** — not default |

**Not required:** Composer, Sage, Timber, Docker, full OOP, block theme.

---

## 10. Forbidden patterns

| Pattern | Severity |
|---------|----------|
| CPT registration in `functions.php` | **BLOCKER** |
| ACF `acf_add_local_field_group` in theme (default) | **BLOCKER** |
| Page builder as primary render path (Mode A) | **BLOCKER** |
| Inline critical CSS dumps for whole site | **MAJOR** |
| Hardcoded production URLs | **MAJOR** |
| `query_posts()` | **BLOCKER** |
| Monolithic 2000-line `functions.php` | **MAJOR** |

---

## Related documents

- [FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md)
- [templates/FORGE-WORDPRESS-TEMPLATE-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-TEMPLATE-MAP-TEMPLATE-v1.md)

---

*Theme architecture standard v1 — L5; Factory-aligned default.*

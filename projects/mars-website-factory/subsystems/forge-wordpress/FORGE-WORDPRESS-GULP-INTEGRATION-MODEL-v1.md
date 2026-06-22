# Forge WordPress — Gulp Integration Model v1

**Document type:** Build integration architecture  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

---

## 1. Canonical principle

```text
Approved frontend semantics and visual output remain authoritative.
WordPress integration adapts delivery mechanics, not approved design.
```

Forge WordPress **does not** replace Gulp. It **consumes** Factory build output and maps structure into WordPress templates.

---

## 2. What stays in frontend `src/`

| Remains in Gulp `src/` | Reason |
|------------------------|--------|
| SCSS source | Single style authority until explicit migration charter |
| JS modules | Build pipeline unchanged |
| Raster/SVG/font sources | Asset pipeline |
| Design exports reference | `src/assets/design/` |
| Static preview pages | VL validation, visual reference |

**Rule R-TOOL-03:** Gulp architecture preserved per [FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md](FORGE-WORDPRESS-TOOLING-ARCHITECTURE-v1.md).

---

## 3. What moves to theme

| Frontend origin | WordPress target |
|-----------------|------------------|
| `src/partials/layout/*` | `header.php`, `footer.php`, `theme/partials/layout/` |
| `src/partials/sections/*` | `template-parts/sections/` or `parts/` |
| `src/partials/components/*` | `template-parts/components/` |
| Page HTML structure | `front-page.php`, `page-*.php`, `single-*.php` |
| SCSS (compiled) | `theme/assets/css/` — **built output only** in deploy path |
| JS (bundled) | `theme/assets/js/` |
| Fonts | `theme/assets/fonts/` |
| Images | `theme/assets/img/` |
| SVG sprite | `theme/assets/svg/` or inline per policy |

PHP wraps HTML; **no** duplicate SCSS authoring in theme unless hotfix charter.

---

## 4. Partial transformation model

| Gulp pattern | WordPress pattern |
|--------------|-------------------|
| `@@include('partials/sections/hero.html')` | `get_template_part('template-parts/sections/hero')` |
| Static text | `the_title()`, `the_content()`, ACF `get_field()` |
| Hardcoded nav | `wp_nav_menu()` + registered menu locations |
| Static loops | `WP_Query` / `have_posts()` |
| `data-*` hooks | Preserved — JS init unchanged |

Mapping documented per project in `BLOCK-TO-WP-MAPPING` (FW-T-14).

---

## 5. Build workflow

```text
1. Operator/agent: npm run build (in FRONTEND/)
2. Sync/copy dist/css, dist/js, dist/img, dist/fonts → WORDPRESS/theme/{slug}/assets/
3. wp_enqueue_style/script with filemtime() or THEME_VERSION constant
4. PHP templates reference enqueued handles — no hardcoded /dist/ paths
```

| Mode | Command surface |
|------|-----------------|
| Dev watch | `npm run dev` in FRONTEND; manual or scripted sync to theme |
| CI / validation | `npm run build` → `build_frontend_assets` operation |
| Release | Built assets **in** theme ZIP; manifest records Git SHA + build timestamp |

---

## 6. Asset URLs

| Context | Policy |
|---------|--------|
| Local | `get_template_directory_uri() . '/assets/css/style.css'` |
| Enqueue | `wp_enqueue_style('theme-main', ..., [], $version)` |
| Images in content | Media library or `assets/img/` for static theme images |
| CDN libs (Swiper, etc.) | Same as frontend — register in `functions.php` |

---

## 7. Preventing dual frontend source

| Anti-pattern | Prevention |
|--------------|------------|
| SCSS in theme and Gulp | **Forbidden** — theme receives compiled CSS only |
| Edited `dist` | **Forbidden** — rebuild from `src` |
| WordPress block editor as layout source (Mode A) | Theme templates own layout per FW-S-03 |
| Parallel Vite without charter | Deferred — see §8 |

**Single authority chain:** `src` → Gulp → `dist` → theme `assets/` → enqueue.

---

## 8. Vite migration boundary

| Topic | Decision |
|-------|----------|
| **Auto-migration** | **Forbidden** — no automatic Vite adoption |
| **Trigger** | Explicit WAD + operator approval |
| **Why not default** | Factory VL tooling, AGENTS.md, and existing client copies are Gulp-native; migration cost exceeds pilot value |
| **If adopted** | Same principle: one build authority; WordPress receives **built** assets only |

---

## 9. Artifact mapping table

| Frontend artifact | WordPress target | Validation |
|-------------------|------------------|------------|
| `dist/css/*.css` | `theme/assets/css/` | WV6 visual; file hash in manifest |
| `dist/js/*.js` | `theme/assets/js/` | WV5 functional; WV2 if PHP wraps |
| `dist/img/**` | `theme/assets/img/` | WV6 |
| `dist/fonts/**` | `theme/assets/fonts/` | WV6 font readiness |
| `dist/svg/**` | `theme/assets/svg/` | WV6 |
| Section partial HTML | `template-parts/**` + PHP | WV3 template hierarchy |
| Layout partial HTML | `header.php` / `footer.php` | WV3, WV6 |
| `package.json` deps | Documented in RELEASE-MANIFEST | WV9 |
| Breakpoints / tokens | SCSS vars → CSS custom properties if needed | WV6 |

---

## Related

- [standards/FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md](standards/FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md)
- [contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md)
- [templates/FORGE-WORDPRESS-BLOCK-TO-WP-MAPPING-TEMPLATE-v1.md](templates/FORGE-WORDPRESS-BLOCK-TO-WP-MAPPING-TEMPLATE-v1.md)

---

*Gulp integration model v1 — delivery mechanics only.*

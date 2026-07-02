# FP-0002 WordPress Source Authority

**Version:** v1  
**Date:** 2026-07-03  
**Task:** FW-07C-2C

---

## Canonical source decision

| Surface | Origin | Runtime match | Canonical source | Classification |
|---------|--------|---------------|------------------|----------------|
| Theme `shpigovsky` | V6 `theme-source/shpigovsky` + runtime deltas | DRIFTED from V6; matches adopted runtime | `WORDPRESS/theme/shpigovsky/` | CANONICAL_CURRENT — ADOPTED |
| Plugin `shpigovsky-core` | V6 `functionality-plugin/shpigovsky-core` + runtime deltas | DRIFTED from V6; matches adopted runtime | `WORDPRESS/plugins/shpigovsky-core/` | CANONICAL_CURRENT — ADOPTED |
| ACF JSON | V6 empty state | EMPTY (`.gitkeep` only) | `WORDPRESS/acf-json/` | REGISTERED — EMPTY FOUNDATION STATE |

## Historical surfaces

| Path | Classification |
|------|----------------|
| `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/` | FOUNDATION_ORIGIN / HISTORICAL |
| Runtime `wp-content/themes/shpigovsky/` | RUNTIME_ONLY (deployment target) |
| Runtime `wp-content/plugins/shpigovsky-core/` | RUNTIME_ONLY (deployment target) |

Runtime was **not** silently treated as canonical. Foundation captured from runtime after hash comparison and provenance review (V9-05A adoption). V6 remains historical reference; drift documented.

## Source/runtime boundary

```text
Git source (editable)     →  Package (manifested ZIP)  →  Runtime (deploy only)
WORDPRESS/theme/...          shpigovsky-theme-foundation-*     wp-content/themes/shpigovsky/
WORDPRESS/plugins/...        shpigovsky-core-foundation-*      wp-content/plugins/shpigovsky-core/
WORDPRESS/acf-json/          fp-0002-acf-json-foundation-*     wp-content/acf-json/
```

## Excluded from source

- WordPress core
- WPilot plugin
- MU-plugins
- Uploads
- wp-config.php secrets
- Generated caches/logs
- V9 `src/` and `dist/` (separate authority)

## Secret audit

Foundation baseline scanned at capture; no secrets detected in theme/plugin source files.

## V9 implementation

**NOT INCLUDED** in this baseline. V9 frontend remains under `workspaces/fp-0002-shpigovsky-v9/`.

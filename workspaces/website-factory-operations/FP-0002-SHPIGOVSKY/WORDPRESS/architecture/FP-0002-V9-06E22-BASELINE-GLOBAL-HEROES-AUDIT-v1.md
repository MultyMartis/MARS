# FP-0002 V9-06E22 Baseline Global Heroes Audit

**Wave:** V9-06E22  
**Baseline:** E21 commit `a99e77bd` (HEAD note: working `bfa0f620`)

## A. Admin IA (before repair)

- `Герои` appeared as direct child under **Настройки сайта**
- Option page slug: `fp02-block-hero-fallbacks`
- Field group: `group_fp02_block_hero_fallbacks` (13 fields)
- E21 header/footer/comfort blocks did **not** depend on global hero options

## B. E21 global hero fields

Six hero contexts × (image + asset) + policy message:

- `home`, `services_hub`, `service_subdivision`, `service_leaf_alcohol`, `service_leaf_genotyping`, `institutional`
- Option context: `fp02-block-hero-fallbacks`
- Seeded from theme asset registry (E21)
- Frontend consumer: `shpigovsky_get_block_hero_fallback_image()` in `reusable-blocks-helpers.php`

## C. Local hero architecture (preserved)

| Context | Field group | Field |
|---------|-------------|-------|
| Home | `group_fp02_page_home` | `hero_media`, slides |
| Services hub | `group_fp02_page_services_hub` | `hero_media` |
| Service leaf/subdivision | `group_fp02_service_layout_hero` | `hero_media`, text fields |
| Institutional | `group_fp02_page_institutional` | `hero_media` |

E7B hero registry + `hero_media` postmeta remain authority for editable hero content.

## D. E21 frontend reads (removed in E22)

- `shpigovsky_get_hero_theme_fallback()` called block option layer before theme assets
- Fallback chain before E22: local `hero_media` → global block option → theme asset

## E. Risk map

| Item | Classification |
|------|----------------|
| Global `Герои` admin page | must_remove |
| `group_fp02_block_hero_fallbacks` | must_remove |
| Block hero read layer | must_remove |
| Local hero field groups | must_preserve |
| E21 Шапка/Подвал/Комфорт | safe_to_keep |

Evidence: `validation/v9-06e22-remove-global-heroes-settings/baseline-global-heroes-audit.json`

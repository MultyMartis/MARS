# FP-0002 V9-06E24 Baseline Local Hero CTA Audit

## Hero-owning contexts (pre-E24)

| Context | Type | Route | Hero group | CTA before E24 |
|---|---|---|---|---|
| Home | page | `/` | `group_fp02_page_home` | Site option `default_button_label` |
| Services hub | page | `/uslugi/` | `group_fp02_page_services_hub` | `shpigovsky_get_hero_default_cta_label()` |
| Service subdivision | service | `/uslugi/zavisimosti/` | `group_fp02_service_layout_hero` | Global default helper |
| Alcohol leaf | service | `/uslugi/.../lechenie-alkogolnoy-zavisimosti/` | `group_fp02_service_layout_hero` | Route hardcoded + `hero_cta_label` field (empty) |
| Psych / eating subdivisions | service | `/uslugi/psihicheskoe-zdorovie/` etc. | `group_fp02_service_layout_hero` | Global default |
| O-centre | page | `/o-centre/` | `group_fp02_page_institutional` | `hero_cta_label` field (empty) + default |
| Contacts | page | `/kontakty/` | none | NO hero CTA |
| Legal / reviews | page | `/privacy-policy/`, `/otzyvy/` | none | NO hero CTA |

## Global hero absence (E22 preserved)

- No `Герои` under **Настройки сайта**
- No `group_fp02_block_hero_fallbacks`
- No `shpigovsky_get_block_hero_fallback_image()`

Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/baseline-local-hero-cta-audit.json`

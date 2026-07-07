# FP-0002 V9-06E24 Local Hero CTA Seed

Seeded `hero_cta_label` for hero-owning entities when empty.

| Context | Post ID | Seed value | Source |
|---|---:|---|---|
| Home | 4 | `Заказать звонок` | CURRENT_HARDCODED (site default) |
| Services hub | 5 | `Заказать звонок` | CURRENT_HARDCODED |
| Zavisimosti subdivision | 73 | `Заказать звонок` | CURRENT_HARDCODED |
| Alcohol leaf | 74 | `Записаться на консультацию` | V9_STATIC |
| Demo/narcotic leaves | 314–316 | `Заказать звонок` | CURRENT_HARDCODED |
| Psych / eating subdivisions | 77, 84 | `Заказать звонок` | CURRENT_HARDCODED |
| O-centre | 11 | `Заказать звонок` | CURRENT_HARDCODED |

**DB writes:** 10 (hero CTA postmeta only). No image/title/subtitle writes.

Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/local-hero-cta-seed-result.json`

# FP-0002 V9-06E26A Final About Page Contract v1

## Delivered state

| Item | Value |
|------|-------|
| Page ID | 11 |
| Route | `/o-centre/` |
| Template | `institutional.php` |
| Sections | 14 (full V9 stack) |
| Skeleton-only | **NO** |

## ACF

- Group: `group_fp02_page_institutional`
- Hub fields: `about_*`, `infrastructure_g0_g5`
- Hero: local `hero_cta_label` preserved

## Reusable blocks

- Specialists, reviews, CTA bands, final form — unchanged global options

## Child pages

- IDs 12–16: institutional template placeholder unchanged

## Known limitations

- Infrastructure gallery images: static theme asset paths (not WP media library)
- Visual screenshots: HTML marker validation only (headless)
- Program lead/intro: V9 static lorem placeholders retained

## Operator QA

- [ ] Admin: `/o-centre/` shows about ACF sections
- [ ] Frontend: all anchor sections present
- [ ] Mobile sanity on `/o-centre/`
- [ ] Regression routes 200

Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/final-e26a-about-page-contract.json`

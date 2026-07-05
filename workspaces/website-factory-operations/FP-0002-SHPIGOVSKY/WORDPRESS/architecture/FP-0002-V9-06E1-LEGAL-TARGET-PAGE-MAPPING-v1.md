# FP-0002 V9-06E1 Legal Target Page Mapping v1

**Phase:** V9-06E1  
**Date:** 2026-07-06

## Canonical mapping

| Static title | WP ID | Slug | Route | Result |
|---|---:|---|---|---|
| Политика конфиденциальности | 3 | privacy-policy | /privacy-policy/ | MAPPED |
| Пользовательское соглашение | 22 | user-agreement | /user-agreement/ | MAPPED |
| Согласие на обработку персональных данных | 23 | consent-personal-data | /consent-personal-data/ | MAPPED |
| Политика Cookie-файлов | 24 | cookie-files-policy | /cookie-files-policy/ | MAPPED |

## Privacy alignment

- **Canonical privacy page:** #3 `/privacy-policy/`
- **WP privacy setting target:** `wp_page_for_privacy_policy = 3`
- **Legacy system page #25** `/privacy-policy-page/`: preserved; not canonical; not seeded

## Footer / menu compatibility

Footer fallback and legal nav slugs unchanged. No menu mutation performed.

Evidence: `validation/v9-06e1-legal-static-copy-seed/legal-target-page-mapping.json`

# FP-0002 V9-06E0 — Native / Legal Page Inventory v1

**Phase:** V9-06E0  
**Date:** 2026-07-06  
**Mode:** READ-ONLY  
**Evidence:** `validation/v9-06e0-legal-native-content-review/native-legal-page-inventory.json`

---

## Scope

Thirteen page IDs from D9-M/D9-Z deferred and legal sets: **3, 6–10, 17, 19, 21–25**.

---

## Inventory summary

| Page ID | Title | Slug | Status | Native len | Template | Classification |
|--------:|-------|------|--------|------------:|----------|----------------|
| 3 | Политика конфиденциальности | privacy-policy | draft | 8736 | legal.php | GARBLED_LEGAL_SEED |
| 6 | Зависимости | zavisimosti | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 7 | Психическое здоровье | psihicheskoe-zdorovie | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 8 | Расстройства пищевого поведения | rasstroystva-pischevogo-povedeniya | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 9 | Генотипирование | genotipirovanie | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 10 | Специалисты | specyalisty | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 17 | Интервью и СМИ | intervyu-i-smi | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 19 | Статьи | blog | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 21 | Правовая информация | pravovaya-informaciya-pilzovatelyu | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |
| 22 | Пользовательское соглашение | user-agreement | publish | 0 | legal.php | TEMPLATE_MANAGED_EMPTY_OK |
| 23 | Согласие на обработку ПД | consent-personal-data | publish | 0 | legal.php | TEMPLATE_MANAGED_EMPTY_OK |
| 24 | Политика Cookie-файлов | cookie-files-policy | publish | 0 | legal.php | TEMPLATE_MANAGED_EMPTY_OK |
| 25 | Политика конфиденциальности (системная) | privacy-policy-page | publish | 169 | — | PLACEHOLDER_LOCAL_DEV |

---

## Key findings

1. **ID 3** — Canonical `/privacy-policy/` slug; **draft**; garbled WP privacy-policy seed in `post_content` (SHA256 unchanged from D9-M); native editor **retained**; in footer fallback and legal menu.
2. **IDs 22–24** — D9-M cleared to `post_content=0`; `legal.php` template; native editor **hidden** (D9-N); footer legal links active; frontend shows title shell only (`document-page.php` skeleton).
3. **ID 25** — WordPress `wp_page_for_privacy_policy` setting; placeholder stub; slug `/privacy-policy-page/`; **not** footer fallback target.
4. **IDs 6–10, 17, 19** — Identical local-dev placeholder paragraph (169 UTF-8 chars); native editor retained; mostly legacy routes superseded by CPT or deferred waves.

---

## Navigation exposure

| Surface | Page IDs |
|---------|----------|
| Footer legal fallback | 3, 22, 23, 24 |
| Legal nav menu (`legal`) | 21, 3, 22, 23, 24 |
| WP Privacy setting | 25 |

---

## Verdict

**CLASSIFIED** — all thirteen pages inventoried; no mutations performed.

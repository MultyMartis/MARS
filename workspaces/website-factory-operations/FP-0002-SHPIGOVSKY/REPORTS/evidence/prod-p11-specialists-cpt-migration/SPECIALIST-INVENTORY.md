# SPECIALIST-INVENTORY — PROD-P11 Stage A

**Captured:** 2026-08-14 (UTC) via SSH MySQL READ-ONLY  
**Hub:** `/specyalisty/` page `#1030` (`post_type=page`, publish, parent 0)  
**Ownership before migration:** Specialist profiles = **child pages** of hub `#1030`  
**Template:** all children use `page-templates/generic.php`  
**Structured fields:** ACF group `group_fp02_specialist_profile` (P08)

## Count

**4** Specialist child pages.

## Inventory

| ID | Slug | Title | Status | Parent | menu_order | Featured image | Cert gallery IDs | Public URL | HTTP |
|----|------|-------|--------|--------|------------|----------------|------------------|------------|------|
| 1031 | shipovsky | Сергей Юрьевич Шпиговский | publish | 1030 | 10 | 1092 | — | `/specyalisty/shipovsky/` | 200 |
| 1032 | kazakov | Максим Михайлович Казаков | publish | 1030 | 20 | 1094 | — | `/specyalisty/kazakov/` | 200 |
| 1033 | kostyuk | Дарья Владимировна Костюк | publish | 1030 | 30 | 1096 | 1853, 1855, 1854 | `/specyalisty/kostyuk/` | 200 |
| 1097 | shapiguzova | Шапигузова Татьяна Андреевна | publish | 1030 | 40 | 1821 | — | `/specyalisty/shapiguzova/` | 200 |

## ACF / content notes

| ID | role | experience | structured WYSIWYG | additional | generic_page_body (legacy) |
|----|------|------------|--------------------|------------|----------------------------|
| 1031 | Аддиктолог, интервенционист | empty | mostly empty | present | preserved (len 312) |
| 1032 | Психолог… | empty | mostly empty | present | preserved (len 338) |
| 1033 | Психолог, EMDR… | Опыт — 2,5 года | fuller profile | empty | preserved (len 1807) |
| 1097 | Гонг-мастер… | empty | mostly empty | present | preserved (len 367) |

## SEO / Search / Sitemap (pre-migration)

- Smart Search group **Специалисты** classifies hub child pages (P09/P10).
- Sitemap provider `wp-sitemap-specialists-1.xml` lists the same child pages.
- SEO ownership: no Yoast/RankMath specialist-specific meta observed in interest keys; titles from `post_title`.
- Canonical public host: `http://shpigovsky.beget.tech/` (temporary Beget).

## Hub page `#1030`

- Remains a **page** with Generic Content template.
- Body is placeholder copy (not a live card listing).
- Listing owner for cards/sliders: `shpigovsky_get_specialists_cards()` (was page children → will be CPT).

## Snapshots

Exact DB row dumps:

`X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p11-db-snapshots\`

- `post-{ID}-wp_posts.sql` + `.sha256`
- `post-{ID}-wp_postmeta.sql` + `.sha256`
- `hub-1030-*.sql`
- `inventory-raw.json`

## Migration plan (IDs only)

`1031, 1032, 1033, 1097`: `post_type page → specialist`; `post_parent → 0` after URL proof.

**No mutation in Stage A.**

# SITE-002 — STABLE PRODUCTION — Catalog Sort Menu Order

**Status:** **ACTIVE** — third controlled Production change verified  
**Environment:** PRODUCTION (`site-002-prod`)  
**URL:** https://bzpm.ru/  
**Date:** 2026-07-06  
**OCPilot run:** 4.177  
**Operation ID:** SITE-002-PROD-SORT-MENU-ORDER-01  
**Parent checkpoint:** SITE-002-STABLE-PROD-SORT-AZ-01

---

## Scope

Third controlled Production mutation for SITE-002. Catalog sort dropdown order corrected in one Twig template only; «Умолчанию» removed.

| Field | Value |
|-------|-------|
| Remote target | `/public_html/catalog/view/theme/default/template/product/category.twig` |
| Changed files | 1 |
| Change type | catalog sort menu order |
| Removed item | «Умолчанию» (`sort=p.date_added&order=DESC`) |
| Menu order | `pd.name ASC` → `pd.name DESC` → `p.price ASC` → `p.price DESC` |
| Default catalog sort (controller) | unchanged — `pd.name ASC` (Run 4.176) |
| Uploads | 1 |
| Deletes / renames | 0 / 0 |
| Database operations | 0 |
| Admin saves | 0 |
| Controller / CSS / JS | **not modified** |

---

## Verification

| Gate | Result |
|------|--------|
| Fresh Production file downloaded | PASS |
| Backup + rollback copies (SHA match) | PASS |
| Precondition (single `data-sort-menu` block, 5 sort items) | PASS |
| Dry-run scope (`data-sort-menu` only) | PASS |
| Pre-upload remote SHA unchanged | PASS |
| Remote hash after upload | PASS |
| HTTP `/katalog/nejtralnoe-oborudovanie/stoly` | PASS — 200 |
| Sort menu order + «Умолчанию» absent | PASS |
| Default visible sort A→Я | PASS |
| Sort action URLs (4 variants) | PASS — 200 |
| Desktop screenshot 1440×1200 | PASS |
| Mobile screenshot 390×844 | PASS |

---

## Hashes

| Item | SHA-256 |
|------|---------|
| Source / rollback | `2b325d8ac349c89efbc400f29ff9be740fecda3bc40079f7a5b861bcb8e6a92b` |
| Prepared / remote after upload | `91fda8da557963a601fc1cd5fc4c21c3711faf7e6e97f0efe8308769484a23c9` |

---

## Storage binding

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-SORT-MENU-ORDER-01\
```

Operation evidence:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SORT-MENU-ORDER-01\
```

---

## Rollback authority

Rollback file: `rollback/category.twig` from fresh Production source (SHA matches source hash).

Procedure:

1. Upload `rollback/category.twig` to `/public_html/catalog/view/theme/default/template/product/category.twig`.
2. Download remote file; verify SHA-256 equals source hash.
3. Confirm category pages return HTTP 200 and sort menu restores prior order with «Умолчанию».

---

## Proven deploy class

```text
single-Twig-file FTP deploy with backup, dry-run, verification, rollback readiness
```

Does **not** prove multi-file frontend deploy, CSS/JS deploy, cache clearing, or database operations.

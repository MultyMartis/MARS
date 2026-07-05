# SITE-002 — STABLE PRODUCTION — Catalog Default Sort A→Я

**Status:** **ACTIVE** — second controlled Production change verified  
**Environment:** PRODUCTION (`site-002-prod`)  
**URL:** https://bzpm.ru/  
**Date:** 2026-07-05  
**OCPilot run:** 4.176  
**Operation ID:** SITE-002-PROD-SORT-AZ-01  
**Parent checkpoint:** SITE-002-STABLE-PROD-TEXT-CHANGE-01

---

## Scope

Second controlled Production mutation for SITE-002. Default catalog sort changed in one PHP controller only.

| Field | Value |
|-------|-------|
| Remote target | `/public_html/catalog/controller/product/category.php` |
| Changed files | 1 |
| Change type | catalog default sort |
| Old default | `sort = p.date_added`, `order = DESC` |
| New default | `sort = pd.name`, `order = ASC` |
| Uploads | 1 |
| Deletes / renames | 0 / 0 |
| Database operations | 0 |
| Admin saves | 0 |
| Twig / CSS / JS | **not modified** |

---

## Verification

| Gate | Result |
|------|--------|
| Fresh Production file downloaded | PASS |
| Backup + rollback copies (SHA match) | PASS |
| Precondition (OpenCart category controller) | PASS |
| Dry-run scope (2 default lines only) | PASS |
| Pre-upload remote SHA unchanged | PASS |
| Remote hash after upload | PASS |
| HTTP `/katalog/nejtralnoe-oborudovanie/stoly` | PASS — 200 |
| HTTP `/katalog/nejtralnoe-oborudovanie` | PASS — 200 |
| Sort label «Название - от А до Я» | PASS |
| Limit selector present | PASS |
| Desktop screenshot 1440×1200 | PASS |
| Mobile screenshot 390×844 | PASS |

---

## Hashes

| Item | SHA-256 |
|------|---------|
| Source / rollback | `05bf86805989471c411a27d07fdc7bd5216a090b0592c5e4407d8aedd0040db2` |
| Prepared / remote after upload | `82333135b35de8ed90a95ef321f0cbd125fe0e87293eb5244d77521377849f96` |

---

## Storage binding

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-SORT-AZ-01\
```

Operation evidence:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SORT-AZ-01\
```

---

## Rollback authority

Rollback file: `rollback/category.php` from fresh Production source (SHA matches source hash).

Procedure:

1. Upload `rollback/category.php` to `/public_html/catalog/controller/product/category.php`.
2. Download remote file; verify SHA-256 equals source hash.
3. Confirm category pages return HTTP 200 and default sort restores to `p.date_added DESC`.

---

## Proven deploy class

```text
single-controller-file FTP deploy with backup, dry-run, verification, rollback readiness
```

Does **not** prove multi-file frontend deploy, Twig/CSS deploy, cache clearing, or database operations.

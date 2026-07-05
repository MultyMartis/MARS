# REPORT — SITE-002 Production Catalog Sort Menu Order

**OCPilot run:** 4.177  
**Operation ID:** SITE-002-PROD-SORT-MENU-ORDER-01  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/

---

## 1. Scope

Controlled single-Twig Production deploy: reorder catalog sort dropdown in `category.twig`; remove «Умолчанию»; preserve Run 4.176 default sort (`pd.name ASC` in controller).

| Allowed | Forbidden (not touched) |
|---------|-------------------------|
| `category.twig` (sort menu block) | `category.php`, CSS, JS, model |
| FTP read/upload (1 file) | Database, admin, cache clear |
| Backup, dry-run, verification | Operator unrelated Twig/CSS WIP |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-task) | `c188cd2ec94dfba47efd2c9ce6e26ff768ce9982` |
| Staged files | **none** |
| Parent checkpoint | `SITE-002-STABLE-PROD-SORT-AZ-01` |

**Foreign WIP (not staged, not touched):**

- FP-0002 modified paths under `workspaces/fp-0002-*` and `projects/mars-website-factory/...`
- SITE-002 untracked backup copies under `projects/ocpilot/sites/site-002/backups/*.twig.bak`, `*.css.bak`
- `.recovery-temp/` untracked artefacts

No SITE-002 Twig/CSS tracked modifications in git index.

---

## 3. Operator WIP protection

- Source of truth: **fresh live FTP download** immediately before edit.
- No repo baseline or July capture used as deploy source.
- Only `data-sort-menu` block modified; all other live Twig content preserved.
- CSS not touched.

---

## 4. Target file discovery

| Field | Value |
|-------|-------|
| FTP-visible path | `/public_html/catalog/view/theme/default/template/product/category.twig` |
| Hosting path | `/bzpm.ru/public_html/catalog/view/theme/default/template/product/category.twig` |
| Discovery | `data-sort-menu` found once with full catalog sort buttons |
| Secondary note | `search.twig` contains stub sort menu without `data-sort` attributes — **out of scope** |

---

## 5. Live source acquisition

Download timestamp: `2026-07-05T17:06:37+00:00`

| Copy | Path |
|------|------|
| Source | `deployments/.../source/category.twig` |
| Backup | `deployments/.../backup/category.twig.pre-sort-menu-order.bak` |
| Rollback | `deployments/.../rollback/category.twig` |

**SHA-256 (all three match):** `2b325d8ac349c89efbc400f29ff9be740fecda3bc40079f7a5b861bcb8e6a92b`

Remote metadata: size 6507 bytes; MDTM `213 20260701180721`

---

## 6. Preconditions

| Check | Result |
|-------|--------|
| Single `data-sort-menu` block | PASS |
| «Умолчанию» (`p.date_added DESC`) present | PASS |
| Price ASC/DESC items present | PASS |
| Name ASC/DESC items present | PASS |
| Menu not PHP-generated array | PASS — static Twig buttons |
| Controller default sort compatible | PASS — `{{ sorttext }}` unchanged |

Live markup uses `data-sort-menu hidden` and plain `&` in `data-sort` attributes (not HTML entities).

---

## 7. Backup and rollback readiness

- Backup and rollback copies created from identical live source.
- Rollback plan: `manifests/rollback-plan.json`
- Rollback upload target: same remote path; source hash verified.

---

## 8. Dry-run

| Field | Value |
|-------|-------|
| Remote files to upload | 1 |
| Database impact | NONE |
| Controller/CSS/JS impact | NONE |
| Diff scope | **PASS** — `data-sort-menu` block only |
| Removed | «Умолчанию» button |
| Final order | A→Я, Я→А, cheaper, expensive |

Manifests: `manifests/dry-run.json`, `manifests/dry-run.md`, `manifests/category.diff`

---

## 9. Deploy

| Field | Value |
|-------|--------|
| Pre-upload remote SHA | matched source |
| Upload count | 1 |
| Remote target | `/public_html/catalog/view/theme/default/template/product/category.twig` |
| Deletes / renames | 0 / 0 |

**Prepared SHA-256:** `91fda8da557963a601fc1cd5fc4c21c3711faf7e6e97f0efe8308769484a23c9`

---

## 10. File-level verification

| Check | Result |
|-------|--------|
| Remote after-upload SHA == prepared | PASS |
| «Умолчанию» absent in menu | PASS |
| Button order keys | PASS |
| No extra items removed | PASS |

---

## 11. HTTP verification

Primary URL: https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly

| Check | Result |
|-------|--------|
| HTTP status | 200 |
| PHP/Twig errors | none |
| Product grid | renders |
| Sort menu labels (4 items, correct order) | PASS |
| «Умолчанию» absent | PASS |
| Default visible sort A→Я | PASS |
| Limit selector | present |
| Explicit sort URLs (4 variants) | PASS — 200 |

Parent hub URL `/katalog/nejtralnoe-oborudovanie` uses hub layout without product sort menu — excluded from sort-menu gate (not cache failure).

Manifests: `manifests/http-verification.json`, `manifests/http-verification-supplement.json`

---

## 12. Visual verification

| Viewport | File | Result |
|----------|------|--------|
| Desktop 1440×1200 | `verification/desktop-stoly-sort-menu-order.png` | PASS |
| Desktop open menu | `verification/desktop-stoly-sort-menu-open.png` | PASS |
| Mobile 390×844 | `verification/mobile-stoly-sort-menu-order.png` | PASS |
| Mobile open menu | `verification/mobile-stoly-sort-menu-open.png` | PASS |

Manifest: `manifests/visual-verification.json`

---

## 13. Rollback status

**Not executed** — deploy and verification passed; rollback file retained and hash-verified.

---

## 14. Storage artefacts

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SORT-MENU-ORDER-01\
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-SORT-MENU-ORDER-01\
```

Tool: `projects/ocpilot/sites/site-002/tools/site-002-prod-sort-menu-order-01.py`

---

## 15. Checkpoint

**Issued:** `SITE-002-STABLE-PROD-SORT-MENU-ORDER-01`  
**Parent:** `SITE-002-STABLE-PROD-SORT-AZ-01`  
Repository: [baselines/SITE-002-STABLE-PROD-SORT-MENU-ORDER-01.md](../baselines/SITE-002-STABLE-PROD-SORT-MENU-ORDER-01.md)

---

## 16. Authority updates

Updated: `OCPILOT-STATE.md`, `OPERATIONAL-INDEX.md`, `production-profile.md`, `site-passport.md`, `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`

---

## 17. Remote mutation summary

| Operation | Count |
|-----------|------:|
| Remote uploads | 1 |
| Remote edits through upload | 1 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Database operations | 0 |
| Admin saves | 0 |
| Cache clears | 0 |

---

## 18. Git status

Docs/report/checkpoint only staged selectively after this report. Storage artefacts and live Twig copies excluded from git.

---

## 19. Final verdict

**SITE-002 CATALOG SORT MENU ORDER COMPLETE — DEPLOY AND ROLLBACK READINESS VERIFIED**

Catalog sort menu on product-listing category pages:

1. Название — от А до Я  
2. Название — от Я до А  
3. Сначала дешевле  
4. Сначала дороже  

«Умолчанию» removed. Default visible sort remains A→Я (Run 4.176 controller default).

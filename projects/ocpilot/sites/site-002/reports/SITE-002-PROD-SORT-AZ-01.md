# REPORT — SITE-002 Production Catalog Default Sort A→Я

**OCPilot run:** 4.176  
**Operation ID:** SITE-002-PROD-SORT-AZ-01  
**Date:** 2026-07-05  
**Environment:** PRODUCTION — https://bzpm.ru/

---

## 1. Scope

Controlled single-file Production deploy: change default catalog sort from `p.date_added DESC` to `pd.name ASC` in `category.php` only.

| Allowed | Forbidden (not touched) |
|---------|-------------------------|
| `category.php` controller | Twig, CSS, JS |
| FTP read/upload (1 file) | Database, admin, cache clear |
| Backup, dry-run, verification | Operator Twig/CSS WIP |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `72391b6fdddaf72114722cf7d15d1ed7d1844166` |
| Staged files | **none** |
| Parent checkpoint | `SITE-002-STABLE-PROD-TEXT-CHANGE-01` |
| Run 4.174 contamination | Documented in Run 4.175 — not rewritten |

**Foreign WIP (not staged, not touched):**

- FP-0002 modified paths under `workspaces/fp-0002-*` and `projects/mars-website-factory/...`
- SITE-002 untracked backup copies under `projects/ocpilot/sites/site-002/backups/*.twig.bak`, `*.css.bak`
- `.recovery-temp/` untracked artefacts

No SITE-002 Twig/CSS tracked modifications in git index.

---

## 3. Operator WIP protection

- Source of truth: **fresh live FTP download** immediately before edit (not July baseline).
- No Twig or CSS deployed.
- No baseline copies used to overwrite live Production.
- Line endings and unrelated whitespace preserved.

---

## 4. Target file

| Field | Value |
|-------|-------|
| Hosting path | `/bzpm.ru/public_html/catalog/controller/product/category.php` |
| FTP-visible path | `/public_html/catalog/controller/product/category.php` |
| File size (live) | 23067 bytes |
| FTP MDTM | `213 20260701180721` |

---

## 5. Live source acquisition

Download timestamp: `2026-07-05T16:57:27+00:00`

| Copy | Path |
|------|------|
| Source | `deployments/.../source/category.php` |
| Backup | `deployments/.../backup/category.php.pre-sort-az.bak` |
| Rollback | `deployments/.../rollback/category.php` |

**SHA-256 (all three match):** `05bf86805989471c411a27d07fdc7bd5216a090b0592c5e4407d8aedd0040db2`

---

## 6. Preconditions

| Check | Result |
|-------|--------|
| OpenCart `ControllerProductCategory` | PASS |
| Default sort `p.date_added` (single occurrence) | PASS |
| Default order `DESC` (single occurrence) | PASS |
| Explicit `sort`/`order` request override preserved | PASS |
| `pd.name ASC` sorttext rule present | PASS |
| Model/template change required | **NO** |

`sorttext` initial value `Умолчанию` left unchanged — existing conditional `($sort == 'pd.name') AND ($order == 'ASC')` sets label to «Название - от А до Я» when defaults apply.

---

## 7. Backup and rollback readiness

- Backup and rollback copies created from identical live source.
- Rollback plan: `manifests/rollback-plan.json`
- Rollback upload target: same remote path, source hash verified.

---

## 8. Dry-run

| Field | Value |
|-------|-------|
| Remote files to upload | 1 |
| Database impact | NONE |
| Twig/CSS/JS impact | NONE |
| Diff scope | **PASS** — 2 lines only |

```diff
-			$sort = 'p.date_added';
+			$sort = 'pd.name';
-			$order = 'DESC';
+			$order = 'ASC';
```

Manifests: `manifests/dry-run.json`, `manifests/dry-run.md`, `manifests/category.diff`

---

## 9. Deploy

Pre-upload remote SHA matched source SHA.

| Operation | Count |
|-----------|-------|
| Uploads | 1 |
| Deletes | 0 |
| Renames | 0 |

Upload: `prepared/category.php` → `/public_html/catalog/controller/product/category.php`

---

## 10. File-level verification

| Hash | Value |
|------|-------|
| prepared_sha256 | `82333135b35de8ed90a95ef321f0cbd125fe0e87293eb5244d77521377849f96` |
| remote_after_sha256 | `82333135b35de8ed90a95ef321f0cbd125fe0e87293eb5244d77521377849f96` |

Remote content checks after upload:

- Default sort fallback = `pd.name` — PASS
- Default order fallback = `ASC` — PASS
- Old default `$sort = 'p.date_added'` assignment removed — PASS

---

## 11. HTTP verification

| URL | Status | Notes |
|-----|--------|-------|
| `/katalog/nejtralnoe-oborudovanie/stoly` | 200 | Sort label «от А до Я» visible; limit selector present; no PHP/Twig errors |
| `/katalog/nejtralnoe-oborudovanie` | 200 | Product grid renders; no errors |

Explicit sort links (`date_added`, `pd.name DESC`, price sorts) remain in page HTML.

Manifest: `manifests/http-verification.json`

---

## 12. Visual verification

| Viewport | File | Status |
|----------|------|--------|
| Desktop 1440×1200 | `verification/desktop-stoly-sort-az.png` | PASS |
| Mobile 390×844 | `verification/mobile-stoly-sort-az.png` | PASS |

Sort label present; no Twig/PHP error text; body content rendered.

---

## 13. Rollback status

**Not executed** — deploy and verification passed. Rollback file ready at `rollback/category.php`.

---

## 14. Storage artefacts

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SORT-AZ-01\
  source\  prepared\  backup\  verification\  rollback\  manifests\  logs\
```

Baseline copy:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-SORT-AZ-01\
```

Deploy utility (repo): `projects/ocpilot/sites/site-002/tools/site-002-prod-sort-az-01.py`

---

## 15. Checkpoint

**ISSUED:** `SITE-002-STABLE-PROD-SORT-AZ-01`

- Repository: [../baselines/SITE-002-STABLE-PROD-SORT-AZ-01.md](../baselines/SITE-002-STABLE-PROD-SORT-AZ-01.md)
- Parent: `SITE-002-STABLE-PROD-TEXT-CHANGE-01`

---

## 16. Authority updates

Updated in this operation wave:

- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/OPERATIONAL-INDEX.md` (Run 4.176)
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`

---

## 17. Remote mutation summary

| Operation | Count |
|-----------|-------|
| Remote uploads | 1 |
| Remote edits through upload | 1 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Database operations | 0 |
| Admin saves | 0 |
| Cache clears | 0 |

---

## 18. Git status

Repository docs/report/checkpoint staged selectively after this report. Storage artefacts, secrets, live Production files, screenshots, and foreign WIP excluded from commit.

---

## 19. Final verdict

**SITE-002 CATALOG DEFAULT SORT A→Я COMPLETE — DEPLOY AND ROLLBACK READINESS VERIFIED**

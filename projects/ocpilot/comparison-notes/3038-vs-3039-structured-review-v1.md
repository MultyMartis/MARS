# Structured Difference Review — ocStore 3.0.3.8 (rs.2) vs 3.0.3.9 (rs.1)

**Purpose:** evidence-based comparison of promoted reference baselines after Run 3.5 file promotion.

**Date:** 2026-05-30  
**Method:** relative path set comparison on `baselines/.../files/` trees — **no** byte-level diff of all files.

**Sources:**

- `baselines/ocstore-3038-rs2/files/` — 4055 files
- `baselines/ocstore-3039-rs1/files/` — 3553 files

**Related:** [run-3-initial-comparison-v1.md](../run-3-initial-comparison-v1.md), [baseline-comparison-methodology.md](../baseline-comparison-methodology.md)

---

## Version identity (verified)

| Baseline | VERSION constant | rs label | Evidence |
|----------|------------------|----------|----------|
| ocstore-3038-rs2 | `3.0.3.8` | rs.2 | `files/index.php` → `define('VERSION', '3.0.3.8')` |
| ocstore-3039-rs1 | `3.0.3.9` | rs.1 | `files/index.php` → `define('VERSION', '3.0.3.9')` |

rs build numbers from package folder names — **not** independently verified against ocstore.com release notes.

---

## File counts (promoted trees)

| Area | 3038-rs2 | 3039-rs1 | Delta (3039 − 3038) |
|------|----------|----------|---------------------|
| **Total files** | 4055 | 3553 | **−502** |
| `admin/` (path contains) | 1315 | 1325 | +10 |
| `catalog/` | 794 | 793 | −1 |
| `image/` | 154 | 173 | +19 |
| `install/` | 112 | 117 | +5 |
| `system/` | 1912 | 1391 | **−521** |

Path-based counts include nested paths (e.g. admin language files under other dirs may be counted in area totals). Top-level directory file counts from Run 3 manifest remain valid for archive-level reference.

---

## Path set comparison (relative paths)

| Metric | Count |
|--------|------:|
| Paths only in 3038-rs2 | 896 |
| Paths only in 3039-rs1 | 394 |
| Common paths (same relative path in both) | 3159 |

**Interpretation:** 502 net file-count reduction in 3039 is consistent with large vendor/pruning delta under `system/` plus path renames/additions elsewhere. Exact semantic reason for each removed path — **SAFE UNKNOWN** without per-file classification.

---

## `system/` difference

| Metric | Value |
|--------|------:|
| Paths only in 3038-rs2 under `system/` | 853 |
| Paths only in 3039-rs1 under `system/` | 332 |
| `system/storage/vendor/` file paths | 1809 (3038) vs 1291 (3039) |
| `system/storage/modification/` paths | 26 (3038) vs 23 (3039) |

### Top-level `system/` children

Both baselines share identical top-level entries:

```
.htaccess, config/, engine/, framework.php, helper/, library/, modification.xml,
startup.php, storage/, tweak.ocmod.xml, tweak-54fz.ocmod.xml
```

### Notable `system/` evidence (samples only)

**Only in 3038-rs2 (examples):**

- Older Guzzle 5-era paths under `system/storage/vendor/guzzlehttp/guzzle/src/` (e.g. `BatchResults.php`, `Collection.php`, `Mimetypes.php`)
- Cardinity SDK paths under `Method/Void/` naming
- `system/storage/modification/admin/view/template/catalog/category_form.twig` (and related modification cache twig files)
- `system/storage/vendor/bin/pscss.bat`

**Only in 3039-rs1 (examples):**

- Guzzle 6+ style paths (`HandlerStack.php`, `Middleware.php`, `RedirectMiddleware.php`, …)
- Cardinity SDK renamed to `Method/VoidPayment/` paths
- Composer 2 metadata: `system/storage/vendor/composer/installed.php`, `InstalledVersions.php`, `platform_check.php`

**Evidence-based conclusion:** Major `system/` delta aligns with **Composer vendor dependency refresh** (especially Guzzle and payment SDKs) and **modification cache template differences** — not with live operational storage. Full vendor version matrix — **SAFE UNKNOWN** without parsing `composer.lock` / `installed.json` per package.

---

## `install/` difference

| Metric | Value |
|--------|------:|
| Paths only in 3038-rs2 under `install/` | 2 |
| Paths only in 3039-rs1 under `install/` | 7 |

**Only in 3038-rs2:**

- `install/view/javascript/jquery/jquery-2.1.1.min.js`
- `install/view/javascript/jquery/jquery-2.1.1.min.map`

**Only in 3039-rs1:**

- `install/view/javascript/jquery/jquery-3.7.0.min.js`
- `install/view/javascript/jquery/jquery-3.7.0.min.map`
- Bootstrap source maps: `bootstrap-theme.css.map`, `bootstrap-theme.min.css.map`, `bootstrap.css.map`, `bootstrap.min.css.map`
- `install/view/javascript/bootstrap/js/npm.js`

**Evidence-based conclusion:** Installer front-end assets updated (jQuery 2.1.1 → 3.7.0; additional Bootstrap map/npm files in 3039). Core PHP install logic may also differ in shared paths — **SAFE UNKNOWN** without diff of common install PHP files.

---

## `admin/` and `catalog/` difference

| Area | Only in 3038 | Only in 3039 |
|------|-------------:|-------------:|
| `admin/` | 25 | 38 |
| `catalog/` | 16 | 17 |
| `image/` | 0 | 0 |

**Evidence:** Non-zero admin/catalog path deltas exist; specific functional areas (controllers, languages, extensions) not classified in this run — **SAFE UNKNOWN** for feature-level changelog.

---

## Notable package / integration differences

| Signal | 3038-rs2 | 3039-rs1 | Notes |
|--------|----------|----------|-------|
| `wechat` path matches | 26 | 96 | More WeChat-related vendor/integration files in 3039 |
| `deleted-files.zip` (root) | 1 190 104 B | 1 084 625 B | Different nested archive size |
| `install/opencart.sql` | 192 868 B | 193 177 B | Same 136 table names; content diff not fully analyzed |
| ocStore OCMOD pair | present | present | `tweak.ocmod.xml`, `tweak-54fz.ocmod.xml` |
| `ru-ru/` locale | present | present | Run 3: 348 paths each in archive listing |

---

## ocStore vs upstream OpenCart

**SAFE UNKNOWN** — repo has no pinned upstream OpenCart 3.0.3.8 / 3.0.3.9 clean baselines for subtraction.

---

## Comparison workflow implications

1. Site on **3.0.3.8 rs.2** → compare against `ocstore-3038-rs2` only.
2. Site on **3.0.3.9 rs.1** → compare against `ocstore-3039-rs1` only.
3. Cross-version diff (this document) is for **baseline understanding**, not site audit substitution.
4. Large `system/storage/vendor/` deltas mean extension/payment audits must use **version-matched** baseline.

---

## SAFE UNKNOWN

- Byte-identical vs modified files among 3159 common paths.
- Complete list of 896 / 394 unique paths (available via regenerate path-set diff; not embedded here).
- Semantic changelog from ocStore vendor release notes.
- Contents of nested `deleted-files.zip` in each baseline.
- Whether admin/catalog path deltas map to specific features or bugfixes.

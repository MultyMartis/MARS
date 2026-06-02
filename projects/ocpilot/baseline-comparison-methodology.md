# OCPilot — Baseline Comparison Methodology

**Purpose:** define how OCPilot compares a **project site** against a **versioned clean baseline** across layered dimensions — without confusing core, ocStore, extensions, theme, and custom code.

**Status:** documented methodology only; **no** automated diff tool claimed.

---

## Comparison goal

Given evidence from a project site (read-only audit) and a ready baseline (see [baseline-readiness-checklist.md](baseline-readiness-checklist.md)), classify every observed difference:

| Class | Meaning |
|-------|---------|
| **OpenCart core** | Vendor file or schema expected in upstream OpenCart for that version |
| **ocStore modification** | File or schema change introduced by ocStore distribution vs plain OpenCart |
| **Third-party extension** | Module, payment, shipping, feed, SEO tool — vendor is not OpenCart/ocStore |
| **Theme modification** | Template, stylesheet, layout override in active theme path |
| **Project customization** | Site-specific logic, custom controllers/models, one-off patches |
| **SAFE UNKNOWN** | Insufficient evidence to classify — must not be assumed |

---

## Comparison order

Always proceed **top to bottom**. Do not skip to theme or extensions before platform and version are confirmed.

```
1. Confirm platform (OpenCart vs ocStore) and version
2. Verify baseline readiness
3. Layer 1 — Core OpenCart
4. Layer 2 — ocStore (if applicable)
5. Layer 3 — Theme
6. Layer 4 — Extensions
7. Layer 5 — Project customizations
```

### What to compare first

| Priority | Question | Evidence source |
|----------|----------|-----------------|
| 1 | Is this OpenCart or ocStore? Exact version? | Admin footer, `index.php`, version file, operator brief |
| 2 | Does a ready baseline exist for that platform+version? | [baseline-readiness-checklist.md](baseline-readiness-checklist.md) |
| 3 | Which files differ from **OpenCart core** baseline? | File tree vs `baselines/opencart-*/files/` or ocStore equivalent |
| 4 | Which differences are **ocStore-known**? | `comparison-notes/` on ocStore baseline |
| 5 | Which differences live under **theme paths**? | `catalog/view/theme/<theme>/`, admin view overrides |
| 6 | Which paths match **extension** conventions? | `catalog/controller/extension/`, `system/library/`, ocMod XML |
| 7 | What remains **project-specific**? | Custom routes, dealership logic, non-vendor naming |

### What should never be assumed

- A changed file in `system/` is **not** automatically «custom» — could be ocStore or ocMod.
- A file under `catalog/view/theme/` is **not** automatically «theme only» — may embed PHP logic via modifications.
- An extra DB table is **not** automatically «extension» — verify against baseline schema metadata.
- Matching version **major** is **not** enough — 3.0.2.x vs 3.0.3.7 can produce false diffs.
- Empty baseline folders do **not** mean «no differences» — means **comparison blocked**.

---

## Layer 1 — Core OpenCart comparison

**Baseline:** `baselines/opencart-<version>/` (or ocStore baseline for ocStore-only core paths after Layer 2).

**Scope:** vendor directories and files expected in a clean OpenCart install:

- `admin/` (core controllers, models, language — not third-party extensions)
- `catalog/` (core — excluding `extension/` subtree and theme overrides)
- `system/` (engine, library core — caution: ocMod may alter)
- Root entry files (`index.php`, `.htaccess` patterns)

**Method:**

1. Match site version to baseline folder.
2. Compare path presence: missing core file vs added file vs modified file.
3. Record hash/size/content notes in site `opencart-analysis/` — not necessarily full binary in repo.

**Examples:**

| Observation | Classification |
|-------------|----------------|
| `catalog/controller/product/product.php` differs from OpenCart 3.0.3.7 baseline | **Investigate** — could be ocMod, ocStore, or custom; not auto-labeled |
| `system/engine/router.php` missing on site | **SAFE UNKNOWN** until evidence — could be path rewrite or incomplete export |
| Site runs 3.0.3.7, baseline is 2.3.0 | **Block comparison** — wrong baseline |

---

## Layer 2 — ocStore comparison

**Apply when:** project site is **ocStore**, not plain OpenCart.

**Baseline:** `baselines/ocstore-<version>/` + `comparison-notes/`.

**Scope:** known ocStore deltas vs upstream OpenCart for the same version line:

- Modified core files shipped with ocStore
- Additional admin/catalog files in ocStore package
- Schema differences documented in baseline `database/` metadata

**Method:**

1. After Layer 1 raw diff, subtract differences documented in baseline `comparison-notes/`.
2. Remaining core-path diffs → candidate **extension**, **ocMod**, or **project custom**.

**Examples:**

| Observation | Classification |
|-------------|----------------|
| File changed in ocStore baseline `comparison-notes/` as known ocStore patch | **ocStore modification** |
| Extra table `oc_*` documented in ocStore schema metadata | **ocStore modification** |
| File changed on site but **not** in ocStore notes and **not** in OpenCart baseline | **Extension or project custom** — Layer 4/5 |

**Plain OpenCart site:** skip Layer 2; use OpenCart baseline only.

---

## Layer 3 — Theme comparison

**Scope:** presentation layer — templates, assets, theme config.

Typical paths (version-dependent):

- `catalog/view/theme/<active-theme>/`
- `catalog/view/javascript/`, `catalog/view/stylesheet/` (theme-linked)
- Admin theme overrides if present

**Method:**

1. Identify active theme name from site audit.
2. Compare theme subtree to baseline **default theme** structure (usually `default` in clean install).
3. Classify: **vendor default theme** | **third-party theme** | **project overrides**.

**Examples:**

| Observation | Classification |
|-------------|----------------|
| Custom `product.twig` / `product.tpl` in active theme | **Theme modification** |
| New template `dealership_locations.twig` | **Project customization** (if not from theme package) |
| Changed `stylesheet.css` with dealership branding | **Theme modification** |

Theme changes do **not** explain backend controller logic — cross-check Layer 5.

---

## Layer 4 — Extensions comparison

**Scope:** modules, payments, shipping, feeds, SEO, import tools.

Typical paths:

- `catalog/controller/extension/`
- `admin/controller/extension/`
- `catalog/model/extension/`
- `system/config/*.php` for extension configs (metadata only — no secrets)
- ocMod: `system/*.ocmod.xml` or modification cache paths
- vQmod (2.x legacy): `vqmod/` if present

**Method:**

1. Inventory extension entries from admin (read-only) or file tree.
2. Match against baseline — clean baseline typically has **no** third-party extensions installed.
3. Each extension directory or ocMod XML → **third-party extension** unless proven project-authored.

**Examples:**

| Observation | Classification |
|-------------|----------------|
| Added module `catalog/controller/extension/module/filter.php` | **Third-party extension** (verify vendor) |
| ocMod XML modifying `catalog/model/catalog/product.php` | **Extension via ocMod** — trace to XML author |
| Payment module under `catalog/controller/extension/payment/` | **Third-party extension** |

---

## Layer 5 — Project customizations

**Scope:** site-specific logic not attributable to vendor core, ocStore, theme package, or named extension.

Typical signals:

- Custom controllers outside `extension/` namespace
- Dealership-specific models or language keys
- One-off SQL migrations in operator notes
- Hard-coded business rules in modified core files (after ruling out ocStore/ocMod)

**Method:**

1. Apply only after Layers 1–4 exhausted.
2. Document in site `controller-analysis/`, `database-analysis/`, `opencart-analysis/`.
3. Mark rollback scope: project custom is usually safe to revert **if** dependencies mapped.

**Examples:**

| Observation | Classification |
|-------------|----------------|
| `catalog/controller/information/dealer_map.php` — not in any baseline | **Project customization** |
| Modified `product.php` controller after ocMod ruled out | **Project customization** or **unsafe ocMod** — verify |
| Custom table `oc_dealer_stock` not in any baseline schema | **Project customization** (DB layer) |

---

## Database comparison (cross-cutting)

After file layers, compare schema evidence:

| Check | Baseline source |
|-------|-----------------|
| Table prefix | passport + `database/` metadata |
| Core tables present | baseline schema metadata |
| Extra tables | likely extension or project custom |
| Modified core table columns | ocStore note, extension, or project custom |

**Never assume** extra tables are «safe to drop» without classification.

---

## Recording outputs

| Output location | Content |
|-----------------|---------|
| `sites/<slug>/opencart-analysis/` | Version, platform, core diff summary |
| `sites/<slug>/extension-analysis/` | Extension inventory |
| `sites/<slug>/theme-analysis/` | Theme delta |
| `sites/<slug>/controller-analysis/` | Controller/model custom logic |
| `sites/<slug>/database-analysis/` | Schema delta |
| `sites/<slug>/safe-unknown/` | Blocked classifications |
| `sites/<slug>/reports/` | `# REPORT — …` audit artifact |

Template: [templates/inspection-report-template.md](templates/inspection-report-template.md).

---

## When comparison must stop

- Baseline fails [baseline-readiness-checklist.md](baseline-readiness-checklist.md) → request operator upload; **do not silently continue**.
- Platform or version **SAFE UNKNOWN** → no layer claims beyond evidence.
- Wrong baseline selected → stop and re-select.

---

## Related documents

| Doc | Role |
|-----|------|
| [baseline-storage-model.md](baseline-storage-model.md) | What baselines contain |
| [baseline-readiness-checklist.md](baseline-readiness-checklist.md) | Pre-comparison gate |
| [project-sites-workflow.md](project-sites-workflow.md) | Baseline selection workflow |
| [clean-opencart-baseline.md](clean-opencart-baseline.md) | Baseline rationale |

---

## SAFE UNKNOWN

- Specific diff tooling (rsync, git diff, custom scripts) — not defined in Run 2; human-operated comparison assumed until chartered.

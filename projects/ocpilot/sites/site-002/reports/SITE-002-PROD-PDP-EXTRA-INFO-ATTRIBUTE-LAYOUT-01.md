# REPORT — SITE-002 PDP Extra Info Attribute Layout

**Operation:** `SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01`  
**OCPilot run:** 4.218  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`  
**Baseline after:** `SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01`  
**Mode:** controlled Production patch — PDP layout only

---

## 1. Scope

Move attribute **«Дополнительные сведения»** out of the PDP specs table (`spec-table__row`) into a separate prose block immediately after `product-content__specs-toggle-wrap`.

**In scope:** controller display extraction, `producttabs.twig` block, scoped CSS.  
**Out of scope:** DB, admin, product/attribute data, header/footer/Yandex, sitemap/robots/llms, meta generator logic change.

---

## 2. Operator backup confirmation

| Item | Status |
|------|--------|
| Beget full backup before Run 4.217 | **Confirmed by operator** |
| Used as controlled patch gate | **Yes** — recorded in operation manifest |

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume | `X:` — label **AI WS** — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged, not touched** |

---

## 4. Source authority completion

**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01\manifests\`

| Remote path | Exists | Role | Patch |
|-------------|--------|------|-------|
| `/public_html/catalog/controller/product/product.php` | yes | PDP controller | **yes** |
| `/public_html/catalog/view/theme/default/template/product/producttabs.twig` | yes | Specs partial (authority for spec table) | **yes** |
| `/public_html/assets/css/style.css` | yes | Site CSS | **yes** |
| `/public_html/catalog/view/theme/default/template/product/product.twig` | yes | PDP shell | no |
| `/public_html/catalog/view/theme/default/template/product/producthero.twig` | yes | PDP hero | no |
| `/storage/modification/.../product.php` | **no** | Modification overlay | n/a |
| `/storage/modification/.../producttabs.twig` | **no** | Modification overlay | n/a |

**Finding:** Spec table and toggle live in **`producttabs.twig`**, not `product.twig`. No active modification overlays for PDP controller/template.

---

## 5. Live before snapshot

**Example PDP:** держатель гастроёмкостей ПГ-10/3 — HTTP **200**

| Field | Before |
|-------|--------|
| «Дополнительные сведения» in `spec-table__row` | **yes** |
| Separate `product-content__extra-info` block | **no** |
| `product-content__specs-toggle-wrap` | present |
| Value length (example) | **242** chars |

**Samples:** 5 PDP with attribute + 5 without (from Run 4.217 CSV) + branch probes.

**Storage:** `http-before/`

---

## 6. Implementation design

**Approach:** controller extraction (Option A from intake).

1. Meta generator continues using **unfiltered** `$attribute_groups` loaded at lines 272–274 (before display mutation).
2. After `super_atts` / `SUPER_ATTS` hero processing, controller extracts exact-name match `Дополнительные сведения` into `$data['extra_info_attribute']` and removes it from display `$data['attribute_groups']`.
3. `producttabs.twig` renders block after toggle wrap when `extra_info_attribute.text` is non-empty.
4. Scoped CSS in `assets/css/style.css`.

**Storage:** `manifests/implementation-design.{md,json}`

---

## 7. Patch plan and rollback

**Rollback:** re-upload exact `source-before/` copies from:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01\source-before\`

**Storage:** `rollback/remote-before-manifest.json`, `rollback/rollback-plan.md`

---

## 8. Local patch summary

| File | Change |
|------|--------|
| `product.php` | Display-only extraction of `extra_info_attribute` |
| `producttabs.twig` | `product-content__extra-info` block after specs toggle |
| `assets/css/style.css` | Typography/spacing for extra-info block |

**PHP lint:** SAFE UNKNOWN if CLI absent; static inspection clean.

**Storage:** `patch/changed-files.{csv,json}`, `patch/diff-*.diff`

---

## 9. Dry-run gates

| Gate | Result |
|------|--------|
| G1 Source authority | **PASS** |
| G2 Modification overlays absent | **PASS** |
| G3 Rollback captured | **PASS** |
| G4 Scoped files only (3) | **PASS** |
| G5 No DB/admin/data | **PASS** |
| G6 No header/footer | **PASS** |
| G7 No sitemap/robots/llms | **PASS** |
| G8 PHP/static checks | **PASS** |
| G9 Verification plan | **PASS** |
| G10 Beget backup | **PASS** |

---

## 10. Controlled deploy

| Remote file | Upload SHA verified |
|-------------|---------------------|
| `/public_html/catalog/controller/product/product.php` | **yes** |
| `/public_html/catalog/view/theme/default/template/product/producttabs.twig` | **yes** |
| `/public_html/assets/css/style.css` | **yes** |

**Storage:** `verification/upload-manifest.json`

---

## 11. Live verification after

**Example PDP after patch:**

| Check | Result |
|-------|--------|
| HTTP 200 | **yes** |
| «Дополнительные сведения» in spec table | **no** |
| Separate block after toggle | **yes** |
| Value preserved (244 chars) | **yes** |
| Buy box / images | **yes** |
| Title / meta description | **unchanged** |
| Public **БЗПМ** | **0** |

---

## 12. Sample PDP results

| Cohort | Count | Pass |
|--------|-------|------|
| With «Дополнительные сведения» | 5 | **5/5** — removed from table, separate block after toggle |
| Without attribute | 5 | **5/5** — no empty block, specs unchanged |
| Branch probes (stoly/polki PDP + category PLPs) | 4 | **2/2 PDP pass**; 2 category PLPs N/A (not product pages) |

**Overall comparison:** **12/14** automated rows pass; 2 failures are category PLPs (expected N/A).

---

## 13. Sanity checks

| URL | Status | Notes |
|-----|--------|-------|
| `/` | 200 | body_count **1**, Yandex Metrika present |
| `/katalog` | 200 | OK |
| `/katalog/.../stoly` | 200 | Load More present |
| `/llms.txt` | 200 | UTF-8 BOM, **БЗПМ** 0, **ЗПМ** 2 |
| `/robots.txt` | 200 | OK |
| `/sitemap.xml` | 200 | **1377** URLs |

---

## 14. Brand regression check

| Metric | Result |
|--------|--------|
| Public **БЗПМ** introduced | **no** |
| **ЗПМ** on sample PDPs | present as before |
| Domain bzpm.ru | unchanged |

---

## 15. Product meta generator preservation

Meta description/keywords still computed from **original** `$attribute_groups` before display filter. Example PDP meta description **byte-identical** before/after deploy. Generator methods in `product.php` **not reordered or removed**.

---

## 16. Rollback status

**Not required** — verification passed.

---

## 17. Production mutation summary

| Item | Count |
|------|------:|
| Remote uploads | **3** |
| Remote overwrites | **3** |
| Remote deletes | **0** |
| Remote renames | **0** |
| Admin saves | **0** |
| DB direct operations | **0** |
| Product data changes | **0** |
| Attribute data changes | **0** |
| Product PDP layout changes | **yes** |
| Product generator changes | **no** (preserved) |
| Category meta/structure/status/URL changes | **0** |
| Images generated/uploaded | **0** |
| Homepage changes | **0** |
| Catalog changes | **0** |
| PDP template changes | **yes** — `producttabs.twig` |
| CSS changes | **yes** — `assets/css/style.css` |
| llms.txt changes | **0** |
| Header/footer changes | **0** |
| Yandex.Metrika/Webmaster changes | **0** |
| Robots changes | **0** |
| Sitemap changes | **0** |
| Cron/import runs | **0** |
| Mail changes | **0** |
| Cache clears | **0** |
| Manual sitemap edits | **0** |
| public **БЗПМ** introduced | **no** |

---

## 18. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01\`

Checkpoint mirror: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01\`

---

## 19. Authority updates

Repository docs updated: OPERATIONAL-INDEX, OCPILOT-STATE, production-profile, site-passport, technical knowledge map, tools README.

---

## 20. Git status

Selective commit of operation report, baseline, tool, and scoped doc updates only. Storage artefacts **not** committed.

---

## 21. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| PHP CLI on operator host | not verified — static review only |
| Lari/konditerskiy **product** PDP in sample | no product URL in intake sample — category PLP probes only |
| Home Yandex Webmaster string in automated probe | `yandex_webmaster: false` in probe (Metrika true); header/footer untouched — **not a regression signal from this patch** |

---

## 22. Final verdict

**SITE-002 PDP EXTRA INFO ATTRIBUTE LAYOUT COMPLETE — EXTRA INFO BLOCK VERIFIED**

---

## 23. Next task recommendation

**SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01** — add Лари + Кондитерский инвентарь tiles to homepage/neutral hub per Run 4.217 charter (`category_visibility.php` + admin category images).

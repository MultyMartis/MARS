# REPORT — SITE-002 Stable Checkpoint After M9

**Program:** BZPM Product Roadmap  
**Milestone:** Stable Baseline  
**Site:** SITE-002 (ЗПМ)  
**Environment:** TEST only — https://zpm.new-site.space/  
**Checkpoint:** `SITE-002-STABLE-M9-COMPLETE-20260615`  
**Execution UTC:** 2026-06-14 / 2026-06-15  
**Mode:** Read-only checkpoint — **no** implementation · **no** deploy · **no** production · **no** commit · **no** push

---

## QA Snapshot

**Summary:** 18 pass · 0 fail · 0 warn  
**Evidence:** `backups/stable-baselines/SITE-002-STABLE-M9-COMPLETE-20260615/qa-snapshot.json`

### Pre-flight

| Check | Result |
|-------|--------|
| TEST accessible | **PASS** — all required URLs HTTP 200 |
| PHP warnings/notices | **PASS** — no error markers on any page |
| M9 profiles active | **PASS** — 301/80/322/207/326 branch filters verified |
| Root Hub active | **PASS** — `category--hub`, 5 branch cards, no PLP chrome |
| M8 cleanup active | **PASS** — no TEST/packaging/service attrs in filters; DB unchanged since Wave 1 |

### Required URLs

| URL | Result |
|-----|--------|
| `/` | **PASS** — HTTP 200 |
| `/katalog` | **PASS** — HTTP 200 |
| `/katalog/nejtralnoe-oborudovanie` | **PASS** — hub mode, 5 cards |
| `/katalog/nejtralnoe-oborudovanie/stoly/` | **PASS** — table profile 10/10 primary |
| `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | **PASS** — sink profile 8/8 primary |
| `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | **PASS** — branch PLP grid + filter |
| `/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/` | **PASS** — branch PLP grid + filter |
| Reference table PDP (SPKB-18/7-ВЛ5) | **PASS** — HTTP 200 |
| Reference sink PDP (VMC-P3-2-500) | **PASS** — HTTP 200 |

### Additional checks

| Check | Result |
|-------|--------|
| Megamenu single neutral root | **PASS** |
| Footer catalog links | **PASS** — neutral hub only |
| Filter — Столы (no cross-family/global hidden) | **PASS** |
| Filter — Моечные ванны | **PASS** |
| Hub — no filter sidebar / product grid / pagination | **PASS** |
| Profile conflicts | **PASS** — none detected |
| Broken links (required set) | **PASS** |

---

## Stable State Summary

| Item | Value |
|------|-------|
| Checkpoint name | `SITE-002-STABLE-M9-COMPLETE-20260615` |
| Baseline folder | `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9-COMPLETE-20260615/` |
| Manifest | `…/manifest.json` |
| Supersedes | `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` |
| M7.1 Launch Mode | Deployed on TEST |
| M8.3 Wave 1 TEST Cleanup | Active — DB cleanup; product 3071 hidden; TEST attrs removed |
| M8.3 Wave 2 Packaging & Service | Active — `attribute_filter_visibility.php` layer |
| M9 Phase 1 (301 Столы) | Deployed on TEST |
| M9 Phase 2 (80 Моечные ванны) | Deployed on TEST |
| M9 Phase 3 (322/207/326) | Deployed on TEST |
| M9.5 Root Hub (cat 79) | Deployed on TEST |
| M10 | **Not authorized** — out of scope |

---

## Files Backed Up

21 live files captured via FTP (read-only). Hashes in `manifest.json`.

| Remote path | Milestones | Bytes | SHA256 |
|-------------|------------|------:|--------|
| `system/library/zpm/category_visibility.php` | M7.1, M9.5 | 3965 | `029b22a35513cb79d728a7e78b07f9a4741b2dde4650562cf0297da5b508623f` |
| `catalog/controller/product/katalog.php` | M7.1 | 5700 | `f91b9a894c55fa50d689de39df6ef44ec5d4e4180f66ae462069695c2ae9cc0e` |
| `catalog/controller/product/category.php` | M7.1, M9, M9.5 | 22103 | `4ed6db8db424cf7c2123ab6ea6c74e8dad8c9d10b3e922e2014cf207c611538e` |
| `catalog/controller/common/header.php` | M7.1 | 7592 | `804548a608a1579eeacc92ded17bcf27b8966ec244fff53f4446ba1ab08e4bc2` |
| `catalog/controller/common/footer.php` | M7.1 | 3339 | `1d4b15cb9fd96a7cc792d6c3b3a43c15b01924535a6517d2af8a7a42cd19a7c5` |
| `catalog/controller/common/home.php` | M7.1 | 3709 | `8bdf16d6ee30078d541518bfc23fd39683f2676cf6cc44a1413440fa47d16a00` |
| `catalog/view/theme/default/template/common/megamenu.twig` | M7.1 | 4190 | `78b9cfc5c3647a09aae87c6f632eafbe77cc0c45861c0b4a608199548d354978` |
| `catalog/view/theme/default/template/common/footer.twig` | M7.1 | 9710 | `9be5bcf2fa8cea09b940305f9fba1367c35608fe26683e921efae83c174b1b47` |
| `catalog/view/theme/default/template/sections/catalogsections.twig` | M7.1 | 984 | `cf9bd96f334bc6d93f10f626e22e525b2ddf1d09bfdcb2fee880367c4d75ba81` |
| `catalog/view/theme/default/template/sections/offcanvasmenu.twig` | M7.1 | 5157 | `1dc6b22372cdecd0aa5fb0124ae0fa1e5714edd1f82cfcd25e5e6fc0ae11606f` |
| `system/library/zpm/attribute_filter_visibility.php` | M8.3-W2 | 1724 | `99bb35e0bb1ca3888a97f84d0afe46d9357372aa3c54bd0098b578b848af3e00` |
| `catalog/model/catalog/product.php` | M8.3-W2, M9 | 58556 | `4dea62375e261bfb2fea986511405f34b28b5c3d4a98c1bbda8520bc31094659` |
| `system/library/zpm/filter_profile_resolver.php` | M9 | 6207 | `a987d4fbf6fc24429f7196a297b227d390a6a5e2e315c3f616fb94ee0b47087e` |
| `system/library/zpm/filter_profiles/global_hidden.php` | M9 | 569 | `63d146bc82a556e52b3adc4a003b003791ddf5ee0134117ff41f3adec3039ea4` |
| `system/library/zpm/filter_profiles/301_stoly.php` | M9-Phase1 | 1316 | `27b89d4203887c8e59c20aef1e333fcb2d484e181bd2edd1b5e1d0e1dbe16538` |
| `system/library/zpm/filter_profiles/80_moechnye_vanny.php` | M9-Phase2 | 1441 | `7650df0ba4dc251bfcff09aae669a4c213c06fb022d41165e6c668208854094b` |
| `system/library/zpm/filter_profiles/322_podtovarniki.php` | M9-Phase3 | 1703 | `87e3c4eddba97b02727209cc0348f54a04ce7e5c1d62d1aa511b46f9acea1de9` |
| `system/library/zpm/filter_profiles/207_zonty.php` | M9-Phase3 | 1163 | `8a33cc1c9bd8d0005fbfe4c05895cc7ca9153077aeb3c341fc7bacdb31ae80fb` |
| `system/library/zpm/filter_profiles/326_telezhki.php` | M9-Phase3 | 764 | `f98cbf903995908d5b8f9ab45bd2ab2eb981d3f32cdbef88bae0ebeca107950b` |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | M9 | 18478 | `bcf9d1e9d0fc5f74af7698a9c7275df2c8c1fa504783be48fbd291f944cff049` |
| `catalog/view/theme/default/template/product/category.twig` | M9.5 | 5769 | `291daa368db27daca9185c47a9164cb07139a1be727cd0d47e7cb0190c65c94e` |

Local copies under: `…/files/` (mirrors remote tree)

**Deploy manifest references:** `m7.1-launch-mode-work/`, `m8.3-wave1-cleanup-work/`, `m8.3-wave2-cleanup-work/`, `m9-phase1-tables-work/`, `m9-phase2-sinks-work/`, `m9-phase3-remaining-work/`, `m9.5-root-hub-work/`

---

## Data Snapshot

**Evidence:** `…/data-snapshot.json` · scoped JSON under `…/database/`

| Metric | Value |
|--------|------:|
| Active SKU count (`status=1`) | **608** |
| Inactive SKU count | **2526** |
| Total SKU count | **3134** |
| Total categories (`oc_category`) | **190** |
| Active attribute definitions (post M8.3 Wave 1) | **46** |
| Total attribute rows in DB | **53** |

### Profile categories (M9 + M9.5)

| ID | Name | Mode | Profile file |
|----|------|------|--------------|
| 79 | Нейтральное оборудование | **hub** | — (M9.5) |
| 301 | Столы | branch | `301_stoly.php` |
| 80 | Моечные ванны | branch | `80_moechnye_vanny.php` |
| 322 | Подтоварники и подставки | branch | `322_podtovarniki.php` |
| 207 | Зонты вытяжные | branch | `207_zonty.php` |
| 326 | Тележки сервировочные | branch | `326_telezhki.php` |

### Hidden attribute policy

| Layer | Policy |
|-------|--------|
| M8.3 Wave 1 | TEST attribute defs removed from DB; product 3071 hidden (`status=0`) |
| M8.3 Wave 2 | Packaging + SERVICE hidden via `attribute_filter_visibility.php` (STORE_ONLY) |
| M9 global | `global_hidden.php` — 32 attribute IDs (TEST/SERVICE/Packaging/TECHNICAL/dead) |

**DB state note:** M9 and M9.5 were **code-only**. Scoped JSON exports match prior baseline `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` (hash-verified carry-forward).

### DB backup artifacts

| Table | Rows | SHA256 (prefix) |
|-------|-----:|-----------------|
| `oc_product` | 3134 | `3bd2525a…` |
| `oc_product_attribute` | 10169 | `ce7acf8b…` |
| `oc_attribute` | 53 | `355dcb8e…` |
| `oc_attribute_description` | 53 | `b83422ef…` |
| `oc_category` | 190 | `81eeaeed…` |
| `oc_category_description` | 190 | `4db61ba8…` |

**Full mysqldump:** Not obtained — phpMyAdmin `export.php` HTTP 500 (same as prior checkpoint).

---

## Updated State Documents

| File | Change |
|------|--------|
| `projects/ocpilot/sites/site-002/site-passport.md` | Active baseline → M9 complete |
| `projects/ocpilot/sites/site-002/README.md` | Active checkpoint + M10 not authorized |
| `projects/ocpilot/OCPILOT-STATE.md` | SITE-002 current state updated |

---

## Rollback Source

### Primary (this checkpoint)

`projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9-COMPLETE-20260615/`

1. Verify SHA256 of files in `files/` against `manifest.json`.
2. Upload each file to matching path on FTP (`polygonws.beget.tech`, site root).
3. Clear Twig cache: `system/storage/cache/template/*`
4. Clear attribute cache: `system/storage/cache/cache.category.attributes.*`
5. Re-run QA URLs from `qa-snapshot.json`.

### Pre-M9 rollback (historical)

`SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` — use if rolling back M9/M9.5 code only while keeping M8.3 data state.

### Database

- Scoped JSON in `database/*.json` — TEST only; operator-controlled import.
- Full DB beyond scoped tables — Beget panel backup (not in repo).

---

## M10 Readiness

| Item | Status |
|------|--------|
| Stable baseline registered | **YES** — this checkpoint |
| M9 filter profiles on TEST | **YES** — 5 branch profiles + global hidden |
| Root Hub on TEST | **YES** — category 79 hub mode |
| M8 cleanup verified | **YES** |
| QA snapshot PASS | **YES** — 18/18 |
| M10 authorized | **NO** — requires operator charter |
| Production deploy | **NO** |

**Readiness verdict:** TEST is in a **stable post-M9 state** suitable as rollback anchor for future M10 work. M10 itself is **not started** and **not authorized** by this task.

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Full mysqldump unavailable (HTTP 500) | Medium | Use scoped JSON + Beget panel backup for full DB |
| DB JSON carry-forward from M8.3 baseline | Low | M9/M9.5 were code-only; COUNT queries confirm unchanged totals |
| phpMyAdmin paginated export incomplete on first pass | Low | Corrected via verified carry-forward from prior baseline |
| DB JSON contains catalog row data | Medium | Treat as sensitive; review before optional commit |
| FTP credentials in operator scripts (not in manifest) | Low | External storage only |
| Operator visual HITL not re-run in this checkpoint | Low | Automated QA PASS; prior M9/M9.5 reports hold implementation evidence |

---

## Git Status

Checkpoint artifacts are **untracked/modified** until operator chooses commit.  
**No commit performed** (per task).  
**No push performed.**

Suggested paths for optional future commit:

- `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9-COMPLETE-20260615/`
- `projects/ocpilot/sites/site-002/backups/stable-baselines/create-stable-m9-complete.py`
- `projects/ocpilot/sites/site-002/reports/SITE-002-STABLE-M9-COMPLETE.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/README.md`
- `projects/ocpilot/OCPILOT-STATE.md`

---

## UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Full mysqldump via phpMyAdmin unavailable (HTTP 500) |
| **UNKNOWN** | M10 scope and authorization timeline |
| **SECURITY** | DB JSON dumps contain product/catalog data — treat as sensitive |
| **SECURITY** | FTP/DB credentials used from existing operator scripts — not stored in manifest |

**Site/DB modified during task:** **NO** (read-only)  
**Implementation performed:** **NO**  
**Deploy performed:** **NO**

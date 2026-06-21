# REPORT — SITE-002 Stable Backup Before M9

**Program:** BZPM / SITE-002 (ЗПМ)  
**Environment:** https://zpm.new-site.space/ (TEST only)  
**Checkpoint:** `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`  
**Execution UTC:** 2026-06-14 / 2026-06-15 (local folder stamp 20260615-0159)  
**Mode:** Read-only backup — **no** code changes · **no** DB writes · **no** production deploy · **no** M9 implementation

---

## Stable State

| Item | Value |
|------|-------|
| M7.1 Launch Mode | Deployed on TEST |
| M8.3 Wave 1 TEST Cleanup | Deployed on TEST (DB cleanup; product 3071 inactive) |
| M8.3 Wave 2 Packaging & Service Cleanup | Deployed on TEST (filter visibility code layer) |
| M9 Filter Profile System | Architecture referenced in roadmap — **implementation not started** |
| Baseline folder | `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/` |
| Manifest | `…/manifest.json` |

---

## QA Before Backup

**Summary:** 13 pass · 0 fail · 0 warn

| Check | Result |
|-------|--------|
| PHP warnings/notices on home | **PASS** — no error markers |
| `/` | **PASS** — HTTP 200 |
| `/katalog` | **PASS** — HTTP 200 |
| `/katalog/nejtralnoe-oborudovanie` | **PASS** — HTTP 200 |
| `/katalog/nejtralnoe-oborudovanie/stoly/` | **PASS** — HTTP 200 |
| `/katalog/nejtralnoe-oborudovanie/vanny-moechnye/` | **NOTE** — task URL returns **404** (stale slug) |
| `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | **PASS** — canonical slug HTTP 200; filter clean |
| Reference PDP (SPKB-18/7-ВЛ5) | **PASS** — HTTP 200 |
| Megamenu single neutral root | **PASS** — «Нейтральное оборудование» only |
| Footer catalog links | **PASS** — neutral hub + service links only |
| Filter — no TEST attrs (Столы PLP) | **PASS** |
| Filter — no packaging/service attrs | **PASS** (Столы + Моечные ванны) |

Full QA JSON: `…/qa-before-backup.json`

---

## Files Backed Up

12 live files captured via FTP (read-only). **M8.3 Wave 1** did not change PHP files on server (DB-only cleanup).

| Remote path | Milestone | Size | SHA256 |
|-------------|-----------|-----:|--------|
| `system/library/zpm/category_visibility.php` | M7.1 | 3504 | `746e9feac85a9f63340e4188178ffe1da0588bcd3da4bc48a4b7155a8c2a3187` |
| `catalog/controller/product/katalog.php` | M7.1 | 5700 | `f91b9a894c55fa50d689de39df6ef44ec5d4e4180f66ae462069695c2ae9cc0e` |
| `catalog/controller/product/category.php` | M7.1 | 19469 | `71ae2e3676cbcc4a53d982e8a2922601530a760ccf809b9980055d820e1ecef6` |
| `catalog/controller/common/header.php` | M7.1 | 7592 | `804548a608a1579eeacc92ded17bcf27b8966ec244fff53f4446ba1ab08e4bc2` |
| `catalog/controller/common/footer.php` | M7.1 | 3339 | `1d4b15cb9fd96a7cc792d6c3b3a43c15b01924535a6517d2af8a7a42cd19a7c5` |
| `catalog/controller/common/home.php` | M7.1 | 3709 | `8bdf16d6ee30078d541518bfc23fd39683f2676cf6cc44a1413440fa47d16a00` |
| `catalog/view/theme/default/template/common/megamenu.twig` | M7.1 | 4190 | `78b9cfc5c3647a09aae87c6f632eafbe77cc0c45861c0b4a608199548d354978` |
| `catalog/view/theme/default/template/common/footer.twig` | M7.1 | 9710 | `9be5bcf2fa8cea09b940305f9fba1367c35608fe26683e921efae83c174b1b47` |
| `catalog/view/theme/default/template/sections/catalogsections.twig` | M7.1 | 984 | `cf9bd96f334bc6d93f10f626e22e525b2ddf1d09bfdcb2fee880367c4d75ba81` |
| `catalog/view/theme/default/template/sections/offcanvasmenu.twig` | M7.1 | 5157 | `1dc6b22372cdecd0aa5fb0124ae0fa1e5714edd1f82cfcd25e5e6fc0ae11606f` |
| `system/library/zpm/attribute_filter_visibility.php` | M8.3-W2 | 1724 | `99bb35e0bb1ca3888a97f84d0afe46d9357372aa3c54bd0098b578b848af3e00` |
| `catalog/model/catalog/product.php` | M8.3-W2 | 58071 | `afb59aa8c09e5780d391d2e22e2f09ec3c46d9c8434a05e4963e78efc8a51c0b` |

Local copies under: `…/files/` (mirrors remote tree)

---

## DB Backup

**Full mysqldump:** **Not obtained** — phpMyAdmin `export.php` returned HTTP 500 on TEST hosting.

**Scoped tables (JSON via sql.php):** **Complete** — all rows exported

| Table | Rows exported | File size | SHA256 |
|-------|--------------:|----------:|--------|
| `oc_product` | 3134 / 3134 | 2 402 644 | `3bd2525a863496a3b6cfd5b958f519239b99ccd584c8903105c25978c77d4727` |
| `oc_product_attribute` | 10169 / 10169 | 1 052 252 | `ce7acf8bcf03ff8fa4ecc508afdfa417d24141422f5881085182e0ac22c829ff` |
| `oc_attribute` | 53 / 53 | 3 958 | `355dcb8e09abb2e5f2eb618e1a28b7dacaaaaafcbb86a6c29632343322c13108` |
| `oc_attribute_description` | 53 / 53 | 6 257 | `b83422ef4e36bc9472a8009c8f46c275bf39c8c8fd65d4583c05b7c5729c6958` |
| `oc_category` | 190 / 190 | 41 916 | `81eeaeed6514e4dc7092e36be3520a5f38f2683897f36353794980c2e9d760a8` |
| `oc_category_description` | 190 / 190 | 54 889 | `4db61ba8941246a7d16029fe1d654ea358688e0bb08052b7399dc09d6b2e5d50` |

Each JSON file includes `create_table` snippet + full `rows` array.  
**Operator recommendation:** use Beget hosting panel for full DB backup if full mysqldump is required.

---

## Manifest

| Field | Value |
|-------|-------|
| Path | `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/manifest.json` |
| Timestamp (UTC) | 2026-06-14T19:00:18Z (capture start) |
| TEST URL | https://zpm.new-site.space |
| Files | 12 |
| DB artifacts | 6 scoped JSON tables |
| QA summary | 13 pass / 0 fail |

---

## Updated State Docs

| File | Change |
|------|--------|
| `projects/ocpilot/sites/site-002/site-passport.md` | Active baseline → M8.3 before M9 |
| `projects/ocpilot/sites/site-002/README.md` | Active checkpoint + next planned M9 |
| `projects/ocpilot/OCPILOT-STATE.md` | SITE-002 current state updated |

---

## Rollback Instruction

### Files (M7.1 + M8.3 Wave 2 code)

1. Verify SHA256 of files in `files/` against manifest.
2. Upload each file to matching path on FTP (`polygonws.beget.tech`, site root = `public_html`).
3. Clear Twig cache: `system/storage/cache/template/*`
4. Clear attribute cache files: `system/storage/cache/cache.category.attributes.*`

### Database (M8.3 Wave 1 data state)

1. Restore row data from `database/*.json` files via operator script or controlled import on **TEST only**.
2. For full DB rollback beyond scoped tables — use **Beget panel backup** (not in this repo).

### Verify after rollback

- Home, `/katalog`, neutral hub — HTTP 200
- Megamenu — single «Нейтральное оборудование»
- Footer — neutral catalog link only
- PLP filters — no TEST / packaging / service attrs
- Reference PDP opens

---

## Git Status

Checkpoint artifacts are **untracked** until operator chooses commit.  
**No commit performed** (default policy).  
If committing: use **precise paths only** under `projects/ocpilot/sites/site-002/` — do not add unrelated dirty MARS files.

Suggested paths for optional commit:

- `projects/ocpilot/sites/site-002/backups/stable-baselines/`
- `projects/ocpilot/sites/site-002/reports/SITE-002-STABLE-M8.3-BEFORE-M9.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/README.md`
- `projects/ocpilot/OCPILOT-STATE.md`

**Note:** DB JSON files contain catalog row data — review size/sensitivity before commit.

---

## Next Step

**M9 Filter Profile System implementation** — blocked until operator charter for implementation pass.  
Use this checkpoint as rollback source; live-capture any additional files before M9 deploy.

---

## UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Full mysqldump via phpMyAdmin unavailable (HTTP 500) |
| **UNKNOWN** | M9 architecture doc path in repo (referenced in task; not verified in this run) |
| **SECURITY** | DB JSON dumps contain product/catalog data — treat as sensitive; FTP credentials used from existing operator scripts (not stored in manifest) |
| **NOTE** | Task URL `/vanny-moechnye/` is stale; live slug is `/moechnye-vanny/` |

**Production deploy:** NO  
**M9 implementation:** NO  
**Site/DB modified during task:** NO (read-only)

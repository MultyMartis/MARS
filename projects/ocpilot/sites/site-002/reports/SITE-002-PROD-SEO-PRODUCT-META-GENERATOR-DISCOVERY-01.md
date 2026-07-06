# REPORT — SITE-002 Product Meta Generator Discovery

**Operation:** `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01`  
**OCPilot run:** 4.200  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline:** `SITE-002-STABLE-PROD-SEO-INFORMATION-META-01`  
**Mode:** read-only discovery — **no Production mutation**

---

## 1. Scope

Read-only discovery of how product PDP `meta description`, `meta keywords`, and `title` are produced on Production. Covers:

- 24 representative PDP HTTP samples (neutral-equipment families prioritized)
- FTP read-only source/runtime file capture
- Admin read-only product SEO field comparison (6 products)
- Category attribute profile for future generator design
- Implementation plan for `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01`
- Deferred `llms.txt` next-task plan (`SITE-002-PROD-LLMS-TXT-01`)

**Excluded:** product saves, DB writes, controller deploy, cache clear, header/footer/Yandex, robots/sitemap, llms.txt creation.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` — label **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `2a3b1768` |
| Staged files before task | **none** |
| Foreign WIP | FP-0002 / unrelated paths — **not staged** |

---

## 3. PDP sample inventory

**Source:** `sitemap.xml` (1296 deep PDP URLs) + `stoly` PLP supplement.

**Sample size:** 24 URLs across families: stoly (3), polki (5), telezhki (3), shkafy_lari (2), podstavki (3), stellazhi (3), moechnye_vanny (3), legacy shkafy/polki hub paths (2).

**Storage:**

- `pdp-samples/pdp-url-samples.csv`
- `pdp-samples/pdp-url-samples.json`

---

## 4. Live product meta snapshot

| Metric | Value |
|--------|-------|
| HTTP 200 | 24/24 |
| Missing `meta description` | **8/24** (33%) |
| Missing `meta keywords` | **24/24** (100%) |
| Description length 50–170 | **12/24** |
| «купить» in description/keywords | **0/24** |
| Import-like descriptions (no commercial intent) | **13/24** |
| `index, follow` | all sampled PDPs |
| Yandex.Metrika / Webmaster | present on sampled pages |
| `body` count | 1 (Run 4.190 fix holds) |

**Patterns observed:**

1. **Description present** — typically **160 characters**, truncated mid-sentence — matches `mb_substr(strip_tags(description), 0, 160)` from 1C import.
2. **Description missing** — products with empty 1C `Описание` (e.g. polki holders, shkafy, stellazhi samples) → empty `meta_description` in DB → empty live tag.
3. **Keywords** — always empty on sampled PDPs.
4. **Title** — from `meta_title` (= product name on import); suffix `| ООО «ЗПМ»` added by theme/header; one sample has operator artifact `!!!!!НЕ БРАТЬ!!!!` in title/H1.
5. **No runtime SEO extension** on PDP — standard `document->setDescription($product_info['meta_description'])`.

**Storage:**

- `meta-samples/product-meta-snapshot.csv`
- `meta-samples/product-meta-snapshot.json`
- `meta-samples/product-meta-summary.md`
- `html/*.html` (24 captures)

---

## 5. Source discovery

### Runtime authority (PDP)

| Layer | Path | Role |
|-------|------|------|
| **Source controller** | `/public_html/catalog/controller/product/product.php` | `setTitle/setDescription/setKeywords` from `$product_info` DB fields — **no runtime generator** |
| **Import generator** | `/public_html/catalog/controller/common/import_1C_process.php` | On insert/update: `meta_description = mb_substr(strip_tags(description), 0, 160)`; `meta_title = name`; **no `meta_keyword`** |
| **Model** | `/public_html/catalog/model/catalog/product.php` | Reads meta fields; `getProductAttributes()` available |
| **Modification overlay** | `/storage/modification/catalog/controller/product/product.php` | **Not present** (FTP 550) — source file is runtime authority |
| **SEO extension** | extension dirs probed | No product-meta-specific extension found |

**Key code paths (Production FTP, read-only):**

```php
// product.php — runtime pass-through
$this->document->setTitle($product_info['meta_title']);
$this->document->setDescription($product_info['meta_description']);
$this->document->setKeywords($product_info['meta_keyword']);

// import_1C_process.php — import-time generator (Sergey legacy)
meta_description = mb_substr(strip_tags($description), 0, 160)
meta_title = name
// meta_keyword not set
```

`getProductAttributes()` is called **after** meta is set in `product.php` (~line 479) — a runtime generator should load attributes before `setDescription` or use `$product_info` dimensions (`length`, `width`, `height`, `weight`).

**Storage:**

- `source/` — 8 FTP files (product controller/model, import_1C*, category, document, product.twig)
- `generator-analysis/source-discovery.json`
- `generator-analysis/source-discovery.md`

---

## 6. Admin read-only comparison

**Status:** COMPLETED READ-ONLY (Playwright, 6 products, no saves).

| Finding | Detail |
|---------|--------|
| Admin SEO textarea values | Automated read returned **empty** for all 6 samples |
| Live meta on same URLs | **160 chars** description where 1C description exists; **0** where import had no description |
| Live equals admin | **False** for all 6 (automation did not read populated DB values — likely SEO tab / `language_id` selector mismatch) |
| Admin keywords | Empty in form read |

**Interpretation:** Live meta correlates with import-time DB population, not a hidden runtime generator. Admin form automation limitation — manual operator verification of SEO tab recommended before FIX run. DB-sourced path confirmed by import source + live HTML correlation.

**Storage:** `admin-evidence/product-seo-fields-readonly.md` · `.json`

---

## 7. Attribute profile discovery

Families sampled with priority attribute hints for future generator:

| Family | Samples | High-value attributes for meta |
|--------|---------|--------------------------------|
| stoly | 3 | dimensions, shelf, board, stainless |
| polki | 5 | mount type, levels, dimensions |
| telezhki | 3 | wheels, levels, GN/trays, dimensions |
| shkafy_lari | 2 | doors, shelves, dimensions |
| podstavki | 3 | dimensions, load, GN levels |
| stellazhi | 3 | levels, dimensions |
| moechnye_vanny | 3 | dimensions, sink type |

Visible attribute HTML parsing returned **SAFE UNKNOWN** in automated pass — specs exist in product body/description text; `getProductAttributes()` + `length/width/height` in `$product_info` are available in controller.

**Storage:** `attribute-map/category-attribute-profile.md` · `.json`

---

## 8. Current generator decision

| Question | Answer |
|----------|--------|
| **Generator exists?** | **Yes — import-time only** (`import_1C_process.php`), not PDP controller |
| **Runtime PDP generator?** | **No** — DB field pass-through |
| **Includes «купить»?** | **No** |
| **Includes attributes?** | **No** (truncated plain description only) |
| **Includes category context?** | **No** |
| **Respects manual meta?** | **No on re-import** — import overwrites `product_description` row |
| **Keywords generated?** | **No** — always empty in samples |
| **Good enough?** | **No** — missing keywords, 33% missing descriptions, no commercial intent, truncated stubs |
| **Implementation path** | Controller fallback in `product.php` when meta empty/short/generic; preserve meaningful manual meta; optional import improvement later (separate charter) |
| **Model change required?** | **No** for v1 — use `$product_info` + `getProductAttributes()` with reorder |
| **Single-controller safe?** | **Yes** — with FTP backup; no modification file currently |
| **Rollback** | Restore `product.php` from Storage backup |

**Storage:** `generator-analysis/current-generator-decision.md` · `.json`

---

## 9. Proposed product meta generator design

**Policy (runtime, FIX task):**

- Keep manual `meta_description` if length ≥ 80 and not generic import stub
- Generate when empty, &lt; 50 chars, or import-truncation pattern without commercial intent
- Generate `meta_keyword` when empty
- Template concept: `Купить {name} БЗПМ из нержавеющей стали для общепита. {1–3 specs}. Производство и поставка по России.` (≤ 165 chars)
- Category-specific attribute priority per family (tables, shelves, carts, cabinets, stands)
- Keywords: name, category, купить, БЗПМ, нержавеющая сталь, нейтральное оборудование, selected attributes — no stuffing
- No price/stock/superlative claims unless data proves

**Storage:** `generator-analysis/proposed-product-meta-generator-design.md` · `.json`

---

## 10. Next implementation plan

**Operation:** `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01`

- Patch `/public_html/catalog/controller/product/product.php` (primary)
- Reorder: load attributes / dimensions before meta set
- Backup + verify 24+ PDP samples
- No DB writes in v1
- Import script change optional separate charter (would affect re-import overwrite behavior)

**Storage:** `manifests/product-meta-generator-fix-plan.md`

---

## 11. llms.txt next task plan

**Operation:** `SITE-002-PROD-LLMS-TXT-01` — create `/public_html/llms.txt` at https://bzpm.ru/llms.txt; informational for AI agents; does not replace robots/sitemap; no secrets. **Not executed in this run.**

**Storage:** `manifests/llms-txt-next-task.md`

---

## 12. Remote mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves | 0 |
| DB writes | 0 |
| Cache clears | 0 |
| Product/PDP changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| llms.txt changes | 0 |
| Cron/import changes | 0 |
| Mail changes | 0 |

---

## 13. Storage artefacts

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01\
```

Subfolders: `source\`, `runtime-source\`, `html\`, `pdp-samples\`, `admin-evidence\`, `meta-samples\`, `attribute-map\`, `generator-analysis\`, `manifests\`, `reports\`, `logs\`

---

## 14. Authority updates

- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) — Run 4.200
- [OCPILOT-STATE.md](../../OCPILOT-STATE.md)
- [production-profile.md](../production-profile.md)
- [site-passport.md](../site-passport.md)
- [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
- Tool: [site-002-prod-seo-product-meta-generator-discovery-01.py](../tools/site-002-prod-seo-product-meta-generator-discovery-01.py)

**No new Production checkpoint** (read-only discovery).

---

## 15. Git status

Selective commit of repo docs/report/tool only. Storage artefacts not in git.

---

## 16. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Admin SEO field automation vs DB | Form read empty while live meta present — **manual SEO tab verification** recommended before FIX |
| Visible attribute DOM selectors | Automated HTML parse did not extract spec table — use controller data in FIX |
| `zonty-vytyazhnye` / `telezhki-servirovochnye` PDP samples | Limited in 24-sample set — extend verification in FIX |
| Import script change for persistent DB meta | Out of scope — separate charter if operator wants import-time + runtime dual strategy |

---

## 17. Final verdict

**SITE-002 PRODUCT META GENERATOR DISCOVERY COMPLETE — IMPLEMENTATION PLAN READY**

---

## 18. Next task recommendation

1. **`SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01`** — deploy runtime controller fallback meta generator in `product.php`; verify 24+ PDPs; preserve manual meta; populate keywords.
2. **`SITE-002-PROD-LLMS-TXT-01`** — create `/public_html/llms.txt` per manifest (operator-approved).

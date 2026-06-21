# Makita Product Surface Inventory v1

**Status:** **verified — operator-named scope**  
**Layer:** MIG Product Surface (groundtruth only)  
**Date:** 2026-06-07  
**Pilot:** Makita Snab  
**Primary website:** https://makita-snab.ru  
**ATLAS context:** `atlas_client_org_ref = ORG-0007`  
**Region (session context):** Moscow + Moscow Oblast  
**Sales model:** Retail  

**Boundaries:** No Wordstat · No keyword registry · No ORCA · No PPC · No campaign architecture · No demand inference.

---

## Input Source

| Input | Source | Observed |
|-------|--------|----------|
| Approved SKU list | Operator correction task (conversation context) — named anchors | **8 SKUs** explicitly enumerated |
| List bookends | Starts CL114FDWI…DCL284FRF; ends DPP200ZK…SD100DZ | Middle SKUs indicated by `…` not separately enumerated in agent-accessible persistence |

**Scope for this pass:** all **8 operator-named SKUs** from the correction instruction. No SKU skipped within that scope.

---

## Capture Method

| Step | Method |
|------|--------|
| 1 | Resolve product URL via `sitemap.xml` (`/magazin/product/{slug}` containing SKU) |
| 2 | `GET` product page — HTTP 200 required |
| 3 | `product_title` ← `<h1>` |
| 4 | `product_url` ← `<link rel="canonical">` when present; else sitemap product URL |
| 5 | `category` ← breadcrumb trail when present on page |
| 6 | `page_found = true` only when dedicated product page loads with SKU match in `<h1>` / page body |

**Note:** `GET https://makita-snab.ru/?search={SKU}` returns catalog homepage (no SKU filter) at capture time — **not used** as primary resolution path.

**Capture timestamp:** 2026-06-07

---

## Coverage Summary

| Metric | Value |
|--------|-------|
| Approved SKUs in scope | **8** |
| SKUs verified on site | **8** |
| `page_found = true` | **8** |
| `page_found = false` | **0** |
| Coverage rate | **100%** (within named scope) |

---

## Product Inventory

| sku | product_title | product_url | category | page_found | safe_unknown |
|-----|---------------|-------------|----------|------------|--------------|
| CL114FDWI | Аккумуляторный пылесос Makita CL114FDWI | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl114fdwi | — | true | category breadcrumb not observable; canonical link tag absent |
| CL106FDWY | Аккумуляторный пылесос Makita CL106FDWY | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-cl106fdwy | — | true | category breadcrumb not observable; canonical link tag absent |
| CL121DWA | Аккумуляторный пылесос Makita CL121DWA | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-cl121dwa | — | true | category breadcrumb not observable; canonical link tag absent |
| DCL284FRF | Аккумуляторный пылесос Makita DCL284FRF | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl284frf | — | true | category breadcrumb not observable; canonical link tag absent |
| DPP200ZK | Аккумуляторный дырокол с гидравлическим приводом Makita DPP200ZK | https://makita-snab.ru/magazin/product/akkumulyatornyj-dyrokol-s-gidravlicheskim-privodom-makita-dpp200zk | — | true | category breadcrumb not observable; canonical link tag absent |
| DSC121ZK | Шпилькорез Makita DSC121ZK | https://makita-snab.ru/magazin/product/shpilkorez-makita-dsc121zk | — | true | category breadcrumb not observable; canonical link tag absent |
| PV7000C | Полировальная машина Makita PV7000C | https://makita-snab.ru/magazin/product/polirovalnaya-mashina-makita-pv7000c | — | true | category breadcrumb not observable; canonical link tag absent |
| SD100DZ | Аккумуляторная пила для гипсокартона Makita SD100DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-pila-dlya-gipsokartona-makita-sd100dz | — | true | category breadcrumb not observable; canonical link tag absent |

---

## Products Found

All **8** SKUs in scope — dedicated product pages on makita-snab.ru:

| sku | product_title |
|-----|---------------|
| CL114FDWI | Аккумуляторный пылесос Makita CL114FDWI |
| CL106FDWY | Аккумуляторный пылесос Makita CL106FDWY |
| CL121DWA | Аккумуляторный пылесос Makita CL121DWA |
| DCL284FRF | Аккумуляторный пылесос Makita DCL284FRF |
| DPP200ZK | Аккумуляторный дырокол с гидравлическим приводом Makita DPP200ZK |
| DSC121ZK | Шпилькорез Makita DSC121ZK |
| PV7000C | Полировальная машина Makita PV7000C |
| SD100DZ | Аккумуляторная пила для гипсокартона Makita SD100DZ |

---

## Products Missing

**None** within the 8-SKU named scope.

---

## Category Summary

**Site navigation category (`category` field):** **not observable** on product pages for any SKU in scope (breadcrumb markup absent or not extractable at capture time).

**Product-type signals from verified `<h1>` titles** *(informational — not site taxonomy assignment):*

| Product-type signal (from title) | Count | SKUs |
|----------------------------------|-------|------|
| Аккумуляторный пылесос | 4 | CL114FDWI, CL106FDWY, CL121DWA, DCL284FRF |
| Аккумуляторный дырокол | 1 | DPP200ZK |
| Шпилькорез | 1 | DSC121ZK |
| Полировальная машина | 1 | PV7000C |
| Аккумуляторная пила для гипсокартона | 1 | SD100DZ |

**Homepage catalog filters observed** (not mapped to SKUs): Аккумуляторный инструмент, Электрический инструмент, Измерительный инструмент, Расходные материалы, Запасные части MAKITA, and others.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Additional approved SKUs between bookends (`…` in operator list) | **SAFE UNKNOWN** — not separately enumerated in agent-accessible persistence; only 8 named SKUs verified |
| Site navigation `category` per SKU | **SAFE UNKNOWN** — breadcrumb not observable on product pages |
| `<link rel="canonical">` on product pages | **Absent** at capture — sitemap URL used |
| Variant pages (e.g. `bez-akb-i-bez-zu` slugs) | Alternate URLs exist in sitemap; primary product slug selected per selection rule |
| Stock / price / offer signals | **Out of scope** |
| `atlas_website_ref` / `WEB-*` | **SAFE UNKNOWN** — Website not attested in ATLAS |
| Search route `/?search={SKU}` | Returns unfiltered catalog at capture — unreliable for SKU resolution |

---

## Evidence Pointers

| Ref | Path / note |
|-----|-------------|
| ATLAS org | `projects/atlas/population/ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md` — ORG-0007 |
| Sitemap capture | `https://makita-snab.ru/sitemap.xml` (2026-06-07) |
| Verification output | `.recovery-temp/makita-surface-results.json` |
| Verification script | `.recovery-temp/makita-surface-sitemap-verify.mjs` |

---

## Recommended Next Step

**Prepare Demand Surface from verified product titles** — separate MIG pass; seed product-type language from `<h1>` titles above; Wordstat not in Product Surface scope.

If additional SKUs exist in the full approved list beyond the 8 named anchors, re-run this inventory pass for those SKUs before Demand Surface binding.

---

*Makita Product Surface Inventory v1 — groundtruth capture · documentation only*

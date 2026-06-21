# Makita Product Surface Inventory v2

**Status:** verified — full approved SKU scope  
**Layer:** MIG Product Surface (groundtruth only)  
**Date:** 2026-06-07  
**Pilot:** Makita Snab  
**Primary website:** https://makita-snab.ru  
**ATLAS context:** atlas_client_org_ref = ORG-0007  
**Region:** Москва и Московская область  
**Sales model:** Retail  

**Boundaries:** No Wordstat · No keyword registry · No ORCA · No PPC · No campaign architecture · No demand inference.

---

## Input Source

| Input | Source | Observed |
|-------|--------|----------|
| Approved SKU list | incoming/mig/pilots/makita/approved-sku-list-v1.md | **70 SKUs** enumerated |

**Scope for this pass:** all **70** SKUs from approved-sku-list-v1.md. No SKU skipped. No SKU inferred beyond source.

---

## Capture Method

| Step | Method |
|------|--------|
| 1 | Resolve product URL via live sitemap.xml (/magazin/product/{slug} containing SKU) |
| 2 | GET product page — HTTP 200 required |
| 3 | product_title ← h1 |
| 4 | product_url ← link rel=canonical when present; else sitemap product URL |
| 5 | category ← breadcrumb trail when present on page |
| 6 | page_found = true only when dedicated product page loads with SKU match in h1 / page body |

**Capture timestamp:** 2026-06-07

---

## Coverage Summary

| Metric | Value |
|--------|-------|
| Approved SKUs in scope | **70** |
| SKUs verified on site | **70** |
| page_found = true | **70** |
| page_found = false | **0** |
| Coverage rate | **100%** |

---

## Product Inventory

| sku | product_title | product_url | category | page_found | safe_unknown |
|-----|---------------|-------------|----------|------------|--------------|
| CL114FDWI | Аккумуляторный пылесос Makita CL114FDWI | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl114fdwi | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| CL106FDWY | Аккумуляторный пылесос Makita CL106FDWY | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-cl106fdwy | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| CL121DWA | Аккумуляторный пылесос Makita CL121DWA | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-cl121dwa | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DCL284FRF | Аккумуляторный пылесос Makita DCL284FRF | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl284frf | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DCL181FZ | Аккумуляторный пылесос Makita DCL181FZ | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-dcl181fz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DCL184Z | Аккумуляторный пылесос Makita DCL184Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl184z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DCL281FZ | Аккумуляторный пылесос Makita DCL281FZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl281fz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DCL284FZ | Аккумуляторный пылесос Makita DCL284FZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl284fz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DCL286FZ | Аккумуляторный пылесос Makita DCL286FZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl286fz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| CL001GZ04 | Аккумуляторный пылесос Makita CL001GZ04 | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl001gz04 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| CL003GZ | Аккумуляторный пылесос Makita CL003GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl003gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DVC261ZX11 | Аккумуляторный пылесос Makita DVC261ZX11 | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-dvc261zx11 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DVC265ZXU | Аккумуляторный ранцевый пылесос Makita DVC265ZXU | https://makita-snab.ru/magazin/product/pylesos-makita-dvc265zxu | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DVC157LZX3 | Аккумуляторный пылесос Makita DVC157LZX3 | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dvc157lzx3 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 1910D4-2 | Насадка Циклон для аккумуляторных пылесосов Makita 1910D4-2 | https://makita-snab.ru/magazin/product/nasadka-ciklon-dlya-akkumulyatornyh-pylesosov-makita-1910d4-2 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 1911L1-0 | Напольная подставка для пылесоса CXT/LXT/XGT Makita 1911L1-0 | https://makita-snab.ru/magazin/product/napolnaya-podstavka-dlya-pylesosa-cxt-lxt-xgt-makita-1911l1-0 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 191D73-9 | Насадка Циклон для аккумуляторных пылесосов Makita 191D73-9 | https://makita-snab.ru/magazin/product/nasadka-ciklon-dlya-akkumulyatornyh-pylesosov-makita-191d73-9 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DTW700Z | Аккумуляторный ударный гайковерт Makita DTW700Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-udarnyj-gajkovert-makita-dtw700z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DP4010 | Дрель Makita DP4010 | https://makita-snab.ru/magazin/product/drel-makita-dp4010 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| UX01GZ | Аккумуляторный мотоблок Makita UX01GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-motoblok-makita-ux01gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DK0116 | Набор инструмента,2шт Makita DK0116 | https://makita-snab.ru/magazin/product/nabor-instrumenta-2sht-makita-dk0116 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DK0117 | Набор инструмента,2шт Makita DK0117 | https://makita-snab.ru/magazin/product/nabor-instrumenta-2sht-makita-dk0117 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DK0167 | Набор инструмента,2шт Makita DK0167 | https://makita-snab.ru/magazin/product/nabor-instrumenta-2sht-makita-dk0167 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| UR3501 | Электрический триммер Makita UR3501 | https://makita-snab.ru/magazin/product/elektricheskiy-trimmer-makita-ur3501 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| UR3502 | Электрический триммер Makita UR3502 | https://makita-snab.ru/magazin/product/elektricheskiy-trimmer-makita-ur3502 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 191X80-2 | Кейс MAKPAC с органайзером Makita 191X80-2 | https://makita-snab.ru/magazin/product/kejs-makpac-s-organajzerom-makita-191x80-2 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 792264-7 | Матрица Makita 792264-7 | https://makita-snab.ru/magazin/product/matritsa-makita-792264-7 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 792536-0 | Боковой резец  Makita 792536-0 | https://makita-snab.ru/magazin/product/bokovoy-rezets-makita-792536-0 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 824651-3 | Чемодан для пил Makita 824651-3 | https://makita-snab.ru/magazin/product/chemodan-dlya-pil-makita-824651-3 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 824755-1 | Чемодан для углошлифовальных машин Makita 824755-1 | https://makita-snab.ru/magazin/product/chemodan-dlya-ugloshlifovalnykh-mashin-makita-824755-1 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 832188-6 | Сумка для инструмента Makita 832188-6 | https://makita-snab.ru/magazin/product/sumka-dlya-instrumenta-makita-832188-6 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 831278-2 | Сумка для инструментов Makita 831278-2 | https://makita-snab.ru/magazin/product/sumka-dlya-instrumentov-makita-831278-2 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 831271-6 | Сумка для инструментов Makita 831271-6 | https://makita-snab.ru/magazin/product/sumka-dlya-instrumentov-makita-831271-6 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| 1912E8-3 | Цепь 15см Makita 1912E8-3 | https://makita-snab.ru/magazin/product/cep-15sm-makita-1912e8-3 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| YA00000474 | Катушка для триммеров Makita YA00000474 | https://makita-snab.ru/magazin/product/katushka-dlya-trimmerov-makita-ya00000474 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| YA00000491 | Защитный кожух в сборе для UR3500/UR3501 Makita YA00000491 | https://makita-snab.ru/magazin/product/zashchitnyy-kozhukh-v-sbore-dlya-ur3500-ur3501-makita-ya00000491 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| ADP08 | Адаптер USB для 10.8V CXT Makita ADP08 | https://makita-snab.ru/magazin/product/adapter-usb-dlya-10-8v-cxt-makita-adp08 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| AS001GZ | Воздуходувка XGT Makita AS001GZ | https://makita-snab.ru/magazin/product/vozduhoduvka-xgt-makita-as001gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DA332DZ | Аккумуляторная угловая дрель Makita DA332DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-uglovaya-drel-makita-da332dz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DGD801Z | Аккумуляторная прямая шлифовальная машина Makita DGD801Z | https://makita-snab.ru/magazin/product/shlifmashina-pr-makita-dgd801z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DHR202RF | Аккумуляторный перфоратор Makita DHR202RF | https://makita-snab.ru/magazin/product/akkumulyatornyy-perforator-makita-dhr202rf | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DJV185Z | Аккумуляторный лобзик Makita DJV185Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-lobzik-makita-djv185z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DKP181ZU | Аккумуляторный рубанок Makita DKP181ZU | https://makita-snab.ru/magazin/product/akkumulyatornyj-rubanok-makita-dkp181zu | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DTD156Z | Аккумуляторный ударный шуруповерт Makita DTD156Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-udarnyj-shurupovert-makita-dtd156z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DTD172Z | Промо Акция PT1322-1 Makita DDF485Z + DTD172Z | https://makita-snab.ru/magazin/product/promo-akciya-pt1322-1-makita-ddf485z-dtd172z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DTW190Z | Аккумуляторный ударный гайковерт Makita DTW190Z | https://makita-snab.ru/magazin/product/akkumulyatornyy-udarnyy-gaykovert-makita-dtw190z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DUB186Z | Аккумуляторная воздуходувка Makita DUB186Z | https://makita-snab.ru/magazin/product/akkumulyatornaya-vozduhoduvka-makita-dub186z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DUC204SF | Аккумуляторная цепная пила Makita DUC204SF | https://makita-snab.ru/magazin/product/pila-cepnaya-makita-duc204sf | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DUC302Z | Аккумуляторная цепная пила Makita DUC302Z | https://makita-snab.ru/magazin/product/akkumulyatornaya-tsepnaya-pila-makita-duc302z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DUC356Z | Аккумуляторная цепная пила Makita DUC356Z | https://makita-snab.ru/magazin/product/akkumulyatornaya-cepnaya-pila-makita-duc356z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DUX18Z | Аккумуляторный мотоблок Makita DUX18Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-motoblok-makita-dux18z | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| GA005GZ | Угловая шлифмашина XGT Makita GA005GZ | https://makita-snab.ru/magazin/product/uglovaya-shlifmashina-xgt-makita-ga005gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| GA5030RK | Углошлифовальная машина Makita GA5030RK | https://makita-snab.ru/magazin/product/ugloshlifovalnaya-mashina-makita-ga5030rk | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| GA5100 | Углошлифовальная машина Makita GA5100 | https://makita-snab.ru/magazin/product/ugloshlifovalnaya-mashina-makita-ga5100 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| GA7090N | Углошлифовальная машина Makita GA7090N | https://makita-snab.ru/magazin/product/ugloshlifovalnaya-mashina-makita-ga7090n | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| GD0800C | Прямая шлифовальная машина Makita GD0800C | https://makita-snab.ru/magazin/product/pryamaya-shlifovalnaya-mashina-makita-gd0800c | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| HR004GZ | Перфоратор SDS+ 3-х режимный XGT HR004GZ | https://makita-snab.ru/magazin/product/perforator-sds-3-h-rezhimnyj-xgt-hr004gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| HS7000 | Дисковая пила Makita HS7000 | https://makita-snab.ru/magazin/product/diskovaya-pila-makita-hs7000 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| JV001GZ01 | Лобзик XGT Makita JV001GZ01 | https://makita-snab.ru/magazin/product/lobzik-xgt-makita-jv001gz01 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| JV002GZ | Лобзик XGT Makita JV002GZ | https://makita-snab.ru/magazin/product/lobzik-xgt-makita-jv002gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| KP001GZ | Аккумуляторный рубанок Makita KP001GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-rubanok-makita-kp001gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| KT001GZ | Аккумуляторный чайник Makita KT001GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-chajnik-makita-kt001gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| M8701 | Перфоратор Makita MT (Красная) M8701 | https://makita-snab.ru/magazin/product/perforator-makita-mt-krasnaya-m8701 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| TD003GA201 | Импульсный шуруповерт (винтоверт) XGT Makita TD003GA201 | https://makita-snab.ru/magazin/product/impulsnyj-shurupovert-vintovert-xgt-makita-td003ga201 | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| TW007GZ | Ударный гайковерт XGT Makita TW007GZ | https://makita-snab.ru/magazin/product/udarnyj-gajkovert-xgt-makita-tw007gz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| UC100DZ | Аккумуляторная цепная пила Makita UC100DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-cepnaya-pila-makita-uc100dz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DPP200ZK | Аккумуляторный дырокол с гидравлическим приводом Makita DPP200ZK | https://makita-snab.ru/magazin/product/akkumulyatornyj-dyrokol-s-gidravlicheskim-privodom-makita-dpp200zk | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| DSC121ZK | Шпилькорез Makita DSC121ZK | https://makita-snab.ru/magazin/product/shpilkorez-makita-dsc121zk | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| PV7000C | Полировальная машина Makita PV7000C | https://makita-snab.ru/magazin/product/polirovalnaya-mashina-makita-pv7000c | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |
| SD100DZ | Аккумуляторная пила для гипсокартона Makita SD100DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-pila-dlya-gipsokartona-makita-sd100dz | — | true | category breadcrumb not observable on product page; canonical link tag absent; using sitemap product URL |

---

## Evidence Pointers

| Ref | Path / note |
|-----|-------------|
| Approved SKU source | incoming/mig/pilots/makita/approved-sku-list-v1.md |
| Sitemap capture | https://makita-snab.ru/sitemap.xml (2026-06-07) |
| Verification output | .recovery-temp/makita-surface-v2-results.json |
| Verification script | .recovery-temp/makita-surface-v2-verify.mjs |

---

*Makita Product Surface Inventory v2 — groundtruth capture · documentation only*

# Makita Demand Surface Seed List v1

**Status:** seed list — operator Wordstat input  
**Layer:** MIG Demand Surface (seed normalization only)  
**Date:** 2026-06-07  
**Pilot:** Makita Snab  
**Source:** incoming/mig/pilots/makita/product-surface-inventory-v2.md  
**Primary website:** https://makita-snab.ru  
**ATLAS context:** atlas_client_org_ref = ORG-0007  
**Region:** Москва и Московская область  
**Sales model:** Retail  

**Boundaries:** No Wordstat · No frequency inference · No keyword registry · No ORCA · No PPC · No campaign architecture.

---

## Normalization Rules (this pass)

| Rule | Application |
|------|-------------|
| Phrase shape | `{product_type} makita {sku_lower}` |
| Casing | lowercase throughout |
| Modifiers stripped | аккумуляторный/ая/ое, ударный/ая, электрический, XGT, CXT/LXT/XGT platform tags |
| Short types | углошлифовальная машина → **ушм**; аккумуляторная цепная пила → **цепная пила** |
| demand_class | PRIMARY · SECONDARY · ACCESSORY · SPECIALIZED — assigned from product type, not demand volume |

---

## Coverage Summary

| Metric | Value |
|--------|-------|
| Source SKUs (verified Product Surface v2) | **70** |
| Seed rows emitted | **70** |
| Coverage rate | **100%** |

| demand_class | Count |
|--------------|-------|
| PRIMARY | **46** |
| SECONDARY | **6** |
| ACCESSORY | **15** |
| SPECIALIZED | **3** |

---

## Seed List

| sku | product_title | landing_url | product_type | normalized_demand_phrase | demand_class | safe_unknown |
|-----|---------------|-------------|--------------|--------------------------|--------------|--------------|
| CL114FDWI | Аккумуляторный пылесос Makita CL114FDWI | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl114fdwi | пылесос | пылесос makita cl114fdwi | PRIMARY | — |
| CL106FDWY | Аккумуляторный пылесос Makita CL106FDWY | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-cl106fdwy | пылесос | пылесос makita cl106fdwy | PRIMARY | — |
| CL121DWA | Аккумуляторный пылесос Makita CL121DWA | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-cl121dwa | пылесос | пылесос makita cl121dwa | PRIMARY | — |
| DCL284FRF | Аккумуляторный пылесос Makita DCL284FRF | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl284frf | пылесос | пылесос makita dcl284frf | PRIMARY | — |
| DCL181FZ | Аккумуляторный пылесос Makita DCL181FZ | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-dcl181fz | пылесос | пылесос makita dcl181fz | PRIMARY | — |
| DCL184Z | Аккумуляторный пылесос Makita DCL184Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl184z | пылесос | пылесос makita dcl184z | PRIMARY | — |
| DCL281FZ | Аккумуляторный пылесос Makita DCL281FZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl281fz | пылесос | пылесос makita dcl281fz | PRIMARY | — |
| DCL284FZ | Аккумуляторный пылесос Makita DCL284FZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl284fz | пылесос | пылесос makita dcl284fz | PRIMARY | — |
| DCL286FZ | Аккумуляторный пылесос Makita DCL286FZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dcl286fz | пылесос | пылесос makita dcl286fz | PRIMARY | — |
| CL001GZ04 | Аккумуляторный пылесос Makita CL001GZ04 | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl001gz04 | пылесос | пылесос makita cl001gz04 | PRIMARY | — |
| CL003GZ | Аккумуляторный пылесос Makita CL003GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-cl003gz | пылесос | пылесос makita cl003gz | PRIMARY | — |
| DVC261ZX11 | Аккумуляторный пылесос Makita DVC261ZX11 | https://makita-snab.ru/magazin/product/akkumulyatornyy-pylesos-makita-dvc261zx11 | пылесос | пылесос makita dvc261zx11 | PRIMARY | — |
| DVC265ZXU | Аккумуляторный ранцевый пылесос Makita DVC265ZXU | https://makita-snab.ru/magazin/product/pylesos-makita-dvc265zxu | ранцевый пылесос | ранцевый пылесос makita dvc265zxu | PRIMARY | product_type inferred from title modifier «ранцевый»; not in canonical short-type list |
| DVC157LZX3 | Аккумуляторный пылесос Makita DVC157LZX3 | https://makita-snab.ru/magazin/product/akkumulyatornyj-pylesos-makita-dvc157lzx3 | пылесос | пылесос makita dvc157lzx3 | PRIMARY | — |
| 1910D4-2 | Насадка Циклон для аккумуляторных пылесосов Makita 1910D4-2 | https://makita-snab.ru/magazin/product/nasadka-ciklon-dlya-akkumulyatornyh-pylesosov-makita-1910d4-2 | насадка циклон | насадка циклон makita 1910d4-2 | ACCESSORY | — |
| 1911L1-0 | Напольная подставка для пылесоса CXT/LXT/XGT Makita 1911L1-0 | https://makita-snab.ru/magazin/product/napolnaya-podstavka-dlya-pylesosa-cxt-lxt-xgt-makita-1911l1-0 | подставка для пылесоса | подставка для пылесоса makita 1911l1-0 | ACCESSORY | — |
| 191D73-9 | Насадка Циклон для аккумуляторных пылесосов Makita 191D73-9 | https://makita-snab.ru/magazin/product/nasadka-ciklon-dlya-akkumulyatornyh-pylesosov-makita-191d73-9 | насадка циклон | насадка циклон makita 191d73-9 | ACCESSORY | — |
| DTW700Z | Аккумуляторный ударный гайковерт Makita DTW700Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-udarnyj-gajkovert-makita-dtw700z | гайковерт | гайковерт makita dtw700z | PRIMARY | — |
| DP4010 | Дрель Makita DP4010 | https://makita-snab.ru/magazin/product/drel-makita-dp4010 | дрель | дрель makita dp4010 | PRIMARY | — |
| UX01GZ | Аккумуляторный мотоблок Makita UX01GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-motoblok-makita-ux01gz | мотоблок | мотоблок makita ux01gz | SECONDARY | — |
| DK0116 | Набор инструмента,2шт Makita DK0116 | https://makita-snab.ru/magazin/product/nabor-instrumenta-2sht-makita-dk0116 | набор инструмента | набор инструмента makita dk0116 | PRIMARY | bundle composition not resolved from title alone |
| DK0117 | Набор инструмента,2шт Makita DK0117 | https://makita-snab.ru/magazin/product/nabor-instrumenta-2sht-makita-dk0117 | набор инструмента | набор инструмента makita dk0117 | PRIMARY | bundle composition not resolved from title alone |
| DK0167 | Набор инструмента,2шт Makita DK0167 | https://makita-snab.ru/magazin/product/nabor-instrumenta-2sht-makita-dk0167 | набор инструмента | набор инструмента makita dk0167 | PRIMARY | bundle composition not resolved from title alone |
| UR3501 | Электрический триммер Makita UR3501 | https://makita-snab.ru/magazin/product/elektricheskiy-trimmer-makita-ur3501 | триммер | триммер makita ur3501 | SECONDARY | — |
| UR3502 | Электрический триммер Makita UR3502 | https://makita-snab.ru/magazin/product/elektricheskiy-trimmer-makita-ur3502 | триммер | триммер makita ur3502 | SECONDARY | — |
| 191X80-2 | Кейс MAKPAC с органайзером Makita 191X80-2 | https://makita-snab.ru/magazin/product/kejs-makpac-s-organajzerom-makita-191x80-2 | кейс | кейс makita 191x80-2 | ACCESSORY | — |
| 792264-7 | Матрица Makita 792264-7 | https://makita-snab.ru/magazin/product/matritsa-makita-792264-7 | матрица | матрица makita 792264-7 | ACCESSORY | — |
| 792536-0 | Боковой резец  Makita 792536-0 | https://makita-snab.ru/magazin/product/bokovoy-rezets-makita-792536-0 | боковой резец | боковой резец makita 792536-0 | ACCESSORY | — |
| 824651-3 | Чемодан для пил Makita 824651-3 | https://makita-snab.ru/magazin/product/chemodan-dlya-pil-makita-824651-3 | чемодан для пил | чемодан для пил makita 824651-3 | ACCESSORY | — |
| 824755-1 | Чемодан для углошлифовальных машин Makita 824755-1 | https://makita-snab.ru/magazin/product/chemodan-dlya-ugloshlifovalnykh-mashin-makita-824755-1 | чемодан для ушм | чемодан для ушм makita 824755-1 | ACCESSORY | — |
| 832188-6 | Сумка для инструмента Makita 832188-6 | https://makita-snab.ru/magazin/product/sumka-dlya-instrumenta-makita-832188-6 | сумка | сумка makita 832188-6 | ACCESSORY | — |
| 831278-2 | Сумка для инструментов Makita 831278-2 | https://makita-snab.ru/magazin/product/sumka-dlya-instrumentov-makita-831278-2 | сумка | сумка makita 831278-2 | ACCESSORY | — |
| 831271-6 | Сумка для инструментов Makita 831271-6 | https://makita-snab.ru/magazin/product/sumka-dlya-instrumentov-makita-831271-6 | сумка | сумка makita 831271-6 | ACCESSORY | — |
| 1912E8-3 | Цепь 15см Makita 1912E8-3 | https://makita-snab.ru/magazin/product/cep-15sm-makita-1912e8-3 | цепь | цепь makita 1912e8-3 | ACCESSORY | — |
| YA00000474 | Катушка для триммеров Makita YA00000474 | https://makita-snab.ru/magazin/product/katushka-dlya-trimmerov-makita-ya00000474 | катушка для триммера | катушка для триммера makita ya00000474 | ACCESSORY | — |
| YA00000491 | Защитный кожух в сборе для UR3500/UR3501 Makita YA00000491 | https://makita-snab.ru/magazin/product/zashchitnyy-kozhukh-v-sbore-dlya-ur3500-ur3501-makita-ya00000491 | защитный кожух | защитный кожух makita ya00000491 | ACCESSORY | — |
| ADP08 | Адаптер USB для 10.8V CXT Makita ADP08 | https://makita-snab.ru/magazin/product/adapter-usb-dlya-10-8v-cxt-makita-adp08 | адаптер | адаптер makita adp08 | ACCESSORY | — |
| AS001GZ | Воздуходувка XGT Makita AS001GZ | https://makita-snab.ru/magazin/product/vozduhoduvka-xgt-makita-as001gz | воздуходувка | воздуходувка makita as001gz | SECONDARY | — |
| DA332DZ | Аккумуляторная угловая дрель Makita DA332DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-uglovaya-drel-makita-da332dz | угловая дрель | угловая дрель makita da332dz | PRIMARY | — |
| DGD801Z | Аккумуляторная прямая шлифовальная машина Makita DGD801Z | https://makita-snab.ru/magazin/product/shlifmashina-pr-makita-dgd801z | шлифмашина | шлифмашина makita dgd801z | PRIMARY | — |
| DHR202RF | Аккумуляторный перфоратор Makita DHR202RF | https://makita-snab.ru/magazin/product/akkumulyatornyy-perforator-makita-dhr202rf | перфоратор | перфоратор makita dhr202rf | PRIMARY | — |
| DJV185Z | Аккумуляторный лобзик Makita DJV185Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-lobzik-makita-djv185z | лобзик | лобзик makita djv185z | PRIMARY | — |
| DKP181ZU | Аккумуляторный рубанок Makita DKP181ZU | https://makita-snab.ru/magazin/product/akkumulyatornyj-rubanok-makita-dkp181zu | рубанок | рубанок makita dkp181zu | PRIMARY | — |
| DTD156Z | Аккумуляторный ударный шуруповерт Makita DTD156Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-udarnyj-shurupovert-makita-dtd156z | шуруповерт | шуруповерт makita dtd156z | PRIMARY | — |
| DTD172Z | Промо Акция PT1322-1 Makita DDF485Z + DTD172Z | https://makita-snab.ru/magazin/product/promo-akciya-pt1322-1-makita-ddf485z-dtd172z | шуруповерт | шуруповерт makita dtd172z | PRIMARY | promo bundle page lists DDF485Z + DTD172Z; seed phrase anchored to listed SKU DTD172Z only |
| DTW190Z | Аккумуляторный ударный гайковерт Makita DTW190Z | https://makita-snab.ru/magazin/product/akkumulyatornyy-udarnyy-gaykovert-makita-dtw190z | гайковерт | гайковерт makita dtw190z | PRIMARY | — |
| DUB186Z | Аккумуляторная воздуходувка Makita DUB186Z | https://makita-snab.ru/magazin/product/akkumulyatornaya-vozduhoduvka-makita-dub186z | воздуходувка | воздуходувка makita dub186z | SECONDARY | — |
| DUC204SF | Аккумуляторная цепная пила Makita DUC204SF | https://makita-snab.ru/magazin/product/pila-cepnaya-makita-duc204sf | цепная пила | цепная пила makita duc204sf | PRIMARY | — |
| DUC302Z | Аккумуляторная цепная пила Makita DUC302Z | https://makita-snab.ru/magazin/product/akkumulyatornaya-tsepnaya-pila-makita-duc302z | цепная пила | цепная пила makita duc302z | PRIMARY | — |
| DUC356Z | Аккумуляторная цепная пила Makita DUC356Z | https://makita-snab.ru/magazin/product/akkumulyatornaya-cepnaya-pila-makita-duc356z | цепная пила | цепная пила makita duc356z | PRIMARY | — |
| DUX18Z | Аккумуляторный мотоблок Makita DUX18Z | https://makita-snab.ru/magazin/product/akkumulyatornyj-motoblok-makita-dux18z | мотоблок | мотоблок makita dux18z | SECONDARY | — |
| GA005GZ | Угловая шлифмашина XGT Makita GA005GZ | https://makita-snab.ru/magazin/product/uglovaya-shlifmashina-xgt-makita-ga005gz | ушм | ушм makita ga005gz | PRIMARY | — |
| GA5030RK | Углошлифовальная машина Makita GA5030RK | https://makita-snab.ru/magazin/product/ugloshlifovalnaya-mashina-makita-ga5030rk | ушм | ушм makita ga5030rk | PRIMARY | — |
| GA5100 | Углошлифовальная машина Makita GA5100 | https://makita-snab.ru/magazin/product/ugloshlifovalnaya-mashina-makita-ga5100 | ушм | ушм makita ga5100 | PRIMARY | — |
| GA7090N | Углошлифовальная машина Makita GA7090N | https://makita-snab.ru/magazin/product/ugloshlifovalnaya-mashina-makita-ga7090n | ушм | ушм makita ga7090n | PRIMARY | — |
| GD0800C | Прямая шлифовальная машина Makita GD0800C | https://makita-snab.ru/magazin/product/pryamaya-shlifovalnaya-mashina-makita-gd0800c | шлифмашина | шлифмашина makita gd0800c | PRIMARY | — |
| HR004GZ | Перфоратор SDS+ 3-х режимный XGT HR004GZ | https://makita-snab.ru/magazin/product/perforator-sds-3-h-rezhimnyj-xgt-hr004gz | перфоратор | перфоратор makita hr004gz | PRIMARY | — |
| HS7000 | Дисковая пила Makita HS7000 | https://makita-snab.ru/magazin/product/diskovaya-pila-makita-hs7000 | дисковая пила | дисковая пила makita hs7000 | PRIMARY | — |
| JV001GZ01 | Лобзик XGT Makita JV001GZ01 | https://makita-snab.ru/magazin/product/lobzik-xgt-makita-jv001gz01 | лобзик | лобзик makita jv001gz01 | PRIMARY | — |
| JV002GZ | Лобзик XGT Makita JV002GZ | https://makita-snab.ru/magazin/product/lobzik-xgt-makita-jv002gz | лобзик | лобзик makita jv002gz | PRIMARY | — |
| KP001GZ | Аккумуляторный рубанок Makita KP001GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-rubanok-makita-kp001gz | рубанок | рубанок makita kp001gz | PRIMARY | — |
| KT001GZ | Аккумуляторный чайник Makita KT001GZ | https://makita-snab.ru/magazin/product/akkumulyatornyj-chajnik-makita-kt001gz | чайник | чайник makita kt001gz | SPECIALIZED | product category outside core power-tool taxonomy; demand_class assigned by rarity |
| M8701 | Перфоратор Makita MT (Красная) M8701 | https://makita-snab.ru/magazin/product/perforator-makita-mt-krasnaya-m8701 | перфоратор | перфоратор makita m8701 | PRIMARY | — |
| TD003GA201 | Импульсный шуруповерт (винтоверт) XGT Makita TD003GA201 | https://makita-snab.ru/magazin/product/impulsnyj-shurupovert-vintovert-xgt-makita-td003ga201 | шуруповерт | шуруповерт makita td003ga201 | PRIMARY | title lists винтоверт synonym; seed uses шуруповерт as primary retail type |
| TW007GZ | Ударный гайковерт XGT Makita TW007GZ | https://makita-snab.ru/magazin/product/udarnyj-gajkovert-xgt-makita-tw007gz | гайковерт | гайковерт makita tw007gz | PRIMARY | — |
| UC100DZ | Аккумуляторная цепная пила Makita UC100DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-cepnaya-pila-makita-uc100dz | цепная пила | цепная пила makita uc100dz | PRIMARY | — |
| DPP200ZK | Аккумуляторный дырокол с гидравлическим приводом Makita DPP200ZK | https://makita-snab.ru/magazin/product/akkumulyatornyj-dyrokol-s-gidravlicheskim-privodom-makita-dpp200zk | дырокол | дырокол makita dpp200zk | SPECIALIZED | — |
| DSC121ZK | Шпилькорез Makita DSC121ZK | https://makita-snab.ru/magazin/product/shpilkorez-makita-dsc121zk | шпилькорез | шпилькорез makita dsc121zk | SPECIALIZED | — |
| PV7000C | Полировальная машина Makita PV7000C | https://makita-snab.ru/magazin/product/polirovalnaya-mashina-makita-pv7000c | полировальная машина | полировальная машина makita pv7000c | PRIMARY | — |
| SD100DZ | Аккумуляторная пила для гипсокартона Makita SD100DZ | https://makita-snab.ru/magazin/product/akkumulyatornaya-pila-dlya-gipsokartona-makita-sd100dz | пила для гипсокартона | пила для гипсокартона makita sd100dz | PRIMARY | niche saw type retained in product_type per title |

---

## Product Groups (by product_type)

| product_type | Count | demand_class mix |
|--------------|-------|------------------|
| пылесос | 13 | PRIMARY |
| ранцевый пылесос | 1 | PRIMARY |
| ушм | 4 | PRIMARY |
| цепная пила | 4 | PRIMARY |
| перфоратор | 3 | PRIMARY |
| лобзик | 3 | PRIMARY |
| гайковерт | 3 | PRIMARY |
| набор инструмента | 3 | PRIMARY |
| шуруповерт | 3 | PRIMARY |
| сумка | 3 | PRIMARY |
| триммер | 2 | SECONDARY |
| мотоблок | 2 | SECONDARY |
| воздуходувка | 2 | SECONDARY |
| шлифмашина | 2 | PRIMARY |
| рубанок | 2 | PRIMARY |
| насадка циклон | 2 | ACCESSORY |
| дрель / угловая дрель | 2 | PRIMARY |
| дисковая пила / пила для гипсокартона / полировальная машина | 3 | PRIMARY |
| accessory singles (кейс, матрица, резец, чемоданы, цепь, катушка, кожух, адаптер, подставка) | 10 | ACCESSORY |
| дырокол / шпилькорез / чайник | 3 | SPECIALIZED |

---

## Evidence Pointers

| Ref | Path / note |
|-----|-------------|
| Product Surface source | incoming/mig/pilots/makita/product-surface-inventory-v2.md |
| Approved SKU source | incoming/mig/pilots/makita/approved-sku-list-v1.md |
| ATLAS org | atlas_client_org_ref = ORG-0007 |

---

## Recommended Next Step

**Operator Wordstat Collection** — run normalized_demand_phrase set against Wordstat for Москва и Московская область; no frequency inference in this pass.

---

*Makita Demand Surface Seed List v1 — seed normalization · documentation only*

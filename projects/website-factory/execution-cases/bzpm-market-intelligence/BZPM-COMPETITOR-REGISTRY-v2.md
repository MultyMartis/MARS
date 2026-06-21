# REPORT — BZPM MI W3X Registry Consolidation

**Программа:** BZPM Market Intelligence  
**Волна:** W3X — Registry Consolidation & Master Report v1  
**Lane:** A  
**Authority:** W1 · W2 · W2.5 · W3 · W3R · W3S (approved) · BZPM MI Methodology v1  
**Scope:** consolidation only — без competitor intelligence, UX, PDP, catalog analysis и рекомендаций  
**Дата:** 2026-06-14  

---

## Executive Summary

Сформирован **BZPM Competitor Registry v2** — консолидированный baseline из W3 Registry (**46** approved entities), W3R regional pool (**38** raw rows → **48** canonical expansion slots после dedup), W3S SERP pool (**27** new domains), W2.5 deferred (**21**) и W2 rejections (**11**).

**Canonical universe:** **126** entities после deduplication (branch/subdomain merge).

### Registry Statistics

| Metric | Value |
| --- | --- |
| Total canonical entities | 126 |
| Approved Registry (W3) | 46 |
| Strong Expansion Candidates | 21 |
| Possible Expansion Candidates | 22 |
| Deferred | 26 |
| Excluded | 11 |
| W2 raw discovery universe | 80 |
| W3R raw regional rows | 38 |
| W3S new SERP domains | 27 |

### Coverage Statistics (Registry v2 — Approved + Strong expansion)

| Coverage Zone | Approved (W3) | Strong expansion adds |
| --- | --- | --- |
| Siberia | 14 | +6 (Lerius, Алтай-Посуда, Kobor, НОТИС, …) |
| Ural | 13 | +2 (Юниторг, Комплекс Трейд) |
| Far East | 8 indirect | +3 (Kobor, ТоХоРека, ФудПром FE) |
| Kazakhstan | 10 | +4 (Bioshop, FoodPro.kz, Атико, KarTC) |
| Belarus | 10 | +2 (ПРОФИ, Сервиспищеторг) |
| European Russia | 28 | +5 federal/OEM (Практика, Проммash, КАМИК, …) |

### Visibility Statistics (W3S — top 15)

| Company | Website | Appearances | In Registry v2 Approved? |
| --- | --- | --- | --- |
| Trapeza | https://www.trapeza.ru/ | 8 | Yes (COMP-BZPM-011) |
| КЛЕН | https://www.klenmarket.ru/ | 7 | Yes (COMP-BZPM-012) |
| РЕФРО | https://www.refro.ru/ | 5 | Yes (COMP-BZPM-016) |
| Практика | https://www.pectopah.ru/ | 5 | Strong expansion |
| Проммash | https://prommash.com/ | 5 | Strong expansion |
| Kobor | https://kobor.ru/ | 5 | Strong expansion |
| Abat | https://abat.ru/ | 4 | Yes (COMP-BZPM-001) |
| Restoll | https://restoll.ru/ | 4 | Yes (COMP-BZPM-018) |
| Finist | https://f-inox.ru/ | 4 | Yes (COMP-BZPM-003) |
| Ресторан Комплект | https://r-komplekt.ru/ | 4 | Strong expansion |
| КАМИК | https://kamik-group.ru/ | 4 | Strong expansion |
| МетаКон | https://zavod-metakon.ru/ | 4 | Strong expansion |
| НОТИС | https://www.notis.ru/ | 4 | Strong expansion |
| Энтерo | https://entero.ru/ | 3 | Yes (COMP-BZPM-013) |
| Комплекс Трейд | https://kompleks-trade.ru/ | 3 | Strong expansion |

---

## TASK 1 — Candidate Merge Table

Classification of every canonical entity across W2 · W2.5 · W3 · W3R · W3S.

| Company | Website | Merge Status | Current Status | Canonical ID |
| --- | --- | --- | --- | --- |
| Abat (Чувашторгтехника) | https://abat.ru/ | Approved Registry | Approved | COMP-BZPM-001 |
| Restoinox | https://restoinox.ru/ | Approved Registry | Approved | COMP-BZPM-002 |
| Finist (Завод ФИНИСТ) | https://f-inox.ru/ | Approved Registry | Approved | COMP-BZPM-003 |
| Kroner | https://kroner.pro/ | Approved Registry | Approved | COMP-BZPM-004 |
| BSV-inox (БСВ-Компания) | https://bsv.ru/ | Approved Registry | Approved | COMP-BZPM-005 |
| Техно-ТТ | https://www.tehno-tt.ru/ | Approved Registry | Approved | COMP-BZPM-006 |
| УЗНМ | https://zavod-uznm.ru/ | Approved Registry | Approved | COMP-BZPM-007 |
| Стальная Империя | https://stalnaya-imperiya.com/ | Approved Registry | Approved | COMP-BZPM-008 |
| Metal-Food | https://metal-food.ru/ | Approved Registry | Approved | COMP-BZPM-009 |
| Inox-Tech | https://inox-tech.ru/ | Approved Registry | Approved | COMP-BZPM-010 |
| Trapeza (Деловая Русь) | https://www.trapeza.ru/ | Approved Registry | Approved | COMP-BZPM-011 |
| КЛЕН | https://www.klenmarket.ru/ | Approved Registry | Approved | COMP-BZPM-012 |
| Энтеро | https://entero.ru/ | Approved Registry | Approved | COMP-BZPM-013 |
| Фуд Сервис | https://www.food-service.ru/ | Approved Registry | Approved | COMP-BZPM-014 |
| Horeca.ru (PRO-Biznes) | https://horeca.ru/ | Approved Registry | Approved | COMP-BZPM-015 |
| РЕФРО | https://www.refro.ru/ | Approved Registry | Approved | COMP-BZPM-016 |
| Торговый Дизайн | https://t-d.ru/ | Approved Registry | Approved | COMP-BZPM-017 |
| Restoll | https://restoll.ru/ | Approved Registry | Approved | COMP-BZPM-018 |
| Атланта-Сервис | https://atlanta-service.ru/ | Approved Registry | Approved | COMP-BZPM-019 |
| ФудПром | https://novosibirsk.foodprom66.ru/ | Approved Registry | Approved | COMP-BZPM-020 |
| СибХолод | https://sibholod.ru/ | Approved Registry | Approved | COMP-BZPM-021 |
| РестоБУМ | https://restobum.ru/ | Approved Registry | Approved | COMP-BZPM-022 |
| ГастроСтар | https://gastrostar.ru/ | Approved Registry | Approved | COMP-BZPM-023 |
| EverPeak | https://everpeak.kz/ | Approved Registry | Approved | COMP-BZPM-024 |
| БелТоргХолод (BTH) | https://bth.by/ | Approved Registry | Approved | COMP-BZPM-025 |
| Endwest | https://endwest.by/ | Approved Registry | Approved | COMP-BZPM-026 |
| OBORUD.INFO | https://www.oborud.info/ | Approved Registry | Approved | COMP-BZPM-027 |
| OborudUnion | https://www.oborudunion.ru/ | Approved Registry | Approved | COMP-BZPM-028 |
| Pulscen | https://pulscen.ru/ | Approved Registry | Approved | COMP-BZPM-029 |
| ProductCenter | https://productcenter.ru/ | Approved Registry | Approved | COMP-BZPM-030 |
| HF.ru | https://hf.ru/ | Approved Registry | Approved | COMP-BZPM-031 |
| ChefClick | https://www.chefclick.ru/ | Approved Registry | Approved | COMP-BZPM-032 |
| Restomari | https://restomari.ru/ | Approved Registry | Approved | COMP-BZPM-033 |
| Prof-Rest (Рестомания) | https://prof-rest.ru/ | Approved Registry | Approved | COMP-BZPM-034 |
| Ru-Holod | https://ru-holod.ru/ | Approved Registry | Approved | COMP-BZPM-035 |
| RestoShop | https://restoshop.ru/ | Approved Registry | Approved | COMP-BZPM-036 |
| Rational | https://www.rational-online.com/ | Approved Registry | Approved | COMP-BZPM-037 |
| Hoshizaki | https://www.hoshizaki.com/ | Approved Registry | Approved | COMP-BZPM-038 |
| Henny Penny | https://www.hennypenny.com/ | Approved Registry | Approved | COMP-BZPM-039 |
| Electrolux Professional | https://www.electroluxprofessional.com/ | Approved Registry | Approved | COMP-BZPM-040 |
| Hobart | https://www.hobartcorp.com/ | Approved Registry | Approved | COMP-BZPM-041 |
| Advance Tabco | https://advancetabco.com/ | Approved Registry | Approved | COMP-BZPM-042 |
| Eagle Group | https://www.eaglegrp.com/ | Approved Registry | Approved | COMP-BZPM-043 |
| Winterhalter | https://www.winterhalter.com/ | Approved Registry | Approved | COMP-BZPM-044 |
| UNOX | https://www.unox.com/ | Approved Registry | Approved | COMP-BZPM-045 |
| MKN | https://www.mkn.com/ | Approved Registry | Approved | COMP-BZPM-046 |
| Lerius | https://lerius.ru/ | Strong Expansion Candidate | Lerius HQ + barnaul.lerius.ru + delivery cities merged | CAN-EXP-001 |
| Алтай-Посуда (Алтайский центр комплектации) | https://www.altai-posuda.ru/ | Strong Expansion Candidate | Barnaul home-market gap | CAN-EXP-002 |
| Kobor | https://kobor.ru/ | Strong Expansion Candidate | Regional subsites merged | CAN-EXP-003 |
| Комплекс Трейд | https://kompleks-trade.ru/ | Strong Expansion Candidate | City subdomains merged | CAN-EXP-004 |
| ГК Юниторг | https://www.unitorg.ru/ | Strong Expansion Candidate | Chelyabinsk + Tyumen merged | CAN-EXP-005 |
| ТоХоРека | https://www.tohoreca.ru/ | Strong Expansion Candidate | vladivostok.tohoreca.ru merged | CAN-EXP-006 |
| ФудПром (Far East network) | https://vladivostok.foodprom66.ru/ | Strong Expansion Candidate | FE branches; W3 has NSK only | CAN-EXP-007 |
| Bioshop (Компания БИО) | https://bioshop.kz/ | Strong Expansion Candidate | W2.5 deferred uplift | CAN-EXP-008 |
| FoodPro.kz | https://foodpro.kz/ | Strong Expansion Candidate | W2.5 deferred uplift | CAN-EXP-009 |
| ТД Атико | https://td-atiko.kz/ | Strong Expansion Candidate |  | CAN-EXP-010 |
| KarTC | https://kartc.kz/ | Strong Expansion Candidate |  | CAN-EXP-011 |
| Компания ПРОФИ | https://kprofi.by/ | Strong Expansion Candidate |  | CAN-EXP-012 |
| Сервиспищеторг | http://pichetorg.by/ | Strong Expansion Candidate |  | CAN-EXP-013 |
| Практика (Pectopah) | https://www.pectopah.ru/ | Strong Expansion Candidate | W3S 5× visibility | CAN-EXP-014 |
| Завод Проммаш | https://prommash.com/ | Strong Expansion Candidate | W3S 5× visibility | CAN-EXP-015 |
| Ресторан Комплект | https://r-komplekt.ru/ | Strong Expansion Candidate | W3S 4× visibility | CAN-EXP-016 |
| КАМИК | https://kamik-group.ru/ | Strong Expansion Candidate | W3S 4× neutral OEM | CAN-EXP-017 |
| Завод МетаКон | https://zavod-metakon.ru/ | Strong Expansion Candidate | W3S 4× visibility | CAN-EXP-018 |
| НОТИС | https://www.notis.ru/ | Strong Expansion Candidate | W3S 4× NSK | CAN-EXP-019 |
| INOXme | https://inoxme.ru/ | Strong Expansion Candidate | Distinct from InoxMebel | CAN-EXP-020 |
| Torgpit | https://torgpit.ru/ | Strong Expansion Candidate | W3S 3× visibility | CAN-EXP-021 |
| АЛЬФАПРОМ | https://barnaul.alfaprom.org/ | Possible Expansion Candidate | Barnaul hub | CAN-EXP-022 |
| Мебель Фронт | https://barnaul.mebelf.com/ | Possible Expansion Candidate | Local neutral OEM | CAN-EXP-023 |
| Челябторгтехника | https://chtt-trade.ru/ | Possible Expansion Candidate |  | CAN-EXP-024 |
| ATC (Horeca-Tech) | https://horeca-tech.kz/ | Possible Expansion Candidate | W2.5 deferred uplift | CAN-EXP-025 |
| RKS | https://rks.kz/ | Possible Expansion Candidate |  | CAN-EXP-026 |
| ПромПит | https://prompit.by/ | Possible Expansion Candidate |  | CAN-EXP-027 |
| Авитрейд | https://www.avitrade.by/ | Possible Expansion Candidate |  | CAN-EXP-028 |
| Ресторан Сервис | https://restoran-service.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-029 |
| СтройПромСталь (L-Steel) | https://l-steel.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-030 |
| Luxstahl | https://luxstahl.ru/ | Possible Expansion Candidate | W2.5 deferred uplift | CAN-EXP-031 |
| RestoVL (Fresto) | https://www.restovl.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-032 |
| Зенит-ТО | https://zenit-to.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-033 |
| ТД Хлеботехника | https://hleboteh.ru/ | Possible Expansion Candidate | W3S 2× Omsk | CAN-EXP-034 |
| Сиб Агро | https://sibagro24.com/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-035 |
| Акрон | https://krasnoyarsk.akrongroup.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-036 |
| БалтTech | https://balttech.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-037 |
| Ratora Shop | https://ratorarestaurantequipment.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-038 |
| Equipnet | https://www.equipnet.ru/ | Possible Expansion Candidate | W2.5 deferred uplift | CAN-EXP-039 |
| Диалог (Stolovay) | https://www.stolovay.ru/ | Possible Expansion Candidate | W3S 2× | CAN-EXP-040 |
| Whitegoods | https://whitegoods.ru/ | Possible Expansion Candidate | W2.5 deferred uplift | CAN-EXP-041 |
| GastroShop | https://gastroshop.ru/ | Possible Expansion Candidate | W2.5 deferred uplift | CAN-EXP-042 |
| Restobar | https://restobar.ru/ | Possible Expansion Candidate | W2.5 deferred uplift | CAN-EXP-043 |
| VladHoReca / ВладХорека | https://vlad-horeca.ru/ | Deferred | Liquidation signal; operator check | CAN-EXP-044 |
| Trapeza BY | https://trapeza.by/ | Deferred | CIS node of COMP-BZPM-011 | CAN-EXP-045 |
| KLEN BY | https://klenmarket.by/ | Deferred | CIS node of COMP-BZPM-012 | CAN-EXP-046 |
| Спутник-В | https://sputnik-v.kz/ | Deferred | W2.5 deferred; W3R low | CAN-EXP-047 |
| Vermi Gastro Maschinen | https://www.vermi.kz/ | Deferred | W3R low priority | CAN-EXP-048 |
| NERO (Интегра) | https://ner-o.ru/ | Deferred | W2.5 Tier A exclusion | CAN-DEF-001 |
| InoxMebel | https://inoxmebel.ru/ | Deferred | W2.5 Tier A exclusion | CAN-DEF-002 |
| Промтехнологии (ProTechnology) | https://protechnology.ru/ | Deferred | W2.5 redundant OEM | CAN-DEF-003 |
| Gastros | https://gastros.ru/ | Deferred | W2.5 redundant OEM | CAN-DEF-004 |
| ОбщепитСервис | https://serviceobshepit.ru/ | Deferred | W2.5 Tier B exclusion | CAN-DEF-005 |
| РестоПрофи | https://restoprofi.ru/ | Deferred | W2.5 Tier B exclusion | CAN-DEF-006 |
| Restoracia | https://restoracia.ru/ | Deferred | W2.5 Tier B exclusion | CAN-DEF-007 |
| Kupe-Horeca | https://kupe-horeca.ru/ | Deferred | W2.5 Tier C exclusion | CAN-DEF-008 |
| HoReCa.estate | https://horeca.estate/ | Deferred | W2.5 Tier D exclusion | CAN-DEF-009 |
| Allbiz | https://allbiz.ru/ | Deferred | W2.5 Tier D exclusion | CAN-DEF-010 |
| RestoGate | https://restogate.ru/ | Deferred | W2.5 Tier D exclusion | CAN-DEF-011 |
| Vsem-Podryad | https://vsem-podryad.ru/ | Deferred | Procurement focus | CAN-DEF-012 |
| Hore-CA | https://hore-ca.ru/ | Deferred | W2.5 Tier E exclusion | CAN-DEF-013 |
| Optlist | https://optlist.ru/ | Deferred | W2.5 Tier E exclusion | CAN-DEF-014 |
| Supl.biz | https://supl.biz/ | Deferred | W2.5 Tier E exclusion | CAN-DEF-015 |
| B2B-Center | https://www.b2b-center.ru/ | Deferred | Procurement tier | CAN-DEF-016 |
| Middleby Corporation | https://www.middleby.com/ | Deferred | W2.5 Tier F exclusion | CAN-DEF-017 |
| True Manufacturing | https://www.truerefrigeration.com/ | Deferred | Refrigeration focus | CAN-DEF-018 |
| Turbo Air | https://turboairinc.com/ | Deferred | Refrigeration focus | CAN-DEF-019 |
| Ali Group | https://www.aligroup.com/ | Deferred | Holding vs single-brand | CAN-DEF-020 |
| Manitowoc Ice | https://www.manitowocice.com/ | Deferred | Niche ice equipment | CAN-DEF-021 |
| Restoclub | — | Excluded | Restaurant booking | CAN-EXC-001 |
| Profi.ru | — | Excluded | Services marketplace | CAN-EXC-002 |
| Avito / Youla | — | Excluded | General classifieds | CAN-EXC-003 |
| Polair | https://polair.com/ | Excluded | Cold equipment domain | CAN-EXC-004 |
| Sibcar / SITE-001 | — | Excluded | Automotive | CAN-EXC-005 |
| Makita Snab | — | Excluded | Tools | CAN-EXC-006 |
| Bosch / household retail | — | Excluded | Household | CAN-EXC-007 |
| Automotive / АЗС vendors | — | Excluded | Unrelated industry | CAN-EXC-008 |
| Ozon / Wildberries | — | Excluded | Mass retail | CAN-EXC-009 |
| Metabo / DeWalt distributors | — | Excluded | Tools | CAN-EXC-010 |
| Shpigovsky | https://shpigovsky.ru/ | Excluded | Polygon client | CAN-EXC-011 |

---

## TASK 2 — Deduplication Notes

| Entity group | Branch / alias URLs merged | Canonical entry |
|--------------|---------------------------|-----------------|
| **ФудПром** | novosibirsk.foodprom66.ru · vladivostok.foodprom66.ru · habarovsk.foodprom66.ru | COMP-BZPM-020 (NSK) + CAN-EXP-007 (FE network) |
| **Kobor** | kobor.ru · krasnoyarsk.kobor.ru · irkutsk.kobor.ru · habarovsk.kobor.ru | CAN-EXP-003 |
| **Комплекс Трейд** | kompleks-trade.ru · novosibirsk/ekb/chelyabinsk/tyumen/habarovsk.complex-trade.ru | CAN-EXP-004 |
| **Lerius** | lerius.ru · barnaul.lerius.ru · delivery cities (Tomsk, Kemerovo) | CAN-EXP-001 |
| **ChefClick** | chefclick.ru · vladivostok/habarovsk.chefclick.ru | COMP-BZPM-032 (existing registry) |
| **Trapeza CIS** | trapeza.ru · trapeza.by | COMP-BZPM-011 + CAN-EXP-045 (BY node deferred) |
| **KLEN CIS** | klenmarket.ru · klenmarket.by | COMP-BZPM-012 + CAN-EXP-046 (BY node deferred) |
| **ГК Юниторг** | unitorg.ru · Chelyabinsk + Tyumen offices | CAN-EXP-005 |
| **ТоХоРека** | tohoreca.ru · vladivostok.tohoreca.ru | CAN-EXP-006 |

---

## TASK 3 — BZPM Competitor Registry v2

| ID | Name | Website | Tier | Geography | Coverage Zone | Company Type | Source Waves | Current Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COMP-BZPM-001 | Abat (Чувашторгтехника) | https://abat.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W1D; W2; W2.5; W3 | Approved |
| COMP-BZPM-002 | Restoinox | https://restoinox.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3 | Approved |
| COMP-BZPM-003 | Finist (Завод ФИНИСТ) | https://f-inox.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-004 | Kroner | https://kroner.pro/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3 | Approved |
| COMP-BZPM-005 | BSV-inox (БСВ-Компания) | https://bsv.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3 | Approved |
| COMP-BZPM-006 | Техно-ТТ | https://www.tehno-tt.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-007 | УЗНМ | https://zavod-uznm.ru/ | A | Russia (Урал) | Ural; Siberia | OEM Manufacturer | W2; W2.5; W3; W3R | Approved |
| COMP-BZPM-008 | Стальная Империя | https://stalnaya-imperiya.com/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3 | Approved |
| COMP-BZPM-009 | Metal-Food | https://metal-food.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3 | Approved |
| COMP-BZPM-010 | Inox-Tech | https://inox-tech.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3 | Approved |
| COMP-BZPM-011 | Trapeza (Деловая Русь) | https://www.trapeza.ru/ | B | Russia | European Russia; Siberia; Ural; Far East; CIS | Federal Supplier | W1D; W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-012 | КЛЕН | https://www.klenmarket.ru/ | B | Russia | European Russia; Siberia; Ural; Far East; CIS | Federal Supplier | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-013 | Энтеро | https://entero.ru/ | B | Russia | European Russia; Siberia; Ural; Far East; CIS | Distributor | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-014 | Фуд Сервис | https://www.food-service.ru/ | B | Russia | European Russia; Siberia; Ural; Far East; CIS | Distributor | W2; W2.5; W3 | Approved |
| COMP-BZPM-015 | Horeca.ru (PRO-Biznes) | https://horeca.ru/ | B | Russia | European Russia; Siberia; Ural; Far East | Federal Supplier | W2; W2.5; W3 | Approved |
| COMP-BZPM-016 | РЕФРО | https://www.refro.ru/ | B | Russia | European Russia; Siberia; Ural; Far East; CIS | Distributor | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-017 | Торговый Дизайн | https://t-d.ru/ | B | Russia | European Russia; Siberia; Ural; Far East | Federal Supplier | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-018 | Restoll | https://restoll.ru/ | B | Russia | European Russia; Siberia; Ural; Far East; CIS | Federal Supplier | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-019 | Атланта-Сервис | https://atlanta-service.ru/ | C | Russia (Новосибирск) | Siberia | Regional Supplier | W2; W2.5; W3; W3R | Approved |
| COMP-BZPM-020 | ФудПром | https://novosibirsk.foodprom66.ru/ | C | Russia (Новосибирск) | Siberia | Regional Supplier | W2; W2.5; W3; W3R; W3S | Approved |
| COMP-BZPM-021 | СибХолод | https://sibholod.ru/ | C | Russia (Новосибирск) | Siberia | Regional Supplier | W2; W2.5; W3; W3R | Approved |
| COMP-BZPM-022 | РестоБУМ | https://restobum.ru/ | C | Russia (Екатеринбург) | Ural; Siberia | Regional Supplier | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-023 | ГастроСтар | https://gastrostar.ru/ | C | Russia (Нижний Новгород) | European Russia | Regional Supplier | W2; W2.5; W3 | Approved |
| COMP-BZPM-024 | EverPeak | https://everpeak.kz/ | C | Kazakhstan | Kazakhstan; CIS | Regional Supplier | W2; W2.5; W3; W3R | Approved |
| COMP-BZPM-025 | БелТоргХолод (BTH) | https://bth.by/ | C | Belarus | Belarus; CIS | Regional Supplier | W2; W2.5; W3; W3S | Approved |
| COMP-BZPM-026 | Endwest | https://endwest.by/ | C | Belarus | Belarus; CIS | Regional Supplier | W2; W2.5; W3; W3R | Approved |
| COMP-BZPM-027 | OBORUD.INFO | https://www.oborud.info/ | D | Russia / CIS | European Russia; Siberia; Ural; CIS | Industry Directory | W2; W2.5; W3 | Approved |
| COMP-BZPM-028 | OborudUnion | https://www.oborudunion.ru/ | D | Russia | European Russia; Siberia; Ural | Industry Directory | W2; W2.5; W3 | Approved |
| COMP-BZPM-029 | Pulscen | https://pulscen.ru/ | D | Russia | European Russia; Siberia; Ural | Aggregator | W2; W2.5; W3 | Approved |
| COMP-BZPM-030 | ProductCenter | https://productcenter.ru/ | D | Russia | European Russia; Siberia; Ural | Aggregator | W2; W2.5; W3 | Approved |
| COMP-BZPM-031 | HF.ru | https://hf.ru/ | D | Russia | European Russia; Siberia; Ural | Industry Directory | W2; W2.5; W3 | Approved |
| COMP-BZPM-032 | ChefClick | https://www.chefclick.ru/ | E | Russia | European Russia; Siberia; Ural; Far East | Marketplace | W2; W2.5; W3; W3R | Approved |
| COMP-BZPM-033 | Restomari | https://restomari.ru/ | E | Russia | European Russia; Siberia; Ural | Marketplace | W2; W2.5; W3 | Approved |
| COMP-BZPM-034 | Prof-Rest (Рестомания) | https://prof-rest.ru/ | E | Russia | European Russia; Siberia; Ural | Marketplace | W2; W2.5; W3 | Approved |
| COMP-BZPM-035 | Ru-Holod | https://ru-holod.ru/ | E | Russia | European Russia; Siberia; Ural | Marketplace | W2; W2.5; W3 | Approved |
| COMP-BZPM-036 | RestoShop | https://restoshop.ru/ | E | Russia | European Russia; Siberia; Ural | Marketplace | W2; W2.5; W3 | Approved |
| COMP-BZPM-037 | Rational | https://www.rational-online.com/ | F | International (DE) | International | International OEM | W1D; W2; W2.5; W3 | Approved |
| COMP-BZPM-038 | Hoshizaki | https://www.hoshizaki.com/ | F | International (JP) | International | International OEM | W1D; W2; W2.5; W3 | Approved |
| COMP-BZPM-039 | Henny Penny | https://www.hennypenny.com/ | F | International (US) | International | International OEM | W1D; W2; W2.5; W3 | Approved |
| COMP-BZPM-040 | Electrolux Professional | https://www.electroluxprofessional.com/ | F | International | International | International OEM | W1D; W2; W2.5; W3 | Approved |
| COMP-BZPM-041 | Hobart | https://www.hobartcorp.com/ | F | International (US) | International | International OEM | W2; W2.5; W3 | Approved |
| COMP-BZPM-042 | Advance Tabco | https://advancetabco.com/ | F | International (US) | International | International OEM | W2; W2.5; W3 | Approved |
| COMP-BZPM-043 | Eagle Group | https://www.eaglegrp.com/ | F | International (US) | International | International OEM | W2; W2.5; W3 | Approved |
| COMP-BZPM-044 | Winterhalter | https://www.winterhalter.com/ | F | International (DE) | International | International OEM | W2; W2.5; W3 | Approved |
| COMP-BZPM-045 | UNOX | https://www.unox.com/ | F | International (IT) | International | International OEM | W2; W2.5; W3 | Approved |
| COMP-BZPM-046 | MKN | https://www.mkn.com/ | F | International (DE) | International | International OEM | W2; W2.5; W3 | Approved |
| CAN-EXP-001 | Lerius | https://lerius.ru/ | C | Russia (Новосибирск / Сибирь) | Siberia | Regional Supplier | W2; W3R | Strong Expansion Candidate |
| CAN-EXP-002 | Алтай-Посуда (Алтайский центр комплектации) | https://www.altai-posuda.ru/ | C | Russia (Барнаул) | Siberia | Regional Supplier | W3R | Strong Expansion Candidate |
| CAN-EXP-003 | Kobor | https://kobor.ru/ | B/C | Russia (federal + regional subsites) | Siberia; Far East; European Russia | OEM Manufacturer / Regional Supplier | W2; W3R; W3S | Strong Expansion Candidate |
| CAN-EXP-004 | Комплекс Трейд | https://kompleks-trade.ru/ | C | Russia (multi-city) | Siberia; Ural; Far East | Regional Supplier | W2; W2.5; W3R; W3S | Strong Expansion Candidate |
| CAN-EXP-005 | ГК Юниторг | https://www.unitorg.ru/ | C | Russia (Челябинск / Тюмень) | Ural | Regional Supplier | W3R | Strong Expansion Candidate |
| CAN-EXP-006 | ТоХоРека | https://www.tohoreca.ru/ | C | Russia (Дальний Восток) | Far East | Regional Supplier | W3R; W3S | Strong Expansion Candidate |
| CAN-EXP-007 | ФудПром (Far East network) | https://vladivostok.foodprom66.ru/ | C | Russia (Дальний Восток) | Far East | Regional Supplier | W3R | Strong Expansion Candidate |
| CAN-EXP-008 | Bioshop (Компания БИО) | https://bioshop.kz/ | C | Kazakhstan (Алматы) | Kazakhstan; CIS | Regional Supplier | W2; W2.5; W3R | Strong Expansion Candidate |
| CAN-EXP-009 | FoodPro.kz | https://foodpro.kz/ | C | Kazakhstan (Алматы) | Kazakhstan; CIS | Distributor | W2; W2.5; W3R | Strong Expansion Candidate |
| CAN-EXP-010 | ТД Атико | https://td-atiko.kz/ | C | Kazakhstan (Астана) | Kazakhstan; CIS | Regional Supplier | W3R | Strong Expansion Candidate |
| CAN-EXP-011 | KarTC | https://kartc.kz/ | C | Kazakhstan (Караганда) | Kazakhstan; CIS | Regional Supplier | W3R | Strong Expansion Candidate |
| CAN-EXP-012 | Компания ПРОФИ | https://kprofi.by/ | C | Belarus (Минск) | Belarus; CIS | Regional Supplier | W3R | Strong Expansion Candidate |
| CAN-EXP-013 | Сервиспищеторг | http://pichetorg.by/ | C | Belarus (Минск) | Belarus; CIS | OEM Manufacturer / Distributor | W3R | Strong Expansion Candidate |
| CAN-EXP-014 | Практика (Pectopah) | https://www.pectopah.ru/ | B | Russia (federal) | European Russia; Siberia; Ural | Federal Supplier / Marketplace | W2; W2.5; W3S | Strong Expansion Candidate |
| CAN-EXP-015 | Завод Проммаш | https://prommash.com/ | B | Russia (Саратов) | European Russia; Siberia | OEM Manufacturer / Integrator | W3S | Strong Expansion Candidate |
| CAN-EXP-016 | Ресторан Комплект | https://r-komplekt.ru/ | B | Russia | European Russia | Federal Supplier / Integrator | W3S | Strong Expansion Candidate |
| CAN-EXP-017 | КАМИК | https://kamik-group.ru/ | A | Russia (Москва) | European Russia; Siberia; Ural | OEM Manufacturer | W3S | Strong Expansion Candidate |
| CAN-EXP-018 | Завод МетаКон | https://zavod-metakon.ru/ | A | Russia (Москва) | European Russia; Siberia; Ural | OEM Manufacturer | W3S | Strong Expansion Candidate |
| CAN-EXP-019 | НОТИС | https://www.notis.ru/ | C | Russia (Новосибирск / Бердск) | Siberia | Regional Supplier / OEM | W3S | Strong Expansion Candidate |
| CAN-EXP-020 | INOXme | https://inoxme.ru/ | A | Russia | European Russia; Siberia | OEM Manufacturer | W3S | Strong Expansion Candidate |
| CAN-EXP-021 | Torgpit | https://torgpit.ru/ | B | Russia (federal + Омск) | European Russia; Siberia | Federal Supplier | W2; W2.5; W3S | Strong Expansion Candidate |
| CAN-EXP-022 | АЛЬФАПРОМ | https://barnaul.alfaprom.org/ | C | Russia (Барнаул) | Siberia | Distributor | W3R | Possible Expansion Candidate |
| CAN-EXP-023 | Мебель Фронт | https://barnaul.mebelf.com/ | A | Russia (Барнаул) | Siberia | OEM Manufacturer | W3R | Possible Expansion Candidate |
| CAN-EXP-024 | Челябторгтехника | https://chtt-trade.ru/ | C | Russia (Челябинск) | Ural | Regional Supplier | W3R | Possible Expansion Candidate |
| CAN-EXP-025 | ATC (Horeca-Tech) | https://horeca-tech.kz/ | C | Kazakhstan (Алматы) | Kazakhstan; CIS | Regional Supplier | W2; W2.5; W3R | Possible Expansion Candidate |
| CAN-EXP-026 | RKS | https://rks.kz/ | C | Kazakhstan | Kazakhstan; CIS | OEM Manufacturer / Distributor | W3R | Possible Expansion Candidate |
| CAN-EXP-027 | ПромПит | https://prompit.by/ | C | Belarus (Минск) | Belarus; CIS | Distributor | W3R | Possible Expansion Candidate |
| CAN-EXP-028 | Авитрейд | https://www.avitrade.by/ | C | Belarus (Минск) | Belarus; CIS | Distributor | W3R | Possible Expansion Candidate |
| CAN-EXP-029 | Ресторан Сервис | https://restoran-service.ru/ | B | Russia | European Russia | Integrator | W3S | Possible Expansion Candidate |
| CAN-EXP-030 | СтройПромСталь (L-Steel) | https://l-steel.ru/ | A | Russia | European Russia | OEM Manufacturer | W3S | Possible Expansion Candidate |
| CAN-EXP-031 | Luxstahl | https://luxstahl.ru/ | A | Russia | European Russia; Siberia; Ural | OEM Manufacturer | W2; W2.5; W3S | Possible Expansion Candidate |
| CAN-EXP-032 | RestoVL (Fresto) | https://www.restovl.ru/ | C | Russia (Владивосток) | Far East | Regional Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-033 | Зенит-ТО | https://zenit-to.ru/ | C | Russia (Владивосток) | Far East | Regional Supplier / Integrator | W3S | Possible Expansion Candidate |
| CAN-EXP-034 | ТД Хлеботехника | https://hleboteh.ru/ | C | Russia (Омск) | Siberia | Regional Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-035 | Сиб Агро | https://sibagro24.com/ | C | Russia (Красноярск) | Siberia | Regional Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-036 | Акрон | https://krasnoyarsk.akrongroup.ru/ | C | Russia (Красноярск) | Siberia | Regional Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-037 | БалтTech | https://balttech.ru/ | B | Russia (СПб) | European Russia; Siberia | Federal Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-038 | Ratora Shop | https://ratorarestaurantequipment.ru/ | B | Russia (Москва) | European Russia | Federal Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-039 | Equipnet | https://www.equipnet.ru/ | D | Russia | European Russia; Siberia; Ural | Industry Directory | W2; W2.5; W3S | Possible Expansion Candidate |
| CAN-EXP-040 | Диалог (Stolovay) | https://www.stolovay.ru/ | B | Russia (Москва) | European Russia | Federal Supplier | W3S | Possible Expansion Candidate |
| CAN-EXP-041 | Whitegoods | https://whitegoods.ru/ | B | Russia | European Russia; Siberia; Ural | Federal Supplier | W2; W2.5; W3S | Possible Expansion Candidate |
| CAN-EXP-042 | GastroShop | https://gastroshop.ru/ | B | Russia | European Russia | Federal Supplier | W2; W2.5; W3S | Possible Expansion Candidate |
| CAN-EXP-043 | Restobar | https://restobar.ru/ | B | Russia | European Russia | Federal Supplier | W2; W2.5; W3S | Possible Expansion Candidate |
| CAN-EXP-044 | VladHoReca / ВладХорека | https://vlad-horeca.ru/ | C | Russia (Владивосток) | Far East | Regional Supplier | W2; W2.5; W3R; W3S | Deferred |
| CAN-EXP-045 | Trapeza BY | https://trapeza.by/ | B | Belarus (Минск) | Belarus; CIS | Federal Supplier | W3R | Deferred |
| CAN-EXP-046 | KLEN BY | https://klenmarket.by/ | B | Belarus (Минск) | Belarus; CIS | Federal Supplier | W3R | Deferred |
| CAN-EXP-047 | Спутник-В | https://sputnik-v.kz/ | C | Kazakhstan | Kazakhstan; CIS | Regional Supplier | W2; W2.5; W3R | Deferred |
| CAN-EXP-048 | Vermi Gastro Maschinen | https://www.vermi.kz/ | C | Kazakhstan (Алматы) | Kazakhstan | Regional Supplier | W3R | Deferred |
| CAN-DEF-001 | NERO (Интегра) | https://ner-o.ru/ | A | Russia | European Russia | OEM Manufacturer | W2; W2.5 | Deferred |
| CAN-DEF-002 | InoxMebel | https://inoxmebel.ru/ | A | Russia | European Russia | OEM Manufacturer | W2; W2.5 | Deferred |
| CAN-DEF-003 | Промтехнологии (ProTechnology) | https://protechnology.ru/ | A | Russia | European Russia | OEM Manufacturer | W2; W2.5 | Deferred |
| CAN-DEF-004 | Gastros | https://gastros.ru/ | A | Russia | European Russia | OEM Manufacturer | W2; W2.5 | Deferred |
| CAN-DEF-005 | ОбщепитСервис | https://serviceobshepit.ru/ | B | Russia | European Russia; Siberia | Federal Supplier | W2; W2.5 | Deferred |
| CAN-DEF-006 | РестоПрофи | https://restoprofi.ru/ | B | Russia | European Russia | Federal Supplier | W2; W2.5 | Deferred |
| CAN-DEF-007 | Restoracia | https://restoracia.ru/ | B | Russia | European Russia | Federal Supplier | W2; W2.5 | Deferred |
| CAN-DEF-008 | Kupe-Horeca | https://kupe-horeca.ru/ | C | Russia (Краснодар) | European Russia | Regional Supplier | W2; W2.5 | Deferred |
| CAN-DEF-009 | HoReCa.estate | https://horeca.estate/ | D | Russia | European Russia | Industry Directory | W2; W2.5 | Deferred |
| CAN-DEF-010 | Allbiz | https://allbiz.ru/ | D | Russia / CIS | CIS | Aggregator | W2; W2.5 | Deferred |
| CAN-DEF-011 | RestoGate | https://restogate.ru/ | D | Russia | European Russia | Industry Directory | W2; W2.5 | Deferred |
| CAN-DEF-012 | Vsem-Podryad | https://vsem-podryad.ru/ | D | Russia | European Russia | Aggregator | W2; W2.5 | Deferred |
| CAN-DEF-013 | Hore-CA | https://hore-ca.ru/ | E | Russia | European Russia | Marketplace | W2; W2.5 | Deferred |
| CAN-DEF-014 | Optlist | https://optlist.ru/ | E | Russia | European Russia | Marketplace | W2; W2.5 | Deferred |
| CAN-DEF-015 | Supl.biz | https://supl.biz/ | E | Russia / CIS | CIS | Marketplace | W2; W2.5 | Deferred |
| CAN-DEF-016 | B2B-Center | https://www.b2b-center.ru/ | E | Russia | European Russia | Marketplace | W2; W2.5 | Deferred |
| CAN-DEF-017 | Middleby Corporation | https://www.middleby.com/ | F | International (US) | International | International OEM | W2; W2.5 | Deferred |
| CAN-DEF-018 | True Manufacturing | https://www.truerefrigeration.com/ | F | International (US) | International | International OEM | W2; W2.5 | Deferred |
| CAN-DEF-019 | Turbo Air | https://turboairinc.com/ | F | International (US) | International | International OEM | W2; W2.5 | Deferred |
| CAN-DEF-020 | Ali Group | https://www.aligroup.com/ | F | International | International | International OEM | W2; W2.5 | Deferred |
| CAN-DEF-021 | Manitowoc Ice | https://www.manitowocice.com/ | F | International (US) | International | International OEM | W2; W2.5 | Deferred |
| CAN-EXC-001 | Restoclub | — | — | Russia | — | Unrelated | W2 | Excluded |
| CAN-EXC-002 | Profi.ru | — | — | Russia | — | Unrelated | W2 | Excluded |
| CAN-EXC-003 | Avito / Youla | — | — | Russia | — | Classifieds | W2 | Excluded |
| CAN-EXC-004 | Polair | https://polair.com/ | — | International | — | Refrigeration OEM | W2 | Excluded |
| CAN-EXC-005 | Sibcar / SITE-001 | — | — | Russia | — | Unrelated | W2 | Excluded |
| CAN-EXC-006 | Makita Snab | — | — | Russia | — | Unrelated | W2 | Excluded |
| CAN-EXC-007 | Bosch / household retail | — | — | — | — | Unrelated | W2 | Excluded |
| CAN-EXC-008 | Automotive / АЗС vendors | — | — | Russia | — | Unrelated | W2 | Excluded |
| CAN-EXC-009 | Ozon / Wildberries | — | — | Russia | — | Mass retail | W2 | Excluded |
| CAN-EXC-010 | Metabo / DeWalt distributors | — | — | — | — | Unrelated | W2 | Excluded |
| CAN-EXC-011 | Shpigovsky | https://shpigovsky.ru/ | — | Russia | — | Unrelated client | W2 | Excluded |

---

## TASK 5 — Recommended Manual Review Order

Ordering only — no analysis. Operator opens websites in this sequence before W4.

### 1. Tier A OEM (Approved Registry)

| Order | Company | Website | ID |
| --- | --- | --- | --- |
| 1 | Abat | https://abat.ru/ | COMP-BZPM-001 |
| 2 | Restoinox | https://restoinox.ru/ | COMP-BZPM-002 |
| 3 | Finist | https://f-inox.ru/ | COMP-BZPM-003 |
| 4 | Kroner | https://kroner.pro/ | COMP-BZPM-004 |
| 5 | BSV-inox | https://bsv.ru/ | COMP-BZPM-005 |
| 6 | Техно-ТТ | https://www.tehno-tt.ru/ | COMP-BZPM-006 |
| 7 | УЗНМ | https://zavod-uznm.ru/ | COMP-BZPM-007 |
| 8 | Стальная Империя | https://stalnaya-imperiya.com/ | COMP-BZPM-008 |
| 9 | Metal-Food | https://metal-food.ru/ | COMP-BZPM-009 |
| 10 | Inox-Tech | https://inox-tech.ru/ | COMP-BZPM-010 |

### 2. Strategic Regional (Approved + Strong expansion — Barnaul / Siberia / Ural / Far East)

| Order | Company | Website | Status |
| --- | --- | --- | --- |
| 11 | Алтай-Посуда | https://www.altai-posuda.ru/ | Strong expansion — Barnaul |
| 12 | Lerius | https://lerius.ru/ | Strong expansion — Siberia hub |
| 13 | Атланта-Сервис | https://atlanta-service.ru/ | Approved — COMP-BZPM-019 |
| 14 | ФудПром (NSK) | https://novosibirsk.foodprom66.ru/ | Approved — COMP-BZPM-020 |
| 15 | НОТИС | https://www.notis.ru/ | Strong expansion — NSK |
| 16 | Kobor | https://kobor.ru/ | Strong expansion — multi-region |
| 17 | Комплекс Трейд | https://kompleks-trade.ru/ | Strong expansion |
| 18 | РестоБУМ | https://restobum.ru/ | Approved — COMP-BZPM-022 |
| 19 | ГК Юниторг | https://www.unitorg.ru/ | Strong expansion — Ural |
| 20 | ТоХоРека | https://www.tohoreca.ru/ | Strong expansion — Far East |
| 21 | ФудПром FE | https://vladivostok.foodprom66.ru/ | Strong expansion — Far East |

### 3. Federal Leaders (Approved Registry Tier B)

| Order | Company | Website | ID |
| --- | --- | --- | --- |
| 22 | Trapeza | https://www.trapeza.ru/ | COMP-BZPM-011 |
| 23 | КЛЕН | https://www.klenmarket.ru/ | COMP-BZPM-012 |
| 24 | РЕФРО | https://www.refro.ru/ | COMP-BZPM-016 |
| 25 | Restoll | https://restoll.ru/ | COMP-BZPM-018 |
| 26 | Энтерo | https://entero.ru/ | COMP-BZPM-013 |
| 27 | Фуд Сервис | https://www.food-service.ru/ | COMP-BZPM-014 |
| 28 | Horeca.ru | https://horeca.ru/ | COMP-BZPM-015 |
| 29 | Торговый Дизайн | https://t-d.ru/ | COMP-BZPM-017 |

### 4. International References (Approved Registry Tier F — W1D anchors first)

| Order | Company | Website | ID |
| --- | --- | --- | --- |
| 30 | Hoshizaki | https://www.hoshizaki.com/ | COMP-BZPM-038 |
| 31 | Henny Penny | https://www.hennypenny.com/ | COMP-BZPM-039 |
| 32 | Electrolux Professional | https://www.electroluxprofessional.com/ | COMP-BZPM-040 |
| 33 | Rational | https://www.rational-online.com/ | COMP-BZPM-037 |
| 34 | Advance Tabco | https://advancetabco.com/ | COMP-BZPM-042 |
| 35 | Eagle Group | https://www.eaglegrp.com/ | COMP-BZPM-043 |

### 5. Expansion Queue (Strong then Possible — not yet in approved registry)

| Order | Company | Website | Class |
| --- | --- | --- | --- |
| 36 | Практика (Pectopah) | https://www.pectopah.ru/ | Strong |
| 37 | Завод Проммash | https://prommash.com/ | Strong |
| 38 | КАМИК | https://kamik-group.ru/ | Strong |
| 39 | Завод МетаКон | https://zavod-metakon.ru/ | Strong |
| 40 | INOXme | https://inoxme.ru/ | Strong |
| 41 | Torgpit | https://torgpit.ru/ | Strong |
| 42 | Bioshop | https://bioshop.kz/ | Strong — KZ |
| 43 | FoodPro.kz | https://foodpro.kz/ | Strong — KZ |
| 44 | Компания ПРОФИ | https://kprofi.by/ | Strong — BY |
| 45 | Сервиспищеторг | http://pichetorg.by/ | Strong — BY |
| 46 | Luxstahl | https://luxstahl.ru/ | Possible |
| 47 | Whitegoods | https://whitegoods.ru/ | Possible |
| 48 | Equipnet | https://www.equipnet.ru/ | Possible |

---

**Changed files:** `projects/website-factory/execution-cases/bzpm-market-intelligence/BZPM-COMPETITOR-REGISTRY-v2.md`  
**Git:** No changes  

**UNKNOWN:**
- BZPM MI Methodology v1 и W1 Market Mapping Report — не найдены in-repo
- W3R/W3S source reports — session transcripts + `.recovery-temp` extracts, не committed artifacts до W3X
- SERP counts — W3S curated synthesis; Yandex automated parse blocked
- Expansion canonical IDs (CAN-EXP/DEF/EXC) — consolidation placeholders; COMP-BZPM-NNN assigned only after operator approval wave
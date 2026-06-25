# Strategic Segmentation Map — Корво Неро v1

**Stage:** ORCA Stage 1 — interpretive only · **superseded for scope** by full-service correction 2026-06-22  
**Active architecture:** [production/campaign-architecture-v1.md](../production/campaign-architecture-v1.md) — **all directions below IN SCOPE** unless phrase-level reject only

---

## Legend

| Field | Meaning |
|-------|---------|
| **Intent** | Dominant user intent (evidence-informed) |
| **Buyer** | ЮЛ / ИП (B2B services) |
| **Urgency** | low / medium / high |
| **Lead value** | qualitative — not revenue-modeled |
| **Noise** | informational, vacancy, regulatory, web-studio bleed |
| **Demand** | MIG cluster verdict |
| **SERP** | R1 where available; else Stage 2 grade C |
| **Fit** | Corvonero intake + site alignment |
| **Landing** | current Tilda universal page |
| **Budget risk** | spend waste / bleed risk at 100k scale |
| **Status** | strategic status for initial launch |

**Strategic statuses:** primary candidate · secondary candidate · test candidate · narrow specialist · defer · reject for initial launch · needs operator validation

---

## 1. Программист 1С (общие услуги)

| Dimension | Assessment |
|-----------|------------|
| Intent | Direct commercial — hire 1C developer / outsource work |
| Buyer | ЮЛ, ИП |
| Urgency | medium |
| Lead value | high potential but mixed lead quality (vacancy bleed) |
| Noise | **high** — job-seeking, training, salary (R1 r1q01 vacancy_noise_observed) |
| Demand | conditionally_supported |
| SERP | R1 Grade B r1q01 — commercial + franchise + vacancy blocks |
| Fit | Core expertise claimed; site H1 aligned |
| Landing | Broad mention — usable with minor edits for geo + B2B framing |
| Budget risk | **high** on head terms without tight intent filters |
| **Status** | **secondary candidate** (core anchor only with strict future semantic hygiene) |

---

## 2. Сопровождение 1С

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — ongoing support / абонентское сопровождение |
| Buyer | ЮЛ, ИП with existing 1C |
| Urgency | medium |
| Lead value | medium–high (retainer potential) |
| Noise | moderate — SLA/informational comparisons |
| Demand | conditionally_supported |
| SERP | R1 Grade B r1q02 |
| Fit | On site (Поддержка); intake aligned |
| Landing | Service listed — **usable with minor edits** (SLA, configs) |
| Budget risk | moderate — competes with franchise support positioning |
| **Status** | **primary candidate** (Model A core) |

---

## 3. Доработки 1С

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — customization / modification tasks |
| Buyer | ЮЛ, ИП |
| Urgency | medium–high |
| Lead value | **high** — task-based, hourly model fits |
| Noise | low–moderate |
| Demand | **supported** |
| SERP | R1 Grade B r1q03; competitors show price tables |
| Fit | Strong — site lists разработка/доработки |
| Landing | **usable with minor edits** — add task examples, min order |
| Budget risk | low–moderate |
| **Status** | **primary candidate** |

---

## 4. Отчёты и печатные формы

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — specific deliverable (report/form) |
| Buyer | ЮЛ, ИП |
| Urgency | medium |
| Lead value | high — scoped tasks, site shows «от 7500₽» |
| Noise | low |
| Demand | **supported** |
| SERP | R1 Grade B r1q04 |
| Fit | Explicit on site |
| Landing | **usable with minor edits** — hero specificity for narrow traffic weak |
| Budget risk | low |
| **Status** | **primary candidate** |

---

## 5. Интеграции с сайтом

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — 1C ↔ website exchange |
| Buyer | ЮЛ with e-commerce / site |
| Urgency | medium |
| Lead value | high project value |
| Noise | moderate — **web-studio intent** competes in SERP |
| Demand | **supported** |
| SERP | R1 Grade B r1q05 — 1C firms + web studios |
| Fit | Site mentions site integration |
| Landing | Generic integration block — **requires dedicated landing** for paid isolation |
| Budget risk | **high** — wrong clicks to studio shoppers |
| **Status** | **test candidate** (isolate if selected; not default broad mix) |

---

## 6. Интеграции с Битрикс

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — CRM/site + 1C |
| Buyer | ЮЛ using Bitrix |
| Urgency | medium |
| Lead value | high |
| Noise | moderate–high — web-studio SERP |
| Demand | **mixed** |
| SERP | R1 CAPTCHA Grade C r1q06 — **composition unknown** |
| Fit | Intake claims; site generic «интеграция» |
| Landing | **requires dedicated landing** + proof of Bitrix experience |
| Budget risk | high without dedicated page and negatives (future stage) |
| **Status** | **defer** for initial launch unless operator confirms capacity + page |

---

## 7. Интеграции с кассой

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — KKT / cash register + 1C |
| Buyer | Retail / HoReCa ЮЛ, ИП |
| Urgency | medium–high |
| Lead value | medium–high |
| Noise | moderate — overlaps marking specialists |
| Demand | conditionally_supported |
| SERP | Stage 2 grade C only |
| Fit | Site mentions касса; intake aligned |
| Landing | **usable with minor edits** — weak specialization proof |
| Budget risk | moderate |
| **Status** | **secondary candidate** |

---

## 8. Синхронизация и обмен

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — data exchange between bases/systems |
| Buyer | ЮЛ with multi-base or remote store setups |
| Urgency | medium |
| Lead value | medium–high |
| Noise | moderate — technical/informational adjacency |
| Demand | conditionally_supported (ws-p2-004 strong national semantic — not regional volume) |
| SERP | No dedicated R1 query |
| Fit | Intake service; site partial |
| Landing | **usable with minor edits** or narrow section anchor |
| Budget risk | moderate — broad technical queries |
| **Status** | **secondary candidate** |

---

## 9. Маркировка (generic)

| Dimension | Assessment |
|-----------|------------|
| Intent | Mixed commercial + **regulatory/informational** |
| Buyer | ЮЛ in marked goods categories |
| Urgency | medium (compliance-driven) |
| Lead value | medium–high if commercial intent confirmed |
| Noise | **high** — regulatory vocabulary (539 regulatory_noise rows in Pass A layer) |
| Demand | **mixed** |
| SERP | R1 CAPTCHA Grade C r1q07 |
| Fit | Generic mention on site; intake broader |
| Landing | **requires dedicated landing** for paid marking traffic |
| Budget risk | **high** informational bleed |
| **Status** | **test candidate** — do not merge with general 1C without isolation |

---

## 10. Честный знак

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — implementation / setup in 1C |
| Buyer | ЮЛ, ИП in marked categories |
| Urgency | medium–high (compliance) |
| Lead value | medium–high |
| Noise | moderate–high regulatory adjacency |
| Demand | **supported** |
| SERP | R1 Grade B r1q08; AB OnlineKassa local landing pattern |
| Fit | Mentioned on site; specialists compete |
| Landing | **requires dedicated landing** — competitors use narrow commercial pages |
| Budget risk | moderate with dedicated page; high on universal page |
| **Status** | **narrow specialist** / **test candidate** (Model B add-on) |

---

## 11. Продуктовая маркировка

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — category-specific marking (beer, water, etc.) |
| Buyer | ЮЛ in specific niches |
| Urgency | medium |
| Lead value | medium — niche projects |
| Noise | moderate |
| Demand | conditionally_supported |
| SERP | Stage 2 grade C — no R1 per product |
| Fit | **Intake lists 11 categories; site does not prove breadth** |
| Landing | **requires dedicated landing** per category or hub — not proven on site |
| Budget risk | high dispersion if all categories tested |
| **Status** | **defer** (initial launch) except operator-picked 1–2 categories |

---

## 12. Troubleshooting / «1С не работает»

| Dimension | Assessment |
|-----------|------------|
| Intent | Problem-based — urgent fix |
| Buyer | ЮЛ, ИП in distress |
| Urgency | **high** |
| Lead value | medium–high (may convert to support/mod work) |
| Noise | **high** — vacancy on r1q10; «срочно программист 1С» Wordstat no-result |
| Demand | **mixed** |
| SERP | R1 Grade B r1q10 with vacancy_noise_observed |
| Fit | Site mentions audit / «почему не работает» |
| Landing | **usable with minor edits** — urgency CTA; proof weak |
| Budget risk | moderate — wrong intent (job seekers) |
| **Status** | **test candidate** (Model C) — not primary head-term programmer |

---

## 13. РМК (рабочее место кассира)

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — cashier workplace setup / sync |
| Buyer | Retail ЮЛ, ИП |
| Urgency | medium |
| Lead value | medium |
| Noise | moderate — often bound to marking/honest sign phrases |
| Demand | **weak** (seed no-result; alternatives exist in Pass A) |
| SERP | Stage 2 grade C only |
| Fit | Not dedicated on site |
| Landing | **not ready** for narrow RMK traffic |
| Budget risk | moderate — low volume risk at regional level **SAFE UNKNOWN** |
| **Status** | **defer** |

---

## 14. Расчёт себестоимости

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — feature implementation in 1C |
| Buyer | ЮЛ (trade/production) |
| Urgency | low–medium |
| Lead value | medium |
| Noise | moderate informational (how-to) |
| Demand | **needs operator validation** — not isolated in MIG cluster verdicts |
| SERP | Not in R1 priority set |
| Fit | Intake service; site not explicit |
| Landing | **SAFE UNKNOWN** / likely **requires dedicated landing** |
| Budget risk | moderate |
| **Status** | **needs operator validation** |

---

## 15. Закупки и платёжный календарь

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — module setup / customization |
| Buyer | ЮЛ |
| Urgency | low–medium |
| Lead value | medium |
| Noise | moderate informational |
| Demand | **needs operator validation** |
| SERP | Not in R1 priority set |
| Fit | Intake only |
| Landing | **not ready** |
| Budget risk | low–moderate |
| **Status** | **defer** |

---

## 16. Обновление доработанной базы

| Dimension | Assessment |
|-----------|------------|
| Intent | Commercial — update with customizations preserved |
| Buyer | ЮЛ with customized 1C |
| Urgency | medium–high (update pain) |
| Lead value | medium–high |
| Noise | low–moderate |
| Demand | conditionally_supported (site + Wordstat troubleshooting adjacency) |
| SERP | Indirect via troubleshooting cluster |
| Fit | **Explicit on site** («обновление с сохранением доработок») |
| Landing | **usable with minor edits** |
| Budget risk | low |
| **Status** | **secondary candidate** (Model C friendly) |

---

## 17. ТС ПИОТ

| Dimension | Assessment |
|-----------|------------|
| Intent | Mixed — regulatory setup / equipment traceability |
| Buyer | ЮЛ in regulated categories |
| Urgency | medium |
| Lead value | **SAFE UNKNOWN** |
| Noise | **high** informational |
| Demand | **defer** (r1q09 not captured) |
| SERP | **none** at R1 |
| Fit | Intake claims; site not proven |
| Landing | **not ready** |
| Budget risk | high uncertainty + narrow volume |
| **Status** | **reject for initial launch** / **defer** until operator confirms demand and capture |

---

## Summary matrix (full-service architecture — active)

| Architecture role | Directions |
|-------------------|------------|
| **Campaign C01 — general** | programmer, setup, implementation, support, maintenance, one-off, subscription |
| **Campaign C02 — modifications** | all modification + update preservation directions |
| **Campaign C03 — reports/forms** | reports, print forms, external processing, RMK |
| **Campaign C04 — management** | cost, procurement, payment calendar |
| **Campaign C05 — integrations** | website, Bitrix, cash, sync, data transfer |
| **Campaign C06 — marking** | generic marking, Honest Sign, all product categories |
| **Campaign C07 — troubleshooting** | urgent fix, errors, sync failure, recovery |
| **Campaign C08 — specialist** | TS PIOT |

**Previous Stage 1 statuses (primary/defer/reject) are historical.** No service direction removed from full-service architecture. Narrow groups use Tier 3–4 bids.

---

## Historical summary matrix (Stage 1 — superseded for scope)

| Status | Directions |
|--------|------------|
| **primary candidate** | сопровождение, доработки, отчёты/формы |
| **secondary candidate** | программист 1С (filtered), касса, синхронизация, обновление доработанной базы |
| **test candidate** | интеграция сайт, маркировка generic, Честный знак, troubleshooting |
| **narrow specialist** | Честный знак (if isolated) |
| **defer** | Битрикс, продуктовая маркировка, РМК, закупки/календарь, ТС ПИОТ |
| **needs operator validation** | расчёт себестоимости |
| **reject for initial launch** | ТС ПИОТ (evidence gap) |

---

*Interpretive map only. Final architecture requires operator model selection and later ORCA stages.*

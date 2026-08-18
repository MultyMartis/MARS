# CORVONERO — Yandex Direct official source notes v1.1

**Status:** BOUNDED_OFFICIAL_RESEARCH / ARCHITECTURE_REVISION  
**Access date:** 2026-08-19  
**Project:** CorvoNero / Корво Неро  
**Rule:** official Yandex Help / Advertising news / Direct API docs only. Agency blogs and SEO articles are not authority.

This file records a bounded research pass for the RSY architecture revision. Paraphrases only. No long quotes. Claims without an official URL are marked `OPERATOR_INSIGHT / NOT_OFFICIAL_DOC_CONFIRMED`.

Storage twin: `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-REVISION-PACK-2026-08-19\06-CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md`

---

## Research questions — short answers

| # | Question | Official finding | Confidence |
|---|---------|------------------|------------|
| 1 | What are portfolio/package strategies? | Official name in Russian Help: **пакетная стратегия**. Combines several campaigns of the **same type** under one strategy-indicator setup. Conversions in the package train all campaigns in it. Also used when one shared budget must cover several campaigns with different tasks. | HIGH |
| 2 | Which campaign types can be combined? | Help (current): available in **Единая перфоманс-кампания (ЕПК)**, except campaigns with messenger placements and app promotion. Only same-type campaigns. Up to 100 campaigns per package; up to 500 active packages. 2023 news still mentioned text-image / dynamic / smart-banner same-type pairing; current Help is ЕПК-centric. Account confirmation required. | HIGH on ЕПК; MEDIUM on legacy type labels vs this account |
| 3 | Official purpose? | (a) Fix conversion shortage for learning. (b) Work with one budget across several campaigns. (c) Reuse strategy settings. New campaign added to a running package reaches optimization faster. | HIGH |
| 4 | Does Yandex say the package distributes budget by performance? | Yes. Help: budget in a package is distributed between campaigns depending on their effectiveness. News example: three campaigns with a shared weekly budget instead of three equal splits that under-spend. Weak/expensive campaigns get lower bids, not a full stop. | HIGH |
| 5 | Automated strategy learning / conversion volume? | Help: at least **10 conversions per week** for the package **in sum**, not per campaign. Maximize conversions: minimum **10 conversions per week** (70 for app promotion). Evaluate after **7–14 days**. Changing attribution or goal retrains. Troubleshooting: pick a goal that can fire ≥10 times/week; strategy needs **1–2 weeks** to learn. | HIGH |
| 6 | Budget requirements for conversion strategies? | Help: for Maximize conversions, weekly budget should be **not less than 10 × conversion price**. Absolute minimum weekly budget **300 ₽**. Troubleshooting: weekly budget must cover at least 10 conversions of the **most expensive** goal. Insufficient **account balance** / campaign stop due to empty funds **degrades** optimization. Do not change weekly budget more than about once per **2–3 weeks**. | HIGH |
| 7 | Campaign vs group in modern Direct / ЕПК? | Campaign: placements (Search / RSY / Maps), strategy, dates, schedule, shared extras. Group: geo, autotargeting, keywords, interests, audience segments, group scenario, site-content type, URL tags, **group-level CPA/ДРР/CPC adjustments**. Ads: creatives. Official: more groups → more data for strategy learning. | HIGH |
| 8 | Restriction against several related services of one site via groups? | **No official prohibition found.** Help explicitly allows many groups with different targeting in one campaign and uses a category example (sofas / beds / chairs) with different group CPA/ДРР adjustments. Same-domain ads also **do not compete** with each other on billed price. Exact CorvoNero RSY-only ЕПК UI still needs cabinet confirmation. | HIGH that no ban was found; MEDIUM that this account’s UI matches Help |
| 9 | Remaining SAFE UNKNOWN | See §SAFE UNKNOWN below. | — |

---

## Sources used (official)

### S1 — Пакетная стратегия (Help)

- **Title:** Пакетная стратегия
- **URL:** https://yandex.ru/support/direct/ru/strategies/portfolio-strategy
- **Access date:** 2026-08-19
- **Topic:** Package/portfolio strategy definition, eligibility, budget, learning, limits
- **Paraphrase:** A package strategy unites several same-type campaigns under one indicator setup. It solves conversion shortage: conversions from the package train all included campaigns. It is also useful when one budget must serve several campaigns with different tasks; that budget is distributed by effectiveness. Available in ЕПК except messenger and app-promotion campaigns. Types: Maximize clicks / Maximize conversions / Maximize profit. Up to 100 campaigns; up to 500 active packages. Weekly budget in campaign settings must be enough **for all** campaigns. Adding a live campaign changes its strategy; prior learning data for that campaign is kept. Package learning volume: **≥10 conversions/week in sum**. Weak campaigns are bid-down, not fully stopped. Commander: editing strategy on a packaged campaign **unlinks** it and installs a normal strategy with the same settings — weekly budget then applies to that campaign alone.
- **Impact on CorvoNero:** Two RSY campaigns LOCAL/REMOTE may share learning and budget **if** they are the same ЕПК type and the operator binds them to one package. Independent conversion strategies are not required by the split itself.
- **Confidence:** HIGH

### S2 — Объединяйте кампании… Пакетные стратегии (Yandex Advertising news)

- **Title:** Объединяйте кампании, чтобы улучшить их результаты, с помощью Пакетных стратегий
- **URL:** https://yandex.ru/adv/news/paketnie-strategii
- **Access date:** 2026-08-19
- **Date on page:** 23 March 2023
- **Topic:** Launch rationale; shared budget example; 10 conversions/week for the package
- **Paraphrase:** Splitting same-type campaigns can starve each strategy of data. A package pools data from the start. Stable work still wants about 10 conversions/week on chosen goals — **across the package**, not per campaign. Shared weekly budget example: 10 000 ₽ across Search + RSY + mixed retargeting instead of three rigid 3 333 ₽ caps. Before packaging live campaigns, check that the last week already has ≥10 conversions in sum. Creating a package from an existing trained campaign is preferred. 2023 text said Commander/API support would come later; current Help already describes Commander unlink behaviour — treat 2023 UI limits as possibly stale.
- **Impact on CorvoNero:** Officially supports the operator insight that limited balance + many independent budgets can under-deliver. Search+RSY in **one** package is mentioned as a news example; whether that is still best practice for this account is TO_CONFIRM (one later case in the same article preferred Search and RSY in **different** packages).
- **Confidence:** HIGH for purpose; MEDIUM for 2023 type list vs 2026 ЕПК Help

### S3 — Единая перфоманс-кампания (Help)

- **Title:** Единая перфоманс-кампания
- **URL:** https://yandex.ru/support/direct/ru/unified-performance-campaign/about
- **Access date:** 2026-08-19
- **Topic:** ЕПК levels; package support; expert-mode vs Master
- **Paraphrase:** ЕПК is the expert tool for Search, Maps, and RSY in one campaign type. Campaign level: placements, strategy, period, schedule. Group level: audience targeting including geography. Ad level: creatives. Package strategy can unite several ЕПК, including campaigns with different placements or ad types. Expert mode vs Master: expert can choose Search-only or RSY-only, many groups, group-level target-action price adjustment, and packages.
- **Impact on CorvoNero:** Planned RSY campaigns should be treated as **ЕПК with Networks-only placement** unless cabinet shows otherwise. LOCAL vs REMOTE geo can live at **group** level inside one campaign, or as two campaigns later packaged.
- **Confidence:** HIGH

### S4 — Создание ЕПК / группы (Help)

- **Title:** Создание кампании (ЕПК) / Шаг 2. Создание группы. Настройка таргетингов
- **URL:** https://yandex.ru/support/direct/ru/unified-performance-campaign/create-campaign
- **URL:** https://yandex.ru/support/direct/ru/unified-performance-campaign/create-group
- **Access date:** 2026-08-19
- **Topic:** Campaign vs group settings; several groups; CPA adjustments
- **Paraphrase:** Strategy (including package) is chosen at campaign creation. Groups can differ in targeting and ad types. Official: the more groups, the more data for strategy learning. Campaign strategy sets a target CPA/ДРР/CPC; a group may need a higher or lower acquisition cost via **group adjustment**. Example: product categories in one campaign with +50% / −20% group adjustments. Geography is a group setting. Create-campaign also notes call tracking and that call goals can be used as strategy goals.
- **Impact on CorvoNero:** Five related 1C services on one site can legally sit as groups in one RSY campaign. Weak directions can stay included with **lower exposure** via group adjustments / later budget phase, not by deleting them from the map. LOCAL and REMOTE can be two geo-groups or two campaigns.
- **Confidence:** HIGH

### S5 — Выбор стратегии (Help)

- **Title:** Выбор стратегии
- **URL:** https://yandex.ru/support/direct/ru/strategies/select-strategy
- **Access date:** 2026-08-19
- **Topic:** One strategy per campaign; ЕПК strategy list includes package
- **Paraphrase:** A campaign has one strategy for all its ads. ЕПК may use Maximize conversions, Maximize clicks, Maximize clicks with manual bids (Search-only), Maximize profit (beta), or a package strategy.
- **Impact on CorvoNero:** Splitting LOCAL/REMOTE into two campaigns **creates two strategies** unless they share a package. Groups inside one campaign share one strategy.
- **Confidence:** HIGH

### S6 — Максимум конверсий (Help)

- **Title:** Максимум конверсий
- **URL:** https://yandex.ru/support/direct/ru/strategies/average-cpa
- **Access date:** 2026-08-19
- **Topic:** Conversion strategy learning, CPA, Metrica
- **Paraphrase:** Needs a Metrica counter with goals. Changing attribution or goal retrains. Pay-per-conversion or pay-per-click. Deviations from target CPA include: fewer than **10 conversions/week** (70 for apps); first 7–14 days; strategy restart after changes; bid adjustments (example: 200 ₽ CPA + 50% group adj = 300 ₽ for that group); minimum budget. Statistical error is unbounded below 25 conversions or at the 300 ₽ minimum budget.
- **Impact on CorvoNero:** Search currently showed **6 conversions in ~23 days** — below the official 10/week learning guide **even as a whole account Search slice**. Copying Search CPA ≈ 4 517 ₽ into two independent RSY conversion strategies is unsafe. Goal quality (forms vs phone) must be confirmed before conversion optimization.
- **Confidence:** HIGH

### S7 — Недельный бюджет (Help)

- **Title:** Недельный бюджет
- **URL:** https://yandex.ru/support/direct/ru/strategies/week-budget
- **Access date:** 2026-08-19
- **Topic:** Weekly budget mechanics and conversion-strategy sizing
- **Paraphrase:** Strategy holds a calendar-week budget (Mon–Sun). Minimum weekly budget 300 ₽. For Maximize conversions, recommended weekly budget ≥ **10 × conversion price**. Daily spend can reach up to 35% of weekly budget when the schedule has 3+ days. Changing weekly budget restarts spend. Advice: do not change it too often; change near the start of the week. Low spend can mean poor keywords, **insufficient account funds**, low max bid, or too-low CPA.
- **Impact on CorvoNero:** Package weekly budget must cover **all** RSY campaigns in the package. Account balance (operator example 50 000 ₽) can be smaller than the sum of independent campaign demands. Operator must fill real RSY weekly/monthly numbers; this pack does not invent them.
- **Confidence:** HIGH

### S8 — У кампании мало конверсий (Help)

- **Title:** У кампании мало конверсий
- **URL:** https://yandex.ru/support/direct/ru/troubleshooting/conversions
- **Access date:** 2026-08-19
- **Topic:** Learning failures; goals; balance
- **Paraphrase:** Choose a goal that fires at least 10 times/week; learning takes at least 1–2 weeks. If there is no history, start Maximize conversions with **weekly budget only** and one frequent goal. Change weekly budget at most every 2–3 weeks. Weekly budget must buy ≥10 conversions of the costliest goal. **Shared account** must have enough funds; stopping for empty balance hurts algorithms. Check account weekly budget cap. If goals are rare, try pay-per-click first, then switch to pay-per-conversion after volume appears.
- **Impact on CorvoNero:** Phone leads **outside Metrica** (~3, operator approximate) do **not** train Direct unless imported as call/offline goals. Unclear Metrica goals are a launch blocker for conversion strategies.
- **Confidence:** HIGH

### S9 — Неконкуренция объявлений (Help)

- **Title:** Неконкуренция объявлений
- **URL:** https://yandex.ru/support/direct/ru/technologies-and-services/compete
- **Access date:** 2026-08-19
- **Topic:** Same-advertiser competition
- **Paraphrase:** Own ads do not raise billed price against each other if they are in one campaign **or** land on the same domain (including mirrors), even across campaigns/logins.
- **Impact on CorvoNero:** Multiple service groups / two LOCAL-REMOTE campaigns on `lk.corvonero.ru` should not bid-war each other on billed price. This does **not** remove the **budget/learning fragmentation** problem of independent strategies.
- **Confidence:** HIGH

### S10 — Яндекс Метрика в Директе / цели (Help)

- **Title:** Яндекс Метрика / Целевые действия и их ценность
- **URL:** https://yandex.ru/support/direct/ru/statistics/metrika
- **URL:** https://yandex.ru/support/direct/ru/strategies/priority-goals
- **Access date:** 2026-08-19
- **Topic:** Goals required for auto strategies
- **Paraphrase:** Goals in Metrica enable conversion strategies. Strategy settings select site goals (and Business profile goals if Maps/org placements are used).
- **Impact on CorvoNero:** Exact CorvoNero goal names remain SAFE UNKNOWN. Must be confirmed before RSY conversion optimization.
- **Confidence:** HIGH for the mechanism; SAFE UNKNOWN for this account’s goal list

### S11 — Звонки / коллтрекинг (Help)

- **Title:** (create-campaign call-tracking note; efficiency check-list; call conversions)
- **URL:** https://yandex.ru/support/direct/ru/unified-performance-campaign/create-campaign
- **URL:** https://yandex.ru/support/direct/ru/efficiency/check-list
- **URL:** https://yandex.ru/support/direct/ru/strategies/call-conversions
- **Access date:** 2026-08-19
- **Topic:** Calls as optimization signals
- **Paraphrase:** Official path is call tracking into Metrica (or click-to-call as a weaker proxy). Call-type goals can be selected as strategy goals. Approximate operator-counted phone leads that never enter Metrica are **not** an official optimization signal.
- **Impact on CorvoNero:** Keep phone-outside-Metrica as OPERATOR_REPORTED_APPROXIMATE. Do not feed it into CPA targets until tracking is confirmed.
- **Confidence:** HIGH

### S12 — Direct API Strategy object (developer docs)

- **Title:** Пакетная стратегия (Strategy)
- **URL:** https://yandex.ru/dev/direct/doc/ru/objects/strategy
- **Access date:** 2026-08-19
- **Topic:** API confirmation of package purpose
- **Paraphrase:** Same definition as Help: same-type campaigns, shared indicators, conversions train all campaigns in the package. Unlinking requires a new bidding strategy and a suitable budget limit on that campaign.
- **Impact on CorvoNero:** Confirms Help; no extra product rule for CorvoNero structure.
- **Confidence:** HIGH

---

## Operator insight (not official documentation)

**SOURCE_STATUS:** `OPERATOR_INSIGHT / NOT_OFFICIAL_DOC_CONFIRMED`

If account balance is limited (example given: 50 000 ₽) and several independent campaigns each have their own budget/strategy while combined demand exceeds the balance, delivery and learning can degrade. Automated strategies need enough spend and conversion volume. Semantically compatible campaigns on one site with close goals can be packed into package-strategy logic so budget and learning stay coherent.

This is **practice-based operator knowledge**. Official Help **does** independently support: package pooling of conversions; shared budget distributed by effectiveness; 10 conversions/week; weekly budget ≥ 10 × CPA; empty account balance hurting algorithms. Official Help does **not** document the 50 000 ₽ example or CorvoNero Search LOCAL/REMOTE package containers.

---

## SAFE UNKNOWN / cabinet confirmation

| Item | Why unknown |
|------|-------------|
| Does **this** Direct login currently expose пакетные стратегии for RSY-only ЕПК? | Help says ЕПК supports packages; UI/account must confirm. |
| Current live campaign **type** of Search V2.6.2 (legacy text-image vs ЕПК) | No current Commander/Direct snapshot in this task. |
| Can Search LOCAL/REMOTE packages and new RSY campaigns share **one** package? | News 2023 example mixed Search+RSY+retargeting; same article’s REDMOND note preferred separate Search vs RSY packages. Help now: same **type** only. |
| Exact weekly budget, CPA, and replenishment rhythm for RSY | Operator fill fields. |
| Exact Metrica goal names and whether they fire ≥10/week | Not in Search exports. |
| Whether phone calls are imported to Metrica/Direct | Operator approximate only. |
| Whether Commander will be used for RSY and thus risk unlinking packages | Process choice. |
| Combinatorial vs graphic ads requirement for new RSY ЕПК creatives | Help notes TG ads in ЕПК are edit-only since 2026-06-30; creative format is a later generation task. |

---

## What this research does not do

- Does not log into Direct.
- Does not treat agency blogs as authority.
- Does not set a numeric RSY budget or CPA.
- Does not approve import or launch.

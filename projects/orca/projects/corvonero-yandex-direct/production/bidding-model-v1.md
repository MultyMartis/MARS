# Starting Bid Model — Корво Неро v1

**Budget context:** 100 000 ₽/month — controls exposure, not scope  
**Strategy:** Manual CPC (Search) — aligned with Triumph Commander template v1  
**Stage:** 2A — starting rules for Stage 2C XLSX  
**No CPL forecast claimed**

---

## Bid tiers

| Tier | Label | Starting group max bid (₽) | Starting group min bid (₽) | Use |
|------|-------|---------------------------|---------------------------|-----|
| **T1** | Strongest direct commercial | 450–550 | 360–440 | Head commercial: programmer services, mod, reports, Honest Sign, urgent fix |
| **T2** | Specific task/service | 350–450 | 280–360 | Setup, integration, marking setup, errors, config mod |
| **T3** | Test/narrow | 250–350 | 200–280 | RMK, management tasks, product marking categories, TS PIOT |
| **T4** | High-noise controlled test | 180–250 | 150–200 | Regulatory-adjacent marking queries, very narrow categories |

**Rule:** Never use 0 ₽ bids (Triumph BID-MANAGEMENT-RULES-v1).

---

## Within-group spread

| Parameter | Value |
|-----------|-------|
| Primary phrase | Tier max bid |
| Secondary phrases | Step down 15–25 ₽ per priority rank |
| Max spread inside group | 10–90 ₽ (Triumph reproducible rule) |
| Flat bidding | **Prohibited** |

Formula:
```text
phrase_bid = group_max_bid - (priority_rank - 1) * step
group_min_bid >= group_max_bid - 90
```

---

## Tier assignment by group (summary)

| Campaign | Tier 1 groups | Tier 2 | Tier 3 | Tier 4 |
|----------|---------------|--------|--------|--------|
| C01 | G01-01, G01-02, G01-05 | G01-03,04,06,07,08 | — | — |
| C02 | G02-01 | G02-02–06 | — | — |
| C03 | G03-01,03,04 | G03-02,05 | G03-06 | — |
| C04 | — | — | G04-01–03 | — |
| C05 | G05-01 | G05-02–05 | G05-06 | — |
| C06 | G06-03 | G06-01,02,04 | G06-05–08,10 | G06-09,11–13 |
| C07 | G07-01 | G07-02–04 | — | — |
| C08 | — | — | G08-01,02 | — |

---

## Budget boundary via bids (100k/month)

| Control | Mechanism |
|---------|-----------|
| Total exposure | Sum of (phrase_bid × expected_clicks) — **not modeled**; human daily caps in Commander |
| High-noise lanes | Tier 4 + strict negatives — limited groups |
| Narrow categories | Tier 3–4 starting bids; raise only on conversion evidence |
| Head terms | Tier 1 max 550 ₽ cap at launch |
| Campaign priority | C01+C02+C03 receive higher daily budget share (~52%); C06 test ~18%; C08 ~2% |

---

## Competition class (qualitative)

| Class | Groups | Bid posture |
|-------|--------|-------------|
| High (franchise SERP) | G01-01, G01-05, G02-01 | T1 upper range |
| Medium | Integrations, marking setup | T2 |
| Noisy | G01-01 head programmer, G07-01 urgent | T1 with heavy negatives |
| Narrow/unknown volume | RMK, TS PIOT, product Tier 4 | T3–T4 |

---

## Post-import (human)

1. Apply bids in Commander column «Ставка» per phrase row.  
2. Set campaign daily budgets totaling ~100 000 ₽/month.  
3. Review search query report after 7 days — adjust tiers, not architecture.  
4. Do not delete groups for budget — lower tier or pause group.

---

## XLSX field

| Commander column | Value |
|------------------|-------|
| «Ставка» | Phrase-level bid per tier rules (col 54 per header map) |

*Triumph reference: [BID-MANAGEMENT-RULES-v1.md](../../../freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md)*

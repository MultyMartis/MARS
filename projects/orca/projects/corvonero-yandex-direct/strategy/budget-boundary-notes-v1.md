# Budget Boundary Notes — Корво Неро v1

**Budget:** 100 000 ₽/month — **bid and priority control** — **not** service scope filter  
**Operator correction (2026-06-22):** Budget does **not** authorize removing operator service directions from architecture  
**Active bidding:** [production/bidding-model-v1.md](../production/bidding-model-v1.md)

---

## Reasonable simultaneous strategic directions

At 100 000 ₽/month with **no historical CPC/CPL** and **one universal landing**, ORCA interprets:

| Simultaneous directions | Assessment |
|-------------------------|------------|
| **2–3** related B2B service intents (Model A) | **Reasonable** for learning |
| **3 core + 1 specialist** (Model B) | **Upper bound** — requires isolation discipline |
| **4+ unrelated families** (e.g. core + marking + integration + urgent) | **Unreasonable** — dispersion risk dominates learning |
| **17 directions** | **In architecture** — 8 campaigns / 48 groups; exposure controlled by bid tiers T1–T4, not deletion |

---

## Segments that must not be mixed (strategic level)

| Segment A | Segment B | Why |
|-----------|-----------|-----|
| General 1C / support / mod | Marking / Честный знак | Different intent, proof, and landing; informational noise in marking |
| 1C services | Website / Bitrix integration | Web-studio shopper intent; wrong landing narrative |
| B2B outsource | Employment / vacancy queries | Registry noise: job-seeking, salary |
| Commercial services | Training / courses | Wordstat + SERP course ads on head terms |
| Scoped tasks (reports) | Broad «programmist» head | Budget bleed + vacancy noise |
| Troubleshooting urgent | Generic support retainer | Different ad promise and qualification |

*Future campaign structure must enforce separation — not designed in Stage 1.*

---

## High informational traffic risk

| Area | Evidence |
|------|----------|
| Marking (generic) | 539 regulatory_noise rows Pass A; r1q07 CAPTCHA |
| Честный знак | Regulatory adjacency in Wordstat |
| ТС ПИОТ | Informational dominance in demand_surface cluster |
| Broad programmer | Training + employment noise |
| Product marking | Category how-to / regulatory mix |

**Strategic stance:** exclude or isolate at architecture stage; not primary on universal page without dedicated funnel.

---

## Narrow directions — volume sufficiency

| Direction | Regional volume | ORCA note |
|-----------|-------------------|-----------|
| РМК | **SAFE UNKNOWN**; seed no-result | Likely insufficient alone for dedicated test |
| ТС ПИОТ | **SAFE UNKNOWN**; no R1 | Defer — cannot confirm commercial SERP |
| Product marking (each SKU class) | **SAFE UNKNOWN** | Too narrow to test many at once |
| Bitrix integration | **SAFE UNKNOWN** composition | Defer without R1 evidence |

---

## Future isolated test limits (conceptual)

If operator expands after initial learning:

| Lane | Suggested pattern |
|------|-------------------|
| Честный знак | Separate test with dedicated landing + own future budget floor |
| Troubleshooting | Separate test; monitor vacancy waste |
| Website integration | Separate test only with integration landing + studio negatives (future) |
| Remote geo outside NSO | Separate charter — intake allows remote; geo targeting decision pending |

---

## Budget vs proof interaction

100k does **not** compensate for weak proof on high-trust queries (marking, urgent fix). Proof gaps increase effective cost of learning — **qualitative** only; no CPL modeled.

---

*Stage 1 boundary interpretation only.*

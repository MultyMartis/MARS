# Full-Service Campaign Charter — Корво Неро v1

**Operating model:** FULL-SERVICE CLUSTERED SEARCH CAMPAIGN  
**Project:** PRJ-0013 / `corvonero-yandex-direct`  
**Date:** 2026-06-22

---

## Charter

Корво Неро запускает **полную поисковую рекламную кампанию** по всем услугам, переданным оператором на старте проекта. Каждая услуга разбивается на столько смысловых рекламных групп, сколько требует фактическая семантика Wordstat/MIG. Бюджет 100 000 ₽/month управляет ставками и приоритетами, но **не удаляет** направления услуг из архитектуры.

---

## Principles

1. **Full operator scope** — все направления услуг включены в кластеризацию и архитектуру.
2. **Semantic purity** — одна группа = один смысл = одно объявление (минимум).
3. **Multi-campaign separation** — marking, integrations, troubleshooting не смешиваются с general 1C.
4. **Evidence-bound keywords** — только фразы из MIG Keyword Registry и operator seeds; без выдуманных услуг.
5. **Budget via bids** — Tier 1–4 starting bids; narrow groups at Tier 3–4; no group deletion for budget.
6. **Landing after XLSX** — тексты посадочных страниц после валидации импортного файла.
7. **Roman builds on Tilda** — URL-план готов; страницы **PLANNED — NOT YET PUBLISHED**.

---

## Commercial facts (confirmed — use in ads/landings)

| Fact | Value |
|------|-------|
| Brand | Центр автоматизации «Корво Неро» |
| Geo | Новосибирск; удалённая работа; выезд — Новосибирск |
| Audience | ЮЛ, ИП |
| Rate | 3 000 ₽/час |
| Minimum | 2 часа / от 6 000 ₽ |
| Payment | договор; безналичная оплата |
| Configurations | 1С:УТ · УНФ · Розница · КА · Бухгалтерия предприятия |
| VAT | **SAFE UNKNOWN** — do not claim |

---

## Prohibited claims (unless verified later)

Partner status · 24/7 · guaranteed deadlines · free work · certifications · case results · team size · years of experience beyond evidence

---

## Production deliverables (this project)

| Deliverable | Stage | Path |
|-------------|-------|------|
| Campaign architecture | 2A ✓ | [production/campaign-architecture-v1.md](../production/campaign-architecture-v1.md) |
| Ad group registry | 2A ✓ | [production/ad-group-registry-v1.json](../production/ad-group-registry-v1.json) |
| Negative architecture | 2A ✓ | [production/negative-keyword-architecture-v1.md](../production/negative-keyword-architecture-v1.md) |
| Bidding model | 2A ✓ | [production/bidding-model-v1.md](../production/bidding-model-v1.md) |
| URL/landing map | 2A ✓ | [production/url-landing-map-v1.md](../production/url-landing-map-v1.md) |
| Commander format contract | 2A ✓ | [production/direct-commander-format-contract-v1.md](../production/direct-commander-format-contract-v1.md) |
| Ads + full keywords | 2B | pending |
| Commander XLSX | 2C | pending |
| Landing `.md` + `.docx` | 3 | pending |

---

## Status

| Gate | State |
|------|-------|
| MIG | **COMPLETE** |
| ORCA Stage 1 recommendation | **SUPERSEDED BY OPERATOR** |
| ORCA Stage 2A | **COMPLETE** |
| Launch | **NOT AUTHORIZED** |

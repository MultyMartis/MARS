# Bid QA v1.3

**Date:** 2026-05-29  
**Gate:** Pre-Commander import  
**Rules:** [BID-MANAGEMENT-RULES-v1.md](../ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md)

---

## Automated QA result

| Check | Result |
|-------|--------|
| All keyword rows have bid (col 54) | **PASS** |
| Numeric, > 0 | **PASS** |
| Range 400–600 ₽ | **PASS** |
| No flat bidding per group (2+ phrases) | **PASS** |
| Spread 10–90 ₽ per group | **PASS** |
| Zero bids | **PASS** (0) |

Validator: `tools/exporter-cli/_validate-launch-ready-v1.3.js`

---

## Assignment logic (deterministic)

Module: `tools/exporter-cli/bid-assignment-v1.3.js`

- Sort: `is_primary` first, then JSON order  
- `group_max` = 600 ₽, step sized so spread ∈ [10, 90]  
- Primary phrase → highest bid in group  
- Single-phrase groups → 580 ₽ anchor

---

## Per-group summary

| Group | Route | Phrases | Bid min–max (₽) | Spread (₽) |
|-------|-------|---------|-----------------|--------------|
| 01 — 5 тонн | 5-tonn | 6 | 510–600 | 90 |
| 02 — Бытовки | bytovki | 5 | 512–600 | 88 |
| 03 — Стройматериалы | stroymaterialy | 5 | 512–600 | 88 |
| 04 — Юрлица | yurlic | 4 | 510–600 | 90 |
| 05 — 6×6 | vezdehod | 5 | 512–600 | 88 |
| 06 — Оборудование | oborudovanie | 5 | 512–600 | 88 |
| 07 — Контейнеры | konteynery | 5 | 512–600 | 88 |
| 08 — Арматура | armatura | 5 | 512–600 | 88 |
| 09 — Кирпич/блоки | kirpich-bloki | 5 | 512–600 | 88 |
| 10 — ФБС/ЖБИ | fbs-zhbi | 6 | 510–600 | 90 |
| 11 — Край | kray | 6 | 510–600 | 90 |
| 12 — Заказ | zakaz | 7 | 510–600 | 90 |

---

## Human spot-check (required)

- [ ] Commander shows **ручные** ставки на поиске, not autobid  
- [ ] Primary phrase in each group has top bid  
- [ ] No campaign-level bid override conflicting with phrase bids  

---

## SAFE UNKNOWN

Live auction CPC vs static 400–600 band — operator may recalibrate post–search terms report (human-only).

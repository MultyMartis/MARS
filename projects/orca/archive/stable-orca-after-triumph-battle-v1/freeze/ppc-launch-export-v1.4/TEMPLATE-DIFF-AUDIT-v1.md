# Template Diff Audit v1

**Date:** 2026-05-29  
**Lane:** ORCA Triumph Commander Launch XLSX v1.4  
**Template SoT:** `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx`  
**Baseline export:** `triumph-sheet1-patch-launch-ready-v1.3.xlsx`  
**Fixed export:** `triumph-sheet1-patch-launch-ready-v1.4.xlsx`  
**Tool:** `tools/exporter-cli/_template-diff-audit.js`

---

## Method

Reverse-engineering via ExcelJS (metadata rows 1–15, headers row 14) and XML cell diff on sheet **Тексты**. Compared template v1 vs export v1.3 (pre-fix) and v1.4 (post-fix).

---

## Campaign metadata block (rows 6–13)

| Row | Col | Label / field | Template v1 value | Export v1.3 | Export v1.4 | Status v1.4 |
|-----|-----|---------------|-------------------|-------------|-------------|-------------|
| 7 | 5 | Тип кампании | Единая перфоманс-кампания | same | same | **MATCH** |
| 7 | 8 | Места показа | search | same | same | **MATCH** |
| 8 | 8 | Валюта | RUB | same | same | **MATCH** |
| 9 | 5 | Минус-фразы на кампанию | -вакансии -работа … | same | same | **MATCH** |
| 10 | 5 | Оптимизировать текст… | 0 | same | same | **MATCH** |
| 11 | 5 | Объект продвижения | https://manipulator-triumph.ru/ | **5-tonn.html URL** | root URL | **FIXED v1.4** |
| 12–13 | — | Яндекс Бизнес / телефон | empty | same | same | **MATCH** |

**Finding (v1.3):** Exporter patched `campaigns.promotion_url` from first group landing (`5-tonn.html`) instead of template root promotion object. Commander may ignore or mis-apply campaign settings when promotion URL diverges from calibrated template.

**Finding (v1.4):** All metadata cells cols 1–12 match template — **zero metadata diffs**.

---

## Fields NOT present in template XLSX

| Setting | In template? | Notes |
|---------|--------------|-------|
| Стратегия (manual CPC label) | **No dedicated column** | Implied by col 53 «Автоставка» = `-` on data rows = manual bids |
| Недельный / дневной бюджет | **Not in metadata block** | Set in Commander UI post-import — **SAFE UNKNOWN** for XLSX transport |
| Автотаргетинг | **No dedicated column** | Autotarget markers suppressed in exporter (`---autotargeting` never exported) |
| Режим показов | Row 7 col 8 = `search` | Patched explicitly in v1.4 |

---

## Data table header map (row 14 — verified)

| Col | Header | Role |
|-----|--------|------|
| 1 | Доп. объявление группы | Second+ ad marker (`+`) |
| 2 | Тип объявления | Search: «Текстово-графическое» |
| 5 | Название группы | Group name |
| 6 | Номер группы | Distinct 1–12 |
| 8 | Фраза (с минус-словами) | Keyword row |
| 48 | Ссылка | Landing URL |
| 52 | Регион | Краснодарский край |
| 53 | Автоставка | `-` = manual (template SoT) |
| 54 | Ставка | Manual CPC on keyword rows |
| 68 | Минус-фразы на группу | Group cross-negatives |

---

## Row model diff (intentional — not a v1.4 regression)

| Model | Template v1 | Export v1.3/v1.4 |
|-------|-------------|------------------|
| Transport | Combined ad+phrase rows (84 ad-like rows) | Transport split v1.2 (20 ad + 64 keyword = 84 rows) |
| Bids on ad rows | Present in template sample | On keyword rows only (by design) |
| Col 1 first ad | `-` (template mask) | empty (transport split convention) |

**Scope lock:** Ads, phrases, URLs, bids, group structure unchanged from JSON — only settings/syntax fidelity fixed.

---

## Group negatives diff (v1.3 → v1.4)

| Aspect | v1.3 | v1.4 |
|--------|------|------|
| Wildcard tokens (`бытовк*`, …) | 12/12 groups | **0** |
| Commander syntax | **FAIL** (asterisk rejected) | **PASS** |
| Template minimal negatives | Only 2 groups had negatives in template sample | All 12 groups have expanded doctrine + cross-route negatives |

Template sample negatives (phrase-level, no `*`): `-перевозка бытовок`, `-перевозка контейнеров`. v1.4 uses these phrase forms plus stem expansions (`бытовка`, `бытовки`, …).

---

## SAFE UNKNOWN

- Whether Commander reads budget/strategy from a sheet outside **Тексты** for this account type  
- Optimal negative breadth vs template minimal sample — operator validates post-import

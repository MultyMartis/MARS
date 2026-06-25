# Direct Commander Format Contract — Корво Неро v1

**Target:** Yandex Direct · Search · Text-and-image ads · XLSX import via Direct Commander  
**Reference SoT:** Triumph `triumph-manipulator-commander-template-v1.xlsx` (production-validated 2026-05-29)  
**Corvonero status:** Contract defined — **no import-ready XLSX in Stage 2A**

---

## Template asset (verified on disk)

| Field | Value |
|-------|-------|
| File | `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` |
| Size | 439 514 bytes |
| Verified | 2026-06-22 — `Test-Path` True |
| Supersedes | `triumph-manipulator-commander-template-v0.xlsx` (reference only) |
| Freeze doc | [COMMANDER-TEMPLATE-SOT-v1.md](../../../freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md) |

**Corvonero production:** Patch same template shape OR fork `corvonero-commander-template-v1.xlsx` from v1 after column verification — Stage 2C.

---

## Worksheets (from template-sheet-index-v0.json)

| Sheet | Role |
|-------|------|
| **Тексты** | Primary import — campaigns, groups, keywords, ads, extensions |
| **Регионы** | Geo reference tree (17 461 rows) — lookup only |
| **Словарь значений полей** | Enum reference — campaign types, ad types |

---

## Sheet «Тексты» — regions

| Region | Rows | Content |
|--------|------|---------|
| Campaign metadata block | 6–13 | Key-value pairs above data table |
| Header row | 14 | Column headers (78 columns) |
| Data rows | 15+ | Group/ad/keyword rows |

### Campaign metadata block (verified headers)

| Header (exact Russian) | Logical field | Required |
|------------------------|---------------|----------|
| Тип кампании: | campaign_type | Yes |
| Места показа: | placement | Yes — Search only |
| Минус-фразы на кампанию: | campaign_negatives | Yes |
| Объект продвижения: | promotion_url | Yes |
| Организация из Яндекс Бизнеса: | yandex_business_org | Manual/post-import |
| Номер телефона: | phone | Manual/post-import |

**Campaign type literal:** «Текстово-графическая кампания» or «Единая перфоманс-кампания» per account — verify at import (dictionary sheet).

---

## Data table — mandatory columns (verified from commander-header-map-v0.json)

| Col | Header (exact) | Entity | Export |
|-----|----------------|--------|--------|
| 1 | Доп. объявление группы | ad | «+» on 2nd+ ad in group |
| 2 | Тип объявления | ad | «Текстово-графическое» |
| 4 | ID группы | group | Stable ORCA group id / Commander id |
| 5 | Название группы | group | Verbatim |
| 6 | Номер группы | group | Distinct per group — **required** |
| 7 | ID фразы | keyword | Traceability |
| 8 | Фраза (с минус-словами) | keyword | Phrase + inline negatives |
| 9 | ID объявления | ad | Traceability |
| 10 | Заголовок 1 | ad | Max 56 chars |
| 11 | Заголовок 2 | ad | Max 30 chars |
| 12 | Текст | ad | Max 81 chars |
| 48 | Ссылка | ad | Final URL + UTM |
| 49 | Отображаемая ссылка | ad | Display path |
| 52 | Регион | geo | «Новосибирск» / «Новосибирская область» |
| 54 | Ставка | keyword | Manual CPC ₽ — **must not be 0** |
| 56 | Статус объявления | ad | draft/active |
| 57 | Статус фразы | keyword | active |
| 58 | Заголовки быстрых ссылок | sitelinks | Combined cell |
| 59 | Описания быстрых ссылок | sitelinks | Combined cell |
| 60 | Адреса быстрых ссылок | sitelinks | Combined cell |
| 67 | Уточнения | callouts | Combined cell |
| 68 | Минус-фразы на группу | group_negatives | Cross-negative matrix |

---

## Unsupported / manual fields

| Field | Status |
|-------|--------|
| Match type (dedicated column) | **unsupported** — encode in phrase text |
| Campaign name (data table column) | **unsupported** — metadata / implicit |
| UTM (dedicated column) | **unsupported** — append to «Ссылка» |
| Image binary | Col 64 «Изображение» — cleared for search export; upload manual if required |
| Creative / moderation cols 65–66 | Cleared in Triumph search-only export |
| Daily budget | Manual in Commander post-import |
| Autobidding | Out of scope — manual bids only |

---

## Row generation rules (Triumph v1.2)

1. One row per keyword phrase; ad fields repeat on keyword rows.  
2. First row in group carries full ad + extensions.  
3. «Доп. объявление группы» = «+» for second ad variant.  
4. «Номер группы» unique per ORCA group.  
5. Validation **before** export — not after.  
6. Post-export QA: `validate:no-duplicate-ads-v1.2` pattern (adapt for Corvonero CLI).

---

## Corvonero production binding (Stage 2C)

| Step | Tool/path |
|------|-----------|
| SoT JSON | `production/ad-group-registry-v1.json` + ads payload |
| Template base | Triumph v1 xlsx (fork to corvonero path) |
| Exporter pattern | Triumph `sheet1-patch-export.js` — adapt, do not reinvent columns |
| Validation | Hygiene audit + no-duplicate-ads + launch-ready checklist |

---

## SAFE UNKNOWN

- Exact Commander UI column order if Yandex updated since 2026-05-29 — diff template before Stage 2C.  
- Account-specific Unified Performance Campaign field requirements — human check on first import.  
- Combined sitelink/callout cell encoding — copy Triumph writer logic.

**No fake import-ready claim for Stage 2A.**

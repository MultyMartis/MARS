# CORVONERO COMMANDER CT-6 CA-01 — Forensic Comparison v1

**Audited file:** `CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v5.xlsx`  
**Binding version:** v5  
**SHA-256:** `80e62d262b33e154c86a6a2642c84d4c8a37c263f7464ac9fffc13e082702210`  
**Verdict:** PASS — AUTHORITY WORKBOOK MATCHES OPERATOR IMPORT

---

## Structure counts

| Metric | Authority | Operator import |
|--------|-----------|-----------------|
| Campaigns | 1 | 1 |
| Groups | 7 | 7 |
| Keyword rows | 339 | 339 |
| Ad rows | 7 | 7 |
| Groups over 200 | 0 | — |
| Max group phrases | 144 | — |
| Unparsed rows | — | 0 |

---

## Callouts (col 67 — «Уточнения»)

| Item | Value |
|------|-------|
| Status | valid |
| Delimiter | `||` (Commander-correct) |
| Ad rows checked | 7 |

Individual callouts (authority-approved):

| Callout | Chars |
|---------|-------|
| Удалённо по России | 18 |
| Выезд в Новосибирске | 20 |
| Работа по договору | 18 |
| Минимальный заказ 2 часа | 24 |

v2 `;;` delimiter defect: **resolved** (CT-5R1)

---

## URLs (col 48)

| Item | Value |
|------|-------|
| Status | clean, no UTM |
| Affected ads | 7 |
| Clean landing URL | `https://lk.corvonero.ru/programmist-1s/` |

v2 UTM injection defect: **resolved** (CT-5R1)

---

## Region and organization

| Field | Value | Status |
|-------|-------|--------|
| Region | Новосибирская область | PASS |
| Organization | blank | PASS |

---

## Bid policy

| Item | Value |
|------|-------|
| Policy | `CORVONERO_BALANCED_CYCLIC_10_RUB_V1` |
| Distinct bids | 10 |
| Range | 410–500 RUB |
| Flat at base | NO |

---

## Group negatives / campaign negatives

OPERATOR CONFIRMED GENERALLY — DETAILED FIELD-BY-FIELD INSPECTION NOT RECORDED

---

## Server safety

| Action | Status |
|--------|--------|
| Server upload | NOT PERFORMED |
| Synchronization | NOT PERFORMED |
| Launch | NOT PERFORMED |

Machine-readable: `CORVONERO-COMMANDER-CT6-CA01-FORENSIC-COMPARISON-v1.json`

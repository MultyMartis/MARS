# Campaign Architecture — Корво Неро v1

**Stage:** ORCA 2A — full-service search architecture  
**Operating model:** FULL-SERVICE CLUSTERED SEARCH CAMPAIGN  
**Geo:** Новосибирск + Новосибирская область  
**Placement:** Search only — no RSYA / networks  
**Groups total:** 48 across 8 campaigns

---

## Hierarchy

```text
Campaign (8)
  → Service direction
    → Semantic cluster
      → Ad group (48)
        → Keywords (15–25 each at production)
          → Ad (≥1 text-and-image per group)
            → Landing URL (31 unique pages)
```

---

## Campaign catalog

### CORV-C01 — Общие услуги 1С

| Field | Value |
|-------|-------|
| **Purpose** | Broad B2B 1C outsource: programmer, setup, implementation, support, maintenance |
| **Groups** | CORV-G01-01 … G01-08 (8 groups) |
| **Excluded meanings** | Vacancy, training, marking, integration studio, troubleshooting urgent |
| **Geo** | Новосибирск + НСО |
| **Search boundary** | Search only |
| **Schedule** | Mon–Fri 08:00–20:00 NSO (recommended; confirm at launch) |
| **Bid strategy** | Manual CPC — Tier 1–2 primary |
| **Budget role** | ~25% monthly exposure cap via bid tiers |
| **Campaign negatives** | Global employment/training/download negatives |
| **UTM** | `utm_campaign=corv_general_1c` |
| **Landing family** | LP-01 … LP-04 |

### CORV-C02 — Доработки 1С

| Field | Value |
|-------|-------|
| **Purpose** | Customization, config mods, update preservation |
| **Groups** | CORV-G02-01 … G02-06 (6) |
| **Excluded** | General support retainer, marking, reports-only |
| **Bid strategy** | Manual CPC — Tier 1–2 |
| **Budget role** | ~15% |
| **UTM** | `corv_modifications` |
| **Landing family** | LP-05, LP-06 |

### CORV-C03 — Отчёты и печатные формы

| Field | Value |
|-------|-------|
| **Purpose** | Reports, print forms, external processing, RMK |
| **Groups** | CORV-G03-01 … G03-06 (6) |
| **Excluded** | General mod without report/form intent |
| **Bid strategy** | Tier 1–3 |
| **Budget role** | ~12% |
| **UTM** | `corv_reports_forms` |
| **Landing family** | LP-07 … LP-09 |

### CORV-C04 — Управленческие задачи

| Field | Value |
|-------|-------|
| **Purpose** | Cost calculation, procurement planning, payment calendar |
| **Groups** | CORV-G04-01 … G04-03 (3) |
| **Excluded** | Generic setup, marking |
| **Bid strategy** | Tier 2–3 (evidence partial — operator intake + Wordstat adjacency) |
| **Budget role** | ~5% test exposure |
| **UTM** | `corv_management` |
| **Landing family** | LP-10 … LP-12 |

### CORV-C05 — Интеграции

| Field | Value |
|-------|-------|
| **Purpose** | Website, Bitrix, cash register, sync/exchange, data migration |
| **Groups** | CORV-G05-01 … G05-06 (6) |
| **Excluded** | Web-studio-only shoppers (via negatives), marking, general programmer |
| **Bid strategy** | Tier 1–3 |
| **Budget role** | ~15% |
| **UTM** | `corv_integrations` |
| **Landing family** | LP-13 … LP-17 |

### CORV-C06 — Маркировка и Честный знак

| Field | Value |
|-------|-------|
| **Purpose** | Marking setup, Honest Sign, product-category marking, error fix |
| **Groups** | CORV-G06-01 … G06-13 (13) |
| **Excluded** | Pure regulatory research, equipment-only, general 1C services |
| **Bid strategy** | Tier 2–4 (narrow categories Tier 4) |
| **Budget role** | ~18% — controlled test on categories |
| **UTM** | `corv_marking` |
| **Landing family** | LP-18 … LP-28 |

### CORV-C07 — Неисправности и восстановление

| Field | Value |
|-------|-------|
| **Purpose** | Urgent fix, errors, sync failure, recovery |
| **Groups** | CORV-G07-01 … G07-04 (4) |
| **Excluded** | Vacancy «срочно программист», training |
| **Bid strategy** | Tier 1–2 |
| **Budget role** | ~8% |
| **UTM** | `corv_troubleshooting` |
| **Landing family** | LP-29, LP-30 |

### CORV-C08 — Специализированные

| Field | Value |
|-------|-------|
| **Purpose** | ТС ПИОТ setup and 1C integration |
| **Groups** | CORV-G08-01 … G08-02 (2) |
| **Excluded** | Generic marking, informational regulatory |
| **Bid strategy** | Tier 3 (narrow test) |
| **Budget role** | ~2% controlled test |
| **UTM** | `corv_specialist` |
| **Landing family** | LP-31 |

---

## Cross-campaign isolation rules

| Must not mix | Reason |
|--------------|--------|
| C01 general ↔ C06 marking | Intent + proof + landing differ |
| C01/C02 ↔ C05 integrations | Web-studio bleed |
| C01 ↔ C07 troubleshooting | Ad promise and qualification differ |
| C06 generic marking ↔ C06 product categories | Category-specific ads required |
| Employment queries | Global negatives all campaigns |

---

## UTM structure (all campaigns)

```text
https://lk.corvonero.ru/{path}?utm_source=yandex&utm_medium=cpc&utm_campaign={campaign_code}&utm_content={group_id}&utm_term={phrase}
```

`utm_term` — populated at XLSX export when import supports dynamic params; else embedded in final URL at production.

---

## Manual post-import configuration

| Field | Manual in Commander |
|-------|---------------------|
| Daily budget caps per campaign | Yes — human sets ~100k total split |
| Geo fine-tuning beyond region label | Yes if account requires |
| Organization from Yandex Business | Yes — metadata block |
| Phone number | Yes — metadata block |
| Image/creative upload for text-and-image ads | Yes if not in export row |
| Metrika goals linkage | Yes — SAFE UNKNOWN status |

---

*Machine-readable group list: [ad-group-registry-v1.json](ad-group-registry-v1.json)*

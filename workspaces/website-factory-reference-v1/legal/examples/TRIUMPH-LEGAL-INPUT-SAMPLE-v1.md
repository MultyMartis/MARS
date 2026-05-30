# Triumph Manipulator — Legal Input Sample v1

**Статус:** SAMPLE ONLY — **not operator-signed**  
**Назначение:** демонстрация заполнения [LEGAL-INPUT-SHEET-TEMPLATE-v1.md](../LEGAL-INPUT-SHEET-TEMPLATE-v1.md) на основе pilot audit  
**Pilot plan:** [TRIUMPH-LEGAL-PILOT-PLAN-v1.md](../pilots/TRIUMPH-LEGAL-PILOT-PLAN-v1.md)  
**Gap report:** [TRIUMPH-LEGAL-GAP-REPORT-v1.md](../pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md)

> **Внимание:** поля `company_name`, `legal_name`, `address` помечены `UNKNOWN` там, где audit не дал operator-confirmed значения.  
> **Не использовать для generation** без operator sign-off.

---

## Meta

| Поле | Значение |
|------|----------|
| **sheet_id** | `triumph-manipulator-v6-sample-2026-05-30` |
| **project_name** | Triumph Manipulator Landing |
| **workspace_path** | `workspaces/triumph-manipulator-landing-v6/` |
| **created_date** | 2026-05-30 |
| **last_updated** | 2026-05-30 |

---

## Site Type

| Поле | Значение |
|------|----------|
| **site_type** | `LANDING` |

**Mapping:** L1, L2, L3, L4 required; Footer Rule + Consent Rule — per [SITE-TYPE-LEGAL-MAPPING-v2.md](../SITE-TYPE-LEGAL-MAPPING-v2.md) LANDING row.

---

## Identity (Required)

| Поле | Значение | Variable | Source / Notes |
|------|----------|----------|----------------|
| **company_name** | `UNKNOWN` | `{{company_name}}` | Footer v6 показывает «ООО «ТРИУМФ»» (`v5-page01/landing-footer.html`), но legal footer variant использует «Триумф» без ООО. **Operator sign-off required** per [TRIUMPH-LEGAL-GAP-REPORT-v1.md](../pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md) §1.2. |
| **legal_name** | `UNKNOWN` | audit only | Полное наименование по ЕГРЮЛ **не подтверждено** оператором. ИНН/OGRN указывают на юрлицо, но точная строка из учредительных документов отсутствует в audit sources. |
| **domain** | `manipulator-triumph.ru` | `{{domain}}` | Canonical в `src/pages/*.html` — **High confidence** (gap report §1.2). |
| **email** | `info@manipulator-triumph.ru` | `{{email}}` | Footer, `backend/config.php` — **High confidence**. |
| **phone** | `+7 (918) 991-2-991` | `{{phone}}` | Header, footer, forms — **High confidence**. |

---

## Legal Entity

| Поле | Значение | Variable | Source / Notes |
|------|----------|----------|----------------|
| **entity_type** | `LEGAL_ENTITY` | — | ИНН 10 цифр → юрлицо (не ИП). Operator may confirm. |
| **inn** | `5009114932` | `{{inn}}` | Footer v6 — **High confidence**. |
| **ogrn** | `1185027010321` | `{{ogrn}}` | Footer v6 — **High confidence**. |

---

## Address

| Поле | Значение |
|------|----------|
| **address_status** | `NOT_PROVIDED` |
| **address** | *(empty)* |

**Notes on address decision:** Юридический адрес **не найден** в footer/legal partials audited in gap report §1.2. Город «Краснодар» присутствует в marketing copy — **не является** юридическим адресом для `{{address}}`. Generation may proceed with Core templates v1 (no `{{address}}` in template bodies). If operator later requires address in requisites — obtain from client registration docs and update sheet to `PROVIDED`.

---

## Derived URLs (Required)

| Поле | Значение | Variable |
|------|----------|----------|
| **privacy_policy_url** | `https://manipulator-triumph.ru/privacy-policy/` | `{{privacy_policy_url}}` |
| **consent_personal_data_url** | `https://manipulator-triumph.ru/consent-personal-data/` | `{{consent_personal_data_url}}` |

---

## Cookie Inventory (Optional)

### Analytics systems

| System | Active | Notes |
|--------|:------:|-------|
| Yandex Metrika | UNKNOWN | Not confirmed in gap report audit |
| Google Analytics | UNKNOWN | Not confirmed |
| Other | — | |

### Tracking systems

| System | Active | Notes |
|--------|:------:|-------|
| reCAPTCHA | UNKNOWN | Gap report §3.5 — SAFE UNKNOWN for L4 factual accuracy |
| Chat widgets | UNKNOWN | |
| Call tracking | UNKNOWN | |
| Other | — | |

---

## Footer Confirmation

| Check | Confirmed |
|-------|:---------:|
| Footer will use 4 canonical links per LEGAL-IMPLEMENTATION-RULES §3 | **no** — current v6 drift: L4 → `/cookies/` + «Cookie файлы» (gap report §1.4) |

**Required fix before production:** align all footer partials to canonical L4 URL and text.

---

## Consent Confirmation

| Check | Confirmed |
|-------|:---------:|
| All PD forms will use canonical Consent Rule per LEGAL-IMPLEMENTATION-RULES §4 | **yes** — gap report §1.7 PASS |

**Forms with PD collection (sampled):** hero form, FAQ form, CTA form — full scan required at execution.

---

## Notes

### Audit sources

- Primary: `workspaces/triumph-manipulator-landing-v6/`
- Governance: `projects/triumph-manipulator-landing/`

### Legacy signals (must not appear in generated L1–L4)

- `gruzotaxi-triumph.ru`, `info@gktriumph.ru` — removed from templates; must not reappear
- `opergt@gktriumph.ru` in backend BCC — review at deploy, outside legal page body

### Blocking items for generation

1. `company_name` = UNKNOWN — operator must confirm exact string
2. `legal_name` = UNKNOWN — operator should confirm against ЕГРЮЛ
3. Footer L4 drift — fix required before production sign-off
4. Legal pages L1–L4 — not yet in v6 build (gap report §1.6)

---

## Operator Sign-Off

| Field | Value |
|-------|-------|
| **Signed by** | *(not signed — sample only)* |
| **Date** | — |
| **Generation authorized** | **no** |

---

*Sample version: v1. Location: `workspaces/website-factory-reference-v1/legal/examples/`.*

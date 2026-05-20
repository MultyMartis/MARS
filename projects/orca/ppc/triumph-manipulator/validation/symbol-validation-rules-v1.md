# Symbol Validation Rules v1 (SY-*)

**Class:** `symbol`  
**Goal:** Enforce Yandex Direct field limits with **spaces included**. **No silent truncation.**

**Authority order:**

1. [assets/direct-commander-template/](../assets/direct-commander-template/)  
2. [ad-entity-schema-v1.md](../schema/ad-entity-schema-v1.md)  
3. Live Direct UI (**SAFE UNKNOWN** if drift)

---

## Global symbol principles

| Principle | Rule |
|-----------|------|
| Spaces count | All `≤ N` limits include spaces |
| No auto-trim | Over-limit → `error`; operator shortens copy |
| Empty required | Missing `headline_1`, `description` → `error` |
| Truncation risk | Near-limit word break → `warn` (SY-07) |
| Draft ads | Symbol rules still apply at export time for rows marked active |

---

## SY-01 — Headline 1 length

| Field | Value |
|-------|-------|
| **rule_id** | SY-01 |
| **title** | Headline 1 within 56 characters |
| **severity** | error |
| **target_entity** | ad (`headline_1`) |
| **purpose** | Prevent Commander import rejection and mid-word truncation in SERP |
| **failure_examples** | `Манипулятор 5 тонн в Краснодаре — заказ сегодня со скидкой` (>56); padded trailing spaces |
| **validation_logic_summary** | `len(headline_1)` ≤ 56 including spaces; trim check for leading/trailing space (SY-09) |
| **recommended_operator_action** | Shorten to intent anchor + geo; move detail to H2 or description |

---

## SY-02 — Headline 2 length

| Field | Value |
|-------|-------|
| **rule_id** | SY-02 |
| **title** | Headline 2 within 30 characters if present |
| **severity** | error |
| **target_entity** | ad (`headline_2`) |
| **purpose** | Secondary line must fit Direct secondary headline slot |
| **failure_examples** | Long qualifier pasted into H2 instead of description |
| **validation_logic_summary** | If `headline_2` non-empty → `len` ≤ 30 |
| **recommended_operator_action** | Compress to geo or single proof point («Краснодар», «Борт 5 т») |

---

## SY-03 — Description length

| Field | Value |
|-------|-------|
| **rule_id** | SY-03 |
| **title** | Description within 81 characters |
| **severity** | error |
| **target_entity** | ad (`description`) |
| **purpose** | Full description visible without platform cut |
| **failure_examples** | Stuffed keyword list in description; copy-paste from landing page first paragraph |
| **validation_logic_summary** | `len(description)` ≤ 81 |
| **recommended_operator_action** | One capability + one trust + CTA path; drop SEO fluff |

---

## SY-04 — Fastlink title length

| Field | Value |
|-------|-------|
| **rule_id** | SY-04 |
| **title** | Each fastlink title ≤ 30 characters |
| **severity** | error |
| **target_entity** | ad (`fastlinks[].title`) |
| **purpose** | Sitelink titles must fit extension limits |
| **failure_examples** | `Перевозка и установка бытовок на объекте` (>30) |
| **validation_logic_summary** | For each fastlink in ad, `len(title)` ≤ 30 |
| **recommended_operator_action** | Short intent label: «Перевозка бытовок», «Безнал юрлицам» |

---

## SY-05 — Callout length

| Field | Value |
|-------|-------|
| **rule_id** | SY-05 |
| **title** | Each callout ≤ 25 characters |
| **severity** | error |
| **target_entity** | ad (`callouts[].text`) |
| **purpose** | Callout extensions have strict character budget |
| **failure_examples** | `Работаем без посредников по Краснодару` (>25) |
| **validation_logic_summary** | For each callout, `len(text)` ≤ 25 |
| **recommended_operator_action** | Split into multiple callouts or move text to description |

---

## SY-06 — Display URL path segments

| Field | Value |
|-------|-------|
| **rule_id** | SY-06 |
| **title** | Display URL path segments ≤ 20 characters each |
| **severity** | error |
| **target_entity** | ad (`display_url.path_1`, `path_2`) |
| **purpose** | Visible URL path must not break Commander validation |
| **failure_examples** | `path_1: manipulyator-5-tonn-krasnodar` (>20) |
| **validation_logic_summary** | Each non-empty path segment `len` ≤ 20; domain required on `display_url.domain` |
| **recommended_operator_action** | Use short slug: `5t`, `bytovka`, `yurlica` |

---

## SY-07 — Truncation risk near limit

| Field | Value |
|-------|-------|
| **rule_id** | SY-07 |
| **title** | Truncation risk at limit boundary |
| **severity** | warn |
| **target_entity** | ad (H1, H2, description, extensions) |
| **purpose** | Flag copy that may display poorly even if technically under limit |
| **failure_examples** | H1 length 54–56 ending mid-compound word; description ends without punctuation at 79–81 |
| **validation_logic_summary** | If `len(field)` ≥ limit−3 and last token split would occur at display boundary → warn |
| **recommended_operator_action** | Leave 2–3 char buffer; end on complete word or punctuation |

---

## SY-08 — Punctuation budget

| Field | Value |
|-------|-------|
| **rule_id** | SY-08 |
| **title** | Excessive punctuation consuming character budget |
| **severity** | warn |
| **target_entity** | ad (headlines, description) |
| **purpose** | Avoid wasting limits on `!!!`, `— —`, repeated pipes |
| **failure_examples** | `Манипулятор 5т!!! Краснодар —— выезд` |
| **validation_logic_summary** | Count `!?.…—|*` runs; warn if >2 decorative clusters or >15% of field length |
| **recommended_operator_action** | One separator max; remove hype punctuation |

---

## SY-09 — Whitespace hygiene

| Field | Value |
|-------|-------|
| **rule_id** | SY-09 |
| **title** | Duplicate or edge whitespace |
| **severity** | warn |
| **target_entity** | ad (all string fields) |
| **purpose** | Prevent accidental length failures and sloppy import |
| **failure_examples** | Double space in H1; trailing space pushing over limit on re-edit |
| **validation_logic_summary** | Fail warn on leading/trailing space, `\s{2,}` inside field |
| **recommended_operator_action** | Normalize spaces before re-measuring length |

---

## SY-10 — Empty required symbol fields

| Field | Value |
|-------|-------|
| **rule_id** | SY-10 |
| **title** | Required ad text fields non-empty |
| **severity** | error |
| **target_entity** | ad |
| **purpose** | Block export of incomplete creatives |
| **failure_examples** | `headline_1: ""`; `description: " "`; missing `display_url.domain` |
| **validation_logic_summary** | `headline_1`, `description`, `display_url.domain` must be non-empty after trim; active ads only |
| **recommended_operator_action** | Complete draft or set ad `status` to draft and exclude from export |

---

## SY-11 — Fastlink / callout count limits

| Field | Value |
|-------|-------|
| **rule_id** | SY-11 |
| **title** | Extension counts within platform max |
| **severity** | error |
| **target_entity** | ad |
| **purpose** | Commander row expansion must match template max |
| **failure_examples** | 8 fastlinks when template allows 4; 10 callouts |
| **validation_logic_summary** | Compare `len(fastlinks)`, `len(callouts)` to template README max (**SAFE UNKNOWN** if template silent → warn) |
| **recommended_operator_action** | Keep highest-intent extensions only |

---

## SY-12 — Display URL vs landing domain coherence

| Field | Value |
|-------|-------|
| **rule_id** | SY-12 |
| **title** | Display URL domain aligns with landing host |
| **severity** | warn |
| **target_entity** | ad |
| **purpose** | User trust — visible domain should match click domain |
| **failure_examples** | `display_url.domain: example.com`, `landing_url: https://triumph-krd.ru/...` |
| **validation_logic_summary** | Parse host from `landing_url` and `display_url.domain`; warn if mismatch |
| **recommended_operator_action** | Set display domain to Triumph production host |

---

## No silent truncation (policy)

If any SY-01–SY-06 would fail after hypothetical auto-trim:

- Validator **must not** write trimmed strings back to document  
- Emit `fail` with `suggested_fix` showing a shorter **example** only  

---

## Registry cross-reference

Full catalog index: [rule-registry-v1.md](rule-registry-v1.md).

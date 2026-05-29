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

## SY-06 — Display URL path segments (document source)

| Field | Value |
|-------|-------|
| **rule_id** | SY-06 |
| **title** | Display path source segments ≤ 20 characters each |
| **severity** | error |
| **target_entity** | ad (`display_url.path_1`, `path_2`) |
| **purpose** | JSON source paths must fit before transport normalization |
| **failure_examples** | `path_1: manipulyator-5-tonn-krasnodar` (>20) |
| **validation_logic_summary** | Each non-empty path segment `len` ≤ 20; domain required on `display_url.domain` |
| **recommended_operator_action** | Use short commercial paths: `manip-5-tonn`, `perevozka-byt`, `manip-dlya-b2b` |

**Note (v0.3):** Commander col 49 receives **normalized transport path** from exporter — see SY-17/SY-18. Document `path_1` may equal intended display path; exporter strips domain/slash if legacy values present.

---

## SY-17 — Commander display path format (v0.3)

| Field | Value |
|-------|-------|
| **rule_id** | SY-17 |
| **title** | Display path is short Commander artifact — not landing URL |
| **severity** | error |
| **target_entity** | ad (`display_url` → transport path) |
| **purpose** | Prevent `domain/slug` composite in «Отображаемая ссылка» |
| **failure_examples** | `manipulator-triumph.ru/manipulyator-5-tonn`; `https://...`; `/manipulyator-5-tonn/` |
| **validation_logic_summary** | After normalization: no `.`, `/`, `:`; charset `^[a-z0-9-]+$`; non-empty for export-ready ads |
| **recommended_operator_action** | Set `path_1` to kebab commercial path; landing stays in `landing_url` |

**Commander behavior (operator-confirmed):** Display field ≈ **20 chars**, letters/digits/hyphen only — **not** a navigable URL.

---

## SY-18 — Display path length thresholds (v0.3)

| Field | Value |
|-------|-------|
| **rule_id** | SY-18 |
| **title** | Display path length warn/error |
| **severity** | warn if > 18; **error** if > 20 or empty when required |
| **target_entity** | ad (normalized display path) |
| **purpose** | Buffer before Commander hard reject |
| **failure_examples** | Empty display path on active ad; 21-char path after normalization |
| **validation_logic_summary** | `len(normalized_path)` — warn ≥ 19; error > 20; error if empty on export-ready |
| **recommended_operator_action** | Shorten to commercial token; split long SEO slug across path_1/path_2 only in JSON if needed |

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

## SY-11 — Fastlink count (ORCA doctrine v0.2)

| Field | Value |
|-------|-------|
| **rule_id** | SY-11 |
| **title** | Fastlink count within platform max; target 8 |
| **severity** | error if > 8 or malformed; **warn** if < 6 |
| **target_entity** | ad (`fastlinks[]`) |
| **purpose** | Maximize SERP sitelink footprint without breaking Commander transport |
| **failure_examples** | 9+ fastlinks; 0 fastlinks on launch-ready ad; duplicate titles |
| **validation_logic_summary** | `len(fastlinks)` ≤ 8 (hard max). Launch-ready / export-ready: **warn** if `len` < 6. **Target:** 8 intent-continuing links. Callouts: separate max (≤ 8 typical — **SAFE UNKNOWN** per template) |
| **recommended_operator_action** | Fill to 8 with diversified commercial routes (capability, use-case, B2B, geo, pricing) per [commercial-validation-rules-v1.md](commercial-validation-rules-v1.md) CM-10 |

**Doctrine (v0.2):** Do **not** default to 2–4 minimal fastlinks — under-utilizes mobile SERP sitelink area and bold-highlight echo slots.

---

## SY-13 — Fastlink URL format

| Field | Value |
|-------|-------|
| **rule_id** | SY-13 |
| **title** | Fastlink URLs well-formed and on-brand |
| **severity** | error |
| **target_entity** | ad (`fastlinks[].url`) |
| **purpose** | Prevent broken or off-domain sitelinks |
| **failure_examples** | `htp://...`; empty URL when title present; `example.com` host |
| **validation_logic_summary** | Each non-empty `url` must parse as `http`/`https` absolute URL; host should match production pack host (`manipulator-triumph.ru`) or documented staging — **warn** on mismatch |
| **recommended_operator_action** | Use production slug table in [landing-routing-schema-v1.md](../schema/landing-routing-schema-v1.md) |

---

## SY-14 — Duplicate fastlinks (v0.3)

| Field | Value |
|-------|-------|
| **rule_id** | SY-14 |
| **title** | No duplicate fastlink title or URL in same ad |
| **severity** | error |
| **target_entity** | ad |
| **purpose** | Commander combined cells and SERP display waste duplicate slots |
| **failure_examples** | Two links titled «Манипулятор 5 т»; same URL twice with different titles; «Безнал» + «Для юрлиц» → same B2B URL |
| **validation_logic_summary** | Normalize title (trim, casefold) and URL (trim, lowercase host); **error** on duplicate title OR duplicate URL within ad |
| **recommended_operator_action** | Diversify intent coverage; one slot per production slug; exporter drops duplicate URLs on transport |

---

## SY-15 — Fastlink description length

| Field | Value |
|-------|-------|
| **rule_id** | SY-15 |
| **title** | Fastlink description within extension budget |
| **severity** | error |
| **target_entity** | ad (`fastlinks[].description_1` or `description`) |
| **purpose** | Avoid Commander rejection or invisible truncation |
| **failure_examples** | Multi-sentence marketing copy in description field |
| **validation_logic_summary** | If description present: `len` ≤ 60 characters (**SAFE UNKNOWN** — confirm against live Direct UI / template) |
| **recommended_operator_action** | One short qualification clause per link |

---

## SY-16 — Fastlink title required when URL present

| Field | Value |
|-------|-------|
| **rule_id** | SY-16 |
| **title** | Fastlink title non-empty when URL set |
| **severity** | error |
| **target_entity** | ad |
| **purpose** | Pair integrity for transport `||` join columns |
| **failure_examples** | URL only row in JSON |
| **validation_logic_summary** | If `url` non-empty after trim → `title` must be non-empty and ≤ 30 (SY-04) |
| **recommended_operator_action** | Add short Russian intent label |

---

## Fastlinks doctrine — SERP footprint (v0.2)

| Aspect | Guidance |
|--------|----------|
| **Why 8** | Yandex Search ads can show multiple sitelinks; more qualified links improve CTR and query-match surface |
| **CTR** | Diversified intents (use-case + capability + B2B + geo) catch secondary clicks without changing group keyword |
| **Bold highlight** | Titles/descriptions may echo query stems — plan in `yandex_bold_highlight.highlight_planned_in` |
| **Mobile** | Sitelinks stack on narrow viewports — short titles (SY-04) scan faster |
| **Minimum 6** | Below 6 → **warn** (under-filled footprint); target **8** before launch-ready |

---

## SY-12 — Display URL vs landing domain coherence

| Field | Value |
|-------|-------|
| **rule_id** | SY-12 |
| **title** | Display URL domain aligns with landing host |
| **severity** | warn |
| **target_entity** | ad |
| **purpose** | User trust — visible domain should match click domain |
| **failure_examples** | `display_url.domain: example.com`, `landing_url: https://manipulator-triumph.ru/...` with `display_url.domain: triumph-krd.ru` |
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

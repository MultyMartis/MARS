# MIG Landing Analysis v2 — Design Contract

**Status:** **documented** — design and contracts only; **no runtime implementation** in this deliverable.  
**Supersedes (projection and operator model):** count-first index semantics and flat pack bullets in Pilot #1.  
**Preserves:** [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md) boundary (MIG structures reality; ORCA interprets).  
**Pilot SoT:** session `mig-20260604-61b585` (Триумф / грузотакси Краснодар).

**Normative boundary:**

> Landing Analysis **may describe** visible page facts with evidence.  
> Landing Analysis **may not conclude** strategy, positioning, conversion quality, or competitor strength.

---

## 1. Problem statement (Pilot #1)

Pilot #1 proved the pipeline **captures** rich facts in per-landing artifacts but **projects** operator value poorly:

| Layer | Pilot #1 behavior | Operator need |
|-------|-------------------|---------------|
| `landing_observations.json` index | `offer_count`, `cta_count`, `trust_count` | Actionable observation families with verbatim strings |
| `landing_observation.json` detail | Full arrays exist | Classification, dedup, family grouping |
| `research_pack.draft.md` | Capped flat bullets; nav headings as «offers» | Intelligence-ready sections per competitor |

**Evidence:** counts in index do not match operator-relevant marketing signals (e.g. Gruzovichec `offer_count: 17` includes section titles; Taxi Maxim `offer_count: 1` while `trust_count: 7`).

---

## 2. Artifact model (v2)

### 2.1 Schema phase label

```text
analysis_phase: landing_analysis_v2
schema_version: 0.2   (design target; not implemented yet)
```

### 2.1 Index (`landing_observations.json`)

**Remove** count-only rows as primary operator signal. **Add** per-landing `observation_summary`:

```json
{
  "landing_id": "…",
  "snapshot_id": "…",
  "domain": "…",
  "evidence_grade": "B",
  "families_present": ["OFFERS", "PRICING", "CTA", "TRUST", "LEAD_CAPTURE"],
  "families_unknown": ["SOCIAL_PROOF"],
  "top_signals": [
    { "family": "DELIVERY_PROMISE", "text": "…", "observation_id": "…-obs012", "confidence": "B" }
  ],
  "artifact_ref": "landings/…/landing_observation.json"
}
```

Counts may remain as **derived debug fields** (`_derived.offer_count`) — not pack-facing.

### 2.2 Detail (`landings/{id}/landing_observation.json`)

Unify typed observations under `observations[]` (family-tagged). Legacy arrays (`offers[]`, `trust_patterns[]`, …) may map 1:1 during migration.

**Canonical observation item:**

| Field | Required | Meaning |
|-------|----------|---------|
| `observation_id` | Yes | `{landing_id}-obs{seq}` |
| `family` | Yes | Observation family enum (§3) |
| `text` | Yes | Verbatim visible string |
| `sub_type` | No | Family-specific subtype (e.g. trust `rating_display`) |
| `category` | No | Offer/marketing category when family = OFFERS (§5) |
| `block_id` | No | Containing visible block |
| `confidence` | Yes | `A` \| `B` \| `C` \| `X` (structural evidence grade) |
| `ambiguity` | No | `none` \| `multi_interpretation` \| `high` |
| `evidence` | Yes | §2.3 |
| `excluded_reason` | No | If filtered from operator projection (nav_noise, duplicate) |

### 2.3 Evidence block (unchanged discipline)

| Field | Required |
|-------|----------|
| `source` | `website_snapshot` \| `page_html` \| `manual_annotation` |
| `snapshot_id` | Yes when source = website_snapshot |
| `snapshot_field` | JSON pointer or null |
| `html_anchor` | Optional DOM anchor |
| `verbatim_text` | Must equal captured text |
| `capture_time` | From snapshot |

**Forbidden:** evidence without snapshot or HTML backing; paraphrase as `verbatim_text`.

---

## 3. Observation families

Minimum families (normative). Each family has: **definition**, **evidence sources**, **confidence rules**, **SAFE UNKNOWN**.

### 3.1 OFFERS

| | |
|--|--|
| **Definition** | Verbatim value or service promise visible to visitor (speed, fleet, scope, discount hook) — **not** section nav labels. |
| **Evidence** | `website_snapshot.offers[]`, `headings[]`, hero/card copy in `page.html` when snapshot missed hero promos. |
| **Confidence** | **B** snapshot field; **C** HTML-only without snapshot field; **X** cannot anchor text. |
| **SAFE UNKNOWN** | Emit family row `status: unknown` — «no marketing offer strings classified after nav-filter»; do not invent offers. |
| **Exclusions** | «Отзывы о нас», «Вопросы и ответы», «О Компании», «Контакты» → `MARKETING_PATTERNS` or drop with `excluded_reason: nav_noise`. |

### 3.2 PRICING

| | |
|--|--|
| **Definition** | Visible price lines, tariffs, «от N ₽», hourly/km rates, fixed-price claims. |
| **Evidence** | `pricing_signals[]`, pricing blocks in HTML. |
| **Confidence** | **B** if currency/number in verbatim text; **C** if rate buried in long blob; **X** if price implied only. |
| **SAFE UNKNOWN** | «pricing visible but not parseable into lines» — list raw blobs max 3. |

### 3.3 CTA

| | |
|--|--|
| **Definition** | Visible action surfaces: phone, form submit, messenger, callback, app download, anchor CTAs. |
| **Evidence** | `cta_elements[]`, `forms[]`, `contacts`. |
| **Confidence** | **B** typed CTA with href/tel; **C** generic «Заказать» without target; **X** JS-only button not in snapshot. |
| **SAFE UNKNOWN** | «CTA surface not resolved» when forms exist but labels missing. |

### 3.4 TRUST

| | |
|--|--|
| **Definition** | Credibility signals: ratings, reviews, guarantees, fleet/experience stats, certificates, legal identifiers. |
| **Evidence** | `trust_signals_visible[]`, review blocks, footer legal. |
| **Confidence** | **B** explicit rating/review text; **C** prose classified as trust; **X** aggregator widget without visible text in capture. |
| **SAFE UNKNOWN** | «trust block detected, verbatim text not extracted». See [mig-landing-trust-signals-model-v2.md](mig-landing-trust-signals-model-v2.md). |

### 3.5 LEAD_CAPTURE

| | |
|--|--|
| **Definition** | Lead forms, callback widgets, multi-step wizards (structure only). |
| **Evidence** | `forms[]`, form-adjacent headings. |
| **Confidence** | **B** field list from snapshot; **C** form detected, fields partial. |
| **SAFE UNKNOWN** | «form marker in HTML, fields not enumerated». |

### 3.6 SOCIAL_PROOF

| | |
|--|--|
| **Definition** | Third-party proof beyond inline trust: platform badges, «N отзывов», Avito/Yandex rating lines, client logos. |
| **Evidence** | Review snippets, logo lists, widget text. |
| **Confidence** | **B** named platform + number; **C** «Reviews section visible» without quotes. |
| **SAFE UNKNOWN** | reviews block in `visible_blocks` but no extractable snippet. |

### 3.7 CONTACT_MODEL

| | |
|--|--|
| **Definition** | How visitor reaches business: phones, email, messengers, app-only, call center hours. |
| **Evidence** | `contacts`, header/footer contact blocks. |
| **Confidence** | **B** tel:/email visible; **C** phone digits without tel link. |
| **SAFE UNKNOWN** | «contact intent visible, channel list incomplete». |

### 3.8 DELIVERY_PROMISE

| | |
|--|--|
| **Definition** | Time/availability promises: подача за N минут, 24/7, срочный вызов, круглосуточно. |
| **Evidence** | Hero, offer lines, trust lines containing time tokens. |
| **Confidence** | **B** explicit duration in text; **C** vague «быстро». |
| **SAFE UNKNOWN** | no time promise string found. |

### 3.9 SERVICE_COVERAGE

| | |
|--|--|
| **Definition** | Geo and service scope: city, край, межгород, vehicle types, tonnage, service lines (переезд, вывоз). |
| **Evidence** | Headings, service lists, FAQ answers. |
| **Confidence** | **B** explicit geo in text; **C** inferred only from page title. |
| **SAFE UNKNOWN** | «service list present, scope lines not classified». |

### 3.10 MARKETING_PATTERNS

| | |
|--|--|
| **Definition** | Structural/page patterns visible without strategy label: app-first, phone-only, calculator LP, FAQ-heavy, aggregator landing, multi-form. |
| **Evidence** | Block graph + CTA mix + acquisition meta. |
| **Confidence** | **B** when ≥2 structural signals agree; **C** single signal. |
| **SAFE UNKNOWN** | do not tag pattern without evidence combo. |

**Forbidden pattern labels:** «weak landing», «strong offer», «better than market».

---

## 4. Trust Signals Model (design)

Structured subtypes (map from v1 `trust_type` + HTML scan). Full spec: [mig-landing-trust-signals-model-v2.md](mig-landing-trust-signals-model-v2.md).

| Subtype | Example (Pilot) | Notes |
|---------|-----------------|-------|
| `rating_display` | Яндекс 5 · 129+ оценок | Parse numbers optional; no authenticity check |
| `review_snippet` | «избранные отзывы с Авито» | Verbatim quote or section descriptor |
| `client_logos` | SAFE UNKNOWN unless alt text captured |
| `experience_claim` | «с 2010 года» | Years in business |
| `fleet_size` | «более 50 машин» | Fleet / capacity |
| `completed_orders` | only if verbatim order count |
| `guarantee` | «гарантируем квалифицированный сервис» | No legal advice |
| `certificate` | license/ISO visible |
| `legal_entity` | ИНН/ОГРН in footer |
| `partner_badge` | bank/partner logos |

**Pilot gap:** v1 mislabels long marketing paragraphs as `statistics` (Taxi Maxim). v2 requires subtype rules + max line length for trust extraction.

---

## 5. Offer Extraction Model (design)

Full contract: [mig-landing-offer-model-v2.md](mig-landing-offer-model-v2.md).

**Canonical offer observation** (subset of `observations[]` where `family = OFFERS`):

```yaml
observation_id: mig-…-obs014
family: OFFERS
text: "срочный вызов Газели занимает всего лишь 20 минут"
category: speed          # enum — rules-only classifier
sub_type: delivery_promise
offer_surface: body      # heading | hero | card | list_item | button_label
confidence: B
evidence:
  source: website_snapshot
  snapshot_id: mig-…-ws003
  snapshot_field: /headings/13
  verbatim_text: "…"
```

**Category enum (rules-only, no LLM):** `speed`, `price`, `fleet`, `scope`, `quality`, `convenience`, `b2b`, `app_channel`, `unknown`.

---

## 6. Research Pack projection (v2)

Pack remains a **view**; `landing_observation.json` stays SoT.

### 6.1 Section layout per captured competitor

Replace flat global lists with **per-domain intelligence cards**:

```markdown
## Landing intelligence — {domain}

**Refs:** `{landing_id}` · `{snapshot_id}` · grade **{B}**

### Value & offers
- {text} — `{category}` · conf **B** · ev `{snapshot_field}`

### Pricing (visible)
- …

### Delivery & coverage
- …

### Trust & social proof
- …

### Contact & CTA
- …

### Page structure
- blocks: hero → pricing → …

### SAFE UNKNOWN
- …
```

### 6.2 Caps (operator-first)

| Family | Max lines per landing in pack |
|--------|------------------------------|
| OFFERS (marketing) | 8 |
| PRICING | 6 |
| DELIVERY_PROMISE + SERVICE_COVERAGE | 5 combined |
| TRUST + SOCIAL_PROOF | 6 |
| CTA + LEAD_CAPTURE | 6 |
| MARKETING_PATTERNS | 4 tags |

Nav-noise exclusions **do not** consume caps.

### 6.3 Session summary

Replace count table with:

- landings analyzed / skipped  
- families with data vs SAFE UNKNOWN counts  
- **no** strategic synthesis line

---

## 7. Reality constraints (prohibited)

| Prohibited | Reason |
|------------|--------|
| LLM invention of offers, trust, or blocks | Violates evidence-first / R1 |
| Marketing assumptions («primary offer», «main CTA») | ORCA / human strategy |
| Strategic interpretation in pack | ORCA R2 |
| Competitor ranking or «stronger/weaker» | ORCA |
| UX/conversion scoring | ORCA |
| Deep Research synthesis in Landing pass | Phase 4 separate |
| New HTTP fetch | Website Acquisition only |
| ORCA handoff automation changes | Out of scope |

---

## 8. Migration from v1 (future implementation)

1. Add `observations[]` builder from existing extractors.  
2. Nav-noise filter before OFFERS projection.  
3. Trust subtype classifier + blob split.  
4. Pack formatter v2 (`formatLandingIntelligenceCard`).  
5. Index `observation_summary` replaces count-first UX.  
6. Keep v1 arrays as `_legacy` during one pilot regression window.

---

## 9. Related documents

| Document | Role |
|----------|------|
| [mig-landing-observation-families-v2.md](mig-landing-observation-families-v2.md) | Family reference tables |
| [mig-landing-offer-model-v2.md](mig-landing-offer-model-v2.md) | Offer object + category rules |
| [mig-landing-trust-signals-model-v2.md](mig-landing-trust-signals-model-v2.md) | Trust subtypes |
| [../reports/REPORT-mig-landing-analysis-v2-design.md](../reports/REPORT-mig-landing-analysis-v2-design.md) | Pilot backtest + REPORT |

---

*Landing Analysis v2 — design only. Pilot session: `projects/mig/sessions/mig-20260604-61b585/`.*

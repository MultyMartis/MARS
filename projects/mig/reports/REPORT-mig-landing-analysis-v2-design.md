# REPORT — Landing Analysis v2 Design

**Lane:** A · **Scope:** documentation-only · **Pilot SoT:** `projects/mig/sessions/mig-20260604-61b585/`  
**Contracts:** [mig-landing-analysis-v2.md](../contracts/mig-landing-analysis-v2.md) · [families](../contracts/mig-landing-observation-families-v2.md) · [offer](../contracts/mig-landing-offer-model-v2.md) · [trust](../contracts/mig-landing-trust-signals-model-v2.md)

---

## Current State Review

### Pipeline (Pilot #1 executed)

```text
manual SERP → Competitor Discovery → Website Acquisition → Landing Analysis v1 → research_pack.draft.md
```

Session **`mig-20260604-61b585`** (request `triumph-gruzotaxi-krasnodar-v1`, outcome in `incoming/mig/completed/`).

### What already works

| Stage | Artifact | Captured signals (proved) |
|-------|----------|---------------------------|
| Website Acquisition | `website_snapshots.json` + `snapshots/sites/*/website_snapshot.json` | title, meta, headings, offers[], pricing_signals[], cta_elements[], forms[], contacts, trust_signals_visible[] |
| Landing Analysis v1 | `landing_observations.json` + `landings/*/landing_observation.json` | visible_blocks[], offers[], cta_patterns[], pricing_patterns[], trust_patterns[], form_patterns[] — each with `evidence` |
| Research Pack | `research_pack.draft.md` | Per-landing metadata; capped bullets for offers, pricing, CTA, trust, blocks |

### What operators see first (weak)

Index rows are **count-only**:

| Landing | Domain | offer_count | cta_count | trust_count |
|---------|--------|-------------|-----------|-------------|
| la001 | gruzotaxi-triumph.ru | 11 | 12 | 9 |
| la003 | krasnodar.gruzovichec.ru | 17 | 4 | 3 |
| la004 | krasnodar.taximaxim.ru | 1 | 2 | 7 |

Pack «Landing observations (structured)» shows only snapshot ref — **no marketing intelligence** in that subsection. Actionable text appears later under flat global headings, still mixed with noise.

### Architecture vs runtime

- **Documented:** [mig-landing-analysis-architecture-v1.md](../contracts/mig-landing-analysis-architecture-v1.md) already defines typed offers, trust, CTA — aligned with detail artifacts.  
- **Implemented (repo evidence):** `lib/landing-analysis/*`, session `mig-20260604-61b585` landings populated.  
- **Gap:** operator projection and index semantics — not acquisition depth.

---

## Information Loss Analysis

| Signal in snapshot / detail JSON | Available? | Lost or degraded where | v2 mitigation |
|----------------------------------|------------|------------------------|---------------|
| Hero promos («50 машин», «20 минут») | Yes — headings/offers | Buried in offer list; pack cap 5/17 | Family OFFERS + DELIVERY_PROMISE; nav filter; higher cap |
| Tariff lines (₽/час, от 539) | Yes — pricing_signals | Shown but not grouped with vehicle class | PRICING family + structured lines |
| Ratings (Яндекс/Авито) | Yes — HTML trust | One blob; subtype `statistics` | TRUST `rating_display` + platform |
| Forms (15 fields Triumph) | Yes — forms[] | Pack: «Lead form» without field summary | LEAD_CAPTURE family |
| Telegram / app CTAs | Yes | Listed under CTA only | CONTACT_MODEL + MARKETING_PATTERNS `app_first` |
| Block order (hero → pricing → FAQ) | Yes — visible_blocks | Pack block list OK | Keep under «Page structure» |
| Section nav headings | Yes — mis-tagged as offers | Pollute OFFERS («Отзывы о нас») | Nav-noise exclusion |
| Taxi Maxim service promise | Weak — 1 offer row | `offer_count: 1` misleads | SERVICE_COVERAGE + TRUST split; no count-first index |
| Reviews block Gruzovichec | Partial — «Reviews section visible» | No quotes | SOCIAL_PROOF SAFE UNKNOWN discipline |
| Aggregator competitors | Not captured (URL plan skip) | N/A for this task | Out of scope |

**Root cause:** projection projects **arrays** as flat bullets; index projects **lengths**. Neither projects **families** or **filtered marketing observations**.

---

## Observation Model

v2 centers on **`observations[]`** with ten families (minimum):

OFFERS · PRICING · CTA · TRUST · LEAD_CAPTURE · SOCIAL_PROOF · CONTACT_MODEL · DELIVERY_PROMISE · SERVICE_COVERAGE · MARKETING_PATTERNS

Each observation:

- verbatim `text`  
- `family` + optional `sub_type` / `category`  
- `confidence` A|B|C|X  
- mandatory `evidence` (snapshot_id + field or HTML)

Index replaces count-first UX with `observation_summary.top_signals[]` (3–5 verbatim lines per landing).

Full tables: [mig-landing-observation-families-v2.md](../contracts/mig-landing-observation-families-v2.md).

---

## Trust Signal Model

v2 structured subtypes: `rating_display`, `review_snippet`, `client_logos`, `experience_claim`, `fleet_size`, `completed_orders`, `guarantee`, `certificate`, `legal_entity`, `partner_badge`.

- **Deprecated:** `statistics` for long marketing paragraphs.  
- **SOCIAL_PROOF** family for platform-linked proof.  
- Numeric fields parsed, never validated.

Spec: [mig-landing-trust-signals-model-v2.md](../contracts/mig-landing-trust-signals-model-v2.md).

---

## Offer Model

Canonical offer = observation with `family: OFFERS` + rules-only `category`:

`speed` | `price` | `fleet` | `scope` | `quality` | `convenience` | `b2b` | `app_channel` | `unknown`

Example:

```yaml
text: "Через мобильное приложение цена ниже на 20%"
category: price
confidence: B
evidence: /headings/4 @ ws003
```

Spec: [mig-landing-offer-model-v2.md](../contracts/mig-landing-offer-model-v2.md).

---

## Projection Model

### research_pack.draft.md (v2 target)

Per competitor **intelligence card** (Russian operator headings):

1. **Ценность и офферы** — filtered OFFERS (≤8)  
2. **Цены** — PRICING (≤6)  
3. **Подача и охват** — DELIVERY_PROMISE + SERVICE_COVERAGE  
4. **Доверие** — TRUST + SOCIAL_PROOF  
5. **Контакт и действия** — CONTACT_MODEL + CTA + LEAD_CAPTURE  
6. **Структура страницы** — blocks + MARKETING_PATTERNS tags  
7. **SAFE UNKNOWN** — per landing

Each bullet: `текст` — категория/подтип · conf **B** · ev `snapshot_field` или `page_html`

**Not in pack:** raw JSON dumps, `offer_count`, strategic lines, ORCA recommendations.

Session summary: landings analyzed / skipped; family coverage — **no** competitor ranking.

---

## Reality Constraints

| Allowed | Forbidden |
|---------|-----------|
| Describe visible text with evidence | LLM-invented offers/trust/blocks |
| Rules-only category/subtype | Marketing «primary offer» / funnel judgment |
| SAFE UNKNOWN per family | Strategic interpretation |
| Re-read page.html for structure | New HTTP fetch |
| Structural MARKETING_PATTERNS tags | UX score, «weak/strong landing» |
| Cite snapshot_id in pack | ORCA scope (positioning, PPC plan) |
| | Deep Research synthesis in this pass |

---

## Pilot Backtest

Source: `mig-20260604-61b585` — [landing_observations.json](../sessions/mig-20260604-61b585/landing_observations.json), detail landings, [research_pack.draft.md](../sessions/mig-20260604-61b585/research_pack.draft.md).

### Triumph — gruzotaxi-triumph.ru (la001)

**Current (index + operator scan):**

```yaml
offer_count: 11
cta_count: 12
trust_count: 9
pack_offers_sample:
  - "Грузовое такси в Краснодаре" [heading]
  - "Отзывы о нас" [heading]
  - "Цены на ГРУЗОВОЕ ТАКСИ" [heading]
pack_trust_sample:
  - "Рейтинг в Яндексе 5 129+ оценок …" [review_snippet]
```

**Expected v2 (excerpt):**

```markdown
## Landing intelligence — gruzotaxi-triumph.ru

### Ценность и офферы
- Автомобиль будет подан, через 20 минут или быстрее! — speed · B · ev page_html
- Квартирный / офисный / дачный переезд — scope · B · ev page_html
- Пассажирское место по городу БЕСПЛАТНО — scope · B · ev page_html
- (excluded: «Отзывы о нас», «Вопросы и ответы» — nav_noise)

### Цены
- от 960 ₽/час … — price · B · ev /pricing_signals/2
- от 1260 ₽/час … — price · B · ev /pricing_signals/3
- Фиксированная цена - известна Вам сразу — price · B · ev /pricing_signals/0

### Доверие
- Рейтинг в Яндексе 5 · 129+ оценок — rating_display/yandex · B
- Рейтинг в Авито 4,8 · 222+ отзывов — rating_display/avito · B

### Контакт и действия
- 2× lead form (15 fields) — LEAD_CAPTURE · B
- Заказать звонок — callback_request · B
- tel +79189912991, +78619912991 — CONTACT_MODEL · B
- telegram: gruzotaxi_triumph — CTA messenger · B

### Структура
- hero → offer/pricing → faq → reviews → contacts → forms
- patterns: dual_lead_form, phone_primary, faq_heavy
```

---

### Gruzovichec — krasnodar.gruzovichec.ru (la003)

**Current:**

```yaml
offer_count: 17
cta_count: 4
trust_count: 3
pack_offers_sample:
  - "СРОЧНЫЙ ВЫЗОВ ГАЗЕЛИ … ОТ 539 РУБ!"
  - "В АВТОПАРКЕ БОЛЕЕ 50 МАШИН…"
  - "Через мобильное приложение цена ниже на 20%"
pack_missing: 12 offers not shown (cap 5)
```

**Expected v2 (excerpt):**

```markdown
## Landing intelligence — krasnodar.gruzovichec.ru

### Ценность и офферы
- СРОЧНЫЙ ВЫЗОВ ГАЗЕЛИ С ПОМИНУТНОЙ ОПЛАТОЙ ОТ 539 РУБ! — price+speed · B · /offers/0
- В АВТОПАРКЕ БОЛЕЕ 50 МАШИН… — fleet · B · /offers/1
- Через мобильное приложение цена ниже на 20% — price · B · /headings/4
- Грузоперевозки по городу Краснодар 24 часа в сутки — convenience · B · /headings/12
- срочный вызов Газели … 20 минут днём и ночью — speed · B · /headings/13
- Работаем без рации! — convenience · B · /headings/14

### Цены
- Грузовое такси … от 539 руб! — price · B
- Город 1500 руб/час · Межгород 17 руб/км — price · B
- Газель рефрижиратор 650 руб/час — price · B

### Доверие
- Reviews section visible — SOCIAL_PROOF · C · page_html
- оперативно … круглосуточно — DELIVERY_PROMISE (dedup) · B

### Контакт и действия
- тел. 8(861)205-25-08 (multiple formats) — CONTACT_MODEL · B
- Скачать приложение для заказа грузового такси — app_channel · B

### Структура
- patterns: app_first_order, phone_primary, tariff_grid
```

---

### Taxi Maxim — krasnodar.taximaxim.ru (la004)

**Current:**

```yaml
offer_count: 1
cta_count: 2
trust_count: 7
pack_offer:
  - "Когда водитель выполнит заказ, окончательная стоимость…" [unknown]
pack_trust: long essays tagged [statistics]
```

**Expected v2 (excerpt):**

```markdown
## Landing intelligence — krasnodar.taximaxim.ru

### Ценность и офферы
- SAFE UNKNOWN — no classified promo offers after nav_filter
- (pricing narrative ≠ service offer — moved to PRICING)

### Цены
- Когда водитель выполнит заказ, окончательная стоимость появится на экране приложения — pricing_model/app · B · /pricing_signals/0

### Подача и охват
- работаем круглосуточно и без выходных — DELIVERY_PROMISE · B · page_html (split from trust blob)
- заказ через оператора, сайт или приложение «Максим» — convenience · B

### Доверие
- (exclude 200+ char marketing paragraphs from TRUST)
- «Оцените все преимущества заказа в сервисе «Максим»» — MARKETING_PATTERNS copy_block · C

### Контакт и действия
- +78619999999 — phone · B
- telegram: taximaxim — messenger · B

### Структура
- patterns: app_first_order, phone_primary, thin_landing (3 blocks)
- OFFERS: safe_unknown
```

---

## Benefits

- Operators read **verbatim market language** grouped by decision area, not counts.  
- Evidence refs survive into pack — audit trail for R1 / Human Review.  
- Pilot-rich sites (Gruzovichec) surface **hero signals** despite long offer arrays.  
- Thin landings (Taxi Maxim) show **SAFE UNKNOWN** instead of false `offer_count: 1`.  
- ORCA receives cleaner typed feed without MIG making strategy calls.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Rules-only category errors | `unknown` + ambiguity flag; human review |
| Over-splitting HTML blobs | Max line length; manual_annotation path |
| Pack length creep | Family caps; exclude nav noise from caps |
| v1/v2 schema drift | `_legacy` arrays one regression window |
| OPERATIONAL-INDEX still says «Landing not implemented» | Update index when implementation starts — design does not change runtime claim |

---

## Recommended Next Step

1. **Approve** v2 contracts (this deliverable).  
2. **Implement** (separate task): `observations[]` builder, nav-noise filter, trust splitter, `formatLandingIntelligenceCard` in `build-research-pack.js`, schema `0.2`.  
3. **Re-run** adapter on frozen pilot request; diff pack vs `mig-20260604-61b585`.  
4. **Human gate:** `evidence/review.md` per [MIG-REALITY-ACQUISITION-MODEL-v1.md](../contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md) before ORCA handoff.

**Explicitly out of scope:** Deep Research, ORCA redesign, new acquisition layers, LLM extraction.

---

*Report generated from Pilot #1 session artifacts — design only.*

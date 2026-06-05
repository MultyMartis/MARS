# REPORT — MIG Stabilization Pass v1

Session: `mig-20260605-mlint01` · Rebuild only · No acquisition · Lane A

## Delivery Promise Fix

### Audit — prior rules

- `build-observations-v2.js` routed delivery tokens only from **offers** via `hasDeliveryTimeTokens`.
- Trust blobs with rating + dispatch text stayed in **SOCIAL_PROOF** / **TRUST** (no split).
- `pricing_signals` with time lexicon stayed in **PRICING**.
- Contract cross-family rule (`mig-landing-observation-families-v2.md`) preferred DELIVERY_PROMISE when time token present — not applied to trust/pricing paths.

### Documented misclassifications (before)

| Domain | Evidence text | Was | Should be |
| --- | --- | --- | --- |
| gruzotaxi-triumph.ru | `Автомобиль будет подан, через 20 минут или быстрее!` | SOCIAL_PROOF (inside rating blob) | DELIVERY_PROMISE |
| gruzovichec.ru | `Оперативная доставка – от 20 минут…` | PRICING | DELIVERY_PROMISE |
| gruzovichec.ru | `…приедем всего за 20 минут…` | TRUST | DELIVERY_PROMISE |
| krasnodar.gruzovichkof.ru | `подача за 15 минут` | DELIVERY_PROMISE | OK (already correct) |

### Implementation

- New `delivery-promise-rules.js` — positive/negative rules, segment extraction, pricing-minute exclusions.
- Trust/pricing/meta/title paths re-route matching segments to **DELIVERY_PROMISE** with evidence refs preserved.

## Phone Presence Model

- Removed raw competitor phone numbers from comparison matrix and research pack contact sections.
- Intelligence layer emits: `phone_present`, `phone_prominent`, `contact_model` (enum: phone_first, form_first, app_first, messenger_first, mixed).
- Phone CTAs redacted to `Phone CTA → tel:[present]` in observations.
- Raw numbers remain in `website_snapshot.json`, `_legacy.contact_patterns`, and `page.html`.

## Geo-Awareness

- New `geo-awareness.js` — compares `session_manifest.scope.city` to visible city tokens in title, meta, headings, offers.
- Flags `geo_mismatch` with evidence (no correction).
- **gruzovichec.ru** flagged: research target Краснодар, observed `пензе` in headings/meta.

## Rebuilt Outputs

Tool: `projects/mig/tools/rebuild-stabilization-pass.mjs`

| Artifact | Status |
| --- | --- |
| `landing_observations.json` + per-landing JSON | Rebuilt |
| `market-leader-comparison-matrix.json` / `.md` | Rebuilt |
| `research_pack.draft.md` | Rebuilt |

## Before / After

| Signal | Before | After |
| --- | --- | --- |
| triumph 20 min promise | trust_signals column | delivery_promise column |
| gruzovichkof 15 min | delivery_promise | delivery_promise (unchanged) |
| gruzovichec 20 min lines | PRICING / TRUST | delivery_promise (2 lines) |
| contact_model column | `phones: +79…` | `phone_present; phone_prominent; contact_model` |
| gruzovichec region | not flagged | `geo_mismatch: observed пензе` |

## Remaining Issues

- Marketing/pricing verbatim blobs may still contain embedded tel fragments (page copy, not contact-model intelligence).
- `_legacy` blocks retain full capture for audit; operator cards should read v2 `observations[]`.
- Geo lexicon is pilot-scoped (Krasnodar, Penza, Moscow, SPb); other cities → SAFE UNKNOWN until lexicon expanded.
- Single-URL capture per domain; Penza homepage for `gruzovichec.ru` is a capture routing issue, not auto-fixed.

## Recommended Next Step

Human review of `geo_mismatch` on gruzovichec.ru (wrong regional landing captured) and comparison matrix delivery/trust columns; no strategy synthesis.

---

*Generated 2026-06-05 · MIG stabilization pass v1*

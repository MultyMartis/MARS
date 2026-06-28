# CORVONERO Production Extensions Final Checkpoint v1

Generated: 2026-06-29  
Repository: `C:\MARS Phenix\AI MARS`  
Branch: `mars/canonical-post-recovery`

## Protected baseline

| Item | Value |
|------|-------|
| Prior final-ad commit | `508837a02658e357ce18dca777a46231d2575b25` |
| Prior final-ad tag | `corvonero-final-p1-search-ads-2026-06` |
| Pre-commit HEAD | `f39d9b9dabd45c6ba609c9fd60cc5226613b049d` |
| Planned tag | `corvonero-final-production-extensions-2026-06` |

## Validation totals

| Metric | Value |
|--------|------:|
| Campaigns | 5 |
| Deployable groups | 15 |
| Deployable phrases | 895 |
| Sitelinks | 20 / 20 — APPROVED, URLS PROVISIONAL |
| Callout sets | 5 / 5 — APPROVED |
| Approved shared negatives | 9 |
| License/product phrase negatives per campaign | 2 |
| Additional CA-05 phrase negative | 1 |
| Cross-campaign negatives deployed | 0 |
| UTM campaign slugs (unique) | 5 |

## Approved campaign settings

- Search: **APPROVED**
- Yandex Advertising Network: **DISABLED**
- Auto-targeting: **DISABLED**
- Geography: **Новосибирск + Новосибирская область**
- Device adjustments: **NONE**
- Demographic adjustments: **NONE**
- Launch: **NOT AUTHORIZED**

## Unresolved settings (unchanged)

- Budget: **OPERATOR_DECISION_REQUIRED**
- Bid strategy: **OPERATOR_DECISION_REQUIRED**
- Schedule: **OPERATOR_DECISION_REQUIRED**
- Metrica counter: **NOT PROVIDED**
- Conversion goals: **NOT PROVIDED**

## Integrity

- No mixed-script `кassa` in approved v2 sitelinks
- No unsupported касса claim
- No `{keyword}` in approved production UTM suffix
- No provisional URL labelled published
- No provisional anchor labelled final
- No cross-negative deployed
- Final ads unchanged since `508837a0`
- Landing-page copy unchanged since `508837a0`

## Scope preserved

Extensions Wave 1 v1 research/proposals, operator-approved v2 sitelinks and callouts, controlled negative deployment list, cross-negative disable decision, base UTM policy, campaign-settings decisions, Commander import profile, readiness gates, wave reports, and deterministic generators `execute-ext-wave-1-v1.mjs` / `execute-ext-wave-1-v2-operator-decisions.mjs`.

## Boundaries

- Commander XLSX: **NOT CREATED**
- Campaign import: **NOT AUTHORIZED**
- Yandex Direct changes: **NOT AUTHORIZED**
- URL publication: **NOT AUTHORIZED**
- Moderation submission: **NOT AUTHORIZED**
- Advertising launch: **NOT STARTED**

## Remaining owners and blockers

1. **Operator** — budget, bid strategy, schedule per campaign; Metrica counter and conversion goals.
2. **Roman** — publish and verify LP URLs; final Tilda anchor IDs.
3. **Commander template owner** — confirm `utm_term={keyword}` macro support before extending production URL suffix.

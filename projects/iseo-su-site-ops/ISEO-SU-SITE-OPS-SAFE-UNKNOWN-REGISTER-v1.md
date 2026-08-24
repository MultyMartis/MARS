# ISEO-SU-SITE-OPS SAFE UNKNOWN Register v1

**Status:** CURRENT
**Updated:** 2026-08-24
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

Rule: do not invent values. `SAFE_UNKNOWN`, `OPEN_TECH`, and `DEFERRED_OPTIONAL` are different classes:

- `SAFE_UNKNOWN` — fact is not proven; non-blocking unless a task touches it.
- `OPEN_TECH` — proven defect/required implementation.
- `DEFERRED_OPTIONAL` — understood choice intentionally postponed; not a blocker.

## Current authority links

- [Current State](ISEO-SU-CURRENT-STATE-v1.md)
- [Knowledge Base](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)
- [Route Matrix](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)
- [Sitemap State](ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md)
- [Tech SEO Evidence](ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md)

## SAFE_UNKNOWN

| ID | Proven current fact | Unknown | Operational rule / evidence needed |
|---|---|---|---|
| `U-007` | Site serves accepted WordPress baseline | Exact current PHP runtime version | Confirm in hosting panel/Site Health only when compatibility task needs it |
| `U-015b` | `/offers` + CPT `offer` + ACF + `single-offer.php` are technically mapped | Exact staff scope of nickname “web-KP” | Route by technical owner; one-line operator confirmation for naming |
| `U-017` | Shared helper invokes PHP mail path | Exact SMTP/relay transport behind hosting | Do not change delivery assumptions; chartered mail review |
| `U-020` | Beget backups are required/used | Exact current restore click-path/object IDs | Operator restore notes or bounded restore drill |
| `U-023` | Known parallel/drift surfaces include home/blog and service delegates | Complete runtime twin/drift inventory | Fetch/diff only chartered paths; maintain drift evidence |
| `U-036` | WPilot RC6 active; bridge/write/dev flags false | Auth-header behavior through deferred bridge | Resolve only in Phase 6D charter |
| `U-041` | WPilot schema was historically reported | Physical current DB table state | DB charter only; not needed for ordinary work |
| `U-047` | `/services.html` once returned 500 and later 200 | Cause of transient failure | Revalidate after services edit; logs/HITL if repeated |
| `U-048` | Main ACF groups and consuming templates are known | Full exact location-rule export | Export/inspect before schema/location change |
| `U-049` | `/offers` page and offer CPT exist | Exact current offers listing composition detail | Bounded template trace before listing UX edit |
| `U-050` | `varvara-new.php` existed as VVR-Searcher surface | Current business owner/use | Do not edit without operator attribution |
| `G-U-004` | Glossary server inventory JSON historically existed; import UI disabled | Retention/removal preference | No cleanup without explicit operator decision |
| `G-U-006` | Published expert terms carry accepted content | Current official status wording for legacy algorithms | Primary-source expert verification before content polish |
| `G-U-007` | GEO terms are in accepted public corpus | Long-term vocabulary stability | Optional future expert review |

`U-022` (whether canonical offline source exists) is **closed**: canonical mirrors are established under `production-source/` and `wordpress/iseoblog-glossary/`. This does not imply every production file has a full source mirror.

## OPEN_TECH

| ID | Required work | Severity/status | Owner |
|---|---|---|---|
| `SM-CHILD-404` | Repair root `/sitemap.xml` to reference working `/sitemap-static.xml` and `/wp-sitemap.xml`; remove obsolete 404 children; then verify robots | HIGH / `OPEN_TECH` | MARS / SITE OPS |
| `STATIC-SITEMAP-MAINT` | Decide/implement safe automatic static sitemap maintenance; fallback bounded rebuild + documented procedure | REQUIRED / `OPEN_TECH` | MARS / SITE OPS |
| `IMG-BROKEN` | Repair relative blog `img/...` path pattern (≈96 sampled broken URLs) and regression-crawl | HIGH / `OPEN_TECH` | MARS / SITE OPS |
| `TECH-SEO-BACKLOG` | Review/route 6 MEDIUM, 8 LOW, 14 REVIEW audit signals using actual CSV IDs/owners | REQUIRED / `OPEN_TECH` + `SEO_REVIEW` | MARS / SITE OPS and SEO REVIEW per CSV |

These four tasks replace the stale statement `OPEN_REQUIRED = 0`.

## DEFERRED_OPTIONAL

Exactly five non-blocking items:

1. Mobile glossary offcanvas parity.
2. Glossary archive Yoast meta description.
3. MERGED alias/search polish.
4. Sitemap duplication beyond the target two-surface root index, if ever justified.
5. WPilot Phase 6D bridge/read-only smoke.

## Proven / closed facts

| Prior uncertainty or stale claim | Current accepted outcome |
|---|---|
| Glossary draft-only / archive 404 | Closed: archive and 184 eligible singles are public |
| Glossary related terms/menu/overflow | Closed: related terms and desktop menu live; overflow fixed |
| Glossary URL form | Closed: slash CPT URLs, not blog-style `.html` |
| Form validation/anti-spam absent | Closed: shared server validation and layered controls active |
| Production recipient unknown | Closed: `nikel007i33@yandex.ru` only; `test_mode=false` |
| Metrika production counter unknown/example | Closed: counter 54287016; example 39163020 is not production |
| Visitor-IP addon absent/unknown | Closed: addon ON, `ipaddress`, validated `REMOTE_ADDR`, kill-switchable |
| Healthy Yoast-style root sitemap | Closed as false: current root advertises three 404 children |
| WPilot onboarding required | Closed as false for ordinary Site Ops; Phase 6D remains optional |

## Summary

- `OPEN_BLOCKER`: 0 site-outage blockers.
- `OPEN_TECH`: 4 required task groups, including 2 confirmed HIGH findings.
- `DEFERRED_OPTIONAL`: 5.
- `SAFE_UNKNOWN`: 14 named non-blocking items.

Follow Current State, Task Routing, Route Matrix, and specialized baselines; unknowns do not authorize broad rediscovery.

# FP-0002 Service Subdivision Pass 1 — Component Reuse v1

| Region | Existing partial/pattern | Decision | New HTML | New CSS |
|--------|--------------------------|----------|--------:|--------:|
| Header | `layout/header.html` | REUSE_EXACT | 0 | 0 |
| Hero | `services-inner-hero-v2` | REUSE_WITH_CONTENT | 0 | 0 |
| Breadcrumbs | `breadcrumbs` | REUSE_WITH_CONTENT | 0 | 0 |
| Subnav | `services-page-subnav` | REUSE_WITH_CONTENT | 0 | 0 |
| Intro | `home-recovery-intro` classes | REUSE_WITH_SCOPED_VARIANT | 1 partial | scoped |
| Primary | `services-category-section-v2` | REUSE_WITH_SCOPED_VARIANT | 0 | scoped |
| Footer/Modal | shared | REUSE_EXACT | 0 | 0 |

**New components:** `service-subdivision-intro-v1.html` only.

**Result:** `REUSE_FIRST_PASS`

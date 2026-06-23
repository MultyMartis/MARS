# FP-0002 — WordPress Plugin Register v1

**Version:** v1 | **Date:** 2026-06-23 | **Stage:** FW-06A.1  
**Policy:** Minimum justified set

## Lifecycle stages

```text
FOUNDATION → FRONTEND INTEGRATION → CONTENT POPULATION → PRE-PRODUCTION → PRODUCTION
```

## Installed (FOUNDATION)

| Plugin | Purpose | Source | Version | Required | Lifecycle stage | Data ownership | Security | Performance | Updates | Rollback | Production eligible |
|--------|---------|--------|---------|----------|-----------------|----------------|----------|-------------|---------|----------|---------------------|
| **mars-local-runtime** (MU) | Local guard, mail suppress, URL guard | MLI standard | 1.0.0 | **YES** | **FOUNDATION** | N/A | Low | Low | Manual | Baseline reset | Local only |
| **shpigovsky-core** | Project functionality boundary | Brain workspace | 0.1.0 | **YES** | **FOUNDATION** | Theme-independent settings (future) | Low | Low | Manual sync | Baseline reset | TBD at handoff |
| **advanced-custom-fields** | Field framework | wordpress.org | 6.8.4 | **YES** (Free path) | **FOUNDATION** | ACF JSON in brain | Medium — keep updated | Low local | **Manual** — no auto-update | Deactivate + baseline | TBD — Pro may replace |
| **akismet** | Bundled with core | core bundle | 5.7 | No | Inactive | — | — | — | — | — | No |
| **hello** | Sample | core bundle | 1.7.2 | No | Inactive | — | — | — | — | — | No |

## Deferred — decision stage

| Plugin category | Lifecycle stage for decision | Status |
|-----------------|------------------------------|--------|
| SEO plugin | FRONTEND INTEGRATION or later | **Not installed** |
| Form builder | FRONTEND INTEGRATION | **Not installed** — architecture not confirmed |
| Cache | PRE-PRODUCTION | **Not installed** — not needed on local foundation |
| Security suite | PRE-PRODUCTION | **Not installed** |
| Page builder | — | **FORBIDDEN** |
| SMTP | CONTENT POPULATION or later | **Not installed** — MU mail suppress sufficient |
| WPilot | Separate controlled install | **HOLD** — see WPilot report |
| Redirects | CONTENT POPULATION | **Not installed** |
| Image optimizer | PRE-PRODUCTION | **Not installed** |

## Explicitly not installed (FW-06A.1 verified)

SEO plugin, form builder, SMTP plugin, cache plugin, security suite, redirect plugin, image optimizer, page builder.

## Update policy

```text
Manual operator decision only. No auto-update for plugins/themes/core on this runtime.
```

---

*FP-0002 plugin register — FW-06A.1 complete.*

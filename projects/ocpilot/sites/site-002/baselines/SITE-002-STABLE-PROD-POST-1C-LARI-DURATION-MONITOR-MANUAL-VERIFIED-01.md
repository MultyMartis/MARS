# BASELINE — SITE-002 Stable Prod Post-1C Lari Duration Monitor Manual Verified 01

**Checkpoint ID:** `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01`  
**Issued:** 2026-07-10  
**Operation:** `SITE-002-STABLE-CHECKPOINT-CONSOLIDATION-01`  
**OCPilot run:** 4.252  
**Parent checkpoint:** [SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md](SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md)  
**Environment:** https://bzpm.ru/ (Production)

## Scope and wording

Stable production checkpoint after post-1C **Lari reparent**, **Duration fix**, and **manual monitor verification** (Runs 4.248, 4.250, 4.251). This checkpoint consolidates verified read-only evidence and operator-approved manual monitor run results. It does **not** claim natural scheduled post-hardening timing proof.

## Verified

| Area | Status |
|------|--------|
| Duration fix (Run 4.239) | **CONFIRMED** — post-patch import `mars_1c_import_2026-07-10_080008.txt`; Duration **6.17 seconds**; SUCCESS |
| Lari reparent (Run 4.235) | **CONFIRMED** — category **88** under **358**; nested canonical `/shkafy-i-lari/lari`; flat `/lari` **301** |
| Sitemap / contact / SEO | **PASS** — sitemap **1424** URLs; `/contact` 200; Wave E H1 samples intact |
| Monitor runner | **CONFIRMED** — Task `\MARS_SITE_002_Post_1C_Catalog_Monitor`; manual run SUCCESS; LastTaskResult **0** |
| Hardened monitor artifacts | **CONFIRMED_MANUALLY** — folder `2026-07-10_13-27-20`; full Run 4.228 contract |

## Explicit exclusions

- Natural scheduled post-hardening run on **2026-07-10 12:30 +07** was **not observed** because the operator workstation was **off/unavailable** at the scheduled slot. Task Scheduler **run missed catch-up disabled**. This is **not** classified as monitor/Task Scheduler failure.
- Historical scheduled run **2026-07-08 12:30 +07** confirmed with LastTaskResult **0** (pre-hardening artifact set only).
- This checkpoint does **not** claim natural scheduled post-hardening timing proof on or after Run 4.228 hardening deploy.

## Onboarding

| Field | Value |
|-------|-------|
| Monitor classification | **ONBOARDING_REQUIRED** |
| Onboarding needs | **5** |
| Next charter | `SITE-002-PROD-CATALOG-ONBOARDING-REVIEW-01` |

## Production mutation

**None** in consolidation — documentation/checkpoint only.

## Rollback

Not applicable — docs/checkpoint only; no production changes in Run 4.252.

## Git authority

Baseline and consolidation report created from temp worktree `X:\AI MARS STORAGE\git-sync-e01\repo`. Main worktree `X:\AI MARS` not mutated.

## Reports

- [SITE-002-STABLE-CHECKPOINT-CONSOLIDATION-01.md](../reports/SITE-002-STABLE-CHECKPOINT-CONSOLIDATION-01.md)
- [SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md](../reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) (Run 4.250)
- [SITE-002-LOCAL-MONITOR-MANUAL-RUN-01.md](../reports/SITE-002-LOCAL-MONITOR-MANUAL-RUN-01.md) (Run 4.251)
- [SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02.md](../reports/SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02.md) (Run 4.248)

## Storage manifest

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01\`

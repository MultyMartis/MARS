# METALLKA — WPilot Current Baseline Reconciliation v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4B-FIX01 — i-seo current WPilot baseline reconciliation  
**Date:** 2026-07-26  
**Sites:** source `https://i-seo.su/` · target `https://metallka.ru/`  
**Status:** **COMPLETE — ISEO BASELINE RECONCILED; METALLKA CODE ALREADY MATCHES**

```text
No tokens, credentials, option values, or connection secrets are recorded here.
```

---

## 1. Operator correction

Operator instructed that Phase 4B RC6 on metallka was **not** the intended current deployment baseline, and that **i-seo.su** currently holds the newer/current WPilot build:

> «надо взять ту же версию что и там и поставить сюда»

This FIX01 treated **i-seo.su production plugin CODE** as provisional source authority for metallka alignment, **without** transferring i-seo token/options/DB/state.

---

## 2. Production identity — i-seo.su (factual)

| Field | Value |
|-------|-------|
| Plugin directory | `wp-content/plugins/metacode-wpilot/` |
| Active | **YES** (WP Admin plugins page) |
| Plugin header Version | **0.3.0** |
| Internal `VERSION` | **0.3.0** |
| `RELEASE_CANDIDATE` | **RC6** |
| `RELEASE_LABEL` | **0.3.0-RC6** |
| `SCHEMA_VERSION` | **0.2.0** |
| `REST_NAMESPACE` | **wpilot/v1** |
| File count | **27** |
| Aggregate manifest SHA-256 | `f2be244567da7c0c69e210f3b7a4dce1680889ce79f5d6c1dfd9654db3ee37ed` |
| ISEO production writes (FIX01) | **0** |

**Do not assume a post-RC6 build:** production constants and file inventory prove **RC6**.

---

## 3. Source / package reconciliation

| Candidate | Relationship to i-seo production CODE |
|-----------|----------------------------------------|
| Canonical source `projects/wpilot/plugin/metacode-wpilot/` | **BYTE-IDENTICAL** (27/27) |
| Deploy package `metacode-wpilot-v0.3.0-rc6.zip` | **BYTE-IDENTICAL** |
| Package SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Older RC1–RC5 ZIPs | **Not identical** |

**Verdict:** **MATCHES CURRENT CANONICAL SOURCE** and **MATCHES EXISTING DEPLOY PACKAGE** (`metacode-wpilot-v0.3.0-rc6.zip`).

No new deploy package was created. RC6 ZIP was **not** overwritten.

---

## 4. Metallka comparison

| Field | Pre-FIX01 metallka |
|-------|--------------------|
| Installed / active | **YES / YES** |
| Version / RC / schema | **0.3.0 / RC6 / 0.2.0** |
| File count | **27** |
| Aggregate manifest SHA-256 | `f2be244567da7c0c69e210f3b7a4dce1680889ce79f5d6c1dfd9654db3ee37ed` |
| **METALLKA CODE == ISEO CODE** | **YES** (byte-for-byte) |

---

## 5. Baseline correction (documentary)

| Prior statement | FIX01 outcome |
|-----------------|---------------|
| «RC6 is the current latest deployment baseline» (Phase 4B project assumption) | **Confirmed against live i-seo**, not merely assumed |
| Operator hypothesis that i-seo runs a **newer-than-RC6** build | **Falsified by production evidence** — i-seo runtime **is** `0.3.0-RC6` |
| Phase 4B metallka RC6 install | Remains **technically successful**; **not failed**. As deployment baseline it is **aligned** with current i-seo after FIX01 proof |

**Current metallka deployment baseline (post-FIX01):** i-seo-proven **`0.3.0-RC6`** / package SHA `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6`.

---

## 6. Update decision

Because metallka plugin CODE was already byte-identical to i-seo:

| Action | Result |
|--------|--------|
| New package build | **NOT REQUIRED** |
| Metallka plugin ZIP replace / filesystem replace | **NOT EXECUTED** (would be no-op / unnecessary risk) |
| Plugin update operations | **0** |
| Tokens created | **0** |
| Metallka token preserved | **YES** |

---

## 7. Stale / follow-up notes

| Item | Note |
|------|------|
| Metallka docs that treat RC6 as “assumed” without i-seo runtime proof | Superseded by this reconciliation artefact |
| Upstream `projects/wpilot/` Operational Index (RC5 authority framing) | Still accurate as programme freeze narrative; **no wpilot/ mutation in FIX01** — optional follow-up to cite i-seo/metallka production RC6 alignment |
| ISEO-SU docs stating accepted RC6 baseline | **Consistent** with FIX01 production probe |

---

## 8. Evidence paths (Storage)

`X:\AI MARS STORAGE\wpilot\evidence\metallka-ru-site-ops\phase-4b-fix01\`

- `iseo-readonly-probe.json` / `iseo-readonly-probe-summary.json`
- `iseo-active-readonly.json`
- `metallka-preupdate-probe.json` / `metallka-preupdate-probe-summary.json`
- `before-plugin/` (CODE-only snapshot)
- `metallka-fix01-smoke.json`

---

*METALLKA WPilot Current Baseline Reconciliation v1 · Phase 4B-FIX01.*

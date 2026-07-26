# METALLKA-RU SITE OPS — README

**Programme:** METALLKA-RU-SITE-OPS  
**Website:** `metallka.ru`  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Fast entry:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

## Purpose

Human-supervised MARS programme for **existing production WordPress site operations** on **metallka.ru**, including controlled WPilot onboarding when separately chartered.

This locus is the **documentary home** for charter, baseline, protected zones, SAFE UNKNOWN register, artifact register, and phase reports.

---

## Current phase

| Field | Value |
|-------|-------|
| **Phase** | **PHASE 4C-R1 COMPLETE** — Gate E retry; auth + read-only REST **PROVEN** |
| **Lifecycle** | **COMPLETE — WPILOT PRODUCTION AUTH + READ-ONLY REST PROVEN** |
| **Production** | **CONNECTED** — WPilot installed/active; read bridge ON; writes OFF |
| **WPilot posture** | `dev_confirmed=true` · `bridge_enabled=true` · `write_enabled=false` · build **0.3.0-RC6** |
| **CHANGE 0001** | **COMPLETE / production validated** |
| **WPilot writes** | **BLOCKED** (Phase 4D+ not started) |
| **Git persistence** | **P4-R2** — clean git-sync commit on remote canonical tip; dirty Active Brain is source-only; push separately gated |
| **Authoritative current state** | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) · [METALLKA-WPILOT-CONNECTION-STATE-v1.md](METALLKA-WPILOT-CONNECTION-STATE-v1.md) |

---

## Historical Phase 1.5 non-claims (superseded)

The following were true at Phase 1.5 locus creation and remain **historical** only (do not treat as current):

- No production access yet  
- No credentials requested  
- No WPilot install / token / bridge / REST smoke on metallka.ru  
- No production writes · no local mirror · no ATLAS ORG/WEB/DOM mint  

---

## Precedent split (none is a 1:1 blueprint)

| Precedent | Role for this programme |
|-----------|-------------------------|
| **i-seo.su** (`projects/iseo-su-site-ops/`) | Production onboarding / security precedent (RC6 install·update·token; safe defaults) |
| **dev.gktriumph.ru** (WPilot DEV) | The7 / WPBakery technical DEV precedent (nested `vc_*`, `vc_raw_html`, `post_content` mutation experience) |
| **FP-0002 / Forge** | Source/runtime/admin ownership methodology (bounded rollout, rollback, QA discipline) |

**Do not** transfer site IDs, theme options, paths, tokens, shortcodes, page structure, ACF schemas, or CPT models from any precedent.

---

## What this programme owns

- Project charter and phase/gate model
- OPERATIONAL-INDEX and programme registers
- Site discovery / access / backup / WPilot onboarding **planning** (when drafted)
- Protected zones and SAFE UNKNOWN discipline for metallka.ru
- Programme reports under `reports/`

---

## What it does not own

| Surface | Owner / note |
|---------|----------------|
| WPilot programme + plugin contracts | `projects/wpilot/` |
| WPilot plugin source | `projects/wpilot/plugin/metacode-wpilot/` |
| i-seo.su site ops | `projects/iseo-su-site-ops/` |
| Website Factory / Forge | `projects/mars-website-factory/` |
| FP-0002 delivery | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` |
| ATLAS identity mint | `projects/atlas/` — mint **not authorized** here |
| MLI runtime profiles | `projects/mars-localhost-infrastructure/` — mirror **DEFER** |

---

## Core documents

| Doc | Role |
|-----|------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Current stage + read order |
| [METALLKA-SITE-OPS-CHARTER-v1.md](METALLKA-SITE-OPS-CHARTER-v1.md) | Scope, gates, boundaries |
| [METALLKA-SITE-OPS-CURRENT-BASELINE-v1.md](METALLKA-SITE-OPS-CURRENT-BASELINE-v1.md) | Consolidated programme baseline |
| [METALLKA-PROTECTED-ZONES-v1.md](METALLKA-PROTECTED-ZONES-v1.md) | Default-protect surfaces |
| [METALLKA-SAFE-UNKNOWN-REGISTER-v1.md](METALLKA-SAFE-UNKNOWN-REGISTER-v1.md) | Unknowns — no analogy fill |
| [METALLKA-ARTIFACT-REGISTER-v1.md](METALLKA-ARTIFACT-REGISTER-v1.md) | Complete vs planned artifacts |
| [reports/](reports/) | Phase reports |

---

## Registry / ATLAS note

- **project_id registration** in `registry/project-registry.md`: **not performed** in Phase 1.5 (registry mutation not authorized by this charter).
- **ATLAS binding:** **PARTIAL / INCOMPLETE** — Person `PER-0003` known; Organization / Website / Domain **NOT FOUND**. Person record does **not** prove ownership or legal binding.

---

*METALLKA-RU-SITE-OPS · current = Phase 4C-R1 PROVEN (T/T/F) · writes BLOCKED · Git P4-R2 remote-canonical prep · Phase 1.5 setup historical.*

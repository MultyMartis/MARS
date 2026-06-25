# Triumph Manipulator — Production Evidence Inventory

**Generated:** 2026-06-22  
**Method:** Repository-only evidence — no memory assumptions  
**Purpose:** Canonical inventory for ORCA Campaign Production Contract derivation

---

## Authority note

| Version | Path | Operator-approved? | Notes |
|---------|------|-------------------|-------|
| Battle stable state | `freeze/battle-pilot-triumph-search-v1/TRIUMPH-SEARCH-RK-STABLE-STATE-v1.md` | **Partial** — Commander import PASS, not launch | Final battle milestone |
| Archive copy | `ppc/triumph-manipulator/archive/stable-search-rk-after-commander-import-v1/` | Same as battle | Full backup |
| JSON instance | `ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | **Not** launch-approved semantic lock | Battle-stable fixture |

**Contradiction preserved:** Stable state claims Commander PASS; launch, budget, schedule remain pending. JSON is draft fixture — not operator semantic lock.

---

## Evidence records

| Path | Artefact type | Lifecycle | Operator-approved | Production decision proved | Reusable | Project-specific | Confidence |
|------|---------------|-----------|-------------------|---------------------------|----------|------------------|------------|
| `ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | PPC JSON instance | Battle-stable | No (draft fixture) | 1 campaign, 12 groups, 64 phrases, manual CPC, per-group negatives | Pattern only | Triumph routes/URLs | **High** |
| `ppc/triumph-manipulator/doctrine/generation-logic-v0.md` | Doctrine | Frozen | Documented architecture | Search intent first; one intent per group; anti-garbage | **Yes** | Tone examples Triumph | **High** |
| `ppc/triumph-manipulator/research/intent-groups-v1.md` | Intent tiers | Frozen | Documented | S/A tier launch priority; tier-X reject | **Yes** | Triumph segment names | **High** |
| `ppc/triumph-manipulator/validation/semantic-validation-rules-v1.md` | Validation rules SE-* | Frozen | Documented | Single intent per group; employment blocklist | **Yes** | Triumph examples | **High** |
| `ppc/triumph-manipulator/validation/commercial-validation-rules-v1.md` | Validation rules CM-* | Frozen | Documented | CTA fit; capability truthfulness; geo consistency | **Yes** | 5t/14m claims | **High** |
| `ppc/triumph-manipulator/validation/landing-continuity-rules-v1.md` | Landing rules LM-* | Frozen | Documented | Ad↔landing intent continuity required | **Yes** | Triumph blueprints | **High** |
| `ppc/triumph-manipulator/tools/validation-cli/` | Validator CLI | Battle-stable | Human-triggered PASS | 345 rules before export | **Yes** | Triumph schema | **High** |
| `ppc/triumph-manipulator/tools/exporter-cli/cross-negative-matrix-v1.4.js` | Cross-negative builder | Battle-stable | Mandatory pre-export | Route-family negatives before export | **Yes** | 12-route matrix | **High** |
| `freeze/ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md` | Cross-negative policy | Frozen | Documented | Negatives after ownership; group scope | **Yes** | Triumph routes | **High** |
| `freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md` | Bid policy | Frozen | Documented | 400–600 anchor; within-group spread | Conditional | Krasnodar manipulator | **High** |
| `freeze/ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md` | Hygiene checklist | Frozen | Documented | Pre-export READY gates | **Yes** | — | **High** |
| `freeze/ppc-launch-export-v1.4/GROUP-FIDELITY-QA-v1.md` | Export QA | Battle evidence | Human spot-check | 12/12 groups; negatives present | **Yes** | — | **High** |
| `freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md` | Post-battle analysis | Frozen | Documented lessons | Semantic≠final copy; URL sync gate; QA≠authority | **Yes** | Triumph battle | **High** |
| `freeze/battle-pilot-triumph-search-v1/COMMANDER-IMPORT-FINDINGS-v1.md` | Import observations | Battle evidence | Human-validated | Transport split; negative syntax | **Yes** | Commander quirks | **High** |
| `freeze/route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md` | Route family | Frozen | Pre-implementation | 12 distinct commercial routes | Pattern | Triumph slugs | **High** |
| `freeze/commander-url-sync-v1/URL-SYNCHRONIZATION-REPORT-v1.md` | URL sync | Frozen | Human gate PASS | Registry↔JSON↔exporter alignment | **Yes** | manipulator-triumph.ru | **High** |
| `ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` | Commander template | SoT | Template only | Sheet1 transport; 78 cols row 14 | **Yes** | Column layout | **High** |
| `ppc/triumph-manipulator/tools/exporter-cli/commander-header-map-v0.json` | Header map | Frozen | Documented | Column contract | **Yes** | Yandex Direct RU | **High** |
| `projects/triumph-manipulator-krasnodar/landing-route-registry.json` | Landing registry | Project | Partial | URL ownership per route | Pattern | Triumph URLs | **Medium** |
| `calibration/triumph-manipulator/` | Calibration loop | Documented | Lessons not launch | Factory↔ORCA drift control | **Yes** | Triumph v6 frontend | **Medium** |
| `projects/corvonero-yandex-direct/production/triumph-production-pattern-audit-v1.md` | Pattern audit | Corvonero Stage 2A | Factual reuse map | Triumph pipeline adapted for Corvonero | **Yes** | Corvonero 8-dir model | **High** |
| `incoming/mig/completed/triumph-gruzotaxi-krasnodar-v1.canonical.json` | MIG intake | Completed pilot | External intake | Business scope intake pattern | Pattern | Triumph brand | **Medium** |
| `workspaces/triumph-manipulator-landing-v6/` | Frontend delivery | Client copy | Deploy checklist exists | Landing continuity for PPC | Pattern | Triumph design | **Medium** |
| `content-packs/examples/triumph-manipulyator-5-tonn-pack-v1/` | Content pack | Example | Pack status docs | Semantic pack ≠ deployed copy | **Yes** | 5t route | **Medium** |

---

## Gaps (SAFE UNKNOWN)

| Item | Status |
|------|--------|
| Gitignored launch XLSX (`exporter-cli/output/`) | By design — not in repo |
| Operator-signed launch approval document | **Not found** in repo |
| Live campaign performance data | **Not in repo** |
| Triumph Word landing `.docx` specs | **Not found** — Tilda/live domain used |

---

## Corvonero contrast evidence (failure patterns)

| Path | Proves |
|------|--------|
| `projects/corvonero-yandex-direct/artifacts/REPORT-orca-evidence-audit-and-commander-v5.md` | Template semantic evidence; classifier overreach |
| `projects/corvonero-yandex-direct/production/audit/v6-rejection` (via reports) | Commercial scope loss; HOLD without operator |
| `projects/corvonero-yandex-direct/production/recovery/v7-production-input-package.json` | 41 seed restorations; operator authority recovery |

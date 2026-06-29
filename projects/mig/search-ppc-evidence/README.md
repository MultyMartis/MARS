# MIG Search PPC Evidence — Canonical Locus

**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (Wave 2 core, uncommitted)  
**Runtime version:** `wave2-mig-evidence-v1`

## Placement decision

Canonical Search PPC evidence production locus:

```text
projects/mig/search-ppc-evidence/
```

**Rationale:** MIG owns SPPC-02, SPPC-03, SPPC-10, SPPC-11 evidence stages per lifecycle contract. Co-locating evidence production under `projects/mig/` preserves existing MIG conventions (`lib/`, `tools/`, `contracts/`, `incoming/mig/` storage) while linking to the cross-system lifecycle in `projects/mars-search-ppc-production/`.

**Cross-link:** [mars-search-ppc-production README](../../../mars-search-ppc-production/README.md)

## Structure

| Path | Role |
|------|------|
| `contracts/` | Session, query-selection, storage contracts |
| `schemas/` | JSON schemas for registry, observations, manifest |
| `runtime/lib/` | Source registry, corpus, normalization, paid SERP, competitors |
| `runtime/cli/mig-evidence.mjs` | Gated CLI |
| `fixtures/` | Bounded test fixtures (no live Yandex dependency) |
| `tests/` | Fixture suite + Wave 2 bypass audit |
| `reports/` | Test results, audits |

## Storage boundary

Large/raw evidence → `X:\AI MARS STORAGE\incoming\mig\` or repo-relative `incoming/mig/` per project session. Git holds contracts, schemas, manifests, checksums, sanitized fixtures only.

## CLI (gated)

```text
node projects/mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs <command> --manifest <path>
```

Commands: `source:register`, `corpus:intake`, `corpus:normalize`, `paid-serp:validate-window`, `paid-serp:run`, `competitors:build-pack`, `evidence:status`

Every production command requires lifecycle authorization via `mig-ppc-gate.mjs`.

## Paid SERP mode

Canonical: **`PAID SERP — BUSINESS HOURS`** — project/region-aware windows; no universal schedule hardcoded.

## Corvonero

**FROZEN** — read-only compatibility audit only; no new collection via this layer.

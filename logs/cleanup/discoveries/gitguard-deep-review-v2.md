# GitGuard Deep Review v2

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2 Discovery  
**Mode:** Investigation + classification only (**no registry edit**, **no pack creation**, **no hook deploy**)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb`)  
**Prior evidence:** Census A-009/A-010; Wave 1 W1-022; [s1-gitguard-positioning-review-v1.md](../../projects/mars-survivability/reports/s1-gitguard-positioning-review-v1.md)

---

## Executive determination

| Question | Answer |
|----------|--------|
| Is GitGuard merely Git discipline? | **No** — broader **survivability advisory framework** (snapshots, protected zones, rollback maps, validation, observability) |
| Is GitGuard a deployed Backup / Checkpoint / Rollback / Survivability **product**? | **No** — **human-operated** docs + CLI helpers under `projects/mars-survivability/`; no `projects/gitguard/` |
| Recommended band | **KEEP** (as survivability sub-concept) + **REGISTER** decision deferred + **MERGE** entity-model narrative with reality index |

**Not ARCHIVE CANDIDATE** — active documentation and tooling map; wrong to treat as dead import.

---

## 1. Original purpose

| Source | Statement |
|--------|-----------|
| `governance/system-entity-model.md` | **GitGuard** listed as example **Program / Operational System** |
| `projects/mars-survivability/registries/gitguard-system-entry-v1.md` | Human-operated **survivability helper**: snapshots, protected folders, rollback maps, emergency restore, pre-destructive verification |
| `contracts/gitguard-survivability-evolution-v1.md` | Evolution contract — **not** shipped software |
| `contracts/gitguard-advisory-layer-v1.md` | Advisory framework: validation + helpers + snapshot discipline + rollback protocols + observability |
| Web-GPT / architecture heritage | “Git checkpoints” as **process signal** (`GIT CHECKPOINT NEEDED`) — **related but not identical** to GitGuard concept |

**Original intent:** Reduce blast radius of Cursor AGENT + full-privilege shell **before** technical hooks exist — bridge from git discipline to structured survivability.

---

## 2. Current artifacts (repository-wide)

### 2.1 Canonical documentation pack

| Path | Role |
|------|------|
| `projects/mars-survivability/registries/gitguard-system-entry-v1.md` | System entry + phase table G0–G5+ |
| `projects/mars-survivability/contracts/gitguard-survivability-evolution-v1.md` | Evolution / future CLI |
| `projects/mars-survivability/contracts/gitguard-advisory-layer-v1.md` | Layer model + language discipline |
| `projects/mars-survivability/contracts/gitguard-tooling-map-v1.md` | G2 validator → GitGuard map |
| `projects/mars-survivability/contracts/destructive-operations-policy-v1.md` | Human-operated enforcement baseline |
| `projects/mars-survivability/protocols/safe-execution-layer-v1.md` | GitGuard snapshot references (planned) |
| `projects/mars-survivability/reports/s1-gitguard-positioning-review-v1.md` | Frozen positioning audit |

### 2.2 Implemented helpers (human-invoked — evidence of maturity)

| Tool | Path | Autonomous? |
|------|------|-------------|
| Scoped operation validator | `tools/validator/scoped-operation-validator-v1.mjs` | **No** |
| Snapshot helper | `tools/helpers/snapshot-helper-v1.mjs` | **No** |
| Scope analyzer | `tools/helpers/scope-analyzer-v1.mjs` | **No** |
| Manifest cross-validator | `tools/observability/manifest-cross-validator-v1.mjs` | **No** |
| Registry drift linter | `tools/observability/registry-drift-linter-v1.mjs` | **No** |
| Rollback map schema | `tools/observability/rollback-map-schema-v1.json` | Schema only |
| Drill reports | `tools/*/reports/d01-*.md` | Evidence |

**Count:** 32 files under `projects/mars-survivability/tools/` (validator, helpers, observability).

### 2.3 What does **not** exist

| Missing | Evidence |
|---------|----------|
| `projects/gitguard/` pack | Explicitly denied in entry + reality index |
| `gitguard` CLI product | Future language in evolution contract only |
| Cursor hooks (G3+) | **Planned** — charter required |
| Autonomous backup service | Non-goals in advisory layer |
| `rollback-map.json` at `projects/gitguard/` | Future path in evolution doc only |

### 2.4 Related but separate: “GIT CHECKPOINT”

| Mechanism | Location | Relation to GitGuard |
|-----------|----------|----------------------|
| `GIT CHECKPOINT NEEDED` / `NO GIT CHECKPOINT` | `governance/system-signals-dictionary.md`, `AGENTS.md`, `web-gpt-sources/04-workflows__git-rules.md` | **Process signal** for rare git commits — **not** GitGuard product |
| ORCA git-checkpoint docs | `projects/orca/starter-pack/git-checkpoint-preparation-v1.md`, freeze folders | Program-local checkpoint **discipline** |
| Lifecycle log | evt 0013 mentions GIT CHECKPOINT scope exclusions | Governance event, not GitGuard |

---

## 3. Current references (sample)

| Consumer | Pattern |
|----------|---------|
| `governance/ecosystem-topology-index.md` | GitGuard = named example; no `projects/gitguard/` |
| `governance/mars-reality-index-v0.md` | GitGuard = **UNKNOWN** (no product pack) |
| `governance/external-systems-relationship-map-v0.md` | Operational ownership **SAFE UNKNOWN** |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/08_SYSTEM_MATURITY_MAP.md` | SAFE UNKNOWN — entity model only |
| `projects/mars-survivability/QUICKSTART.md` | GitGuard = advisory + helpers |
| `projects/mars-survivability/reports/mars-survivability-scorecard-v1.md` | Rollback readiness HIGH RISK — mitigation via GitGuard pilot |
| `projects/homegateway-v4-ai/README.md` | HomeGateway **not** replacement for GitGuard |
| Census / cleanup actions | A-009 REGISTER vs KEEP; W1-022 INVESTIGATE entity-model vs survivability |

**Reference density:** High in survivability pack; **sparse** as standalone program elsewhere.

---

## 4. Maturity evaluation — four intelligence layers

| Layer | Claimed in docs? | Actual reality in repo |
|-------|------------------|-------------------------|
| **Backup Intelligence** | Snapshot manifests, `workspaces/_snapshots/` convention | **Partial** — helpers draft manifests; **human** copies files; no appliance |
| **Checkpoint Intelligence** | Pre-agent snapshot triggers; GIT CHECKPOINT signals elsewhere | **Partial** — discipline + signals; **no** unified checkpoint engine |
| **Rollback Intelligence** | Rollback map schema, advisors, `logs/rollback-history/` | **Partial** — documentation + drills; **no** autonomous rollback |
| **Repository Survivability** | Protected zones, validator, halt/drift protocols, observability | **Strongest** — G0–G4 **Done** as **advisory + CLI** |

**Verdict:** GitGuard is **not merely git discipline** — it is a **documented survivability framework** with **real but human-operated** tooling. It is **not** an autonomous Backup/Checkpoint/Rollback **product layer**.

---

## 5. Classification options (Wave 2 recommendation)

| Option | Recommendation | Rationale |
|--------|----------------|-----------|
| **KEEP** | **Yes** | Active contracts, tools, drills; aligns with `mars-survivability` program |
| **REGISTER** | **Defer — operator decision** | Separate `project_id` only if charter for `projects/gitguard/` pack is approved |
| **MERGE** | **Yes (narrative)** | Entity model “Program example” → cross-link **mars-survivability implements GitGuard direction** |
| **ARCHIVE CANDIDATE** | **No** | Would lose survivability positioning and tool map |

---

## 6. Relationship to Git / MARS cleanup / lifecycle

| System | Relationship |
|--------|--------------|
| Git hosting | GitGuard does **not** replace |
| Lifecycle log | Independent — material survivability policy may warrant lifecycle evt (optional) |
| Cleanup program | Survivability protected zones include `continuity/`, `governance/` — cleanup must respect |
| Incoming | No GitGuard automation on `incoming/` drops |

---

## 7. Proposed operator decisions (deferred)

| ID | Question |
|----|----------|
| G-01 | Promote GitGuard to own `project_id` row? |
| G-02 | Resolve entity-model “Program” vs reality-index “UNKNOWN” in topology index |
| G-03 | Charter G3+ Cursor hooks pilot workspace |
| G-04 | Create `projects/gitguard/rollback-map.json` first entry (human-maintained) |

---

## 8. SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Cursor hook API support for G3+ | Charter says verify — not audited here |
| Operator use frequency of validator CLI | No telemetry |
| Whether `workspaces/_snapshots/` populated on operator machine | Per-workspace |
| External backup appliances | Out of repo |

---

*GitGuard Deep Review v2 — Wave 2 Discovery evidence only.*

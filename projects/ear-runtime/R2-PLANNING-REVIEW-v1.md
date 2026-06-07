# R2 Planning Review v1

**Type:** Architecture planning review — **no** implementation  
**Phase:** R2 Planning Review (post-R1)  
**Date:** 2026-06-04  
**Lane:** B — EAR Runtime Architecture Review  
**Prior phase:** R1.9 Store Hardening — **DONE**  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)  
**Decision companion:** [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md)

---

## Purpose

Define the **intentional scope of R2** before implementation begins. R1 delivered the mock pipeline foundation (Config → Listing → Manifest → Evidence → Snapshot → Store). R2 must not absorb acquisition, connectors, persistence redesign, or OCPilot integration — those are separate charters.

**Evidence rule:** Claims below cite architecture documents and existing runtime source only. No speculation.

---

## Executive summary

| Area | Finding |
|------|---------|
| **Target snapshot** | OpenCart logical tree with 10 sections and quality levels 0–3 per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| **Current runtime snapshot** | Flat in-memory `SnapshotPackage` + mock Store with **three JSON files**; honest **Level 0** at persist |
| **Architecture backlog R2** | **Evidence Package Generator** — not OpenCart section population ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md)) |
| **OCPilot minimum (Run 5 structural)** | **Level 1+** with `file-manifest` — **R3** engineering target per backlog |
| **Recommended program R2 scope** | Evidence Package contract alignment + quarantine layout charter; defer section builders to R3 |
| **Recommended first milestone** | **R2 Evidence Package Generator** (charter) — dependency gate before R3 |

---

## Current Runtime Capability

### Pipeline (mock only)

```text
Config → Listing → Manifest → Evidence → Snapshot → Store
```

| Stage | Runtime artefact | Evidence |
|-------|------------------|----------|
| Config | `config_loader.py`, sample fixtures | R1.2 |
| Listing | `listing_models.py`, `mock_listing.py` (12 synthetic entries) | R1.4 |
| Manifest | `manifest_models.py`, `manifest_builder.py` | R1.5 |
| Evidence | `evidence_models.py`, `evidence_builder.py` | R1.6 |
| Snapshot | `snapshot_models.py`, `snapshot_builder.py` | R1.7 |
| Store | `persistence_layout_builder.py`, `snapshot_store.py` | R1.8 |

**Constraints (unchanged):** Mock only; network disabled; connector skeleton only; no live acquisition; no Publish.

### In-memory `SnapshotPackage` (R1.7)

| Field | Present | OpenCart spec equivalent |
|-------|---------|--------------------------|
| `snapshot_id` | Yes (mock format) | `metadata.snapshot_id` — format not production |
| `site_id` | Yes | `metadata.site_id` |
| `source`, `connector`, `created_from` | Yes | Runtime-internal → `acquisition-log` partial |
| `quality_level` | Yes (`"mock"`) | Must map to `package_quality_level` 0–3 |
| `entry_count`, `excluded_count` | Yes | Manifest **summary only** — not `file-manifest/` |
| `safe_unknown`, `notes` | Yes (flat lists) | `safe-unknown/` — shape differs |

**Not present in runtime model:** `snapshot_contract`, `parent_contract`, `created_at`, `ear_mode`, `operator_approval`, any OpenCart inventory sections.

Source: `runtime/shared/snapshot_models.py`, [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md).

### Mock Store contents (R1.8)

Per snapshot directory under `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/`:

| File | Role |
|------|------|
| `metadata.json` | Contract ids, `package_quality_level: 0`, `environment_class` from config, counts, `store_state: stored_unpublished` |
| `safe-unknown.json` | OpenCart-shaped entries for all `MOCK_UNPOPULATED_SECTIONS` + flat runtime topics |
| `acquisition-log.json` | Partial session log (`acquisition_id`, channel, mode, pilot) |

**Not written:** `file-manifest/`, `theme-info/`, `extension-inventory/`, `ocmod-inventory/`, `database-metadata/`, `seo-structure/`, `environment/` as section folders.

Source: `runtime/persistence/snapshot_store.py`, `runtime/shared/persistence_contract.py` (`MOCK_UNPOPULATED_SECTIONS`, `DEFAULT_PACKAGE_QUALITY_LEVEL_MOCK = 0`).

### Declared quality level (honest)

| Claim | Value | Evidence |
|-------|-------|----------|
| Runtime mock pipeline | `quality_level: "mock"` | `evidence_builder.py` / mock chain |
| Persisted `package_quality_level` | **0** | `persistence_contract.py` |
| Max honest consumer level today | **0** — identity + environment summary + acquisition-log + exhaustive `safe-unknown` | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) Level 0 |

---

## Target Snapshot Capability

### Normative OpenCart package (architecture)

Logical tree per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md):

```text
Snapshot/
├── metadata/
├── file-manifest/
├── theme-info/
├── extension-inventory/
├── ocmod-inventory/
├── database-metadata/
├── seo-structure/
├── environment/
├── safe-unknown/
└── acquisition-log/
```

### Package identity (required at root / metadata)

| Field | Required |
|-------|----------|
| `snapshot_id` | Yes |
| `snapshot_contract` | `ear-opencart-snapshot-v1` |
| `parent_contract` | `ear-snapshot-v1` |
| `site_id` | Yes |
| `created_at` | ISO 8601 |
| `ear_mode` | `0`, `1`, or `2` |
| `operator_approval` | Non-secret approver id |

### Target evidence table — full OpenCart snapshot contents

| Section | Purpose | L0 | L1 | L2 | L3 | Typical source (architecture) |
|---------|---------|----|----|----|----|------------------------------|
| **metadata** | Identity, platform, baseline, quality | Min identity set | + version proof or safe-unknown | + extension context | + comprehensive metadata | Operator + acquisition |
| **environment** | Safety enum (`TEST`…`PRODUCTION`/`UNKNOWN`) | Required | Required | Required | Required | Operator assertion |
| **safe-unknown** | Explicit gaps | Lists all missing sections | Per-section or residual | Per-section | Residual only | Acquisition honesty |
| **acquisition-log** | How evidence was obtained | Min approval + mode | Full trail | Full trail | Full trail | Operator + EAR |
| **file-manifest** | Baseline diff, version proof files | — | Root folders + counts or path subset | — | Comprehensive path list | ZIP/SFTP/SSH scan |
| **database-metadata** | Schema only, no PII | — | Prefix + table list or safe-unknown | — | Extra/missing vs baseline | PMA/SSH/operator export |
| **seo-structure** | SEO/routing indicators | — | SEO flag or safe-unknown | — | Rewrite + extension cross-ref | Config/htaccess scan |
| **theme-info** | Active theme | — | Active theme or safe-unknown | — | Extended theme map | Admin / scan |
| **extension-inventory** | Risk surface | — | — | Installed list | Modules + integrations | Admin + file scan |
| **ocmod-inventory** | Customization map | — | — | Mod list + enabled or safe-unknown | Custom/unknown classified | Mod storage scan |

Parent generic contract ([EAR-SNAPSHOT-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-CONTRACT-v1.md)) uses `access-log` instead of `acquisition-log` and omits OpenCart-only sections — OpenCart spec is **source of truth** for OpenCart packages.

### Lifecycle expectation

```
Acquire → Validate → Store → Consume → Archive
```

Consumers intake only **published** snapshots ([EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md), [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../shared/external-access-runtime/EAR-OPENCART-CONSUMER-GUIDE-v1.md)). Runtime today stops at **stored_unpublished** — Publish is R4.

### Evidence Package (pre-snapshot — R2 architecture target)

Per [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md), distinct from snapshot:

| Category | Required in evidence package |
|----------|------------------------------|
| Identity | `acquisition_id`, `site_ref`, `connector_class` |
| Provenance | channel, timestamps, operator approval ref |
| Scope echo | approved vs attempted paths/tables |
| Artifact index | manifest file, exports, screenshots (refs) |
| Connector status | success / partial / failed |
| Errors/warnings | per connector contract |

Runtime R1.6 `EvidencePackage` today carries only: `source`, `site_id`, `connector`, manifest counts, `quality_level`, flat `safe_unknown`/`notes` — **does not** satisfy evidence spec identity or artifact index.

---

## Gap Matrix

### Runtime vs OpenCart snapshot (summary)

| Capability | Status | Notes |
|------------|--------|-------|
| Pipeline skeleton | **Implemented** | Mock end-to-end |
| Package identity fields | **Partially implemented** | Enriched at persist boundary only; not in `SnapshotPackage` |
| `metadata/` section (full) | **Missing** | Platform/version/baseline fields absent |
| `environment/` section | **Partially implemented** | `environment_class` in `metadata.json` only |
| `safe-unknown/` | **Partially implemented** | OpenCart-shaped at persist; runtime flat strings |
| `acquisition-log/` | **Partially implemented** | Single JSON; missing publish/scope/HITL fields |
| `file-manifest/` | **Missing** | Counts only in metadata |
| `theme-info/` | **Missing** | Listed in `MOCK_UNPOPULATED_SECTIONS` |
| `extension-inventory/` | **Missing** | Level 2+ |
| `ocmod-inventory/` | **Missing** | Level 2+ |
| `database-metadata/` | **Missing** | Level 1+ |
| `seo-structure/` | **Missing** | Level 1+ |
| Quality level 1–3 | **Missing** | Honest max = 0 |
| Publish / consumer intake | **Missing** | R4; store unpublished |
| Evidence Package (full spec) | **Partially implemented** | R1.6 skeleton ≠ EAR-EVIDENCE-PACKAGE-v1 |
| Evidence quarantine storage | **Missing** | R1.8E note — not written |
| Live acquisition / SFTP | **Out of scope** | R1 connector skeleton; Phase 3 pilot |

### Section-level gap matrix

| Section / concern | Implemented | Partially implemented | Missing |
|-------------------|-------------|----------------------|---------|
| **metadata** (contract ids, timestamps, mode, approval) | `site_id`, `snapshot_id` in layout | `snapshot_contract`, `parent_contract`, `created_at`, `ear_mode`, `consumer_target`, counts | Platform/version, baseline fields, `Detected version` |
| **environment** | `environment_class` in metadata JSON | — | Dedicated `environment/` section; `operator_assertion`, weak signals |
| **safe-unknown** | Persist entries for unpopulated sections | Flat runtime strings reshaped at persist | Per-topic acquisition honesty from real evidence |
| **acquisition-log** | `acquisition_id`, channel, mode, tooling | — | `approved_by/at`, `published_by`, `scope`, `hitl_reference`, `partial_run` |
| **file-manifest** | `entry_count`/`excluded_count` | Manifest `entries[]` in memory only — not persisted as section | Path list, hashes, baseline diff fields |
| **theme-info** | — | — | All elements |
| **extension-inventory** | — | — | All elements |
| **ocmod-inventory** | — | — | All elements |
| **database-metadata** | — | — | All elements |
| **seo-structure** | — | — | All elements |
| **Store layout** | 3 JSON + immutability | — | Section folders / ZIP encoding per R1.8C full tree |
| **Validate gate** | Structural validators (in-memory) | — | Quality-level possession checks (R5) |
| **Publish** | — | `store_state: stored_unpublished` | Published consumer reference (R4) |

Source cross-walk: [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Task 2.

---

## Consumer Assessment

### Current runtime quality level

| Assessment | Evidence |
|------------|----------|
| **Honest published quality** | **Level 0** — `DEFAULT_PACKAGE_QUALITY_LEVEL_MOCK = 0`; all L1+ sections declared in `safe-unknown` |
| **OCPilot Run 5 structural work** | **Blocked** — requires Level **1+** and `file-manifest` minimum ([EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../shared/external-access-runtime/EAR-OPENCART-CONSUMER-GUIDE-v1.md), [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md)) |
| **OCPilot extension risk phases** | **Blocked** — Level **2+** |
| **Full read-only audit (Level 3)** | **Blocked** — comprehensive metadata per spec |

### Minimum level required (architecture — evidence only)

| Gate | Minimum level | Key sections | Source |
|------|---------------|--------------|--------|
| OCPilot intake / register snapshot | 0 | metadata min, environment, safe-unknown, acquisition-log | Consumer guide § Quality gating |
| OCPilot consumption (any analysis) | Published snapshot only | Lifecycle Validate → Store → **Publish** | Lifecycle, Publishing spec |
| Run 5 structural resume | **1+** | `file-manifest` adequate for version proof / baseline diff | OCPilot integration § Audit Layer; freeze B-EV-02 |
| Extension risk / ocMod map | **2+** | `extension-inventory`, `ocmod-inventory` | Quality mapping L2 |
| Full read-only audit charter | **3** | Comprehensive manifest + DB indicators + residual safe-unknown only | Quality mapping L3 |
| Connected acquisition (Mode 2) | Possession rules unchanged; **not** a substitute for level | — | Quality mapping § Mode interaction |
| Pilot execution (SITE-001 SFTP) | **Separate authorization** — not implied by level alone | PILOT-GOVERNANCE | Out of R2 planning implementation |

### OCPilot requirements split

| Tier | Requirement | Evidence |
|------|-------------|----------|
| **Required for OCPilot** | Published package; `snapshot_contract` = `ear-opencart-snapshot-v1`; read `safe-unknown` before phases; quality level gates phases; `snapshot_id` on reports; corroborate version via manifest — not metadata alone; halt on level/section gap | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../shared/external-access-runtime/EAR-OPENCART-CONSUMER-GUIDE-v1.md) |
| **Required for OCPilot (Run 5 documented minimum)** | Level **1+** with `file-manifest` | [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) § Audit Layer |
| **Nice to have** | Rich `acquisition-log`; `baseline_approved`; acquisition track metadata; bulk refs for large XML | Integration doc § Connected assumptions; consumer guide |
| **Future** | Operations layer live changes; multi-snapshot diff automation; Mode 2 connected acquire; auto latest-snapshot pointer | Integration § Operations Layer; SAFE UNKNOWN sections |
| **Future consumers (not OCPilot v1)** | WPilot, Website Factory, Landing Pilot — separate specs | [EAR-FUTURE-CONSUMERS-v1.md](../../shared/external-access-runtime/EAR-FUTURE-CONSUMERS-v1.md) |

**No speculation:** OCPilot code paths, UI, and exact phase ID naming are **SAFE UNKNOWN** per consumer guide.

### Freeze alignment (SITE-001 — documentation only)

| Blocker | Snapshot section | Runtime today |
|---------|------------------|---------------|
| B-EV-01 | Version proof / metadata | Missing |
| B-EV-02 | `file-manifest` | Missing |
| B-EV-04 | theme, extension, SEO, DB sections | Missing |

Source: [projects/ocpilot/freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md). **No SITE-001 data in runtime** — by charter.

---

## Candidate Work Packages

Classification uses **architecture backlog IDs** where they exist. User-listed categories mapped — **no implementation assignment**.

| Work package | Class | Rationale (evidence) |
|--------------|-------|----------------------|
| **Evidence Package Generator** (architecture **R2**) | **R2** | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R2; [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md); R1.6 gap |
| **Evidence quarantine / storage layout** | **R2** | Backlog R2 storage row; R1.8E note — evidence folder not written |
| **Environment section** (dedicated `environment/`) | **R3** | Level 0 requires class — partial in metadata; full section = snapshot builder |
| **File manifest expansion** | **R3** | Backlog R3 — Snapshot Builder Level **1**; OCPilot Run 5 blocker |
| **Theme info** | **R3** | Level 1 requirement in OpenCart spec |
| **Database metadata** | **R3** | Level 1 requirement |
| **SEO structure** | **R3** | Level 1 requirement |
| **Extension inventory** | **R3+** | Level 2; R3 backlog non-goals exclude L2+ |
| **OCMOD inventory** | **R3+** | Level 2 |
| **OpenCart section tree / snapshot assembly from evidence** | **R3** | Backlog R3 implements OpenCart spec + mapping |
| **Snapshot validation expansion** (quality possession, publish gates) | **R5** (may parallel R3 after R2 stable) | Backlog R5; lifecycle Validate stage |
| **Store expansion** (section folders, encoding) | **R3** (candidate layout) / **R4** (publish metadata) | R1.8 minimal 3-file layout; R1.8C full tree deferred |
| **Snapshot Publisher** | **R4** | Consumer intake requires Publish |
| **Live SFTP / connected acquisition** | **R3+ / Phase 3 pilot** | Not R2; PILOT execution not authorized |
| **OCPilot integration / Run 5 execution** | **Out of R2** | Consumer-only per boundary |
| **JSON Schema / automated quality validator** | **SAFE UNKNOWN** | OpenCart spec § SAFE UNKNOWN |
| **Comprehensive manifest path threshold** | **SAFE UNKNOWN** | Per-site charter at Request — quality mapping |
| **Physical ZIP vs folder encoding** | **SAFE UNKNOWN** | Spec + R1.8A |
| **WordPress / Factory unified contract** | **R3+ / Phase 4** | Future consumers doc |

### Backlog ID alignment (critical)

| Program label | Architecture backlog meaning |
|---------------|------------------------------|
| **R2** (this planning phase) | **Evidence Package Generator** — not “all snapshot gaps” |
| **R3** | Snapshot Builder — **Level 1** OpenCart sections |
| **R4** | Snapshot Publisher |
| **R5** | Validation Helpers |

Section-expansion work packages listed in the planning brief largely land in **R3+**, not architecture **R2**.

---

## Recommended R2 Scope

### In scope for R2 (program charter — planning recommendation)

1. **Evidence Package contract alignment** — map mock/live connector output to [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) fields (`acquisition_id`, artifact index, scope echo, status).
2. **Evidence quarantine layout charter** — paths under external bulk; separable from snapshot tree; no secrets in git.
3. **Translation boundary spec** — Evidence → candidate snapshot inputs (handoff to R3) without claiming quality level > evidence supports.
4. **Mock-path evidence generator** — extend mock pipeline to emit contract-shaped evidence **without** live network (consistent with R1 mock-only discipline until pilot chartered).

### Explicitly out of R2 scope

| Item | Defer to |
|------|----------|
| OpenCart `file-manifest/` and L1 section population | **R3** |
| Level 2+ inventories | **R3+** |
| Publish / OCPilot intake | **R4** + consumer |
| Quality possession validator automation | **R5** |
| Live SFTP, SITE-001 pilot, connected Mode 2 | Phase 3 pilot charter |
| Persistence redesign / Store hardening changes | Closed at R1.9 |
| OCPilot integration implementation | OCPilot program |

### Non-goals (carry forward)

Per backlog § R2 non-goals: no consumer publish; no final quality claim; no automated redaction engine beyond chartered rules.

---

## Recommended First Milestone

**Single choice:** **R2 — Evidence Package Generator (implementation charter)**

### Justification (architecture evidence)

1. **Dependency order:** Architecture backlog requires `R1 → R2 → R3` ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md)). Section population (file-manifest) is **R3**, not R2.
2. **Pipeline position:** [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) places Evidence between Connector and Validation/Snapshot — R1.6 skeleton does not satisfy this contract.
3. **R1.8E follow-up:** Evidence quarantine persist explicitly deferred to **R2+** ([R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md)).
4. **OCPilot path:** Level 1 `file-manifest` requires validated evidence assembly first — jumping to manifest without R2 violates acquisition-internal vs snapshot boundary.
5. **Honesty:** Current store is Level 0; first milestone must not imply Level 1 publish.

**Not chosen as first milestone:** File Manifest Expansion — correct priority for OCPilot outcomes, but **backlog-owned by R3** after R2 evidence shape is stable.

---

## Risks

| Risk | Severity | Mitigation (planning) |
|------|----------|------------------------|
| **R2 label confusion** — engineers treat R2 as “snapshot sections” | High | Charter must cite backlog § R2; this review names R3 for manifest |
| **Quality level inflation** — mock persist claims L1 without sections | High | Fail closed at Validate; keep `package_quality_level: 0` until R3 |
| **Evidence/snapshot boundary blur** | Medium | Separate quarantine vs snapshot paths in R2 charter |
| **Pilot pressure (SITE-001/SFTP)** | Medium | Explicit OUT OF SCOPE until Execution Authorization |
| **Publish before Validate** | Medium | R4 gated; store remains `stored_unpublished` |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Official JSON Schema for snapshot or evidence | Not in repo |
| Evidence retention after successful publish | Architecture SAFE UNKNOWN |
| Exact “comprehensive manifest” path counts | Per-site Request charter |
| ZIP vs folder physical encoding | Phase 2B+ |
| OCPilot phase ID ↔ quality matrix in OCPilot repo | Consumer guide SAFE UNKNOWN |
| Hybrid 1:N `acquisition_id` → `snapshot_id` merge policy | Architecture SAFE UNKNOWN |
| Whether R5 runs before or in parallel with R3 | Charter may reorder with risk acceptance per backlog |

---

## Evidence index

| ID | Source |
|----|--------|
| E-R2-01 | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| E-R2-02 | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../shared/external-access-runtime/EAR-OPENCART-CONSUMER-GUIDE-v1.md) |
| E-R2-03 | [EAR-SNAPSHOT-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-CONTRACT-v1.md) |
| E-R2-04 | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| E-R2-05 | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| E-R2-06 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| E-R2-07 | [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) |
| E-R2-08 | [EAR-FUTURE-CONSUMERS-v1.md](../../shared/external-access-runtime/EAR-FUTURE-CONSUMERS-v1.md) |
| E-R2-09 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| E-R2-10 | Runtime models and persist — `runtime/shared/*.py`, `runtime/persistence/snapshot_store.py` |
| E-R2-11 | [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md), [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) | Kickoff decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |

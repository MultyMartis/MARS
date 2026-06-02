# EAR Connector Contract v1

**Purpose:** Canonical **conceptual contract** between Mode 2 connectors and EAR — inputs, outputs, status, errors, warnings, and SAFE UNKNOWN behavior.  
**Status:** contract specification only — **no** schemas, serializers, validators, or code.  
**Phase:** 2D

**Consumers of this contract:** EAR validation layer (future), operator tooling, connector implementers (future charter). **Not** OCPilot — consumers receive **Snapshot Packages**, not connector outputs.

---

## Contract overview

```
Connector Input  →  [Connector execution]  →  Connector Output
                      ↓
              Connector Status
              Connector Errors
              Connector Warnings
```

Every connector interaction is **bounded in time** (one acquisition session unless Hybrid charter defines multi-session merge).

---

## Connector Input (conceptual)

What EAR / operator must supply before a connector may run.

| Input category | Required | Description |
|----------------|----------|-------------|
| `acquisition_id` | Yes | Correlates Request, Evidence, and eventual `snapshot_id` |
| `site_ref` | Yes | Consumer site id (e.g. `SITE-001`) |
| `connector_class` | Yes | One of [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md) |
| `channel` | Yes | Echo of approved channel for `acquisition-log` |
| `ear_mode` | Yes | Must be `2` for connected connector execution |
| `scope` | Yes | Paths, tables, max size, environment class, exclusions |
| `credential_ref` | Conditional | Required for connected channels; **reference only** — see [EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md) |
| `operator_approval_ref` | Yes | HITL record id or charter pointer (non-secret) |
| `quality_target` | Optional | Intended snapshot level — connector does not guarantee |
| `hybrid_plan_ref` | Optional | When part of Hybrid Coordinator |

**Forbidden in Connector Input:** Raw passwords, private keys, session cookies in git-bound copies.

---

## Connector Output (conceptual)

What a connector returns on completion (success, partial, or failure with artifacts).

| Output category | Required on success | Description |
|-----------------|---------------------|-------------|
| `evidence_package_ref` | Yes | Pointer to Evidence Package (logical or external bulk) |
| `connector_class` | Yes | Echo |
| `acquisition_id` | Yes | Echo |
| `completed_at` | Yes | ISO 8601 timestamp |
| `scope_echo` | Yes | What was actually attempted vs approved scope |
| `artifact_index` | Yes | Logical list of evidence items (names, types, sizes — no secrets) |
| `read_only_attestation` | Yes | Connector asserts no write operations attempted; violations flagged separately |

**Optional output:**

| Category | Description |
|----------|-------------|
| `bulk_root_ref` | External path for large blobs |
| `supplementary_refs` | Screenshots, exports, sidecar manifests |

Output is **not** a Snapshot Package. EAR Validation maps output → snapshot sections.

---

## Connector Status (conceptual)

Terminal state of a connector session.

| Status | Meaning | EAR Validation |
|--------|---------|----------------|
| `success` | Scope completed; evidence complete per connector capability | May proceed if other gates pass |
| `partial` | Some evidence collected; gaps explicit in warnings | Proceed only with degraded quality + `safe-unknown` |
| `failed` | No usable evidence or read-only violation | Stop Acquire; no publish without new cycle |
| `aborted` | Operator or EAR halted before completion | No evidence package or discard per policy |
| `not_started` | Armed but not executed | N/A |

Status is **connector-local**. Workflow stage status (Validate, Publish) is separate per [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md).

---

## Connector Errors (conceptual)

Hard failures — evidence must not be treated as complete.

| Error class | Examples | Connector behavior |
|-------------|----------|-------------------|
| `authentication_failed` | Bad password, key rejected | Stop; no partial publish as success |
| `connection_failed` | Host unreachable, TLS error | Stop; retry is new session |
| `timeout` | Scope too large, network hang | Stop or `partial` if policy allows salvage |
| `scope_violation` | Path outside approved prefix | Stop; error required |
| `read_only_violation` | Write attempted or detected | Stop; escalate operator |
| `corrupt_artifact` | Unreadable zip, truncated download | Stop or `partial` with explicit error |
| `internal_connector_fault` | Implementation bug | Stop; log without secrets |

Errors are listed in **Connector Output** and copied in summary form to snapshot `acquisition-log` — never include secret values.

---

## Connector Warnings (conceptual)

Non-fatal issues — acquisition may continue with honesty.

| Warning class | Examples |
|---------------|----------|
| `incomplete_scope` | Max size reached before full tree |
| `skipped_path` | Permission denied on one directory |
| `stale_evidence` | ZIP timestamp old vs live claim |
| `weak_evidence` | Screenshot-only for version claim |
| `contradiction_detected` | Admin version ≠ file version — see failures doc |
| `redaction_applied` | `config.php` stripped — fields unknown |
| `degraded_quality` | Cannot reach `quality_target` |

Warnings feed **Evidence Package** metadata and later **`safe-unknown`** entries after validation.

---

## SAFE UNKNOWN behavior

| Situation | Connector | EAR Validation | Snapshot |
|-----------|-----------|----------------|----------|
| Cannot determine version | Emit warning; optional best-effort file | Do not upgrade claim to verified | `safe-unknown` + weak `metadata` |
| Cannot list path | Warning per path | No silent omit from manifest | Explicit gap |
| DB scope denied | Error or partial per charter | No invented table list | `database-metadata` gap |
| Environment class unclear | Warning | Operator declaration wins if present | `environment` may be operator-only |
| Hybrid leg failed | Status per leg | Merge only successful legs; document gaps | Combined `safe-unknown` |

**Rule:** UNKNOWN is always **explicit**. Connectors must not emit placeholder values that look like verified facts (e.g. fake `0.0.0` version).

---

## Contract boundaries

| Boundary | Rule |
|----------|------|
| Connector → EAR | Evidence Package + status/errors/warnings only |
| EAR → Connector | Input + abort signal only during Acquire |
| EAR → Consumer | Snapshot Package only after Publish |
| Connector → Consumer | **Forbidden** direct handoff |

---

## Relation to Snapshot Contract

| Connector contract | Snapshot contract |
|--------------------|-------------------|
| Temporary, acquisition-time | Durable, publish-time |
| May contain bulk refs + raw exports | Contains sections per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| May include pre-redaction raw paths | Must not include secrets at publish |
| `connector_class` provenance | `acquisition-log` channel entries |

---

## SAFE UNKNOWN (contract level)

- Formal enum registry for error/warning codes — use descriptive strings until Phase 3.
- Retry policy (auto vs operator) — not defined in v1 contract.

---

## Non-goals

- JSON Schema, OpenAPI, Protobuf, or in-repo validator for this contract.

# R1 — Contract Mapping v1

**Type:** Audit remediation — config ↔ connector contract alignment  
**Date:** 2026-06-04  
**Purpose:** Prevent R1.3 drift between operator JSON config (R1.2) and architecture connector contract  
**Scope:** Documentation only — **no** schema, **no** code, **no** redesign

**Sources:**

- Operator config: [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md), [runtime/configs/sample-r1-site-001.json](runtime/configs/sample-r1-site-001.json)
- Architecture contract: [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md)

---

## Layer model

```
Operator JSON (R1.2)     Runtime assembly (R1.3+)      Connector contract (architecture)
────────────────────     ─────────────────────────     ────────────────────────────────
site_id, pilot_id,   →   acquisition_id (generated)  →  acquisition_id
environment, etc.          operator_approval_ref (ref)     site_ref
                           scope bundle (mapped)           connector_class, channel
                           quality_target (mapped)         ear_mode, scope
                           credential_ref (passthrough)    credential_ref
                                                         →  Connector Input (conceptual)
```

**Translation layer (future runtime code, not built in R1.2):** a function or module that reads validated operator JSON and produces **Connector Input** dict for connector execution. R1.2 validates operator JSON only — it does **not** emit Connector Input.

---

## Field classification

### Contract fields (architecture — [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) § Connector Input)

| Contract field | Required | Present in R1.2 JSON? | Notes |
|----------------|----------|----------------------|-------|
| `acquisition_id` | Yes | **No** | **Runtime-generated** at session start; correlates log, evidence, snapshot |
| `site_ref` | Yes | **Mapped** from `site_id` | 1:1 rename at translation |
| `connector_class` | Yes | **Mapped** from `connector` | R1.2 value `sftp_readonly` must match [EAR-CONNECTOR-TYPES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-TYPES-v1.md) |
| `channel` | Yes | **Derived** | From `track` + `connector` — e.g. connected SFTP read-only channel for acquisition-log |
| `ear_mode` | Yes | **Mapped** from `mode` | R1.2 `mode_2` → contract `2` |
| `scope` | Yes | **Composite** | Built from `remote_root`, `allowed_paths`, `excluded_paths`, `environment` |
| `credential_ref` | Conditional | **Yes** — direct | Passthrough; resolution is adapter + credential boundary |
| `operator_approval_ref` | Yes | **No** | **Runtime/pilot** — HITL record, charter pointer, or PILOT STATUS ref — not operator JSON in R1.2 |
| `quality_target` | Optional | **Mapped** from `snapshot_target` | R1.2 `level_1` → intended Level 1 snapshot |
| `hybrid_plan_ref` | Optional | **No** | N/A for R1 SFTP path |

### Runtime fields (operator JSON — R1.2 only)

These exist for **CLI ergonomics, pilot binding, and dry-run safety**. They are **not** Connector Input fields. Translation layer may consume them but must not pass them verbatim to contract without mapping.

| R1.2 field | Purpose | Contract fate |
|------------|---------|---------------|
| `pilot_id` | Bind run to PILOT-001 governance | Runtime metadata; may appear in acquisition log — **not** contract input |
| `environment` | TEST / PROD class label | Feeds `scope.environment_class`; operator declaration wins per contract SAFE UNKNOWN rules |
| `output_root` | External bulk output location | **Runtime output binding** — not Connector Input; maps to local/bulk write policy per [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| `dry_run` | R1.2 safety gate — must be `true` until R1.3+ charter allows otherwise | **Runtime guard** — blocks connector execution when `true`; not a contract field |

### Adapter fields (SFTP connector — R1.3+ ownership)

Owned by `runtime/connectors/sftp_readonly/` (future). Not in operator JSON directly.

| Adapter concern | Source from translation | Notes |
|-----------------|-------------------------|-------|
| SFTP host / port | Resolved from `credential_ref` | **Credential boundary** — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) |
| Username / key material | Resolved from `credential_ref` | Never in git JSON |
| Session root path | `scope.sftp_root` ← `remote_root` | CON-L1-A path semantics |
| Path allow/deny | `allowed_paths`, `excluded_paths` | Merge with [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) |
| Read-only session flags | Adapter policy | paramiko (or chosen client) — no write API surface |
| Connection timeout / retry | Adapter config | New session per contract — no silent auto-retry in v1 |

---

## Field mapping table (R1.2 → Connector Input)

| R1.2 JSON field | Connector Input field | Transform |
|-----------------|----------------------|-----------|
| — | `acquisition_id` | Runtime: generate UUID or structured id at session start |
| `site_id` | `site_ref` | Direct map |
| `connector` | `connector_class` | Direct map (`sftp_readonly`) |
| `track` + `connector` | `channel` | Runtime enum / string per acquisition-log convention |
| `mode` | `ear_mode` | `mode_2` → `2` |
| `remote_root` | `scope.sftp_root` (SFTP) | Direct map into scope object |
| `allowed_paths` | `scope.allowed_prefixes` | List passthrough |
| `excluded_paths` | `scope.excluded_patterns` | List passthrough + default exclusions merge |
| `environment` | `scope.environment_class` | Direct map |
| `credential_ref` | `credential_ref` | Direct map — resolve outside loader |
| — | `operator_approval_ref` | Runtime: pilot STATUS, charter id, or operator session record |
| `snapshot_target` | `quality_target` | `level_1` → Level 1 |
| `pilot_id` | — | Runtime metadata only |
| `output_root` | — | Runtime output binding only |
| `dry_run` | — | Runtime execution guard only |

---

## Translation layer (future ownership)

| Component | Owner | Phase |
|-----------|-------|-------|
| JSON load + validate | `shared/config_loader.py` | **R1.2 — DONE** |
| Operator JSON → Connector Input assembly | `shared/` or `connectors/` helper — **TBD in R1.3 charter** | R1.3+ |
| Credential resolution | `shared/` credential helper — **NOT STARTED** | R1.3+ (test-connection) |
| Connector Input → paramiko session | `connectors/sftp_readonly/` | R1.3+ |
| Connector Output → evidence refs | `connectors/sftp_readonly/` + R2 | R1.6+ / R2 |

**Rule:** R1.3 must **not** add fields to operator JSON without updating this mapping and [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md) amendment note.

---

## Contract output fields (R1.3+ — not in config)

Connector Output per architecture — produced by adapter, **not** read from JSON:

| Output field | R1 phase |
|--------------|----------|
| `evidence_package_ref` | Stub in R1; R2 assembles |
| `completed_at` | R1.3+ session |
| `scope_echo` | R1.4+ listing |
| `artifact_index` | R1.6+ manifest |
| `read_only_attestation` | R1.3+ connection / R1.4+ listing |
| Status / errors / warnings | R1.3+ per [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) |

---

## Drift prevention checklist (R1.3)

Before R1.3 code:

- [ ] New operator JSON fields? → Update R1.2 doc + this mapping
- [ ] Renamed contract field? → Architecture amendment — **not** runtime-only rename
- [ ] `dry_run: false` needed? → Explicit charter + decision gate amendment
- [ ] Skip `operator_approval_ref`? → **Forbidden** — fail closed at translation
- [ ] Pass secrets in JSON? → **Forbidden** — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md)

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R1.2 JSON is Connector Input | **No** — it is operator config; translation required |
| Mapping replaces JSON Schema | **No** — conceptual alignment only |
| Connector code exists | **No** |
| Translation layer exists | **No** — documented for R1.3 |

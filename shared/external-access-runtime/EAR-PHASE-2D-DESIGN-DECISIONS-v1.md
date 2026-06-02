# EAR Phase 2D Design Decisions v1

**Purpose:** Capture major architectural decisions for Mode 2 Read-Only Connector Architecture.  
**Phase:** 2D — frozen at documentation completion  
**Status:** decisions record — **no** implementation

---

## DD-2D-01 — Connectors separated from consumers

**Decision:** Connectors produce **Evidence Packages**; consumers receive **Snapshot Packages** only after Publish.

**Rationale:** OCPilot and siblings perform analysis, not acquisition. Mixing roles causes credential drift, non-reproducible audits, and consumer-specific channel logic.

**Alternatives rejected:** Consumer pulls live SFTP directly; connector writes OCPilot report sections.

**Consequences:** Extra validation stage; clear [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md) boundary.

---

## DD-2D-02 — Evidence Package exists as distinct artifact

**Decision:** Introduce **Evidence Package** between connector output and snapshot assembly.

**Rationale:** Raw acquisition may contain secrets, partial trees, and pre-redaction config. Publishing directly from connector would bypass quarantine and quality gates.

**Alternatives rejected:** Connector emits snapshot-shaped tree directly.

**Consequences:** Storage for quarantine; validation mapping layer required at runtime.

---

## DD-2D-03 — Credentials remain external

**Decision:** Connectors use `credential_ref` only; no secrets in git, snapshots, or reports.

**Rationale:** Aligns with [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) and MARS survivability; limits blast radius of repo leaks.

**Alternatives rejected:** Encrypted credentials in snapshot metadata for consumer reconnect.

**Consequences:** Mode 2 requires operator-maintained secret store; connected acquisition fails without ref.

---

## DD-2D-04 — Validation sits between acquisition and snapshot

**Decision:** **EAR Validation** (workflow stage) maps evidence → snapshot sections; connectors do not certify quality level.

**Rationale:** Phase 2B already defined Validate; connectors are untrusted for completeness and redaction.

**Alternatives rejected:** Connector self-certifies `package_quality_level`.

**Consequences:** Human operator still approves Publish; validation may be manual in first runtime pilot.

---

## DD-2D-05 — Mode 2 architecture precedes runtime implementation

**Decision:** Phase 2D completes connector **architecture only**; runtime forbidden without Phase 3 assessment + charter.

**Rationale:** SITE-001 and OCPilot Run 5 paused on access shape; implementing SFTP scripts before contracts repeats prior drift incidents.

**Alternatives rejected:** Implement SFTP connector in parallel with Phase 2C.

**Consequences:** Mode 0/1 remain operational path until charter; documentation is source of truth.

---

## DD-2D-06 — Connector classes align to Phase 2C channels

**Decision:** Nine connector classes map 1:1 to foundation connection types plus Hybrid Coordinator.

**Rationale:** Operators already think in channels; connectors are implementable adapters.

**Alternatives rejected:** Single mega-connector per platform.

**Consequences:** Hybrid required for OpenCart L3 in most hosts.

---

## DD-2D-07 — Partial acquisition is first-class

**Decision:** Connector status `partial` with explicit warnings; publish allowed only with degraded level and operator acceptance.

**Rationale:** Real hosts timeout, deny paths, or block DB; silent completeness is worse than honest `safe-unknown`.

**Alternatives rejected:** All-or-nothing acquire with no publish on any warning.

**Consequences:** Consumers must read `safe-unknown` and quality level — unchanged OCPilot discipline.

---

## DD-2D-08 — Read-only violation is hard stop

**Decision:** `read_only_violation` → connector `failed`; no publish from session.

**Rationale:** v1 forbids Mode 3; violation may indicate SITE mutation.

**Alternatives rejected:** Log warning and continue.

**Consequences:** Operator must assess SITE; possible remediation outside EAR.

---

## DD-2D-09 — Snapshot mapping table is normative for OpenCart

**Decision:** [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) defines primary vs secondary connector roles per section.

**Rationale:** Prevents ad-hoc “admin-only Run 5” packages without file-manifest.

**Alternatives rejected:** Per-site mapping only in operator head.

**Consequences:** Hybrid plans can be checked against mapping before Acquire.

---

## DD-2D-10 — OpenCart reference architecture is non-executing

**Decision:** [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md) illustrates SITE-001 flow without credentials or access.

**Rationale:** Teaches stack for charter authors; does not imply live connection authority.

**Alternatives rejected:** Embed SITE-001 secrets in example.

**Consequences:** Phase 3 pilot must still write site-specific charter.

---

## DD-2D-11 — No formal schemas in Phase 2D

**Decision:** Connector contract and evidence package remain **conceptual** — no JSON Schema in repo.

**Rationale:** Schema freeze premature before first runtime pilot; Phase 2A already avoided serializers.

**Alternatives rejected:** Publish OpenAPI for connectors in Phase 2D.

**Consequences:** Phase 3 may add schemas with version bump charter.

---

## DD-2D-12 — acquisition-log vs access-log naming

**Decision:** OpenCart snapshot uses `acquisition-log`; generic contract uses `access-log` — same semantic role.

**Rationale:** Phase 2A OpenCart spec already frozen `acquisition-log`; mapping doc bridges both.

**Alternatives rejected:** Rename OpenCart section in 2D (would violate 2A freeze).

**Consequences:** Validation consolidates connector provenance into platform-appropriate section name.

---

## Traceability

| Decision | Primary doc |
|----------|-------------|
| DD-2D-01 | EAR-CONNECTOR-ARCHITECTURE-v1.md |
| DD-2D-02 | EAR-EVIDENCE-PACKAGE-v1.md |
| DD-2D-03 | EAR-CREDENTIAL-BOUNDARY-v1.md |
| DD-2D-04 | EAR-ACQUISITION-WORKFLOW-v1.md |
| DD-2D-05 | EAR-RUNTIME-READINESS-v1.md |
| DD-2D-06 | EAR-CONNECTOR-TYPES-v1.md |
| DD-2D-07–08 | EAR-CONNECTOR-FAILURES-v1.md |
| DD-2D-09 | EAR-SNAPSHOT-MAPPING-v1.md |
| DD-2D-10 | EAR-MODE-2-OPENCART-REFERENCE-v1.md |
| DD-2D-11 | EAR-CONNECTOR-CONTRACT-v1.md |

---

## SAFE UNKNOWN

- Date of first runtime charter approval — operator schedule.
- Whether first implemented connector is ZIP Intake vs SFTP — Phase 3 assessment.

# PILOT-001 — Success Criteria v1

**Pilot ID:** `PILOT-001`  
**Applies to:** Assessment stage (and Implementation Sub-Charter planning)  
**Quality cap:** Snapshot Level **1** only  
**Status:** Charter-defined — **not** yet evaluated

---

## 1. How to read these criteria

| Stage | Criteria apply as |
|-------|-------------------|
| **Charter (now)** | Design-time checklist — architecture traceability |
| **Implementation Sub-Charter** | Must be reflected in sub-charter scope |
| **Execution + Assessment** | Evidence judged pass/fail |

A criterion marked **Charter** may be satisfied by documentation alone. Criteria marked **Execution** require controlled pilot run under separate authorization.

---

## 2. Primary success definition

**Pilot succeeds** if assessors conclude — with cited evidence — that a **future SFTP Read-Only** connector operating under this charter **could** produce an **honest Snapshot Level 1** for SITE-001 TEST consumable by OCPilot, without requiring site modification or write access.

**Pilot does not succeed** if assessment shows architectural contradiction, mandatory write access, or inability to map SFTP evidence to Level 1 sections even under ideal operator discipline.

---

## 3. Success criteria matrix

| ID | Criterion | Stage | Evidence type |
|----|-----------|-------|---------------|
| SC-01 | **Snapshot Level 1 contract defined** — logical package maps to [EAR-SNAPSHOT-CONTRACT-v1.md](../../EAR-SNAPSHOT-CONTRACT-v1.md) + OpenCart spec | Charter | Traceability doc / mapping table |
| SC-02 | **Acquisition path defined** — CON-L1-A documented with connector → evidence → validate → publish | Charter | [PILOT-CHARTER-v1.md](PILOT-CHARTER-v1.md), [EAR-CONNECTED-PATHS-v1.md](../../EAR-CONNECTED-PATHS-v1.md) |
| SC-03 | **Credential boundary respected** — `credential_ref` only; no secrets in git, snapshot, or reports | Charter + Execution | Boundary review + redaction audit |
| SC-04 | **Read-only scope maintained** — no write operations on host, DB, or admin | Execution | Acquisition log + operator attestation |
| SC-05 | **No write operations** — connector and operator actions read-only only | Execution | Protocol logs (future) / operator checklist |
| SC-06 | **Consumer path documented** — OCPilot intake at Level 1 per [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../EAR-OPENCART-CONSUMER-GUIDE-v1.md) | Charter | Consumer guide crosswalk |
| SC-07 | **Validation path documented** — Validate stage + Level 1 gates per [EAR-READINESS-GATES-v1.md](../../EAR-READINESS-GATES-v1.md) | Charter | Gate checklist |
| SC-08 | **SFTP → snapshot mapping** — file-manifest and version proof sections mappable per [EAR-SNAPSHOT-MAPPING-v1.md](../../EAR-SNAPSHOT-MAPPING-v1.md) | Charter | Mapping table |
| SC-09 | **Level 1 minimum evidence identifiable** — version proof, root inventory, DB/theme/SEO per quality mapping or honest `safe-unknown` | Charter + Execution | Candidate package review |
| SC-10 | **Evidence vs snapshot separation** — Evidence Package distinct from published snapshot per [EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md) | Execution | Artifact tree review |
| SC-11 | **Failure semantics exercised** — partial acquisition documented; no publish on inflated level | Execution | Failure drill or live partial case |
| SC-12 | **Publish gate respected** — operator HITL before consumer visibility | Execution | Publish record |
| SC-13 | **Environment honesty** — published `environment: TEST`; no production drift | Execution | Metadata + operator confirmation |
| SC-14 | **Request (G0) complete** — embedded charter Request or equivalent record | Charter | [PILOT-CHARTER-v1.md](PILOT-CHARTER-v1.md) §6 |
| SC-15 | **Stop conditions not triggered** — see [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) | All stages | Incident log empty or resolved |
| SC-16 | **No pilot-to-runtime confusion** — deliverables labeled pilot vs implementation | Charter | [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) compliance |
| SC-17 | **Acquisition log present** — channel, scope, `acquisition_id`, timestamps | Execution | `acquisition-log` section |
| SC-18 | **OCPilot handoff path** — Run 5 resume prerequisites stated without claiming Run 5 complete | Charter | [EAR-OCPILOT-INTEGRATION-v1.md](../../EAR-OCPILOT-INTEGRATION-v1.md) |

---

## 4. Level 1 section checklist (OpenCart)

For **Execution** assessment, candidate Level 1 package must address:

| Section | Minimum (per quality mapping) | SFTP-only expectation |
|---------|------------------------------|------------------------|
| Version proof | From version files or `safe-unknown` | SFTP selective download of `index.php`, `admin/index.php`, etc. |
| `file-manifest` | Root folders + counts or path list | SFTP listing primary source |
| `database-metadata` | Prefix + table list or `safe-unknown` | Often **deferred** without PMA — honest `safe-unknown` acceptable |
| `seo-structure` | Flags or `safe-unknown` | File scan or deferred |
| `theme-info` | Name or `safe-unknown` | Often deferred without Admin |

**Success at Level 1** does not require every section fully populated if `safe-unknown` is honest and consumer gates respected.

---

## 5. Explicit non-success (not required for pilot pass)

| Item | Note |
|------|------|
| Level 2 or 3 publish | Out of scope |
| Full extension inventory | Out of scope |
| Automated validator in repo | Soft gap — manual Validate OK |
| Run 5 audit completion | Consumer scope — not pilot pass criterion |
| 100% DB metadata without PMA | Not required if `safe-unknown` documented |

---

## 6. Assessment verdict template (future)

| Verdict | Meaning |
|---------|---------|
| **PASS** | All mandatory criteria met for declared stage |
| **CONDITIONAL PASS** | Architecture valid; execution gaps documented with follow-up |
| **FAIL** | Stop condition triggered or architectural contradiction |
| **NOT ASSESSED** | Execution not authorized |

**Current verdict:** **NOT ASSESSED**

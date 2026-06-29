# EAR Scope v1

**Status:** conceptual scope for documentation and future human-chartered work. **Not** implementation backlog with commitments.

---

## In scope (v1 foundation)

### Architecture and contracts

- Layer definitions ([EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md))
- Operational modes 0–2 specification ([EAR-MODES-v1.md](EAR-MODES-v1.md))
- Snapshot package schema ([EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md))
- Security and HITL rules ([EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md))
- Connection type catalog with risks ([EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md))

### Acquisition semantics (conceptual)

- **Read-only** collection of:
  - File trees and manifests (or hashes)
  - Extension / module inventories (platform-dependent)
  - Database **metadata** (schema, table list, prefixes) — not necessarily full dumps in v1
  - Version / environment markers where available
  - Access log (who approved, which channel, when)
- **Operator-mediated** Mode 0 and Mode 1 flows
- **Connected read-only** Mode 2 as **design target** for first implementations

### Consumer handoff

- Deliver snapshot to approved external storage or consumer intake path
- Ensure consumers never require raw credentials in git

---

## In scope (future phases — documented only)

See [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md):

- Phase 2: OpenCart / ocStore read-only acquisition patterns
- Phase 3: WordPress read-only acquisition patterns
- Phase 4: Unified snapshot contract across platforms
- Phase 5: Write-mode evaluation (not v1)

---

## Platform coverage (intent)

| Platform family | v1 docs | Implementation |
|-----------------|---------|----------------|
| OpenCart / ocStore | Referenced (OCPilot) | Phase 2 — **not claimed** |
| WordPress | Referenced (WPilot) | Phase 3 — **not claimed** |
| Generic SFTP/FTP/SSH | Connection catalog | **SAFE UNKNOWN** priority |
| DB exports (PMA, dumps) | Metadata-first | Full dump policy TBD per charter |

---

## Operational boundaries

- EAR operates on **external** systems; MARS repo holds **metadata and contracts** only by default.
- Bulk artifacts live outside git per pilot storage policy (e.g. OCPilot `X:\AI MARS STORAGE\`).
- Quarantine and intake rules of each consumer still apply after snapshot delivery.

---

## Out of scope

Listed in detail in [EAR-NON-GOALS-v1.md](EAR-NON-GOALS-v1.md).

---

## SAFE UNKNOWN

- Exact file naming conventions per consumer intake folder — may align with OCPilot external storage in Phase 2 charter.
- Whether one snapshot format serves all CMS families without extension fields — Phase 4 question.

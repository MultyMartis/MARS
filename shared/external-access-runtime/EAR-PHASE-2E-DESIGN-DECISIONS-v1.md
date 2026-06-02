# EAR Phase 2E Design Decisions v1

**Purpose:** Capture approved architectural decisions for **Acquisition Tracks** (Offline + Connected).  
**Phase:** 2E — frozen at documentation completion  
**Status:** decisions record — **no** implementation

---

## DD-2E-01 — EAR supports Offline and Connected acquisition

**Decision:** EAR formally supports **two acquisition families** (tracks): **Offline** (Model A) and **Connected** (Model B). Neither replaces the other.

**Rationale:** OCPilot SITE-001 operational work proved managed projects need Connected channels; legacy and no-access engagements require Offline. Single-track models force consumer bypass.

**Alternatives rejected:** Connected-only EAR; Offline as deprecated interim.

**Consequences:** Phase 2E document set; track recorded at Request; paths split in OFF-* and CON-* docs.

**Primary doc:** [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md)

---

## DD-2E-02 — Offline remains permanent

**Decision:** **Offline Acquisition** is a **permanent** EAR capability, not a bridge until Mode 2 exists.

**Rationale:** Archive-first audits, client packages, air-gapped reviews, and legacy sites remain core MARS workloads indefinitely.

**Alternatives rejected:** Sunset Offline after connector runtime; treat ZIP-only as “legacy mode.”

**Consequences:** [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md) Archive First philosophy; OFF-* paths maintained alongside CON-*.

---

## DD-2E-03 — Connected required for operational projects

**Decision:** **Connected Acquisition** is the **required strategic track** for actively maintained operational projects (SITE-001, BZPM, dealership support, recurring audits) when channels and charter exist.

**Rationale:** Recurring snapshots, structured provenance, and Level 2–3 repeatability depend on read-only connectors under Phase 2D architecture.

**Alternatives rejected:** Permanent Mode 0/1 only for all managed sites.

**Consequences:** Phase 3 **Connected Acquisition Pilot Charter** is explicit next step; Mode 0/1 remain valid **until** runtime chartered.

**Note:** “Required” is **architectural intent**, not mandatory execution before runtime exists.

---

## DD-2E-04 — Consumers never bypass EAR

**Decision:** No consumer (OCPilot, WPilot, Factory, pilots) may acquire live evidence outside EAR when snapshot-based analysis is chartered.

**Rationale:** Extends DD-2D-01; two tracks strengthen boundary — consumers cannot prefer SFTP “just for speed.”

**Alternatives rejected:** OCPilot optional live manifest refresh; consumer-owned connector plugins.

**Consequences:** [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md), [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md).

---

## DD-2E-05 — Hybrid is a lifecycle pattern, not a third family

**Decision:** **Hybrid** denotes multi-leg or multi-snapshot plans combining Offline and Connected — not a third connector family or track enum at foundation level.

**Rationale:** Avoids taxonomy explosion; keeps connector model (Phase 2D) under Connected leg only.

**Alternatives rejected:** Track C = Hybrid with separate connector base class.

**Consequences:** [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) Hybrid section; separate `snapshot_id` per leg default.

---

## DD-2E-06 — Tracks orthogonal to EAR modes 0–3

**Decision:** Acquisition **track** (Offline / Connected) is documented **orthogonal** to **EAR mode** (0 / 1 / 2). Offline → Mode 0–1; Connected → Mode 2.

**Rationale:** Modes describe collection mechanics; tracks describe operational family and project lifecycle.

**Alternatives rejected:** Rename Mode 0 to “Offline Mode” only — would confuse Mode 1 guided offline.

**Consequences:** Both `ear_mode` and `acquisition_track` recommended in metadata when published — serialization Phase 3.

---

## DD-2E-07 — Phase 2E is architecture only

**Decision:** Phase 2E delivers **documentation only** — no code, runtime, connectors, scripts, schemas, or live access.

**Rationale:** Consistent with Phases 2A–2D; SITE-001 must not be used as execution pretext.

**Alternatives rejected:** Implement ZIP intake helper in 2E.

**Consequences:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) Phase 2E DONE; Phase 3 next.

---

## DD-2E-08 — Canonical paths split by track

**Decision:** Canonical path catalogs are split: [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md) and [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md), aligned with but not replacing [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md).

**Rationale:** Operators select track first; OpenCart doc remains platform channel authority.

**Alternatives rejected:** Duplicate entire OpenCart path doc inside track docs only.

**Consequences:** Cross-links in path docs; mapping tables in OFF/CON summaries.

---

## DD-2E-09 — Selection guide is normative for Request stage

**Decision:** [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) is the **normative human decision aid** at EAR Request for track choice.

**Rationale:** Reduces ad-hoc track choice during SITE-001 and future pilots.

**Alternatives rejected:** Track choice implicit in mode field only.

**Consequences:** Request template should cite guide — template update **SAFE UNKNOWN** until Phase 3.

---

## DD-2E-10 — OCPilot integration doc extends consumer guide

**Decision:** [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md) documents track-specific OCPilot workflows without modifying frozen Phase 2A consumer guide sections.

**Rationale:** 2A freeze preserved; 2E adds track lens and Operations Layer boundary.

**Alternatives rejected:** Rewrite EAR-OPENCART-CONSUMER-GUIDE-v1 in place.

**Consequences:** OCPilot authors read both guides.

---

## DD-2E-11 — Phase 3 next step is Connected Acquisition Pilot Charter

**Decision:** After Phase 2E, documented **next** phase intent is Phase 3 **Connected Acquisition Pilot Charter** (assessment + pilot scope), not implicit runtime build.

**Rationale:** Aligns [EAR-RUNTIME-READINESS-v1.md](EAR-RUNTIME-READINESS-v1.md) — charter before implementation.

**Alternatives rejected:** “Phase 3 = implement SFTP immediately.”

**Consequences:** OPERATIONAL-INDEX Phase table update.

---

## Traceability

| Decision | Primary doc |
|----------|-------------|
| DD-2E-01 | EAR-ACQUISITION-TRACKS-v1.md |
| DD-2E-02 | EAR-OFFLINE-ACQUISITION-v1.md |
| DD-2E-03 | EAR-CONNECTED-ACQUISITION-v1.md |
| DD-2E-04 | EAR-OCPILOT-INTEGRATION-v1.md, EAR-FUTURE-CONSUMERS-v1.md |
| DD-2E-05 | EAR-ACQUISITION-SELECTION-GUIDE-v1.md |
| DD-2E-06 | EAR-ACQUISITION-TRACKS-v1.md |
| DD-2E-07 | OPERATIONAL-INDEX.md |
| DD-2E-08 | EAR-OFFLINE-PATHS-v1.md, EAR-CONNECTED-PATHS-v1.md |
| DD-2E-09 | EAR-ACQUISITION-SELECTION-GUIDE-v1.md |
| DD-2E-10 | EAR-OCPILOT-INTEGRATION-v1.md |
| DD-2E-11 | OPERATIONAL-INDEX.md |

---

## Relation to Phase 2D

| 2D decision | 2E reinforcement |
|-------------|------------------|
| DD-2D-01 Consumers separated from connectors | DD-2E-04 across both tracks |
| DD-2D-05 Architecture before runtime | DD-2E-07, DD-2E-11 |
| DD-2D-06 Connector classes = channels | Connected track paths use CON-* |

No Phase 2D decision is revoked by Phase 2E.

---

## SAFE UNKNOWN

- Approval date of first Connected pilot — operator schedule.
- Mandatory `acquisition_track` metadata field — Phase 3 schema charter.

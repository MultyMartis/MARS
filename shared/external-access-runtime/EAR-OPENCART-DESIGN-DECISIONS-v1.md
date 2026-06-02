# EAR OpenCart Design Decisions v1

**Purpose:** Capture **Phase 2C** architecture decisions for OpenCart read-only acquisition.  
**Status:** frozen for Phase 2C scope — changes require explicit charter.  
**Phase:** 2C

---

## D-2C-01 — Acquisition separated from consumers

| | |
|---|---|
| **Decision** | EAR owns evidence **collection and snapshot assembly**; consumers (OCPilot, WPilot, etc.) own **analysis, diff, and reports** only. |
| **Why** | SITE-001 freeze showed pilots re-implementing FTP/SSH/PMA mechanics; duplicated risk and inconsistent packages. |
| **Consequence** | Consumers intake **published snapshots**; no credential handoff in contract. |
| **Evidence** | [projects/ocpilot/freeze/site-001-pre-runtime-bridge/LESSONS-LEARNED-v1.md](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/LESSONS-LEARNED-v1.md), [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md) |

---

## D-2C-02 — Snapshot contract as stable interface

| | |
|---|---|
| **Decision** | Phase 2A OpenCart Snapshot Package (`ear-opencart-snapshot-v1`) is the **only** supported handoff interface between acquisition and consumers. |
| **Why** | Decouples live access volatility from audit methodology; enables baseline diff without live SITE. |
| **Consequence** | Phase 2C maps **channels → sections → levels**; consumers do not depend on SFTP/FTP/etc. |
| **Evidence** | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) |

---

## D-2C-03 — Mode 2 precedes runtime implementation

| | |
|---|---|
| **Decision** | Document **Mode 2 (Connected read-only)** target and channel design **before** building connectors (Phase 2D+). |
| **Why** | Prevents ad-hoc scripts from defining workflow; SITE-001 today uses Mode 0/1 until connectors exist. |
| **Consequence** | Phase 2C is design-only; Phase 2D defines connector **architecture**, not execution in this charter. |
| **Evidence** | [EAR-MODES-v1.md](EAR-MODES-v1.md), [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md) |

---

## D-2C-04 — EAR remains read-only at acquisition

| | |
|---|---|
| **Decision** | All nine channel classes are **read-only** by definition; Mode 3 write is out of v1 scope. |
| **Why** | Audit charter and MARS survivability default; Run 5 SITE-001 is read-only. |
| **Consequence** | Validate halts on suspected write; [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md) defines behavior. |
| **Evidence** | [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md), [EAR-CHARTER-v1.md](EAR-CHARTER-v1.md) |

---

## D-2C-05 — Direct consumer access discouraged

| | |
|---|---|
| **Decision** | Consumers should **not** perform parallel live FTP/SSH/PMA for routine audit phases when a snapshot exists or is planned. |
| **Why** | Bypasses Validate/Publish gates; splits audit trail; increases credential exposure in consumer repos. |
| **Consequence** | OCPilot Run 5 resumes on **published snapshot**; live access only via separate operator charter if ever needed. |
| **Evidence** | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md), freeze blockers |

---

## D-2C-06 — Metadata-first levels 1–3

| | |
|---|---|
| **Decision** | Quality levels emphasize **manifests and inventories**, not full file/row payloads in the published package. |
| **Why** | Git safety, PII avoidance, storage cost; aligns with OCPilot baseline diff model. |
| **Consequence** | ZIP/SSH may produce large **external** bulk; package holds references + manifest. |
| **Evidence** | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) Level 3 note |

---

## D-2C-07 — Hybrid acquisition default for Level 2–3

| | |
|---|---|
| **Decision** | No single channel reliably delivers Level 3; **Hybrid** is the nominal path for full audit snapshots. |
| **Why** | Capability matrix shows Admin lacks manifest; PMA lacks files; Browser caps at 0. |
| **Consequence** | `acquisition-log` must enumerate channels; mismatch risks documented. |
| **Evidence** | [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md) matrix |

---

## D-2C-08 — Honest quality downgrades mandatory

| | |
|---|---|
| **Decision** | EAR must not Publish a level higher than Validate possession per [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md). |
| **Why** | Prevents false Run 5 resume and consumer phase halts mid-audit. |
| **Consequence** | `safe-unknown` preferred over silent omission. |
| **Evidence** | [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) |

---

## D-2C-09 — Nine-channel taxonomy frozen for OpenCart v1

| | |
|---|---|
| **Decision** | Standard channels: ZIP, SFTP, FTP, SSH, Hosting Panel, OpenCart Admin, phpMyAdmin, Browser, Hybrid. |
| **Why** | Covers SITE-001 access brief and foundation connection types; extensible via charter. |
| **Consequence** | WordPress-specific channels remain in [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) until WPilot Phase. |

---

## Deferred (not decisions — SAFE UNKNOWN)

| Topic | Phase |
|-------|-------|
| Connector implementation | 2D architecture |
| Automated Validate CLI | 4+ candidate |
| Credential vault product | 2D+ |
| Hybrid timestamp merge rules | Operator + future tooling |

---

## Cross-references

| Document | Use |
|----------|-----|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Phase status |
| [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md) | Phase 2D pointer |

# EAR Glossary v1

Terms frozen for EAR v1 documentation. Pilot-specific terms may extend but should not contradict these definitions.

---

## Core terms

| Term | Definition |
|------|------------|
| **EAR** | External Access Runtime — supervised access **acquisition** layer (documentation / future implementation). |
| **Snapshot** | Versioned **Snapshot Package** produced by EAR for consumers. |
| **Snapshot Package** | Structured evidence bundle per [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md). |
| **Consumer** | System that **reads** a snapshot and performs analysis (e.g. OCPilot). |
| **Operator** | Human with authority over hosting, credentials, and approval gates. |
| **HITL** | Human-in-the-loop — mandatory approval before connected acquisition. |
| **Acquisition** | Collecting evidence from external systems into a snapshot. |
| **Channel** | Access path (SFTP, SSH, admin UI, export file, etc.). |
| **Connector** | Future adapter mapping a channel to acquisition steps — **not claimed implemented** in v1. |
| **Mode** | Operational maturity level 0–3 per [EAR-MODES-v1.md](EAR-MODES-v1.md). |

---

## Mode shorthand

| Mode | Name |
|------|------|
| 0 | Manual |
| 1 | Assisted |
| 2 | Connected Read Only (**v1 target**) |
| 3 | Connected Read Write (**forbidden in v1**) |

---

## Snapshot sections

| Term | Definition |
|------|------------|
| **metadata** | Site id, URLs, environment, platform claims, timestamps. |
| **file-manifest** | Paths, sizes, hashes — or reference to external archive. |
| **extension-inventory** | Modules, plugins, ocMod list — platform-dependent. |
| **database-metadata** | Schema summary; not necessarily full SQL dump. |
| **access-log** | Human approvals, channel used, operator identity (non-secret). |
| **safe-unknown** | Explicit list of missing or unverified items. |

---

## Security terms

| Term | Definition |
|------|------------|
| **Secret reference** | Pointer to external `secrets/` or vault — never raw password in git. |
| **Read-only default** | No writes unless future Mode 3 charter — not v1. |
| **Rollback requirement** | For future write modes: documented restore path before any write class work. |

---

## Legacy / alias

| Term | Note |
|------|------|
| **Runtime Bridge** | Informal operator name for EAR-shaped layer before EAR naming freeze — same architectural slot as EAR. |

---

## SAFE UNKNOWN

- Official Russian translations for operator-facing UI — not fixed in v1 glossary.
- ISO registry codes for snapshot format version — use `v1` suffix in filenames until charter defines semver.

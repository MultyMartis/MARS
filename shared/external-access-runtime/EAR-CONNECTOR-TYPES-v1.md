# EAR Connector Types v1

**Purpose:** Catalog of **Mode 2 connector classes** — purpose, inputs, outputs, strengths, limitations, and maximum snapshot quality each can support.  
**Status:** architecture specification only — **no** implementation claimed.  
**Phase:** 2D  
**Relation:** Specializes [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) into connector-shaped adapters. Aligns with [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md) channels.

**Maximum snapshot quality:** Highest OpenCart package quality level (0–3 per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md)) a connector class can **contribute toward** when used alone with ideal scope and operator discipline. Final level requires EAR Validation + operator publish — connectors do not certify levels.

---

## Connector class summary

| Connector class | Channel basis | Typical max quality (alone) |
|-----------------|---------------|----------------------------|
| SFTP Connector | SFTP | Level 3 (files); L1–2 DB without second connector |
| FTP Connector | FTP / FTPS | Level 3 (files); same DB gap as SFTP |
| SSH Connector | SSH | Level 3 (files + DB metadata possible) |
| phpMyAdmin Export Connector | PMA export | L2–3 DB metadata; weak file-manifest alone |
| OpenCart Admin Connector | Admin UI | L2 extension/theme; weak file-manifest |
| ZIP Intake Connector | File archive | Level 3 (offline tree); stale vs live risk |
| Hosting Panel Connector | Panel | L1 environment; usually secondary |
| Browser Evidence Connector | Browser-only | Level 0–1; non-reproducible |
| Hybrid Coordinator | Multi-channel | Level 3 when combined scope complete |

---

## SFTP Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Live read-only recursive listing and selective download from remote file space |
| **Input** | Approved target host, port, username; scope (remote root prefix, exclude globs, max bytes); credential reference (external) |
| **Output** | Evidence Package: file listing, selective file blobs or external bulk refs, hashes, optional small version file reads |
| **Strengths** | Current live tree; selective download; standard on many hosts; strong `file-manifest` |
| **Limitations** | Chroot/symlink ambiguity; slow on large `image/`; no DB without another connector |
| **Maximum snapshot quality** | **L3** for file-backed sections; **L1** for `database-metadata` unless paired |

---

## FTP Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Same as SFTP where only FTP/FTPS is available |
| **Input** | Host, FTPS/plain policy, credentials ref, passive/active hint, path scope |
| **Output** | Same evidence classes as SFTP when listing succeeds |
| **Strengths** | Ubiquitous on legacy shared hosting |
| **Limitations** | Cleartext on plain FTP; fragile listings; firewall issues; often less reliable than SFTP |
| **Maximum snapshot quality** | **L3** files (quality reduced if listings incomplete — validation must record gaps) |

---

## SSH Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Read-only remote inspection: find, checksums, selective cat; optional read-only DB CLI |
| **Input** | Host, key or password ref, scope paths, optional DB read-only grant and table allowlist |
| **Output** | High-quality manifest; version file contents; optional `SHOW TABLES` / schema summaries |
| **Strengths** | Efficient manifests; can combine file + DB metadata in one supervised session |
| **Limitations** | Not on all shared hosts; high damage risk if scope violated; operator shell discipline required |
| **Maximum snapshot quality** | **L3** when DB read-only scope approved and executed; **L3** files |

---

## phpMyAdmin Export Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Ingest structure-only or metadata exports from PMA (operator-supervised browser export or future automated download of export file only) |
| **Input** | Export file path or drop ref; export type (structure-only vs full — full requires explicit charter); DB name scope |
| **Output** | Table list, engines, prefix, optional row counts; no live file tree |
| **Strengths** | Strong `database-metadata` without SSH |
| **Limitations** | Export size limits; PII risk if full dump; no file-manifest from PMA alone |
| **Maximum snapshot quality** | **L2–3** for `database-metadata`; **L0–1** for file sections without another connector |

---

## OpenCart Admin Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Read-only navigation of admin UI to capture extension lists, theme name, version strings, settings screenshots (evidence artifacts, not live API unless future charter) |
| **Input** | Admin URL pattern, session via operator; screen scope checklist; no save actions |
| **Output** | Structured lists, screenshots, optional exported admin reports if host provides read-only export |
| **Strengths** | Authoritative extension/theme claims; complements file scan |
| **Limitations** | Misclick risk; cache side effects; non-reproducible without screenshots; weak hashes |
| **Maximum snapshot quality** | **L2** for `extension-inventory`, `theme-info`, partial `metadata`; **L1** `file-manifest` without file connector |

---

## ZIP Intake Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Ingest operator- or backup-delivered archive into quarantine; inventory and extract for evidence (not republish to live host) |
| **Input** | Archive path (external bulk); expected root layout hint; redaction policy for `config.php` |
| **Output** | Offline file manifest, version files, extension/theme paths from tree |
| **Strengths** | No live session; works from backup only; strong offline **L3** file evidence |
| **Limitations** | Stale vs live; zip bombs; path traversal; secrets in config if not scrubbed |
| **Maximum snapshot quality** | **L3** files offline; **L0–1** DB unless export included in zip |

---

## Hosting Panel Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Capture panel-visible facts: PHP version, backup links, cron list, account labels (screenshot or panel export) |
| **Input** | Panel URL, operator session; download-only actions |
| **Output** | Environment signals, optional backup archive ref for ZIP Intake |
| **Strengths** | Deployment class and host context for `environment` |
| **Limitations** | Panel-specific; easy to trigger destructive actions if scope drifts — usually **secondary** |
| **Maximum snapshot quality** | **L1–2** for `environment`; rarely primary for OCPilot Run 5 alone |

---

## Browser Evidence Connector

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Mode 2 fallback when no file protocol — structured capture of read-only pages |
| **Input** | URL list, capture checklist, operator attestation |
| **Output** | Screenshots, optional printed PDFs, manual transcription blocks |
| **Strengths** | Works when only UI access exists |
| **Limitations** | Non-reproducible; no reliable manifest; OCR ambiguity |
| **Maximum snapshot quality** | **L0–1** — consumers must treat claims as weak until corroborated |

---

## Hybrid Coordinator

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Orchestrate multiple connector classes in one acquisition cycle under single HITL scope — merge evidence before validation |
| **Input** | Ordered connector plan (e.g. SFTP + PMA + Admin); shared `acquisition_id`; per-connector scope slices |
| **Output** | Combined Evidence Package or ordered package set with cross-references |
| **Strengths** | Reaches **L3** OpenCart snapshot when no single channel suffices |
| **Limitations** | Contradictory evidence risk; longer operator time; failure in one leg may block level |
| **Maximum snapshot quality** | **L3** when plan covers all required sections per [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) |

---

## Selection guidance (OpenCart)

| Need | Prefer |
|------|--------|
| Live file manifest L3 | SFTP or SSH |
| DB metadata without SSH | phpMyAdmin Export + file connector |
| Extension truth vs tree drift | OpenCart Admin + SFTP |
| Backup-only SITE | ZIP Intake |
| Minimum viable Run 5 | Hybrid or SFTP + Admin |

---

## SAFE UNKNOWN

- FTPS-only vs plain FTP policy at runtime — charter decision.
- OpenCart REST read-only endpoints — not assumed; Admin connector remains UI-oriented in v1.

---

## Non-goals

- Connector implementation, drivers, or protocol libraries in MARS repo at Phase 2D.

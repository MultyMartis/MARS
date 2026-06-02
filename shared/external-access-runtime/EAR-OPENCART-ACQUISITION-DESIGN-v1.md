# EAR OpenCart Acquisition Design v1

**Purpose:** Canonical **read-only acquisition design** for OpenCart / ocStore — how external evidence can be collected to produce Snapshot Levels 0–3.  
**Status:** architecture specification only — **no** code, runtime, connectors, scripts, automation, SSH/FTP implementation, or access execution.  
**Phase:** 2C — OpenCart Read-Only Acquisition Design  
**Supersedes in role:** channel semantics for acquisition; complements [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) (Phase 2B process).

**Source of truth:** All future Mode 2 connectors, runbooks, and operator guides for OpenCart acquisition must align with this document and its Phase 2C siblings.

---

## Architectural position

```
SITE (external, passive)
    ↓
Acquisition Channel(s) — human-operated, read-only
    ↓
Evidence artifacts (raw, external bulk)
    ↓
EAR Assemble (workflow Phase 2B — future Mode 2 assists only)
    ↓
OpenCart Snapshot Package (Phase 2A contract)
    ↓
Consumer (OCPilot, etc.)
```

Phase 2A defined **what** a snapshot contains ([EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md)).  
Phase 2B defined **how** evidence flows through Request → Archive ([EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md)).  
Phase 2C defines **which channels exist**, **what evidence each can yield**, and **which snapshot levels each channel can support** (alone or in combination).

---

## Design constraints (non-negotiable)

| Constraint | Meaning |
|------------|---------|
| **Read-only** | No writes to live SITE during acquisition; no install/uninstall, no SQL mutation, no file upload to host |
| **No runtime** | This phase does not implement connectors or execute access |
| **Metadata-first** | Levels 1–3 emphasize inventories and manifests; bulk file contents remain optional external references |
| **SAFE UNKNOWN** | Missing or unverified evidence must be explicit; channels do not imply completeness |
| **HITL** | Operator approves channel, scope, and publish; EAR documents and assembles — does not replace human authority |

---

## Acquisition channels

Each channel is a **class of human-operated evidence collection**. None are claimed implemented in MARS at Phase 2C freeze.

Cross-reference: [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) (foundation catalog), [shared/external-access-patterns/](../external-access-patterns/README.md) (human gates).

---

### 1. ZIP Archive

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Ingest a point-in-time file tree (or subtree) delivered as `.zip` / `.tar.gz` without live protocol access |
| **Evidence types available** | Full or partial file tree; version proof files (`index.php`, `admin/index.php`, `system/version.php`); `extension/` tree; `system/modification.xml` and ocMod storage paths; theme directories; `.htaccess`; `config.php` **structure** (operator must redact secrets before any git-bound copy) |
| **Advantages** | Offline analysis; repeatable manifest generation; no live credential session during EAR assembly; works when only backup exists |
| **Limitations** | Stale vs live site; may omit `storage/` or DB; zip bombs and path traversal risk; secrets may be embedded in `config.php` if not scrubbed |
| **Risks** | Wrong root inside archive; mixed environments (dev files in prod zip); incomplete exclusions documented |
| **SAFE UNKNOWN** | Virus scan policy; whether SITE backup zip includes full tree or admin-only export |

---

### 2. SFTP

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Live read-only recursive listing and selective download from host file space |
| **Evidence types available** | File manifest (paths, sizes, hashes); version proof files; theme and extension directory inventories; environment signals (PHP files, cron snippets if readable); partial `config.php` read with redaction |
| **Advantages** | Current live tree; selective download avoids full bulk in package; standard on many hosts |
| **Limitations** | Chroot may hide true root; symlinks; slow on large `image/` trees; credential handling external to git |
| **Risks** | Wrong remote root; downloading cache/session bulk; accidental write if client not read-only |
| **SAFE UNKNOWN** | Host-specific layout (e.g. Beget chroot) for any given SITE |

---

### 3. FTP (plain / FTPS)

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Legacy read-only file listing and download where SFTP unavailable |
| **Evidence types available** | Same class as SFTP when listing succeeds — file manifest, version files, extension/theme paths |
| **Advantages** | Ubiquitous on shared hosting |
| **Limitations** | Cleartext risk on plain FTP; fragile listings; passive/active firewall issues; often slower and less reliable than SFTP |
| **Risks** | Credential interception; incomplete listings interpreted as missing files |
| **SAFE UNKNOWN** | Whether MARS future implementation will support plain FTP or FTPS-only |

---

### 4. SSH

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Read-only remote inspection via shell: `find`, checksums, selective `cat` of small version files; optional read-only DB CLI |
| **Evidence types available** | High-quality file manifest; fast hash sweeps on `system/`, `catalog/`, `admin/`; environment (PHP version, disk); DB metadata via `mysql` read-only (`SHOW TABLES`, `information_schema`) if granted |
| **Advantages** | Efficient manifest generation; can combine file + DB metadata in one supervised session |
| **Limitations** | Not available on all shared hosts; high damage potential if operator runs destructive commands |
| **Risks** | Mistaken `rm`/`mv`; production shell access; keys in scripts |
| **SAFE UNKNOWN** | Whether a given SITE has SSH enabled and read-only DB user |

---

### 5. Hosting Panel

| Dimension | Detail |
|-----------|--------|
| **Purpose** | View or download backups, file manager listings, PHP version, cron lists, database tools UI — without direct protocol clients |
| **Evidence types available** | Backup download links (→ often feeds ZIP channel); file manager export; PHP/runtime environment metadata; sometimes one-click DB export |
| **Advantages** | Single UI for operators unfamiliar with SFTP; backup restore path visibility |
| **Limitations** | Non-reproducible unless exported; screenshots weak for manifest; panel actions may restart services |
| **Risks** | Wrong account/site; accidental restore or delete clicks; conflating panel backup date with live state |
| **SAFE UNKNOWN** | Beget-specific panel patterns for any SITE not documented in repo |

---

### 6. OpenCart Admin

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Read-only navigation of admin UI for version string, extension list, theme name, module settings **without** save/install |
| **Evidence types available** | Extension inventory (admin list); theme-info (active theme); partial metadata (version claim); SEO-related settings flags; ocMod/extension UI state where visible |
| **Advantages** | Authoritative for “what admin believes is installed”; no full file tree required for extension list |
| **Limitations** | Does not prove filesystem reality; cache refresh side effects; route differences ocStore vs OpenCart; no file manifest |
| **Risks** | Misclick install/uninstall/save; session on production; incomplete list if pagination not captured |
| **SAFE UNKNOWN** | ocStore 3.0.3.8 admin routes and extension screens for a given SITE |

---

### 7. phpMyAdmin Export

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Schema-level database evidence: table list, prefix, engines, structure-only export |
| **Evidence types available** | `database-metadata` (prefix, tables, counts); optional `oc_setting` keys for version markers **without row PII policy**; SEO table presence |
| **Advantages** | Direct schema truth; supports Level 1+ DB requirements |
| **Limitations** | Full dumps risk PII and secrets in `oc_setting`; export size limits; browser session security |
| **Risks** | Accidental import on wrong DB; downloading full data dump into git; GDPR exposure |
| **SAFE UNKNOWN** | Max export size; whether read-only DB user exists vs admin PMA login |

---

### 8. Browser Evidence

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Screenshots, copied text, storefront HTML view, public robots/sitemap — when no file or DB protocol available |
| **Evidence types available** | Environment class hints; public SEO URLs; version strings visible on storefront; admin login page pattern (no creds); weak extension/theme signals |
| **Advantages** | Minimal access footprint; Mode 0 fallback |
| **Limitations** | Low reproducibility; no reliable file manifest; cannot reach Level 3 alone |
| **Risks** | OCR/interpretation errors; stale screenshots; false confidence from marketing footers |
| **SAFE UNKNOWN** | Minimum browser evidence acceptable for version gate at Validate |

---

### 9. Hybrid Acquisition

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Combine channels in one acquisition cycle to cover gaps (recommended for Level 2–3) |
| **Evidence types available** | Union of participating channels; `acquisition-log` must list each channel and scope |
| **Advantages** | Fills single-channel gaps (e.g. SFTP manifest + PMA schema + Admin extension list) |
| **Limitations** | Version/timestamp mismatch across channels; higher operator burden; more SAFE UNKNOWN coordination |
| **Risks** | Inconsistent snapshots if file zip is old but DB export is new; duplicate conflicting claims in metadata |
| **SAFE UNKNOWN** | Maximum recommended channel count per cycle without formal merge rules — operator judgment + Validate gate |

---

## Acquisition capability matrix

**Legend:** YES = channel can reliably supply section data for snapshot assembly (with operator skill); PARTIAL = partial or claim-only without corroboration; NO = not obtainable from channel alone.

| Channel | Metadata | File Manifest | Theme Info | Extension Inventory | OCMOD Inventory | Database Metadata | SEO Structure | Environment | **Quality Level Max** |
|---------|----------|---------------|------------|---------------------|-----------------|-------------------|---------------|-------------|----------------------|
| **ZIP** | YES | YES | PARTIAL | PARTIAL | PARTIAL | NO | PARTIAL | PARTIAL | **2** (3 if manifest policy comprehensive + hybrid DB) |
| **SFTP** | PARTIAL | YES | PARTIAL | PARTIAL | PARTIAL | NO | PARTIAL | PARTIAL | **2** (3 with hybrid DB) |
| **FTP** | PARTIAL | YES | PARTIAL | PARTIAL | PARTIAL | NO | PARTIAL | PARTIAL | **2** (3 with hybrid DB) |
| **SSH** | PARTIAL | YES | PARTIAL | PARTIAL | PARTIAL | YES | PARTIAL | YES | **3** (with scope policy) |
| **Hosting** | PARTIAL | PARTIAL | NO | NO | NO | PARTIAL | NO | YES | **1** (2 if backup zip + listing) |
| **Admin** | YES | NO | YES | YES | PARTIAL | NO | PARTIAL | PARTIAL | **2** |
| **phpMyAdmin** | PARTIAL | NO | NO | NO | NO | YES | PARTIAL | NO | **1** (2 with hybrid files) |
| **Browser** | PARTIAL | NO | PARTIAL | NO | NO | NO | PARTIAL | PARTIAL | **0** |
| **Hybrid** | YES | YES | YES | YES | YES | YES | YES | YES | **3** (subject to scope + Validate) |

**Notes:**

- **Quality Level Max** is the highest level **theoretically achievable** if operator executes full read-only scope for that channel (or hybrid plan). Validate may still **downgrade** published level.
- **Browser** alone caps at Level 0 (identity claims only) unless corroborated — see [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md).
- Level 3 requires **comprehensive metadata coverage**, not necessarily full file contents in package ([EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md)).

---

## Channel selection guide (conceptual)

| Target level | Minimum channel strategy |
|--------------|-------------------------|
| **0** | Browser and/or operator declaration only |
| **1** | ZIP **or** SFTP/FTP/SSH (manifest subset) **+** phpMyAdmin **or** SAFE UNKNOWN for DB; theme via Admin or scan |
| **2** | Hybrid: file channel (ZIP/SFTP/SSH) **+** Admin extension list **or** deep file scan of `extension/` |
| **3** | Hybrid: SSH or SFTP comprehensive manifest **+** Admin and/or file scan for extensions/ocMod **+** PMA/SSH DB metadata |

Detailed paths: [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md).

---

## Relation to acquisition modes

| EAR mode | Typical channels |
|----------|------------------|
| **0 — Manual drop** | ZIP, Browser, operator-prepared exports |
| **1 — Guided evidence** | Any channel per checklist; operator executes |
| **2 — Connected read-only** | SFTP, FTP, SSH, PMA, Admin (future connectors assist — not Phase 2C) |

See [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md).

---

## Phase 2C document map

| Document | Role |
|----------|------|
| [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) | Canonical multi-channel paths to Levels 0–3 |
| [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md) | Per-channel risks and EAR behavior |
| [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) | Level requirements vs evidence possession |
| [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | Reference pilot options (example only) |
| [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md) | Pre-acquisition checklist |
| [EAR-OPENCART-DESIGN-DECISIONS-v1.md](EAR-OPENCART-DESIGN-DECISIONS-v1.md) | Phase 2C decisions |

---

## SAFE UNKNOWN (design-level)

- Automated channel merge rules and timestamp tolerance across hybrid sources — not defined.
- Formal hash algorithm enforcement tooling — recommended SHA-256, not implemented.
- Connector library choice and credential vault product — Phase 2D+.
- WordPress acquisition channel parity — out of scope for this document.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | Package sections and quality levels |
| [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) | Request → Archive |
| [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) | Foundation connection catalog |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |

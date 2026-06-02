# EAR Snapshot Mapping v1

**Purpose:** Map **snapshot sections** to **connector classes** — who can contribute, primary vs secondary roles.  
**Status:** architecture specification only — **no** implementation.  
**Phase:** 2D  
**Normative sections:** OpenCart package per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md). Generic contract sections per [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) where noted.

**Legend:** **P** = primary contributor (can fully populate section in ideal conditions); **S** = secondary (supplements or weak contribution); **—** = no meaningful contribution alone.

---

## Section: metadata

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | S | Version files support claims |
| FTP Connector | S | Same as SFTP |
| SSH Connector | S | Fast version file read |
| phpMyAdmin Export Connector | — | DB-only |
| OpenCart Admin Connector | P | Version strings, platform labels — corroborate required |
| ZIP Intake Connector | S | Offline version files |
| Hosting Panel Connector | S | PHP version, host labels |
| Browser Evidence Connector | S | Weak claims only |
| Hybrid Coordinator | P | Combines primaries |

**Validation rule:** Admin **P** claims must be corroborated for high quality levels — else `safe-unknown`.

---

## Section: file-manifest

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | P | Live manifest + hashes |
| FTP Connector | P | If listing complete |
| SSH Connector | P | find + checksum |
| phpMyAdmin Export Connector | — | |
| OpenCart Admin Connector | — | No tree |
| ZIP Intake Connector | P | Offline manifest |
| Hosting Panel Connector | — | |
| Browser Evidence Connector | — | |
| Hybrid Coordinator | P | Prefer SFTP/SSH/ZIP leg |

---

## Section: theme-info

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | P | `catalog/view/theme/` scan |
| FTP Connector | P | Same |
| SSH Connector | P | Same |
| phpMyAdmin Export Connector | — | |
| OpenCart Admin Connector | P | Active theme from admin |
| ZIP Intake Connector | P | Offline |
| Hosting Panel Connector | — | |
| Browser Evidence Connector | S | Screenshots only |
| Hybrid Coordinator | P | Admin + file corroboration |

---

## Section: extension-inventory

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | P | `extension/` tree |
| FTP Connector | P | |
| SSH Connector | P | |
| phpMyAdmin Export Connector | — | |
| OpenCart Admin Connector | P | Extension list UI |
| ZIP Intake Connector | P | |
| Hosting Panel Connector | — | |
| Browser Evidence Connector | S | Screenshots |
| Hybrid Coordinator | P | |

---

## Section: ocmod-inventory

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | P | `system/modification.xml`, storage paths |
| FTP Connector | P | |
| SSH Connector | P | |
| phpMyAdmin Export Connector | — | |
| OpenCart Admin Connector | S | May list modifications if UI exposes |
| ZIP Intake Connector | P | |
| Hosting Panel Connector | — | |
| Browser Evidence Connector | — | |
| Hybrid Coordinator | P | File leg required for L2+ |

---

## Section: database-metadata

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | — | Unless SQL files in tree |
| FTP Connector | — | |
| SSH Connector | P | Read-only CLI |
| phpMyAdmin Export Connector | P | Structure export |
| OpenCart Admin Connector | — | |
| ZIP Intake Connector | S | If sql dump in archive (charter) |
| Hosting Panel Connector | — | |
| Browser Evidence Connector | — | |
| Hybrid Coordinator | P | SSH or PMA leg |

---

## Section: seo-structure

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | P | `.htaccess`, `config.php` flags (redacted), robots |
| FTP Connector | P | |
| SSH Connector | P | |
| phpMyAdmin Export Connector | S | SEO-related tables metadata only |
| OpenCart Admin Connector | S | SEO extension screens |
| ZIP Intake Connector | P | |
| Hosting Panel Connector | — | |
| Browser Evidence Connector | S | Weak |
| Hybrid Coordinator | P | File leg primary |

---

## Section: environment

| Connector class | Role | Notes |
|-----------------|------|-------|
| SFTP Connector | S | Path layout signals |
| FTP Connector | S | |
| SSH Connector | S | `php -v`, paths |
| phpMyAdmin Export Connector | — | |
| OpenCart Admin Connector | — | |
| ZIP Intake Connector | S | May be stale |
| Hosting Panel Connector | P | PHP version, account type |
| Browser Evidence Connector | — | |
| Hybrid Coordinator | P | Operator declaration always **P** at validation |

**Note:** Operator-recorded environment class remains authoritative for halt rules; connectors supply **signals** only.

---

## Section: safe-unknown

| Connector class | Role | Notes |
|-----------------|------|-------|
| All connectors | S | Emit warnings → validation maps to entries |
| EAR Validation | P | Final authoritative list at publish |
| Hybrid Coordinator | S | Aggregates leg gaps |

Connectors do not **remove** `safe-unknown` entries — only validation after operator review.

---

## Section: acquisition-log (OpenCart) / access-log (generic)

| Connector class | Role | Notes |
|-----------------|------|-------|
| All connectors | S | Per-leg status in evidence |
| EAR Validation | P | Consolidated audit trail at publish |
| Operator | P | HITL approval ids |

Maps to generic `access-log` in [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md).

---

## Quality level hints (OpenCart)

| Target level | Typical connector plan |
|--------------|------------------------|
| **L0** | Browser Evidence or incomplete any |
| **L1** | Single file connector partial scope |
| **L2** | SFTP/ZIP + Admin or SSH without full DB |
| **L3** | Hybrid: file **P** (SFTP/SSH/ZIP) + DB **P** (SSH or PMA) + Admin **S** corroboration |

Connectors do not set `package_quality_level` — validation + operator do.

---

## Mapping matrix (compact)

| Section | SFTP | FTP | SSH | PMA | Admin | ZIP | Panel | Browser | Hybrid |
|---------|------|-----|-----|-----|-------|-----|-------|---------|--------|
| metadata | S | S | S | — | P | S | S | S | P |
| file-manifest | P | P | P | — | — | P | — | — | P |
| theme-info | P | P | P | — | P | P | — | S | P |
| extension-inventory | P | P | P | — | P | P | — | S | P |
| ocmod-inventory | P | P | P | — | S | P | — | — | P |
| database-metadata | — | — | P | P | — | S | — | — | P |
| seo-structure | P | P | P | S | S | P | — | S | P |
| environment | S | S | S | — | — | S | P | — | P |
| safe-unknown | S | S | S | S | S | S | S | S | S |
| acquisition-log | S | S | S | S | S | S | S | S | P |

---

## SAFE UNKNOWN

- WordPress snapshot section names at mapping — future WPilot phase.
- Unified cross-CMS mapping table — Phase 4 **SAFE UNKNOWN**.

---

## Non-goals

- Automated mapper implementation or section serializer.

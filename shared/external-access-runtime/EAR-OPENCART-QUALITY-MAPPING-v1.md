# EAR OpenCart Quality Mapping v1

**Purpose:** Map Snapshot Quality Levels **0–3** to **minimum acquisition requirements** — what EAR must possess (evidence in hand, validated) before claiming each level at Publish.  
**Status:** design only — **no** automated validator claimed.  
**Phase:** 2C  
**Normative level definitions:** [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md)

---

## Definitions

| Term | Meaning |
|------|---------|
| **Possess** | Evidence collected, assembled into candidate package, and accepted at Validate — not merely planned in Request |
| **Honest claim** | Published `quality_level` matches Validate outcome; gaps in `safe-unknown/` |
| **Corroborate** | Second source agrees (e.g. admin list + file scan) or filesystem proof exists |

---

## Level 0 — Identity only

### Minimum acquisition requirements

| Requirement | Evidence EAR must possess |
|-------------|---------------------------|
| Site identity | `site_id`, platform claim (may be operator declaration) |
| Package identity | `snapshot_id`, contract ids, `created_at`, `ear_mode` |
| Environment class | `environment/` with class or explicit `UNKNOWN` |
| Acquisition audit | `acquisition-log/` minimum: approver, mode, channel(s) or `declaration` |
| Honesty | `safe-unknown/` listing **all** sections not acquired |

### Channels typically sufficient

- Operator declaration (Path L0-A)
- Browser Evidence optional (Path L0-B)

### EAR must NOT claim before Publish

- Baseline diff capability
- Structural file proof
- Extension or ocMod analysis

---

## Level 1 — Identity + structure

### Minimum acquisition requirements (Level 0 plus)

| Section | EAR must possess |
|---------|------------------|
| **Version proof** | `Detected version` from version files **or** explicit `safe-unknown` with unblock for version-dependent work |
| **file-manifest** | Root folders (`admin/`, `catalog/`, `system/`, etc.) **and** file counts or path list covering version proof files |
| **database-metadata** | Table prefix + table list **or** section-level `safe-unknown` |
| **seo-structure** | SEO enabled flag / rewrite indicators **or** `safe-unknown` |
| **theme-info** | Active theme name **or** `safe-unknown` |

### Typical channel possession

| Evidence | Channels |
|----------|----------|
| File manifest subset | ZIP, SFTP, FTP, SSH |
| DB metadata | phpMyAdmin, SSH (read-only), or deferred |
| Theme name | OpenCart Admin, ZIP scan, or deferred |
| SEO flags | File scan (`.htaccess`, config patterns), Admin, or deferred |

### Validate gate (conceptual)

- If manifest cannot support version proof → **fail Level 1** → remain Level 0 or no Publish

---

## Level 2 — Identity + structure + extensions

### Minimum acquisition requirements (Level 1 plus)

| Section | EAR must possess |
|---------|------------------|
| **extension-inventory** | Installed extensions list (unknowns bucket allowed) |
| **ocmod-inventory** | Installed mods with enabled state **or** section-level `safe-unknown` |

### Typical channel possession

| Evidence | Channels |
|----------|----------|
| Extension list | OpenCart Admin + file scan corroboration **recommended** |
| ocMod state | ZIP/SFTP/SSH scan of modification storage + XML names |

### EAR must NOT claim Level 2 if

- Only admin screenshot without extension names parseable
- Only browser evidence of “plugins exist”

---

## Level 3 — Full read-only audit snapshot

### Minimum acquisition requirements (Level 2 plus)

| Section | EAR must possess |
|---------|------------------|
| **file-manifest** | Comprehensive path list per **acquisition scope policy** (exclusions documented in manifest metadata) |
| **extension-inventory** | Modules and integration indicators populated (residual unknowns allowed in bucket) |
| **ocmod-inventory** | Custom and unknown mods classified where possible |
| **database-metadata** | Extra/missing tables vs baseline indicators (not necessarily full schema dump in package) |
| **seo-structure** | Rewrite indicators + SEO extension cross-ref where applicable |
| **safe-unknown** | Only genuinely residual unknowns — not bulk missing sections |

### Typical channel possession

- **Hybrid** required in most real sites: SSH or SFTP comprehensive manifest + PMA/SSH DB + Admin corroboration ([EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) L3-A/B/C)

### Level 3 does NOT require

- Full file **contents** inside published package
- Database **row** data
- Live connector after Publish

---

## Possession vs publish claim matrix

| If EAR possesses only… | Max honest `quality_level` |
|------------------------|----------------------------|
| Declaration + browser | **0** |
| ZIP/SFTP manifest subset + version files, DB unknown | **1** (with DB safe-unknown) |
| Level 1 + extension list, ocMod partial | **2** (with ocMod safe-unknown) or **1** if extensions missing |
| Level 2 + comprehensive manifest + DB baseline indicators + residual safe-unknown only | **3** |

---

## Mode interaction

| Mode | Quality implication |
|------|---------------------|
| **0** | Can reach 1–3 if operator drops sufficient artifacts; possession = external bulk + assembled package |
| **1** | Same; guided checklist defines possession targets |
| **2** | Future connectors assist collection; **possession rules unchanged** |

---

## Partial snapshots and re-entry

| Scenario | Mapping rule |
|----------|--------------|
| `snap-…-p1` at Level 1 | OCPilot may consume; extension phases blocked |
| Scoped acquire for extensions only | Validate **p2** independently; may jump 1→2 without re-collecting entire tree if `prior snapshot reference` documents inheritance |
| Cannot inherit manifest | New comprehensive Acquire required for Level 3 |

---

## SAFE UNKNOWN

- Machine-readable validator for possession rules — not in-repo.
- Exact path count threshold for “comprehensive manifest” — defined per SITE charter / scope policy at Request, not global numeric limit in Phase 2C.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md) | Capability matrix |
| [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) | G4 publish gate |
| [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md) | Consumer phase gating |

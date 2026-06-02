# EAR OpenCart Snapshot Paths v1

**Purpose:** Canonical **acquisition paths** — which channel combinations can produce Snapshot Quality Levels 0–3.  
**Status:** design only — **no** execution, connectors, or access attempts.  
**Phase:** 2C  
**Parent:** [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md)

Paths are **conceptual recipes**. Operator must still pass [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md) and Phase 2B workflow gates.

---

## Path notation

```
[Channel A] + [Channel B] + …
    ↓
Assemble (EAR / operator — Mode 0–2)
    ↓
Validate (quality gates)
    ↓
Snapshot Level N (published claim)
```

**Re-entry:** A higher level may use a **scoped partial path** (e.g. extension-only) starting at Request with new `snapshot_id`.

---

## Level 0 paths

### Path L0-A — Declaration only

```
Operator declaration (site_id, platform claim, environment class)
    ↓
Snapshot Level 0
```

| Channels | None required |
|----------|----------------|
| Use case | Register acquisition intent; block consumer diff phases |
| Max honest level | **0** |

---

### Path L0-B — Browser corroboration

```
Browser Evidence (storefront/admin login page screenshots, public URLs)
    ↓
Snapshot Level 0
```

| Channels | Browser only |
|----------|----------------|
| Use case | No file protocol; existence proof for charter |
| Max honest level | **0** (may add metadata claims — not structural proof) |

---

## Level 1 paths

### Path L1-A — ZIP only

```
ZIP Archive (site root or agreed subtree)
    ↓
Manifest subset + version proof files from archive
    ↓
Snapshot Level 1
```

| Requirements | Root folders + version proof files in manifest; DB and theme via scan **or** `safe-unknown` |
| Gap handling | Missing DB → `database-metadata` safe-unknown; missing theme → `theme-info` safe-unknown |
| Max level alone | **1** (not 2 without extension/ocMod evidence) |

---

### Path L1-B — SFTP + metadata session

```
SFTP (list + download version proof + root folder inventory)
    ↓
Operator records environment + URLs in metadata
    ↓
Snapshot Level 1
```

| Optional add | phpMyAdmin Export for `database-metadata` |
|--------------|-------------------------------------------|
| Max level alone | **1** without DB channel |

---

### Path L1-C — FTP equivalent

Same as **L1-B** with FTP/FTPS instead of SFTP.

---

### Path L1-D — Hosting panel → ZIP

```
Hosting Panel (download file backup / export)
    ↓
ZIP Archive (extract externally)
    ↓
Snapshot Level 1
```

| Note | Backup date must be recorded in `acquisition-log`; stale backup → document in `safe-unknown` |
|------|----------------------------------------------------------------------------------------------|

---

### Path L1-E — Hybrid minimal (files + DB)

```
SFTP or ZIP  +  phpMyAdmin Export (structure only)
    ↓
Snapshot Level 1
```

| Strength | Satisfies DB prefix/table list without SSH |
|----------|---------------------------------------------|

---

### Path L1-F — Admin-assisted identity

```
OpenCart Admin (version, theme name)  +  Browser or partial ZIP
    ↓
Snapshot Level 1
```

| Caution | Admin claims require file corroboration for `Detected version` or explicit safe-unknown |
|---------|----------------------------------------------------------------------------------------|

---

## Level 2 paths

### Path L2-A — ZIP + Admin

```
ZIP Archive (extension/ + system/modification paths)
    +
OpenCart Admin (extension list, enabled modules)
    ↓
Snapshot Level 2
```

| ocMod | From ZIP scan and/or admin; unknowns → `safe-unknown` |
|-------|------------------------------------------------------|

---

### Path L2-B — SFTP + Admin

```
SFTP (full extension/ and catalog scan policy)
    +
OpenCart Admin (extension inventory corroboration)
    ↓
Snapshot Level 2
```

---

### Path L2-C — SSH file-only

```
SSH (find + hashes on system/, extension/, modification storage)
    ↓
Snapshot Level 2
```

| DB | Optional; Level 2 achievable without DB if Level 1 DB already in prior snapshot or safe-unknown documented |

---

### Path L2-D — Guided Mode 1 multi-drop

```
Operator drops: manifest text + admin screenshots/exports + PMA table list
    (no single protocol — Mode 1)
    ↓
Snapshot Level 2
```

| Aligns with | [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md) Mode 1 |

---

## Level 3 paths

### Path L3-A — SSH comprehensive (preferred future Mode 2)

```
SSH (comprehensive manifest per scope policy)
    +
SSH or phpMyAdmin (DB metadata + extra/missing table indicators)
    ↓
Snapshot Level 3
```

| Exclusions | Document cache/logs/sessions excluded in manifest policy |

---

### Path L3-B — SFTP + PMA + Admin (hybrid)

```
SFTP (comprehensive path list)
    +
phpMyAdmin Export (schema metadata)
    +
OpenCart Admin (extension + ocMod UI state)
    ↓
Snapshot Level 3
```

| Risk | Timestamp alignment — record acquisition window in `acquisition-log` |

---

### Path L3-C — ZIP (fresh full tree) + PMA + Admin

```
ZIP Archive (full scoped tree, recent)
    +
phpMyAdmin Export
    +
OpenCart Admin
    ↓
Snapshot Level 3
```

| When | SSH/SFTP unavailable but fresh panel backup exists |

---

### Path L3-D — Incremental from Level 2

```
Published snap-…-p1 at Level 2
    ↓
Request (scoped: ocmod-inventory + manifest expansion)
    ↓
SFTP or SSH (delta manifest policy)
    ↓
Validate
    ↓
snap-…-p2 at Level 3
```

| Pattern | Partial re-entry per [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) |

---

## Path selection matrix (quick reference)

| Path ID | Primary channels | Target level |
|---------|------------------|--------------|
| L0-A | Declaration | 0 |
| L0-B | Browser | 0 |
| L1-A | ZIP | 1 |
| L1-B | SFTP | 1 |
| L1-C | FTP | 1 |
| L1-D | Hosting → ZIP | 1 |
| L1-E | SFTP/ZIP + PMA | 1 |
| L1-F | Admin + partial files | 1 |
| L2-A | ZIP + Admin | 2 |
| L2-B | SFTP + Admin | 2 |
| L2-C | SSH | 2 |
| L2-D | Mode 1 multi-drop | 2 |
| L3-A | SSH + DB | 3 |
| L3-B | SFTP + PMA + Admin | 3 |
| L3-C | ZIP + PMA + Admin | 3 |
| L3-D | Incremental from L2 | 3 |

---

## Invalid paths (do not publish inflated level)

| Anti-pattern | Why |
|--------------|-----|
| Browser only → Level 1+ | No manifest |
| Admin only → Level 2+ | No filesystem corroboration for ocMod/file overrides |
| Stale ZIP + live PMA without note | Version/environment mismatch |
| PMA full row dump in git package | PII / secrets violation |
| Skip Validate after Acquire | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) |

---

## SAFE UNKNOWN

- Mandatory acquisition order when multiple channels used — operator-defined per Request.
- Whether Level 3 always requires fresh live manifest vs acceptable panel backup — charter per SITE.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) | Minimum evidence per level |
| [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md) | Hybrid mismatch risks |
| [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) | Validate / Publish gates |

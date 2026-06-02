# EAR Connected Paths v1

**Purpose:** Canonical **Connected Acquisition** paths — live read-only channel recipes mapped to **Snapshot Quality Levels 0–3**.  
**Status:** design only — **no** implementation, connectors, scripts, or access execution.  
**Phase:** 2E  
**Parent:** [EAR-CONNECTED-ACQUISITION-v1.md](EAR-CONNECTED-ACQUISITION-v1.md)

**Alignment:** Maps to [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) and [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md). Acquire stage assumes **Mode 2** and Phase 2D connector semantics when runtime exists.

---

## Path notation

```
[Connector / Channel A] + [Connector / Channel B] + …
    ↓
Evidence Package(s) — Hybrid Coordinator if multi-leg
    ↓
EAR Validate
    ↓
Snapshot Level N (published claim)
```

**HITL:** Operator approves target, scope, and `credential_ref` before Acquire.

---

## Level 0 paths (connected-eligible but minimal)

### CON-L0-A — Browser connector only

```
Browser Evidence connector (public / login page capture)
    ↓
Snapshot Level 0
```

| Use | Charter registration before file channels approved |
| Maps to OpenCart | Path L0-B |

---

## Level 1 paths

### CON-L1-A — SFTP read-only

```
SFTP Connector (list + download version proof + root inventory)
    ↓
Evidence Package
    ↓
Snapshot Level 1
```

| Optional | PMA connector for `database-metadata` → stronger L1 |
| Maps to OpenCart | Path L1-B |

---

### CON-L1-B — SSH file-only (narrow)

```
SSH Connector (scoped find/list per charter)
    ↓
Snapshot Level 1
```

| Maps to OpenCart | Path L1-B variant (SSH instead of SFTP) |

---

### CON-L1-C — SFTP + PMA metadata

```
SFTP Connector
    +
phpMyAdmin Metadata Connector (structure export, table list)
    ↓
Snapshot Level 1 (strong)
```

| Maps to OpenCart | Path L1-E |

---

### CON-L1-D — Admin read + corroboration

```
OpenCart Admin Read Connector (version, theme identity)
    +
SFTP or Browser corroboration
    ↓
Snapshot Level 1
```

| Maps to OpenCart | Path L1-F |
| Caution | Admin claims require file corroboration or safe-unknown |

---

## Level 2 paths

### CON-L2-A — SFTP + Admin

```
SFTP Connector (extension/, modification paths)
    +
OpenCart Admin Read Connector
    ↓
Snapshot Level 2
```

| Maps to OpenCart | Path L2-B |

---

### CON-L2-B — SSH extension scan

```
SSH Connector (extension + modification storage policy)
    ↓
Snapshot Level 2
```

| Maps to OpenCart | Path L2-C |
| DB | Optional if prior snapshot or safe-unknown documents gap |

---

### CON-L2-C — ZIP intake connector (connected semantics)

```
ZIP Intake Connector (operator-triggered staging on approved storage)
    ↓
Treated as connected session with acquisition-log
    ↓
Snapshot Level 2
```

| Note | **SAFE UNKNOWN** whether first runtime pilot uses ZIP Intake vs SFTP — Phase 3 charter |
| Use | Bridge when host only allows panel→staging but session is EAR-governed |

---

## Level 3 paths

### CON-L3-A — SSH comprehensive

```
SSH Connector (comprehensive manifest per scope policy)
    +
SSH or PMA (DB metadata + table indicators)
    ↓
Snapshot Level 3
```

| Maps to OpenCart | Path L3-A |
| Preferred | When SSH fully available and chartered |

---

### CON-L3-B — SFTP + PMA + Admin (hybrid coordinator)

```
SFTP Connector (comprehensive path list)
    +
phpMyAdmin Metadata Connector
    +
OpenCart Admin Read Connector
    ↓
Hybrid Coordinator merges evidence
    ↓
Snapshot Level 3
```

| Maps to OpenCart | Path L3-B |
| SITE-001 | Theoretical target when all channels confirmed — [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) |

---

### CON-L3-C — SSH hybrid (file + DB legs)

```
SSH comprehensive file leg
    +
PMA or SSH DB metadata leg
    ↓
Snapshot Level 3
```

| Maps to OpenCart | Path L3-C |

---

## Special connected patterns

### CON-S1 — Scoped partial re-acquisition

```
Prior published snapshot Level 1
    ↓
Request: scope = extension-inventory only
    ↓
Admin + SFTP connectors (narrow)
    ↓
New snapshot_id Level 2
```

| Use | OCPilot Run 5 extension pass after baseline |

---

### CON-S2 — SSH hybrid operations (read-only)

```
SSH Connector primary
    +
SFTP fallback connector (charter defines precedence)
    ↓
Single Hybrid Coordinator plan
    ↓
Snapshot Level 2–3
```

| Label | **SSH Hybrid** — one coordinator, multiple connector classes |
| Write | **Forbidden** — read-only only |

---

### CON-S3 — Recurring connected snapshot

```
Charter: quarterly read-only audit
    ↓
Repeat CON-L3-B (or narrowed CON-L1-A) per schedule with HITL each cycle
    ↓
New snapshot_id per cycle
```

| Automation | Unattended schedule **not** v1 architecture default |

---

## Future connected channels (architecture placeholders)

| Channel | Consumer context | Status |
|---------|------------------|--------|
| WordPress Admin read | WPilot | **SAFE UNKNOWN** — connector class TBD |
| REST read-only API | Future CMS pilots | Not in v1 |
| Hosting panel API | Factory scale | **SAFE UNKNOWN** |

---

## Path → level summary

| Path ID | Connector mix | Typical max level |
|---------|---------------|-------------------|
| CON-L0-A | Browser | 0 |
| CON-L1-A | SFTP | 1 |
| CON-L1-B | SSH narrow | 1 |
| CON-L1-C | SFTP + PMA | 1 (strong) |
| CON-L1-D | Admin + corroboration | 1 |
| CON-L2-A | SFTP + Admin | 2 |
| CON-L2-B | SSH extension | 2 |
| CON-L2-C | ZIP intake (connected) | 2 |
| CON-L3-A | SSH comprehensive | 3 |
| CON-L3-B | SFTP + PMA + Admin | 3 |
| CON-L3-C | SSH hybrid DB+file | 3 |
| CON-S1 | Scoped partial | 2 (typical) |
| CON-S2 | SSH + SFTP hybrid | 2–3 |
| CON-S3 | Recurring | 1–3 per charter |

---

## Connector failure interaction

Partial legs use `partial` status per [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md). Publish at degraded level only with operator acceptance — or trigger Offline hybrid gap fill (OFF-S3).

---

## SAFE UNKNOWN

- FTP/FTPS vs SFTP preference per host — operator Request.
- First implemented path for Phase 3 pilot — assessment output.
- WordPress connected path catalog — future WPilot phase.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md) | Reference sequence diagram |
| [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) | Section mapping |
| [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md) | Layer model |

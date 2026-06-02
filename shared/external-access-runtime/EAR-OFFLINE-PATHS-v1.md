# EAR Offline Paths v1

**Purpose:** Canonical **Offline Acquisition** paths — archive-first recipes mapped to **Snapshot Quality Levels 0–3**.  
**Status:** design only — **no** implementation, scripts, or access execution.  
**Phase:** 2E  
**Parent:** [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md)

**Alignment:** OpenCart paths L0–L3 that do not require live connectors align with [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md). This document names **track-specific** offline recipes for cross-platform use.

---

## Path notation

```
[Offline input A] + [Offline input B] + …
    ↓
Operator deliver → EAR Intake (Mode 0/1)
    ↓
Validate
    ↓
Snapshot Level N (published claim)
```

**Re-entry:** Higher levels may use scoped partial drops with new `snapshot_id`.

---

## Level 0 paths

### OFF-L0-A — Declaration only

```
Operator declaration (site_id, platform, environment)
    ↓
Snapshot Level 0
```

| Inputs | None required |
| Max level | **0** |

---

### OFF-L0-B — Browser corroboration (no archive)

```
Browser evidence (public URLs, login page screenshots)
    ↓
Snapshot Level 0
```

| Use | Charter existence; block consumer diff until Level 1+ |

---

## Level 1 paths

### OFF-L1-A — ZIP only

```
Site archive (ZIP of web root or agreed subtree)
    ↓
Manifest subset + version proof from archive scan
    ↓
Snapshot Level 1
```

| Gap handling | Missing DB → `database-metadata` safe-unknown |
| Maps to OpenCart | Path L1-A |

---

### OFF-L1-B — ZIP + DB dump

```
Site archive (ZIP)
    +
Database archive (structure-only SQL or table list export)
    ↓
Snapshot Level 1 (strong)
```

| Maps to OpenCart | Path L1-A + L1-E (offline variant) |
| Caution | Full row dumps discouraged for v1 contract |

---

### OFF-L1-C — Hosting panel export → ZIP

```
Hosting panel backup download (operator)
    ↓
Extract / verify externally
    ↓
EAR intake as OFF-L1-A or OFF-L1-B
    ↓
Snapshot Level 1
```

| Maps to OpenCart | Path L1-D |
| `acquisition-log` | Record backup job date; unknown date → safe-unknown |

---

### OFF-L1-D — Multi-file guided drop (Mode 1)

```
EAR artifact checklist
    → Operator drops: partial ZIP + PMA export file + screenshots
    ↓
Snapshot Level 1
```

| Maps to OpenCart | Path L1-F, Mode 1 |
| Partial common | Honest safe-unknown entries |

---

## Level 2 paths

### OFF-L2-A — ZIP + admin corroboration package

```
Site archive (extension/, modification paths present)
    +
Admin exports / screenshots (extension list, ocMod UI)
    ↓
Snapshot Level 2
```

| Maps to OpenCart | Path L2-A |

---

### OFF-L2-B — Dual archive (site + extension-focused)

```
Full site ZIP
    +
Supplementary extension inventory file (operator-prepared)
    ↓
Snapshot Level 2
```

| Use | Large sites where single ZIP omits agreed paths |

---

### OFF-L2-C — Guided Mode 1 comprehensive drop

```
Operator fulfills Level 2 checklist (no live connector)
    ↓
Snapshot Level 2
```

| Maps to OpenCart | Path L2-D |

---

## Level 3 paths

### OFF-L3-A — Comprehensive offline package (rare)

```
Site archive (full scoped tree per manifest policy)
    +
Database structure export (complete table list + prefix)
    +
Admin + theme/SEO corroboration drops
    +
Operator-prepared machine-readable manifest (if chartered)
    ↓
Snapshot Level 3
```

| Honesty | Level 3 offline is **rare** — operator must prove manifest policy equivalent to connected comprehensive path |
| Maps to OpenCart | Theoretical; compare L3-C offline preparation |

**Default expectation:** Offline engagements most often publish **Level 0–2**; Level 3 offline requires explicit charter and validation rigor.

---

## Special offline patterns

### OFF-S1 — Archive refresh

```
Prior snapshot (any level) exists
    ↓
Operator delivers NEW site archive (+ optional new DB dump)
    ↓
New snapshot_id — Validate — Publish
    ↓
Consumer compares if chartered
```

| Use | Stale backup replacement; not live delta sync |

---

### OFF-S2 — Multi-archive compare (documentation)

```
Snapshot A from archive dated D1
    +
Snapshot B from archive dated D2
    ↓
Consumer diff (OCPilot) — two published snapshots
```

| EAR role | Two separate acquisitions; EAR does not merge archives in v1 |

---

### OFF-S3 — Archive-only gap fill (Hybrid leg)

```
Connected acquisition partial (e.g. missing DB metadata)
    ↓
Operator delivers PMA export file (offline leg)
    ↓
New snapshot or scoped partial — charter defines
```

| Track | **Hybrid** — see [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) |

---

## Path → level summary

| Path ID | Primary inputs | Typical max level |
|---------|----------------|-------------------|
| OFF-L0-A/B | Declaration / browser | 0 |
| OFF-L1-A | ZIP only | 1 |
| OFF-L1-B | ZIP + DB | 1 |
| OFF-L1-C | Panel → ZIP | 1 |
| OFF-L1-D | Guided drops | 1 |
| OFF-L2-A/B/C | Archives + admin/inventory | 2 |
| OFF-L3-A | Comprehensive offline package | 3 (rare) |
| OFF-S1 | Archive refresh | 1–3 (depends on package) |
| OFF-S2 | Multi-archive compare | N/A (two snapshots) |
| OFF-S3 | Hybrid gap fill | Completes partial connected |

---

## Validation reminders

- Paths state **ceiling** — Validate may **downgrade** published level.
- Missing sections → **`safe-unknown`** — no inflation.
- Mode **0** or **1** only on Acquire stage.

---

## SAFE UNKNOWN

- Standard naming for operator drop folders — not frozen.
- Whether OFF-L3-A is allowed for SITE-001 without connected leg — operator charter.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) | OpenCart channel path detail |
| [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) | Minimum evidence per level |
| [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) | Lifecycle gates |

# EAR SITE-001 Acquisition Options v1

**Purpose:** Evaluate **theoretical** acquisition channels and achievable snapshot levels for **SITE-001** only — example pilot, **not** execution.  
**Status:** documentation analysis — **no** access attempts, credentials, or live host verification.  
**Phase:** 2C

**Facts source:** Repository documents only — primarily [projects/ocpilot/sites/site-001/project-access-brief.md](../../projects/ocpilot/sites/site-001/project-access-brief.md), [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md), [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/).

---

## SITE-001 identity (repository facts)

| Field | Value (from repo) |
|-------|-------------------|
| `site_id` | `SITE-001` |
| Name | Автосалон СИБКАР |
| Platform | ocStore 3.0.3.8 (rs.2) |
| Baseline | `ocstore-3038-rs2` |
| Environment | **TEST** (declared) |
| Test URL | `https://sibcar.new-site.space/` |
| Consumer | OCPilot Run 5 (read-only audit chartered; **paused** pending acquisition path) |
| Hosting context | Beget referenced (backup location) — **panel patterns not documented in repo** |

---

## Theoretically available channels

Per access brief, access types marked **Available: YES** (credentials location and Run 5 channel use remain **SAFE UNKNOWN**):

| Channel | Theoretically available? | Repo evidence | Run 5 execution |
|---------|-------------------------|---------------|-----------------|
| **Hosting Panel** | YES (claimed) | project-access-brief | **Not confirmed** — operator must confirm |
| **FTP / SFTP** | YES (claimed) | project-access-brief | **Not confirmed** |
| **SSH** | YES (claimed) | project-access-brief | **Not confirmed** |
| **phpMyAdmin** | YES (claimed) | project-access-brief | **Not confirmed** |
| **OpenCart Admin** | YES (claimed) | project-access-brief | **Not confirmed** |
| **ZIP Archive** | YES (via backup/export) | Backup YES, Beget backup 31.05.2026 | **Not verified** — backup contents unknown |
| **Browser Evidence** | YES (public test URL) | Test URL in passport/brief | Usable without creds for **Level 0** signals only |
| **Hybrid** | YES (combination of above) | Logical if operator confirms channels | Recommended for Level 2–3 **when** channels confirmed |

**Not in repo:** SFTP vs FTP preference; SSH enabled on account; admin URL path; PMA URL; whether backup zip is full tree.

---

## Theoretically achievable snapshot levels

| Level | Achievable in theory? | Preconditions (no execution assumed) |
|-------|----------------------|--------------------------------------|
| **0** | **YES** | Operator declaration + browser screenshots of test URL |
| **1** | **YES** | File manifest path (ZIP from Beget backup **or** SFTP/FTP/SSH after operator confirms) + DB table list (PMA **or** safe-unknown) + theme/SEO per path L1-A/E |
| **2** | **YES** | Level 1 possession + extension inventory (Admin + file scan) per path L2-A/B |
| **3** | **YES (conditional)** | Hybrid L3-B/C: comprehensive manifest + PMA metadata + Admin; requires confirmed channels and fresh consistent evidence |

**OCPilot Run 5 minimum (documented elsewhere):** Level **1+** with `file-manifest` minimum before structural audit resume — see freeze blockers and [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md).

---

## Recommended theoretical paths for SITE-001

### Path SITE-001-1 (Run 5 resume — aligns with workflow example)

```
Mode 1 Guided Evidence
    → ZIP from Beget backup OR SFTP (operator confirms)
    → phpMyAdmin table list (or safe-unknown)
    → Path L1-A or L1-E
    → Snapshot Level 1
```

| Matches | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) |
|---------|-----------------------------------------------------------------------------|

### Path SITE-001-2 (extension gap closure)

```
After Level 1 published
    → Request scoped: extension-inventory + ocmod-inventory
    → Admin + SFTP/ZIP corroboration
    → Path L2-A or L2-D
    → Snapshot Level 2
```

### Path SITE-001-3 (full audit snapshot — future)

```
Hybrid L3-B
    SFTP manifest + PMA schema metadata + Admin extension/ocMod UI
    → Snapshot Level 3
```

**Requires:** Operator confirms all channels read-only; TEST environment re-verified at Request.

---

## Additional evidence required (by target level)

| Target | Additional evidence beyond prior level |
|--------|----------------------------------------|
| **1** | Version proof files in manifest; root folder inventory; DB prefix/tables or honest safe-unknown; theme name or safe-unknown; SEO flag or safe-unknown |
| **2** | Extension list; ocMod inventory or safe-unknown |
| **3** | Comprehensive manifest per scope policy; DB extra/missing table indicators vs baseline; corroborated extension/integration indicators; residual-only safe-unknown |

### SITE-001-specific gaps (from freeze / Run 5 docs)

| Gap | Evidence needed | Suggested channel |
|-----|-----------------|-------------------|
| No published snapshot yet | First `snapshot_id` package | Mode 0/1 per operator choice |
| `file-manifest` blocker for Run 5 | Manifest file or SFTP listing | ZIP backup export, SFTP, or SSH |
| ocMod unknown in example | ocmod-inventory section | ZIP scan or Admin + SFTP |
| Channel confirmation (P3-C) | Written operator record in Request | Not EAR-automated |

---

## What this document does not assume

| Item | Status |
|------|--------|
| Credentials exist or work | **SAFE UNKNOWN** |
| Beget backup contains full OpenCart tree | **SAFE UNKNOWN** |
| SSH enabled | **SAFE UNKNOWN** |
| Admin URL | **SAFE UNKNOWN** |
| SFTP vs FTP | **SAFE UNKNOWN** |
| First publish Mode 0 vs 1 | Operator choice |

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) | Path IDs L1-A – L3-D |
| [projects/ocpilot/freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) | Blockers B-EV-* |
| [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md) | Pre-acquisition gates |

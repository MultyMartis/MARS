# MARS Localhost Infrastructure — Identity v1

**Document type:** Infrastructure identity record  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00  
**Operator decision:** Approved — dual-zone model (C: brain / D: runtime)

---

## Canonical identity

| Field | Value |
|-------|-------|
| **Canonical name** | MARS Localhost Infrastructure |
| **Operator name** | MLI |
| **Class** | Shared local development infrastructure |
| **Lifecycle** | FOUNDATION |
| **Runtime class** | Local operator-controlled web runtime |
| **Host OS** | Windows |
| **Canonical brain root** | `C:\AI MARS` |
| **Canonical runtime root** | `D:\MARS-Localhost` |
| **Production authority** | NONE |
| **Client production access** | NONE |

---

## Mandatory formulation

```text
MARS Localhost Infrastructure is an execution environment.
It is not the MARS brain, governance source, project registry or Git authority.
```

---

## Purpose

Provide a **shared**, **operator-controlled**, **Windows-local** web execution surface for MARS systems that require PHP, MariaDB/MySQL, Apache/Nginx, CMS runtimes, synthetic validation sites, and generic PHP simulations — without placing runtime state in the MARS git repository or conflating execution with governance.

---

## Physical boundaries

| Zone | Path | Authority |
|------|------|-----------|
| **Brain** | `C:\AI MARS` | Governance, architecture, manifests, pointers, reports, Git SoT |
| **Runtime** | `D:\MARS-Localhost` | Live servers, CMS cores, DB data, uploads, caches, logs, runtime backups |
| **Bulk support** | `C:\AI MARS STORAGE` | Optional large artefacts (dumps archives, release ZIPs, visual baselines) — **not** canonical runtime root |

**Canonical principle:**

```text
C:\AI MARS governs.
D:\MARS-Localhost executes.
```

---

## Consumers

| Consumer | Relationship |
|----------|--------------|
| **Forge WordPress** | Consumes WordPress runtime profile (synthetic, projects, sandboxes) |
| **OCPilot** | May consume OpenCart/ocStore runtime profile (planned; no migration in MLI-00) |
| **Website Factory** | May supply frontend packages; does **not** own PHP runtime |
| **WPilot** | May accept verified WordPress packages or work with registered DEV; does **not** own localhost infra |
| **Future consumers** | Generic PHP agents, migration simulators, API/webhook tests |

Consumers **use** MLI; they **do not own** `D:\MARS-Localhost`.

---

## Exclusions

MLI is **not**:

| Exclusion | Notes |
|-----------|-------|
| MARS brain / governance root | Stays on `C:\AI MARS` |
| Second MARS git repository | `D:\MARS-Localhost` is outside Git |
| **MARS STORAGE** | Bulk layer only; see [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md) |
| **Website Factory** program pack | Factory methodology lives under `projects/mars-website-factory/` |
| **Forge WordPress** subsystem | Implementation methodology; consumes MLI WordPress profile |
| **WPilot** | Remote DEV/production operations reference |
| **OCPilot** program | OpenCart operational pack; separate identity |
| Production hosting | No production authority |
| Remote DEV hosting | Beget-class hosts remain external |
| Registered MARS agent | No `agents/registry.md` entry |
| Client project lifecycle | Not a client delivery entity |

---

## Lifecycle

| Stage | Meaning |
|-------|---------|
| **FOUNDATION** (current) | Architecture, boundaries, directory standard, policies documented; empty safe D: tree |
| **ENABLEMENT** (MLI-01+) | Operator-controlled Laragon install and toolchain |
| **PROFILE VALIDATION** (MLI-03/04) | Evidence that WordPress/OpenCart profiles work |
| **OPERATIONAL** (future) | Only after profile validation — **not** claimed in MLI-00 |

---

## Production boundary

- **No** production endpoints as defaults
- **No** production database connections by default
- **No** production credentials in MARS docs or Git
- **No** reuse of production domains for local URLs (see domain standard)

---

## Relations

### MARS brain (`C:\AI MARS`)

- Stores identity, standards, runtime manifest **pointers**, enablement inputs, validation reports
- Remains Git source of truth
- Must **not** host permanent WordPress/OpenCart cores, live DB data, or large runtime logs

### MARS STORAGE (`C:\AI MARS STORAGE`)

- Optional consumer for **archived** dumps, release packages, visual baselines
- Example: `C:\AI MARS STORAGE\forge-wordpress\{FP-ID}\` for bulk artefacts
- **Not** a substitute for `D:\MARS-Localhost` live runtime

### Hosting (external)

- Production and registered DEV (e.g. WPilot Beget DEV) remain **outside** MLI
- MLI is **local-only** execution infrastructure

### Cursor

- Cursor tasks run from `C:\AI MARS` workspace
- May reference `D:\MARS-Localhost` paths in manifests and operator tasks
- Service start/stop only via approved operator commands (see service control policy)
- Cursor does **not** gain production access through MLI

---

## Placement

| Item | Path |
|------|------|
| Program root | [projects/mars-localhost-infrastructure/](.) |
| Runtime root | `D:\MARS-Localhost\` |
| Runtime manifests (brain) | [manifests/](manifests/) |

---

## Related

- [MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md](MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md)
- [MARS-LOCALHOST-CONSUMER-MODEL-v1.md](MARS-LOCALHOST-CONSUMER-MODEL-v1.md)
- [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md)

---

*Identity v1 — MLI-00 foundation.*

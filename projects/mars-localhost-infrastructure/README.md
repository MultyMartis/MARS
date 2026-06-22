# MARS Localhost Infrastructure

**Canonical name:** MARS Localhost Infrastructure  
**Operator alias:** MLI  
**Class:** Shared local development infrastructure  
**Lifecycle:** FOUNDATION  
**Status:** MLI-00 **COMPLETE** — MLI-01 **NEXT** (Laragon enablement; **not** executed in MLI-00)

---

## Principle

```text
C:\AI MARS governs.
D:\MARS-Localhost executes.
```

MARS Localhost Infrastructure is an **execution environment**. It is **not** the MARS brain, governance source, project registry, or Git authority.

---

## Physical boundaries

| Zone | Path | Role |
|------|------|------|
| **Brain** | `C:\AI MARS` | Governance, manifests, pointers, validation reports (Git) |
| **Runtime** | `D:\MARS-Localhost` | Local web stack, CMS runtimes, databases, uploads, caches, logs (**outside Git**) |
| **Bulk (optional)** | `C:\AI MARS STORAGE` | Large archives, release packages, visual baselines — **not** live runtime root |

---

## Entry points

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub |
| [roadmap.md](roadmap.md) | MLI-00 … MLI-06 stages |
| [MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md](MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md) | Identity and exclusions |
| [MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md](MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md) | C:/D: contract |
| [reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md) | Next authorized stage input |

---

## Consumers (do not own MLI)

- **Forge WordPress** — WordPress runtime profile
- **OCPilot** — OpenCart/ocStore runtime profile (planned consumption)
- **Website Factory** — frontend packages only; no PHP runtime ownership
- **WPilot** — may consume verified packages or registered DEV; no localhost ownership

---

## Honesty

- **Not** a MARS git repository
- **Not** production hosting
- **Not** operational until MLI-03/MLI-04 profile validation evidence exists
- Laragon **not** installed by MLI-00

---

*MLI foundation — operator-approved 2026-06-22.*

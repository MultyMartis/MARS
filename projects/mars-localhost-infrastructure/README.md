# MARS Localhost Infrastructure

**Canonical name:** MARS Localhost Infrastructure  
**Operator alias:** MLI  
**Class:** Shared local development infrastructure  
**Lifecycle:** ENABLEMENT  
**Status:** MLI-01 **COMPLETE** — MLI-02 **NEXT**

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
| **Runtime** | `D:\MARS-Localhost` | Laragon, CMS sites, databases, uploads, logs (**outside Git**) |
| **Bulk (optional)** | `C:\AI MARS STORAGE` | Large archives — **not** live runtime root |

---

## Laragon (MLI-01)

| Item | Path |
|------|------|
| **Laragon root** | `D:\MARS-Localhost\laragon` |
| **Sites** | `D:\MARS-Localhost\sites` |
| **CLI activation** | `D:\MARS-Localhost\tools\activate-mli.cmd` |
| **Smoke URL** | `http://mli-smoke-001.test/` |

---

## Entry points

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub |
| [roadmap.md](roadmap.md) | MLI-00 … MLI-06 stages |
| [MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md](MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md) | Canonical Laragon path |
| [reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md) | Next stage input |

---

## Consumers (do not own MLI)

- **Forge WordPress** — WordPress runtime consumer
- **OCPilot** — OpenCart runtime consumer (planned)
- **Website Factory** — frontend packages only

---

## Honesty

- **Not** a MARS git repository
- **Not** production hosting
- **Not** CMS-profile operational until MLI-03/MLI-04
- Laragon **enabled** MLI-01; WordPress/OpenCart sites **not** created in MLI-01

---

*MLI — MLI-01 complete.*

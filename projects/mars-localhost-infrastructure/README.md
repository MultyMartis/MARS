# MARS Localhost Infrastructure

**Canonical name:** MARS Localhost Infrastructure  
**Operator alias:** MLI  
**Class:** Shared local development infrastructure  
**Lifecycle:** ENABLEMENT  
**Status:** MLI-02 **COMPLETE** — MLI-03 **NEXT**

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

## Laragon (MLI-01+)

| Item | Path |
|------|------|
| **Laragon root** | `D:\MARS-Localhost\laragon` |
| **Sites** | `D:\MARS-Localhost\sites` |
| **CLI activation** | `D:\MARS-Localhost\tools\activate-mli.cmd` |
| **Hosts scripts** | `D:\MARS-Localhost\tools\hosts\` |
| **Smoke URL** | `http://mli-smoke-001.test/` (hosts elevation may be required) |
| **HTTPS smoke** | `https://mli-smoke-001.test/` (self-signed; see MLI-02 HTTPS report) |

---

## Entry points

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub |
| [roadmap.md](roadmap.md) | MLI-00 … MLI-06 stages |
| [registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md](registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md) | Tool versions |
| [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md) | Next stage input |

---

## Consumers (do not own MLI)

- **Forge WordPress** — WordPress runtime consumer (profile MLI-03)
- **OCPilot** — OpenCart runtime consumer (planned MLI-04)
- **Website Factory** — frontend packages only

---

## Honesty

- **Not** a MARS git repository on D:
- **Not** production hosting
- **Not** WordPress/OpenCart operational until MLI-03/MLI-04
- Shared toolchain **hardened** MLI-02; CMS profiles **not** created

---

*MLI — MLI-02 complete.*

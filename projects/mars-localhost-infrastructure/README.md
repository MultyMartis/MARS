# MARS Localhost Infrastructure

**Canonical name:** MARS Localhost Infrastructure  
**Operator alias:** MLI  
**Class:** Shared local development infrastructure  
**Lifecycle:** ENABLEMENT  
**Status:** MLI-03 **COMPLETE**

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
| **Hosts scripts** | `D:\MARS-Localhost\tools\hosts\` (multi-domain registry-driven) |
| **Smoke URL** | `http://mli-smoke-001.test/` |
| **WordPress synthetic** | `http://fws-0001.test/` — MLI-WP-SYN-001 |

---

## Entry points

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub |
| [roadmap.md](roadmap.md) | MLI-00 … MLI-06 stages |
| [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md) | WordPress profile standard |
| [registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md](registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md) | WordPress runtimes |

---

## Consumers (do not own MLI)

- **Forge WordPress** — WordPress runtime consumer (**FW-05R complete**)
- **OCPilot** — OpenCart runtime consumer (planned MLI-04)
- **Website Factory** — frontend packages only

---

## Honesty

- **Not** a MARS git repository on D:
- **Not** production hosting
- WordPress synthetic runtime **proven with limitations** (MLI-03)
- OpenCart profile **not** created (MLI-04)

---

*MLI — MLI-03 complete.*

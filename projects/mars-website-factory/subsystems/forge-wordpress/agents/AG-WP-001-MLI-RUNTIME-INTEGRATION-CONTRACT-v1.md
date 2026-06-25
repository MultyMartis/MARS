# AG-WP-001 — MLI Runtime Integration Contract v1

**Document type:** Runtime integration contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Principle:**

```text
C:\AI MARS governs.
D:\MARS-Localhost executes.
```

---

## 1. MLI responsibilities

| Responsibility | Owner |
|----------------|-------|
| Runtime provisioning (PHP/MySQL/Apache) | MLI |
| Domain and hosts | MLI |
| Certificates (local) | MLI |
| DB isolation per runtime ID | MLI |
| Credentials boundary | MLI manifests in brain; secrets outside Git |
| Backups (runtime zone) | MLI / operator |
| Runtime manifests | `projects/mars-localhost-infrastructure/` |
| Test execution environment | MLI profile |

---

## 2. AG-WP-001 responsibilities

| Responsibility | Boundary |
|----------------|----------|
| Consume approved runtime profile | Read manifest; validate before work |
| Validate environment matches project | Gate D |
| **Not** rewrite MLI architecture | Forbidden |
| **Not** expose secrets in artifacts | Forbidden |
| **Not** broaden listeners / ports | Forbidden |
| **Not** select alternate datadir | Forbidden |
| **Not** alter Laragon globally | Infrastructure task only |

---

## 3. Approved runtime consumption

Agent reads:

- [MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md](../../../mars-localhost-infrastructure/registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md)
- Project runtime ID (e.g. `MLI-WP-FP0002-LOCAL`)

Agent validates URL, PHP version, mail suppression policy before R2+ work.

---

## 4. Path boundaries

| Zone | Agent may |
|------|-----------|
| `C:\AI MARS` (brain, WORDPRESS source) | Read/write project artifacts per Git |
| `D:\MARS-Localhost` | **No structural changes** without MLI task; consume runtime only |

---

## 5. Known limitations

| Item | State |
|------|-------|
| Laragon cold-start persistence | PROVEN (commit `266e2a86`) |
| Full Windows reboot retest | SAFE UNKNOWN — operator |

---

*MLI integration v1 — consumer only, not infrastructure owner.*

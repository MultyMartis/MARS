# MARS Localhost — Node and npm Standard v1

**Document type:** Node/npm policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Canonical source

| Tool | Source | MLI-02 verified |
|------|--------|-----------------|
| **Node** | **System** Node 24.x | v24.13.1 |
| **npm** | **System** npm | 11.8.0 |
| Laragon `bin\nodejs` | **NOT USED** | Incomplete / stale |

MLI activation **does not** prepend Laragon Node.

---

## Policy

| Rule | Value |
|------|-------|
| Duplicate Node in `D:\MARS-Localhost\tools` | **Avoid** unless justified |
| Dependencies | **Project-local** `node_modules` |
| Lockfiles | **Mandatory** for validation fixtures |
| Global packages | Only approved CLIs; no shared global Playwright |
| System Node changes | **Out of scope** — operator manages OS install |
| Node 22 LTS fallback | Document per-project if Node 24 breaks a consumer build |

---

## Consumers

- Website Factory Gulp builds (system Node)
- MLI Playwright smoke fixture (`tools\playwright-smoke\`)
- Future Forge frontend validation

---

## Related

- [reports/MARS-LOCALHOST-MLI-02-PLAYWRIGHT-SMOKE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-02-PLAYWRIGHT-SMOKE-REPORT-v1.md)

---

*Node and npm standard v1 — MLI-02.*

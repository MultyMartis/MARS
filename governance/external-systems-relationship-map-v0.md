# MARS — External systems relationship map v0

**Status:** **documented** — lightweight relationship layer.  
**Date:** 2026-05-19.  
**Complements:** [external-system-boundaries.md](external-system-boundaries.md) (MetaBOT focus), [system-boundaries.md](system-boundaries.md), [ecosystem-topology-index.md](ecosystem-topology-index.md).

**Not:** integration platform, ownership registry, or runtime topology.

---

## Classification key

| Label | Meaning |
|-------|---------|
| **External operational** | Real workflows run outside MARS repo; MARS holds operator docs/contracts. |
| **In-repo conceptual** | Contracts, maps, planned bridges — **no** execution ownership. |
| **In-repo experimental** | Narrow R1 helpers — **not** system dispatch. |
| **Not MARS core runtime** | Must not be cited as Control Plane, orchestrator, or autonomous MARS product. |

**Execution truth:** live provider consoles (n8n, WordPress admin, hosting, Telegram, etc.) — not markdown alone.

---

## Relationship diagram

```text
                    ┌─────────────────────────────┐
                    │  MARS repo (documentation)   │
                    │  governance + registries     │
                    │  projects/* packs            │
                    │  agents/* doc packs          │
                    └──────────────┬──────────────┘
                                   │ human-supervised
           ┌───────────────────────┼───────────────────────┐
           ▼                       ▼                       ▼
    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
    │ MetaBOT     │         │ WPilot      │         │ WordPress/  │
    │ (n8n)       │         │ ops docs    │         │ Beget/host  │
    └─────────────┘         └──────┬──────┘         └─────────────┘
                                   │ planned bridge
                                   ▼
                         Website Factory (future handoff)
```

---

## Systems table

### MetaBOT — SEO Content Agent

| Dimension | Detail |
|-----------|--------|
| **Operational ownership** | **MetaBOT / n8n operators** — graphs, credentials, retries. |
| **MARS relationship** | **Canonical doc pack** `projects/metabot-seo-content-agent/`; registry `metabot-seo-content-agent` **active**. |
| **External** | n8n runtime, Telegram, provider APIs, live workflow IDs. |
| **Conceptual in-repo** | Integration contracts, sanitized exports, governance boundaries. |
| **Operational in-repo** | Human-maintained docs and operator runbooks — **not** execution. |
| **Not MARS core runtime** | MARS does **not** dispatch or own MetaBOT; adapters under `mars-runtime/adapters/` are **experimental** demos only. |
| **Legacy** | `projects/seo-content-agent/` — **do not extend**. |

---

### ORCA

| Dimension | Detail |
|-----------|--------|
| **Operational ownership** | **Human PPC operator** — reviews, pilots, heuristics. |
| **MARS relationship** | Self-contained pack `projects/orca/`; registry **active**, runtime **excluded**. |
| **External** | Ad platforms, SERP/live UI, customer sites — **outside** repo. |
| **Conceptual in-repo** | Methodology, templates, fast-path rules. |
| **Operational in-repo** | OPERATIONAL-INDEX, checklists, report templates. |
| **Not MARS core runtime** | No bidding, scheduling, or autonomous optimization claims. |

---

### WPilot

| Dimension | Detail |
|-----------|--------|
| **Operational ownership** | **Human operator** on designated test WordPress / Beget environment. |
| **MARS relationship** | Pack `projects/wpilot/`; registry `wpilot`; **future** Factory-native WordPress bridge (**planned**). |
| **External** | WordPress admin, FTP/SFTP, hosting panel, DB (read-only awareness in MVP), Beget. |
| **Conceptual in-repo** | Plugin concept + MVP roadmap — **no** plugin source in tree at stabilization. |
| **Operational in-repo** | Phase 1 MVP sequence, backup/rollback, QA templates, local-only `backups/` / `local/` policy (machine paths — **not** repo SoT). |
| **Not MARS core runtime** | Not deploy bot; not autonomous CMS agent. |
| **Modes** | **Mode A** Factory-native (target) vs **Mode B** legacy/WPBakery compatibility — see plugin concept doc. |

---

### GitGuard

| Dimension | Detail |
|-----------|--------|
| **Operational ownership** | **SAFE UNKNOWN** — no `projects/gitguard/` pack in repo. |
| **MARS relationship** | **Example entity name** in [system-entity-model.md](system-entity-model.md) only. |
| **External / conceptual** | Treat as **future specialist system** until documented pack + registry row exist. |
| **Not MARS core runtime** | Do not imply live integration or MARS ownership without evidence. |

---

### Future specialist systems (documented candidates only)

| Candidate | Evidence in-repo | Posture |
|-----------|------------------|---------|
| WPilot agent roles (`wp-audit-agent`, etc.) | `projects/wpilot/README.md` § Future Agent Candidates | **Not** in `agents/registry.md` — cards **only if** human adds them |
| Website Factory planned agents | `agents/registry.md` §4.1 | **Planned** cards — documentation only |
| Control Plane routing | `control-plane/contract.md` | **Conceptual / future** — no implementation |

**Rule:** External workflow IDs and platform node names **do not** become MARS canonical entities without explicit human registry mapping.

---

## MARS core runtime boundary (restatement)

| In-repo | Role relative to external systems |
|---------|-------------------------------------|
| `mars-runtime/**/*.js` | **Experimental** bridges — label **adapter**, not product name of external system |
| `control-plane/`, `workflows/` | **Contracts** — not dispatch to MetaBOT/WP/ORCA |
| `governance/*` | **Honesty and boundaries** — not enforcement against external platforms |
| `workspaces/*` | **Local execution** for frontends — not WordPress/n8n SoT |

---

## Cross-system edges (operator-visible)

| From | To | Relationship | Status |
|------|-----|--------------|--------|
| Website Factory | WPilot | Future approved WordPress payload / human publish gate | **Planned** — see Factory workflow + WPilot plugin concept |
| Website Factory | Gulp/Forge | Frontend delivery discipline | **Operational doc packs** |
| MetaBOT | MARS | Docs + optional R1 adapter experiment | **External owns execution** |
| ORCA | MARS | Shared governance honesty only | **Loosely coupled** |
| IdeaBox (`continuity/`) | All | Human memory hygiene | **Does not** sync to external systems |

---

## Maintenance

- Add a row here when a **new external operational pack** appears under `projects/`.  
- Update [registry/project-registry.md](../registry/project-registry.md) in the same editorial pass.  
- Do **not** duplicate full pack READMEs — **link** only.

---

*Lightweight map — Phase 1 stabilization.*

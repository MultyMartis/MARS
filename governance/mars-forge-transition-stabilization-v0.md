# MARS Forge — transition stabilization v0

**Status:** **documented** — stabilization notes only.  
**Date:** 2026-05-19.  
**Trigger:** [mars-v2-structural-coherence-audit-v0.md](mars-v2-structural-coherence-audit-v0.md) — live Forge pack exists while older governance still describes Forge as “not created.”

**Not:** a rewrite of Forge methodology, new agent card, or runtime claim.

---

## Current truth (evidence-based)

| Fact | Evidence |
|------|----------|
| Forge **pack exists** | `agents/mars-forge/` (README, AGENT.md, workflow, overlay checklists) |
| Forge **card exists** | `agents/cards/mars-forge-frontend-agent-v0.md` |
| Registry row **exists** | `agents/registry.md` §4.1 — `mars_forge_frontend_agent`, **`operational_doc_pack`** |
| Forge is an **overlay** on Gulp foundation | Pack README, registry notes — **not** parallel SoT |

**Operational posture:** human + Cursor/Codex discipline only — **not** autonomous runtime.

---

## Stale guidance (read as historical / design precedent)

These documents remain useful for **design rationale** but must **not** be read as “Forge does not exist yet”:

| Document | Stale claim | Correct reading today |
|----------|-------------|------------------------|
| [mars-forge-operational-design-v0.md](mars-forge-operational-design-v0.md) (header, §1.3 diagram label) | “Not an agent pack”; “Explicitly not created: `agents/mars-forge/`” | **Design v0 precedent** — pack was authored **after** design doc; pack **defers** to design inheritance rules |
| [frontend-legacy-and-foundation-map-v0.md](frontend-legacy-and-foundation-map-v0.md) §5 | “Reserved future role — pack not created” | **Superseded for existence** — §5 reserved **evolution** language; live pack is **operational_doc_pack** overlay |
| [governance/README.md](README.md) addenda table (Forge row) | “not agent pack or runtime” | Still true for **runtime**; **incorrect** if interpreted as “no pack directory” — see [agents/mars-forge/README.md](../agents/mars-forge/README.md) |

**Operator rule:** If stale prose conflicts with `agents/mars-forge/README.md` or `agents/registry.md` §4.1 on **existence or status**, trust the **pack + registry**.

---

## Relationship normalization

```text
Website Factory frontend contracts (SoT for handoff / production rules)
        ↓
gulp_frontend_agent  (canonical foundation pack)
        ↓ inherits
mars_forge_frontend_agent  (overlay: pipeline, freeze, overlay QA)
        ↓ discipline only
workspaces/*  (external gulp-starter execution — not MARS SoT)
```

| Layer | Owns |
|-------|------|
| Factory `frontend-handoff-contract-v0.md`, `frontend-production-rules-v0.md` | Handoff fields, operator law |
| `agents/frontend-gulp-agent/` | Gulp workflow, base QA, reporting patterns |
| `agents/mars-forge/` | Phased pipeline, freeze, **overlay** checklists (not duplicate Factory governance corpora) |
| Planned **Frontend QA Agent** (card) | Stage 12 reviewer — separate from Forge overlay |

---

## Minimal doc hygiene (done / ongoing)

| Action | Status |
|--------|--------|
| Add this stabilization note | **Done** (this file) |
| Update foundation map §5 banner + anti-chaos row | **Done** (see foundation map) |
| Add design-doc banner on operational design v0 | **Done** (see design doc header) |
| Point topology index to live Forge paths | **Done** ([ecosystem-topology-index.md](ecosystem-topology-index.md)) |
| Merge design doc into pack (giant rewrite) | **Out of scope** — defer to human editorial pass |
| Mark design doc `deprecated` | **Not recommended** — still cites inheritance model; use **historical precedent** label |

---

## Forbidden drift (unchanged)

- Claiming Forge **replaces** Gulp foundation or Factory handoff SoT  
- Marking Forge **`active`** runtime without implementation evidence  
- Describing overlay checklists as **autonomous QA services**  
- Citing `workspaces/*` as canonical MARS frontend home  

---

## SAFE UNKNOWN

- Whether every overlay checklist is **required** for every project — **operator / project charter** decides  
- Pixel-perfect / visual automation tooling — **future experiment** only if evidenced  
- Triumph V3 battle test outcomes — **documentation exercise** until implementation explicitly opened  

---

*Phase 1 stabilization — clarity only.*

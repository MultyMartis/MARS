# Forge WordPress AG-WP-001 Promotion Decision v1

**Document type:** Agent promotion decision record  
**Version:** v1  
**Stage:** FW-04  
**Date:** 2026-06-22

---

## Decision

```text
AG-WP-001 remains UNREGISTERED.
The primary specialist profile becomes operational_doc_pack only after synthetic validation.
Formal agent registration is deferred until proven execution.
```

**No row added to `agents/registry.md`.**

---

## Context

| Item | State |
|------|-------|
| AG-WP-001 seed | Exists at `workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/` |
| Canonical subsystem | `projects/mars-website-factory/subsystems/forge-wordpress/` |
| FW-04 primary specialist | `capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md` |
| Runtime | None |
| Synthetic validation | Not started (FW-05) |

---

## Options considered

| Option | Decision |
|--------|----------|
| Remains seed only | **Selected** — until FW-05 proves execution |
| Becomes internal specialist profile | **Partial** — specialist doc pack is operational for Cursor; not registry agent |
| Registers later | **Yes** — after synthetic validation + operator charter |
| Never registers | **Not selected** — deferred, not rejected |

---

## Relationship model

```text
AG-WP-001 (seed, historical)
    → informs research and boundaries
FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1 (FW-04)
    → active Cursor execution profile
agents/registry.md
    → no entry until separate promotion charter
```

---

## Promotion prerequisites (future)

1. FW-05 synthetic validation **PASS**
2. Capability readiness matrix — client pilot eligibility review
3. Operator charter for agent registration
4. Separate decision record — not automatic from FW-04

---

## Seed alignment note

Update seed cross-links to point to `capability/` pack. Seed status remains **SEED** — not OPERATIONAL agent.

See [AG-WP-001-FORGE-WORDPRESS-SEED.md](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/AG-WP-001-FORGE-WORDPRESS-SEED.md).

---

*Promotion decision v1 — AG-WP-001 unregistered.*

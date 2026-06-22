# Forge WordPress AG-WP-001 Promotion Decision v1

**Document type:** Agent promotion decision record  
**Version:** v1  
**Stage:** FW-04  
**Date:** 2026-06-22

---

## Decision (FW-05R update — 2026-06-23)

```text
AG-WP-001 remains UNREGISTERED.
Prompt-driven operational_doc_pack candidate: ELIGIBLE WITH DOCUMENTED LIMITATIONS.
Formal agent registration: STILL REQUIRES OPERATOR CHARTER.
```

**No row added to `agents/registry.md`.**

---

## FW-05 evidence

| Item | State |
|------|-------|
| Synthetic case FWS-0001 | COMPLETE |
| Synthetic outcome (static) | PROVEN WITH LIMITATIONS |
| Registry promotion | NOT PERFORMED |

---

## FW-05R evidence (2026-06-23)

| Item | State |
|------|-------|
| Live runtime MLI-WP-SYN-001 | VALIDATED |
| Live synthetic outcome | PROVEN WITH LIMITATIONS |
| PHP syntax / PHPCS / routes | PASS (with documented PHPCS residuals) |
| Visual parity | PASS WITH DOCUMENTED DEVIATIONS — WV6 PENDING |
| Registry promotion | NOT PERFORMED — charter still required |
| Doc pack eligibility | **ELIGIBLE WITH DOCUMENTED LIMITATIONS** |

---

## FW-05R checkpoint (2026-06-23)

```text
AG-WP-001:
ELIGIBLE WITH DOCUMENTED LIMITATIONS

Operational model: prompt-driven operational_doc_pack
Formal registration: REQUIRES OPERATOR CHARTER
Autonomous runtime: NONE
Production authority: NONE
Registry row: NOT ADDED
```

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

1. FW-05 + FW-05R synthetic validation **PASS WITH LIMITATIONS** — **MET**
2. Capability readiness matrix — client pilot eligibility review — **FW-06**
3. Operator charter for agent registration — **OPEN**
4. Operator WV6 on live visual parity — **PENDING**
5. Separate decision record — not automatic from FW-04 or FW-05R

---

## Seed alignment note

Update seed cross-links to point to `capability/` pack. Seed status remains **SEED** — not OPERATIONAL agent.

See [AG-WP-001-FORGE-WORDPRESS-SEED.md](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/AG-WP-001-FORGE-WORDPRESS-SEED.md).

---

*Promotion decision v1 — AG-WP-001 unregistered.*

# Canvas Pack Regeneration v1

**Date:** 2026-06-03  
**Lane:** B — MARS Visual Brain Refresh 2026-06

---

## Generator changes

**File:** `docs/visualization/obsidian-canvas/_generate_pack.py`

| Function | Change |
|----------|--------|
| `build_programs` | +GitGuard, +IdeaBox; survivability→GitGuard edge |
| `build_website_factory` | Execution cases hub; ISBD edge; Triumph v6 text |
| `build_infrastructure` | Incoming hybrid nodes/edges; observed-flow group |
| `build_archive` | Lifecycle Log **KEEP** label |
| `build_master` | Archive layer wording (historical imports) |

**orca.canvas** — generator unchanged; regen produced identical structure.

---

## Regeneration command

```text
py -3 docs/visualization/obsidian-canvas/_generate_pack.py
```

**Output (node, edge counts):**

| File | Nodes | Edges |
|------|-------|-------|
| master.canvas | 10 | 10 |
| programs.canvas | 14 | 13 |
| website-factory.canvas | 13 | 14 |
| orca.canvas | 8 | 8 |
| infrastructure.canvas | 16 | 13 |
| archive.canvas | 31 | 1 |

---

## Consistency checks

- [x] GitGuard on programs matches REGISTERED survivability entry
- [x] ISBD linked from execution cases hub
- [x] Lifecycle Log in OPERATIONAL with KEEP
- [x] Incoming hybrid edges present on infrastructure
- [x] README paths and refresh note updated

---

*Canvas pack regeneration v1 — Task 7 evidence.*

# MARS — Active Brain / Visual Brain / Cold Brain (Sync Pack 2026-06)

**Status:** **CORE**  
**Evidence:** `logs/releases/mars-v2-stable-baseline-2026-06.md`, `logs/visualization/mars-visual-brain-awareness-alignment-2026-06.md`

These are **operator navigation layers** — not runtime subsystems, not autonomous memory products.

---

## Active Brain

| Attribute | Value |
|-----------|--------|
| **Path** | `C:\AI MARS` |
| **Role** | Git-tracked working intelligence — governance, projects, registry, workspaces, `docs/`, narrow `mars-runtime/` R1 |
| **Status** | **OPERATIONAL** (human-supervised repo work) |
| **Is not** | Deployed orchestrator, 24/7 agent host, or second instance at another drive letter without confirmation |

All MARS agent filesystem scope defaults here. Checkpoint `45518bb` is the authoritative git snapshot for Stable Baseline scope; post-cleanup alignment at `aafacf8` appends ecosystem alignment.

**Ecosystem intake (post-cleanup):** repo-root `incoming/` is **Active Incoming** — untrusted drops until human promotion. Policy: `incoming/README.md`.

**Factory LOC-ZONE:** `workspaces/website-factory-operations/` — physical records in Active Brain (awareness pass 2026-06-13).

---

## Visual Brain

| Attribute | Value |
|-----------|--------|
| **Role** | Spatial / navigational understanding of the ecosystem |
| **Status** | **READY** (dual surface) |

### Dual surface

| Surface | Path | Role |
|---------|------|------|
| **Source (git)** | `docs/visualization/obsidian-canvas/` | 6 `.canvas` files + README + generator |
| **Operator copy** | `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` | Obsidian navigation, canvas copies, program cards |

**Canonical pack:** `docs/visualization/obsidian-canvas/README.md` (Export Pack v1).

**Canvases:** `master`, `programs`, `website-factory`, `orca`, `infrastructure`, `archive`.

### Post-awareness canvas entities (2026-06-13)

| Canvas | Additions |
|--------|-----------|
| `programs.canvas` | **OPS** node; **ATLAS** population label (Waves 1–6B docs); edges `hub→ops`, `ops→atlas` |
| `website-factory.canvas` | **BZPM** (#3 execution case); **LOC-ZONE** pointer |
| `infrastructure.canvas` | LOC-ZONE note on workspaces node |

Regenerate: `docs/visualization/obsidian-canvas/_generate_pack.py`

**Is not:** registry sync engine, governance auto-update, or proof that every KC folder is populated.

**Opening order (Obsidian):** `master.canvas` → `programs.canvas` → lane-specific canvas.

---

## Cold Brain

| Attribute | Value |
|-----------|--------|
| **Path** | `C:\AI MARS STORAGE\ARCHIVE` |
| **Role** | Long-term bulk archives; operator-defined cold retention |
| **Status** | **MATERIALIZED** (root exists) |
| **Is not** | Git-backed SoT, searchable MARS memory product, or auto-synced governance mirror |

**SAFE UNKNOWN:** individual archive contents and sync state unless verified per session.

---

## Relationship diagram

```text
Active Brain (C:\AI MARS)     ← git SoT, agents, packs, contracts
        │
        ├─► Visual Brain source (docs/visualization/obsidian-canvas/)
        │         └─► mirrored in KC (operator Obsidian)
        │
Storage layer (C:\AI MARS STORAGE)
        ├─► Knowledge Center (navigation / Visual Brain operator surface)
        └─► ARCHIVE (Cold Brain)
```

---

## Anti-mythology

| Do not claim | Because |
|--------------|---------|
| "Three brains" as running AI services | Layers are **organizational** — human-operated |
| KC in git | KC is **out-of-git** bulk/navigation |
| Canvas = live telemetry | Canvas mirrors **documented** topology at export time |
| Cold Brain auto-ingests repo | Archive is operator-managed |
| Canvas updates = runtime registration | Visibility alignment only |

---

*Brain layer semantics for Web-GPT — reconcile with KC README on operator machine when navigating.*

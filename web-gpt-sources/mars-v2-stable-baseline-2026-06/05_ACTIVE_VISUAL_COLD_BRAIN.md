# MARS — Active Brain / Visual Brain / Cold Brain (Stable Baseline 2026-06)

**Status:** **CORE**  
**Publication evidence:** `logs/releases/mars-v2-stable-baseline-2026-06.md`

These are **operator navigation layers** — not runtime subsystems, not autonomous memory products.

---

## Active Brain

| Attribute | Value |
|-----------|--------|
| **Path** | `C:\AI MARS` |
| **Role** | Git-tracked working intelligence — governance, projects, registry, workspaces, `docs/`, narrow `mars-runtime/` R1 |
| **Status** | **OPERATIONAL** (human-supervised repo work) |
| **Is not** | Deployed orchestrator, 24/7 agent host, or second instance at another drive letter without confirmation |

All MARS agent filesystem scope defaults here. Checkpoint `45518bb` is the authoritative git snapshot for Stable Baseline scope.

**Ecosystem intake (post-cleanup 2026-06):** repo-root `incoming/` is **Active Incoming** in Active Brain — untrusted drops until human promotion. Historical bulk may move to Storage/Cold Brain **after** operator triage. Policy: `incoming/README.md` — **not** in baseline checkpoint `45518bb` by design.

---

## Visual Brain

| Attribute | Value |
|-----------|--------|
| **Role** | Spatial / navigational understanding of the ecosystem |
| **Status** | **READY** (dual surface) |

### Dual surface

| Surface | Path | Role |
|---------|------|------|
| **Source (git)** | `docs/visualization/obsidian-canvas/` | 6 `.canvas` files + README + generator — tracked at `45518bb` |
| **Operator copy** | `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` | Obsidian navigation, canvas copies, program cards |

**Canonical pack:** `docs/visualization/obsidian-canvas/README.md` (Export Pack v1, 2026-06-02).

**Canvases:** `master`, `programs`, `website-factory`, `orca`, `infrastructure`, `archive`.

**Post-alignment entities (2026-06-13):** `programs.canvas` includes **OPS** (→ ATLAS edge); **ATLAS** population note; `website-factory.canvas` includes **BZPM** (#3) and **LOC-ZONE** pointer. Regenerate: `docs/visualization/obsidian-canvas/_generate_pack.py`.

**Is not:** registry sync engine, governance auto-update, or proof that every KC folder is populated.

**Opening order (Obsidian):** `master.canvas` → `programs.canvas` → lane-specific canvas.

---

## Cold Brain

| Attribute | Value |
|-----------|--------|
| **Path** | `C:\AI MARS STORAGE\ARCHIVE` |
| **Role** | Long-term bulk archives; operator-defined cold retention |
| **Status** | **MATERIALIZED** (root exists — 7 top-level items verified 2026-06-03) |
| **Is not** | Git-backed SoT, searchable MARS memory product, or auto-synced governance mirror |

Per Knowledge Center README: cold paths for retired bulk. **SAFE UNKNOWN:** individual archive contents and sync state unless verified per session.

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
| “Three brains” as running AI services | Layers are **organizational** — human-operated |
| KC in git | KC is **out-of-git** bulk/navigation per infrastructure reality |
| Canvas = live telemetry | Canvas mirrors **documented** topology at export time |
| Cold Brain auto-ingests repo | Archive is operator-managed |

---

*Brain layer semantics for Web-GPT — reconcile with KC README on operator machine when navigating.*

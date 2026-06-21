# Infrastructure Canvas Refresh v1

**Date:** 2026-06-03  
**Lane:** B — MARS Visual Brain Refresh 2026-06  
**Artifact:** `docs/visualization/obsidian-canvas/infrastructure.canvas`

---

## Approved Incoming model (documentation only)

| Layer | Visual node | Flow |
|-------|-------------|------|
| **Active Incoming** | `n-inf-incoming-active` | Edge → **Active Brain** (`n-inf-brain`) — label `staging` |
| **Historical Bulk** | `n-inf-incoming-bulk` | Edge → **Storage Layer** (`n-inf-storage-root`) — label `retirement` |

**SoT:** `incoming/README.md`, `logs/cleanup/actions/incoming-hybrid-alignment-v1.md`

**Explicit:** No runtime, queue, or automation implied.

---

## Brain / Storage clarifications

- Active Brain header notes **Active Incoming** (`incoming/`).
- Storage Layer header notes **Historical Bulk** after operator triage.
- Renamed misleading “archive candidates” subnodes to **archive** (distinct from `incoming/` quarantine).

---

## Observed information flow (Task 6)

Lightweight labelled group at bottom of canvas:

- Group label: **OBSERVED INFORMATION FLOW — NOT runtime · NOT architecture**
- Chain text matches `logs/cleanup/discoveries/observed-information-flow-v1.md`

---

## Node counts (post-regen)

16 nodes · 13 edges.

---

*Infrastructure canvas refresh v1 — Task 4 evidence.*

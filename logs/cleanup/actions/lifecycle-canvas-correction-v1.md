# Lifecycle Canvas Correction v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2A  
**Upstream:** [lifecycle-log-deep-review-v2.md](../discoveries/lifecycle-log-deep-review-v2.md) §4, Wave 2 Discovery W2-A05  
**Finding:** Lifecycle Log node was classified under **ARCHIVE CANDIDATE** in Obsidian pack — contradicts governance **KEEP** determination.

---

## Misclassification confirmed

| Surface | Before | After |
|---------|--------|-------|
| `docs/visualization/obsidian-canvas/_generate_pack.py` | `n-ent-lifecycle-log` → `n-cat-archive-cand` | → `n-cat-operational` |
| `docs/visualization/obsidian-canvas/archive.canvas` | Node at archive-cand coordinates (780, 450) | Node at operational coordinates (300, 270) |

**Not changed:** `web-gpt-sources/`, `chat-migration imports` — remain archive-candidate **visualization** buckets per generator (historical import posture).

**Not changed:** Canvas topology redesign, master.canvas structure, infrastructure.canvas.

---

## Rationale

Lifecycle log is **normative governance event SoT** ([logs/lifecycle-log.md](../../../logs/lifecycle-log.md)); Wave 2 classified it **KEEP**, not ARCHIVE CANDIDATE. Canvas labels are navigation aids only but were reinforcing wrong cleanup mental model (census D-007 / deep review §4).

---

## Regeneration note

Source of truth for node placement is `_generate_pack.py`. `archive.canvas` updated manually to match operational bucket offsets without full pack regen.

---

## Files changed

- `docs/visualization/obsidian-canvas/_generate_pack.py`
- `docs/visualization/obsidian-canvas/archive.canvas`

---

*Lifecycle canvas correction v1 — Wave 2A evidence.*

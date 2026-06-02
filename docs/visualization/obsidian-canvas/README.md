# MARS Obsidian Canvas Export Pack v1

Visualization-only export of the MARS ecosystem as native [JSON Canvas](https://jsoncanvas.org/) files (`.canvas`). Open in **Obsidian** (Canvas core plugin) or any JSON Canvas–compatible viewer.

**This pack is not:** an audit, registry sync, or governance update. It mirrors documented topology for spatial navigation.

**Canonical sources used at export time:**

- [`governance/ecosystem-topology-index.md`](../../governance/ecosystem-topology-index.md)
- [`governance/mars-reality-index-v0.md`](../../governance/mars-reality-index-v0.md)
- [`governance/mars-v2-structural-coherence-audit-v0.md`](../../governance/mars-v2-structural-coherence-audit-v0.md)
- [`governance/mars-infrastructure-reality-v1.md`](../../governance/mars-infrastructure-reality-v1.md)
- [`registry/project-registry.md`](../../registry/project-registry.md)
- Pack `OPERATIONAL-INDEX.md` files (ORCA, Website Factory)

**Note:** The in-repo artifact titled **REPORT — MARS Ecosystem Visualization Pack v1** was **not found** at export time; placement follows the sources above. Regenerate when that report exists.

---

## Canvases

| File | Purpose |
|------|---------|
| [`master.canvas`](master.canvas) | Top-level nine-layer MARS map (governance → archive) |
| [`programs.canvas`](programs.canvas) | Program/project packs and cross-program relationships |
| [`website-factory.canvas`](website-factory.canvas) | Website Factory internal layers, Triumph, ISBD placeholder |
| [`orca.canvas`](orca.canvas) | ORCA lanes: Fast Path, review, PPC, freeze, handoffs |
| [`infrastructure.canvas`](infrastructure.canvas) | `C:\AI MARS` (Active Brain) vs `C:\AI MARS STORAGE` |
| [`archive.canvas`](archive.canvas) | Lifecycle visualization buckets (ACTIVE … ARCHIVE CANDIDATE) |

---

## Recommended opening order

1. **`master.canvas`** — orient to layers and drill-down targets.
2. **`programs.canvas`** — see which programs exist and how they relate.
3. **Lane-specific** (pick one per session):
   - Website production → `website-factory.canvas`
   - PPC / ORCA → `orca.canvas`
   - Paths / bulk storage → `infrastructure.canvas`
   - Lifecycle / retirement posture → `archive.canvas`

---

## Navigation instructions

1. **Open in Obsidian:** Copy or symlink `docs/visualization/obsidian-canvas/` into your vault, or open the folder as a vault fragment. Double-click a `.canvas` file.
2. **Follow edges:** Arrow labels describe relationship *role* (handoff, overlay, optional), not runtime APIs.
3. **Stable node IDs:** Nodes use semantic `id` values (e.g. `n-prog-orca`) so future pack versions can diff cleanly.
4. **Cross-canvas:** Text nodes name sibling canvases (e.g. infrastructure layer → `infrastructure.canvas`). Open those files in a new tab when zooming in.
5. **Regenerate:** Run `python _generate_pack.py` from this folder after topology changes (generator is maintainer tooling, not part of the visualization product).

---

## Maintainer

- Generator: [`_generate_pack.py`](_generate_pack.py) (optional; safe to delete from vault copies if you only consume `.canvas` files).

*Export pack v1 — 2026-06-02.*

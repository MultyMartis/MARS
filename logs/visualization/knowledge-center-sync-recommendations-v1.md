# Knowledge Center Sync Recommendations v1

**Date:** 2026-06-03  
**Lane:** B — MARS Visual Brain Refresh 2026-06  
**Rule:** **Recommendations only** — **no** changes to `C:\AI MARS STORAGE`

**KC path:** `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER`  
**Git Visual Brain source:** `C:\AI MARS\docs\visualization\obsidian-canvas\`

**Upstream:** `logs/cleanup/knowledge-center-drift-report-v1.md` (extended for post-refresh pack)

---

## Files to copy (from Active Brain → KC)

Copy after operator verifies regenerated pack in Obsidian:

| Source (git) | KC destination (typical) | Action |
|--------------|-------------------------|--------|
| `docs/visualization/obsidian-canvas/master.canvas` | `00 START HERE/canvas/master.canvas` (or vault equivalent) | **Replace** |
| `docs/visualization/obsidian-canvas/programs.canvas` | `00 START HERE/canvas/programs.canvas` | **Replace** |
| `docs/visualization/obsidian-canvas/website-factory.canvas` | `00 START HERE/canvas/website-factory.canvas` | **Replace** |
| `docs/visualization/obsidian-canvas/orca.canvas` | `00 START HERE/canvas/orca.canvas` | **Replace** (unchanged content; optional skip) |
| `docs/visualization/obsidian-canvas/infrastructure.canvas` | `00 START HERE/canvas/infrastructure.canvas` | **Replace** |
| `docs/visualization/obsidian-canvas/archive.canvas` | `00 START HERE/canvas/archive.canvas` | **Replace** |
| `docs/visualization/obsidian-canvas/README.md` | `00 START HERE/canvas/README.md` or operator notes | **Copy** (maintainer reference) |

**Do not copy** `_generate_pack.py` into KC unless maintainer wants generator in vault (optional).

---

## Canvases to replace (priority)

| Priority | Canvas | Why |
|----------|--------|-----|
| **High** | `programs.canvas` | New GitGuard + IdeaBox nodes |
| **High** | `infrastructure.canvas` | Incoming hybrid + observed-flow note |
| **High** | `website-factory.canvas` | ISBD edge + execution-case framing |
| **Medium** | `archive.canvas` | Lifecycle Log **KEEP** label |
| **Low** | `master.canvas` | Minor archive-layer wording |
| **Low** | `orca.canvas` | No structural delta this refresh |

---

## Markdown files recommended for update (KC prose, not git)

| KC area | Update | Repo pointer |
|---------|--------|--------------|
| `01 ECOSYSTEM` — GitGuard | REGISTERED · mars-survivability | `gitguard-system-entry-v1.md` |
| `01 ECOSYSTEM` — IdeaBox | Optional Incubation Layer | `continuity/README.md` |
| `01 ECOSYSTEM` — Incoming | Hybrid Active + Historical Bulk | `incoming/README.md` |
| `02 PROGRAMS` — Triumph | v6 canonical workspace | `triumph-workspace-authority-map-v1.md` |
| `03 EXECUTION CASES` — ISBD | Case #2 · not program | `execution-cases-registry-v1.md` |
| `04 GOVERNANCE` | Terminology pointers | `canonical-terminology-registry.md` |
| `05 INFRASTRUCTURE` | Match refreshed infrastructure canvas | `mars-infrastructure-reality-v1.md` |
| Lifecycle card | **KEEP** · Key Event History | `logs/lifecycle-log.md` |

Full checklist: `logs/cleanup/knowledge-center-drift-report-v1.md` (KC-01 … KC-15).

---

## Operator sequence

1. **Pull / open** latest `C:\AI MARS` commit with refreshed `docs/visualization/obsidian-canvas/`.
2. **Open** each `.canvas` in Obsidian from git path — verify layout (GitGuard, Incoming, ISBD edge, Lifecycle KEEP).
3. **Backup** current KC `canvas/` folder (operator snapshot).
4. **Replace** six `.canvas` files into KC mirror path.
5. **Update** KC markdown cards per table above (high priority first).
6. **Do not** treat KC edits as governance SoT — backport factual fixes to Active Brain if needed.
7. **Record** operator sync date in KC dashboard or personal note (no repo telemetry).

---

## Explicit non-actions

| Action | Status |
|--------|--------|
| Agent writes to STORAGE | **Not performed** |
| Auto-sync KC ↔ git | **Not available** |
| Upload KC to Web-GPT | **Not recommended** |

---

## SAFE UNKNOWN

- Exact KC folder names on operator disk (verify `06_KNOWLEDGE_CENTER.md` structure)
- Last KC sync date vs this refresh commit

---

*Knowledge Center sync recommendations v1 — Task 8 (recommendations only).*

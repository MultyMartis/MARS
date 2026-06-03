# MARS — Knowledge Center (Stable Baseline 2026-06)

**Status:** **CORE** (operator surface)  
**Path:** `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER`  
**Publication status:** **READY** — operator navigation system (not in git)

---

## What the Knowledge Center is

The **MARS Knowledge Center (KC)** is the **Visual Brain operator layer**: Obsidian-oriented navigation, dashboards, program cards, and canvas mirrors for the ecosystem. It complements git-tracked docs in **Active Brain** (`C:\AI MARS`).

| Attribute | Value |
|-----------|--------|
| Layer | Visual Brain (operator copy) |
| Authority | Human-operated; KC README defines role |
| Git | **Not in git** — bulk/navigation per `governance/mars-infrastructure-reality-v1.md` |
| Relationship to canvas pack | Git source: `docs/visualization/obsidian-canvas/` — copies under KC |

---

## Documented structure (operator vault)

| Section | Purpose |
|---------|---------|
| `00 START HERE` | Operator landing — e.g. `MARS DASHBOARD.md` |
| `01 ECOSYSTEM` | Ecosystem orientation |
| `02 PROGRAMS` | Program cards / pack pointers |
| `03 EXECUTION CASES` | Case-oriented navigation |
| `04 GOVERNANCE` | Governance pointers (not SoT replacement) |
| `05 INFRASTRUCTURE` | Paths, storage, brain layers |
| `06 ARCHIVE` | Archive orientation |
| `99 EXPORTS` | Export staging |

Canvas mirrors may live under KC (e.g. `00 START HERE/canvas/master.canvas`).

---

## How Web-GPT should use KC

| Do | Don't |
|----|-------|
| Treat KC as **operator navigation** when user references it | Assume KC files are in repo or auto-synced to git |
| Point to git SoT for authoritative changes | Edit governance only in KC without repo pass |
| Re-verify KC layout if user pastes paths | Invent KC folder contents not evidenced |
| Use `docs/visualization/obsidian-canvas/` for versioned maps | Upload entire KC to Web-GPT as pack material |

**Workflow:** Plan in Web-GPT → execute doc changes in `C:\AI MARS` → operator may refresh KC mirrors manually.

**Post-cleanup (2026-06):** KC mirrors may lag git SoT for GitGuard REGISTERED, Incoming hybrid, ISBD execution case, Triumph v6 — operator refresh recommended per `logs/cleanup/knowledge-center-drift-report-v1.md` (no auto-sync).

---

## SAFE UNKNOWN (session-level)

- Whether every KC section is populated on disk  
- Sync between KC and latest git commit  
- Obsidian plugins/settings on operator machine  
- Per-program card freshness vs `OPERATIONAL-INDEX.md`  

Verify with operator paste or session listing when KC paths matter to the task.

---

## Related repo surfaces

| Topic | Path |
|-------|------|
| Infrastructure reality | `governance/mars-infrastructure-reality-v1.md` |
| Visual Brain source pack | `docs/visualization/obsidian-canvas/README.md` |
| Stable Baseline evidence | `logs/releases/mars-v2-stable-baseline-2026-06.md` |

---

*KC is READY at baseline publication — navigation aid, not MARS runtime.*

# Section replacement & survivability contract (Wave 1)

**Status:** **documented** — **implementation survivability** for Gulp/include sections.  
**Not:** meta-governance; **not** automated enforcement.

**Scope:** static HTML/SCSS/JS sections in workspace `src/`.  
**Related:** Forge freeze — [agents/mars-forge/AGENT.md](../../agents/mars-forge/AGENT.md); reliability — [implementation-reliability-governance.md](implementation-reliability-governance.md).

---

## 1. Section as unit

A **section** is the smallest **freeze/replace** unit when:

- tied to a `block_id` (or documented ad hoc ID in handoff);
- owns a **partial** (HTML include) + **scoped SCSS** (+ optional JS module);
- listed in REPORT with file paths.

**Component** changes inside a frozen section require **unfreeze** if they affect contract fields (structure, CTA, breakpoints, hooks).

---

## 2. Freeze / unfreeze

| State | Meaning | Allowed edits |
|-------|---------|---------------|
| **Open** | In progress | Full phase work per Forge |
| **Frozen** | QA accepted for scope; regression-sensitive | **None** without unfreeze record |
| **Deferred** | Known gaps; not delivery-ready | Only items in deferral list |
| **Superseded** | Replaced by new section charter | Old partial **read-only** reference |

**Freeze requires:** Standard+ mode QA, build evidence or SAFE UNKNOWN, `frozen: true` in REPORT, file list.

**Unfreeze requires:** REPORT line — **reason**, **blast radius**, **re-freeze criteria**; mode ≥ Standard.

---

## 3. Blast radius rules

| Change class | Typical radius | Minimum mode |
|--------------|----------------|--------------|
| Local class inside section partial | Section only | Lite |
| Section partial HTML structure | Section + adjacent cadence | Standard |
| Shared SCSS variable / mixin | **Global** — all dependent sections | Critical |
| `gulp-file-include` graph edge | All includes upstream/downstream | Standard–Critical |
| JS hook rename (`data-*`) | All binders + HTML | Standard |
| Header / hero / global nav | First-screen + layout shell | Critical |

**Rule:** if unsure, assume **wider** radius and escalate mode.

---

## 4. Allowed mutation scope

| In frozen section | Allowed |
|-------------------|---------|
| Copy typo in LOCKED semantics | **No** — HITL + unfreeze |
| Cosmetic color one-off | **No** unless handoff marks FLEXIBLE |
| Bugfix breaking layout | Unfreeze + regression note |
| Adjacent section spacing only | **Yes** if cadence doc cited; record CADENCE FINDINGS |

**Local vs global:**

- **Local:** selector and partial under section directory — default for replacement.
- **Global:** `_variables`, mixins, layout shell, utilities — **Critical** + explicit dependency list in REPORT.

---

## 5. Section replacement lifecycle

```text
1. Charter     — block_id, reason (drift / redesign / A-B), source vN
2. Impact      — blast radius table + mode
3. Unfreeze    — if prior freeze exists
4. Detach      — remove or isolate old partial from include graph
5. Implement   — new partial + SCSS (+ JS) per handoff
6. Regression  — adjacent sections, header/hero, mobile, CTAs
7. QA          — Standard+ overlay + foundation QA
8. Re-freeze   — or Defer with open findings
9. REPORT      — before/after paths, findings, freeze state
```

**Survivable replacement:** new section **does not** silently change global tokens or shared partials without listing them.

---

## 6. Regression expectations

After replace or unfreeze, check **at least**:

- include resolves (no broken `@@include`);
- build succeeds or SAFE UNKNOWN documented;
- default viewport: no horizontal scroll on touched page;
- CTA/hook IDs still unique and bound once;
- **Adjacent** section cadence (gap before/after);
- frozen neighbors: **no accidental** style leakage via shared selectors.

**Partial ownership:** section author owns section partial; **shared** partial owner must be named in REPORT when touched.

---

## 7. Safe replacement workflow (operator)

1. Confirm **active design version** and handoff — not archive.
2. List **all files** to touch before edit.
3. If any **frozen** neighbor depends on shared assets — escalate Critical.
4. Prefer **replace partial** over in-place rewrite when drift > 30% DOM (judgment — state in REPORT).
5. Run build; capture command output in REPORT.
6. Do not delete old partial until new include wired — or document rollback path.
7. Re-freeze only when QA checklist slice passes for **new** scope.

---

## 8. Failure modes (name in REPORT)

| Failure | Response |
|---------|----------|
| Hidden global change | Rollback; Critical review |
| Freeze without evidence | Invalidate freeze; Standard QA |
| Replace changes CTA hierarchy | STRATEGIC / DESIGN INTENT finding; HITL |
| Mobile collapse | RESPONSIVE INTENT finding before freeze |

---

*Wave 1 — section survivability normalization for frontend production acceleration.*

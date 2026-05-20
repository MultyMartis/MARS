# Production freeze discipline v1 (Wave 6)

**Status:** **documented** — lightweight freeze levels for Gulp Factory workspaces.  
**Related:** [production-hardening-rules-v1.md](production-hardening-rules-v1.md) · [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md).

**Not:** CI gates, **not** automated lock files, **not** enterprise change boards.

---

## Freeze levels

| Level | Scope | Typical trigger |
|-------|--------|-----------------|
| **L0 — open** | Edits allowed | bootstrap, pre-first-build |
| **L1 — section** | Named `block_id` partial + SCSS (+ section JS) | section QA PASS |
| **L2 — workspace** | Full `src/` except hotfix path | pre-delivery / client sign-off |
| **L3 — foundation** | `scss/foundations/`, `js/core/` | brand tokens + lifecycle frozen |
| **L4 — delivery** | Workspace + REPORT archive | production handoff complete |

Higher level wins: L3 freeze blocks casual token edits even if L1 section was open.

---

## Section freeze (L1)

**When:** block reaches **validated** tier ([block-quality-tiers-v1.md](block-quality-tiers-v1.md)) and compact QA PASS.

**Frozen artifacts:**

- `partials/sections/{block_id}.html`  
- `scss/sections/_{block_id}.scss`  
- `js/sections/{block_id}.js` if present

**Allowed without unfreeze:** copy-only text inside partial (HITL); analytics attributes.

**Requires unfreeze:** layout structure, grid breakpoints, new CTAs, token scope changes, new `data-module`.

**Record:** `# REPORT — <slug> section freeze <block_id>` with build output.

---

## Workspace freeze (L2)

**When:** all handoff blocks built; [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md) PASS; hardening spot-check done.

**Frozen:** entire `src/pages`, `src/partials`, `src/scss/sections`, section JS.

**Still editable with Standard REPORT:** none — use unfreeze procedure.

---

## Foundation freeze (L3)

**When:** brand tokens approved; modal/form/lifecycle verified once per workspace.

**Frozen:** `scss/foundations/*`, `js/core/*`.

**Override:** only via foundation unfreeze (below) — blast radius **Critical** per golden slice.

---

## Override procedure

1. Operator states **level** being broken and **reason** (one sentence).  
2. Forge mode **Standard** minimum for L2–L3.  
3. Implement minimal diff.  
4. Re-run `npm run build` + [operational-qa-entry-v1.md](operational-qa-entry-v1.md).  
5. `# REPORT — <slug> freeze override` with before/after file list.  
6. Re-apply freeze at same or higher level when PASS.

**No override** for `dist/` edits — rebuild only.

---

## Hotfix procedure

For production defects **after L2**:

| Step | Action |
|------|--------|
| 1 | Classify: copy / CSS / JS / foundation |
| 2 | Touch **only** implicated block or hotfix branch |
| 3 | If foundation: L3 unfreeze + explicit REPORT |
| 4 | Build + QA + redeploy `dist/` from pipeline |
| 5 | Post-hotfix: re-freeze at prior level |

**Timebox:** hotfix ≠ redesign; new blocks → new `block_id`, not silent reshape under freeze.

---

## Replacement under freeze

Per [section-replacement-contract-v1.md](section-replacement-contract-v1.md):

1. `destroySection`  
2. Swap partial  
3. `initSection`  
4. Re-QA affected block + modal/sticky if touched  

**L1 frozen block:** replacement of **content** inside same structure = allowed. **Structure** change = unfreeze L1 first.

---

## QA before unfreeze

| Level unfreeze | Required |
|----------------|----------|
| L1 | Section QA + survivability note |
| L2 | Full compact QA + adoption validation |
| L3 | Foundation-lite checklist + hardening rules z-index/modal |

---

## REPORT obligations

Every freeze and unfreeze produces:

```markdown
# REPORT — <project> freeze <L1|L2|L3|L4>
- Level:
- Blocks/scope:
- Build: PASS | FAIL
- QA entry: operational-qa-entry-v1 — PASS | gaps
- Next allowed edits:
```

Store with delivery artifacts; chat is **not** SoT.

---

*Wave 6 — production freeze discipline.*

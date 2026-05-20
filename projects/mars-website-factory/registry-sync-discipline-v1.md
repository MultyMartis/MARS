# Registry ↔ implementation sync discipline v1 (Wave 6)

**Status:** **documented** — human-maintained alignment between planning registry and reference `src/`.  
**Registry:** [block-registry-v0.md](block-registry-v0.md) · **Library:** [curated-library-index-v1.md](curated-library-index-v1.md).

**Not:** automated sync, **not** a registry engine, **not** runtime validation product.

---

## Source of truth split

| Concern | Wins when |
|---------|-----------|
| **Semantic role** (purpose, SEO, anti-patterns) | `block-registry-v0.md` unless project handoff overrides |
| **HTML/SCSS/JS structure** | Reference workspace + extraction REPORT |
| **Quality tier / adoption** | `curated-library-index-v1.md` |
| **Operational status** | Latest REPORT + consolidation map |

**Conflict rule:** implementation wins for **structure**; registry wins for **naming and compatibility** until human updates registry.

---

## When registry must update

Update `block-registry-v0.md` (or project handoff table) when:

- New `block_id` added to reference library  
- `compatible_site_types` / `incompatible_site_types` change from pilot evidence  
- `frontend_complexity` or `QA_focus` no longer matches reality  
- Deprecation of a block role (mark in registry **notes**, do not delete rows silently)

**Not required** for: copy tweaks, token brand colors, hotfix CSS inside frozen structure.

---

## When implementation wins

- Extraction neutralized structure differs from registry prose — fix registry **notes**, not forced revert of working partial  
- Registry used conceptual role name — map to canonical `block_id` in REPORT  
- Pilot proves anti-pattern is avoidable with HITL — document exception in project artefact, optional registry note

---

## Extraction sync rules

After each real extraction:

1. `data-block-id` = registry `block_id` (snake_case).  
2. Add/update row in [curated-library-index-v1.md](curated-library-index-v1.md).  
3. Set tier per [block-quality-tiers-v1.md](block-quality-tiers-v1.md).  
4. Link REPORT in `operational-examples/wave*-extraction-report-*.md`.  
5. If registry had no row (e.g. gap) — add registry row **or** log **SAFE UNKNOWN** in REPORT.

---

## Implementation status rules

| Status | Meaning |
|--------|---------|
| **not started** | Registry row only |
| **experimental** | In reference, tier experimental |
| **ready** | In reference, tier validated+ |
| **deprecated** | Partial removed; registry row retained with deprecation note |

Update [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md) block list when reference set changes.

---

## Deprecated block handling

1. Mark deprecated in curated index (do not delete history).  
2. Registry row: add `notes: deprecated — use <successor>`.  
3. Remove from reference `index.html` only after REPORT.  
4. Client workspaces: migration note in pilot/legacy REPORT — **not** auto-migrated.

---

## Quality tier updates

| Event | Action |
|-------|--------|
| Extraction PASS | tier ≥ validated in curated index |
| Swap demo PASS | promote toward battle-tested |
| Pilot freeze without issues | may promote battle-tested → canonical (HITL) |
| Drift / failed QA | demote tier; implementation fix or deprecate |

Registry v0 has **no** tier field — tiers live **only** in curated index + tier doc.

---

## Adoption state updates

Track in pilot REPORT (not registry):

- blocks copied to client workspace  
- freeze level reached  
- lessons learned  

Optional one-line pointer in [registry/project-registry.md](../../registry/project-registry.md) project notes — **human only**.

---

## Drift detection (lightweight)

Operator suspicion triggers sync review:

- Handoff cites `block_id` not in reference  
- Partial exists, no curated index row  
- Tier says canonical but no golden slice mention  

Fix in one session: implementation **or** docs — record in REPORT.

---

*Wave 6 — registry sync discipline.*

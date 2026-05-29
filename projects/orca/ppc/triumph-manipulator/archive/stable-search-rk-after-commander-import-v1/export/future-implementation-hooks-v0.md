# Future implementation hooks — Triumph Manipulator PPC

**Status:** Documentation targets only. **No** runtime, schema files, exporters, or n8n workflows exist in this repository for this pack unless separately proven elsewhere.

**Human supervision remains mandatory** for launch and budget decisions.

---

## Design constraints (carry forward)

1. **Search-only** until explicitly chartered otherwise  
2. **Structured entities** are SoT — Excel is transport  
3. **Validation before export** — non-optional in doctrine  
4. **Exporter is dumb** — no semantic reasoning in export layer  
5. **Anti-entropy** — prefer 10 strong groups over 100 weak ones  

---

## Hook 1 — JSON entity schema (Phase 2 target)

Represent:

- `campaign` — name, geo, negatives, strategy, extensions, settings  
- `group` — intent label, keyword cluster, negatives, landing URL, ads[]  
- `ad` — headline_1/2, description, display_url, fastlinks[], callouts[], landing_url, draft flag  
- `landing_ref` — blueprint id linking to `landing-pages/*.md` intent  

Suggested future path: `schemas/ppc-entity-v0.json` (not created in Phase 1).

---

## Hook 2 — Validation engine (Phase 3 target)

Pre-export checks aligned with [direct-commander-foundation-v0.md](direct-commander-foundation-v0.md) and [generation-logic-v0.md](../doctrine/generation-logic-v0.md):

| Class | Examples |
|-------|----------|
| Structural | Required fields present |
| Symbol | Yandex Direct field limits, truncation risk |
| Semantic | One intent per group, no mixed employment/buy/repair |
| Commercial | Capability/use-case fit plausible for Triumph machine |
| Survivability | No giant keyword dumps, no generic forbidden phrases |
| Continuation | Ad intent matches `landing_ref` |

Output: validation report artifact for human — not auto-fix silently.

---

## Hook 3 — Exporter engine (Phase 4 target)

- Input: validated JSON entity graph  
- Output: Commander-compatible `.xlsx` using [assets/direct-commander-template/](../assets/direct-commander-template/) as field map  
- Must **not** embed generation or intent logic  

Suggested future path: `tools/export-commander-v0/` (not created).

---

## Hook 4 — Prompt system (Phase 5 target)

- Constrained prompts that emit **JSON entities**, not raw Excel or unbounded ad spam  
- System prompts must inject doctrine excerpts by reference (intent purity, anti-generic list, Yandex bold-highlight)  
- Human review gate before any export call  

Suggested future path: `prompts/` with versioned prompt packs — not created.

---

## Hook 5 — n8n workflows (Phase 6 target)

Possible **human-triggered** flows (experimental isolation):

- Intake form → intent map draft → human approve  
- SERP notes → segmentation suggestion → human approve  
- Validated JSON → export file → notify operator  

**Not** autonomous campaign launch loops.

---

## Hook 6 — MARS / Website Factory integration (Phase 7 target)

| Integration | Direction |
|-------------|-----------|
| Website Factory | Landing blueprints → page build briefs; continuation QA |
| Parent ORCA | SERP review, landing-match, campaign-qa-assembly cross-links |
| Continuity lane | Decision records for tier launches — human-written |

---

## Event-driven validation (operational discipline today)

Until engines exist, treat these as **human events**:

| Event | Action |
|-------|--------|
| New group proposed | Intent purity check against [intent-groups-v1.md](../research/intent-groups-v1.md) |
| Ad draft written | Bold-highlight + anti-generic pass |
| Landing assigned | Continuation check vs blueprint |
| Pre-import | Symbol + duplicate + negative pass |
| Post-import (platform) | Human confirms Commander acceptance |

---

## What not to build without charter

- Autonomous bid management  
- Auto-launch / auto-pause  
- RSYA or Master Campaign generators  
- “AI ad manager” orchestration claiming production autonomy  

---

## Evidence rule

Promote any future automation from **experiment → pattern** only with human-reviewed evidence (MARS operational experiment semantics). Do not merge experiment scripts into this pack’s doctrine SoT without review.

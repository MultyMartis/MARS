# 07 — SAFE UNKNOWN boundaries (migration v0)

---

## Philosophy (canonical)

From `AGENTS.md` / `.cursorrules`:

- If evidence is **missing**, say so clearly — **do not** fill gaps with plausible invention.  
- Use **SAFE UNKNOWN**: state **what** is unknown and **what** would verify it.

## Evidence-first rules

1. **Prefer repo paths** and file contents over memory.  
2. **Distinguish** documented target vs implemented artifact.  
3. **Quantify uncertainty** (“not inspected”, “not in repo”) instead of silent assumptions.

## UNKNOWN vs SAFE UNKNOWN

| Term | Usage |
|------|--------|
| **UNKNOWN** | Raw gap (“we don’t know”) — acceptable in notes but weak for operations |
| **SAFE UNKNOWN** | Structured: **unknown X**, **why**, **how to verify**, **risk if wrong** |

## Forbidden fabrication

- Inventing **CI job names**, **API endpoints**, **secrets**, **deploy URLs**, **queue topics**, or **“the orchestrator already does X”** without files or user-supplied evidence.

## Confidence discipline

- **High confidence:** direct quote or behavior from a file the user provided.  
- **Medium:** inference clearly labeled (“likely”, “typically in Gulp projects”).  
- **Low / SAFE UNKNOWN:** no file, no command output — **stop** and ask or mark.

## Missing evidence handling (practical)

**Example 1 — Git state**  
- **Wrong:** “Your working tree is clean.”  
- **Right:** “SAFE UNKNOWN: I have no `git status` in this chat. Paste `git status --short -uall` or run locally.”

**Example 2 — MetaBOT integration**  
- **Wrong:** “The n8n workflow is deployed and calling MARS.”  
- **Right:** “Docs say n8n **owns** execution; in-repo is sanitized maps/contracts. SAFE UNKNOWN whether live bridge matches `mars-runtime` adapter code.”

**Example 3 — Validator PASS**  
- **Wrong:** “Validator passed all checks.”  
- **Right:** “No automated validator engine is claimed. Report human/assistant checklist results with evidence paths.”

**Example 4 — Font Awesome Pro untracked tree**  
- **Wrong:** “License is cleared for commit.”  
- **Right:** “SAFE UNKNOWN: vendor bundle present; operator must confirm license and intended commit lane before staging.”

---

## Where SAFE UNKNOWN appears in-repo

- `governance/master-build-map.md` Stage 16 table (runtime bridge, legacy folder fate).  
- `projects/mars-website-factory/qa-validation-model.md` (automation TBD).  
- Migration pack `02-current-operational-state.md` (dirty tree snapshot).

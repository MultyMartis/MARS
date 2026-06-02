# OCPilot — Battle Pilot Workflow

**Pattern source:** ORCA battle pilot discipline (freeze, lessons) — **not** ORCA PPC scope.  
**First battle pilot name:** **Read-Only OpenCart Dealership Audit**

## Pilot rules (hard)

| Allowed | Forbidden |
|---------|-----------|
| Inspect target (files/DB/public/admin as chartered) | Writes to disk or DB |
| Build site passport | Catalog import |
| Identify OC version, theme, modules | Theme edits |
| Map catalog structure (categories, filters, attributes) | Controller edits |
| Note DB snapshot **availability** | ocMod/vQmod **changes** |
| Compare to clean baseline if available | Any production mutation |

## Sequence

1. **Charter** — operator confirms site-slug, read-only only, target URL/host.
2. **Passport** — [templates/site-passport-template.md](templates/site-passport-template.md) or [project-site-passport-template.md](templates/project-site-passport-template.md).
3. **Inspect** — files tree signals, `admin/`, `catalog/`, `system/`, extensions, ocMod/vQmod presence (facts only).
4. **Catalog map** — high-level structure; no bulk export to repo unless sanitized policy allows.
5. **Baseline compare** — if Run 2 baseline exists; else SAFE UNKNOWN for core/custom split.
6. **SAFE UNKNOWN list** — `sites/<slug>/safe-unknown/` + report section.
7. **Next-step plan** — planned runs 6–7 only as proposals; no execution in this pilot.
8. **Report** — `# REPORT — OCPilot Battle Pilot Read-Only — <site-slug>`.
9. **Freeze optional** — lessons → `freeze/battle-pilots/` (metadata markdown only).

## Stop cues (ORCA-style)

- STOP when passport + top findings + SAFE UNKNOWN + next plan are done.
- Do not expand into full security audit or full DB analytics without new charter.

## Freeze folder

`freeze/battle-pilots/` holds **pilot outcome summaries** for regression learning — not live site state.

## Relation to OPERATIONAL-INDEX

Maps to **Run 5 — Battle Pilot Read-Only** (planned until operator starts pilot after Runs 2–4).

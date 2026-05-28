# ORCA → Website Factory Semantic Lock v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — cross-lane content continuity contract.

Not a runtime integration. Not an API. Not proof that Factory enforces this automatically.

## Purpose

When ORCA has produced **approved** research, landing briefs, or handoff documents, Website Factory (Lane A / Frontend Production) must preserve **semantic continuity** — offers, positioning, intent, CTA strategy, and supportable claims.

Factory may adapt **presentation**. Factory may not rewrite **commercial meaning** without explicit operator override.

## Preconditions (lock active)

Semantic lock applies when **all** are true:

1. An ORCA **approved** artifact exists: landing brief, handoff doc, or strategy doc in `approved` / `production-ready` status.
2. Handoff explicitly references ORCA SoT paths.
3. Operator session is **MODE 1** (below).

If only draft ORCA materials exist, lock is **inactive** — Factory must treat content as provisional.

## Locked Semantics (Factory MUST NOT change)

| Domain | Locked examples |
|--------|-----------------|
| Offers | Price framing, "from X rub", service scope, tonnage/capability claims |
| Positioning | Master vs capability vs use-case vs B2B framing |
| Intent continuity | Ad query intent → hero → section order supporting qualification |
| CTA strategy | Call-first vs form-first, channel priority (phone / WhatsApp / form) |
| Claims | Guarantees, speed promises, geography, fleet facts — only as ORCA approved |
| Trust proof | Review sources, ratings text, legal entity references |
| Negative space | What the page must NOT promise (anti-junk, anti-broad rental) |

## Allowed Factory Changes (presentation layer)

| Domain | Allowed |
|--------|---------|
| Layout | Grid, section spacing, component arrangement |
| Responsive | Breakpoints, mobile stacking, touch targets |
| Typography | Font sizes, weights, line-height within brand system |
| UI adaptation | Icons, imagery crops, button styling |
| Accessibility | Contrast fixes that do not alter claim text |
| Asset pipeline | Build, minify, favicon, perf — no semantic edits |

## Forbidden Without Explicit Operator Override

- Rewriting headlines that carry intent qualification.
- "Improving" offer copy for marketing flair.
- Merging capability and use-case intents on one page.
- Inventing statistics, reviews, or fleet capabilities.
- Changing CTA hierarchy (e.g. form-primary when ORCA says call-first).
- Placeholder lorem replacing approved Russian copy in MODE 1.

## Production Modes

### MODE 1 — ORCA-driven production (content locked)

- **Input SoT:** ORCA approved landing brief and/or handoff (e.g. `*-handoff.md` in Triumph pack).
- **Factory role:** Implement layout and UI; copy paste or structural bind from handoff.
- **QA:** Continuation check — ad intent ↔ hero ↔ CTA ↔ trust (human checklist).
- **Violation handling:** Stop build; escalate to operator — do not silently "fix" copy.

### MODE 2 — Demo / exploratory (content may be placeholder)

- **Use when:** No approved ORCA brief, design exploration, component library work.
- **Placeholder copy** allowed if marked `demo` in path or `PROJECT.md`.
- **Must not** ship to paid traffic paths without MODE 1 conversion.
- **Must not** be cited as ORCA continuity proof.

## Handoff Contract (minimum fields)

ORCA handoff should include or reference:

| Field | Purpose |
|-------|---------|
| `handoff_id`, `version`, `date` | Traceability |
| `source_artifacts[]` | Approved ORCA paths |
| `page_intent` | capability / use-case / B2B / master / … |
| `hero_contract` | H1, subhead, proof line rules |
| `section_order[]` | Locked narrative sequence |
| `cta_contract` | Primary/secondary CTA, channels |
| `claims_allowed[]` / `claims_forbidden[]` | Claim boundary |
| `safe_unknown[]` | Gaps Factory must not invent |

**Validated example:** `projects/orca/ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md`

## Relationship to Factory Blueprints

Factory reference blueprints (e.g. `projects/mars-website-factory/reference-cases/`) provide **registry shape** only.

When handoff exists, **handoff overrides** section order and copy for that page build.

## Lane Boundaries

| Lane | Responsibility |
|------|----------------|
| ORCA (B) | Evidence, intent, briefs, PPC continuity, handoff authorship |
| Website Factory (A) | HTML/CSS/JS production, build pipeline, visual QA |
| Operator | Mode selection, approval, override logging |

No autonomous cross-lane merger. No shared runtime orchestrator claimed.

## HITL Override Protocol

1. Operator documents override in `approvals/` or handoff amendment.
2. States what changed and why.
3. Updates ORCA artifact status if commercial meaning changed.
4. Factory rebuild references new approval id.

## SAFE UNKNOWN

- Whether Factory CLI will enforce lock automatically — **not in repo**.
- Whether all Factory workspaces read handoff path by default — **operator responsibility** in v0.

## Related Documents

- [orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md)
- [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md)
- [orca-operational-principles-v0.md](../orca-operational-principles-v0.md)
- Triumph handoff: `projects/orca/ppc/triumph-manipulator/handoff/`

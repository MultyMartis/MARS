# MARS — Governance enforcement (documentation layer)

**Status:** **documented** — human-readable **anti-drift** aids. **Not** runtime code, **not** CI policy, **not** autonomous governance.

---

## Purpose

Reduce **documentation drift**, **terminology drift**, and **fake-runtime** language by giving reviewers a **small, explicit** catalog: what to look for, what wording is risky, and what stays **human-only**.

## Scope (in)

- Markdown under `governance/enforcement/` (check catalog, forbidden phrases, terminology boundaries, future validation *strategy* only).
- Cross-links from `governance/README.md` and minimal pointers elsewhere.

## Scope (out)

- No orchestration, queues, daemons, or hidden automation.
- No rewrite of MARS architecture or expansion of product philosophy.
- No production/frontend lane work; no `workspaces/*` changes.

## Non-runtime nature

Enforcement here means **review discipline** and **shared vocabulary** — not executable enforcement inside a MARS process. Experimental code under `mars-runtime/` is **out of scope** for this folder except as **wording** and **registry-boundary** context (see [../runtime-registry-boundaries.md](../runtime-registry-boundaries.md)).

## Human-first governance

**HITL** and **documentation-first** remain primary per [../../AGENTS.md](../../AGENTS.md). These files help humans say “stop” when claims outrun evidence.

## Anti–fake-runtime role

Call out language that implies shipped **MARS core** automation when the repo only has **contracts** and **narrow R1** experiments. Canonical honesty rules: [../../AGENTS.md](../../AGENTS.md) (status honesty, three-way split, SAFE UNKNOWN).

## Lightweight enforcement model

| Artefact | Role |
|----------|------|
| [governance-checks.md](governance-checks.md) | Review checklist IDs (detection ideas + human action). |
| [forbidden-runtime-claims.md](forbidden-runtime-claims.md) | Phrase patterns → governance review. |
| [terminology-boundaries.md](terminology-boundaries.md) | Stable term distinctions. |
| [lightweight-validation-strategy.md](lightweight-validation-strategy.md) | What might *later* be semi-automated vs must stay human-reviewed. |

---

*Phase S1 — governance enforcement layer; documentation only.*

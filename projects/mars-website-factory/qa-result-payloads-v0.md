# MARS Website Factory — QA result payloads v0

**Status:** **documentation only** — **field vocabulary** for QA outputs across lanes ([qa-validation-model.md](qa-validation-model.md)). **Not** a JSON API, **not** an automated QA engine.

**Related:** [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

---

## Core payload concepts

| Field | Meaning |
|-------|---------|
| **severity** | e.g. `info` \| `warn` \| `blocker` — project-normalized scale; exact enum **SAFE UNKNOWN** globally. |
| **category** | Lane-specific bucket (SEO metadata, conversion friction, a11y, build, policy). |
| **evidence** | Repro steps, URL, selector, screenshot reference — **human-auditable**. |
| **escalation_signal** | Maps to governance signals: **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE**, **SECURITY RISK**, **UNKNOWN**, **SAFE UNKNOWN**. |
| **waiver** | Boolean / note: issue accepted under named approver + date. |
| **blocker** | True when downstream stage must not proceed without fix or waiver. |
| **SAFE UNKNOWN** | Finding cannot be concluded from available evidence — do not assert pass. |
| **confidence** | Reviewer judgment `low` \| `medium` \| `high` — **not** ML confidence unless separately defined. |
| **HITL required** | Whether human sign-off is mandatory for this item class. |
| **approval status** | e.g. `open` \| `waived` \| `resolved` — format **TBD** per tooling. |

---

## Lane relationships

| Lane | Typical categories | Validator overlap |
|------|---------------------|-------------------|
| **Design QA** | Fidelity, token drift, state coverage | Structural checks if design files in scope |
| **SEO QA** | Titles, headings, thin content, schema honesty | Policy/link integrity |
| **Conversion QA** | CTA clarity, trust honesty, form friction | Guardrail language |
| **Frontend QA** | Build, semantics, responsive, JS scope | Secrets / dangerous patterns when routed |
| **Validator integration** | Cross-cutting **task** fit, forbidden paths | **Complements** specialists — split **TBD** per [agent-map.md](agent-map.md) |

---

## Non-claims

- **No** assertion that QA payloads are persisted, streamed, or validated by code in this repo.
- Automated visual regression / Lighthouse CI — **SAFE UNKNOWN** for Factory v0 per [qa-validation-model.md](qa-validation-model.md).

---

*Last updated: 2026-05-11.*

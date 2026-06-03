# IdeaBox Alignment v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2B  
**Upstream:** [ideabox-deep-review-v2.md](../discoveries/ideabox-deep-review-v2.md)  
**Architect decision:** IdeaBox = **Incubation Layer** (optional; not mandatory entry path)

---

## Alignment posture

| Field | Value |
|-------|-------|
| **Entity** | IdeaBox (`continuity/`) |
| **Classification** | **OPERATIONAL** human-operated discipline |
| **Ecosystem role** | **Incubation Layer** (optional) |
| **`project_id` row** | **No** |
| **Forced routing** | **No** — direct program/governance creation remains valid |

---

## When to use IdeaBox

Use **`continuity/`** when:

- An **idea** exists but **implementation is deferred**
- Session continuity needs lightweight capture (ideas, discoveries, decisions)
- Operator wants anti-entropy markdown without registry mutation

**Do not require** IdeaBox before creating `projects/*` packs or governance docs.

---

## Distinction from other capture surfaces

| Surface | Trust | Purpose |
|---------|-------|---------|
| **IdeaBox** (`continuity/`) | Human-authored | Optional incubation |
| **Incoming** (`incoming/`) | Untrusted until triage | External artefact quarantine |
| **Cleanup discoveries** (`logs/cleanup/discoveries/`) | Audit evidence | Ecosystem census — not session capture |
| **Registry** | Normative identity | Current `project_id` rows |

---

## Actions taken

| Surface | Change |
|---------|--------|
| `continuity/README.md` | Incubation Layer (optional) + direct-creation rule |
| `registry/project-registry.md` | IdeaBox note → Incubation Layer |
| `governance/ecosystem-topology-index.md` | Continuity / IdeaBox § — incubation role |
| `governance/canonical-terminology-registry.md` | IdeaBox type + optional incubation |
| `governance/context-continuity-rules.md` | Optional incubation pointer |

**Deferred (operator):** `continuity/INCUBATION-PATH-v0.md` (Wave 2A W2-A06).

---

## Files changed

- `continuity/README.md`
- `registry/project-registry.md`
- `governance/ecosystem-topology-index.md`
- `governance/canonical-terminology-registry.md`
- `governance/context-continuity-rules.md`

---

*IdeaBox alignment v1 — Wave 2B evidence.*

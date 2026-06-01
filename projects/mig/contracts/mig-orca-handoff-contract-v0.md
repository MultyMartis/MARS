# MIG → ORCA Handoff Contract v0

**Status:** **documented** — minimum human handoff artifact.  
**Not:** API spec, transport protocol, file watcher, or automated pipeline.

**Direction:** MIG → ORCA only (after human approval).  
**Transport:** **Human handoff only** — operator delivers pack; no mandated channel.

---

## Purpose

Define the **minimum fields** ORCA needs to begin R2 (Marketing Intelligence Analysis) without re-doing groundtruth capture.

ORCA **must not** treat missing fields as silently inferable — use **SAFE UNKNOWN** and request human clarification.

---

## Required fields

| Field | Requirement |
|-------|-------------|
| **Research Scope** | What market/question boundary was studied (vertical, intent surface, competitor set, etc.). |
| **Region** | Geographic or locale scope of capture. |
| **Date** | Session date or capture window (ISO-8601 preferred). |
| **Queries** | List of queries or observation triggers used. |
| **Evidence Sources** | URLs, surfaces, tools used by humans (names only — no automation claim). |
| **Snapshots** | Pointers or attachments to preserved captures (files, hashes, or explicit paths in session folder). |
| **Observations** | Normalized human-readable observation set (SERP, local pack, reviews, trust, offer, CTA as applicable). |
| **Evidence Grade** | Session-level and/or per-observation grade per MIG grading discipline. |
| **SAFE UNKNOWN** | Explicit list of unknowns — gaps, blocked pages, inconclusive captures. |
| **Approved By** | Human identifier + approval date — **mandatory** before ORCA intake |

---

## Optional fields (v0)

Operators may add narrative context, session id, or manifest checksum — **not required** for v0 validity.

---

## Acceptance rules (ORCA side)

1. Reject or halt if **Approved By** is missing.
2. Do not infer **semantic clusters** from raw observations without ORCA methodology.
3. Preserve **SAFE UNKNOWN** through analysis — do not collapse unknowns into false confidence.
4. Do not treat this contract as proof of automated snapshot integrity unless separately verified.

---

## Non-goals (this contract)

- No API endpoints · no webhooks · no queue · no schema registry engine  
- No n8n · no agent dispatch · no mars-runtime execution binding  

---

## Related

- Research Request (upstream intake): [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md)  
- Research Pack (domain object): [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md)  
- Boundaries: [../boundaries.md](../boundaries.md)  
- Report template: [../reports/REPORT-TEMPLATE.md](../reports/REPORT-TEMPLATE.md)  
- ORCA pack: [../../orca/README.md](../../orca/README.md) — **read-only** reference; do not modify ORCA in bootstrap v1

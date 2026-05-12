# MARS Website Factory — Validation evidence model v0

**Status:** **documentation only** — **evidence taxonomy** for QA and validation narratives. **Not** a storage schema, **not** a chain-of-custody engine.

**Version:** v0.

**Related:** [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

---

## 1. Evidence classes

| Class | Definition |
|-------|------------|
| **direct** | Observation tied immediately to artifact content (quoted snippet, file path + section, selector, diff hunk). |
| **inferred** | Conclusion justified by explicit reasoning steps from direct evidence — must remain auditable (“because A and B, therefore C”). |
| **linked** | Evidence that points to another artifact, envelope, or approval record as SoT (“see handoff §X”). |
| **external** | SoT outside the repo (client CMS, analytics, legal doc) — name the source; **SAFE UNKNOWN** if source cannot be cited. |
| **missing** | Expected proof absent — gate cannot honestly claim completeness for that slice. |
| **conflicting** | Two or more evidence items imply incompatible conclusions — requires resolution or escalation. |
| **SAFE UNKNOWN** | Bounded honesty: scope cannot be verified from available evidence; **no fabrication** — per dictionary, **not** a waiver. |

---

## 2. Evidence confidence

| Level | Meaning |
|-------|---------|
| **high** | Direct evidence + minimal inference; reproducible by a second reviewer from the same artifacts. |
| **medium** | Mix of direct and linked; small inference gaps labeled. |
| **low** | Heavy inference, stale linked SoT, or partial external access — usually pairs with **SAFE UNKNOWN** slices or **NEED HUMAN APPROVAL**. |

Confidence is **reviewer judgment** in v0 unless a future contract defines machine metrics — see [qa-result-payloads-v0.md](qa-result-payloads-v0.md).

---

## 3. Provenance

Each evidence item **should** record (when humans/authors simulate the model):

- **who** collected or asserted it (role / agent name in documentation sense);
- **when** (timestamp — format **TBD**);
- **what** artifact/version/lineage it applies to.

**SAFE UNKNOWN:** persistence format and tooling.

---

## 4. Freshness and stale evidence

- **Fresh** — evidence collected against the **current** artifact lineage and approvals after last material change.
- **Stale** — evidence tied to superseded revision, pre-invalidation lineage, or broken freeze/approval assumption — must **not** silently carry **passed** status; see [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md) (**stale validation**).

---

## 5. Unsupported claims

Claims without evidence class mapping (or with only **missing** / unlabeled inference) are **unsupported**. Packaging:

- downgrade assertiveness;
- emit **SAFE UNKNOWN** or **UNKNOWN** per severity;
- escalate per [validation-escalation-model-v0.md](validation-escalation-model-v0.md).

---

## 6. GOOD vs BAD examples

### GOOD

- “**Direct:** `frontend/src/index.html` L120–128 — single `<h1>` present.”
- “**Linked:** CTA text matches [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) handoff table row `cta_primary` in approved blueprint v3.”
- “**SAFE UNKNOWN:** Lighthouse performance score — not measured in-repo for Factory v0; no performance pass claimed.”

### BAD

- “SEO is fine” (no **direct** / **linked** evidence).
- “Validator approved” (no human attribution where HITL required; conflates role with authority).
- “Waiver implied because SAFE UNKNOWN” (**false** — SAFE UNKNOWN is **not** a waiver per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md)).

---

*Last updated: 2026-05-12.*

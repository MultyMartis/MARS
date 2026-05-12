# MARS Website Factory — Reference Run Reporting v0

**Status:** **documentation only** — operational **REPORT** types for reference runs. Aligns with [reporting-standard-v0.md](reporting-standard-v0.md).

**Version:** v0.

**Related:** [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [reference-run-sequence-v0.md](reference-run-sequence-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md).

---

## 1. Alignment to reporting-standard v0

| This doc’s report type | `reporting-standard-v0.md` lane |
|------------------------|----------------------------------|
| Stage report | §4.1 Documentation REPORT (also used for non-code stage narrative) |
| QA report | §4.3 QA REPORT |
| Escalation report | §3 **HITL flags** + prose section (may be standalone or embedded) |
| Invalidation report | §4.1 + **Artifact changes** / lineage notes |
| Delivery report | §4.1 with delivery-specific evidence; **no** deploy fiction |
| Freeze report | §4.1 — documents freeze scope, anchors, approvers |
| Revision report | §4.1 — documents reopen, scope, impact, QA reset intent |

Frontend-heavy runs additionally use §4.2 where applicable.

---

## 2. Minimal required fields (all types)

Per [reporting-standard-v0.md](reporting-standard-v0.md) §3 — every REPORT includes:

1. Header `# REPORT — <task or stage name>`
2. **Created files** / **Updated files** (or explicit “none”)
3. **Artifact changes** (or “none”)
4. **QA changes** (or “none”)
5. **SAFE UNKNOWN**
6. **Risks**
7. **Git status** (`git status --short`) when repo work occurred
8. **Runtime exclusions** (e.g. paths intentionally untouched)
9. **Push status**

Lane-specific **forbidden** items from §4.x apply unchanged.

---

## 3. Stage report

**When:** End of each R-stage run that changes understanding or files.

| Additional emphasis | Content |
|---------------------|---------|
| **Evidence references** | Links/paths to intake notes, registry rows, blueprint IDs. |
| **Checkpoint intent** | Which checkpoint (C01–C08) the stage advances toward. |
| **Blocker reporting** | Open questions with owner; **do not** hide partial completion. |

---

## 4. QA report

**When:** R06, R09, R12, and any ad-hoc QA prompt.

| Additional emphasis | Content |
|---------------------|---------|
| **Subject** | `artifact_id` or page/template identifier. |
| **Lane** | Design / SEO / Conversion / Frontend / Validator (as applicable). |
| **Findings** | Structured per [qa-result-payloads-v0.md](qa-result-payloads-v0.md). |
| **Recommendation** | pass / fail / conditional only ([reporting-standard-v0.md](reporting-standard-v0.md) §4.3). |

---

## 5. Escalation report

**When:** Signals **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE**, or stuck **UNKNOWN**.

| Additional emphasis | Content |
|---------------------|---------|
| **Trigger** | Exact finding or missing evidence. |
| **Authority** | Named role(s) allowed to resolve. |
| **Deadline** | If time-bound risk exists. |
| **Resolution** | Closed in a follow-up REPORT when decided. |

---

## 6. Invalidation report

**When:** Upstream artifact change stale-ifies downstream consumers.

| Additional emphasis | Content |
|---------------------|---------|
| **Source change** | Parent artifact + REPORT reference. |
| **Impacted set** | List of downstream artifacts/commits now suspect. |
| **Required reruns** | Which R-stages / QA gates must repeat. |

---

## 7. Delivery report

**When:** R15 packaging and handoff.

| Additional emphasis | Content |
|---------------------|---------|
| **Package contents** | Manifest, version/commit/tag, checksums if used. |
| **Environments** | What was smoke-tested vs **SAFE UNKNOWN**. |
| **Rollback notes** | Human steps only ([reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md)). |

---

## 8. Freeze report

**When:** Establishing or changing a freeze associated with **C04–C06**.

| Additional emphasis | Content |
|---------------------|---------|
| **Scope** | URLs/templates/components included/excluded. |
| **Anchors** | Commit/tag/export IDs. |
| **Approvers** | Matches **G*** / HITL roster. |

---

## 9. Revision report

**When:** Reopen after freeze or scoped edit mid-pipeline.

| Additional emphasis | Content |
|---------------------|---------|
| **Revision boundary** | What changed vs what stayed frozen ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| **QA reset** | Which QA results are void. |
| **Lineage** | Parent/child artifact linkage. |

---

## 10. SAFE UNKNOWN reporting

- List unknowns **explicitly**; separate **bounded assumptions** from **unverified** items ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).
- **Validator status** line when relevant: `planned` / `not invoked` / `out of scope` ([reporting-standard-v0.md](reporting-standard-v0.md) §3 optional).

---

## 11. Blocker reporting

Blockers **must** include: owner, severity, whether delivery-blocking, and next **human** action. Silent parking is **forbidden** as a terminal state — either escalate or document intentional park with HITL.

---

*End of Reference Run Reporting v0.*

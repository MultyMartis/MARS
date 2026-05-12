# Operational template — QA review (v0)

**Status:** **documentation-only** unified **QA review shell** for any factory lane (blueprint, design, frontend, semantic, transfer). **Not** automated Validator execution; aligns with [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) vocabulary.

**Normative references:** [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md), [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md), [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md).

---

## 1. Review header

| Field | Value |
|-------|-------|
| QA scope (artifact / stage) | |
| Inputs reviewed (paths / versions) | |
| QA owner lane | |
| Related gate (if any) | |

---

## 2. Verdict summary

Pick one primary posture per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md): **pass** / **fail** / **conditional** / **blocked** / **waiver required**.

**Verdict:**  
**Rationale (1–3 sentences):**

---

## 3. Findings

| ID | Finding | Severity | Evidence pointer |
|----|---------|----------|------------------|
| | | | |

**Severity:** align to project mapping (e.g. V0–V3 style in [validation-result-semantics-v0.md](validation-result-semantics-v0.md)) or blueprint QA checklist categories.

---

## 4. Blockers

List **delivery-blocking** items explicitly. Empty = none.

| Blocker ID | Description | Owner to resolve |
|------------|-------------|------------------|
| | | |

---

## 5. Waivers

Per [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) — **no** silent / auto / implicit waivers.

| Waiver ID | Scope | Authority (HITL role) | Expiry / condition |
|-----------|-------|----------------------|----------------------|
| | | | |

---

## 6. SAFE UNKNOWN

List **unknowns** that **must not** be treated as pass:

| Topic | Why unknown | Next verification step |
|-------|-------------|-------------------------|
| | | |

---

## 7. Freeze impact

Does this QA result **require freeze break**, **extend freeze**, or **leave freeze unchanged**? ([semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md))

**Freeze impact:**

---

## 8. Invalidation scope

Per [dependency-invalidation-v0.md](dependency-invalidation-v0.md) — which downstream artifacts are **stale** or **orphaned** if findings are accepted?

**Invalidation scope:**

---

## 9. Re-test notes

What must be **re-run** after fixes (partial QA vs full lane QA)?

---

## 10. Honesty boundary

- **No** fabricated tool output (Lighthouse scores, crawl counts) unless logs exist and are cited.
- **No** fake “QA sign-off” personas — roles must match real project authority or be labeled **simulation** in reference cases only.

---

*Template v0 — evidence-first QA shell.*

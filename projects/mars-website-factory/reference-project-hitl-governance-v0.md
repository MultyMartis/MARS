# MARS Website Factory — Reference Project HITL Governance v0

**Status:** **documentation only** — **human-in-the-loop (HITL) delivery discipline** for approvals and authority.  
**Not claimed:** policy engines, identity systems, or automated enforcement in this repository.

**Version:** v0.

**Related:** [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [reference-project-model-v0.md](reference-project-model-v0.md), [`../../security/approval-gates.md`](../../security/approval-gates.md).

---

## 1. Authority normalization

Authorities are **roles**, not tools. **Binding** to named people is **project charter / SAFE UNKNOWN** outside this pack.

### 1.1 Approval authority

**Who may grant approvals** that advance frozen handoffs (strategy, blueprint, design, release). Approvers must be **outside** the authorship chain for the artifact under review (see §4). Aligns with **G1–G7** in [workflow-map.md](workflow-map.md).

### 1.2 Rejection authority

**Who may block** progression with a **documented reason** and required remediation path. Typically same role family as approvers; **may** be delegated per charter (documented only).

### 1.3 Freeze authority

**Who may declare** artifact or stage **frozen** for handoff. Often shared with approvers; **technical** freeze (build tags) must still respect **HITL** release rules.

### 1.4 Reopen authority

**Who may authorize** breaking a freeze for **revision** or **regeneration** per [revision-semantics-v0.md](revision-semantics-v0.md). **Reopen** without QA impact analysis is **disallowed** for production `project_type`.

### 1.5 Waiver authority

**Who may accept** residual risk when QA reports **conditional** or **blocked** items. **Stricter** than normal approval; must cite **scope** and **expiry** where applicable per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).

### 1.6 Escalation authority

**Who routes** conflicts (compliance vs speed, design vs SEO) to the correct decision forum. Does **not** imply an automated escalation daemon — **human process** and **signals** per [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 2. Irreversible approvals

Some approvals are **treated as irreversible** for **operational honesty** unless a formal **incident / legal** process applies:

- **Release to production** acceptance by client/ops (contract-defined).
- **Legal/compliance** sign-off where charter states non-repudiation.

**Documentation rule:** label irreversible approvals explicitly in the runbook. **SAFE UNKNOWN:** jurisdiction-specific requirements.

---

## 3. Conditional approvals

**Conditional approvals** advance the stage **only** when listed **conditions** are met (e.g. “ship with known accessibility debt item X remediated within N days”). Downstream teams **must not** strip conditions. See [approval-semantics-v0.md](approval-semantics-v0.md).

---

## 4. Approval inheritance

Downstream handoffs **inherit** upstream approvals **only** for **in-scope** artifacts and **until** invalidation breaks the chain per [dependency-invalidation-v0.md](dependency-invalidation-v0.md). **Inherited** does **not** mean **implicit** — each gate still needs **explicit** acknowledgment where workflow-map demands.

---

## 5. Approval invalidation

Approvals **lose force** when:

- Upstream artifacts they depended on are **revised** or **superseded**.
- **Scope** changes (pages added/removed, locale added) without re-approval.
- **Expiry** or **revocation** per [approval-semantics-v0.md](approval-semantics-v0.md).

**QA verdict inheritance** follows [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) — failing upstream QA **blocks** silent downstream “pass”.

---

## 6. Hard prohibitions (normative for v0)

| Prohibition | Rationale |
|-------------|-----------|
| **Self-approval** | Same party must not **author** and **solely approve** the same gate (**G1–G7** / release). |
| **Autonomous approval** | LLM, script, or cron **must not** record human approval — **NEED HUMAN APPROVAL** per system signals. |
| **Fake delivery acceptance** | Synthetic “client signed” without real HITL is **forbidden**; demo projects must not reuse production approval tokens. |

---

## 7. Validator relationship

The **Validator** agent (where documented) performs **bounded** checks. It **does not** replace **approval authority**, **waiver authority**, or **release authority**.

---

## 8. SAFE UNKNOWN

- Org chart mapping roles to individuals — **charter**.
- Multi-tenant approval routing — **planned-implementation** at best.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Reference Project HITL Governance v0** — authorities, inheritance, prohibitions. |

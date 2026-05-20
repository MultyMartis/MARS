# Multi-Agent Coordination Checklist - MARS Forge

**Status:** Forge overlay QA checklist for human-supervised multi-agent coordination and responsibility boundaries.  
**Not:** runtime orchestrator, autonomous agent governance AI, consensus engine, approval router, or replacement for operator/HITL judgment.

**Factory governance:** [`../../projects/mars-website-factory/multi-agent-coordination-governance.md`](../../projects/mars-website-factory/multi-agent-coordination-governance.md).  
**Responsibility model:** [`../../projects/mars-website-factory/agent-responsibility-boundary-model.md`](../../projects/mars-website-factory/agent-responsibility-boundary-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/multi-agent-drift-taxonomy.md`](../../projects/mars-website-factory/multi-agent-drift-taxonomy.md).

Record findings as **MULTI-AGENT FINDINGS** in the Forge execution REPORT when any item is partial, failed, unknown, HITL-recommended, HITL-required, blocked, or materially affects PASS/freeze confidence.

---

## 1. Role Boundary QA

- [ ] Participating roles are named: executor, reviewer, validator, orchestrator, escalation authority, HITL authority, or other bounded role.
- [ ] Execution ownership is distinct from review ownership.
- [ ] Review ownership is distinct from validation ownership.
- [ ] Orchestration order does not imply authority.
- [ ] HITL authority is not assigned to an AI role by implication.
- [ ] Self-review, if present, is disclosed as non-independent.

---

## 2. Responsibility-Boundary QA

- [ ] Material decisions have visible owners.
- [ ] Assumptions have visible owners and remain labeled as assumptions.
- [ ] Deferrals have a next owner or resolver.
- [ ] SAFE UNKNOWN items state which role should resolve them.
- [ ] Freeze/PASS responsibility is traceable to evidence and authority.
- [ ] No defect, contradiction, waiver, or escalation is owned by "the chain" without a role.

---

## 3. Reviewer Independence QA

- [ ] Reviewer had access to source, evidence, or governance beyond the executor narrative.
- [ ] Reviewer can disagree with executor output without being treated as workflow failure.
- [ ] Reviewer did not silently inherit executor assumptions.
- [ ] Reviewer findings are separate from executor notes and validator conclusions.
- [ ] Review does not rely only on "previous agent said so".
- [ ] Any non-independent review is reported as PARTIAL or scope-limited.

---

## 4. Validator Integrity QA

- [ ] Validator evidence level is named and scoped.
- [ ] Validator did not treat executor/reviewer claims as proof.
- [ ] Validator preserved unknowns, assumptions, and contradictions.
- [ ] PASS/PARTIAL/FAIL language does not exceed evidence.
- [ ] Validation can reduce confidence or block freeze.
- [ ] Circular validation is absent: the chain is not validating itself.

---

## 5. Escalation Ownership QA

- [ ] Escalation triggers are named: ambiguity, contradiction, authority gap, evidence gap, assumption chain, fake consensus, responsibility gap, or HITL dependency.
- [ ] Escalation owner is named.
- [ ] HITL-required decisions are not converted into AI-owned decisions.
- [ ] Open escalations survive handoff into final REPORT.
- [ ] Waivers or approvals, if referenced, are attributable.
- [ ] No duplicated escalation ownership causes inaction.

---

## 6. Orchestration Clarity QA

- [ ] Coordination sequence is explainable without claiming runtime orchestration.
- [ ] Each role's input and output boundary is readable.
- [ ] Stop conditions are visible before PASS/freeze.
- [ ] Authority boundary is clear for source priority, implementation changes, QA confidence, waiver, and approval.
- [ ] Handoffs preserve scope, assumptions, evidence, contradictions, and next owner.
- [ ] Coordination is not used to make output faster at the expense of responsibility clarity.

---

## 7. Handoff Survivability QA

- [ ] A future operator can reconstruct who executed, reviewed, validated, escalated, and approved or deferred.
- [ ] Contradictions survive summaries until resolved.
- [ ] Assumptions do not become facts through repetition.
- [ ] Reviewer/validator disagreement remains visible.
- [ ] Unresolved responsibility gaps are not hidden by "consensus".
- [ ] Remaining SAFE UNKNOWN items include resolver, evidence needed, and decision boundary.

---

## 8. Multi-Agent Drift Scan

Check for named drift from [`multi-agent-drift-taxonomy.md`](../../projects/mars-website-factory/multi-agent-drift-taxonomy.md):

- [ ] Reviewer/executor collapse.
- [ ] Validator contamination.
- [ ] Authority overlap.
- [ ] Chain hallucination amplification.
- [ ] Assumption propagation.
- [ ] Orchestration ambiguity.
- [ ] Duplicate ownership.
- [ ] Unresolved responsibility gap.
- [ ] Escalation orphaning.
- [ ] Circular validation.
- [ ] Feedback-loop contamination.
- [ ] Fake consensus.
- [ ] Responsibility diffusion.

Any material match requires **MULTI-AGENT FINDINGS**.

---

## 9. REPORT Block

Use this block when multi-agent coordination affects the result:

```text
MULTI-AGENT FINDINGS - <scope>

Roles involved:
- Executor:
- Reviewer:
- Validator:
- Orchestrator:
- Escalation authority:
- HITL authority:

Responsibility boundary:
- Execution owner:
- Review owner:
- Validation owner:
- Escalation owner:
- Decision owner:

Independence and integrity:
- Reviewer independence: independent | partial | non-independent | unknown
- Validator integrity: direct evidence | partial evidence | contaminated | unknown
- Assumption inheritance: none | disclosed | unsafe | unknown

Coordination risks:
- Drift patterns:
- Contradictions preserved:
- Responsibility gaps:
- Fake consensus risk:

Disposition:
- continue | continue with disclosure | independent review needed | validator rerun needed | HITL required | blocked

Resolver needed:
- <source priority, evidence, independent review, HITL decision, waiver, ownership assignment, contradiction resolution>
```

---

## 10. Pre-Freeze Closure

- [ ] Multi-agent coordination checklist outcome recorded before PASS/freeze when multiple AI-assisted roles or handoffs affect the scope.
- [ ] `MULTI-AGENT FINDINGS` do not collapse into QA confidence or human escalation findings.
- [ ] Remaining responsibility gaps are not hidden behind consensus.
- [ ] Frozen scope does not imply independent review, validation, approval, or truth beyond recorded evidence and authority.

---

## 11. Not Claimed

- No runtime multi-agent orchestration.
- No consensus truth engine.
- No autonomous governance AI.
- No automatic role enforcement.
- No self-governing agent swarm.
- No replacement for foundation QA, Website Factory governance, operator judgment, or HITL authority.

Forge uses this checklist to preserve responsibility clarity, reviewer independence, validator integrity, escalation ownership, and coordination survivability during frontend production.

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge multi-agent coordination checklist; adds `MULTI-AGENT FINDINGS` for role boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and fake-consensus risk. |

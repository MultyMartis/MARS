# Human Escalation Checklist — MARS Forge

**Status:** Forge overlay QA checklist — human-supervised methodology only.  
**Not:** approval engine, autonomous governance AI, runtime stop gate, or replacement for operator judgment.

**Factory governance:** [`../../projects/mars-website-factory/human-escalation-governance.md`](../../projects/mars-website-factory/human-escalation-governance.md).  
**Decision model:** [`../../projects/mars-website-factory/decision-boundary-model.md`](../../projects/mars-website-factory/decision-boundary-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/escalation-drift-taxonomy.md`](../../projects/mars-website-factory/escalation-drift-taxonomy.md).

Record findings as **HUMAN ESCALATION FINDINGS** in the Forge execution REPORT when any item is partial, failed, unknown, HITL-recommended, HITL-required, or blocked.

---

## 1. Boundary Classification

- [ ] Decision boundary classified as `autonomous-safe`, `autonomous-with-disclosure`, `HITL-recommended`, `HITL-required`, `blocked-by-ambiguity`, or `blocked-by-contradiction`.
- [ ] Decision owner is clear: source artifact, governance rule, prompt scope, implementation pack, operator instruction, or human approval.
- [ ] AI confidence is not being used as a substitute for human authority.
- [ ] SAFE UNKNOWN includes an action: continue with disclosure, request HITL, stop, or block.

---

## 2. Stop-Condition QA

- [ ] No approved-looking source contradiction is unresolved.
- [ ] No material ambiguity affects meaning, hierarchy, CTA role, interaction, responsive intent, state, accessibility, asset authority, freeze, or delivery readiness without boundary classification.
- [ ] No absent approval, waiver, or human decision is implied.
- [ ] No implementation step crosses from execution into source-priority, structural regrouping, business claim, or release authority.
- [ ] Stop conditions are treated as healthy governance, not workflow failure.

---

## 3. Contradiction Escalation QA

- [ ] Conflicting sources, prompts, project notes, or governance rules are named.
- [ ] Current priority rule resolves the conflict, or the work is `blocked-by-contradiction`.
- [ ] Conflict is not minimized as "small" until impact is scoped.
- [ ] Contradiction is not resolved by taste, convenience, prior-session memory, or implementation momentum.

---

## 4. HITL Visibility QA

- [ ] Human-owned decisions are visible before implementation/freeze.
- [ ] Any HITL approval, waiver, override, scope change, or deferral is explicit and attributable.
- [ ] No fake approval is created from silence, prior progress, visual similarity, or build success.
- [ ] Human override records preserve remaining uncertainty and proof boundary.

---

## 5. Assumption-Threshold QA

- [ ] Material assumptions are counted as a chain, not treated as isolated harmless guesses.
- [ ] Low-impact assumptions are disclosed when they affect implementation confidence.
- [ ] Multiple assumptions in one section trigger at least HITL-recommended review.
- [ ] Assumptions affecting meaning, CTA purpose, trust claims, source priority, approval, freeze, or business claims trigger HITL-required.
- [ ] Assumptions caused by source contradiction block continuation until resolved.

---

## 6. Authority-Integrity QA

- [ ] Active source and project pack authority are not overridden by foundation defaults, archived sources, prior sections, or previous session memory.
- [ ] Implementation momentum is not treated as authorization.
- [ ] QA PASS/freeze language does not exceed evidence or approval authority.
- [ ] Bounded autonomy is preserved: AI acts only inside explicit source, prompt, governance, and human decision boundaries.

---

## 7. Escalation Drift Scan

Check for named drift from the taxonomy:

- [ ] Silent continuation.
- [ ] Fake certainty escalation.
- [ ] Assumption chain drift.
- [ ] Unresolved contradiction continuation.
- [ ] Hidden HITL dependency.
- [ ] Authority confusion.
- [ ] Escalation avoidance.
- [ ] Unsafe autonomy.
- [ ] Implementation momentum bias.
- [ ] Contradiction minimization.
- [ ] Ambiguity normalization.
- [ ] Escalation fatigue.
- [ ] Invisible stop-condition drift.

---

## 8. REPORT Format

Use this block when escalation is relevant:

```text
HUMAN ESCALATION FINDINGS — <scope>

Boundary level: <autonomous-safe | autonomous-with-disclosure | HITL-recommended | HITL-required | blocked-by-ambiguity | blocked-by-contradiction>
Trigger: <ambiguity / contradiction / approval / assumption chain / evidence gap / source priority / stop condition>
Decision owner: <source / governance / operator / HITL / unknown>
Evidence: <source paths, prompt notes, QA evidence, or missing evidence>
Drift pattern: <taxonomy term or none>
Disposition: <continue / continue with disclosure / HITL requested / stopped / blocked>
Resolver needed: <approval, source priority, annotated mockup, content decision, waiver, implementation-pack update, QA evidence>
```

---

## 9. Pre-Freeze Closure

- [ ] Human escalation checklist outcome recorded before PASS/freeze when applicable.
- [ ] Remaining SAFE UNKNOWN does not hide HITL-required or blocked decisions.
- [ ] Deferrals are named and owned.
- [ ] Frozen scope does not imply approval beyond the evidence and authority recorded.

---

## 10. Not Claimed

- No runtime HITL workflow.
- No automatic approval routing.
- No autonomous governance agent.
- No universal escalation law.
- No self-approval by Forge.

Forge uses this checklist to preserve human decision visibility during frontend production, not to automate human authority.

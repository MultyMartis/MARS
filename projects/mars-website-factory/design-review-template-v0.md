# Operational template — Design review (v0)

**Status:** **documentation-only** standardized review shell for **design direction** and **design handoff** quality gates. **Not** Figma automation, **not** pixel tooling claims.

**Normative references:** [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [design-layer-model.md](design-layer-model.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md).

---

## 1. Review metadata

| Field | Value |
|-------|-------|
| Artifact(s) under review | |
| Blueprint version / lineage ref | |
| Reviewers (lanes) | |
| Date | |

---

## 2. Hierarchy and layout

- **Visual hierarchy** matches blueprint section intent ([page-blueprint-contract-v0.md](page-blueprint-contract-v0.md)).
- **Scan order** — hero → proof → mechanism → CTA; mobile vs desktop differences called out.
- **Grid / spacing** alignment with design tokens (or explicit **SAFE UNKNOWN** if tokens undefined).

---

## 3. Typography

- Scale readable at primary breakpoints.
- **No** illegible contrast; note WCAG intent (manual verification — **not** automated audit claim).

---

## 4. Spacing and rhythm

- Section spacing supports **commercial pacing** (see [service-landing-template-v0.md](service-landing-template-v0.md)).
- Whitespace vs density tradeoffs documented.

---

## 5. Consistency

- **Component families** — buttons, cards, icons — reuse patterns vs one-offs.
- **Terminology** matches blueprint copy strategy ([cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md)).

---

## 6. Mobile

- Tap targets, nav pattern, sticky behaviors.
- **Content truncation** — acceptable ellipsis vs loss of critical trust.

---

## 7. Trust posture

- Proof blocks **visibly credible** (no “logo wall” without permission).
- Sensitive claims flagged for **HITL** or removal.

---

## 8. CTA rhythm

- Primary CTA **visible** without unreasonable scroll on key breakpoints.
- Secondary CTAs do not **dilute** primary without documented strategy approval ([cta-semantics-v0.md](cta-semantics-v0.md)).

---

## 9. Findings log

| ID | Area | Severity | Finding | Evidence (screenshot / frame ref) |
|----|------|----------|---------|-------------------------------------|
| | | | | |

Severity mapping: align to project QA vocabulary ([validation-result-semantics-v0.md](validation-result-semantics-v0.md) themes) or blueprint QA checklist.

---

## 10. Escalation

- **Blocker** — cannot hand off to frontend until resolved.
- **Conditional** — proceed with documented waivers per [approval-semantics-v0.md](approval-semantics-v0.md).
- **NEED HUMAN APPROVAL** — brand/legal/compliance per [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 11. Outcome

- [ ] Approve handoff
- [ ] Request revision (link to [revision-cycle-template-v0.md](revision-cycle-template-v0.md))
- [ ] Freeze design scope (semantic freeze alignment)

---

*Template v0 — structured human design gate.*

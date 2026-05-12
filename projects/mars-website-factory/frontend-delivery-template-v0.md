# Operational template — Frontend delivery (v0)

**Status:** **documentation-only** execution scaffold for **static frontend production** aligned with the documented **Gulp Frontend Agent** role ([../../agents/cards/gulp-frontend-agent-v0.md](../../agents/cards/gulp-frontend-agent-v0.md)) and [frontend-production-model.md](frontend-production-model.md). **Not** CI/CD, **not** automated deploy.

**Normative references:** [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [reference-delivery-package-v0.md](reference-delivery-package-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).

---

## 1. Source-first frontend execution

- **Authoritative** assets live in **source** (HTML partials/templates, SCSS, ES modules as scoped); **never** hand-edit **`dist/`** output ([frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)).
- Build commands and environment versions — document in handoff; **SAFE UNKNOWN** if not pinned.

---

## 2. Section integration order

Suggested order (adjust per project):

1. **Layout shell** — header/footer/nav, grid tokens.
2. **Global styles** — typography scale, spacing, breakpoints.
3. **Section blocks** top-to-bottom per approved blueprint wire order.
4. **CTA components** — wire to `data-*` hooks and analytics placeholders (no fake IDs).
5. **Progressive enhancement** — JS behavior behind meaningful markup.

Triumph-shaped reference: [reference-cases/triumph-manipulator-landing/frontend-production-plan-v0.md](reference-cases/triumph-manipulator-landing/frontend-production-plan-v0.md).

---

## 3. Responsive QA

- Breakpoint checklist (mobile / tablet / desktop) — **manual** unless separate tooling is evidenced.
- **Touch targets**, overflow, sticky elements — record findings per [qa-result-payloads-v0.md](qa-result-payloads-v0.md) themes.

---

## 4. Freeze policy

- **Freeze point** before “delivery candidate” labeling ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)).
- **Freeze break** requires revision class + HITL per [revision-semantics-v0.md](revision-semantics-v0.md).

---

## 5. Delivery candidate

- Define **what** constitutes a **delivery candidate** package ([reference-delivery-package-v0.md](reference-delivery-package-v0.md)): e.g. source snapshot hash, build log reference, QA report attachment.
- **Frontend QA fail → invalidates Delivery Candidate** shorthand per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) (documentation routing).

---

## 6. Rollback philosophy

Per [reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md) and [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md):

- **Rollback** is a **human decision** documented with **which artifact version** is restored — **no** “automatic rollback engine” claim.
- Prefer **tagged** source states over mystery copies.

---

## 7. Operator checklist (session-sized)

- [ ] Handoff read and ambiguities logged as **SAFE UNKNOWN**
- [ ] No `dist/` edits
- [ ] REPORT produced with changed paths ([reporting-standard-v0.md](reporting-standard-v0.md))
- [ ] Freeze / invalidation state updated if scope changed

---

## 8. SAFE UNKNOWN

- Exact Gulp pipeline plugins and Node version — **unknown** until repo `package.json` evidence exists in target project (may be outside this pack).

---

*Template v0 — Gulp-oriented discipline without deployment automation claims.*

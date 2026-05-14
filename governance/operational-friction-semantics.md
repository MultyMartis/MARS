# MARS — Operational friction semantics

**Status:** **documented** — vocabulary for **human** diagnosis. **Not** performance profiling, **not** APM, **not** user analytics products.

**Purpose:** Define what **friction** means in MARS so audits and retrospectives can name cost without shaming documentation or pretending that all structure is waste.

---

## 1. Friction (working definition)

**Friction** is any **persistent** extra effort—cognitive, navigational, or procedural—that **does not** buy proportional clarity, safety, or speed for the humans doing the work.

Friction is **relational**: the same page may be low-friction for a maintainer and high-friction for a newcomer.

---

## 2. Common friction patterns (examples)

| Pattern | Symptom sketch |
|---------|----------------|
| **Too many docs** | Multiple entry points; unclear which is SoT. |
| **Duplicated semantics** | Same rule restated; updates miss a copy. |
| **Unclear SoT** | “Which file wins?” disputes recur. |
| **Onboarding exhaustion** | Long read lists; unclear mandatory vs optional. |
| **Helper noise** | Output too chatty, false positives, or ignored. |
| **Governance fatigue** | Updating indexes feels heavier than the work governed. |
| **False-positive overload** | Warnings/checklists that train dismissal. |
| **Unclear stabilization state** | Draft language packaged as normative truth. |
| **Runtime ambiguity** | Language implies execution where only design exists. |
| **Excessive ceremony** | Fields or steps that no reader uses. |
| **Migration overload** | Frequent moves/renames without stable pointers. |

---

## 3. Healthy friction vs destructive friction

### Healthy friction (sometimes desirable)

- Short **pause** before risky edits (explicit approval, second reader).
- **Explicit** UNKNOWN labels instead of silent guessing.
- **Narrow** checklists that catch **specific** classes of mistakes.
- **Lightweight** merge or deprecation steps that prevent silent duplication.

Healthy friction **trades** a small, bounded cost for **measurable** risk reduction or clarity.

### Destructive friction

- Unbounded reading before action.
- Duplicated normative text that **diverges**.
- Helpers or governance steps that **simulate** automation or monitoring without delivering reliability.
- Prestige vocabulary that **hides** missing evidence.

Destructive friction **compounds**: each extra doc or warning increases dismissal and mythology risk (see [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md)).

---

## 4. Related governance

- Entropy and merge posture: [documentation-entropy-rules.md](documentation-entropy-rules.md)
- Operator load: [operator-load-management.md](operator-load-management.md)
- Tooling creep signals: [tooling-escalation-warnings.md](tooling-escalation-warnings.md)
- Audit prompts: [reality-audit-questions.md](reality-audit-questions.md)

---

## 5. SAFE UNKNOWN

Team-specific tolerance for friction—**SAFE UNKNOWN** here. What friction is “worth it” is a **human** judgment per context, not a global constant.

# ORCA Semantic Taxonomy — Design Principles v1

**Principles ID:** `orca-semantic-taxonomy-principles`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Principles

1. **Topic is not intent.** Topical relevance to a service domain does not imply commercial intent or eligibility.
2. **Service-term presence is not a commercial signal by itself.** A query may mention a service noun without requesting provider engagement.
3. **Literal interpretation precedes commercial interpretation.** Record what the phrase says before inferring paid-service intent.
4. **Primary intent describes the user's most likely next task.** Intent is task-oriented, not keyword-category oriented.
5. **Secondary intent records a meaningful competing interpretation.** Use when evidence supports more than one plausible task.
6. **Commercial eligibility is separate from intent class.** `PROBLEM_UNRESOLVED` may yield ACCEPT, REJECT, or ABSTAIN depending on evidence.
7. **Provider-hire signal is separate from transaction signal.** Hiring a provider and buying a product/module are distinct evidence axes.
8. **Problem signal is not automatically provider intent.** A stated problem may indicate DIY, documentation, or support paths.
9. **Product/module intent is separate from service intent.** Product purchase cannot silently collapse into service mapping.
10. **ABSTAIN is mandatory for unresolved ambiguity.** When protected conflicts or competing tasks remain unresolved, automated processing must ABSTAIN.
11. **Rules, models and LLMs produce evidence, not operator authority.** Automated outputs are advisory until human/operator gates pass.
12. **Service mapping occurs only after ACCEPT.** Pre-ACCEPT service fields are candidates only.
13. **Diagnostic status is separate from final decision.** Pipeline stage status must not be conflated with eligibility.
14. **Every decision requires provenance and versioning.** Rule, model, prompt, taxonomy, and guideline versions are mandatory for audit.
15. **No semantic decision may be created during export.** SI-16 is transport-only; export cannot invent or repair semantics.

---

## Consequences

- Taxonomies are multi-axis, not a single label column.
- Fixtures validate schema shape only — they are not benchmark gold labels.
- Old Corvonero phrase labels are forbidden as taxonomy authority.

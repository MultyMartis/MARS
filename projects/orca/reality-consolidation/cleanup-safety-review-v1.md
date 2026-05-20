# Cleanup Safety Review v1

## Status

Safety review for low-risk cleanup planning only. No source files changed.

## Safety Principle

Safe cleanup first. Duplication has cost, but over-cleanup is dangerous. Evidence discipline must survive.

## Risk Review

| Risk | Assessment | Mitigation |
|---|---|---|
| Operator confusion | Medium. Six small templates/checklists can make the operator unsure which one to use. | Prefer one consolidated operator template later. |
| Losing nuance | Medium. Low-evidence and escalation checklists contain safety-critical nuance. | Treat them as merge sources, not deletion targets. |
| Hidden dependencies | Unknown. Other docs or operators may reference these files. | Search references before any execution pass. |
| Over-cleanup | Medium. Removing templates before replacement may reduce usability. | Archive-only or redirect-first strategy. |
| Boundary loss | Low to medium. Boundary text is repeated, but safety meaning matters. | Compress wording only after shared boundary is approved. |
| Evidence discipline degradation | Low in this pass if source scope remains templates/checklists only. | Do not touch core evidence/confidence/contradiction logic. |

## Safest Cleanup Sequence

1. Keep `operational-decision-template-v1.md` as temporary base.
2. Draft one consolidated template in a future approved execution pass.
3. Compare all fields from uncertainty, tradeoff, low-evidence, escalation, and decision quality docs.
4. Compress repeated Status and Boundary text inside the consolidated candidate only.
5. Run human review before archiving any original.
6. Use archive-only before delete.
7. Keep rollback simple by preserving original files until the consolidated template is proven usable.

## Rollback Recommendations

- Do not delete in the first execution pass.
- If files are archived later, keep original path references in an archive map.
- If redirect READMEs are used, include direct links to replacement content.
- Keep `git status --short -uall` before and after each cleanup phase.
- Prefer one small cleanup phase per commit if commits are approved later.

## Stop Conditions

Stop cleanup if:

- operator cannot identify the correct template;
- low-evidence warning disappears;
- escalation triggers are less visible;
- SAFE UNKNOWN is removed from the operator path;
- boundary compression creates ambiguity about automation or business decisions;
- any source reference depends on an original template/checklist;
- consolidated template is longer or harder to use than the originals.

## Safety Finding

The safest actual cleanup target is duplicate template/checklist structure, not core docs. The first execution pass should be reversible and archive-first.

## Boundary

This review does not execute cleanup and does not approve deletion.

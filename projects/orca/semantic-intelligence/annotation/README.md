# ORCA Semantic Annotation — Implementation-Neutral Locus

**Locus:** `projects/orca/semantic-intelligence/annotation/`  
**Status:** `P0-C — ANNOTATION GUIDELINE — APPROVED`  
**Package status:** `APPROVED — IMPLEMENTATION NOT STARTED`

Human annotation and adjudication specification for ORCA Semantic Intelligence v1. Not runtime. Not classifier. Not benchmark dataset.

## Authority

- Approved ADR v1
- Approved P0-B taxonomy and semantic record schema (checkpoint `3151953`)
- Operator approvals A1–A7, B1–B7, C1–C7
- Operator decisions D1–D7

## Structure

| Path | Role |
|------|------|
| `guidelines/` | Annotation handbook and adjudication standards |
| `decision-trees/` | Human decision trees terminating in ACCEPT / REJECT / ABSTAIN |
| `examples/` | Training illustrations — not gold benchmark labels |
| `reviewer-tools/` | Checklists and annotator role model |
| `adjudication/` | Disagreement and escalation policy |
| `quality/` | Quality gates and annotator readiness plan |
| `validation/` | Guideline documentation validation |
| `decisions/` | P0-C decision and operator approval records |
| `reports/` | Task reports |

## Gates

| Item | Status |
|------|--------|
| P0-A ADR | APPROVED — CHECKPOINTED |
| P0-B Taxonomy & Schema | APPROVED — CHECKPOINTED (`3151953`) |
| P0-C Annotation Guideline | APPROVED — IMPLEMENTATION NOT STARTED (C1–C7) |
| P0-D Benchmark Charter | AUTHORIZED — NOT STARTED |
| Benchmark / gold labels | NOT STARTED |
| Classifier | NOT STARTED |
| Corvonero | FROZEN |
| Campaign production | BLOCKED |

## Prohibited in this locus

- Full Corvonero corpus labels
- Gold benchmark rows
- Classifier or runtime code
- Campaign export fields

## Reading order

1. [`guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)
2. Commercial evidence standard
3. Protected non-commercial intent standard
4. Problem query adjudication
5. Product vs service adjudication
6. Short head term adjudication
7. ACCEPT / REJECT / ABSTAIN standards
8. Phrase-specific rationale standard
9. Decision tree
10. Example library and anti-patterns
11. Reviewer checklist and role model
12. Disagreement policy
13. Quality gates
14. P0-C decision record
15. P0-C operator approval record (C1–C7)

# ORCA PPC Semantic Intelligence — Research Review v1

**Review date:** 2026-06-22  
**Reviewer role:** MARS Research Intake and Architecture Governance Maintainer  
**Canonical source:** `ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-v1.md`

---

## 1. Research purpose

Synthesize world practices for building PPC semantic-core systems that separate **topical relevance** from **commercial intent**, with hierarchical gates, abstention, human review, negative intelligence timing, gold datasets, and strict separation between Semantic Core production and Campaign Production — applied to ORCA and the Corvonero clean-room diagnostic.

## 2. Core diagnosis

ORCA (as exercised in Corvonero clean-room v1 pipeline) treats **service topical match** as sufficient evidence for **commercial admission**. Research and platform documentation show that downstream match engines amplify admission errors. A conservative admission policy with explicit abstention is required.

## 3. Strong findings

| Finding | Class |
|---------|-------|
| Search intent ≠ topical relevance | documented external practice + academic support |
| Hierarchical gates outperform single-model admission | researcher inference + academic support |
| Commercial precision on auto-accept is the primary production blocker metric | ORCA recommendation (aligned with cost-sensitive classification literature) |
| Negatives and clusters must follow service ownership | documented platform practice + ORCA recommendation |
| Semantic Core must freeze before campaign production | operator decision D7 + ORCA recommendation |
| Platform broad-match logic must not be upstream ground truth for core admission | documented external practice |

## 4. Source-quality assessment

- **Strengths:** Combines official Google/Yandex documentation references, academic intent-taxonomy papers, and explicit ORCA failure-mode alignment with Corvonero brief.
- **Weaknesses:** Citation markers are not fully URL-resolvable from repository bytes; some academic entries lack full bibliographic metadata in-source.
- **Overall:** Quality sufficient for **analytical source** status and selective promotion — not sufficient for automatic architecture adoption.

## 5. Limitations

- No in-repo validation against ORCA gold benchmark (benchmark not yet built — D5).
- Russian B2B service disambiguation requires domain-expert annotation (not in research alone).
- Research stack recommendations (hybrid LLM, weak supervision) are design proposals — **no implementation claimed**.

## 6. SAFE UNKNOWN

- Exact URLs and publication dates for most external sources (not in canonical bytes).
- Availability of historical search terms / CRM labels for Corvonero benchmark strata.
- Optimal abstention rate in production (research suggests ≥ 0.15 on early releases — not operator-validated yet).
- Whether Triumph-derived laws alone satisfy new Semantic Intelligence layer without new ADR.

## 7. Applicability to ORCA

High. Research directly targets ORCA layer model (20-layer reference architecture in research) and aligns with existing documented contracts:

- `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` — campaign production boundary
- `projects/orca/knowledge/triumph-derived-orca-laws-v1.md` — reusable laws
- `projects/orca/artifacts/approval-gates-contract-v0.md` — HITL gates

Gap: no approved **Semantic Intelligence** architecture ADR or classifier in-repo.

## 8. Applicability to Corvonero

Direct. Clean-room v1 pipeline completed intent screening → commercial eligibility → mapping → clusters → negatives on ~2370 phrases with **1892 accepted** — diagnostic evidence of over-admission. Operator decision D2 freezes this run. Reusable: intake, service scope, MIG ledger, raw/normalized/deduped corpus.

## 9. Confirmed current failure mode

**Topic match mistaken for commercial intent** — evidenced by clean-room v1 accepting career, educational, DIY, regulatory, and navigational strata without production-grade commercial adjudication. Pipeline script `tools/run-clean-room-semantic-pipeline-v1.mjs` applied topical/service-scope heuristics without benchmark-gated thresholds.

## 10. Existing ORCA alignment

| Area | Evidence |
|------|----------|
| Campaign production contract | DOCUMENTED — blocks production without authority chain |
| HITL approval gates | DOCUMENTED |
| Triumph production laws | DOCUMENTED — separation lessons from battle pilot |
| Essential signals — semantic contamination | DOCUMENTED — `essential-signals/semantic-contamination-v1.md` |
| Research layer v0 | DOCUMENTED — human-operated research only |

## 11. Critical ORCA gaps

See gap matrix. Summary: Intent screening, commercial eligibility, adjudication schema, gold benchmark, calibration/threshold gate, Semantic Core authority contract — **ABSENT or PARTIAL** as validated capability.

## 12. Decisions D1–D7

Recorded in `decisions/ORCA-PPC-SEMANTIC-INTELLIGENCE-OPERATOR-DECISIONS-v1.md`:

- **D1** — Adopt selectively as basis for target architecture
- **D2** — Freeze Corvonero v1 as diagnostic
- **D3** — Commercial precision ≥ 0.95; protected FPR ≤ 0.01 per class
- **D4** — Mandatory abstention when commercial intent unsupported
- **D5** — Universal benchmark 1200–2000 + Corvonero pilot 300–500
- **D6** — Canonical research path fixed
- **D7** — Corvonero restart boundary until gates pass

## 13. Selective-promotion recommendation

Promote in order: **P0-A** Architecture ADR → **P0-B** taxonomy/schema → **P0-C** annotation guideline → **P0-D/E** benchmark charters → **P0-F/G** baselines and threshold gate → **P0-H** Semantic Core authority contract.

Do **not** promote research wholesale as runtime or phrase registry.

## 14. Next gate

**ORCA SEMANTIC INTELLIGENCE ARCHITECTURE DECISION RECORD** (promotion backlog P0-A).

---

## Evidence class legend (used above)

| Label | Meaning |
|-------|---------|
| documented external practice | Platform docs or named academic work cited in research |
| researcher inference | Synthesis or recommendation in research report |
| operator decision | D1–D7 recorded in this intake |
| proposed ORCA implementation | Backlog P0-* — not started |

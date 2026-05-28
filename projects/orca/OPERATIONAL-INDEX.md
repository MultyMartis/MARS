# ORCA Operational Index

## Live-First Start

Use this index when an operator needs a fast PPC review session, not a full architecture pass.

## FAST PATH

Default to `fast-path/README.md`.

Recommended default path:

1. Define one PPC object.
2. Open one primary review.
3. Add one support signal only if the decision is blocked.
4. Capture top 3 findings.
5. Make one PPC decision or mark SAFE UNKNOWN.
6. STOP NOW.

Document gravity warning: the main overload risk is opening "just one more document." More ORCA reading is usually not more PPC clarity.

## Minimal Session Path

1. Define one PPC object: query, ad, landing page, or search-term set.
2. Pick one primary review from Starter Core.
3. Add at most one support signal if it changes the decision.
4. Record top 3 findings in `reports/orca-live-session-report-template-v1.md`.
5. Stop.

## Recommended Max Review Depth

- One primary checklist.
- One support signal checklist.
- Top 3 findings.
- One PPC decision or one SAFE UNKNOWN.
- Normal target: 10-20 minutes per PPC object.

## Starter Core

- `fast-review/mobile-serp-review-v1.md` - quick mobile SERP scan.
- `fast-review/landing-mismatch-review-v1.md` - query/ad/landing mismatch check.
- `fast-review/cta-pattern-review-v1.md` - CTA clarity and pressure review.
- `fast-review/mobile-friction-review-v1.md` - mobile conversion friction review.
- `essential-signals/trust-patterns-v1.md` - trust cues worth noting.
- `essential-signals/aggregator-pressure-v1.md` - marketplace and directory pressure.
- `essential-signals/semantic-contamination-v1.md` - non-commercial and mixed-intent leakage.

## STOP ANALYSIS Cues

Stop analysis when:

- STOP NOW: one PPC decision is clear enough;
- STOP NOW: three findings already exist;
- STOP NOW: the next document is being opened "just in case";
- the next note will not change the PPC action;
- the finding is already clear enough for a human decision;
- the evidence is weak and would require guessing;
- the review is becoming a full audit;
- the operator is comparing documents instead of reviewing PPC evidence;
- a platform change needs fresh human confirmation.

## Anti-Fatigue Cues

- Shorter is safer when judgment quality drops.
- Fast Path is the default; Starter Core is not a menu to exhaust.
- Do not open every related document.
- Do not classify every weak term.
- Do not inventory every competitor proof point.
- Mark SAFE UNKNOWN instead of forcing certainty.
- Split the session if a second PPC object appears.

## Assembly Areas

- `search-terms-review/` - semantic cleanliness and negative keyword review.
- `landing-match/` - intent-to-page fit.
- `ad-copy/` - ad message and CTA fit.
- `campaign-qa-assembly/` - final human QA before platform work.

## ORCA Content Export Layer v0

Landing **semantic** export (content packs → DOCX / Markdown → Website Factory). **Not** Commander `exporter-cli`. **Not** runtime.

| Doc | Role |
|-----|------|
| [content-packs/README.md](content-packs/README.md) | Layer entry — pack ≠ HTML |
| [content-packs/OPERATIONAL-INDEX.md](content-packs/OPERATIONAL-INDEX.md) | Reading order, schemas, workflows, exporters |
| [content-packs/export-pipeline-v0.md](content-packs/export-pipeline-v0.md) | Research → pack → export → Factory |
| [content-packs/semantic-lock-export-rules-v0.md](content-packs/semantic-lock-export-rules-v0.md) | MODE 1 export + Factory lock rules |
| [content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md](content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md) | Reference capability pack (Triumph 5 т) |

**Bridge:** approved pack → [intelligence/orca-website-factory-semantic-lock-v0.md](intelligence/orca-website-factory-semantic-lock-v0.md) → Factory handoff ([content-packs/workflows/pack-to-factory-workflow-v0.md](content-packs/workflows/pack-to-factory-workflow-v0.md)).

## ORCA Calibration Layer v0

Human-operated loop: research / packs / PPC ↔ Factory implementation ↔ operational lessons. **Not** analytics or runtime.

| Doc | Role |
|-----|------|
| [calibration/README.md](calibration/README.md) | Layer entry |
| [calibration/OPERATIONAL-INDEX.md](calibration/OPERATIONAL-INDEX.md) | Reading order — first case: Triumph master hot |
| [calibration/orca-calibration-system-v0.md](calibration/orca-calibration-system-v0.md) | System definition + drift philosophy |

**Canonical case v0:** [calibration/triumph-manipulator/](calibration/triumph-manipulator/) — «Аренда манипулятора в Краснодаре» (`grp_fc12_zakaz`, `workspaces/triumph-manipulator-landing-v5/`).

## ORCA Intelligence Foundation v0

Pre-implementation architecture layer — intake, projects, evidence, campaign modes, artifacts, research, Factory semantic lock. **Not** runtime. **Not** orchestration.

| Doc | Role |
|-----|------|
| [orca-operational-principles-v0.md](orca-operational-principles-v0.md) | Layer principles and gate questions |
| [intake/orca-universal-intake-architecture-v0.md](intake/orca-universal-intake-architecture-v0.md) | Raw pack → manifest → normalize → distribute |
| [projects/project-structure-contract-v0.md](projects/project-structure-contract-v0.md) | Canonical per-project folder tree |
| [projects/project-md-contract-v0.md](projects/project-md-contract-v0.md) | `PROJECT.md` navigation and status contract |
| [evidence/evidence-classification-system-v0.md](evidence/evidence-classification-system-v0.md) | Evidence grading vocabulary |
| [campaign-modes/orca-campaign-mode-architecture-v0.md](campaign-modes/orca-campaign-mode-architecture-v0.md) | Search / RSYA / retarget / brand / local / experimental separation |
| [intelligence/orca-website-factory-semantic-lock-v0.md](intelligence/orca-website-factory-semantic-lock-v0.md) | ORCA → Website Factory content lock |
| [intelligence/orca-factory-bridge-index-v0.md](intelligence/orca-factory-bridge-index-v0.md) | ORCA → Factory handoff flow index |
| [artifacts/orca-artifact-system-v0.md](artifacts/orca-artifact-system-v0.md) | Artifact types and lifecycle |
| [artifacts/approval-gates-contract-v0.md](artifacts/approval-gates-contract-v0.md) | HITL approval gates (no auto-launch) |
| [research/orca-research-layer-v0.md](research/orca-research-layer-v0.md) | Human-operated research collection |

**Contracts (v0):** [landing-route-registry-contract-v0.md](intelligence/landing-route-registry-contract-v0.md) · [ppc-landing-qa-contract-v0.md](intelligence/ppc-landing-qa-contract-v0.md) · [competitor-snapshot-contract-v0.md](research/competitor-snapshot-contract-v0.md) · [research-session-snapshot-contract-v0.md](research/research-session-snapshot-contract-v0.md) · [moderation-incident-registry-v0.md](moderation/moderation-incident-registry-v0.md)

**Intake drop zone:** `incoming/orca/<project-id>-raw-pack/` (see intake architecture).

## Project operational packs

- `ppc/triumph-manipulator/` - Triumph Manipulator search PPC pack (doctrine, intent tiers, landing blueprints, Commander export foundation). Start: `ppc/triumph-manipulator/OPERATIONAL-INDEX.md`. Relationship to Intelligence Foundation: [ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md](ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md).

## Reality Audit

- `reality-audit/operator-fatigue-review-v1.md`
- `reality-audit/workflow-friction-review-v1.md`
- `reality-audit/low-value-layer-review-v1.md`
- `reality-audit/starter-core-survivability-v1.md`

## Boundaries

ORCA is a human-supervised PPC operational toolkit. It does not bid, launch, optimize, schedule, validate, or orchestrate campaigns.

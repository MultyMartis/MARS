# MARS Website Factory - Trust Drift Taxonomy

**Status:** **documented** - Website Factory trust drift vocabulary and human-supervised credibility review aid only.  
**Not:** automated trust detection, runtime scoring, universal trust law, credibility certification, or complete failure prediction.

**Parent governance:** [trust-calibration-governance.md](trust-calibration-governance.md).  
**Companion model:** [governance-credibility-model.md](governance-credibility-model.md).  
**Forge checklist:** [`../../agents/mars-forge/trust-calibration-checklist.md`](../../agents/mars-forge/trust-calibration-checklist.md).

---

## 1. Purpose

This taxonomy names trust drift patterns that appear when governance looks credible, confident, mature, or thorough while its reliability, evidence, uncertainty, and survivability are weaker than perceived.

Trust drift is dangerous because it can make operators:

- believe confidence that evidence does not support;
- ignore uncertainty because reports look polished;
- treat governance reputation as proof;
- continue through authority gaps;
- lose trust sharply after a preventable failure.

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical signal | Required response |
|---------------|------------|----------------|-------------------|
| **False trust escalation** | Trust rises because a report sounds stronger, not because evidence improved. | Assertive PASS, mature tone, or dense checklist after partial evidence. | Narrow the trust claim and expose evidence boundary. |
| **Governance overconfidence** | Governance claims excessive certainty, authority, coverage, or reliability. | "Fully verified" from source-only, build-only, screenshot-only, or inferred checks. | Reclassify as scoped PASS, PARTIAL, HITL, or SAFE UNKNOWN. |
| **Credibility erosion** | Repeated overstatements weaken belief in the governance system. | Operators stop trusting reports after hidden gaps surface. | Record drift, restore transparency, and reduce confidence language. |
| **Confidence-performance mismatch** | Declared confidence does not match actual system behavior or verification coverage. | Strong confidence followed by unverified responsive, state, interaction, or accessibility failure. | Reconcile confidence with observed performance and update proof boundary. |
| **Trust inflation** | Perceived trust grows through repetition, polish, or institutional familiarity. | "This layer usually catches it" without current evidence. | Require current-scope evidence and reviewable rationale. |
| **Perceived reliability drift** | The system appears more reliable than its evidence supports. | Long report, many links, strong wording, weak direct checks. | Separate rendered confidence from evidence-backed trust. |
| **Institutional overtrust** | Operators rely on Website Factory or Forge because it is established, not because this case is proven. | Governance reputation substitutes for current QA or escalation. | Make institutional trust reviewable and bounded. |
| **Blind governance reliance** | Humans stop inspecting rationale because governance output feels authoritative. | "Trust the checklist" instead of evidence review. | Restore reasoning visibility and trust traceability. |
| **Credibility collapse after failure** | Trust breaks sharply because prior confidence hid known limits. | Failure reveals missing uncertainty disclosure. | Document failure boundary and improve credibility survivability. |
| **False-certainty trust** | Unknowns are converted into reliable-looking conclusions. | Assumptions, inferred checks, or missing devices reported as passed. | Re-label unknowns and disclose uncertainty impact. |
| **Performative confidence** | Confidence is created by tone, polish, structure, or ceremony. | Professional report implies reliability without proof. | Replace performance signals with evidence, scope, and unknowns. |
| **Unverifiable trust signaling** | Trustworthiness is asserted without traceable evidence. | "Reliable," "mature," "safe," or "trusted" with no proof path. | Require trust traceability or mark SAFE UNKNOWN. |
| **Survivability-to-trust mismatch** | Trust granted is stronger than the system's ability to survive failure, handoff, recovery, or future review. | High confidence with weak recovery, context, or continuity evidence. | Reduce trust claim and record survivability gap. |

---

## 3. Anti-Pattern Families

### 3.1 Confidence Aesthetics

Trust drift caused by how governance looks or sounds.

- confidence inflation;
- fake certainty;
- performative confidence;
- professional-tone trust;
- polished unreliability;
- report-length credibility.

**Rule:** presentation may improve readability, but it must not increase trust beyond evidence.

### 3.2 Evidence Mismatch

Trust drift caused by claims exceeding verification.

- source-only confidence escalation;
- build-success trust illusion;
- screenshot certainty drift;
- inferred validation treated as proof;
- partial QA reported as full reliability;
- unverified state, interaction, responsive, accessibility, or recovery claims.

**Rule:** evidence type defines the trust boundary.

### 3.3 Institutional Reliance Drift

Trust drift caused by treating governance reputation as current proof.

- institutional overtrust;
- blind governance reliance;
- checklist authority inflation;
- maturity-signaling trust;
- prior-success overgeneralization;
- governance mythology.

**Rule:** institutional trust must remain reviewable and current-scope evidence must stay visible.

### 3.4 Failure-Survivability Drift

Trust drift caused by confidence that cannot survive failure.

- credibility collapse after failure;
- hidden uncertainty debt;
- rollback trust illusion;
- recovery confidence inflation;
- continuity-trust weakness;
- survivability-to-trust mismatch.

**Rule:** strong trust requires visible failure posture, not just strong current claims.

---

## 4. Detection Questions

Use these questions during review:

- What evidence caused trust to increase?
- Is confidence stronger than direct verification?
- Does the report look more reliable than the checks actually are?
- Are unknowns visible enough to preserve credibility after failure?
- Is institutional governance being treated as proof?
- Can a future operator trace the trust claim to evidence, rationale, and uncertainty?
- Would credibility survive if an unverified area fails?
- Are escalation boundaries protecting trust or hiding trust risk?
- Does report length improve credibility density or create trust theater?

---

## 5. Reporting Guidance

When naming trust drift, record:

```text
TRUST CALIBRATION FINDINGS

- Drift pattern: <taxonomy name>
- Trust claim affected: <PASS / freeze / recommendation / escalation / institutional reliance>
- Evidence boundary: <direct / inferred / source-only / build-only / screenshot-only / unknown>
- Confidence adjustment: <keep / narrow / downgrade / escalate / SAFE UNKNOWN>
- Credibility risk: <why trust may erode or fail to survive>
```

---

## 6. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Drift pattern is suspected but evidence is incomplete | Cannot classify trust risk accurately. |
| Confidence source is unclear | Cannot tell why trust increased. |
| Credibility depends on presentation | Cannot prove evidence-backed trust. |
| Institutional reliance is unreviewed | Cannot know whether trust is current or inherited. |
| Failure survivability is not visible | Cannot know whether credibility would survive a gap. |
| Trust traceability is missing | Cannot reconstruct trust basis later. |

**Action:** name the suspected drift, state the missing evidence, reduce or qualify confidence, and route unresolved trust questions to HITL or SAFE UNKNOWN.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial trust drift taxonomy - false trust escalation, governance overconfidence, credibility erosion, confidence-performance mismatch, trust inflation, perceived reliability drift, institutional overtrust, blind governance reliance, credibility collapse after failure, false-certainty trust, performative confidence, unverifiable trust signaling, and survivability-to-trust mismatch; documentation only. |

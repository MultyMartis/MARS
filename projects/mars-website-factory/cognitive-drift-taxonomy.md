# Cognitive Drift Taxonomy

**Status:** **documented** - Website Factory taxonomy for cognitive-load and review-ergonomics drift only.  
**Parent layer:** [cognitive-load-governance.md](cognitive-load-governance.md).  
**Not:** automated drift detection, cognitive surveillance, universal cognition theory, or perfect readability guarantee.

---

## 1. Purpose

Cognitive drift is the failure mode where governance remains extensive, detailed, traceable, or sophisticated while becoming too exhausting, unreadable, fragmented, or noisy for human review to survive.

This taxonomy gives operators names for those failures so they can be reported, reduced, escalated, or classified as **SAFE UNKNOWN**.

---

## 2. Drift Patterns

| Drift pattern | Meaning | Typical symptom | Governance response |
|---------------|---------|-----------------|---------------------|
| **Reviewer fatigue** | Review quality declines because the report demands too much sustained attention. | Later findings are skimmed or treated as equal priority. | Summarize critical path, group low-value findings, reduce density. |
| **Cognitive overload** | The reviewer cannot hold enough context to make a safe decision. | Many layers, terms, findings, and unknowns compete at once. | Select review layer, prioritize, defer or escalate non-critical depth. |
| **Unreadable reporting** | Detail exists but does not produce clear action. | Findings describe categories without consequence or next step. | Rewrite findings around risk, evidence, disposition, and action. |
| **Attention fragmentation** | Review attention is split across too many equally presented concerns. | Cosmetic, operational, escalation, and critical issues look similar. | Apply risk weighting and signal prioritization. |
| **Governance exhaustion** | Operators become tired of the governance process itself. | Checklists are completed mechanically or skipped. | Use minimalism, economics, adaptive depth, and cognitive-load review. |
| **Signal-to-noise erosion** | Useful signal is diluted by low-value observations. | Critical issues are hard to find inside report volume. | Group noise, lead with blockers, demote informational content. |
| **Review paralysis** | The reviewer cannot decide because the report presents too much unresolved material. | No clear stop, fix, defer, HITL, or continue action. | State next safe action and escalate unresolved authority. |
| **Operator burnout** | Repeated governance cycles become unsustainable for the human operator. | Quality declines across sessions or future reviews become avoided. | Reduce mandatory density and preserve sustainable review cadence. |
| **Governance readability collapse** | The governance method is too dense to explain or resume. | Future operators cannot understand the report path. | Restore operational readability and continuity summary. |
| **Information-density overload** | Evidence volume exceeds decision value. | Many details are accurate but not useful for the current decision. | Keep material evidence, archive or defer supporting detail. |
| **Endless-report drift** | Reports expand by habit until they are no longer reviewable. | Every layer produces a full block regardless of relevance. | Select proportional review layer and apply optional-depth discipline. |
| **Review-survivability erosion** | The ability of the report to survive human review weakens over time. | Dense reporting appears complete but fails handoff or review. | Run cognitive-load QA and record `COGNITIVE LOAD FINDINGS`. |
| **Cognitive continuity failure** | A future reviewer cannot reconstruct what mattered after compression or handoff. | Priorities and rationale are lost despite extensive detail. | Preserve critical-path summary, unknowns, and next safe action. |

---

## 3. Secondary Drift Cues

Use these cues to recognize cognitive drift early:

- findings are numerous but not ordered by consequence;
- every governance layer demands full attention;
- the report becomes harder to scan after each added section;
- terms multiply faster than decision value;
- critical issues appear only after long context;
- summaries hide uncertainty while details hide priority;
- reviewers need private memory to understand the report;
- report volume creates trust pressure without better proof;
- "more detail" becomes the default answer to uncertainty.

---

## 4. Severity Guidance

| Severity | Use when |
|----------|----------|
| **Informational** | Minor density issue exists but critical signal remains visible. |
| **Operational** | Report readability or attention allocation affects review efficiency or handoff. |
| **Continuity** | Future operators may lose priority, rationale, or next action after compression or handoff. |
| **Escalation** | Cognitive overload blocks a human-owned decision, approval, waiver, or contradiction resolution. |
| **Critical** | Critical risk, freeze readiness, delivery confidence, accessibility trust, or source authority may be missed because signal is buried. |

---

## 5. Anti-Patterns

Forbidden cognitive drift:

- endless reports;
- unreadable findings;
- review overload;
- governance verbosity inflation;
- signal burial;
- information-pressure escalation;
- cognitive exhaustion;
- process readability collapse;
- reviewer burnout;
- "more detail always better";
- treating report length as confidence;
- treating every finding as equally review-worthy;
- hiding cognitive overload behind professional formatting.

---

## 6. Relation to Adjacent Drift Taxonomies

| Adjacent taxonomy | Boundary |
|-------------------|----------|
| [governance-bloat-taxonomy.md](governance-bloat-taxonomy.md) | Names governance complexity and rule/checklist bloat. Cognitive drift names human review collapse caused by that or other density pressure. |
| [governance-cost-drift-taxonomy.md](governance-cost-drift-taxonomy.md) | Names operational cost waste. Cognitive drift names attention and readability failure even when cost is accepted. |
| [prioritization-drift-taxonomy.md](prioritization-drift-taxonomy.md) | Names priority collapse. Cognitive drift includes priority collapse when it causes review fatigue or unreadability. |
| [reasoning-drift-taxonomy.md](reasoning-drift-taxonomy.md) | Names opaque rationale. Cognitive drift names excessive or poorly placed rationale that reviewers cannot process. |
| [trust-drift-taxonomy.md](trust-drift-taxonomy.md) | Names overtrust and credibility failures. Cognitive drift names report pressure that can produce overtrust or missed uncertainty. |

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- cognitive drift may exist but evidence is insufficient;
- critical signal visibility cannot be verified;
- reviewer fatigue or overload is suspected but not localized;
- report compression could hide material evidence;
- the right balance between detail and readability is unclear;
- future-review survivability cannot be established.

**Action:** name the suspected drift pattern, identify what signal must remain visible, classify severity, and choose: compress, reorder, group, defer, expand only material evidence, escalate, or preserve as SAFE UNKNOWN.

---

*Documentation only - no runtime enforcement.*

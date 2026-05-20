# MARS Website Factory - Strategic Drift Taxonomy

**Status:** **documented** - Website Factory vocabulary for human-supervised strategic drift review.  
**Not:** automated drift detector, marketing optimizer, analytics model, universal conversion taxonomy, or runtime enforcement.

**Parent governance:** [strategic-intent-governance.md](strategic-intent-governance.md).  
**Continuity model:** [business-intent-continuity-model.md](business-intent-continuity-model.md).  
**Forge checklist:** [`../../agents/mars-forge/strategic-intent-checklist.md`](../../agents/mars-forge/strategic-intent-checklist.md).

---

## 1. Purpose

This taxonomy gives operators a shared vocabulary for naming strategic/business drift in frontend work.

Strategic drift can exist when a frontend:

- looks modern;
- passes QA;
- feels responsive;
- appears polished;
- preserves local semantics;
- avoids obvious implementation bugs.

The failure is deeper: business intent, conversion structure, trust, proof authority, operational seriousness, or stakeholder priorities were weakened during translation.

---

## 2. Drift Families

| Family | Core risk |
|--------|-----------|
| **Conversion drift** | The approved action path weakens, inflates, fragments, or changes role. |
| **Proof drift** | Evidence loses hierarchy, credibility, placement, or authority. |
| **Trust drift** | Operational seriousness is replaced by noise, decoration, pressure, or fake premium signals. |
| **Stakeholder drift** | Approved business priorities are overwritten by agent, template, design, or local UI assumptions. |
| **Local optimization drift** | A local "improvement" damages the global strategy. |
| **Message drift** | Business meaning fragments, genericizes, or contradicts the approved intent. |

---

## 3. Drift Patterns

| Drift pattern | Description | Typical symptom | Response |
|---------------|-------------|-----------------|----------|
| **Conversion-goal erosion** | The main business action becomes less clear or less compelling. | CTA exists but no longer feels like the page's decision path. | Review CTA role, proof support, and section priority. |
| **CTA dilution** | Primary CTA loses strategic dominance through competing buttons, links, cards, or microcopy. | Secondary actions visually or behaviorally rival primary action. | Restore hierarchy or record HITL if source conflict exists. |
| **Proof flattening** | Strong and weak proof receive equal treatment. | Certificates, reviews, specs, badges, and claims all read as equal cards. | Re-rank proof and preserve decisive evidence. |
| **Aesthetic-first contamination** | Visual taste overrides business hierarchy. | Page looks more stylish but less clear about priority, action, or trust. | Compare against strategic source intent. |
| **Operational seriousness collapse** | Serious commercial tone becomes playful, generic, SaaS-like, or fake premium. | Motion, glow, rounded cards, badges, or soft copy lower stakes. | Restore proportionate seriousness or escalate tone ambiguity. |
| **Stakeholder-intent overwrite** | Approved business priorities are replaced without authority. | Copy, CTA, or proof changes because the agent/template "improved" it. | Stop and identify authority chain. |
| **Engagement-maximization drift** | Engagement devices are prioritized over trust and decision clarity. | Pulsing CTAs, animations, hover effects, sticky pressure, gamified feedback. | Remove or justify by source/HITL. |
| **Local optimization destruction** | A local section fix damages global conversion, proof, or message flow. | A cleaner card grid inverts priority or buries proof near CTA. | Review page-level strategy before freeze. |
| **Strategic hierarchy inversion** | Secondary content becomes more prominent than primary business meaning. | Process, FAQ, badges, or support details lead over the offer. | Restore business-priority order. |
| **Business-message fragmentation** | The page contains correct fragments that no longer form one strategic story. | Each section reads fine alone but the overall offer path is unclear. | Reconnect claim, proof, objection, action, and trust sequence. |
| **Trust erosion through styling** | Styling choices reduce credibility despite visual polish. | Fake luxury, heavy glow, over-cardization, noisy icons, or badge saturation. | Shift from decorative trust to real proof hierarchy. |
| **Proof saturation** | Too much evidence appears at once and reduces credibility. | Logos, reviews, metrics, seals, and claims form trust wallpaper. | Pace proof and isolate decisive evidence. |
| **Decorative conversion inflation** | Conversion elements are visually amplified without strategic role. | Buttons, badges, arrows, urgency labels, and CTA panels appear everywhere. | Demote decorative action pressure and preserve role hierarchy. |

---

## 4. Anti-Patterns

Forbidden strategic drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Engagement-over-trust** | Treats attention as success even when credibility declines. |
| **CTA spam** | Multiplies action pressure until conversion hierarchy collapses. |
| **Proof overload** | Confuses evidence volume with authority. |
| **Decorative seriousness** | Simulates seriousness through styling rather than proof and clear hierarchy. |
| **Fake premium business styling** | Imports expensive-looking effects that may contradict operational credibility. |
| **Conversion inflation** | Promotes every action as high-urgency or primary. |
| **Stakeholder intent overwrite** | Replaces approved business priority with agent or template judgment. |
| **Aesthetic-first redesign** | Optimizes look while damaging strategy. |
| **Strategic flattening** | Makes claim, proof, CTA, detail, and support content equal weight. |
| **Business-message dilution** | Turns specific business meaning into generic marketing phrasing. |

---

## 5. Severity Guidance

| Severity | Use when | Example |
|----------|----------|---------|
| **Low** | Drift is possible but not proven; source authority still supports continuation. | Minor proof pacing concern with no CTA impact. |
| **Medium** | Drift weakens one strategic layer but can be repaired or disclosed. | Secondary CTA competes with primary in one section. |
| **High** | Drift materially changes business priority, proof authority, conversion path, or trust. | Main proof is buried and all CTAs read equal. |
| **Blocked** | Authority is missing or contradictory and implementation would decide strategy by assumption. | Stakeholder source says consultation CTA, design says buy-now CTA, no resolver. |

Severity should be tied to business effect, not visual annoyance.

---

## 6. Detection Prompts

Use these prompts during Forge strategic intent QA:

- Did the primary business objective survive this implementation?
- Did the CTA still perform the same strategic role?
- Did proof remain credible, ranked, and placed at the right decision beat?
- Did any local polish weaken the global conversion story?
- Did operational seriousness improve, survive, or collapse?
- Did stakeholder-specific meaning become generic?
- Did responsive collapse invert strategic priority?
- Did animation or interaction increase engagement while lowering trust?
- Did QA pass language hide strategic uncertainty?
- Is any strategy being inferred from an implementation artifact without source lineage?

---

## 7. Reporting Format

Use taxonomy names in `STRATEGIC INTENT FINDINGS`.

```text
STRATEGIC INTENT FINDINGS - <section or scope>

Strategic source: <artifact / HITL / SAFE UNKNOWN>
Business priority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Conversion hierarchy: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Proof hierarchy: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Operational trust: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Stakeholder intent: PASS | PARTIAL | FAIL | SAFE UNKNOWN

Drift pattern(s): <taxonomy names>
Disposition: PASS | PARTIAL | FAIL | HITL REQUIRED | STOP
Evidence / unknowns: <short scope>
```

Do not use this block to claim automatic strategic understanding. It records a human-supervised governance read.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Business objective is not stated | Cannot assess conversion-goal erosion. |
| CTA role is not authorized | Cannot classify CTA dilution vs valid variation. |
| Proof priority is not known | Cannot distinguish proof hierarchy from proof overload. |
| Stakeholder source is absent | Cannot identify overwrite or authority continuity. |
| Operational seriousness is ambiguous | Cannot determine tone drift by taste. |
| Existing page is the only evidence | Cannot know whether current strategy is approved or drifted. |

**Action:** name the missing authority, state risk level, and escalate when implementation would decide business strategy.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Strategic Drift Taxonomy - conversion-goal erosion, CTA dilution, proof flattening, aesthetic-first contamination, operational seriousness collapse, stakeholder overwrite, engagement drift, local optimization destruction, hierarchy inversion, message fragmentation, trust erosion, proof saturation, and decorative conversion inflation; documentation only. |

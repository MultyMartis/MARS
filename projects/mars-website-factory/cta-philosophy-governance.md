# MARS Website Factory — CTA Philosophy Governance

**Status:** **documented** — human-supervised CTA intent and visual-governance methodology.  
**Not:** A/B testing engine, conversion guarantee, behavioral manipulation system, runtime optimization, or universal CTA prescription.

**Purpose:** Define Website Factory's preferred commercial philosophy for CTA dominance, restraint, repetition, tone, and pacing.

**Parent layer:** [Design System Intent Governance](design-system-intent-governance.md).  
**Related semantics:** [cta-semantics-v0.md](cta-semantics-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md).  
**Related visual model:** [UI Weight Distribution Model](ui-weight-distribution-model.md).

---

## 1. Core Principle

CTAs are user obligations, not pressure devices.

They should make the next step clear, commercially useful, and visually paced. A strong CTA is not automatically a louder CTA. Dominance must match section role, user readiness, and trust context.

---

## 2. Primary CTA Dominance

Primary CTA dominance is appropriate when:

- the section is a hero, lead capture, quote request, booking, or final conversion point;
- the user has enough context to act;
- the action is truthful, specific, and technically supported;
- surrounding visual weight does not create competing primaries.

Primary CTA drift:

- primary button shares equal treatment with secondary action;
- primary appears too often in the same viewport;
- primary color is reused on badges, icons, or decorative accents;
- primary CTA is visually strong but semantically vague.

---

## 3. Secondary CTA Restraint

Secondary CTAs should support confidence or navigation without stealing conversion focus.

Acceptable secondary roles:

- learn more;
- view proof/cases/specs;
- call/message as an alternate path;
- continue to catalog or details;
- defer high-friction action until trust improves.

Restraint patterns:

- outline button;
- text link;
- lower-contrast button;
- smaller surface;
- separated placement after primary.

Secondary CTA must not become a second primary through size, contrast, icon weight, shadow, or placement.

---

## 4. Outline CTA Behavior

Outline CTA is not a neutral decoration. It carries specific intent:

| Outline use | Meaning |
|-------------|---------|
| **Secondary action** | Visible but restrained; supports primary path. |
| **Proof navigation** | Moves user to confidence-building content. |
| **Low-friction alternate** | Provides non-conversion next step without pressure. |
| **Dark/light balance** | Maintains CTA presence where solid button would be too heavy. |

Drift:

- outline border too heavy, making it rival primary;
- outline text color too high-contrast in dense areas;
- outline used as primary because designer wanted “modern” style;
- outline repeated until CTA hierarchy becomes noisy.

---

## 5. Conversion Pacing

Conversion pacing is the rhythm of asking.

Rules:

- Early CTAs should match user readiness.
- Dense proof and specs may need CTA breathing before conversion ask.
- Repeated CTAs should appear at meaningful narrative transitions, not after every small block.
- CTA after a light/dark transition may need cadence reset.
- Mobile CTA repetition must preserve tap safety and avoid fatigue.

CTA pacing is part of cadence governance, not isolated button styling.

---

## 6. CTA Repetition Drift

CTA repetition drift happens when the page repeats the same action without added user value.

Symptoms:

- identical CTA after every section;
- multiple primary buttons visible in one viewport;
- CTA blocks inserted to “increase conversion” without trust or narrative reason;
- sticky/floating CTA competing with in-section CTA;
- footer CTA styled like a second hero without source authority.

Repetition is valid only when it follows a meaningful change in user state: after proof, after explanation, after pricing/specs, after FAQ objection handling, or at closure.

---

## 7. CTA Fatigue

CTA fatigue is the reader's perception that the page asks too often or too aggressively.

Typical causes:

- loud primary treatment repeated without pacing;
- aggressive urgency copy;
- oversized buttons in dense sections;
- multiple contact channels all styled as primary;
- CTA clusters crowding proof, forms, or helper text.

Mitigation:

- reduce secondary visual weight;
- replace some conversion asks with proof/navigation;
- increase breathing around true conversion moments;
- clarify action specificity instead of increasing button size.

---

## 8. Operational CTA Tone

Website Factory preferred tone is commercially serious and operational:

- specific action labels;
- clear expectation after click/submission;
- no fake scarcity;
- no coercive urgency;
- no manipulative microcopy;
- no bait-and-switch promises;
- no “premium” performance theater through glow, animation, or exaggerated button mass.

Examples of operational tone:

- “Request estimate”
- “Discuss delivery”
- “Get consultation”
- “View specifications”
- “Call dispatcher”

Avoid generic pressure:

- “Claim your exclusive offer now!!!”
- “Don't miss out”
- “Only today” unless legally and operationally true.

---

## 9. Anti-Aggressive Conversion Rules

Forbidden drift:

| Drift | Why it is forbidden |
|-------|---------------------|
| **CTA screaming** | Visual pressure substitutes for trust and clarity. |
| **Fake urgency** | Creates dishonest commercial pressure. |
| **Primary spam** | Destroys pacing and makes all asks weaker. |
| **Equal dual primaries** | User cannot tell the intended path. |
| **Sticky CTA conflict** | Persistent CTA competes with section-specific CTA. |
| **Conversion before trust** | High-friction ask appears before enough proof/context. |
| **Consent hiding** | Form CTA obscures data usage or required terms. |
| **Aggressive glow/elevation** | Visual effects create fake importance. |

---

## 10. CTA Surface and Weight

CTA weight must be evaluated together with:

- section role;
- surface hierarchy;
- surrounding proof;
- visual density;
- mobile stacking;
- page-level CTA count;
- user readiness.

Use [UI Weight Distribution Model](ui-weight-distribution-model.md) when CTA feels too heavy, too weak, or too repeated.

---

## 11. Forge QA Prompts

Use during design intent QA:

- What is the primary CTA in this section?
- Is there exactly one primary path in the viewport unless the source explicitly says otherwise?
- Does secondary CTA stay subordinate?
- Does CTA placement follow user readiness?
- Does repeated CTA add new value or create fatigue?
- Does CTA tone match operational seriousness?
- Does mobile stacking preserve CTA hierarchy?
- Are contact channels visually ranked, or all shouting?

---

## 12. REPORT Block

Use inside **DESIGN INTENT FINDINGS** or standalone when CTA philosophy is the main concern:

```text
CTA PHILOSOPHY FINDINGS — <section or block_id> — <source ref>

CTA hierarchy: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Primary CTA:
- Secondary CTA:
- Outline / link behavior:
- Equal-primary risk:

Conversion pacing: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- User readiness:
- Repetition drift:
- CTA fatigue risk:
- Mobile CTA behavior:

Tone / restraint: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Operational tone:
- Anti-aggressive conversion:
- Consent / expectation clarity:

Disposition:
- Freeze impact:
- Deferrals / resolver:
```

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- primary CTA role is not identified by source or handoff;
- multiple CTAs exist without hierarchy authority;
- CTA destination/backend is undefined;
- copy implies urgency that cannot be verified;
- mobile CTA behavior is not chartered;
- project deliberately requests aggressive campaign style but approval is absent.

**Action:** request CTA hierarchy note, conversion objective, backend/destination confirmation, mobile source, or HITL decision.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial CTA philosophy governance model. |

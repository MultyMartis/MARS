# ORCA Recommended Operator Stack v1

## Status

Recommended minimal stack for a small PPC operator session.

This stack is extracted from pilot findings. It does not redesign ORCA.

## Use Case

- local service campaign;
- one city or tight region;
- small search campaign;
- one landing page;
- one operator;
- review time under one focused session.

## The Small Stack

### 1. Start Path

Layer:

- `minimal-real-pilot-workflow-v1.md`

Use for:

- niche and region;
- seed queries;
- mobile / desktop review order;
- competitor sample;
- semantic risks;
- confidence and SAFE UNKNOWN.

Operator rule:

`This is the map. Do not open the whole ORCA tree.`

### 2. Session Guard

Layer:

- `session-execution-guide-v1.md`

Use for:

- time limits;
- stop rules;
- minimum outputs;
- preventing documentation drift.

Operator rule:

`If notes grow but the PPC decision does not improve, stop.`

### 3. Fast Review Compression

Layer:

- `fast-review/fast-review-workflow-v1.md`

Use for:

- dominant SERP pressure;
- obvious CTA, trust, local, semantic, landing, and mobile signals;
- short operator action.

Operator rule:

`Capture only what changes action.`

### 4. Signal Filter

Layer:

- `essential-signals/essential-signals-model-v1.md`

Use for:

- separating useful evidence from noise;
- preventing observation inflation.

Operator rule:

`Signal quality beats signal volume.`

### 5. Search-Term Cleanliness

Layer:

- `search-terms-review/search-term-cleanliness-rules-v1.md`

Use for:

- service match;
- commercial intent;
- geo match;
- wrong modifiers;
- DIY, vacancy, materials, comparison, or low-intent risks;
- negative keyword candidates.

Operator rule:

`Clean intent first. Do not overblock from weak evidence.`

### 6. Landing Match

Layer:

- `landing-match/landing-match-boundaries-v1.md`

Use for:

- query-to-page fit;
- CTA support;
- trust evidence;
- price claim support;
- mobile usability;
- business reality.

Operator rule:

`Record observed friction. Do not infer conversion certainty.`

### 7. Ad Copy Safety

Layer:

- `ad-copy/ad-copy-boundaries-v1.md`

Use for:

- avoiding fake urgency;
- avoiding unsupported prices, guarantees, and superiority claims;
- keeping copy aligned with landing and business reality.

Operator rule:

`Say only what the business can prove.`

### 8. Final QA Guard

Layer:

- `campaign-qa-assembly/campaign-qa-boundaries-v1.md`

Use for:

- final human review reminder;
- launch-readiness caution;
- marking unknowns before spend.

Operator rule:

`This does not approve launch. It prevents false readiness.`

### 9. Evidence Guard

Layer:

- `operator-decisions/templates/evidence-review-template-candidate-v1.md`

Use for:

- evidence source;
- evidence strength;
- confidence;
- SAFE UNKNOWN;
- escalation need.

Operator rule:

`Use one short line per field. Do not fill a giant form.`

## Default Session Order

1. Minimal workflow.
2. Session guide.
3. Fast review.
4. Search-term cleanliness.
5. Landing match.
6. Ad copy safety.
7. Final QA guard.
8. Evidence guard only for risky decisions.

## Hard Stop

Stop the session when the operator can identify:

- the risky intent;
- the landing mismatch;
- the claim that needs proof;
- the mobile CTA issue;
- the next action: revise, collect evidence, escalate, or stop.

More ORCA layers should not be opened unless they change that decision.

# Duplication Review v1

## Status

Manual duplication review. No files merged, deleted, moved, or rewritten.

## Reality Note

ORCA is becoming large. Repeated methodology is now a usability risk. Documentation growth can look like progress while slowing the operator down.

## Main Overlapping Layers

| Overlap area | Layers involved | Duplication finding | Cleanup direction |
|---|---|---|---|
| Semantic review | `semantic`, `search-terms-review`, `campaign-qa-assembly`, `qa`, `failure-patterns`, `essential-signals`, `fast-review`, `minimalism` | Semantic contamination, wrong-intent traffic, and semantic cleanliness repeat across many layers. | Keep `semantic` as source, `search-terms-review` as spend-quality application, and reference from QA layers. |
| Landing mismatch | `landing-match`, `campaign-qa-assembly`, `qa`, `failure-patterns`, `essential-signals`, `fast-review`, `minimalism` | Landing clarity, CTA support, mobile friction, and ad-to-landing consistency repeat. | Keep `landing-match` as source and `campaign-qa-assembly` as final check. |
| Trust logic | `offer-evaluation`, `landing-match`, `ad-copy`, `ad-extensions`, `essential-signals`, `failure-patterns`, `fast-review`, `intelligence`, `heuristics` | Trust proof, guarantees, reviews, credibility, and trust collapse repeat. | Keep trust where it changes copy, offer, or landing action; remove theoretical trust commentary. |
| Risk logic | `qa`, `campaign-qa-assembly`, `failure-patterns`, `operator-decisions`, `fast-review`, `essential-signals`, `review`, `confidence` | Risk capture, evidence, escalation, and SAFE UNKNOWN repeat heavily. | Centralize risk language in `evidence` / `operator-decisions`; keep only applied checks in operational layers. |
| Evidence and uncertainty | `evidence`, `confidence`, `contradictions`, `observations`, `operator-decisions`, `review`, `live-observations` | Evidence quality, uncertainty, contradiction handling, and confidence discipline overlap. | Consolidate later into one evidence/reality review family. |
| Methodology control | `methodology`, `review`, `minimalism`, `compression`, `fast-review`, `operator-decisions` | Anti-overanalysis, stop rules, and review discipline repeat. | Keep `minimalism` and `compression`; compress generic methodology docs. |
| Pattern libraries | `patterns`, `heuristics`, `heuristic-mapping`, `failure-patterns`, `essential-signals` | Patterns, heuristics, signals, and failure patterns are adjacent concepts. | Treat as optional reference; require pilot evidence before expansion. |

## Repeated Methodology

- "Human review is mandatory" appears across many layers.
- "Not automation / not orchestration / not runtime" appears across many boundary files.
- "Evidence quality matters" appears across evidence, confidence, decisions, failures, and fast review.
- "Avoid fake certainty" appears across confidence, contradictions, failures, and operator decisions.
- "Speed matters" appears across fast review, minimalism, compression, and operational decision rules.

This repetition is useful as guardrail language, but it now has maintenance cost. A shared short boundary reference may reduce duplication later.

## Duplicated Review Logic

- SERP pressure review repeats in `research`, `fast-review`, `essential-signals`, and `minimalism`.
- Landing review repeats in `landing-match`, `campaign-qa-assembly`, `failure-patterns`, `fast-review`, and `essential-signals`.
- Campaign readiness review repeats in `qa`, `campaign-qa-assembly`, `operator-decisions`, and `workflows`.
- Stop-review logic repeats in `fast-review`, `minimalism`, `compression`, and `operator-decisions`.

## Duplicated Risk Logic

- Semantic risk repeats across semantic, search-term, QA, failure, essential-signal, and minimalism layers.
- Mobile friction repeats across landing, ad-extension, campaign QA, failure, fast-review, and minimalism layers.
- CTA failure repeats across ad-copy, landing, campaign QA, fast-review, essential-signals, and minimalism layers.
- Operator overload repeats across compression, minimalism, failure-patterns, fast-review, and operator-decisions.

## Duplicated Trust Logic

Trust appears as:

- offer strength;
- landing proof;
- ad-copy support;
- extension relevance;
- trust collapse;
- high-value signal;
- fast-review priority.

This is operationally important, but the same logic should not require seven review passes.

## Duplicated Semantic Logic

Semantic cleanliness appears as:

- semantic layer core purpose;
- search-term contamination;
- campaign QA consistency;
- failure pattern;
- high-value signal;
- minimal review priority;
- fast-review item.

The cleanup opportunity is to define one semantic source of truth and let other layers reference it briefly.

## Boundary

This review identifies duplication only. It does not modify, merge, delete, archive, or approve changes.

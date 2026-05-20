# ORCA Layer Inventory v1

## Status

Manual consolidation inventory. Not new architecture, automation, orchestration, telemetry, dashboards, runtime systems, or governance expansion.

## Reality Note

ORCA is becoming large. Complexity has cost. Documentation has maintenance burden. Operator attention is limited. Simplicity is strategic, and practical usefulness matters most.

## Inventory

| Layer | Purpose | Operational value | Overlap risk | Abstraction risk | Maintenance cost | Operator usefulness | Simplification opportunity |
|---|---|---:|---:|---:|---:|---:|---|
| `ad-copy` | PPC ad copy and message discipline | High | Medium | Low | Medium | High | Keep as core output layer; avoid duplicating trust and offer rules. |
| `ad-extensions` | Extension relevance, mobile/contact/sitelink review | High | Medium | Low | Medium | High | Keep practical templates; merge repeated risk language later. |
| `agents` | Documentation of ORCA agent roles | Medium | Medium | Medium | Medium | Medium | Keep only if roles map to real operator entrypoints. |
| `campaign-qa-assembly` | Pre-launch campaign QA and consistency checks | High | High | Low | Medium | High | Keep as final QA spine; reduce duplicate semantic, CTA, mobile, landing checks elsewhere. |
| `confidence` | Confidence and uncertainty discipline | Medium | High | Medium | Medium | Medium | Consolidate with evidence, contradictions, and operator decisions later. |
| `contracts` | Manual contracts and task boundaries | High | Medium | Low | Low | High | Keep concise; use as boundary source instead of repeating contracts everywhere. |
| `contradictions` | Contradiction detection and review | Medium | High | Medium | Medium | Medium | Merge conceptually with evidence/confidence review. |
| `direct-commander` | Practical command/request framing for operator use | High | Medium | Low | Low | High | Keep as entrypoint; avoid adding meta-methodology. |
| `essential-signals` | High-value signal prioritization | Medium | High | Medium | Medium | High | Keep as reference; merge with minimalism or fast-review if duplication grows. |
| `evidence` | Evidence quality and source discipline | High | High | Low | Medium | High | Keep as core reality layer; centralize repeated SAFE UNKNOWN language. |
| `evolution` | Change and learning semantics | Low | High | High | Medium | Low | Treat as experimental until real pilot evidence proves value. |
| `failure-patterns` | PPC failure pattern awareness | Medium | High | Medium | Medium | Medium | Keep compact as reference; avoid becoming diagnosis methodology. |
| `fast-review` | Short high-signal PPC review mode | High | High | Low | Medium | High | Keep as practical operator path; consider merging with minimalism. |
| `heuristic-mapping` | Mapping observations to heuristics | Experimental | High | High | Medium | Medium | Keep only if it reduces operator effort in pilots. |
| `heuristics` | PPC heuristic reference | Experimental | High | High | Medium | Medium | Treat as optional reference, not required workflow. |
| `intelligence` | Market/competition interpretation docs | Low | High | High | High | Low | Avoid expanding; rename or compress if it implies fake intelligence. |
| `landing-match` | Query/ad/offer-to-landing alignment | High | High | Low | Medium | High | Keep as core PPC layer; reduce duplicate trust/mobile/CTA guidance elsewhere. |
| `live-observations` | Human-captured observations from live review | Experimental | Medium | Low | Medium | High if used | Keep as evidence bridge; archive unused observations later. |
| `live-pilots` | Human-run pilot review discipline | Experimental | Medium | Low | Medium | High if used | Keep for real-world validation; do not imply automation. |
| `methodology` | General method framing | Low | High | High | High | Low | Compress aggressively; move useful rules into operator layers. |
| `minimalism` | High-impact-only review and stop discipline | High | High | Medium | Medium | High | Keep as anti-bloat anchor; prevent it from becoming bloat. |
| `compression` | Documentation pruning and anti-bloat rules | High | Medium | Medium | Medium | High | Use for cleanup passes; avoid expanding into governance. |
| `observations` | Observation capture and review semantics | Medium | High | Medium | Medium | Medium | Merge with evidence/live-observations where possible. |
| `offer-evaluation` | Offer clarity, pricing, urgency, trust review | High | High | Low | Medium | High | Keep for commercial realism; reduce duplicated trust/pricing logic. |
| `operator-decisions` | Decision, uncertainty, tradeoff, escalation rules | Medium | High | Medium | Medium | High | Keep compact; merge with evidence/confidence/contradictions later. |
| `patterns` | Pattern library for PPC observations | Medium | High | High | Medium | Medium | Keep only patterns proven useful by pilots. |
| `pilot-cases` | Fictional/manual pilot case structure | Experimental | Medium | Low | Medium | Medium | Keep examples small and clearly non-validated. |
| `qa` | Quality assurance rules | High | High | Low | Medium | High | Keep as QA spine; reduce overlap with campaign-qa-assembly. |
| `research` | SERP and PPC research discipline | High | Medium | Low | Medium | High | Keep as early workflow input; avoid duplicate fast-review chains. |
| `review` | General review process and methodology | Medium | High | Medium | Medium | Medium | Compress into fast-review/minimalism/operator-decisions. |
| `search-terms-review` | Search-term and negative keyword review | High | High | Low | Medium | High | Keep as core spend-quality layer; deduplicate semantic contamination logic. |
| `semantic` | Semantic cleanliness and intent review | High | High | Medium | Medium | High | Keep as core layer; avoid multiplying semantic rules elsewhere. |
| `workflows` | Manual workflow framing | High | Medium | Low | Low | High | Keep as operator navigation layer; do not turn into process chain. |

## Top-Level Support Docs

Top-level docs such as `README.md`, `doc-map-v1.md`, `current-state-v1.md`, `operator-entrypoints-v1.md`, and `session-execution-guide-v1.md` are useful only if they help operators enter the system quickly. They should not become a second documentation system above the layer system.

## Consolidation Finding

The strongest ORCA spine is:

- `workflows`
- `contracts`
- `research`
- `semantic`
- `search-terms-review`
- `landing-match`
- `offer-evaluation`
- `ad-copy`
- `ad-extensions`
- `campaign-qa-assembly`
- `qa`
- `evidence`
- `fast-review`
- `minimalism`
- `compression`

The highest bloat risk is the growing family of meta-review layers around evidence, confidence, contradictions, observations, decisions, patterns, heuristics, methodology, and intelligence.

## Boundary

This inventory does not approve merges or deletions. It identifies review targets only.

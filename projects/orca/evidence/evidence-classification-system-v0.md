# Evidence Classification System v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — cross-cutting evidence vocabulary for intake, research, artifacts, and campaign modes.

Complements (does not replace) [evidence-strength-model-v1.md](evidence-strength-model-v1.md), [evidence-discipline-model-v1.md](evidence-discipline-model-v1.md), and related v1 evidence docs.

## Purpose

Give operators a **shared label set** for manifest items, research notes, and artifacts so ORCA never treats AI suggestions, stale screenshots, or raw drops as verified commercial truth.

## Boundary

Evidence classification is **human-reviewed signaling**. It is not certification, legal proof, or performance prediction.

## Dimension 1 — Strength

| Label | Meaning | Allowed downstream use |
|-------|---------|------------------------|
| `strong` | Repeated, contextualized, low unexplained contradiction | Supports approved strategy with HITL sign-off |
| `weak` | Isolated, thin context, or contradicted | Research lead only — not export SoT |
| `safe_unknown` | Insufficient data to grade | Explicit gap — must not fill with guesses |

Aligns with WEAK / MODERATE / STRONG in v1 strength model; v0 uses operator-facing short labels in manifests.

## Dimension 2 — Verification State

| Label | Meaning |
|-------|---------|
| `verified` | Operator confirmed against source (opened file, checked URL context, matched live SERP) |
| `unverified` | Present in inventory but not checked |
| `operator-confirmed` | Explicit sign-off on a specific claim or file |
| `ai-derived` | Produced or summarized by AI — **requires** re-verification before SoT |
| `historical` | True at past observation time — may not hold now |
| `stale` | Known outdated — keep for traceability, exclude from active decisions unless refreshed |

**Rule:** `ai-derived` never auto-promotes to `verified`.

## Dimension 3 — Provenance (recommended on artifacts)

| Label | Meaning |
|-------|---------|
| `primary_capture` | Operator screenshot, export, or direct observation |
| `secondary_summary` | Human or AI summary of primary |
| `third_party` | External doc — trust bounded |
| `safe_unknown` | Provenance unclear |

## Combined Usage Matrix

| Scenario | Typical tags |
|----------|----------------|
| Fresh SERP screenshot + operator notes | `strong` or `weak` + `verified` + `primary_capture` |
| Old competitor PDF, not re-checked | `weak` + `historical` + `unverified` |
| AI competitor summary | `weak` + `ai-derived` + `unverified` |
| Commander export used for transport | `verified` for **structure** only — not performance truth |
| Missing competitor pricing | `safe_unknown` at claim level |

## SAFE UNKNOWN Discipline

1. **Mandatory** when: niche volatility unknown, personalization suspected, incomplete SERP capture, or conflicting sources.
2. **Forbidden:** replacing UNKNOWN with plausible industry defaults for bids, CR, or budget.
3. **Manifest:** use item-level `safe_unknown: true` and manifest-level `safe_unknown: []` string list for gaps.
4. **Artifacts:** approved docs must list unresolved UNKNOWNs in `approvals/` or artifact front matter.

## HITL Promotion Path

```
unverified → operator review → operator-confirmed → (optional) verified
ai-derived → operator review → operator-confirmed OR reject
stale → refresh observation → new primary_capture OR remain stale + excluded
```

No automated promotion. No "confidence score" as launch authority.

## Relationship to Intake

`inventory-manifest.json` item field `evidence_grade` should use labels from **Verification State** and optionally note strength in `notes` until schema v1 merges fields.

## Relationship to Campaign Modes

Search and RSYA may require different minimum evidence bars — see [orca-campaign-mode-architecture-v0.md](../campaign-modes/orca-campaign-mode-architecture-v0.md).

## Anti-Patterns

- Labeling `verified` because "the file exists."
- Treating `ai-derived` summaries as competitor intelligence without capture.
- Using `strong` for a single SERP screenshot on a volatile query.

## Related Documents

- [evidence-strength-model-v1.md](evidence-strength-model-v1.md)
- [human-validation-rules-v1.md](human-validation-rules-v1.md)
- [orca-research-layer-v0.md](../research/orca-research-layer-v0.md)
- [orca-operational-principles-v0.md](../orca-operational-principles-v0.md)

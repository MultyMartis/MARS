# Pilot Success Criteria — MIG Pilot #1

Measurable outcomes derived from Runtime MVP verification, Task File Adapter (OR-09 intake, OR-10 `groundtruth_run` validation), and contract discipline. **No invented KPIs.**

---

## Runtime execution

| Criterion | Pass condition | Source |
|-----------|----------------|--------|
| Request type accepted | Inbox request keeps `request_type: groundtruth_run`; adapter does not emit `VALIDATION_ERROR` for type | OR-10 + adapter spec §8 |
| Adapter completes | Request in `incoming/mig/completed/` with `*.outcome.json` status `completed` | Task File Adapter spec |
| No critical runtime failure | Outcome not in `failed/`; manifest `status` not terminal `failed` | `runMigSession` lifecycle |
| Session bound | `session_id` assigned; folder under `projects/mig/sessions/` | OR-09 verification |
| Manifest v0.2 | `session_manifest.json` present with schema version 0.2 | OR-09 verification |

---

## Artifacts generated

| Criterion | Pass condition | Source |
|-----------|----------------|--------|
| SERP normalized | `serp_result.json` exists | Runtime P1 |
| Pack generated | `research_pack.draft.md` exists | Runtime P6 |
| Competitors artifact | `competitors.json` exists (content may be `empty` array) | Runtime P2 — empty is valid |
| Website snapshots | If `website_pass: true` and fetchable URLs exist: `website_snapshots.json` with ≥1 `success` **or** explicit fetch failure recorded in manifest/pack | Runtime P3 + MVP fixture pattern |
| Landing observations | If `landing_pass: true` and snapshots succeeded: `landing_observations.json` present **or** SAFE UNKNOWN in pack for skipped landings | Runtime P4 |

---

## Groundtruth quality (human judgment)

| Criterion | Pass condition | Source |
|-----------|----------------|--------|
| SERP from real capture | `manual_serp` matches operator screenshots; no template/fixture URLs | Manual SERP discipline |
| SAFE UNKNOWN honest | Gaps listed in pack / manifest — not silently filled | Research pack contract |
| No fabricated competitors | Competitor entries trace to SERP URLs or discovery rules | Competitor discovery contract |

---

## ORCA readiness

| Criterion | Pass condition | Source |
|-----------|----------------|--------|
| Approved pack | `research_pack.approved.md` + **Approved By** | ORCA handoff contract |
| Handoff fields | Scope, region, date, queries, evidence sources, snapshots, observations, SAFE UNKNOWN | ORCA handoff contract §Required fields |
| ORCA can consume | Operator can start R2 from approved pack without re-capture | Handoff acceptance rules |

---

## Explicit non-goals (not required for pilot pass)

- Keyword volumes / Wordstat (`keyword_pass` off)
- Deep research memo (`deep_research_pass` off)
- Multi-query SERP bundle (MVP single query)
- n8n production workflows
- Automated ORCA ingestion
- Campaign semantics or clustering

---

## Failure signals

| Signal | Meaning |
|--------|---------|
| `VALIDATION_ERROR` on drop | Fix request shape before re-run |
| `serp_mode: fallback` without `manual_serp` | Missing SERP input |
| Zero organic results in `manual_serp` | Capture incomplete — re-capture |
| All website fetches failed | May still pass if honestly documented; operator decides re-run |
| Missing **Approved By** | ORCA handoff blocked — pilot acquisition may still be complete |

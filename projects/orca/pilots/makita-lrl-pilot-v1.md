# Makita LRL Pilot — Execution Plan v1

## Status

**PREPARATION ONLY** — human-operated pilot plan (2026-05-30).

**Not** the pilot itself. **Not** Makita analysis. **Not** PPC export. **Not** launch approval.

## Purpose

Step-by-step execution plan for the first Landing Readiness Layer (LRL) pilot.

**Primary architectural validation:**

> ORCA can operate without Website Factory when `landing_source = existing_client_website`.

**Pilot target:** Makita project (project-id to be confirmed at intake).

**Canonical sequence (from LRL v1):**

```text
Semantic pack (if exists) → [existing client website] → Final Website Copy Pack → Landing Ready Contract → PPC readiness review
```

## Boundaries

| In scope | Out of scope |
|----------|--------------|
| One route end-to-end through LRL v1 | Full Makita route family |
| Human capture from live client site | Website Factory handoff |
| FWCP + LRC creation and approval | PPC JSON generation / export |
| PPC readiness review (gate check only) | Keywords, ads, campaigns, market research |
| Pilot evaluation against success criteria | Exporter, validation-cli, runtime work |

## Prerequisites (before Phase 1)

- Operator has read:
  - [landing-readiness-layer-v1.md](../intelligence/landing-readiness-layer-v1.md)
  - [landing-ready-contract-v1.md](../intelligence/landing-ready-contract-v1.md)
  - [final-website-copy-pack-v1.md](../intelligence/final-website-copy-pack-v1.md)
- This plan and [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md) are available.
- [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md) is open for live notes.
- Makita client site URL(s) are accessible to the operator (no analysis yet — access check only).

## Artifact Paths (canonical)

Per [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md) and LRL v1:

```text
projects/orca/projects/<project-id>/
  PROJECT.md
  artifacts/landing-readiness/
    copy-pack-<route_id>-v1/
      COPY-PACK.md
      PACK-STATUS.md
      SAFE-UNKNOWN.md          (optional)
      evidence/                (optional)
    lrc-<route_id>-v1.md
    evidence/<route_id>/       (recommended)
  logs/
    makita-lrl-pilot-session-<date>.md
```

**Pilot observation log (cross-pilot):** `projects/orca/pilots/makita-lrl-observation-log-v1.md` (append entries during execution).

---

## Phase 1 — Landing Intake

**Goal:** Establish Makita as an ORCA project and declare one pilot route with `landing_source = existing_client_website`. No copy capture yet.

### Inputs

| Input | Source | Required? |
|-------|--------|-----------|
| Makita project identity (`project_id`) | Operator / existing client records | Yes |
| One primary landing URL for pilot route | Client site (access confirmed) | Yes |
| Stable `route_id` slug | Operator naming (aligns with future registry if any) | Yes |
| Semantic content pack (if exists) | `content-packs/` or project normalized layer | Recommended |
| Landing route registry (if exists) | Project `landing-route-registry.json` | Optional |
| Raw pack / intake manifest | `incoming/orca/<project-id>-raw-pack/` | Optional |

### Steps

1. Confirm or create `projects/orca/projects/<project-id>/` per project structure contract.
2. Update or create `PROJECT.md` — note pilot charter: LRL v1, `existing_client_website`, single route scope.
3. Select **one** pilot route (one primary landing URL). Document `route_id`, `route_label`, `page_type`, `intent_group`.
4. Record provenance intent: `landing_source = existing_client_website` (do not use `website_factory`).
5. Confirm URL loads in browser (operator visit — date + identifier only; no copy transcription yet).
6. Log any intake blockers in observation log.

### Outputs

| Output | Location |
|--------|----------|
| Project folder scaffold | `projects/orca/projects/<project-id>/` |
| Intake record in `PROJECT.md` | Project root |
| Route identity block (route_id, URL, source type) | Session log or `PROJECT.md` |
| Phase 1 complete marker | Session log |

### Required Evidence

- Operator note: URL visited and loads (HTTPS, final destination if redirect).
- `project_id` and `route_id` recorded.
- Explicit statement: Factory not used for this pilot route.

### SAFE UNKNOWN Handling

| Unknown | Action |
|---------|--------|
| Exact `project_id` slug | Operator picks stable slug; document choice |
| Multiple candidate URLs | Pick one primary route for pilot; defer others |
| Semantic pack existence | Mark N/A if none; do not block intake |
| Registry existence | Proceed without registry; note in LRC later |
| Redirect chain complexity | Document in intake; resolve in Phase 3 URL section |

### Success Criteria

- [ ] Project folder exists with `PROJECT.md` stating LRL pilot scope.
- [ ] One `route_id` and one `landing_url` declared.
- [ ] `landing_source = existing_client_website` recorded in intake notes.
- [ ] URL load verified by named operator with date.
- [ ] No Website Factory handoff steps invoked.
- [ ] Phase 1 blockers (if any) logged in observation log.

---

## Phase 2 — Final Website Copy Pack Capture

**Goal:** Create and approve a Final Website Copy Pack (FWCP) from the **live** Makita landing page — not from semantic pack draft.

### Inputs

| Input | Source | Required? |
|-------|--------|-----------|
| `landing_url` from Phase 1 | Intake record | Yes |
| `route_id`, `project_id` | Phase 1 | Yes |
| Live page (browser) | Client site | Yes |
| Semantic content pack (if exists) | Upstream ORCA | Recommended (drift comparison only) |
| Capture method choice | Operator | Yes — default `manual_review` for v1 |

### Steps

1. Create folder: `artifacts/landing-readiness/copy-pack-<route_id>-v1/`.
2. Initialize `COPY-PACK.md` with minimum sections per [final-website-copy-pack-v1.md](../intelligence/final-website-copy-pack-v1.md):
   - Meta (route_id, project_id, landing_url, landing_source, capture_date)
   - Hero (H1, lead, primary offer framing)
   - Qualification, Trust, CTA, FAQ, Footer/legal, Drift notes
3. Transcribe **deployed** copy from live page — do not copy from semantic pack without live verification.
4. If semantic pack exists: add drift notes (productive vs destructive); do not treat pack as SoT.
5. Optionally store screenshots under `evidence/` (`screenshot_archive` method).
6. Create `PACK-STATUS.md` — start at `draft`; promote through gates:
   - URL reachable
   - Hero captured
   - CTA captured
   - Drift classified (or N/A)
   - Human sign-off
7. Create `SAFE-UNKNOWN.md` if any copy blocks cannot be verified.
8. Promote FWCP to `approved` (or `production-ready`) only when copy snapshot matches live page.

### Outputs

| Output | Location |
|--------|----------|
| `COPY-PACK.md` | `copy-pack-<route_id>-v1/` |
| `PACK-STATUS.md` with final status | Same folder |
| `SAFE-UNKNOWN.md` (if needed) | Same folder |
| Optional screenshot archive | `evidence/` |

### Required Evidence

- Named operator + `capture_date` in COPY-PACK meta.
- Hero H1 and lead transcribed from live page (not inferred).
- Primary CTA label and type captured.
- PACK-STATUS gates checked with dates.
- Drift notes present or explicitly N/A.

### SAFE UNKNOWN Handling

| Unknown | Action |
|---------|--------|
| Section not visible on page | Note in SAFE-UNKNOWN.md; do not invent copy |
| Mobile-only copy differences | Capture desktop first; flag mobile UNKNOWN for LRC |
| Dynamic / personalized hero | Document behavior; mark affected fields UNKNOWN |
| Semantic pack vs live drift | Classify in drift notes; do not auto-resolve |
| FAQ partial visibility | Capture visible items; UNKNOWN for collapsed content |

### Success Criteria

- [ ] FWCP folder exists with `COPY-PACK.md` and `PACK-STATUS.md`.
- [ ] All minimum COPY-PACK sections populated or explicitly marked UNKNOWN.
- [ ] Copy sourced from live page verification, not semantic pack alone.
- [ ] `landing_source = existing_client_website` in COPY-PACK meta.
- [ ] PACK-STATUS at `approved` or `production-ready`.
- [ ] No Factory handoff or MODE 1 build steps used.

---

## Phase 3 — Landing Ready Contract Completion

**Goal:** Complete one Landing Ready Contract (LRC) that binds URL, copy, CTA, PPC alignment, and provenance — citing approved FWCP.

### Inputs

| Input | Source | Required? |
|-------|--------|-----------|
| Approved FWCP | Phase 2 | Yes |
| Phase 1 route identity | Intake | Yes |
| Live page re-check | Browser | Yes (URL, copy, CTA sections) |
| Semantic strategy / intent tier | Strategy docs or pack | Recommended |
| Landing route registry | Project (if exists) | Optional |
| Ad headline intent (draft or planned) | PPC layer (reference only — no ad creation) | Optional for alignment section |

### Steps

1. Create `artifacts/landing-readiness/lrc-<route_id>-v1.md` (or equivalent section in `LANDING-ROUTES.md`).
2. Complete **Section 1 — Identity** (all required fields).
3. Complete **Section 2 — URL** — re-verify load; record `url_verified_at` / `url_verified_by`.
4. Complete **Section 3 — Copy** — cite FWCP path in `copy_source`; populate hero fields from FWCP + live check.
5. Complete **Section 4 — CTA / Forms** — operator visual check; use SAFE UNKNOWN only where policy allows.
6. Complete **Section 5 — PPC Alignment** — pass/fail/partial against intent tier and negative space; **no semantic-pack-only alignment**.
7. Complete **Section 6 — Readiness Status** — promote to `approved` only when sections 1–5 satisfied.
8. Complete **Section 7 — Provenance** — `landing_source = existing_client_website`; skip Factory fields.
9. Store supporting evidence under `artifacts/landing-readiness/evidence/<route_id>/` if used.

### Outputs

| Output | Location |
|--------|----------|
| LRC document (all 7 sections) | `lrc-<route_id>-v1.md` |
| Evidence refs (optional) | `evidence/<route_id>/` |
| Updated readiness status | LRC Section 6 |

### Required Evidence

- `copy_pack_ref` points to approved FWCP.
- URL and copy verification dates and operator identifiers.
- PPC alignment fields explicitly set (not left blank).
- `blocking_items` empty when status = `approved`.
- Provenance records `existing_client_website` with human `source_description`.

### SAFE UNKNOWN Handling

| Field / situation | Allowed? | Effect |
|-------------------|----------|--------|
| Required LRC field missing | No | Status stays `draft` or `needs_fix` |
| `phone_visible = SAFE UNKNOWN` | Yes | Cannot `approve` for call-first campaigns |
| `mobile_cta_visible = SAFE UNKNOWN` | Yes | Document in `blocking_items` if PPC-relevant |
| `ppc_json_ref` pending | Yes | Use pending path or note; not a blocker for LRC structure test |
| Registry absent | Yes | Omit `registry_ref`; document N/A |
| Section 5 `partial` alignment | Yes | Requires operator note; cannot combine with `approved` without documented variance |

### Success Criteria

- [ ] LRC exists with all required fields in sections 1–7 populated or policy-compliant UNKNOWN.
- [ ] `readiness_status = approved` with named human sign-off.
- [ ] `copy_source` references approved FWCP — not semantic pack.
- [ ] `landing_source = existing_client_website` in provenance.
- [ ] No Factory-specific fields required or falsely populated.
- [ ] LRC would be eligible for PPC JSON citation per contract rules (export itself is out of scope).

---

## Phase 4 — PPC Readiness Review

**Goal:** Validate that the LRL chain satisfies PPC **gate expectations** without creating campaigns, keywords, ads, or exports.

This phase is a **readiness review**, not PPC execution.

### Inputs

| Input | Source | Required? |
|-------|--------|-----------|
| LRC at `approved` | Phase 3 | Yes |
| Approved FWCP | Phase 2 | Yes |
| [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) fast-review tools | ORCA starter core | Recommended |
| Triumph PPC baseline docs (reference only) | Freeze layer | Optional — compare gate semantics, not Triumph URLs |

### Steps

1. Confirm SoT hierarchy: FWCP (via LRC) > semantic pack for landing copy.
2. Run lightweight mismatch review against one hypothetical ad intent (operator-defined query/ad angle — **no ad artifact creation**):
   - Use `fast-review/landing-mismatch-review-v1.md` if helpful.
   - Use `fast-review/cta-pattern-review-v1.md` for CTA check.
3. Verify LRC Section 5 alignment fields are defensible for future PPC work.
4. Check export gate semantics (documentation only):
   - Would PPC JSON be allowed to cite this route? (LRC `approved` → yes per contract)
   - Is `export READY` distinct from `Launch READY`? (document understanding)
5. List **documentation gaps** for future PPC chartered work (e.g. `lrc_ref` field naming in JSON — known SAFE UNKNOWN).
6. Record top 3 findings; STOP per OPERATIONAL-INDEX anti-fatigue cues.

### Outputs

| Output | Location |
|--------|----------|
| PPC readiness review notes | Session log or `logs/makita-lrl-pilot-session-<date>.md` |
| Gate checklist (pass/fail/UNKNOWN) | Same |
| Observation log entries for friction | [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md) |

### Required Evidence

- Explicit statement: review performed without export / Commander / ad creation.
- SoT hierarchy acknowledged in writing.
- Top 3 findings captured.
- Any blockers for **future** PPC export noted (not resolved in pilot).

### SAFE UNKNOWN Handling

| Unknown | Action |
|---------|--------|
| PPC JSON schema for `lrc_ref` | Mark SAFE UNKNOWN — defer to future PPC charter |
| Triumph legacy parity | Do not assume; note difference for new projects |
| Ad headlines not yet written | Review alignment against intent tier + FWCP hero only |
| Mobile SERP behavior | Optional fast-review; mark UNKNOWN if not checked |

### Success Criteria

- [ ] Review confirms LRC `approved` satisfies documented PPC citation gate.
- [ ] No semantic-pack-only landing truth used in review reasoning.
- [ ] Findings logged; no PPC artifacts created.
- [ ] Operator can articulate Factory-independent path for this route.
- [ ] Session stopped after top 3 findings (no audit spiral).

---

## Phase 5 — Pilot Evaluation

**Goal:** Determine whether LRL v1 succeeds or fails for `existing_client_website` using [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md).

### Inputs

| Input | Source | Required? |
|-------|--------|-----------|
| Phases 1–4 outputs | Pilot session | Yes |
| Observation log | [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md) | Yes |
| Success criteria doc | Same folder | Yes |
| Preflight risks | [makita-lrl-preflight-review-v1.md](makita-lrl-preflight-review-v1.md) | Recommended |

### Steps

1. Score pilot against success conditions and failure conditions in success criteria doc.
2. Answer architecture validation questions:
   - Did ORCA complete LRL without Website Factory?
   - Was FWCP → LRC → PPC gate chain operable by a human operator?
3. Consolidate lessons in success criteria **Lessons-captured** section (or linked session report).
4. Mark pilot outcome: **PASS** | **PARTIAL** | **FAIL** with rationale.
5. List deferred items (post-pilot architecture expansion per LRL v1 — only if evidence supports).

### Outputs

| Output | Location |
|--------|----------|
| Pilot evaluation summary | Session log + success criteria lessons section |
| Final observation log state | Observation log |
| Recommended next chartered work | Evaluation summary (human decision) |

### Required Evidence

- Explicit PASS / PARTIAL / FAIL with criteria references.
- At least one architecture validation item addressed with evidence.
- Lessons list (minimum 3 items: worked / friction / unknown).

### SAFE UNKNOWN Handling

| Unknown | Action |
|---------|--------|
| Incomplete phase due to blocker | FAIL or PARTIAL with phase reference |
| Multi-route Makita scope pressure | Document deferral; do not expand pilot mid-flight |
| Automation desire | Log as lesson; do not implement in pilot |

### Success Criteria

- [ ] Evaluation completed against [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md).
- [ ] Outcome recorded with human reviewer identifier and date.
- [ ] No architecture docs modified during evaluation.
- [ ] Clear recommendation for next step (second route, taxonomy doc, PPC charter, etc.) — human decision.

---

## Session Discipline

- **One route** for pilot — resist scope expansion.
- **Human sign-off** at every promotion gate (FWCP approved, LRC approved).
- **STOP NOW** when decision is clear (per OPERATIONAL-INDEX).
- **Do not** open Factory bridge docs unless debugging a mistaken source type.
- **Do not** create PPC JSON, keywords, ads, or XLSX in this pilot.

## Related Documents

- [landing-readiness-layer-v1.md](../intelligence/landing-readiness-layer-v1.md)
- [landing-ready-contract-v1.md](../intelligence/landing-ready-contract-v1.md)
- [final-website-copy-pack-v1.md](../intelligence/final-website-copy-pack-v1.md)
- [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md)
- [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md)
- [makita-lrl-preflight-review-v1.md](makita-lrl-preflight-review-v1.md)

## Boundary

Execution plan only. **No** pilot execution in this document. **No** Makita site analysis. **No** PPC work.

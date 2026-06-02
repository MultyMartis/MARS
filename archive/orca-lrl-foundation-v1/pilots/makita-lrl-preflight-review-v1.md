# Makita LRL Pilot — Preflight Review v1

## Status

**REVIEW ONLY** — pre-pilot risk and ambiguity scan (2026-05-30).

Scanned documents:

- [landing-readiness-layer-v1.md](../intelligence/landing-readiness-layer-v1.md)
- [landing-ready-contract-v1.md](../intelligence/landing-ready-contract-v1.md)
- [final-website-copy-pack-v1.md](../intelligence/final-website-copy-pack-v1.md)

**No architecture changes.** **No redesign.** **No defect fixes applied.**

## Purpose

Identify pilot risks, ambiguities, missing evidence requirements, and operator confusion **before** Makita execution — so tomorrow's session can proceed with eyes open.

**Not** Makita site analysis. **Not** a substitute for Phase 5 evaluation.

---

## Review Method

Static review of LRL v1 foundation docs against pilot constraints:

- `landing_source = existing_client_website`
- No Website Factory
- No PPC export / ad / keyword work
- Human-operated capture only
- One route scope

Findings classified: **Risk** · **Ambiguity** · **Missing evidence** · **Operator confusion**

Severity: **High** · **Medium** · **Low**

---

## Potential Pilot Risks

| ID | Severity | Finding | Pilot impact | Mitigation (procedure only) |
|----|----------|---------|--------------|----------------------------|
| R1 | High | **Makita ORCA project may not exist yet** — no `projects/orca/projects/makita*/` tree found at prep time | Phase 1 delayed on folder / `PROJECT.md` setup | Confirm `project_id` first; use project structure contract scaffold |
| R2 | High | **Triumph muscle memory** — battle pilot normalized semantic-pack → export flow | Operator may skip FWCP or cite semantic hero in LRC | Execution plan Phase 2/3 explicit STOP rules; success criteria F3/F5 |
| R3 | Medium | **No landing-route registry assumed** for Makita | LRC Section 2 `registry_ref` N/A; URL SoT entirely in LRC | Document N/A; do not invent registry |
| R4 | Medium | **PPC alignment without ads** — Section 5 expects pass/fail vs ad headline intent | Phase 3/4 paralysis or fake alignment | Review intent tier + FWCP hero only; mark ad headline refs pending |
| R5 | Medium | **Multi-page client site** — one URL must be chosen | Wrong page captured | Phase 1 lock single `route_id` + URL before FWCP |
| R6 | Medium | **Redirect / www / trailing slash variants** | `landing_url` instability | Phase 1 + 3 record final destination in `redirect_chain_notes` |
| R7 | Low | **AI assist default `draft`** — if agent drafts LRC/FWCP | Anonymous or unverified promotion risk | Human sign-off on every status promotion |
| R8 | Low | **Evidence folder optional** in docs | Weak audit trail | Recommend `evidence/<route_id>/` for URL + hero screenshots |

---

## Potential Ambiguities

| ID | Severity | Topic | Ambiguity | Operator guidance (no doc change) |
|----|----------|-------|-----------|-----------------------------------|
| A1 | Medium | **FWCP vs LRC copy fields** | Hero captured in COPY-PACK.md and again in LRC Section 3 | FWCP = detailed snapshot; LRC = verified summary + refs — re-check live once |
| A2 | Medium | **Status vocabulary overlap** | FWCP uses artifact-system ladder (`draft` → `production-ready`); LRC uses own table (`draft` → `approved`) | FWCP must reach `approved` or `production-ready` before LRC `approved` |
| A3 | Medium | **LRC file location** | Dedicated `lrc-<route_id>-v1.md` vs section in `LANDING-ROUTES.md` | Pick one at Phase 3 start; record path in `copy_pack_ref` / PROJECT.md |
| A4 | Medium | **`page_type` enum** | `master` \| `capability` \| … — Makita page may not map cleanly | Best-fit label + note in `route_label`; do not block on taxonomy |
| A5 | Medium | **`intent_group`** | Requires semantic strategy input that may not exist for Makita | Use strategy doc if present; else operator-defined cluster label + SAFE UNKNOWN note |
| A6 | Low | **COPY-PACK section depth** | "Minimum sections" vs operator-extended layout | Extend sections as needed; do not omit minimums |
| A7 | Low | **`copy_capture_method`** | Three methods listed; `existing_client_website` default unclear | Default `manual_review`; add `screenshot_archive` when evidence stored |
| A8 | Low | **Display URL vs landing URL** | Yandex display path optional | Only populate if known; never substitute for `landing_url` |

---

## Potential Missing Evidence Requirements

| ID | Severity | Gap | Where noticed | Preflight expectation |
|----|----------|-----|---------------|------------------------|
| E1 | Medium | **No worked example** of complete FWCP + LRC for `existing_client_website` | LRL v1 deferred examples post-pilot | Makita pilot **is** the example — capture paths meticulously |
| E2 | Medium | **Screenshot evidence not required** but claims need backing | LRC evidence expectations table | At minimum: URL visit date + optional hero screenshot |
| E3 | Medium | **Mobile verification** optional / UNKNOWN allowed | LRC CTA recommended fields | Explicitly mark `mobile_cta_visible` UNKNOWN unless checked |
| E4 | Low | **Evidence classification grades** referenced but not mandatory for v1 | LRC → evidence-classification-system link | Use plain operator notes unless project already grades evidence |
| E5 | Low | **Form E2E / analytics** explicitly out of scope | LRL SAFE UNKNOWN | Do not invent conversion claims |
| E6 | Low | **PACK-STATUS gate checklist** marked "recommended" not "required" | FWCP doc | Follow checklist anyway for pilot reproducibility |

---

## Potential Operator Confusion

| ID | Severity | Confusion point | Why it happens | Preflight cue |
|----|----------|-----------------|----------------|---------------|
| C1 | High | **Semantic pack treated as landing SoT** | Years of pack → Factory → PPC mental model | Post battle rule banner in session: "PPC must not rely on semantic pack alone" |
| C2 | High | **Website Factory docs in OPERATIONAL-INDEX** | Index lists Factory bridge prominently | For Makita: read only LRL v1 trio + this pilot folder |
| C3 | Medium | **Export READY vs Launch READY vs LRC approved** | Three gate vocabularies across battle freeze + LRC | Phase 4 checklist: LRC `approved` = PPC may cite URL; launch still separate |
| C4 | Medium | **When to mark SAFE UNKNOWN vs leave blank** | Required fields cannot be UNKNOWN-empty | Blank required = `draft`; UNKNOWN only where policy names field |
| C5 | Medium | **Section 5 `partial` + `approved` rule** | Subtle combination constraint | If partial, document variance note or stay below `approved` |
| C6 | Medium | **Drift notes without semantic pack** | FWCP requires drift section | Write "N/A — no upstream semantic pack" |
| C7 | Low | **`production-ready` vs `approved` on FWCP** | Two terminal-ish statuses | Either satisfies LRC gate per FWCP doc — pick one convention in session log |
| C8 | Low | **PPC JSON `lrc_ref` field naming deferred** | FWCP SAFE UNKNOWN | Do not block pilot; note in Phase 4 review |

---

## Cross-Cutting Themes

1. **Examples gap** — v1 is architecture-only; first pilot carries high documentation burden (E1).
2. **Status lattice** — FWCP lifecycle vs LRC readiness vs PPC export READY needs careful operator tracking (A2, C3).
3. **Factory gravity** — OPERATIONAL-INDEX and battle history pull toward Factory path (R2, C2).
4. **Alignment without ads** — Section 5 is structurally required but content-light until PPC charter (R4, A5).

---

## Critical Defects Found

**None identified** in static review sufficient to block pilot.

The following are **gaps**, not defects requiring foundation doc edits before pilot:

- No end-to-end example for `existing_client_website` (explicitly deferred in LRL v1)
- PPC JSON consumer field names for `lrc_ref` / `copy_pack_ref` undeclared (explicitly deferred)
- PACK-STATUS gates "recommended" rather than normative

If pilot execution reveals a **contract contradiction** (e.g. impossible to reach `approved` without Factory-only field), document as critical defect in observation log and success criteria **FAIL F7** — **do not** edit foundation docs during pilot.

---

## Preflight Checklist (operator — pilot morning)

- [ ] LRL v1 trio read (layer, LRC, FWCP)
- [ ] [makita-lrl-pilot-v1.md](makita-lrl-pilot-v1.md) open
- [ ] [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md) ready for entries
- [ ] Makita site URL accessible (load check only)
- [ ] `project_id` slug decided
- [ ] One `route_id` selected
- [ ] Factory bridge docs **not** in session reading list
- [ ] Commitment: no PPC export / ads / keywords in this pilot

---

## Related Documents

- [makita-lrl-pilot-v1.md](makita-lrl-pilot-v1.md)
- [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md)
- [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md)
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md)

## Boundary

Preflight review only. **No** modifications to LRL foundation documents. **No** Makita analysis performed.

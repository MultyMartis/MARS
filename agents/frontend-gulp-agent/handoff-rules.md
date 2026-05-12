# Handoff rules — alignment with Frontend Handoff Contract v0

This pack **consumes** [`../../projects/mars-website-factory/frontend-handoff-contract-v0.md`](../../projects/mars-website-factory/frontend-handoff-contract-v0.md). The contract is SoT for field names and semantics; this file summarizes **operational expectations** for the Gulp Frontend Agent.

## Input artifacts

- Stable **`frontend_handoff_id`**, **`source_blueprint_id`**, **`source_design_handoff_id`** (or documented exception).
- **`target_stack`** (e.g. `gulp-static`) — no aspirational framework drift.
- **`page_slug`** / **`page_type`** for routing the correct page entry and SCSS page bundle.

## Mappings (must be consistent)

- **`section_map`:** ordered **`block_id`** → logical section; drives include order in the page HTML.
- **`partials_mapping`:** how each block maps to **gulp-file-include** (or equivalent) paths under `src/`.
- **`SCSS_mapping`:** which SCSS partials attach to which blocks; shared tokens entry documented.
- **`JS_requirements`:** behaviors per region; dependencies (vanilla vs lib) stated in prose.
- **`data_attribute_hooks`:** required **`data-*`** attributes and which module owns behavior.

## Quality and policy fields

- **`responsive_rules`:** breakpoints, mobile-only components, exceptions vs design **`responsive_behavior`**.
- **`asset_requirements`:** paths, lazy rules, picture/srcset intent.
- **`form_behavior`:** validation level, success state, analytics hooks — **no PII** in logs without policy.
- **`accessibility_requirements`:** landmarks, labels, live regions, focus rules.
- **`performance_requirements`:** LCP hints, lazy embeds, CSS/JS budget **heuristics** unless tooling assigned.
- **`SEO_markup_requirements`:** H1, meta/canonical, JSON-LD only when honest to rendered content.
- **`integration_notes`:** real third-party IDs/URLs or **`n/a`** — no fake CMS.
- **`forbidden_patterns`:** must be mirrored in prompt `constraints` (e.g. no `dist/` edits, no undeclared globals).
- **`QA_requirements`:** minimal acceptance checks for this page/slice.
- **`HITL_required`:** governs when human sign-off is mandatory before merge/publish.

## Freeze and invalidation

- When blueprint or design **freezes** change, treat downstream handoff rows as **stale** until revised; follow factory **dependency invalidation** semantics — acknowledge invalidation in REPORT ([`reporting-standard-v0.md`](../../projects/mars-website-factory/reporting-standard-v0.md)).
- Do not silently implement against an **obsolete** handoff version; confirm active **`frontend_handoff_id`**.

## HITL escalation

- Escalate when: stack mismatch, missing assets/copy, conflicting `block_id` vs registry, new global CSS risk, or any **STRUCTURE CHANGE** (new shared tokens, new framework).
- Record escalation in REPORT **HITL flags** / risks per [`reporting.md`](reporting.md).

## SAFE UNKNOWN

- Record gaps in **`SAFE_UNKNOWN_notes`** from the handoff; add execution unknowns (exact `src` root, CI name) discovered during implementation.

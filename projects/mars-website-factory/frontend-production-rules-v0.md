# MARS Website Factory — Frontend Production Rules v0

**Status:** **documentation only** — compact operator rules for Gulp-oriented static frontend production. **Not** runtime enforcement, **not** an autonomous build agent, **not** a deployed service.

**Consolidates (read for detail):**

| Source | Role |
|--------|------|
| [`agents/frontend-gulp-agent/frontend-rules.md`](../../agents/frontend-gulp-agent/frontend-rules.md) | Pack-local implementation cheat sheet |
| [`agents/frontend-gulp-agent/gulp-architecture.md`](../../agents/frontend-gulp-agent/gulp-architecture.md) | Target tree / paths (verify in target repo) |
| [frontend-production-model.md](frontend-production-model.md) | Stack intent and honesty boundary |
| [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) | Per-page requirements and forbidden patterns |
| [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) | Cursor prompt law for Stage 11 |
| [font-awesome-governance-layer.md](font-awesome-governance-layer.md) | Lightweight Font Awesome semantics, style consistency, and icon drift discipline |
| [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) | **Authority** — RU no word-splitting CSS + selective `&nbsp;` typography |
| [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) | **Canonical** RU commercial landing QA widths + checks |

**Registry index:** [registries.md §6](registries.md#6-frontend-production-rules).

---

## 1. Source-first

- Implement and fix under the project’s agreed **`src/`** tree (or documented equivalent).
- **`dist/`** (or agreed output dir) is **generated only** — record non-default output in handoff **`integration_notes`**.
- Durable fixes live in **source**; rebuild to produce deployable output.

## 2. No `dist/` edits

**Forbidden:** hand-patching `dist/*.html`, `dist/*.css`, `dist/*.js`, search-and-replace across `dist/`, or committing `dist/` as a “quick fix.”

If preview/CDN needs a snapshot, that is a **delivery** step with an explicit packaging prompt — not production editing of generated files.

## 3. Gulp / gulp-file-include discipline

- Page **entries** under `src/pages/` (or project equivalent); **section bodies** in partials, not pasted into entries.
- Assemble HTML via **gulp-file-include** (or documented equivalent) per handoff **`section_map`** / **`partials_mapping`**.
- **`@@include` safety:** trusted partial paths only; no user-controlled include parameters; avoid deep include cycles.
- **One block per prompt** when implementing (see [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) §4).
- Exact folder names and task graph → **SAFE UNKNOWN** until the target repo is inspected ([gulp-architecture.md](../../agents/frontend-gulp-agent/gulp-architecture.md)).

## 4. Modular SCSS discipline

- Section/block **partials**; shared **tokens/mixins** in a dedicated entry — no monolithic mega-sheets unless project policy allows.
- Block-scoped selectors; no unscoped global resets that break third-party widgets without review.
- No **`!important`** waves to “fix” cascade without HITL sign-off.
- No inline `<style>` on sections — styles live in SCSS partials.
- Naming aligned with handoff **`SCSS_mapping`** and project convention.

## 5. JS module discipline

- Behavior in **modules** / agreed entry (`main.js` or equivalent) — **no inline JS** in HTML partials unless handoff + HITL allow.
- **No new `window.*`** without explicit review; prefer modules/IIFE per project policy.
- **No undeclared dependencies** — libraries must appear in handoff or project build config.
- Init is **idempotent** (re-run does not double-bind).

## 6. Data-attribute JS hooks

- Prefer **`data-component="…"`** (or project convention) for binding — not `#id` soup.
- Separate **styling classes** from **behavior hooks** where practical.
- Handoff **`data_attribute_hooks`** is canonical; new hooks need handoff update or **STRUCTURE CHANGE**.
- One behavior owner per hook; avoid competing scroll/interaction owners on one block.

## 7. Responsive breakpoint discipline

- **Mobile-first** unless handoff **`responsive_rules`** say otherwise; honor design tokens and frozen breakpoints.
- Prefer **min-width** media queries; document non-default **max-width** usage in **SAFE_UNKNOWN_notes**.
- Spot-check key viewports before REPORT; automated Lighthouse/CI → **SAFE UNKNOWN** unless project defines jobs.

## 8. Section / component structure discipline

- Canonical **`block_id`** from [block-registry-v0.md](block-registry-v0.md) — no ad-hoc section semantics without mapping.
- Typical layout: `src/partials/sections/`, `src/partials/components/`, `src/partials/layout/` (verify in target repo).
- **One block → one HTML partial + matching SCSS partial** (+ optional scoped JS).
- Reuse shared partials across pages; do not duplicate a section to “tweak” — extend partial, modifiers, or include args.
- Semantic HTML: logical heading order, landmarks, buttons vs links used correctly.

## 9. Icon governance

- Use project-approved icon sources only; for governed Font Awesome work, default to **Font Awesome Pro 5.15.4** per [font-awesome-governance-layer.md](font-awesome-governance-layer.md).
- Treat icon choice as semantic implementation, not visual decoration: role, local text meaning, FA availability, section rhythm, exception.
- Keep family/style consistency inside a section; mixed `fal` / `far` / `fas` / `fab` requires a role-based reason.
- Brand icons and partner marks follow brand/source rules; do not replace official marks with generic UI glyphs.
- Record icon drift or **SAFE UNKNOWN** during visual reconciliation / REPORT when icon meaning, weight, or source is unclear.

## 10. QA before REPORT

Before closing a frontend session:

- Run the project’s **build** command when available; do **not** claim green build without evidence.
- Use pack [`qa-checklist.md`](../../agents/frontend-gulp-agent/qa-checklist.md) + handoff **`QA_requirements`**.
- REPORT per [reporting-standard-v0.md](reporting-standard-v0.md) §4.2 — list **source** paths, not `dist/` fixes.
- Record **SAFE UNKNOWN** for missing CI, scripts, or hosting.

## 11. No autonomous runtime claims

- These rules govern **human-operated** and **Cursor-layer** work only ([AGENTS.md](../../AGENTS.md)).
- **Gulp Frontend Agent** is an **`operational_doc_pack`** — not proof of in-repo Gulp runtime, not autonomous deployment, not a MARS orchestration product.
- Future automated mapping to Tool Layer → **planned only**; must still respect source-first and handoff contracts.

## 12. Russian no word-splitting typography (mandatory for RU landings)

**Authority:** [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) — full forbidden CSS, protected selectors, selective `&nbsp;` ties, overflow policy. **Do not** duplicate rules here.

**RU QA preset:** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) — mandatory widths and checks for **Russian commercial landings**; generic responsive QA lists are supplementary only.

**Operator summary:** Russian words must not break inside the word; fix overflow with layout (`min-width: 0`, containers, grid) before word-breaking CSS; no `&nbsp;` chains between every heading word.

**REPORT line:**

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

**Reference case (signal only, not copy source):** [`workspaces/triumph-manipulator-landing-v5/reports/v5-typography-no-word-splitting-pass-2-report-v1.md`](../../workspaces/triumph-manipulator-landing-v5/reports/v5-typography-no-word-splitting-pass-2-report-v1.md).

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-15 | v0 — consolidation doc (Phase C); satisfies [registries.md §6](registries.md#6-frontend-production-rules). |
| 2026-05-16 | Added Font Awesome governance pointer and compact icon discipline rules. |
| 2026-05-24 | §12 — Russian no word-splitting typography (mandatory); links Triumph V5 reference case. |
| 2026-05-24 | §12 stabilization — authority lock + [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md); rule prose not duplicated. |

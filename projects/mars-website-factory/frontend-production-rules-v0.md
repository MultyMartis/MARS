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
| [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) | **Anti-drift** — breakpoints, container, FAQ, CSS multicol browser QA, build/dist, Windows EBUSY |
| [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | **Inter-section spacing** — same/diff background, mobile, project mapping |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | **Standards gate** — Draft + Approval before Shell |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | **Start gate** — Production Standards + shell + UI demo before Home |
| [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) | **Foundation Demo Page** — mandatory composition before Home |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | **Calibration gate** — token/visual review before Foundation QA |
| [frontend-rules/WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | **Foundation** — mandatory section/container grid discipline (SITE-001 promoted) |
| [frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | **Foundation** — mandatory inner-zone layout discipline (SITE-001 Layout Review promoted) |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | **Precision** — spacing scales, typography px + line-height, no arbitrary values, normalization |
| [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) | **Layout patterns** — mandatory pattern selection before multi-section production |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | **Design mapping** — multi-source extraction, layout chain, Mapping QA before Approval |
| [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) | **Enforcement** — Operator Law, Compiled CSS, Inline Style, ROOT COMPLIANCE gates |
| [frontend-inline-style-allowlist-v1.md](frontend-inline-style-allowlist-v1.md) | **Inline styles** — allowlist for EG-03 |
| [css-multicol-masonry-browser-compatibility-lesson-v1.md](css-multicol-masonry-browser-compatibility-lesson-v1.md) | **CSS multicol** — Chrome/Firefox column group `display` compatibility (WPilot footer incident) |
| [layout-spec-law-v1.md](layout-spec-law-v1.md) | **Layout Spec Gate** — composition before HTML/CSS; operator APPROVED |

**Registry index:** [registries.md §6](registries.md#6-frontend-production-rules).

**Authority order (mandatory):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — Project Production Standards → Approved Operator Laws (OL-01–OL-07) → Factory Governance → Layout Pattern Library → Industry Best Practice → Agent Preference. **Agent Preference never overrides ranks 1–5.**

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
- No inline `<style>` on sections — styles live in `src/scss/style.scss`.
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

- **Responsive base strategy** comes from **Project Production Standards (rank 1)** — e.g. desktop-first or mobile-first. **Do not** default to industry mobile-first when project SSOT states otherwise ([frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md)). Honor design tokens and frozen breakpoints from handoff / standards.
- Prefer **min-width** media queries; document non-default **max-width** usage in **SAFE_UNKNOWN_notes**.
- **Do not invent local breakpoints** — use project-defined tokens/handoff only ([frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §1).
- **Triumph V5 / current V5 lane:** desktop `1025px+`; tablet/mobile `max-width: 1024px`. **Forbidden drift:** ad-hoc `980`/`981` unless project explicitly defines them.
- Spot-check key viewports before REPORT; automated Lighthouse/CI → **SAFE UNKNOWN** unless project defines jobs.

## 8. Section / component structure discipline

- Canonical **`block_id`** from [block-registry-v0.md](block-registry-v0.md) — no ad-hoc section semantics without mapping.
- Typical layout: `src/partials/sections/`, `src/partials/components/`, `src/partials/layout/` (verify in target repo).
- **One project SCSS file (mandatory default):** all project-owned styles in `src/scss/style.scss` — no new section/component/layout/page partials without operator exception ([one-project-scss-file-law-v1.md](one-project-scss-file-law-v1.md)).
- **Unified radius:** `--radius-main` for standard rounding; `--radius-full` for circles/pills — no `--radius-small|medium|large` scale by default ([universal-style-scale-law-v1.md](universal-style-scale-law-v1.md)).
- **No button letter-spacing token:** do not define or use `--button-letter-spacing` ([no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md)).
- **One block → one HTML partial + styles in `style.scss`** (+ optional scoped JS).
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
- **Build failure → stale dist:** if build fails, assume `dist/` is stale; do **not** claim browser-visible changes until build succeeds and compiled output is verified ([frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §7).
- **Windows EBUSY:** prefer deleting dist **contents** over removing the dist root; report file locks clearly ([frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §8).
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

## 13. Production invariants (FAQ, container, native details)

**Authority:** [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) — full rules; **do not** duplicate here.

**Operator summary:**

- Split layouts (FAQ+CTA, 50/50) stay inside **section-shell** / content container.
- Decorative dividers must not break symmetric column geometry — use pseudo-elements or absolute positioning.
- Native `<details>`: **`open` attribute is SoT**; no hybrid JS `max-height` accordion on the same panel.
- FAQ: avoid two-column CSS Grid when answers expand; QA open/close/single-open/neighbor-stretch/keyboard/mobile stack.
- Reusable V5 prompt block → [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) §3b.

## 14. Section spacing and shell-first start (mandatory gates)

**Authority (do not duplicate):**

| Topic | Document |
|-------|----------|
| Production Standards Draft + Approval | [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| Inter-section spacing tokens, same/diff background | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |
| Compact spacing/radius scale; no selector tokens | [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) |
| CSS variable lookup + direct exact geometry | [css-variable-first-law-v1.md](css-variable-first-law-v1.md) |
| Foundation before Home; Foundation Demo Page composition | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) |
| Design Calibration before Foundation QA | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) |
| Foundation QA (consolidated gate) | [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) |
| Shell-first start sequence | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| Cadence methodology (tiers XS–XL) | [vertical-rhythm-governance.md](vertical-rhythm-governance.md), [cadence-tier-model.md](cadence-tier-model.md) |

**Operator summary:**

- Map section spacing in **Project Production Standards** before page production; complete **Draft → Approval** per [production-standards-governance-v1.md](production-standards-governance-v1.md) before Shell.
- Do **not** start Home page if Visual Foundation + Design Calibration + Foundation QA REPORT is missing.
- If operator requests Home first → execute shell-first protocol; cite [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md).
- **Layout Spec before shell/block HTML** — Header, Footer, Hero, any block: operator **APPROVED** Layout Spec required — [layout-spec-law-v1.md](layout-spec-law-v1.md).

## 15. WF Grid Discipline (mandatory — all Factory frontend)

**Authority:** [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) — full rules; **do not** duplicate here.

**Operator summary:**

- `<section>` / `<nav>` / `<header>` / `<footer>` = section shell; inner `div` = container width authority (WF-GRID-001).
- One page = one grid contract (`--container-main`, `--page-padding-inline`) — reuse primary `.container` class (WF-GRID-002, WF-GRID-006).
- Local `max-width` / `padding-inline` / `margin-inline` outside container → `/* WF-GRID-EXCEPTION */` comment (WF-GRID-003).
- Full-bleed backgrounds on section; content still inside container (WF-GRID-004).
- Section/layout region owns external vertical rhythm — not first/last internal child ([frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) §2.6).
- Frontend QA: header / hero / sections / footer alignment before visual PASS (WF-GRID-005).

**REPORT line:**

```text
WF GRID DISCIPLINE — PASS | FAIL (list sections) | SAFE UNKNOWN (widths not tested)
```

**Promotion:** SITE-001 WF-V3 — [WF-GRID-DISCIPLINE-PROMOTION-v1.md](../../workspaces/website-factory-reference-v1/reports/WF-GRID-DISCIPLINE-PROMOTION-v1.md).

## 16. WF Layout Discipline (mandatory — all Factory frontend)

**Authority:** [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) — full rules; **do not** duplicate here. Complements §15 (Container Layer).

**Operator summary:**

- Container Layer (WF-GRID) and Layout Layer (WF-LAYOUT) are separate authorities (WF-LAYOUT-001).
- Hero splits: fr/minmax authority — no default `%` tracks (WF-LAYOUT-002, WF-LAYOUT-007).
- Card grids: documented `N` at desktop (WF-LAYOUT-003); trust strip L5 grid (WF-LAYOUT-004); finance L4/L3 (WF-LAYOUT-005).
- Responsive collapse documented per zone before production freeze (WF-LAYOUT-006).
- New layout models require authority review before freeze (WF-LAYOUT-008).

**REPORT line:**

```text
WF LAYOUT DISCIPLINE — PASS | FAIL (list zones) | SAFE UNKNOWN (collapse not tested)
```

**Promotion:** SITE-001 WF-V3 Layout Review — [WF-LAYOUT-DISCIPLINE-PROMOTION-v1.md](../../workspaces/website-factory-reference-v1/reports/WF-LAYOUT-DISCIPLINE-PROMOTION-v1.md).

## 17. Frontend Precision Governance (mandatory — all Factory frontend)

**Authority:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) — full rules; **do not** duplicate here.

**Operator summary:**

- **Spacing:** gap scale `5/10/20/30/40/50/70`; margin/padding `5/10/15/20/25/30/40/50/70/90` — map design px to nearest approved value; no invented `64px`, `72px`, `80px` unless project SSOT token.
- **Typography:** font-size in **px**; default **`line-height = font-size + 4px`** — mandatory pre-flight + calibration ([typography-rhythm-governance.md](typography-rhythm-governance.md)).
- **No word breaking:** `letter-spacing`, `word-break`, `overflow-wrap: break-word`, `hyphens: auto` forbidden without operator approval — see §12.
- **RU HTML typography:** visible RU copy typographed in HTML — see §12 authority.
- **Layout:** pick documented patterns — [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md); no default `%` grid splits (WF-LAYOUT-007).

**REPORT lines:**

```text
TYPOGRAPHY PRECISION (line-height = font-size + 4px) — PASS | partial (list) | FAIL | N/A (project exceptions documented)
LAYOUT PATTERN LIBRARY — PASS | partial (list LP-*) | NOT READY | N/A (foundation only)
```

## 18. Enforcement gates (mandatory — compiled output)

**Authority:** [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) — full rules; **do not** duplicate here.

**Operator summary:**

- **Operator Law Compliance:** gap/margin/padding vs OL-01–OL-07 in **source and `dist/*.css`**.
- **Compiled CSS Compliance:** mandatory gate on **`dist/*.css`** — not substitutable by SCSS skim.
- **Inline Style Compliance:** `dist/**/*.html` vs [frontend-inline-style-allowlist-v1.md](frontend-inline-style-allowlist-v1.md).
- **Authority Conflict:** rank-1 SSOT vs OL requires Exception Registry — else **FAIL**.
- **ROOT COMPLIANCE:** technical review rollup — **PASS impossible** without it.

**REPORT lines:**

```text
OPERATOR LAW COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
COMPILED CSS COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
INLINE STYLE COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
AUTHORITY CONFLICT STATUS — PASS | FAIL | WAIVED | UNKNOWN
ROOT COMPLIANCE — PASS | FAIL | UNKNOWN
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-15 | v0 — consolidation doc (Phase C); satisfies [registries.md §6](registries.md#6-frontend-production-rules). |
| 2026-05-16 | Added Font Awesome governance pointer and compact icon discipline rules. |
| 2026-05-24 | §12 — Russian no word-splitting typography (mandatory); links Triumph V5 reference case. |
| 2026-05-24 | §12 stabilization — authority lock + [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md); rule prose not duplicated. |
| 2026-05-24 | §7/§10/§13 — Triumph V5 incident lessons; [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md). |
| 2026-06-13 | §14 — section spacing + shell-first start protocol (FP-0002 audit). |
| 2026-06-13 | §15 — WF Grid Discipline foundation authority (SITE-001 WF-V3 promotion). |
| 2026-06-13 | §16 — WF Layout Discipline foundation authority (SITE-001 WF-V3 Layout Review promotion). |
| 2026-06-13 | §14 — Visual Foundation Contract + Design Calibration stage (Evolution Pack v1). |
| 2026-06-13 | §14 — [production-standards-governance-v1.md](production-standards-governance-v1.md) Draft + Approval gate (Production Standards Governance Pack). |
| 2026-06-13 | §17 — Frontend Precision Governance Pack ([frontend-precision-governance-v1.md](frontend-precision-governance-v1.md), [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md)). |
| 2026-06-13 | Authority order pointer + §7 responsive base from Project Production Standards ([frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md)). |
| 2026-06-14 | §18 — Enforcement Pack v1 gates (compiled CSS, inline styles, ROOT COMPLIANCE). |
| 2026-06-14 | §14 — Layout Spec Law pointer ([layout-spec-law-v1.md](layout-spec-law-v1.md)); composition gate before HTML/CSS. |

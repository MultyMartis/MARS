# QA checklist — Gulp Frontend Agent (target project)

Use after **source** edits in the **target** gulp-starter (or equivalent) project. Record honest pass/fail/partial in REPORT.

## Build and output

- [ ] **Build check:** project’s documented build command run; exit success or failure captured (**SAFE UNKNOWN** if not run).
- [ ] **No `dist/` manual edits:** confirm fixes were applied in `src/` only.

## Layout and responsive

- [ ] **Responsive check:** spot widths from handoff **`responsive_rules`** (e.g. 375 / 768 / 1280) — **supplementary** unless project is non-RU.
- [ ] **RU typography / no word-splitting (RU commercial — mandatory):** run [ru-landing-qa-preset-v1.md](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md); authority [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md). REPORT: `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN`.
- [ ] **Overflow check:** horizontal scroll, sticky/fixed elements not clipping tap targets.

## Markup and accessibility

- [ ] **Semantic HTML:** heading order, landmarks, interactive elements use correct tags.
- [ ] **Accessibility basics:** focus visible, accordion/button ARIA as required, form error regions if specified.
- [ ] **Form behavior:** required fields, success state, no PII leakage in client logs.

## Behavior and style

- [ ] **JS hooks:** `data-*` attributes present per **`data_attribute_hooks`**; one clear owner module.
- [ ] **SCSS isolation:** new rules scoped to block; no surprise global resets/`!important` waves.
- [ ] **Section consistency:** order matches **`section_map`**; includes resolve.

## Assets and SEO

- [ ] **Asset paths:** images/fonts resolve; lazy rules respected where specified.
- [ ] **SEO basics:** H1 policy, title/description slots, honest schema if present.

## Risk

- [ ] **Performance risks:** oversized images, blocking scripts, third-party embed weight — note heuristically.
- [ ] **SAFE UNKNOWN:** unchecked items listed with reason (timebox, no device access, CI not defined).

---

**Not claimed:** full automated accessibility audit, Lighthouse CI, visual diff against Figma — unless tooling and scope are explicit in the prompt.

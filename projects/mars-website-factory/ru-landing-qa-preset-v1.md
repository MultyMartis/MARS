# MARS Website Factory — RU Landing QA Preset v1

**Status:** **documented** — **canonical** viewport and typography QA preset for **Russian commercial landings**.  
**Not:** runtime QA automation, Lighthouse CI, or a substitute for project handoff `responsive_rules`.

**Authority (typography / overflow CSS):** [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md)

**Rule:** RU landing QA preset is **mandatory** for Russian commercial landings. Generic responsive QA lists (e.g. 375 / 768 / 1280 only) are **supplementary** — they do not replace this preset.

---

## RU-LANDING-QA-PRESET-V1

### Required widths (px)

`320` · `375` · `390` · `420` · `760` · `1180` · `1320` · `1440`

Use DevTools device toolbar at each width unless project handoff documents a superseding matrix (document deviation in REPORT).

### Checks (all listed widths unless scoped in REPORT)

| Check | Pass criterion |
|-------|----------------|
| No mid-word splitting | Russian words stay intact; no breaks inside words |
| No aggressive overflow wrapping | No `anywhere` / `break-all` / global body `break-word`; UI headings use normal word boundaries |
| No horizontal overflow | Page does not scroll horizontally |
| Headings readable | Multi-line headings wrap at spaces / intentional ties only |
| CTA / buttons readable | Labels intact; min tap targets per project a11y |
| FAQ summaries stable | `summary` / accordion titles do not fragment words |
| FAQ interaction | Open · close · single-open · **no neighbor stretch** · no viewport jump · keyboard · mobile stack ([frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §5) |
| Forms stable | Labels, inputs, validation regions readable; no layout jump breaking focus |
| Mobile header stable | Sticky header does not obscure primary H1 on load; nav usable |

Overflow fixes on RU landings **must** follow [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) — prefer layout/grid, `min-width: 0`, and container adjustments before any word-breaking CSS.

### REPORT line (mandatory for RU commercial landings)

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

---

## Supplementary QA (non-authoritative for RU widths)

- [operational-qa-entry-v1.md](operational-qa-entry-v1.md) — interaction, modal, sticky, z-index passes  
- [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md) — generic 375 / 768 / desktop interaction checklist  
- [visual-regression-workflow-v1.md](visual-regression-workflow-v1.md) — screenshot discipline (375 / 768 / desktop minimum for baselines)

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — canonical RU commercial landing QA preset (stabilization pass) |
| 2026-05-24 | FAQ interaction row — Triumph V5 neighbor-stretch / accordion QA |

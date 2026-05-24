# REPORT — No Word-Splitting Typography Rule Integration

> **HISTORICAL / INTEGRATION SUMMARY ONLY — NOT AUTHORITY.**  
> **Authority:** [russian-no-word-splitting-typography-v1.md](../russian-no-word-splitting-typography-v1.md) · **RU QA preset:** [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md). Do not copy rule tables from this report into live projects.

**Date:** 2026-05-24  
**Lane:** B — Website Factory / Frontend Production Rules  
**Scope:** Documentation and governance only — **no** V5, workspace, build, or production code changes.

---

## Files updated

| File | Change |
|------|--------|
| `projects/mars-website-factory/russian-no-word-splitting-typography-v1.md` | **Created** — canonical mandatory rule, RU typography, QA checklist, reference pointer |
| `projects/mars-website-factory/reports/no-word-splitting-typography-rule-integration-v1.md` | **Created** — this integration report |
| `projects/mars-website-factory/frontend-production-rules-v0.md` | §12 + consolidates table + changelog |
| `projects/mars-website-factory/production-hardening-rules-v1.md` | Overflow edge case aligned — no `anywhere` on UI |
| `projects/mars-website-factory/foundation-systems/responsive-system-v2.md` | Anti-overflow table aligned |
| `projects/mars-website-factory/typography-rhythm-governance.md` | Cross-link to word-splitting layer |
| `projects/mars-website-factory/operational-qa-entry-v1.md` | Compact pass viewports + RU spot check |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Index entry under Cadence / rhythm |
| `agents/frontend-gulp-agent/frontend-rules.md` | Layout/UX — RU no word-splitting rule |
| `agents/frontend-gulp-agent/qa-checklist.md` | Production QA widths + checks |
| `agents/mars-forge/rhythm-governance-checklist.md` | §10 Word-splitting / RU typography; heading check; layer link |
| `agents/mars-forge/responsive-intent-checklist.md` | RU no word-splitting at responsive QA |
| `agents/mars-forge/qa-checklist.md` | Rhythm layer description updated |
| `agents/mars-forge/AGENT.md` | Rhythm governance bullet updated |

**Not touched:** `workspaces/`, Triumph V5 production code, build artifacts, git commit/push.

---

## Rule added

### Russian No Word-Splitting Rule (mandatory for RU landings)

Russian words **must not** break inside the word. Line wraps at **spaces** and intentional typographic ties only.

**Root causes eliminated in governance:**

1. Global `overflow-wrap: break-word` on `body`
2. Aggressive `word-break` / `anywhere` on UI
3. `&nbsp;` chains between **every** word in headings

**Base CSS default:**

```css
html,
body {
  word-break: normal;
  hyphens: manual;
}
```

**Protected UI selectors:**

```css
h1, h2, h3, h4,
.section-title,
button,
.button,
nav a,
summary,
.card-title,
.form label,
.cta-title {
  overflow-wrap: normal;
  word-break: normal;
  hyphens: manual;
}
```

---

## Forbidden CSS

| Property / pattern | Scope |
|--------------------|--------|
| `overflow-wrap: anywhere` | UI, headings, body default |
| `word-break: break-all` | All production UI |
| `word-break: break-word` | Headings and UI |
| `word-wrap: break-word` | Headings and UI |
| `hyphens: auto` | Russian UI copy |
| Global `overflow-wrap: break-word` on `body` | Site-wide default |
| `&nbsp;` between every heading word | HTML headings / short UI strings |

**Supersedes (documentation):** prior guidance recommending `overflow-wrap: anywhere` on narrow columns in `responsive-system-v2.md` and `production-hardening-rules-v1.md`.

---

## Allowed exceptions

`overflow-wrap: break-word` **only** on long ordinary text:

- paragraphs (`p`, `.section-lead`, card body)
- FAQ answer bodies
- legal / disclaimer / consent paragraphs
- long descriptions and notes

**Never** on: H1–H4, buttons, menu, cards, CTA titles, form labels, proof strips, spec labels, or other short UI blocks.

Prefer layout fixes (`min-width: 0`, container width) before break-word on UI.

---

## RU typography rule

**Do (selective ties):**

- Short prepositions/conjunctions: `в&nbsp;Краснодаре`, `и&nbsp;краю`
- Number + unit: `5&nbsp;т`, `3&nbsp;т`, `14&nbsp;м`, `2&nbsp;часа`
- Point ties for orphan prevention — **not** between every word

**Do not typograph:**

- `meta`, `alt`, JSON-LD
- `href`, `src`
- `data-*` and technical attributes

**Heuristic:** more than two `&nbsp;` in fewer than eight visible words → likely drift; review.

---

## QA checklist

Spot-check at **320 / 375 / 390 / 420 / 760 / 1180 / 1320 / 1440** px:

| Check | Pass |
|-------|------|
| Words not split inside | No mid-word breaks in Russian copy |
| Headings | Wrap only at spaces / intentional ties |
| CTA / buttons / nav | Labels intact |
| Cards / forms / FAQ titles | Short labels intact |
| Horizontal overflow | None at listed widths |
| Forbidden CSS | No `anywhere` / `break-all` / global body `break-word` on UI |

**REPORT line:**

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

Integrated into: Gulp `qa-checklist.md`, Forge `rhythm-governance-checklist.md` §10, Forge `responsive-intent-checklist.md`, `operational-qa-entry-v1.md` compact pass.

---

## Reference case

**Signal only — not a copy source:**

[`workspaces/triumph-manipulator-landing-v5/reports/v5-typography-no-word-splitting-pass-2-report-v1.md`](../../workspaces/triumph-manipulator-landing-v5/reports/v5-typography-no-word-splitting-pass-2-report-v1.md)

Triumph V5 Pass 2 confirmed:

- Removed global `overflow-wrap: break-word` from `body`
- Added centralized typography protection partial
- Restored normal spaces in over-`&nbsp;` headings
- Selective RU ties retained

Governance captures the **pattern**, not the V5 file tree.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Automated CSS lint for word-break rules | **Not** implemented — human DevTools spot-check |
| Non-RU primary locales | Rule mandatory for **RU** Factory landings; other locales need explicit pack rule |
| CMS / dynamic copy typography | **SAFE UNKNOWN** until content pipeline defined |
| Third-party embedded widgets | May not inherit project CSS — note in REPORT |
| Retroactive application to frozen legacy workspaces | Requires explicit unfreeze / migration charter — **not** done in this task |

---

## Git status

No commit. No push. Documentation-only diff under `projects/mars-website-factory/` and `agents/`.

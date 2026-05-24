# MARS Website Factory — Russian No Word-Splitting Typography v1

**Status:** **documented** — mandatory production **methodology** for Russian (and mixed RU) landing frontends.  
**Not:** runtime typography engine, automated lint enforcement, or universal typographic truth for all locales.

**Purpose:** Prevent mid-word breaks in Russian UI copy caused by aggressive CSS word-breaking and over-chained `&nbsp;` in headings. Preserve readable line wraps at normal word boundaries for headings, CTAs, navigation, cards, and forms.

**Reference case (production signal only):** [`workspaces/triumph-manipulator-landing-v5/reports/v5-typography-no-word-splitting-pass-2-report-v1.md`](../../workspaces/triumph-manipulator-landing-v5/reports/v5-typography-no-word-splitting-pass-2-report-v1.md) — Triumph V5 confirmed fix; **do not** treat the workspace as a copy source.

**RU QA preset (canonical widths):** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) — mandatory for Russian commercial landings; generic responsive QA lists are supplementary only.  
**Forge checklist overlay:** [`../../agents/mars-forge/rhythm-governance-checklist.md`](../../agents/mars-forge/rhythm-governance-checklist.md) § **Word-splitting / RU typography**.  
**Gulp agent:** [`../../agents/frontend-gulp-agent/frontend-rules.md`](../../agents/frontend-gulp-agent/frontend-rules.md), [`../../agents/frontend-gulp-agent/qa-checklist.md`](../../agents/frontend-gulp-agent/qa-checklist.md).  
**Consolidated rules:** [frontend-production-rules-v0.md](frontend-production-rules-v0.md) §12.

**Related layers:** [typography-rhythm-governance.md](typography-rhythm-governance.md), [production-hardening-rules-v1.md](production-hardening-rules-v1.md), [foundation-systems/responsive-system-v2.md](foundation-systems/responsive-system-v2.md).

---

## 1. Russian No Word-Splitting Rule (mandatory)

Russian words **must not** break inside the word on production landing pages. Line wraps occur at **spaces** (and at intentional typographic ties only).

### 1.1 Forbidden CSS

| Property / pattern | Status |
|--------------------|--------|
| `overflow-wrap: anywhere` | **Forbidden** on UI, headings, body default |
| `word-break: break-all` | **Forbidden** |
| `word-break: break-word` | **Forbidden** on UI and headings |
| `word-wrap: break-word` | **Forbidden** on UI and headings |
| `hyphens: auto` | **Forbidden** for Russian UI copy |
| Global `overflow-wrap: break-word` on `body` | **Forbidden** |
| `&nbsp;` between **every** word in a heading | **Forbidden** — creates one long unbreakable run; browser may split **inside** words when the run overflows |

### 1.2 Base rule (global default)

```css
html,
body {
  word-break: normal;
  hyphens: manual;
}
```

**Do not** set `overflow-wrap: break-word`, `overflow-wrap: anywhere`, `word-break: break-all`, or `word-break: break-word` on `html` or `body`.

### 1.3 Protected UI selectors

Headings and short UI surfaces **must** keep normal word boundaries:

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

Extend the same protection to project-specific heading/UI classes (hero titles, FAQ summaries, spec labels, consent text, footer links) when they carry short Russian UI copy.

### 1.4 Allowed exception — long body copy only

`overflow-wrap: break-word` is **permitted only** on long, multi-line **body** text where a single unbreakable token could cause horizontal overflow:

- paragraphs (`p`, `.section-lead`, card body copy)
- FAQ answer bodies
- legal / disclaimer / consent paragraphs
- long descriptions and notes

**Not permitted** on:

- H1 / H2 / H3 / H4 and visual heading classes
- buttons and CTA labels
- navigation and menu links
- card titles and short card labels
- form labels and short helper lines
- proof strips, badges, spec `dt`/`dd` pairs, and other short UI blocks

Prefer fixing layout width (`min-width: 0` on flex children, container constraints) before applying break-word to UI.

---

## 2. Russian typography rule (HTML)

Apply **selective** non-breaking ties — not wholesale `&nbsp;` chains.

### 2.1 Do tie (examples)

| Pattern | Example |
|---------|---------|
| Short prepositions / conjunctions with following word | `в&nbsp;Краснодаре`, `и&nbsp;краю`, `по&nbsp;России` |
| Number + unit | `5&nbsp;т`, `3&nbsp;т`, `14&nbsp;м`, `2&nbsp;часа` |
| Brand / product name integrity when source requires | project-specific; document in handoff |
| Em dash / quoted fragments | use proper RU punctuation; tie only where orphan prevention is intentional |

### 2.2 Do not tie

- Every word in a heading — use **normal spaces** between words; tie only high-value orphans.
- Meta tags, `alt`, JSON-LD, `href`, `src`, `data-*`, and other technical attributes — **plain text only**, no HTML entities for typography.
- User-generated or CMS-fed strings unless a dedicated content pipeline owns RU typography.

### 2.3 Review heuristic

If a heading string has more than **two** `&nbsp;` in a row of fewer than **eight** words, treat as **likely drift** — review against this rule.

---

## 3. Production QA checklist

**Canonical preset:** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) — required widths, checks, and supplementary-vs-mandatory rule. Do not treat generic 375 / 768 / 1280-only lists as authority for RU commercial landings.

Record in REPORT:

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

---

## 4. Root-cause patterns (from reference case)

Documented lessons from Triumph V5 — **not** automated detection:

1. **Global `overflow-wrap: break-word` on `body`** — inherited by headings and UI; remove from global default.
2. **Aggressive `word-break` / `anywhere` rules** — often added for overflow fixes; scope to long body copy only.
3. **`&nbsp;` between all heading words** — prevents normal wraps; overflow then forces mid-word breaks.

**Action:** centralize protection in a base/typography partial; allowlist break-word for paragraph roles only.

---

## 5. SAFE UNKNOWN

| Gap | Action |
|-----|--------|
| Non-Russian primary locale | This rule is **mandatory for RU** Factory landings; other locales need explicit pack rule |
| CMS / dynamic copy | Typography ties may be **SAFE UNKNOWN** until content pipeline is defined |
| Third-party widgets | Embedded UI may not obey project CSS — note in REPORT |
| Automated CSS audit | **Not** claimed; human DevTools spot-check at listed widths |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — integrated from Triumph V5 production fix; mandatory RU no word-splitting + selective typography ties |
| 2026-05-24 | §3 defers QA widths/checks to [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) (stabilization pass) |

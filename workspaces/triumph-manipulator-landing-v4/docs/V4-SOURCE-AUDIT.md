# Triumph Manipulator Landing V4 — Source Audit

## 1. Audit Scope

V4 is a clean reconstruction run initialized from fresh workspace state:

- Workspace: `workspaces/triumph-manipulator-landing-v4/`
- Primary source path requested for audit: `projects/triumph-manipulator-landing/design/v1/`
- Shared asset path requested for audit: `projects/triumph-manipulator-landing/design/shared-assets/`
- Governance lesson source: V3 documentation only, not V3 implementation.

This document is documentation-first and human-supervised. It does not claim production readiness, pixel-perfect fidelity, autonomous reconstruction, or final responsive accuracy.

## 2. Primary Source Authority

Primary V4 source authority is the V1 source pack described by:

- `projects/triumph-manipulator-landing/design/v1/`
- `projects/triumph-manipulator-landing/design/mockups-index.md`
- `projects/triumph-manipulator-landing/design/frontend-section-map.md` only as V1 continuity context.

The visible V1 index defines four raster slices:

| V1 source | Indexed dimensions | Authority role |
|---|---:|---|
| `design/v1/01.png` | 1672 x 941 | First strip / top segment of continuous landing scroll. |
| `design/v1/02.png` | 1672 x 941 | Continuation strip. |
| `design/v1/03.png` | 1672 x 941 | Continuation strip. |
| `design/v1/04.png` | 1536 x 1024 | Final strip with different export dimensions. |

The indexed natural order is `01.png` -> `02.png` -> `03.png` -> `04.png`.

## 3. Repo-Visible Evidence Status

The V1 folder path is referenced by project docs as the canonical V1 archive location. In this run, file search did not return concrete files from `design/v1/`.

Operational consequence:

- V4 may document the expected V1 authority boundary from project docs.
- V4 must not claim that V1 raster pixels were visually inspected until the files are visible and opened.
- Any section-level reconstruction requiring pixel evidence remains SAFE UNKNOWN until V1 raster files are confirmed.

## 4. Approved Secondary Sources

Secondary sources may guide discipline only:

- Updated Forge governance layers.
- V3 docs as governance lessons, drift history, failure evidence, and anti-pattern references.
- V2 docs only when explicitly used as prior lesson material, not as V4 implementation authority.

Secondary sources must not override V1 visual structure, section hierarchy, copy, cadence, atmosphere, or asset placement.

## 5. Not Authority

The following are not V4 authority:

- V3 partials, SCSS, DOM, layout fixes, hero hacks, responsive patches, reconstruction assets, crops, or local overrides.
- V2 implementation artifacts unless explicitly approved as lesson material.
- Shared asset filenames as section semantics.
- Screenshots or previews that are not part of the approved V1 source pack.
- Any decorative redesign, SaaS-like modernization, or inferred improvement of source intent.

## 6. Screen Structure Finding

Based on the V1 index, V1 is a continuous landing composed of four vertical raster exports, not four separate pages.

Confirmed by docs:

- The first segment is the top landing segment.
- The following three segments continue the vertical landing.
- `04.png` has a different size and therefore must be treated as a possible export/layout variance, not a reason to normalize or redesign.

SAFE UNKNOWN:

- Exact visual content of each V1 strip is not confirmed from raster inspection in this run.
- Exact section names, copy, image crops, CTA positions, and breakpoint behavior remain unverified.

## 7. Section Cadence Finding

The only confirmed cadence at this stage is strip order:

1. Top segment.
2. Continuation.
3. Continuation.
4. Final segment.

The V1 `frontend-section-map.md` maps this to placeholder strip names (`landing-strip-01` through `landing-strip-04`) for continuity only. V4 must not inherit those names as final semantic section names unless later source analysis confirms they are still useful.

## 8. Atmosphere Transition Finding

Atmosphere transitions cannot be honestly reconstructed from docs alone. They require direct visual inspection of V1 `01.png` through `04.png`.

Until raster visibility is restored, V4 may only preserve this rule:

- Atmosphere must follow V1 visual evidence.
- Any transition language such as dark-to-light, technical-to-commercial, proof-to-conversion, or footer closure is SAFE UNKNOWN unless confirmed from V1 pixels.

## 9. Commercial Pressure Rhythm Finding

Commercial pressure rhythm is not yet verified from V1 pixels.

V4 must identify, after raster inspection:

- First conversion pressure.
- Secondary CTA rhythm.
- Proof or trust pressure.
- Form or contact pressure.
- Footer/contact closure.

No CTA priority, form placement, pricing emphasis, or proof hierarchy may be invented from V2/V3 memory.

## 10. Header Ownership Finding

Critical separation for V4:

**HEADER != HERO != SLIDER**

Even if these systems visually occupy the same first viewport, they have separate ownership:

- Header system: brand, navigation, contact affordances, mobile menu ownership, persistence rules.
- First-screen shell: viewport composition and structural containment of first visible screen.
- Hero content system: headline, offer, supporting text, CTA logic, commercial priority.
- Hero background ownership: imagery/background treatment used by first-screen shell or hero.
- Future slider possibility: not authorized unless V1 source or operator explicitly proves slider behavior.
- Mobile header ownership: mobile navigation and contact survivability, not hero layout patchwork.
- Navigation survivability: links and contact entry points must remain understandable under responsive collapse.

## 11. Likely Reusable Visual Systems

From `design/shared-assets/`, likely reusable systems are:

- Brand identity: dark logo, white logo, favicon.
- Social/contact icons: Telegram, WhatsApp, MAX.
- Review/proof marks: Avito logo, Yandex logo, rating star.

These are visual material candidates only. They do not define screen order, section meaning, copy, or layout.

## 12. Typography Survivability Rule

V4 HTML must apply Russian typography survivability as an operational rule.

Use `&nbsp;` where required, including:

- `в&nbsp;Краснодаре`
- `с&nbsp;НДС`
- `от&nbsp;30&nbsp;минут`
- `и&nbsp;т.д.`
- `для&nbsp;юр.&nbsp;лиц`

This is not optional styling. It applies to headings, CTA labels, benefits, cards, forms, proof blocks, footer text, and any user-visible Russian HTML.

## 13. SAFE UNKNOWN

- Concrete V1 raster files were not confirmed by file search during this audit.
- Exact first-screen visual decomposition remains pending direct V1 raster inspection.
- Exact section naming, copy locks, CTA hierarchy, and responsive behavior remain pending source evidence.
- No production readiness or pixel fidelity claim is authorized.

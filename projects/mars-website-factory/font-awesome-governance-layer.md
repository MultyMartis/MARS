# MARS Website Factory — Font Awesome Governance Layer

**Status:** documented governance and implementation discipline only.  
**Scope:** Font Awesome icon selection for Forge frontend rebuilds, Triumph V2 implementation, and future Website Factory static frontend production.  
**Not:** a runtime icon registry, SVG pipeline, React component API, design-token engine, automated icon selector, or license distribution mechanism.

**Companion semantic layer:** [semantic-iconography-governance.md](semantic-iconography-governance.md).

---

## 1. Purpose

This layer prevents icon drift caused by visual approximation:

- semantic mismatch: the glyph looks acceptable but says the wrong thing;
- inconsistent visual weight: light, regular, solid, brands, or custom glyphs mixed without a section rule;
- optical rhythm drift: icon size, gap, alignment, or density breaks the section beat;
- family contamination: FA versions, third-party packs, emoji, or ad-hoc SVGs enter the same UI language.

The layer is intentionally small: select from the approved Font Awesome source, record rationale where risk exists, verify section-local consistency during Forge review, and report exceptions honestly. Font Awesome availability is not semantic authority; icon selection must follow the meaning-first rules in the semantic iconography layer.

---

## 2. Canonical FA Version Policy

| Rule | Policy |
|------|--------|
| Canonical source | **Font Awesome Pro 5.15.4** only, from the project-approved local licensed library when available. |
| Version mixing | Do not mix FA 6+, free CDN substitutes, third-party outline packs, or AI-generated glyphs into the governed UI. |
| Integration mode | Follow the target project: CSS+webfont, extracted individual SVGs, or a small sprite are all acceptable if already used or approved. This layer does not mandate a pipeline. |
| Licensed material | Do not bulk-publish or attach the full Pro library. Copy only selected project assets when the project workflow allows it. |
| Name verification | For FA5 class-based usage, verify icon names against the local FA 5.15.4 CSS or project mapping before implementation. |

**SAFE UNKNOWN:** if the target project has not declared whether icons are consumed via webfont, sprite, or extracted SVG, inspect the implementation before changing icons. Do not introduce a second delivery mode casually.

### 2.1 Startup Readiness Rule

Font Awesome readiness must be decided during project bootstrap, before section implementation. Do not wait until visual QA or late browser review to discover missing icons, square glyphs, broken font paths, or placeholder text marks.

If Font Awesome may be needed:

- inspect the approved FA source first: `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`;
- prepare the local FA delivery structure early, usually `css/` plus `webfonts/` when the project uses CSS+webfont delivery;
- use real `woff2` and `woff` webfonts for webfont delivery;
- preserve the relative `css/` to `webfonts/` path relationship used by `@font-face`;
- avoid SVG-font-only delivery for production frontend output;
- avoid copying the whole Pro library when a small governed subset is enough;
- avoid random icon selection: choose glyphs by semantic meaning first, then by visual fit.

If `woff2` / `woff` assets are missing from the approved local source, record **SAFE UNKNOWN** or block the implementation until the licensed webfont files or an approved conversion/export path is available.

### 2.2 Duotone Delivery Rule

Duotone Font Awesome delivery requires verified matching assets before use:

- real duotone `woff2` and `woff` webfonts that match the CSS `@font-face` paths, or
- an approved inline SVG / SVG sprite source with verified glyphs and licensing.

Absent duotone webfonts are a blocker, not an invitation to guess. Do not fake duotone by changing classes to `fad`, copying CSS that references missing files, or relying on SVG-font-only delivery for final frontend output.

Final build acceptance for any FA webfont mode requires the built `dist` artifact to contain every webfont referenced by CSS.

Visual softening of solid icons does **not** equal duotone. When true duotone is unavailable, do not fake font delivery. Use verified solid icons and visually soften via controlled SCSS:

- opacity;
- outline;
- background restraint;
- sizing balance;
- container pressure.

Duotone may only be considered active when verified duotone webfonts exist and render correctly, or when approved inline SVG duotone assets are used. Absent verified assets, the implementation status must be declared honestly as solid fallback / CSS-softened solid / verified solid delivery.

### 2.3 Glyph Rendering Verification Rule

Font Awesome readiness is not complete until glyph rendering is verified in the built `dist` output. CSS files, copied webfonts, and passing asset paths are necessary but not sufficient.

Before accepting FA delivery:

- verify that every used FA class is mapped in the project CSS;
- verify that every mapped codepoint exists in the selected font source;
- verify that `@font-face` `font-family`, `font-weight`, and relative webfont paths match the rendered classes;
- verify the built page renders real icons, not tofu squares, fallback boxes, or incorrect glyphs;
- treat generated subsets as **untrusted** until checked against the actual used classes and codepoints.

If glyph mapping is uncertain, prefer extracted inline SVG or a local SVG sprite from the approved Font Awesome source over broken icon-font delivery. Do not freeze a page with broken FA glyphs just because CSS and webfont files exist.

---

## 3. Family and Style Consistency

Font Awesome style is part of visual hierarchy, not a decoration choice.

| Style | Preferred use |
|-------|---------------|
| `fal` light | Primary technical / informational marketing icons at medium or large size where clarity and premium calm matter. Prefer for feature rows, trust strips, specification rows, and large explanatory cards if contrast is sufficient. |
| `far` regular | Secondary UI where light is too thin but solid is too heavy: small arrows, compact inline affordances, supporting controls. |
| `fas` solid | Small, dense, or high-contrast UI: plus/minus, check bullets, phone icons, compact stats, small CTA/support indicators. Use deliberately; do not let solid become the default for large marketing panels unless the design source calls for heavy silhouettes. |
| `fab` brands | Brand glyphs only: WhatsApp, Telegram, etc. Do not use brand style for generic UI metaphors. |
| Custom / brand asset | Allowed for official marks not covered by FA Brands, partner logos, marketplace marks, or project-owned symbols with no FA equivalent. Must be documented as an exception. |

**Section rule:** inside one visual section or repeated component family, keep one dominant FA weight unless there is a role hierarchy reason. Mixed light + solid can be valid when light carries explanatory icons and solid carries tiny UI bullets, but arbitrary weight mixing is **mixed-weight UI drift**.

---

## 4. Semantic Icon Matching

Icon selection starts from meaning, then visual fit.

### 4.1 Matching order

1. **Role:** what job does the icon do: feature, trust proof, specification, warning, CTA, contact, brand, decoration?
2. **Semantic noun / action:** what concrete meaning must be recognized: delivery speed, legal payment, route, lifting capacity, operator identity?
3. **FA availability:** choose a FA 5.15.4 glyph that names the same concept or the closest truthful industrial metaphor.
4. **Section rhythm:** confirm the chosen glyph works with the section’s dominant style, size, and spacing.
5. **Exception:** if no truthful FA glyph exists, document custom / brand / SAFE UNKNOWN rather than forcing a visual approximation.

No random Font Awesome usage is allowed. No playful SaaS icon drift should enter operational or commercial landings unless the approved source explicitly establishes that tone.

### 4.2 Recommended naming examples

| Meaning | Preferred FA 5.15.4 direction | Notes |
|---------|--------------------------------|-------|
| Fast equipment arrival | `shipping-fast` | Better than a generic clock when logistics is the meaning. |
| Lifting capacity / tonnage | `weight-hanging` | Direct load metaphor; can repeat across sections if role remains consistent. |
| Route / trips | `route` | Stronger semantic match than a decorative arrow. |
| Work geography | `map-marked-alt` | Area coverage, not only a pin. |
| VAT / business payment | `file-invoice-dollar`, `file-signature`, `balance-scale` | Pick by exact local text: invoice, documents, legal/tax confidence. |
| Operator / staff qualification | `id-badge` | Professional identity without trophy-like noise. |
| Phone CTA | `phone-alt` or project-approved phone glyph | Usually `fas` in small CTA/support contexts. |
| Social contact | `fab fa-whatsapp`, `fab fa-telegram-plane` | Brands only; missing brands remain custom assets. |

### 4.3 Anti-patterns

| Anti-pattern | Drift introduced |
|--------------|------------------|
| Picking the prettiest nearby glyph | **Visual approximation drift** and semantic mismatch. |
| Reusing one document icon for VAT, contract, warranty, and “no hidden fees” | Semantic flattening; one glyph carries multiple incompatible meanings. |
| Using solid stats icons beside light feature icons inside the same trust strip without role separation | **Mixed-weight UI drift**. |
| Replacing partner / messenger marks with generic FA symbols | Brand contamination. |
| Adding emoji or random downloaded SVGs because FA lacks a perfect glyph | Icon contamination and license uncertainty. |

---

## 5. Icon Role Hierarchy

Use role hierarchy to choose weight, size, and review strictness.

| Role | Typical weight | Review priority |
|------|----------------|-----------------|
| Hero / primary feature icon | `fal` or project-approved dominant style | High: affects first-screen quality and semantic read. |
| Trust strip icon | One section-local dominant weight, usually `fal` for large strip or `fas` only for dense strip | High: proof icons can displace or cheapen trust if inconsistent. |
| Specification row icon | `fal` / `far`, stable width column | High: must map to exact spec meaning. |
| CTA / support icon | `fas` or `far` at small size | Medium-high: must not compete with CTA label or break tap target. |
| Prohibition / warning list icon | Usually `fas` for clear small marks, or section-local rule | High: wrong glyph can invert meaning. |
| Decorative / atmospheric icon | Prefer none unless source requires it | High skepticism: decoration often becomes visual noise. |
| Social / contact brand | `fab` or documented custom brand asset | High: brand correctness and licensing. |

Baked image annotations and icons are not icon slots. If an icon, label, number, or callout is already baked into a source image, do not duplicate it as a separate HTML/CSS overlay unless it is independently required content and the duplication decision is documented.

---

## 6. Optical Rhythm Rules

Optical rhythm is checked by the human reviewer in the built UI, not by a runtime system.

- Use `currentColor` or the project’s established color handling unless a brand asset requires fixed color.
- Keep icon + label gap consistent inside a component family, commonly 6-8px for inline UI and 12-16px for larger cards depending on project tokens.
- Give repeated row icons a fixed width / alignment box so text columns do not wobble.
- Set icon `line-height: 1` or equivalent when the project uses font icons.
- Do not scale every glyph to the same CSS box and assume equal optical weight; wide and tall glyphs may need section-local adjustment.
- Prefer one dominant icon size per repeated role: trust strip, spec rows, CTA support, social row.
- If an icon becomes visually louder than its label in a supporting row, reduce size, weight, color contrast, or replace the glyph.
- If light icons disappear at small size or on textured/dark backgrounds, escalate to `far` or `fas` for that role and document the section-local override.
- On light backgrounds, operational icons should usually render as clean glyphs without artificial containers unless the source/design explicitly requires badges. Containerized icon treatment is mainly for dark/contrast sections or when readability requires it.

---

## 7. Allowed Exception Logic

| Exception | Allowed when | Required note |
|-----------|--------------|---------------|
| Brand asset outside FA | Official brand is absent or FA glyph is not legally / visually acceptable. | Name the brand and source path. |
| Custom project SVG | FA has no truthful glyph for a domain-specific object, and the project already owns/approves the asset. | Explain why FA approximation would be misleading. |
| Solid inside a light section | Icon is small, dense, functional, or needs stronger contrast. | State role boundary, e.g. “solid only for CTA/check bullets.” |
| Section-local weight override | Source screen clearly uses heavier/lighter icon rhythm than global default. | Record source reference and section boundary. |
| Temporary placeholder | Design source does not resolve final icon. | Mark **SAFE UNKNOWN** and avoid freezing as final. |

Exceptions are human-supervised decisions. They are not a license to introduce an alternate icon system.

---

## 8. Icon Drift Taxonomy

Use these labels in Forge reports when icon problems appear. Report semantic and operational icon issues as `ICONOGRAPHY FINDINGS`.

| Drift type | Definition |
|------------|------------|
| **Icon semantic mismatch** | Glyph meaning does not match the local text or role. |
| **Icon semantic dilution** | One glyph is reused across multiple different meanings until the section loses specificity. |
| **Visual approximation drift** | Glyph was selected for visual resemblance rather than meaning. |
| **Mixed-weight UI drift** | FA styles / weights mix inside one section without role hierarchy. |
| **Icon family contamination** | FA versions, non-FA packs, emoji, AI-generated SVGs, or unapproved custom icons mix into the governed set. |
| **Brand contamination** | Generic FA UI glyph replaces an official brand or partner mark, or brand glyph is used as generic UI. |
| **Optical rhythm drift** | Icon size, weight, gap, baseline, or alignment breaks repeated component rhythm. |
| **Decorative icon noise** | Added icons increase visual noise without source-backed role. |
| **Role inversion** | Supporting icon becomes more visually dominant than primary copy, CTA, or spec value. |
| **SaaS icon drift** | Playful/generic SaaS icon language replaces operational or industrial meaning. |
| **Baked annotation duplication** | Icons or labels already inside source pixels are recreated as separate UI overlays. |

These terms complement [visual-drift-taxonomy.md](visual-drift-taxonomy.md); they do not replace visual reconciliation.

---

## 9. Forge Implementation Guidance

Forge should treat icon selection as part of visual reconciliation and freeze discipline.

### 9.1 Before implementation

- Read the active design source and implementation pack for icon-bearing regions.
- Identify icon roles before naming glyphs: trust strip, spec rows, CTA/support, lists, social/contact, decoration.
- Check project policy for FA version and delivery mode.
- Prepare a small icon map for risky sections: role, text meaning, FA name/style, confidence, exception if any.

### 9.2 During G6 / G7 review

- **G6 visual reconciliation:** check icon semantic fidelity, family consistency, optical rhythm, and whether icons alter hierarchy or trust placement.
- **G7 composition awareness:** check whether icon rows are visually grouped with the intended copy/spec/list cluster. A correct glyph can still drift if the icon column splits the cluster or over-frames it.
- If icon choice is unresolved, record `PARTIAL` or **SAFE UNKNOWN** rather than freezing silently.

### 9.3 Rebuild freeze checks

Before freeze, confirm:

- no unapproved FA version or icon family entered the section;
- repeated section roles use a consistent style rule;
- exceptions are named and local;
- icons do not change CTA hierarchy, trust dominance, or specification readability;
- source files only were changed; generated output remains build artifact.

### 9.4 REPORT wording

```text
ICONOGRAPHY FINDINGS — <section or block_id> — <source ref>

Icon roles reviewed:
- <trust strip / spec rows / CTA / social / etc.>

FA policy:
- Canonical source: Font Awesome Pro 5.15.4
- Dominant section style: <fal / far / fas / fab / custom exception>

Drift labels:
- <none / icon semantic mismatch / optical rhythm drift / etc.>

Exceptions:
- <brand/custom/SAFE UNKNOWN, if any>

Disposition: PASS | PARTIAL | FAIL
```

---

## 10. Triumph V2 Immediate Usage Recommendations

Triumph V2 should continue treating Font Awesome Pro 5.15.4 as the canonical glyph source, with the project-specific policy and mapping remaining local references.

### 10.1 Screen 01 — hero and trust strip

- Trust strip icons should preserve a single calm technical rhythm, preferably `fal` where size and contrast allow.
- Delivery / response claims should use logistics/time glyphs that match the copy, e.g. `shipping-fast` for fast arrival rather than a generic decorative clock when the meaning is dispatch.
- VAT / documents / legal confidence should not all share one “document” symbol. Match exact local text: invoice, signature/contract, balance/legal confidence.
- CTA and support icons may use stronger `fas` / `far` at small size, but only inside the CTA/support role so they do not contaminate the trust strip.

### 10.2 Screen 02 — machine specifications and transport lists

- Specification rows need direct semantic fidelity: length, boom/reach, lifting capacity, route/transport, dimensions, or similar exact meanings from the approved source.
- Prohibition / transport lists should avoid clever or decorative metaphors. If the list means “transported” vs “not transported,” the icon role should make the contrast obvious without overpowering text.
- Keep specification icon boxes aligned and section-local. Icons should support reading machine facts, not turn the one-machine section into a fleet catalog.
- If FA has no truthful manipulator / crane-boom glyph, use the closest documented industrial metaphor or retain a project-approved SVG as an exception. Do not invent a fake crane icon.

### 10.3 CTA, support, social, and contact icons

- CTA/support icons should be small, robust, and subordinate to labels: phone, arrow, stopwatch, check.
- Social/contact icons should use `fab` for WhatsApp / Telegram where available. Missing or project-specific brands, such as messenger marks absent from FA 5.15.4, remain custom brand assets.
- Review / marketplace partner marks are brand assets, not generic FA replacements.

---

## 11. Relations to Existing Layers

| Neighbor | Relationship |
|----------|--------------|
| [visual-reconciliation-layer.md](visual-reconciliation-layer.md) | Icon governance adds semantic and optical icon-specific checks to the human visual read. |
| [visual-drift-taxonomy.md](visual-drift-taxonomy.md) | Icon drift labels can be reported alongside hierarchy, density, trust, and foundation contamination drift. |
| [compositional-structure-awareness.md](compositional-structure-awareness.md) | Icon rows and list clusters can create or reveal composition fragmentation. |
| [`../../agents/mars-forge/workflow.md`](../../agents/mars-forge/workflow.md) | Forge applies icon review during QA/freeze, not as a separate runtime phase. |
| Triumph V2 icon policy | Project-local policy remains authoritative for exact local paths and implementation mode. This layer supplies reusable governance vocabulary. |

---

## 12. SAFE UNKNOWN

- Exact FA delivery mode is project-specific until the target frontend is inspected.
- Final Triumph V2 icon names for not-yet-implemented screens depend on approved source text and glyph availability verification.
- This layer does not verify license scope, CDN rights, or external redistribution terms; operators must follow local licensed-asset rules.
- This layer does not prove visual parity, accessibility compliance, or build success without a project run and human review.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-16 | Initial Font Awesome governance mini layer for Forge, Triumph V2, and Website Factory frontend production. |
| 2026-05-18 | Added semantic iconography companion, random-FA prohibition, SaaS icon drift warning, baked annotation duplication rule, and `ICONOGRAPHY FINDINGS` wording. |
| 2026-05-18 | Added startup readiness rule: FA source, local delivery structure, webfont paths, `woff2`/`woff`, and semantic icon choice must be settled during bootstrap. |
| 2026-05-18 | Added glyph rendering verification rule: built `dist` rendering, class/codepoint/font matching, and generated subset verification are required before FA readiness can pass. |
| 2026-05-18 | Added duotone delivery rule: duotone requires verified matching webfonts or approved inline SVG/sprite source; missing webfonts block the switch. |
| 2026-05-18 | Added solid-icon softening fallback: when true duotone is unavailable, keep verified solid delivery and soften only through controlled SCSS; CSS softening is not duotone. |

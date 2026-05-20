# MARS Website Factory - Semantic Iconography Governance

**Status:** **documented** - Website Factory icon meaning and operational icon selection methodology only.  
**Not:** automatic icon picker, icon registry engine, SVG pipeline, license manager, or Font Awesome validator.

**Core principle:** icon selection follows semantic meaning first. Visual style is secondary to operational/commercial meaning.

**Related layers:** [font-awesome-governance-layer.md](font-awesome-governance-layer.md), [section-language-governance.md](section-language-governance.md), [commercial-density-governance.md](commercial-density-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md).  
**Forge findings category:** `ICONOGRAPHY FINDINGS`.

---

## 1. Purpose

This layer generalizes icon governance beyond Font Awesome mechanics. V4 exposed that an icon can be technically valid, visually acceptable, and still semantically wrong.

It governs:

- semantic iconography;
- operational icon selection;
- FA semantic compatibility;
- no random Font Awesome usage;
- no playful SaaS icon drift;
- baked image annotation discipline;
- commercial/operational semantics first.

---

## 2. Icon Selection Order

1. **Meaning:** what exact noun, action, proof, operation, or commercial promise must the icon support?
2. **Role:** is it a specification, trust proof, CTA support, social brand, warning, process step, or decoration?
3. **Source authority:** is the icon independent UI content, baked into an image, or absent from the source?
4. **Operational fit:** does the glyph match industrial/service semantics rather than generic SaaS charm?
5. **FA compatibility:** if using Font Awesome, does the FA glyph truthfully map to the meaning?
6. **Visual rhythm:** does the icon fit section weight, size, alignment, and density?
7. **Exception:** if no truthful glyph exists, document custom/brand/SAFE UNKNOWN instead of forcing an icon.

---

## 3. Canonical Rules

- Icon selection must follow semantic meaning first.
- Font Awesome readiness must be decided during project bootstrap, before section implementation, when iconography may be needed.
- If Font Awesome may be needed, inspect `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`, prepare local delivery early, preserve `css/` to `webfonts/` paths, and use real `woff2` / `woff` files for webfont delivery.
- Font Awesome readiness is not complete until built `dist` rendering is verified: CSS/webfont presence is not enough, and generated subsets must be checked against actual used classes and codepoints.
- No random Font Awesome usage.
- No playful SaaS icon drift in operational/commercial landings unless source explicitly calls for it.
- Operational/commercial semantics come before decorative friendliness.
- A generic icon must not replace a specific operational meaning.
- SVG-font-only delivery is not an acceptable final answer for governed CSS+webfont iconography.
- Brand, review, and marketplace marks are assets, not generic icon slots.
- Baked image annotations, labels, callouts, and icons must not be duplicated as HTML/CSS overlays unless they are independently required content and not already baked into the source pixels.
- If the source icon meaning is unclear, record **SAFE UNKNOWN** instead of guessing a glyph.

---

## 4. Drift Lessons Captured

| Drift | Governance lesson |
|-------|-------------------|
| **Random FA icon selection** | FA availability is not semantic authority. |
| **Icon semantic mismatch** | A pretty or nearby glyph can misstate the service promise. |
| **SaaS icon drift** | Playful generic icons can sterilize industrial/commercial tone. |
| **Baked annotation duplication** | Source-image labels and callouts must not be recreated as duplicate overlays. |
| **Operational flattening** | One icon reused for VAT, contract, no hidden fees, documents, and legal work erases meaning. |

Required V4 lesson labels captured: `random FA icon selection`, `icon semantic mismatch`, `SaaS icon drift`.

---

## 5. FA Semantic Compatibility

Font Awesome is allowed only when:

- project policy allows it;
- delivery mode is known or documented;
- selected glyph maps to the local meaning;
- style/weight follows section role;
- exceptions are local and disclosed.

If a Font Awesome glyph is only visually close, but semantically false, do not use it. If a glyph is technically uncertain, renders as a square, or maps to the wrong icon, do not ship the icon-font state. Record `ICONOGRAPHY FINDINGS` and either choose a better verified glyph, use an approved asset, extract inline SVG / sprite from the approved FA source, or mark **SAFE UNKNOWN**.

---

## 6. Forge Use

Record `ICONOGRAPHY FINDINGS` for:

- icon semantic mismatch;
- random FA use;
- SaaS/playful drift;
- operational meaning loss;
- baked annotation duplication;
- brand/generic replacement;
- unresolved icon source authority.

`ICONOGRAPHY FINDINGS` supersede older local wording such as `ICON FINDINGS` where the issue is semantic or operational. Font Awesome delivery/path problems may still be described inside the same category.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Icon is visible only inside a raster export | Cannot prove whether it is independent UI or baked image content. |
| FA version/delivery mode is not known | Cannot safely add Font Awesome. |
| Source copy and icon metaphor conflict | Cannot choose truthfully without decision. |
| Brand mark is absent from approved assets | Cannot replace it with a generic icon silently. |
| Mobile icon behavior is missing | Cannot prove icon-label survivability. |

**Action:** document icon role, source authority, chosen glyph/asset, and unresolved exceptions before freeze.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial semantic iconography governance from Triumph V4 lessons. |
| v0.1 | 2026-05-18 | Added Font Awesome startup readiness and webfont delivery requirements. |
| v0.2 | 2026-05-18 | Added built-output glyph rendering verification and generated-subset caution. |

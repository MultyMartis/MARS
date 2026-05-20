# MARS Website Factory - First-Screen Decomposition Model

**Status:** **documented** - Website Factory first-screen decomposition model for human-supervised reconstruction and QA.  
**Not:** rendering engine, component framework, automatic layout splitter, or universal first-viewport template.

**Core principle:** “first screen” is a composition zone, not a single architectural owner.

**Related layers:** [layout-shell-governance.md](layout-shell-governance.md), [background-ownership-governance.md](background-ownership-governance.md), [commercial-density-governance.md](commercial-density-governance.md), [atmosphere-continuity-governance.md](atmosphere-continuity-governance.md), [section-language-governance.md](section-language-governance.md), [compositional-structure-awareness.md](compositional-structure-awareness.md).  
**Forge findings category:** `FIRST-SCREEN DECOMPOSITION FINDINGS`.

---

## 1. Purpose

This model decomposes first-screen work into separate architectural systems so Forge does not over-merge header, hero, background, atmosphere, mobile navigation, and conversion logic.

It covers:

- first-screen decomposition;
- header layer;
- hero layer;
- atmospheric layer;
- background layer;
- overlay layer;
- mobile navigation layer;
- conversion layer;
- compositional cohabitation.

---

## 2. Layer Taxonomy

| Layer | Owns | Does not own by default |
|-------|------|-------------------------|
| **Header layer** | Brand, nav, menu trigger, persistent navigation readability | Hero headline, hero CTA, hero proof |
| **Hero layer** | Opening offer, H1, support copy, hero CTA/proof/media | Global nav architecture or page shell |
| **Atmospheric layer** | Emotional pressure, visual heaviness, industrial mood, environmental rhythm | Source authority, content hierarchy, or nav behavior |
| **Background layer** | Shell or section-local background surfaces, media, gradients, bands | Overlay behavior unless mapped |
| **Overlay layer** | Scrims, darkening, readability surfaces, foreground separation | Asset mutation or content semantics |
| **Mobile navigation layer** | Mobile menu behavior, focus/tap model, responsive nav ownership | Hero-specific CTA behavior |
| **Conversion layer** | CTA rhythm, trust cues, urgency/proof pressure in the opening viewport | Navigation or decorative atmosphere |

---

## 3. Compositional Cohabitation

First-screen layers may visually occupy the same viewport. Cohabitation is valid when ownership stays visible:

- header may overlay the hero background;
- hero content may sit inside shell max-width rules;
- atmosphere may span header and hero;
- conversion cues may sit inside hero but follow commercial pressure governance;
- mobile navigation may obscure hero temporarily but remains navigation-owned.

Cohabitation becomes drift when shared space becomes shared ownership by accident.

---

## 4. Canonical Rules

- Map first-screen layers before implementation when a rebuild touches header, hero, background, or mobile nav.
- Record which layer owns each background, overlay, CTA, and responsive behavior.
- Do not repair one layer by silently changing another.
- Treat first-screen ambiguity as an architectural finding, not a styling problem.
- Keep the model bounded: use it for first viewport / opening composition, not every page section.

---

## 5. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **One-blob first screen** | All first-viewport concerns are implemented as one owner. |
| **Header/hero collapse** | Header decisions are hidden inside hero implementation. |
| **Atmosphere as background only** | Emotional pressure is reduced to a CSS image or gradient. |
| **Overlay ownership ambiguity** | Scrims and readability layers appear without owner or rationale. |
| **Mobile nav afterthought** | Mobile menu is bolted onto hero layout after desktop work. |
| **Conversion buried in aesthetics** | Hero looks polished but CTA/proof pressure is weak or accidental. |

---

## 6. Drift Patterns

- **First-screen ambiguity drift** - the opening viewport lacks ownership decomposition.
- **Over-merged first-screen logic** - header, hero, atmosphere, background, overlay, mobile nav, and conversion logic share one implementation path.
- **Compositional cohabitation failure** - visually overlapping systems fight because ownership is unmapped.
- **Mobile navigation ambiguity drift** - mobile nav inherits hero layout constraints instead of shell/nav rules.

---

## 7. Triumph V3 Lesson

Triumph V3 showed that the phrase “first screen” hid at least six systems: layout shell, navigation, hero, atmosphere, background/overlay, mobile navigation, and conversion environment.

The reusable governance lesson is to decompose before building. This model is not a visual template or implementation recipe.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Source shows overlap but not ownership | Cannot assign shell, hero, background, or overlay authority. |
| Mobile state is missing | Cannot infer menu behavior, overlay, or focus handling. |
| CTA belongs visually to hero but functionally to sticky/nav | Conversion ownership needs mapping. |
| Background spans multiple layers | Requires background ownership governance. |
| Existing implementation merges all layers | Cannot safely modify one concern without impact review. |

**Action:** create a first-screen ownership map before implementation or freeze.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial First-Screen Decomposition Model from Triumph V3 battle-test lessons. |

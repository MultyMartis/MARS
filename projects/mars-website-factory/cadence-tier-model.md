# MARS Website Factory — Cadence Tier Model

**Status:** **documented** — deterministic Website Factory vocabulary for human-supervised vertical cadence decisions.  
**Not:** universal px scale, spacing-token engine, runtime layout system, autonomous pacing AI, or automatic visual balancing.

**Parent canon:** [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md).  
**Forge checklist:** [`../../agents/mars-forge/cadence-governance-checklist.md`](../../agents/mars-forge/cadence-governance-checklist.md).

---

## 1. Purpose

Cadence tiers give operators a repeatable way to discuss inter-screen spacing as **narrative pacing**, not random margins.

The model uses canonical tier names:

```text
XS → S → M → L → XL
```

These tiers are **intent bands**. They should be mapped to project-specific spacing tokens or ranges inside a project implementation pack. Website Factory does **not** define universal pixel truth.

---

## 2. Tier Model

| Tier | Cadence intention | Pacing role | Breathing role | Density impact | Transition role |
|------|-------------------|-------------|----------------|----------------|-----------------|
| **XS** | Tight continuation | Keeps one micro-beat attached to the previous content | Minimal air; no reset | Safe only for low-density or same-cluster content | Internal continuation, not a section boundary default |
| **S** | Soft continuation | Moves quickly while preserving a visible boundary | Light breathing | Works for similar-density neighbors | Same mood / same narrative lane |
| **M** | Standard section cadence | Default authored transition between ordinary landing sections | Balanced reset | Handles moderate density without fatigue | Normal section-to-section pacing |
| **L** | Pacing reset | Slows the reader before/after density, CTA, or mood shift | Strong breathing | Reduces section pressure and visual exhaustion | Dense → light, light → dense, dark/light, proof → CTA |
| **XL** | Major narrative reset / closure | Marks a chapter break, high-stakes CTA, or terminal closure | Maximum intentional breathing | Prevents dense stacks or final CTAs from feeling bolted together | Hero exit, major CTA isolation, footer closure, large mood transition |

---

## 3. Deterministic Mapping Rule

Each project should map tier names to its own spacing scale:

| Required field | Meaning |
|----------------|---------|
| **tier** | `XS`, `S`, `M`, `L`, or `XL`. |
| **project token / range** | Project-specific token or approved range. Do not treat Website Factory examples as universal px values. |
| **allowed use** | Which section roles or boundaries may use this tier. |
| **forbidden use** | Boundaries where the tier would create compression, collision, or whitespace desert. |
| **mobile adaptation** | How the tier changes at mobile widths while preserving narrative pacing. |
| **source authority** | Design export, implementation pack, section map, or HITL decision that authorizes it. |

If this mapping is absent, cadence QA may still identify obvious risks, but exact tier assignment should be reported as **SAFE UNKNOWN**.

---

## 4. Tier Selection Rules

- Use **XS** only inside tightly related clusters or local component stacks. It should not become the default inter-screen boundary.
- Use **S** for low-pressure continuation when neighboring sections share mood, density, and narrative role.
- Use **M** for ordinary section transitions where neither side creates unusual density, CTA, or contrast pressure.
- Use **L** when the boundary carries density bridge, dark/light cadence, CTA approach, or a rhythm reset.
- Use **XL** for major chapter breaks, CTA isolation, footer closure, or a reset after multiple dense/light sections.
- Do not assign a larger tier just to “make it pretty.” The tier must explain pacing, breathing, density, or transition need.
- Do not assign the same tier everywhere unless the page truly has identical section pressure, which is rare for marketing landings.

---

## 5. Transition Heuristics

| Boundary type | Typical tier direction | Review question |
|---------------|------------------------|-----------------|
| Same role → same role | `S` or `M` | Does continuity remain readable without flattening? |
| Sparse → dense | `M` or `L` | Is there enough approach before the content wall? |
| Dense → sparse | `L` or project-approved `M` | Does the reset breathe without becoming a whitespace desert? |
| Dense → dense | `L` often required | Is visual exhaustion prevented across the stack? |
| Dark → light / light → dark | `L` often required | Does contrast change feel authored, not collided? |
| Proof → CTA | `L` or `XL` | Does the CTA gain isolation and dominance? |
| CTA → footer | `L` or `XL` | Does the footer close the page deliberately? |
| Mobile dense stack | Project-specific compressed `M/L` | Does scan rhythm survive smaller widths? |

These are governance heuristics, not pixel calculations.

---

## 6. Cadence Escalation / Flattening

**Cadence escalation** is appropriate when narrative pressure increases:

- proof density grows
- CTA stakes rise
- dark/light contrast changes
- footer closure approaches
- multiple dense/light sections sit adjacent

**Cadence flattening** is drift when all boundaries use the same gap because of a global class, copied SCSS, or Figma slice compression. Flattening may look consistent but still damage pacing.

---

## 7. Mobile Cadence

Mobile cadence should be smaller in physical space but not smaller in intent.

Review mobile separately:

- Heading wraps need title → body breathing.
- Card stacks need item separation.
- CTA clusters need tap-safe isolation.
- Dense lists need scan breaks.
- Footer groups need closure rhythm.

When mobile source is missing, report exact tier mapping as **SAFE UNKNOWN** and validate only survivability plus reasonable project-scale continuity.

---

## 8. Reporting Shape

Use tier vocabulary in `CADENCE FINDINGS`:

```text
Boundary: <section A> → <section B>
Expected tier: XS | S | M | L | XL | SAFE UNKNOWN
Observed tier / feel: <tight / standard / reset / excessive / contaminated>
Reason: <pacing, breathing, density, transition, closure>
Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN
```

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-16 | Initial deterministic cadence tier model (`XS`–`XL`) without universal px claims. |

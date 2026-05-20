# MARS Website Factory — Token Drift Taxonomy

**Status:** **documented** — Website Factory token drift vocabulary for human-supervised frontend QA.  
**Not:** automated token scanner, style linter, runtime validator, universal design-system standard, or autonomous enforcement.

**Parent governance:** [design-token-intelligence-governance.md](design-token-intelligence-governance.md).  
**Layer model:** [token-semantic-layer-model.md](token-semantic-layer-model.md).  
**Forge checklist:** [`../../agents/mars-forge/design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).

---

## 1. Purpose

This taxonomy names common ways token systems drift while still appearing “organized.”

Token drift is not the existence of local tokens, overrides, or one-off values. Token drift is **uncontrolled token evolution**: values, aliases, overrides, scopes, states, and breakpoints change without preserving semantic design intent.

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical symptom |
|---------------|------------|-----------------|
| **Random token creation** | New tokens appear whenever a local value is needed. | Token map grows but semantics do not become clearer. |
| **Semantic alias confusion** | Token aliases imply roles that do not match actual use. | `primary`, `accent`, `muted`, or `surface` mean different things by context. |
| **Local override chaos** | Overrides replace governed token use as the normal path. | Components depend on local values, utility hacks, or scoped exceptions. |
| **Token inflation** | Too many tokens exist for small variations without distinct intent. | Multiple near-identical colors, gaps, radii, or shadows compete. |
| **Spacing-token fragmentation** | Spacing tokens multiply by section or component without cadence logic. | Page rhythm feels random despite tokenized gaps. |
| **Breakpoint-token divergence** | Responsive tokens change values but not intent. | Mobile survives mechanically while hierarchy, CTA pacing, or grouping collapse. |
| **Radius drift** | Radius tokens or values vary without role logic. | Buttons, cards, media, inputs, and badges look like unrelated systems. |
| **Shadow contamination** | Elevation tokens import unchartered depth, glow, or SaaS feel. | Cards float, proof feels decorative, or every object competes for foreground. |
| **Visual-token mismatch** | Token name suggests one role while the visual outcome reads as another. | `surface.subtle` looks dominant; `text.secondary` reads like disabled. |
| **Token spaghetti** | Alias chains and overrides become too tangled to audit. | Nobody can explain why a component has its final value. |
| **Semantic inconsistency** | Same semantic token supports incompatible roles. | `danger` used for urgent CTA, validation, sale badge, and destructive action. |
| **Design-system illusion** | Values are tokenized but intent is not coherent. | The build “uses tokens” yet hierarchy and visual language drift. |
| **Override leakage** | A local exception spreads into unrelated contexts. | A one-screen CTA, radius, shadow, or spacing pattern becomes global by copy/paste. |

---

## 3. High-Risk Families

### 3.1 Color Drift

- semantic color mismatch;
- text/disabled/muted confusion;
- CTA color escalation;
- success/error/warning contamination;
- surface token overload;
- focus ring color hidden by surface context.

### 3.2 Spacing Drift

- spacing-token fragmentation;
- cadence flattening through repeated gaps;
- local margin nudging;
- dense-section compression;
- mobile spacing collapse;
- tokenized but unauthored whitespace.

### 3.3 Radius Drift

- random local radius values;
- pill-everything escalation;
- imported SaaS softness;
- mixed radius without role logic;
- input/card/button/media radius mismatch.

### 3.4 Shadow and Elevation Drift

- shadow contamination;
- fake premium glow;
- depth escalation;
- card elevation copied from dashboard UI;
- shadow token used as a substitute for hierarchy.

### 3.5 Responsive Token Drift

- breakpoint-token divergence;
- desktop token compression without mobile intent;
- responsive alias names that hide hierarchy changes;
- CTA token behavior changing pressure on mobile;
- spacing and type tokens losing cadence continuity.

### 3.6 Behavioral and State Token Drift

- hover/focus/active state mismatch;
- disabled vs secondary confusion;
- loading and validation token drama;
- CTA state token inconsistency;
- accessibility-sensitive focus tokens hidden or fragmented.

---

## 4. Severity Read

| Severity | Meaning |
|----------|---------|
| **Low** | Local naming or value issue that does not yet damage intent. |
| **Medium** | Token drift affects a component family, section, breakpoint, or repeated state. |
| **High** | Drift damages hierarchy, responsive integrity, behavioral consistency, accessibility trust, or design-system readability. |
| **Blocking** | Token authority is unknowable, aliases conflict materially, or overrides prevent honest freeze without HITL. |

Severity is a human-supervised QA read, not automated scoring.

---

## 5. Reporting Vocabulary

Use these labels in `DESIGN TOKEN FINDINGS`:

- random token creation;
- semantic alias confusion;
- local override chaos;
- token inflation;
- spacing-token fragmentation;
- breakpoint-token divergence;
- radius drift;
- shadow contamination;
- visual-token mismatch;
- token spaghetti;
- semantic inconsistency;
- design-system illusion;
- override leakage;
- behavioral-token mismatch;
- design-system trust erosion.

---

## 6. Non-Drift Clarifications

The following are not automatically drift:

- a repeated raw value that has no reusable semantic role;
- a local token scoped to a real component or section context;
- a one-off override with source authority and a narrow boundary;
- a responsive token that changes value to preserve hierarchy and cadence;
- a state token that differs because the state meaning differs;
- a project-specific token model that does not match another project.

The issue is not difference. The issue is uncontrolled evolution that erodes intent and trust.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Token origin is unclear | Cannot tell whether a token is source, legacy, framework, or local invention. |
| Alias role is ambiguous | Cannot decide whether a token name matches its use. |
| Override scope is undocumented | Cannot judge leakage risk. |
| Breakpoint token meaning is absent | Cannot prove responsive integrity. |
| State token semantics are missing | Cannot prove behavioral consistency. |
| Token map is too large or flat to audit | Cannot distinguish system from token spaghetti. |

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial token drift taxonomy — random creation, alias confusion, override chaos, inflation, fragmentation, breakpoint divergence, radius/shadow drift, token spaghetti, design-system illusion, and override leakage. |

# Website Factory Universal Style Scale Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**

**Scope:** All Website Factory execution cases; Site-Wide Style Foundation; block specifications; SCSS production; visual QA; Gulp Frontend Agent prompts.

**Enforcement:** **DOCUMENTED MANDATORY GATE** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

**Registry:** [website-factory-cross-layer-artefact-registry-v1.md](website-factory-cross-layer-artefact-registry-v1.md) · [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

**Related laws:**

- [css-variable-first-law-v1.md](css-variable-first-law-v1.md) — corrected interpretation: reusable values from shared system; unique geometry may stay direct CSS
- [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) — foundation must declare compact scale before block SCSS
- [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md) — normalization maps evidence to scale roles, not selector names

---

## Core law

Website Factory must build a **compact reusable style scale**.

Tokens represent **system values** and **reusable component families**. Tokens must **not** mirror selectors, blocks, or individual properties.

A new block must **consume** the existing scale. It must **not** create its own spacing vocabulary.

---

## No Selector Token Law

A selector name is **not** a valid reason to create a token.

Header, Footer, Hero, section, and component names must **not** be copied into token names for ordinary spacing or radius values.

**Forbidden examples:**

```text
--header-padding-block-start
--footer-column-gap
--hero-button-radius
--faq-item-gap
```

**Allowed exceptions:**

- operator-approved unique container (e.g. `--container-hero`)
- true reusable component family (e.g. `--control-height-primary`, `--icon-size-small`)
- semantic theme role (color/text tokens)
- repeated technical system
- operator-approved exact geometry documented locally — **not** in `:root` under selector names

---

## No Alias Chain Law

Alias chains that only rename primitives for one block are **prohibited**.

**Forbidden:**

```scss
:root {
	--pad-y: 50px;
	--section-padding: var(--pad-y);
	--footer-padding: var(--section-padding);
}

.site-footer {
	padding-top: var(--footer-padding);
}
```

**Required:**

```scss
.site-footer {
	padding-top: var(--pad-y);
	padding-bottom: var(--pad-y);
}
```

**Alias permitted only when:**

- it creates a stable theme or component abstraction
- it is used by **more than one independent consumer**
- the value may change independently with documented owner and lifecycle

---

## Token admission gate

Before creating any new token, answer:

1. What **system role** does it represent?
2. Is this magnitude **reused** across the site?
3. Does a suitable token **already exist**?
4. Why can the existing scale **not** express the role?
5. Is this **primitive**, **shared component**, or **approved exception**?
6. How many **independent selectors** will consume it?
7. Can it change **independently** of an existing token?
8. Does the name contain a **selector/block/page** fragment?

If answers do not confirm necessity:

```text
NEW TOKEN — DENIED
USE EXISTING SCALE OR DIRECT EXACT VALUE
```

---

## Logical property rule

Website Factory production SCSS uses **physical CSS properties** for padding, margin, and positioning.

Logical properties are **prohibited by default**.

**Use:**

```text
padding-top / padding-right / padding-bottom / padding-left
margin-top / margin-right / margin-bottom / margin-left
top / right / bottom / left
```

**Do not use:**

```text
padding-block / padding-inline
padding-block-start / padding-block-end
padding-inline-start / padding-inline-end
margin-block / margin-inline
margin-block-start / margin-block-end
margin-inline-start / margin-inline-end
inset-block / inset-inline
```

**Exception:** separate operator task for RTL/writing modes with documented architectural reason — not default.

---

## Direct exact value rule (CSS Variable First Law alignment)

**Incorrect interpretation:** every production value must become a global variable.

**Correct interpretation:** every **reusable design value** must come from the shared system. A truly unique evidence-backed geometry value may remain **direct CSS** local to the owning block. It must **not** pollute `:root`.

| Situation | Action |
|-----------|--------|
| Repeated spacing/radius/type/color role | Global or shared component token |
| Component family (button height, icon size) | Shared component token |
| Unique art-directed geometry | Direct local value + review record |
| One-off selector alias | **Denied** |
| Magic number without evidence | **Denied** |

---

## Expected compact foundation pattern (spacing + radius)

Projects declare a **small primitive set** in Site-Wide Style Foundation, for example:

```scss
:root {
	--pad-x: 40px;
	--pad-y: 50px;
	--pad-gap: 30px;
	--pad-gap-line: 15px;
	--pad-gap-mini: 5px;
	--pad-box: 20px;

	--radius-full: 999px;
	--radius-main: 30px;
	--border-radius-form: 10px;
}
```

Project-specific values may differ when evidence requires — **names stay role-based**, not selector-based. Additional scale steps require **repeatability justification** (see Token admission gate).

---

## Production gates

| Gate | Document |
|------|----------|
| Style foundation | [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) |
| Pre-SCSS | [frontend-pre-scss-validation-checklist-v1.md](frontend-pre-scss-validation-checklist-v1.md) |
| Block spec | [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md) |
| SCSS review | [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md) |
| Visual QA | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) |

**On violation:**

```text
STYLE SCALE GATE — FAIL
TOKEN ADMISSION GATE — FAIL
SCSS AUTHORIZATION — DENIED
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — Universal Style Scale Law; No Selector Token Law; No Alias Chain Law; Logical Property Rule; CSS Variable First Law alignment; FP-0002 V6 pilot normalization |

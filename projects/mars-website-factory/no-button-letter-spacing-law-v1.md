# Website Factory No Button Letter Spacing Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**

**Scope:** All Website Factory execution cases; CSS variables; button styles; agent instructions; QA.

**Enforcement:** **DOCUMENTED MANDATORY GATE** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

**Registry:** [website-factory-cross-layer-artefact-registry-v1.md](website-factory-cross-layer-artefact-registry-v1.md)

---

## Core law

Do **not** define or use:

```text
--button-letter-spacing
```

Buttons inherit the **natural letter spacing** of the project font unless the operator explicitly approves a **project-specific exception** for a named control.

Even when approved, the value must **not** automatically become a global Factory variable.

---

## Prohibited patterns

```scss
:root {
	--button-letter-spacing: 0.02em;
}

.button {
	letter-spacing: var(--button-letter-spacing);
}
```

Do **not** replace removed token with `letter-spacing: 0` or another global token by default.

---

## Future rule

```text
Button letter-spacing is not part of the default Website Factory system.

Do not add button letter-spacing unless the operator explicitly requests
it for a specific project and approves the value.
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — FP-0002 V6 operator decision; global prohibition |

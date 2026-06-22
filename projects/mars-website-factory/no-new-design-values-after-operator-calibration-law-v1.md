# Website Factory No New Design Values After Operator Calibration Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Not:** automated value linter or token admission engine.

**Authority:** [operator-canonical-source-law-v1.md](operator-canonical-source-law-v1.md) · [css-variable-first-law-v1.md](css-variable-first-law-v1.md) · [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md)

---

## 1. Core law

```text
Once the operator manually calibrates the project source,
the frontend agent must reuse the established visual system.

The agent must not invent new dimensions, spacing, typography,
button geometry, colors, radii or decorative values.
```

---

## 2. Value freeze

When operator calibration is declared **ACTIVE**, the following are frozen until operator lift:

- containers;
- Header / Hero / Footer geometry;
- typography sizes and weights in use;
- colors;
- buttons;
- radii;
- spacing;
- icon sizes;
- social buttons;
- navigation distribution.

**FP-0002 V6:** `DESIGN VALUE FREEZE — ACTIVE`

---

## 3. Allowed exception classes

| Class | Requires |
|-------|----------|
| `FORM_REQUIRED` | Reason · value lookup · proof no existing value · minimal scope · operator or technical mandate · report |
| `MOBILE_REQUIRED` | Same |
| `ACCESSIBILITY_REQUIRED` | Same |
| `NEW_COMPONENT_REQUIRED` | Same |
| `OPERATOR_APPROVED` | Explicit operator instruction |

**Lookup order:** existing value in current `src` → existing project token → operator-approved exception → implementation.

---

## 4. No silent normalization

Do **not** change an existing value only because:

- it does not match a global scale;
- it looks unusual;
- an old review had a different number;
- another block uses a similar value;
- the agent prefers a “cleaner” number.

Current operator-authored result wins.

---

## 5. Gate

**Fail state:** `DESIGN VALUE FREEZE GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — post-calibration value freeze law |

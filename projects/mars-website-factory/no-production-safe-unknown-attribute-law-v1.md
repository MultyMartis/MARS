# Website Factory No Production SAFE UNKNOWN Attribute Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Not:** automated HTML linter.

**Authority:** [safe-unknown-boundary.md](safe-unknown-boundary.md) · [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)

---

## 1. Core law

```text
SAFE UNKNOWN is a governance/documentation state.
It must never be emitted as data-safe-unknown or another unknown marker
inside production HTML.
```

---

## 2. Forbidden in production DOM

- `data-safe-unknown="..."`
- `data-unknown="..."`
- governance markers as HTML attributes
- hidden inputs carrying unknown registry keys
- HTML comments documenting SAFE UNKNOWN for runtime

---

## 3. Allowed locations for SAFE UNKNOWN

- documentation;
- specifications;
- reviews;
- reports;
- registries;
- operator logs.

---

## 4. HTML quality gate

```text
[ ] data-safe-unknown absent in active src
[ ] data-safe-unknown absent in compiled HTML participating in build
[ ] Visible text uses semantic case (see semantic-text-casing-law-v1.md)
[ ] Production DOM contains no governance markers
```

**Fail state:** `HTML QUALITY GATE — FAIL`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — production DOM prohibition for SAFE UNKNOWN attributes |

# Website Factory Semantic Text Casing Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Not:** automated casing linter.

---

## 1. Core law

```text
Visible text in Website Factory HTML is written in normal semantic case.

Uppercase presentation belongs to CSS through text-transform.
Do not store presentation casing in HTML.
```

---

## 2. Examples

**Wrong:**

```html
<a class="btn">ЗАПИСАТЬСЯ</a>
```

**Right:**

```html
<a class="btn">Записаться</a>
```

```scss
.btn {
  text-transform: uppercase;
}
```

---

## 3. Exceptions (preserve in HTML)

- official acronyms (`PDF`, `SEO` when required);
- brand names officially written in caps;
- technical abbreviations;
- `aria-label` where caps are part of official name;
- text inside SVG assets.

---

## 4. Visual preservation rule

When migrating HTML casing:

- use existing selectors;
- add `text-transform: uppercase` only if the current design already requires uppercase presentation;
- do **not** introduce new `font-size`, `font-weight`, `letter-spacing`, or spacing values;
- do **not** reintroduce `--button-letter-spacing` ([no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md)).

---

## 5. Future content gate

```text
[ ] Visible HTML text uses semantic normal case
[ ] Uppercase appearance is controlled by CSS
[ ] Official acronyms and brand names are preserved
[ ] Button letter-spacing is not introduced
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — semantic HTML casing; CSS owns presentation uppercase |

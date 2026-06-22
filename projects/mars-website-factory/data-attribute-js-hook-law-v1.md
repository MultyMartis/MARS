# Website Factory Data Attribute JS Hook Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Not:** runtime selector validator.

**Authority:** [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) · [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)

---

## 1. Hook ownership

```text
CSS classes control appearance.
Data attributes control JavaScript behavior.
ARIA attributes control accessibility state.
```

---

## 2. Required pattern

```html
<button type="button" class="btn btn_dark" data-modal-open="callback">
  Заказать звонок
</button>
```

```js
const modalTriggers = document.querySelectorAll('[data-modal-open]');
```

---

## 3. Prohibited behavior selectors (default)

Do **not** bind behavior to:

- presentational BEM/CSS classes (`.btn_dark`, `.site-header__callback`);
- tag names (`header button`);
- DOM position (`.footer a:nth-child(2)`);
- text content;
- visual modifiers used as sole hook.

Reading a CSS class for **visual state** after selecting via `data-*` is allowed.

---

## 4. Naming

**Use:** `data-modal-open`, `data-menu-toggle`, `data-accordion`, `data-slider`, `data-form-submit`.

**Avoid:** `data-click`, `data-js`, `data-action-1`, `data-element`.

---

## 5. No unused hooks

Do not add functional `data-*` attributes before the behavior exists.

---

## 6. Gate

```text
[ ] JS hooks use data-* attributes
[ ] CSS/BEM classes are not behavior contracts
[ ] DOM hierarchy is not a behavior contract
[ ] ARIA state is synchronized by JS where applicable
[ ] No unused behavior hooks were added
```

**Fail state:** `JS HOOK GATE — FAIL`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — data-* behavior hook law |

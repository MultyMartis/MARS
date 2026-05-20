# Form foundation system v1 (v2 wave)

**Status:** documented HTML/SCSS/JS contract. **Not** a form framework or backend spec.

**Stack:** static HTML + SCSS + vanilla JS (jQuery-compatible where project already uses it).

---

## 1. HTML contract

Root:

```html
<form class="wf-form" data-module="form" data-form-id="lead-main" novalidate>
  <div class="wf-form__status" role="status" aria-live="polite" hidden></div>
  <!-- fields -->
  <button type="submit" class="wf-form__submit">Send</button>
</form>
```

Field group:

```html
<div class="wf-field" data-field="phone">
  <label class="wf-field__label" for="lead-phone">Phone</label>
  <input class="wf-field__control" id="lead-phone" name="phone" type="tel"
         autocomplete="tel" required aria-describedby="lead-phone-help lead-phone-error">
  <p class="wf-field__help" id="lead-phone-help">We call within 15 minutes.</p>
  <p class="wf-field__error" id="lead-phone-error" role="alert" hidden></p>
</div>
```

**Rules:**

- Every control has matching `label[for]` / `id`.
- Errors use `role="alert"`; help uses static `id` in `aria-describedby`.
- Required fields: `required` + visible indicator (text or `aria-required="true"`).
- Submit is `<button type="submit">`, not div click handlers.

---

## 2. State classes

| Class | Element | Meaning |
|-------|---------|---------|
| `.is-loading` | `form` | Submit in flight |
| `.is-success` | `form` | Server accepted (or client-only thank-you) |
| `.is-error` | `form` | Form-level failure |
| `.has-error` | `.wf-field` | Field invalid |
| `.is-disabled` | control | Non-interactive |

**Forbidden:** color-only error state; disabled submit without `.is-loading` during request.

---

## 3. Validation states

| Phase | Behavior |
|-------|----------|
| **Pristine** | No inline errors |
| **Touched blur** | Validate single field |
| **Submit** | Validate all; focus first error |
| **Server error** | Map `name` → field; form-level banner if unmapped |

Client validation: HTML5 constraints first; custom rules in module — keep messages in one template function.

---

## 4. AJAX lifecycle

```text
submit → preventDefault if invalid
      → lock (is-loading, disable submit)
      → fetch/XHR POST (project endpoint — SAFE UNKNOWN in MARS)
      → 2xx → is-success, optional redirect, fire analytics hook once
      → 4xx/5xx → is-error + field map
      → finally → unlock unless success keeps form hidden
```

**Idempotency:** ignore duplicate submit while `.is-loading`.

**Conversion-safe UX:** success message visible without layout jump — reserve min-height on `.wf-form__status`.

---

## 5. Inputmask posture

- Load mask plugin only if handoff requires masked fields.
- Init mask inside `initForm()`; destroy on `destroyForm()` (remove listeners, unwrap if plugin supports).
- Masked fields still expose raw `name` for server; validate **unmasked** value where rules apply.
- If mask library missing → SAFE UNKNOWN in REPORT; do not fake mask with `pattern` alone.

---

## 6. Accessibility baseline

- Focus first invalid field on submit fail.
- Error text copies to `aria-describedby` target; unhide error node (`hidden` removed, not `display:none` without accessible name).
- Do not remove focus outline without `:focus-visible` replacement.
- Autocomplete attributes on PII fields.

---

## 7. Anti-layout-shift

- Fixed min-height on error/help stack area OR single-line error slot.
- No injecting large images above fold on validation.
- Loading: spinner inside button or `.wf-form__submit` — do not resize button width (use fixed min-width).

---

## 8. Notification flow

| Channel | Use |
|---------|-----|
| Inline `role="status"` | Success copy, non-blocking |
| Inline `role="alert"` | Errors |
| Toast | Optional global — must not steal focus from modal |
| Modal thank-you | Only if handoff specifies; still announce via `aria-live` |

---

## 9. SCSS skeleton

```scss
.wf-form {
  &.is-loading .wf-form__submit { pointer-events: none; opacity: .7; }
}
.wf-field {
  &.has-error .wf-field__control { border-color: var(--color-error, #{$color-error}); }
  .wf-field__error[hidden] { display: none; }
}
```

Colors from [token-system-v2.md](token-system-v2.md) semantic tokens.

---

## 10. JS module sketch (`data-module="form"`)

```javascript
// Contract only — implement in workspace js/core/form.js
function initForm(root) {
  if (root.__wfFormBound) return;
  root.__wfFormBound = true;
  root.addEventListener('submit', onSubmit);
}
function destroyForm(root) {
  root.removeEventListener('submit', onSubmit);
  delete root.__wfFormBound;
}
```

Wire through [js-lifecycle-system-v2.md](js-lifecycle-system-v2.md).

*Wave 2 — form foundation.*

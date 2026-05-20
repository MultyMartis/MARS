# Modal & overlay foundation system v1 (v2 wave)

**Status:** documented lifecycle + layering. **Not** a UI library.

**Distinction:** **overlay** = readability/visual layer inside a section; **modal** = blocking dialog with focus management.

---

## 1. Layer ownership

| Layer | Owner | z-index source |
|-------|--------|----------------|
| Atmosphere / hero media | Section partial | below content |
| Readability overlay | Section SCSS | `$z-overlay-readability` (local stacking context) |
| Sticky header / CTA | Layout partial | `$z-sticky-cta`, `$z-header` |
| Modal backdrop + panel | `js/core/modal.js` | `$z-modal-backdrop`, `$z-modal` |
| Toast | Optional core | `$z-toast` |

**Rule:** modals never set ad hoc z-index; use `_layers.scss` tokens only.

---

## 2. HTML contract (modal)

```html
<div class="wf-modal" data-module="modal" id="modal-callback" hidden aria-hidden="true">
  <div class="wf-modal__backdrop" data-modal-close tabindex="-1"></div>
  <div class="wf-modal__dialog" role="dialog" aria-modal="true" aria-labelledby="modal-callback-title">
    <button type="button" class="wf-modal__close" data-modal-close aria-label="Close"></button>
    <h2 id="modal-callback-title">Callback</h2>
    <!-- content -->
  </div>
</div>
```

Triggers: `<button type="button" data-modal-open="modal-callback">` — not `<a href="#">`.

---

## 3. Lifecycle

```text
closed (hidden, aria-hidden=true)
  → open: remove hidden, aria-hidden=false, body lock, focus dialog, trap focus
  → close: restore focus to trigger, unlock body, hidden=true
  → destroy: remove listeners, force close if open
```

**Events (namespaced):** `wf:modal:open`, `wf:modal:close` on `document` — optional for analytics.

---

## 4. Open / close system

| Action | Behavior |
|--------|----------|
| `data-modal-open` | Open target by id; store `document.activeElement` |
| `data-modal-close` | Close nearest modal |
| ESC | Close topmost modal only |
| Backdrop click | Close if handoff allows (default: yes) |

**Animation restraint:** fade backdrop + translateY(8px) max 250ms — see interaction doc.

---

## 5. Focus trap direction

- On open: focus first focusable in dialog (prefer close button or first field).
- Tab cycles within dialog only (`focusin` listener).
- On close: return focus to trigger element if still in DOM.

**jQuery-compatible:** implement trap in vanilla; wrap with `$(document).on` only if project standard requires — same semantics.

---

## 6. Body lock

```scss
body.is-modal-open { overflow: hidden; }
```

- Compensate scrollbar width on desktop (`padding-right: var(--scrollbar-width)`) to prevent layout shift.
- iOS: avoid nested `position: fixed` on body children — modal panel scrolls internally (`max-height: 90vh; overflow: auto`).

---

## 7. Nested modal posture

**Default:** avoid nesting. If required:

- Raise z-index by +10 per level using CSS variable `--modal-level`.
- ESC closes only top modal.
- Only one body lock counter (`lockCount++/--`).

---

## 8. Mobile behavior

- Full-width dialog below `$bp-md` with safe-area padding.
- Close target min 44×44px.
- Do not open second modal from keyboard-trapped context without closing parent.

---

## 9. Overlay survivability (non-modal)

Hero readability overlay:

- Lives inside section wrapper; dies with section replace.
- Must not intercept clicks meant for CTA (`pointer-events: none` on gradient layer).
- Replacing hero: verify contrast ratio on mobile still passes spot check (human QA — no auto claim).

**Section interaction safety:** opening modal from hero CTA must not leave hero video playing audio under backdrop — pause media in `open` handler when `data-modal-pause-media` present.

---

## 10. Anti-patterns

- Multiple independent modal scripts per page.
- `href="#"` openers.
- Focus left on `body` after close.
- Modal inside partial that duplicates global `#modal` ids.
- Sticky CTA z-index above modal.

*Wave 2 — modal/overlay foundation.*

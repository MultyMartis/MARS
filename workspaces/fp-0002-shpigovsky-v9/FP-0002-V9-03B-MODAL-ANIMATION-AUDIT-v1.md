# FP-0002 V9-03B — Modal Animation Audit v1

**Phase:** V9-03B  
**Implementation:** `src/partials/components/modal-consultation.html`, `src/scss/style.scss`, `src/js/main.js` (`initFp0002ModalAndLeadForms`)

## Previous lifecycle (V9-03A)

- Open: remove `[hidden]`, set `data-modal-state="open"` immediately
- Close: remove open state, set `[hidden]` immediately — **no closing transition**
- Overlay: static rgba background, no fade
- Dialog: open transform present but close was abrupt

## Corrected lifecycle

### Open (~0.3s)

1. Remove `[hidden]`, `aria-hidden="false"`, body `data-modal-state="open"`
2. Double `requestAnimationFrame` then `data-modal-state="open"` (skipped when reduced motion)
3. Overlay: opacity 0 → 1
4. Dialog: opacity 0 → 1, `translateY(8px) scale(0.98)` → `translateY(0) scale(1)`
5. Focus enters dialog promptly after open state

### Close (~0.3s)

1. User trigger (close button, Escape, overlay click)
2. `data-modal-state="closing"` on modal; body `data-modal-state="closing"` (scroll lock retained)
3. Overlay + dialog animate out; modal wrapper opacity → 0
4. On `transitionend` (opacity/transform on dialog) **or** fallback timeout `MODAL_TRANSITION_MS + 80` (380ms)
5. Apply `[hidden]`, remove states, restore focus, unlock scroll

## Accessibility preserved

- Escape, overlay click, close button
- Focus trap while open/closing
- `prefers-reduced-motion`: immediate state change, no animation wait

## Form mode

`STATIC_DEMO_NO_BACKEND` — unchanged

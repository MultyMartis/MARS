# FP-0002 V9-03B — Modal Form Validation v1

**Status:** Automated structure PASS — **operator visual confirmation required**

## Tests

| Test | Automated | Operator |
|------|-----------|----------|
| Open from header | JS lifecycle present | Required |
| Open from page CTA | Bindings unchanged | Required |
| Overlay fade | CSS + closing state | Required |
| Dialog/form fade | CSS transform/opacity | Required |
| Close button | Handler preserved | Required |
| Escape | Handler preserved | Required |
| Overlay click | Handler preserved | Required |
| Closing animation before hidden | `data-modal-state="closing"` + timeout fallback | Required |
| Focus restoration | `finalizeModalClose` | Required |
| Scroll lock open/close | body `data-modal-state` open/closing | Required |
| Rapid open/close | Fallback timeout prevents stale state | Spot-check |
| Mobile 380px | Not automated | Required |
| Reduced motion | Immediate close path | Required |
| Console errors | HTTP 200 all routes | Required |

## Form submission

`STATIC_DEMO_NO_BACKEND` — unchanged

# FP-0002 V9-06D7A Modal / CTA Boundary v1

**Date:** 2026-07-04

## Implemented in D7-A

| Item | Status |
|------|--------|
| Modal markup (`modal-consultation`) | Yes — `template-parts/layout/global-consultation-modal.php` |
| Open/close JS | Yes — via `v9-shell.js` modal system |
| CTA triggers in header/footer/offcanvas | Yes — `data-modal-open="consultation"` |
| Form fields visible | Yes — static markup only |

## Not implemented / deferred

| Item | Status |
|------|--------|
| Form submission | Deferred — submit prevented in D7-A |
| AJAX / fetch endpoint | Deferred — no endpoint configured |
| reCAPTCHA | Deferred |
| Inputmask phone mask | Deferred |
| Plugin forms module | Deferred — plugin source unchanged |

## Options binding

CTA button labels read `default_button_label` / `default_secondary_button_label` from site options when present; i18n fallbacks otherwise.

## Result

COMPLETE (markup + safe open/close boundary)

# FP-0002 V9-03B — Gallery Animation Audit v1

**Library:** `@fancyapps/ui` ^5.0.36 (Fancybox 5)  
**Path:** `node_modules/@fancyapps/ui` → `dist/assets/vendor/fancybox/`

## Entry points

| Group | Pages / sections |
|-------|------------------|
| `comfort` | Home comfort gallery |
| `o-centre-infrastructure` | O-Centre infrastructure sliders |
| `o-centre-infrastructure-g5` | O-Centre comfort-gallery component |
| `services-comfort-v2` | Service comfort galleries (bound in V9-03B) |
| `home-videos` | Home video lightbox |

**Blog inline Fancybox:** not present in V9 source — no change applied.

## Previous behavior

Fancybox bound with toolbar/carousel options only; default zoom-style entrance could feel abrupt; no explicit fade timing tokens.

## Correction (V9-03B)

**JS** (`initComfortFancybox`, `initHomeVideosFancybox`):

```javascript
animated: true,
showClass: 'f-fadeIn',
hideClass: 'f-fadeOut',
Carousel: { transition: 'fade', infinite: false }
```

**SCSS:**

```scss
.fancybox__container.is-animated {
  --f-backdrop-enter-duration: var(--motion-base);
  --f-backdrop-exit-duration: var(--motion-base);
  --f-transition-duration: var(--motion-base);
}
```

Reduced motion: durations → `0.01ms`, animations disabled in SCSS block.

## Constraints honored

- No library replacement
- No image order/content change
- No aggressive zoom configuration added

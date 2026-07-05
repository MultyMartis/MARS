# FP-0002 V9-06D9G FAQ Micro Repair v1

**Date:** 2026-07-05  
**Task:** V9-06D9-G Micro Visual Repair — FAQ heading / id / aria contract

## Defect (from D9-F)

D9-D static V9 transplant copied comfort-section heading contract into FAQ:

| Attribute | Wrong (D9-D typo) | Correct (static V9) |
|-----------|-------------------|---------------------|
| `aria-labelledby` | `comfort-heading` | `faq-heading` |
| heading `id` | `comfort-heading` | `faq-heading` |
| heading text | Комфорт, приватность, забота | Нас часто спрашивают |

Side effect: duplicate `id="comfort-heading"` on comfort + FAQ sections.

## Repair

**File:** `template-parts/home/faq.php` only

```diff
-<section data-reveal class="faq"  aria-labelledby="comfort-heading">
+<section data-reveal class="faq"  aria-labelledby="faq-heading">
   <div class="container">
-    <h2 class="faq__heading" id="comfort-heading">Комфорт, приватность, забота</h2>
+    <h2 class="faq__heading" id="faq-heading">Нас часто спрашивают</h2>
```

No FAQ accordion markup, comfort section, CSS, JS, or ACF changes.

## Runtime delivery

Bounded copy: 1 file to active runtime theme. SHA256 verified match.

## Post-repair validation

All D9-F Home checks re-verified PASS except FAQ defect (now fixed). Comfort section retains sole `comfort-heading`. ACF editability gate unblocked.

## Evidence

`validation/v9-06d9g-micro-visual-repair-faq-heading/`

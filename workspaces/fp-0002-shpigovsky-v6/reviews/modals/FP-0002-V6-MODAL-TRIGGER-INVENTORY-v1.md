# FP-0002 V6 Modal Trigger Inventory v1

**Date:** 2026-06-23  
**Page:** `src/pages/index.html` (full home)

| Order | Section | Current element | Current text | Current href/action | Conversion CTA | Modal required | Modal variant | Connected source ID |
| ----: | ------- | --------------- | ------------ | ------------------- | -------------: | -------------: | ------------- | ------------------- |
| 1 | Header desktop | `button.btn` | Заказать звонок | `data-modal-open` | YES | YES | callback | `header` |
| 2 | Mobile offcanvas | `button.btn.offcanvas__cta` | Заказать звонок | `data-modal-open` | YES | YES | callback | `mobile-header` |
| 3 | Hero | `button.hero__button` | Записаться на консультацию | `data-modal-open` | YES | YES | consultation | `hero` |
| 4 | Founder quote | `button.home-founder-quote__cta` | Записаться на консультацию | `data-modal-open` | YES | YES | consultation | `founder-quote` |
| 5 | Rehabilitation requirements | `button.home-rehabilitation-requirements__cta-button` | Записаться | `data-modal-open` | YES | YES | appointment | `rehabilitation` |
| 6 | Genotyping | `button.home-genotyping__cta` | Записаться на консультацию | `data-modal-open` | YES | YES | consultation | `genotyping` |
| 7 | Footer | `button.btn` | Заказать звонок | `data-modal-open` | YES | YES | callback | `footer-callback` |
| 8 | Footer | `button.btn.btn_dark` | Записаться | `data-modal-open` | YES | YES | consultation | `footer-appointment` |
| 9 | Final form | `form.home-final-form__form` | Записаться на консультацию | inline submit | YES | NO | final | `final-section` (hidden) |

## Preserved non-conversion controls

| Section | Element | Reason |
|---------|---------|--------|
| Header / offcanvas / footer | Nav links `href="#"` | Navigation placeholders |
| Section heads | «подробнее» links | Informational, not conversion modal |
| Rehabilitation | `tel:+79251836464` | Phone link |
| Footer / header | Messenger placeholders | Not modal conversion |
| Comfort gallery | Fancybox `data-fancybox` | Media lightbox |
| Videos | Demo blocks | No live video URLs |

**Total conversion CTA candidates:** 9  
**Modal triggers connected:** 8  
**Final inline form:** 1 (unified `data-lead-form`, not modal trigger)

# FORMS / MAIL FINAL INVENTORY + SUPPRESSION

**Wave:** P17-FU02  
**Send test:** **NOT DONE** (forbidden)  
**SMTP config:** **NOT DONE**  
**Token:** `FORMS READY FOR POST-DNS SMTP CONFIGURATION`

## Inventory

| Form | Location | Handler | Recipient | From / Reply-To | Suppression | SMTP later |
|------|----------|---------|-----------|-----------------|-------------|------------|
| Modal «Записаться на консультацию» | header/CTA `data-modal="consultation"` | `ConsultationHandler` AJAX `fp02_lead_submit` (`admin-ajax.php`) | Constant `client.leads@polygon-ws.ru` (not public; not mailed now) | N/A (no send) | MU `pre_wp_mail` → false; handler does not call `wp_mail` | Same handler + wp_mail/SMTP |
| Final form | `template-parts/components/final-form.php` `data-lead-form` | same AJAX handler | same | N/A | same | same |
| Legacy `admin_post_shpigovsky_consultation` | old POST | no-op redirect | none | none | n/a | keep no-op |
| Contact Form 7 / other plugins | none active | — | — | — | — | — |

No PHP `mail()` in theme / shpigovsky-core / MU (verified by source grep). PHPMailer `phpmailer_init` has no custom filter.

Frontend UX: success copy is acceptance without claiming email delivery: «Заявка принята. Мы свяжемся с вами по указанному телефону.»

## Mail suppression owner

**File:** `wp-content/mu-plugins/fp02-pre-cutover-mail-suppression.php`  
**Filter:** `pre_wp_mail` priority 1 → `false`  
**Keep until:** P18 PHASE B (after DNS + SSL + final domain smoke)

**Exact disable instruction:** rename or delete that MU file on Beget; confirm `has_filter('pre_wp_mail')` is false; configure SMTP; form QA; do not leave PHP `mail()` as fallback.

**Token:** suppression verified; frontend form cannot accidentally deliver via PHP mail; UX is non-fatal.

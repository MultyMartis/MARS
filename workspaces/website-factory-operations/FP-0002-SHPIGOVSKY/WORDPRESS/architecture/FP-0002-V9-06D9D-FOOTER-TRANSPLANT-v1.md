# FP-0002 V9-06D9D Footer Transplant v1

**Date:** 2026-07-05

## Summary

Rebuilt global footer from static V9 `footer.html`:

- Static phone/email/address/schedule fallbacks when options empty
- Static social icons (Telegram, WhatsApp, Max, YouTube placeholder `#`)
- Privacy block (`site-footer__copyr-privacy`)
- Credit line (`Разработка и продвижение: Overseo`)
- Scroll-to-top component
- Nav columns use existing `wp_nav_menu` with V9 fallback items (no menu mutation)

## Evidence

`validation/v9-06d9d-home-main-footer-static-v9-transplant/footer-transplant-result.json`

# WP Forge Social / Contact Module Spec v1

**Class:** B (module) + A (single SoT rule)  
**Maturity:** PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Reference:** FP-0002 P13 SocialPlatformsOptions

---

## Registry architecture

```text
platform type → canonical label + icon
URL
header visibility
footer visibility
(+ mobile if needed)
```

Supported types should include Telegram, WhatsApp, MAX, YouTube, plus a documented extension slot.

**TYPE determines label/icon.** Do not use free-text labels for known platforms.  
**Missing URL or both visibilities off:** do not render empty controls.

Consumers: header, floating header, offcanvas, footer, contacts — **read the same helper**.

## Extraction

**B** after icon SVG set parameterization.

---

*Spec v1.*

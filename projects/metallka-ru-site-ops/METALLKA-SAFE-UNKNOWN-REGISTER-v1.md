# METALLKA — SAFE UNKNOWN Register v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** UPDATED after Phase 2B discovery  
**Date:** 2026-07-26  
**Rule:** Do **not** fill unknowns from analogy. Historical rows retained.

**Production discovery:** **PERFORMED** (Gate A / Phase 2B) — statuses updated below.

---

## Register

| ID | Unknown | Status | Notes |
|----|---------|--------|-------|
| SU-01 | Hosting provider | **RESOLVED** | Beget |
| SU-02 | Docroot | **RESOLVED** | `/home/[REDACTED]/[REDACTED]/metallka.ru/public_html` |
| SU-03 | PHP version | **RESOLVED** | HTTP **8.3.20**; WP-CLI 7.4.33; shell default 5.6.40 |
| SU-04 | WordPress version | **RESOLVED** | **7.0.2** |
| SU-05 | Multisite status | **RESOLVED** | NO |
| SU-06 | DB prefix | **RESOLVED** | `wp_` |
| SU-07 | Permalink model | **RESOLVED** | `/%postname%/` |
| SU-08 | The7 exact version | **RESOLVED** | **11.6.0.1** |
| SU-09 | Child theme name / version | **RESOLVED** | `dt-the7-child` / `the7dtchild` **1.0.0** |
| SU-10 | Parent / child modifications | **PARTIAL** | Child overrides mapped; parent treated as vendor (no proven site-specific parent forks) |
| SU-11 | WPBakery version | **RESOLVED** | **6.10.0** |
| SU-12 | Actual WPBakery storage patterns | **RESOLVED** | Classic shortcodes in `post_content` + `_wpb_vc_js_status` |
| SU-13 | `vc_raw_html` presence | **RESOLVED** | YES on home/contacts/services/requisites; NO on about/legal text pages |
| SU-14 | Custom shortcodes | **PARTIAL** | CF7, Shortcoder, `dt_*`, Ultimate/RevSlider; no child `add_shortcode` |
| SU-15 | Active / inactive plugins | **RESOLVED** | Full inventory captured |
| SU-16 | MU plugins | **RESOLVED** | None |
| SU-17 | Drop-ins | **RESOLVED** | No advanced/object cache drop-ins |
| SU-18 | ACF | **RESOLVED** | **NOT PRESENT** |
| SU-19 | CPTs | **PARTIAL** | Core + CF7 + Popup Maker + Shortcoder + Rank Math types; no custom product CPT found |
| SU-20 | Page templates | **RESOLVED** | Inspected pages use `default` |
| SU-21 | The7 Theme Options ownership | **RESOLVED** | Option `the7dtchild` (956 keys) + generated CSS |
| SU-22 | Header / footer ownership | **RESOLVED** | Header: The7 options + menus; Footer: The7 + child `footer.php` / `sidebar-footer.php` |
| SU-23 | Menu model | **RESOLVED** | primary + mobile locations mapped |
| SU-24 | Forms | **RESOLVED** | CF7 + honeypot + CFDB7 |
| SU-25 | SMTP | **PARTIAL** | No SMTP plugin; transport likely hosting PHP mail |
| SU-26 | CRM / webhooks | **PARTIAL** | None evidenced in plugins; not fully ruled out inside CF7 |
| SU-27 | Custom CSS | **RESOLVED** | Child `style.css` + The7 generated CSS; WP custom CSS empty |
| SU-28 | Custom JS | **RESOLVED** | Child masked input JS; Shortcoder mail script |
| SU-29 | Custom PHP | **RESOLVED** | Child functions/footer/sidebar-footer; `css-versioning` plugin |
| SU-30 | Cache layers | **RESOLVED** | Clearfy + leftover FVM/wmac dirs; no Redis/advanced-cache |
| SU-31 | CDN / WAF / ModSecurity | **PARTIAL** | No CDN/CF; WAF/ModSecurity not proven |
| SU-32 | REST restrictions | **PARTIAL** | Public REST open; Clearfy not clearly disabling REST; CORS header list lacks `X-WPilot-Token` |
| SU-33 | `X-WPilot-Token` forwarding | **PARTIAL** | Likely OK server-side; CORS browser caveat |
| SU-34 | Filesystem ownership | **RESOLVED** | Account-owned docroot; sanitized path documented |
| SU-35 | Backup mechanism | **RESOLVED** | Beget hosting-native (operator + intake) |
| SU-36 | Restore procedure | **PARTIAL** | Available per operator; panel UI not inspected |
| SU-37 | Staging availability | **RESOLVED** | NONE |
| SU-38 | Source / Git authority | **RESOLVED** | No external source; no `.git`; provisional production authority |
| SU-39 | Local mirror need | **RESOLVED** | Decision **DEFER** |
| SU-40 | The7 / WPBakery licenses | **STILL UNKNOWN** | Purchase/license validity not audited (options include purchase fields — values not recorded) |
| SU-41 | Current WPilot presence | **RESOLVED** | ABSENT |
| SU-42 | Duplicate / ghost WPilot folders | **RESOLVED** | NONE |
| SU-43 | Safe first production object | **RESOLVED** | Page **52** About — single `vc_column_text` (recommended) |
| SU-44 | Compatibility with RC6 | **RESOLVED** | **CONDITIONALLY COMPATIBLE** |

---

## Summary

| Metric | Value |
|--------|-------|
| Historical items | **44** |
| **RESOLVED** | **33** |
| **PARTIAL** | **10** |
| **STILL UNKNOWN** | **1** (SU-40) |
| Analogy fills | **0** |

---

*SAFE UNKNOWN Register v1 · updated Phase 2B.*

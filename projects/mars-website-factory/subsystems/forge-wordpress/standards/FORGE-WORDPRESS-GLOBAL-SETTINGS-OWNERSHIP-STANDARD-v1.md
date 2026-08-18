# Forge WordPress — Global Settings Ownership Standard v1

**ID:** FW-S-30  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Extends:** [FW-S-11 Site Settings](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md)  
**Companion:** [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

```text
GLOBAL BUSINESS VALUES HAVE ONE SOURCE OF TRUTH AND MANY FRONTEND CONSUMERS.
```

This document is the **ownership and fallback** layer. FW-S-11 remains the recommended Site Settings schema.

---

## 1. What belongs in Site Settings

**GOOD:** organization identity; phones; email; address; social/messenger URLs; reusable global CTA labels/settings; analytics IDs; verification values; global footer data; global header controls; SEO/integration configuration; breadcrumb visibility if site-wide.

**BAD:** content belonging to one page; records that need their own lifecycle; huge lists that should be CPT; repeated page-specific sections; per-template phone copies.

Contacts **page** may add page-owned maps, extra location prose, or layout — not a second primary phone.

---

## 2. Ownership map (required per site)

Every global-ish value:

| Column | Meaning |
|--------|---------|
| FIELD / ENTITY | Business name (Телефон) |
| STORAGE OWNER | Options group + field name |
| EDITOR | Who may change it |
| FRONTEND CONSUMERS | header, offcanvas, floating header, footer, contacts, forms |
| FALLBACK | hide / programmatic / none |
| VALIDATION | type rules |

Template: [FIELD-OWNERSHIP-MAP](../templates/FORGE-WORDPRESS-FIELD-OWNERSHIP-MAP-TEMPLATE-v1.md) · [SITE-SETTINGS-MAP](../templates/FORGE-WORDPRESS-SITE-SETTINGS-MAP-TEMPLATE-v1.md).

---

## 3. Consumer rule

Chrome partials **consume helpers**, they do not own fields.

```text
Site Settings
  → get_phone_primary()
    → header
    → mobile nav
    → floating header
    → footer
    → contacts
    → CTA phone hint
```

Hardcoded social URLs in templates are AP-007. Independent per-surface contact settings are AP-008 / AP-CMS-004.

---

## 4. Fallback hierarchy for globals

| Situation | Policy |
|-----------|--------|
| Phone empty | Do not render `tel:` control |
| Social URL empty or hidden | Do not render icon |
| Page CTA label empty | Safe global CTA label if designed as fallback |
| Global CTA still empty | Hide CTA |
| Analytics ID empty | No tag |
| Verification empty | No tag |
| Advanced code empty | No output |

Never: demo phone, demo social, Lorem in chrome.

---

## 5. Global reusable content vs Options bloat

| Content | Storage |
|---------|---------|
| Identical CTA defaults on many templates | Options (or a dedicated Options subpage) |
| Same body copied onto 8 pages by hand | Fail — Options or reusable instance |
| Growing list of people/services | CPT, not Options |
| Header/footer chrome strings that marketing changes | Options |
| Design tokens, motion constants | Code |

If an Options screen becomes a dumping ground for page sections, split: Site Settings (globals) vs page ACF vs CPT.

---

## 6. Advanced settings boundary

Raw head/body/footer HTML, verification, integration IDs:

- separate tab, clearly marked dangerous;  
- permission-limited (Administrator / technical operator);  
- sanitized/capability-reviewed;  
- **not** mixed with ordinary content fields (phone next to GTM next to “Hero title”).

---

## 7. Editor instruction principle

Admin help should say **where the value appears**:

- «Показывается в шапке и подвале»  
- «Используется на карточке специалиста»  
- «Текст для SEO, на странице не отображается»

If the editor cannot predict the frontend from the field help, the field is unfinished.

---

## 8. SMTP technical sender identity

The technical website sender mailbox defaults to `noreply@<site-domain>` ([FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §5). This is a **hosting identity**, not a Site Settings password field. Do not store SMTP passwords in Git.

---

*FW-S-30 v1.1 — one owner, many consumers, empty-safe chrome.*

# Forge WordPress — Site Settings Standard v1

**ID:** FW-S-11  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Class:** A (SoT architecture) / E (Admin)  
**Companion:** [FW-S-30 Global Settings Ownership](FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) (ownership maps, fallbacks, consumer helpers) · [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

---

## 1. Rule

```text
ONE ADMIN SOURCE OF TRUTH
→ header
→ floating header
→ mobile offcanvas
→ footer
→ contacts page consumers
```

Do not give each template its own phone/social fields. Hardcoded social URLs in templates are AP-007. Independent per-surface contact settings are AP-008.

---

## 2. Recommended schema (new sites)

Names are roles, not ACF keys. Localize labels.

| # | Section | Responsibility | Frontend consumers | Visibility flags | Empty behavior |
|---|---------|----------------|--------------------|------------------|----------------|
| 1 | **Общие** | Site name extras, legal short, logo refs if not Customizer | chrome | — | hide optional extras |
| 2 | **Контакты** | Phones, email, address, map embeds as **data** | header, footer, contacts | per-item show | do not render empty tel/mail |
| 3 | **Соцсети и мессенджеры** | Platform **type** + URL | header/footer/mobile | header / footer | no empty icons |
| 4 | **SEO и интеграции** | Default title pattern, verification, analytics IDs | `wp_head` | — | empty → no tag |
| 5 | **Sitemap** | Enable, public types, Admin links to `wp-sitemap.xml` | core sitemaps | — | indexing still gated elsewhere |
| 6 | **Умный поиск** | Groups, min chars, limits (if module on) | search JS | — | code defaults if unset |
| 7 | **Аналитика / verification** | Metrica, GA/GTM, Webmaster, Search Console | head | — | empty → no output |
| 8 | **Advanced code** | Extra head / body / footer HTML | theme hooks | Admin-only | capability-gated; no editor role |
| 9 | **System status** | **Not** a settings tab — Dashboard widget | WP Dashboard | Admin | [ADMIN-UX](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) |
| 10 | **Почта и формы** | SMTP, sender `noreply@`, recipients, Metrika **goal** only, lead retention | mail transport + forms | Admin | not chrome; password write-only; [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) |

Merge 4+7 if the project is small. Keep **Advanced code** visually last and dangerous.

---

## 3. Social / messengers (optional module, standard shape)

| Field | Rule |
|-------|------|
| Platform type | Registry: Telegram, WhatsApp, MAX, YouTube, + project extension |
| URL | Validated; type-specific (wa.me vs t.me) as project rules |
| Header visibility | boolean |
| Footer visibility | boolean |
| Icon / label | Derived from **type**, not free text |
| Missing URL or hidden | Do not output a control |

See [SOCIAL-CONTACT-MODULE-SPEC](FORGE-WORDPRESS-SOCIAL-CONTACT-MODULE-SPEC-v1.md).

---

## 4. Validation and defaults

- Validate URLs, phones, emails at save.
- Defaults: empty integrations; indexing closed until launch SOP.
- Do **not** duplicate: Customizer phone, widget phone, ACF-on-every-page phone.
- Contacts **page** may add locations/maps that are page-owned; site-wide phones stay in options.

---

## 5. Storage

ACF options page (or equivalent) in the functionality plugin. Values = **DB content authority**. Field group JSON = **code authority**.

---

*FW-S-11 v1.*

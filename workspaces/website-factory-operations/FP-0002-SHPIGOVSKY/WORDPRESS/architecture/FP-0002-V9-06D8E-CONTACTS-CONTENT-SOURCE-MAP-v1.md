# FP-0002 V9-06D8-E — Contacts Content Source Map v1

**V9 primary:** `src/partials/sections/contacts-map-body.html`, `contacts-rehabilitation-steps.html`

| Section | V9 reference | D8-A option | Target | Seed |
|---------|--------------|-------------|--------|------|
| Intro | `contacts-body__intro` | — | `contacts_form_intro` | YES |
| Phone row | tel link | `phone_primary` | — (template) | NO |
| Messengers | `href="#"` icons | `social_links` | `contacts_messengers` | NO |
| Location MO | location article 1 | — | `contacts_blocks[0]` | YES |
| Location Moscow | location article 2 | — | `contacts_address`, `contacts_blocks[1]` | YES |
| Hours/email | detail rows | `opening_hours`, `site_email` | — (template) | NO |
| Map | static PNG | `map_link` | `contacts_map_url` | NO |
| Rehab steps | static section | — | — (template fallback) | NO |
| CTA band | program-cta-band | options | — (template) | NO |

Evidence: `validation/v9-06d8e-contacts-content-seed/contacts-content-source-map.json`

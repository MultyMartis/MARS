# Social / messenger consumer map (PROD-P13)

Canonical Admin owner: `Настройки сайта → Social networks and messengers` (`social_platforms`).

Legacy `social_links` retained in DB; hidden in Admin; frontend fallback only if new field empty.

## Olya production URLs preserved

- Telegram `https://t.me/Spigovsky_house` (header+footer)
- WhatsApp `https://wa.me/89251836464` (header+footer) — URL stored exactly; not rewritten

## Contacts page rule

Contacts shows every configured platform that has a URL. Header/footer flags do **not** hide Contacts.

| Setting | Header | Floating header | Mobile/offcanvas | Footer | Contacts |
|---|---|---|---|---|---|
| Telegram URL + show_header/show_footer | yes | yes (`context=header`) | yes (`show_header`) | yes | yes |
| WhatsApp URL + show_header/show_footer | yes | yes | yes | yes | yes |
| Missing URL / unknown type | no | no | no | no | no |

Consumers:

- `template-parts/layout/header.php` → `messenger-links` context `header` / `mobile-header`
- `template-parts/layout/floating-header.php` → context `header`
- `template-parts/navigation/offcanvas.php` → context `offcanvas` (header flags)
- `template-parts/navigation/footer-social.php` → footer flags
- `inc/contacts-helpers.php` → `shpigovsky_get_contacts_messenger_rows()` surface `contacts`

Footer broken-button root cause: legacy label «What's up» did not map to `whatsapp.svg` and fell through to YouTube FA. Typed `whatsapp` now loads `whatsapp.svg`. HTTP QA: `whatsapp.svg` present, `fa-youtube` count 0 on home.

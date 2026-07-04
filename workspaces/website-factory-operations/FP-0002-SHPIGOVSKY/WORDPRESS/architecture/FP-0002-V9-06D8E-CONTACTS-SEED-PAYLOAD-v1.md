# FP-0002 V9-06D8-E — Contacts Seed Payload v1

**Target:** Page #20 only

## Writable fields

1. **`contacts_form_intro`** — V9 intro paragraph (replaces D4 minimal placeholder).
2. **`contacts_address`** — `Москва, ул. Ленина, 3` (V9 location 2; D7-E location-two fallback).
3. **`contacts_blocks`** — 2 rows:
   - Центр профилактики… / MO Katuar address
   - Лечение зависимостей Москва / Moscow Lenina 3

## Skipped

- `contacts_map_url`, `contacts_messengers` — operator URLs required
- `contacts_phones` — D8-A canonical

Evidence: `validation/v9-06d8e-contacts-content-seed/proposed-contacts-seed-payload.json`

# Form mailer implementation — v1

## Endpoint

| Item | Value |
|------|--------|
| Path (source) | `backend/send-lead.php` |
| Path (dist) | `dist/backend/send-lead.php` |
| Method | `POST` only |
| Response | JSON `{ "ok": boolean, "message": string }` |

## Recipient

`client.leads@polygon-ws.ru` (constant in PHP; no secrets in repo)

## Forms integrated

All `[data-form]` lead forms use production POST via `src/js/form.js`:

- **Index (`dist/index.html`):** hero (`zakaz-hero-quote`), FAQ/contact (`zakaz-contact-quote`), callback modal (`@@prefix-callback` → `zakaz-callback` on index)
- **Shared partials:** hero + final-contact on PPC section templates (mock handler removed)
- Hidden/meta: `name`, `phone`, `form_id`, `cta_source`, `page_url`, `page_title`, `page_referrer`, `landing_id`, honeypot `company_url`

## Frontend

- Default endpoint: `backend/send-lead.php` (relative to site root)
- Validation, masks, modal CTA bridge unchanged
- Honeypot: empty `company_url` field auto-injected

## Test on hosting

1. Deploy `dist/` to site root (must include `backend/send-lead.php`).
2. Open site over **HTTP/HTTPS** (not `file://`).
3. Submit hero, modal, and FAQ forms with a valid phone.
4. Confirm inbox at `client.leads@polygon-ws.ru`.
5. Submit with empty phone → JSON error «Заполните телефон».

## Limitations

- Uses PHP native `mail()` — delivery depends on host mail configuration (sendmail/exim).
- If `mail()` is disabled or mail goes to spam, plan **SMTP / PHPMailer** in a follow-up (no credentials in this repo).

## Local checks

```bash
cd workspaces/triumph-manipulator-landing-v5
npm run build
php -l backend/send-lead.php
```

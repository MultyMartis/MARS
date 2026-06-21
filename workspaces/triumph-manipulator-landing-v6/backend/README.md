# Backend — form mailer (v5)

## Endpoint

`POST /backend/api/forms/send.php`

Used by landing forms via `data-form-endpoint="/backend/api/forms/send.php"` (default in `src/js/form.js`).

## Recipient

Default: `client.leads@polygon-ws.ru` — set in `backend/config.php`.

Optional override: copy `config.local.example.php` → `config.local.php` (do not commit secrets).

## Deploy layout

On hosting, place the `backend/` folder next to `dist/` at the site web root:

```
/public_html/
  index.html          ← from dist/
  assets/             ← from dist/assets/
  backend/
    api/forms/send.php
    config.php
```

## Test

1. Open the site over **HTTP/HTTPS** (not `file://`).
2. Submit hero, modal, or FAQ contact form with a valid phone.
3. Check inbox `client.leads@polygon-ws.ru`.

PHP syntax check:

```bash
php -l backend/api/forms/send.php
```

## Limitations

- Default transport: **SMTP (Beget, port 465 SSL)** when `use_smtp` is true in `config.php` and `smtp.password` is set in `config.local.php`.
- Fallback: native PHP `mail()` when `use_smtp` is false.
- No dry-run mode in production; local tests should not spam the live inbox.

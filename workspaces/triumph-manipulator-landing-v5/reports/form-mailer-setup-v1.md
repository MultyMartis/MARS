# Form mailer setup — v5

| Item | Value |
|------|--------|
| Endpoint | `/backend/api/forms/send.php` |
| Recipient | `client.leads@polygon-ws.ru` |
| Config | `backend/config.php`, optional `backend/config.local.php` |
| Frontend | `src/js/form.js` (POST `FormData`, honeypot `company_url`) |

See `backend/README.md` for deploy and testing notes.

# Beget SMTP Parameters — Authoritative Source Evidence

**Wave:** PROD-P18D  
**Date:** 2026-08-19  
**Source:** https://beget.com/ru/kb/how-to/mail/obshhie-svedeniya (official Beget documentation, fetched 2026-08-19)  
**Supplementary:** https://beget.com/ru/kb/how-to/mail/nastrojka-mail-na-mac-os-x

---

## Authoritative Beget SMTP Parameters

| Parameter | Value |
|-----------|-------|
| SMTP host | `smtp.beget.com` |
| Port (SSL/implicit TLS) | **465** |
| Encryption on port 465 | **SSL** (implicit TLS — SSL handshake first) |
| Port (STARTTLS / plaintext) | 25 or 2525 |
| Encryption on port 2525 | STARTTLS or none |
| Auth required | YES |
| Username format | Full email address (e.g. `noreply@shpigovsky.ru`) |
| Password | Mailbox password |

**Official Beget quote (translated):**  
"SMTP — 25 или 2525 / SMTP защищённый SSL — **465**"

**Mac OS X doc quote:**  
"порт 465 ‒ защита соединения **SSL**"

---

## Verification Method

Source: official Beget KB page fetched from `beget.com/ru/kb/` — copyright 2007–2026 ООО «Бегет».  
Not inferred from memory or generic hosting defaults.

---

## BEGET SMTP TRANSPORT PARAMETERS VERIFIED FROM AUTHORITATIVE SOURCE

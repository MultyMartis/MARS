# METALLKA — Form Map v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26

```text
Do not submit forms. Do not send mail. Recipient addresses redacted.
```

---

## Form plugin stack

| Component | Status |
|-----------|--------|
| Contact Form 7 | **Active** 6.1.4 |
| CF7 Honeypot | **Active** 3.4.0 — spam protection |
| CFDB7 | **Active** 1.3.5 — stores submissions in WP |
| Dedicated SMTP plugin | **NOT PRESENT** |
| SMTP options (`*smtp*`) | **None** found |
| Mail transport | Likely PHP `mail` / hosting default — **PARTIAL** (not proven) |
| External CRM / webhook | **Not evidenced** in plugin inventory |
| Captcha (reCAPTCHA etc.) | **Not evidenced** as dedicated plugin; honeypot present |

---

## CF7 forms (IDs / titles)

| ID | Title (RU) | Status |
|----|------------|--------|
| 80 | Заказать звонок | publish |
| 81 | Получить консультацию | publish |
| 101 | Обратная связь | publish |
| 290 | Заявка на РЕМОНТ ОТВЕРСТИЙ | publish |
| 291 | Заявка на ТОКАРНЫЕ РАБОТЫ | publish |
| 292 | Заявка на ФРЕЗЕРНЫЕ РАБОТЫ | publish |

Mail sections exist in form content (recipient values **redacted** / not recorded).

---

## Public page usage (content embeds)

| Page | CF7 in `post_content`? |
|------|------------------------|
| contacts (41) | YES |
| remont-otverstij (86) | YES |
| tokarnye-raboty (87) | YES |
| frezernye-raboty (88) | YES |
| home / about / legal pages inspected | NO (in raw content) |

Popup Maker popup **83** (“Заказать звонок”) likely wraps form CTA — treat popups as **PROTECTED** with forms.

---

## Related contact surfaces (not CF7)

| Surface | Owner |
|---------|-------|
| Shortcoder `safe_mail-client` (45) | Obfuscated `document.write` mailto |
| Shortcoder `footer_contacts` (50) | Phone / WhatsApp / Telegram / address HTML |
| Shortcoder `yandex_map` (48) | Map embed |

---

*Form Map v1.*

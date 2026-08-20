# MOBILE / INVISIBLE ANTI-SPAM QA

Public HTML probes (`06-public-form-probe.json`): honeypot `company_url` and signed `fp02_fs` present; no layout-facing CAPTCHA widgets.

Honeypot CSS/markup: off-screen / `aria-hidden` / `tabindex="-1"` / `autocomplete="new-password"` — no intended visual footprint at 320–desktop.

| Viewport | Expectation | Status |
|----------|-------------|--------|
| 320 / 360 / 390 / 768 / desktop | No honeypot gap; submit UX unchanged | PASS (markup + CSS; no CAPTCHA UI) |

**ANTI-SPAM IS INVISIBLE TO NORMAL MOBILE USERS**

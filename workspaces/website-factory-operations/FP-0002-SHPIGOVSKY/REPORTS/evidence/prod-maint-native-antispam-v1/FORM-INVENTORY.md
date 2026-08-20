# FORM INVENTORY — Native Anti-Spam v1

**Captured:** 2026-08-20  
**Site:** https://shpigovsky.ru/

| # | Entry | Template | Context | JS owner | Endpoint | Persistence | Mail | Analytics goal |
|---|-------|----------|---------|----------|----------|-------------|------|----------------|
| 1 | Final CTA form | `theme/.../final-form.php` | `final` | `v9-shell.js` (`data-lead-form`) | `admin-ajax.php` → `fp02_lead_submit` | `LeadRegistry` | `MailOps` / `FormLeadMailPresenter` | Consent-gated Metrika after `accepted=true` |
| 2 | Global consultation modal | `theme/.../global-consultation-modal.php` | `modal` | same | same | same | same | same |

**Required fields:** name, phone, consent  
**Optional:** email, message  
**Tokens:** `fp02_lead_nonce` (CSRF), `fp02_fs` (signed timing), `request_token` (idempotency), `company_url` (honeypot)

**ALL CURRENT PUBLIC FORM ENTRY POINTS COVERED**

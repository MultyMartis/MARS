# Reply-To / From Headers — P18D

**Wave:** PROD-P18D  
**Date:** 2026-08-19

---

## Message Headers (Outgoing Form Notifications)

| Header | Value |
|--------|-------|
| From | `Шпиговский Дом <noreply@shpigovsky.ru>` |
| From Name | `Шпиговский Дом` (from ACF `organisation_name` → blogname fallback) |
| Reply-To | Visitor email — **only if valid** (`is_email($payload['email'])` = true) |
| Reply-To when no email | Header absent (phone-only submissions) |

## Safety Properties

- Visitor email is **never used as From** address.
- No SPF/DKIM violation from noreply@shpigovsky.ru — this is the authenticated sender.
- Reply-To is advisory only; it is never forged.

## SPF/DKIM/DMARC

Current status: **UNKNOWN from source** — DNS records not read in this wave.  
Beget typically provides basic SPF for hosted domains.  
Not blocking SMTP transport verification (Beget accepts mail from authenticated sender regardless of recipient-side DMARC policy check).  
DNS mail authentication records should be verified in a separate deliverability wave if needed.

## SMTP Test Message Headers

| Header | Value |
|--------|-------|
| From | `Шпиговский Дом <noreply@shpigovsky.ru>` |
| To | First configured recipient |
| Subject | `FP-0002 SMTP test [timestamp] UTC (P18D)` |
| Reply-To | (not set — no visitor email in test) |
| Content-Type | `text/plain; charset=UTF-8` |

# FP-0002 — DNS Cutover Status v1

**Wave:** PROD-P02 · **updated P18A** (operator NS + WordPress URL cutover intaken)  
**Date:** 2026-08-18 (P18A)  
**Status:** **`DNS_NS = OPERATOR CUTOVER PERFORMED`** — public apex **not yet** serving WordPress

Historical P02/P17 text that said `DNS_CUTOVER = DEFERRED` / NS not switched is **superseded for current operations**. Those reports remain historical evidence.

---

| Field | Value |
|-------|-------|
| WordPress home / siteurl | `https://shpigovsky.ru` |
| Live domain (intent + WP options) | `shpigovsky.ru` |
| Temporary WP host | `http://shpigovsky.beget.tech/` (inner routes still serve WP) |
| Public NS (system resolver) | Beget: `ns1.beget.ru` `ns2.beget.pro` `ns1.beget.com` `ns1.beget.pro` `ns2.beget.com` `ns2.beget.ru` |
| Apex A @8.8.8.8 | `45.130.41.70` |
| Apex A local cache | `92.255.111.71` (legacy REG.RU website IP) |
| `shpigovsky.beget.tech` A | `91.106.207.76` |
| Public `https://shpigovsky.ru/` | Legacy (non-WP) HTML at P18A intake |
| SSL public apex | Let's Encrypt valid on the **legacy** origin |
| SSL WordPress vhost 443 | not ready (beget.tech HTTPS timeout) |
| Agent DNS writes | **FORBIDDEN** |
| Redirects beget.tech → shpigovsky.ru | Homepage already 301s to public apex (**risk:** users hit legacy site). Inner WP paths still 200. Do not add a blanket temp-host 301 until WP is the public origin. |
| `siteurl` / `home` | **DONE** — do not revert |

---

## P18A classification

```text
NS CUTOVER = DONE BY OPERATOR
WORDPRESS URL CUTOVER = DONE BY OPERATOR
PUBLIC APEX → WORDPRESS ORIGIN = NOT YET
SSL (WP ORIGIN) = IN PROGRESS
```

Next DNS/hosting check: confirm Beget domain `shpigovsky.ru` is attached to `/home/s/shpigovsky/shpigovsky.ru/public_html` and public A/www answer that vhost.

Evidence: `REPORTS/evidence/prod-p18a-live-domain-legal-state/`

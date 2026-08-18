# Forge WordPress — DNS / NS Cutover Standard v1

**ID:** FW-RB-07  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** D  
**Evidence:** FP-0002 P17 — web on one host, zone+mail on registrar

---

## Distinguish

| Mode | What moves |
|------|------------|
| **A-record cutover** | Website IPs only; NS stay; mail records untouched |
| **Nameserver delegation** | Entire zone must be **reproduced** at the target DNS |

```text
MOVING WEBSITE DNS MUST NOT ACCIDENTALLY MOVE OR BREAK MAIL.
```

---

## Before NS change

Inventory the **authoritative** zone (not only public A):

- A / AAAA (apex, www, mail, ftp, extra hosts)  
- CNAME  
- MX  
- SPF / DKIM / DMARC TXT  
- Verification TXT  
- CAA / SRV  
- Subdomains  
- Record TTL  
- Current NS (rollback target)  

Reproduce the zone at the target provider **before** switching NS. Confirm DKIM in the mail panel if not in public DNS.

Worksheet: [DNS-ZONE-MIGRATION-WORKSHEET](../templates/FORGE-WORDPRESS-DNS-ZONE-MIGRATION-WORKSHEET-v1.md).

---

## Rollback

Keep the old zone during stabilization; restore previous NS at the registrar.

---

*FW-RB-07 v1.*

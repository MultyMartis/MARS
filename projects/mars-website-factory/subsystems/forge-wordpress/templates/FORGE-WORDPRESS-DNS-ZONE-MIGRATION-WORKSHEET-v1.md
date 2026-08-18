# WP Forge — DNS zone migration worksheet v1

Project:  
Current registrar / DNS:  
Target DNS:  
Mail provider (may differ from web):  
Mode: A-record only / NS delegation  

## Inventory (copy from authoritative zone)

| Type | Name | Value | TTL | Copy to target? |
|------|------|-------|-----|-----------------|
| NS | | | | rollback |
| A | @ | | | |
| A | www | | | |
| AAAA | | | | |
| CNAME | | | | |
| MX | | | | **MAIL** |
| TXT SPF | | | | **MAIL** |
| TXT DKIM | | | | **MAIL** |
| TXT DMARC | | | | **MAIL** |
| TXT verify | | | | |
| CAA/SRV | | | | |
| Other hosts | | | | |

## Checks

- [ ] Mail records will remain valid after the change  
- [ ] Target zone populated **before** NS switch  
- [ ] Rollback NS recorded  
- [ ] Old zone retained during stabilization  

---

*Worksheet v1. No credentials.*

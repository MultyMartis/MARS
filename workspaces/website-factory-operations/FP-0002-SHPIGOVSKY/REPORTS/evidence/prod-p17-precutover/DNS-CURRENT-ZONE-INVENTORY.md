# DNS CURRENT ZONE INVENTORY — shpigovsky.ru

**Wave:** FP-0002 PROD-P17 CONT1  
**Date (UTC):** 2026-08-18  
**Method:** public recursive DNS (system / 8.8.8.8 / 1.1.1.1 / 9.9.9.9), WHOIS `whois.tcinet.ru`, targeted UDP to REG.RU hosting NS anycast IPs  
**Mutation:** **NONE** — NS not switched  

Token: `CURRENT DNS ZONE MUST BE INVENTORIED BEFORE NAMESERVER CUTOVER`

Machine-readable: `DNS-CURRENT-ZONE-INVENTORY.json`, `DNS-AUTH-SUPPLEMENT.json`, `WHOIS-SHPIGOVSKY-RU.txt`

---

## Current authoritative nameservers

| Source | NS |
|--------|----|
| WHOIS TCI | `ns1.hosting.reg.ru.` `ns2.hosting.reg.ru.` |
| Recursive DNS | `ns1.hosting.reg.ru` `ns2.hosting.reg.ru` |

**Registrar (WHOIS):** `REGRU-RU`  
**State:** `REGISTERED, DELEGATED, UNVERIFIED`  
**Created:** 2024-08-06 · **Paid-till:** 2027-08-06  

**Rollback target (exact):** `ns1.hosting.reg.ru` and `ns2.hosting.reg.ru`

Parent `.ru` referral TTL: **SAFE UNKNOWN** this wave (direct TLD RD=0 query returned empty answer/authority from the queried TLD server). WHOIS + recursive NS are consistent and are the inventory authority for current delegation.

---

## Target Beget nameservers

**Account-panel confirmation:** **OPERATOR INPUT REQUIRED** — Beget control-panel credentials in `secrets.local.md` are empty; this wave did **not** read the account DNS UI.

**Published Beget documentation (not memory):**

Sources:

- https://beget.com/en/kb/manual/domains
- https://beget.com/ru/kb/how-to/domains/izmenenie-ns-serverov-dlya-domennogo-imeni

Published set:

- `ns1.beget.com`
- `ns2.beget.com`
- `ns1.beget.pro`
- `ns2.beget.pro`

Gate NS12: treat this published set as the **target candidate**. Operator must confirm the same four hostnames in the Beget panel for this account before registrar NS mutation.

**NS was not switched in CONT1.**

---

## Apex / website

| Name | Type | Data | TTL observed | Notes |
|------|------|------|--------------|-------|
| `shpigovsky.ru` | A | `92.255.111.71` | recursive ~3600; one REG.RU NS anycast answered TTL 300 | **Old hosting IP** — REPLACE at website cutover |
| `shpigovsky.ru` | AAAA | *none* | — | No apex IPv6 |
| `www.shpigovsky.ru` | A | `92.255.111.71` | same | Not a CNAME |
| `www.shpigovsky.ru` | AAAA | *none* | — | |
| `www.shpigovsky.ru` | CNAME | *none* | — | |

## Mail / related hosts

| Name | Type | Data | Notes |
|------|------|------|-------|
| `shpigovsky.ru` | MX | `10 mx1.hosting.reg.ru.` `20 mx2.hosting.reg.ru.` | Mail provider = **REG.RU hosting mail**, not Beget |
| `shpigovsky.ru` | TXT (SPF) | `v=spf1 ip4:31.31.196.206 a mx include:_spf.hosting.reg.ru ~all` | |
| `mail.shpigovsky.ru` | A | `31.31.196.206` | |
| `mail.shpigovsky.ru` | AAAA | `2a00:f940:2:2:1:1:0:168` | |
| `ftp.shpigovsky.ru` | A / AAAA | `31.31.196.206` / `2a00:f940:2:2:1:1:0:168` | |
| `smtp.shpigovsky.ru` | A / AAAA | same | |
| `pop.shpigovsky.ru` | A / AAAA | same | |

MX target host IPs (informational, do not copy as website A): `mx1/mx2.hosting.reg.ru` → `31.31.194.240`, `31.31.194.241`.

## Absent / not discovered (do not invent)

| Name / type | Result |
|-------------|--------|
| `_dmarc.shpigovsky.ru` TXT | No TXT answer (NODATA / not published) |
| DKIM selectors tried (TXT/CNAME): default, mail, google, k1, k2, s1, s2, selector1, selector2, dkim, yandex, mailru, beget, beget1, fm1–3, cm, s1024, s2048, protonmail, protonmail2, pm, reg, regru, hosting, server168 | **none found** |
| `imap.shpigovsky.ru` | NXDOMAIN |
| `autodiscover.shpigovsky.ru` | NXDOMAIN |
| `autoconfig.shpigovsky.ru` | NXDOMAIN |
| `webmail.shpigovsky.ru` | NXDOMAIN |
| Wildcard `*.shpigovsky.ru` | not present |
| CAA | none |
| SRV (`_autodiscover._tcp`, `_imaps._tcp`, `_submission._tcp`, …) | none found |
| Google / Yandex verification TXT | **not present** on apex (only SPF TXT found) |

SOA (recursive): `server168.hosting.reg.ru. support.reg.ru. 2024080622 10800 3600 604800 86400`

## Temporary Beget website host (not the `shpigovsky.ru` zone)

| Name | Type | Data |
|------|------|------|
| `shpigovsky.beget.tech` | A | `91.106.207.76` |
| `shpigovsky.beget.tech` | AAAA | **none** |
| `www.shpigovsky.beget.tech` | A | `91.106.207.76` |

This A record is the **evidence-based Beget website IPv4** for future apex/`www` replacement. Do not guess another IP.

## AAAA / IPv6 classification

| Record | Classification |
|--------|----------------|
| Apex / www AAAA | **none today** — do not invent; do not leave a stale website AAAA |
| `mail`/`ftp`/`smtp`/`pop` AAAA `2a00:f940:2:2:1:1:0:168` | **COPY TO BEGET** (REG.RU mail/hosting IPv6). Not website routing |
| Beget tech AAAA | none — **do not add website AAAA** unless Beget later publishes one |

Token: stale website AAAA **ruled out** for apex/www.

## TTL notes

- Recursive A/MX/TXT commonly showed **3600** (remaining TTL lower on some lookups).
- One REG.RU NS anycast IP answered apex A with **TTL 300**.
- SOA refresh **10800**, retry **3600**, expire **604800**, minimum **86400**.

Lowering A TTL **before** NS change can shorten **A-record** cache after the new zone is live. It does **not** make parent NS delegation instant. NS/delegation caches follow parent NS TTL and resolver behavior; expect **hours**, Beget documents **24–72 hours** for NS changes.

## Evidence caveat (direct NS anycast)

UDP queries with RD=0 to `31.31.194.245` (one `ns1.hosting.reg.ru` A) returned A for the domain but **empty** MX/TXT/NS/SOA answers (NOERROR/NODATA). Public resolvers (four perspectives) consistently returned MX/SPF/NS/SOA. Inventory of mail/SPF uses **public recursive + WHOIS**, not that single anycast NODATA view.

---

*Inventory only. No registrar or Beget NS write.*

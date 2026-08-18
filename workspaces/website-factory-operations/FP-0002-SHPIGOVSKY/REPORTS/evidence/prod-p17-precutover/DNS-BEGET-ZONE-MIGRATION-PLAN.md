# DNS BEGET ZONE MIGRATION PLAN — shpigovsky.ru

**Wave:** FP-0002 PROD-P17 CONT1  
**NS mutation this wave:** **FORBIDDEN / NOT DONE**  
**Beget DNS panel writes this wave:** **NOT DONE** — panel credentials empty; produce manual instructions only.

CSV: `DNS-BEGET-ZONE-MIGRATION-PLAN.csv`  
JSON: `DNS-BEGET-ZONE-MIGRATION-PLAN.json`

Goal: when Beget NS becomes authoritative, **website** answers on Beget IPv4 and **mail / non-web** services continue on REG.RU hosting DNS data copied into the Beget zone.

Token: `MAIL DNS PRESERVATION PLAN = READY BEFORE NS CUTOVER`

---

## Mail provider (from DNS, not assumption)

| Item | Evidence |
|------|----------|
| Provider | **REG.RU hosting mail** (`mx1/mx2.hosting.reg.ru`) |
| Not Beget | Beget MX (`mx1.beget.com`) appears only on `shpigovsky.beget.tech`, which is a different zone |
| SPF | `v=spf1 ip4:31.31.196.206 a mx include:_spf.hosting.reg.ru ~all` |
| DKIM | **Not published** on probed selectors |
| DMARC | **Not published** |

SMTP for WordPress remains **not configured** this wave. Do not enable PHP mail fallback. Current `fp02-pre-cutover-mail-suppression.php` stays until a later SMTP wave.

---

## Record-by-record

See CSV for the full table. Summary:

**COPY TO BEGET (exact):**

- MX `10 mx1.hosting.reg.ru.` / `20 mx2.hosting.reg.ru.`
- SPF TXT (full string above)
- `mail` / `ftp` / `smtp` / `pop` A `31.31.196.206`
- same four names AAAA `2a00:f940:2:2:1:1:0:168`

**REPLACE FOR WEBSITE CUTOVER:**

- `@` A: `92.255.111.71` → `91.106.207.76` (from `shpigovsky.beget.tech` A)
- `www` A: same replacement

**DO NOT COPY:**

- REG.RU NS/SOA
- empty/absent CAA, SRV, wildcard, imap, autodiscover, autoconfig, webmail
- inventing DMARC/DKIM/verification TXT

**OPERATOR DECISION:**

- Hidden DKIM in REG.RU mail panel (public DNS has none) — confirm before NS switch
- Adding DMARC later
- Search-console verification TXT if created after this inventory

**OBSOLETE / PROVEN UNUSED:** NXDOMAIN hosts listed in CSV

---

## Website DNS target (Beget)

| Name | Type | Target | Evidence |
|------|------|--------|----------|
| `@` | A | `91.106.207.76` | `shpigovsky.beget.tech` A |
| `www` | A | `91.106.207.76` | `www.shpigovsky.beget.tech` A |
| `@` / `www` | AAAA | **omit** | Beget tech has no AAAA |

Expected **after SSL + siteurl** (not now):

- Canonical: `https://shpigovsky.ru/` (project docs; apex)
- Likely: `https://www.shpigovsky.ru/` → 301 → `https://shpigovsky.ru/`
- Inverse (apex → www) is **not** the documented canonical

www↔apex and HTTP→HTTPS are **cutover Apache/WordPress actions**, not this CONT1.

---

## Beget zone preparation — manual (no agent write)

Beget CP credentials = empty. Do **not** use API.

Operator steps **before** registrar NS change (safe: Beget zone is not public until NS switch):

1. Snapshot / screenshot current Beget DNS for `shpigovsky.ru` if a zone already exists. **Do not delete unknown records blindly.**
2. Ensure domain is attached to the existing site directory `~/shpigovsky.ru/public_html` (already the production docroot).
3. Set `@` A and `www` A to `91.106.207.76` (re-check in panel — Beget may show a site IP; **must match live `shpigovsky.beget.tech` A or the IP Beget displays for this site**).
4. Reproduce COPY records exactly (MX, SPF, mail/ftp/smtp/pop A/AAAA).
5. Leave NS at REG.RU until gates pass.
6. After SSL install on Beget DNS, Beget may auto-edit A records ([Beget SSL article](https://beget.com/ru/kb/how-to/sites/podklyuchenie-ssl-k-sajtu)) — re-verify MX/SPF/mail hosts immediately after SSL.

---

## TTL strategy

Lowering **A** TTL at REG.RU (e.g. to 300) **before** NS change can shorten old-A cache **after** the new zone is served. It does **not** make NS delegation instant. Parent/NS caches are independent. Beget documents NS change effect in **24–72 hours**. Plan the cutover window accordingly. Do not claim instant global consistency.

---

## Nameserver rollback

Rollback delegation:

1. At REG.RU (registrar), restore NS to `ns1.hosting.reg.ru` and `ns2.hosting.reg.ru`.
2. **Keep the old REG.RU DNS zone** through the stabilization window. Do not assume REG.RU retains an unused zone forever — operator must **not delete** it until rollback is no longer needed.
3. Verify WHOIS nserver + recursive NS + apex A `92.255.111.71` if rolling all the way back to old web, **or** keep website A on Beget only if that was the intent of a partial rollback (default full rollback = prior NS + prior zone).

Token: `NS ROLLBACK TARGET RECORDED`

---

## Cutover verification (when NS **is** later authorized)

Independently of Windows DNS cache:

1. WHOIS / parent nserver = Beget set
2. Query Beget NS directly for `@` A/AAAA, `www`, MX, TXT/SPF, DKIM, DMARC
3. Public resolvers: 8.8.8.8, 1.1.1.1, 9.9.9.9
4. Website: `https://shpigovsky.ru/` only after SSL
5. Mail: MX still `mx1/mx2.hosting.reg.ru`; SPF unchanged

---

*Plan only. No NS switch. No SMTP. No SSL. No siteurl change.*

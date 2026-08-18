# RUNBOOK — FP-0002 MANUAL NS SWITCH HANDOFF

**Audience:** operator (REG.RU panel)  
**Cursor / Web-GPT:** do **not** change registrar NS, do **not** assume propagation, do **not** start P18 until the operator says **NS SWITCHED**.

No registrar credentials are stored in this document.

---

## BEFORE NS SWITCH

1. Content freeze (`REPORTS/RUNBOOK-FP-0002-PRE-CUTOVER-FREEZE.md`).
2. Fresh full files + DB backup under `X:\AI MARS STORAGE\backups\fp-0002\` after freeze.
3. Beget DNS zone prepared in the Beget panel (copy mail records; website A → Beget `91.106.207.76`). Plan: `REPORTS/evidence/prod-p17-precutover/DNS-BEGET-ZONE-MIGRATION-PLAN.md`.
4. **Preserve mail records** (REG.RU hosting mail, not Beget mail):
   - MX `10 mx1.hosting.reg.ru.` / `20 mx2.hosting.reg.ru.`
   - SPF TXT as inventoried
   - `mail`/`ftp`/`smtp`/`pop` A/AAAA as inventoried
   - Confirm hidden DKIM in REG.RU mail panel if any
5. Current rollback NS recorded:
   - `ns1.hosting.reg.ru`
   - `ns2.hosting.reg.ru`

Target published Beget NS set (panel confirm still required at switch time):

- `ns1.beget.com`
- `ns2.beget.com`
- `ns1.beget.pro`
- `ns2.beget.pro`

---

## OPERATOR ACTION

Change NS in **REG.RU** to the verified Beget NS set.

This is the only registrar write. Cursor must not do it.

---

## AFTER OPERATOR SAYS “NS SWITCHED”

Cursor / Web-GPT must **not** assume propagation.

Then (P18 charter only):

1. Verify public delegation (parent / WHOIS / recursive).
2. Verify authoritative Beget DNS.
3. Verify A / www / MX / TXT against the inventory + Beget zone.
4. Only then continue the final cutover execution charter (SSL → WordPress domain → redirects → SMTP → indexing).

If delegation is still REG.RU: **wait**. Do not force SSL or siteurl.

---

## Rollback NS

Restore `ns1.hosting.reg.ru` and `ns2.hosting.reg.ru` at REG.RU. Keep the REG.RU zone during stabilization; do not delete it immediately.

*P17-FU02 · handoff only · no credentials.*

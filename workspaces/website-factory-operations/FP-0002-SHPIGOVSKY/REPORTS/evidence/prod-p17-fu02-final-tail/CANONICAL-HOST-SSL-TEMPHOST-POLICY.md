# CANONICAL HOST + TEMPORARY BEGET HOST + SSL PLAN

**Wave:** P17-FU02  
**Activate now:** **NO**

## Final canonical host policy

**Recorded:** `https://shpigovsky.ru/` (apex, HTTPS).

`https://www.shpigovsky.ru/*` → **301** → `https://shpigovsky.ru/*`

Project evidence (P17 CONT1 runbook, DNS plan) agrees. No conflicting operator decision found.  
**Token:** `FINAL CANONICAL HOST POLICY RECORDED`

HTTP `http://shpigovsky.ru/*` → HTTPS apex after cert (PHASE A).

## Temporary Beget host post-cutover policy

**Desired (after final-domain smoke, not now):**

`http(s)://shpigovsky.beget.tech/*` → **301** → `https://shpigovsky.ru/*`  
preserving path and query (`REQUEST_URI`).

**Loop control:** rule MUST be `RewriteCond %{HTTP_HOST} ^shpigovsky\.beget\.tech$`.  
If Beget serves both names as `ServerAlias` of one vhost, an unconditioned redirect would loop the canonical host. Do not use a global "redirect this site" panel toggle without verifying `HTTP_HOST`.

**Token:** `TEMPORARY HOST POST-CUTOVER POLICY RECORDED`

## SSL cutover steps (P18, after NS SWITCHED)

**Token:** `SSL CUTOVER STEPS READY`

1. Verify authoritative Beget DNS (not still REG.RU hosting NS).
2. Verify apex A = Beget website IP (`91.106.207.76` as of P17; re-check panel).
3. Verify www record/policy (A to same IP; later www→apex 301).
4. Request/attach SSL (Let's Encrypt / Beget). Keep HTTP answering until issued. Beget may rewrite A on SSL — re-check MX/SPF after.
5. Verify certificate subject/SAN includes `shpigovsky.ru` and `www.shpigovsky.ru`.
6. Verify HTTP and HTTPS both respond on apex.
7. **Only then** enable HTTPS (and www) redirects in `.htaccess` PHASE A.
8. **Only then** WordPress `home`/`siteurl` + exact URL plan.

No SSL cutover in FU02.

# CUTOVER FILE MUTATION PLAN

**Wave:** P17-FU02  
**Execute:** **NO** (P18 after `NS SWITCHED` + DNS + SSL as specified)  
**Token:** `CUTOVER FILE PLAN = EXECUTABLE WITHOUT DISCOVERY`

Phases must not be mixed.

Canonical fragment for legacy paths (already live, do not redo):  
`DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment`

Current production `.htaccess` SHA-256: `ec8f06028d3ecde7442701ed09fce3aa107fc74a41434647e413f4a0088d9f38`

---

## PHASE A — domain / SSL

Do this only after: Beget DNS authoritative, apex resolves, cert issued, HTTP and HTTPS both verified.

### A1. HTTPS redirect (final host)

Owner: `public_html/.htaccess` custom block **after** legacy redirects, **before** `# BEGIN WordPress`.

Host-conditional (prevents looping `shpigovsky.ru` into itself and prevents sending beget-tech requests through the wrong rule):

```apache
# FP-0002 PHASE A — HTTPS on canonical host (P18)
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP_HOST} ^(www\.)?shpigovsky\.ru$ [NC]
RewriteCond %{HTTPS} !=on
RewriteRule ^ https://shpigovsky.ru%{REQUEST_URI} [R=301,L]
</IfModule>
```

Rollback: remove this block; restore Layer B `.htaccess`.

### A2. www → apex

```apache
# FP-0002 PHASE A — www to apex (P18)
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.shpigovsky\.ru$ [NC]
RewriteRule ^ https://shpigovsky.ru%{REQUEST_URI} [R=301,L]
</IfModule>
```

Place **before** the generic HTTPS rule or combine with it. Do not activate now.

### A3. Temporary Beget host → final domain

**After** final-domain smoke (indexing still closed). Host-conditional so `ServerAlias` of the same vhost cannot loop the canonical host:

```apache
# FP-0002 PHASE A — temporary Beget host (P18, after smoke)
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP_HOST} ^shpigovsky\.beget\.tech$ [NC]
RewriteRule ^ https://shpigovsky.ru%{REQUEST_URI} [R=301,L]
</IfModule>
```

Preserves path and query (`REQUEST_URI`). Do not use an unconditioned `RewriteRule` that would also match `shpigovsky.ru`.

### A4. MU / config

- `wp-config.php`: no `WP_HOME` / `WP_SITEURL` overrides today (`null`). Prefer option updates over adding defines. If defines are added in P18, they must match `https://shpigovsky.ru` and be snapshotted first.
- No MU host-redirect owner currently. Do not add one unless Apache cannot express A1–A3.

### A5. robots.txt Sitemap host

May wait for PHASE C. If touched in A, only the Sitemap absolute host; keep `Disallow: /` until PHASE C.

---

## PHASE B — SMTP

- Configure SMTP plugin/constants **only** in P18 after domain smoke.
- Disable/remove `wp-content/mu-plugins/fp02-pre-cutover-mail-suppression.php`.
- Do **not** enable PHP `mail()` fallback.
- Do **not** mix with HTTPS/NS.

Exact removal: delete or rename the MU file on Beget; confirm `has_filter('pre_wp_mail')` is false; then SMTP; then form QA.

---

## PHASE C — indexing

- `blog_public` 0 → 1
- `robots.txt`: allow + Sitemap `https://shpigovsky.ru/wp-sitemap.xml`
- Confirm meta robots no longer force noindex on public templates
- Then sitemap submissions (not a file mutation)

---

## Do not change at cutover

- Legacy 7/7 path rules (already live)
- WordPress `# BEGIN WordPress` block (except if WP itself rewrites it)

*P17-FU02 plan only.*

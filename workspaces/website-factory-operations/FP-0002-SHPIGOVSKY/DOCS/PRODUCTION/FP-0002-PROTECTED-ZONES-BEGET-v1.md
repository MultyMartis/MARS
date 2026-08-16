# FP-0002 — Protected Zones (Beget) v1

**Wave:** PROD-P01 · **updated PROD-P02** (access-specific protection; no production mutation)  
**Rule:** Protected-by-default. Any future mutation requires explicit charter, backup, and exact scope.  
**Access contour:** credentials becoming available does **not** lift protection.

---

## Classification key

| Class | Meaning |
|-------|---------|
| **SOURCE-OWNED** | Canonical under `WORDPRESS/` — change via source → exact deploy |
| **DB/ADMIN-OWNED** | WordPress content/settings — change via Admin (or proven WPilot capability only) |
| **RUNTIME-GENERATED** | Caches, transients, uploads derivatives |
| **PROTECTED OPERATIONAL** | Hosting/security/secrets — operator-only |
| **SAFE UNKNOWN** | Not yet verified on Beget |

---

## Protected-by-default inventory

| Zone | Class | Notes |
|------|-------|-------|
| `wp-config.php` | PROTECTED OPERATIONAL | Never agent-edit on production |
| `.htaccess` / nginx vhost / Beget panel server config | PROTECTED OPERATIONAL | |
| WordPress core | PROTECTED OPERATIONAL | Core updates = separate charter |
| Users / auth / roles / sessions | DB/ADMIN-OWNED + PROTECTED OPERATIONAL | No credential requests in agent waves |
| Production DB schema + data | DB/ADMIN-OWNED | No routine direct SQL |
| `wp-content/uploads/` | RUNTIME-GENERATED / content media | Preserve; no broad mirror |
| Forms + form handlers | SOURCE-OWNED (theme/plugin) + DB/ADMIN-OWNED (options) | No live submit tests without charter |
| SMTP / mail plugins / Beget mail | PROTECTED OPERATIONAL / SAFE UNKNOWN | |
| Menus | DB/ADMIN-OWNED | |
| Header / footer chrome | SOURCE-OWNED (theme) + options | |
| Global Site Settings / ACF options | DB/ADMIN-OWNED with source field definitions | |
| SEO settings / titles / canonicals | DB/ADMIN-OWNED | Temporary hostname risks documented; no mutation here |
| Redirects | PROTECTED OPERATIONAL / DB | Do not add beget.tech → shpigovsky.ru now |
| Cache / optimization plugins | SAFE UNKNOWN / PROTECTED OPERATIONAL | |
| ACF field group schema | SOURCE-OWNED (JSON/PHP) + DB registration | Never broad-sync all groups |
| Theme `shpigovsky` files | SOURCE-OWNED | Exact-file deploy only after drift detect |
| Plugin `shpigovsky-core` | SOURCE-OWNED | |
| Other plugins (ACF PRO, etc.) | Operator-managed / PROTECTED OPERATIONAL | |
| **WPilot plugin + options/token** | PROTECTED OPERATIONAL | Already present post-migration; treat as sensitive |
| Source ↔ production operator drift | PROTECTED OPERATIONAL process | See change model |
| DNS (`shpigovsky.ru`) | PROTECTED OPERATIONAL | **DEFERRED** |
| SSL certificates | PROTECTED OPERATIONAL / SAFE UNKNOWN | |
| Beget hosting settings / cron / quotas | PROTECTED OPERATIONAL | |

---

## FP-0002-specific high-sensitivity surfaces

1. **Treatment Program auto-source** (`#13` children + page titles/slugs/mini-descriptions) — DB/ADMIN content with SOURCE-OWNED render helpers.  
2. **Comfort gallery** — SOURCE-OWNED Fancybox enqueue + markup; media may be theme assets or uploads.  
3. **Operator-tuned CSS** (`v9-style.css` hash `1CCC5A8F…`) — SOURCE-OWNED; publicly hash-matched on Beget as of PROD-P01.  
4. **Migrated absolute local URLs** (`http://shpigovsky.test/...`) in some CTA links — content/theme residue; repair only under future charter.

---

## PROD-P02 access-specific protection

Filling local secrets does **not** authorize action. Default deny remains for:

| Zone | Access note |
|------|-------------|
| DNS | WRITE forbidden until explicit cutover task |
| SSL | Operator/HITL only |
| `wp-config.php` | Never agent-edit on production |
| `.htaccess` / server config | Never agent-edit |
| Users / auth / roles / sessions | No new users, no password changes in access waves |
| DB schema | Full DB backup + charter |
| WordPress core | Separate charter |
| Plugin updates | Separate charter (including WPilot ZIP) |
| Theme updates (vendor) | Separate charter |
| WPilot settings / token / write flag | Separate reconcile/write gates only |
| Global ACF schema | Never broad-sync all groups |
| SMTP | Do not collect/use unless chartered |
| Forms | No live submit tests without charter |
| Redirects | No beget.tech → shpigovsky.ru now |
| SEO globals | No robots/noindex mutation for temporary host without charter |
| Cache configuration / purge | Minimum action only inside a deploy charter |
| Cron | Protected |
| Uploads deletion | Forbidden |

Credential classes (Beget panel, FTP/SFTP, SSH, DB, WP Admin, WPilot token) are **capability stores**. Authorization stays in the Access Matrix and per-task charters.

See [FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md](FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md).

---

## Default deny

- Broad `local → production` sync  
- FTP/SFTP mirror / purge  
- Unchartered WPilot write / bridge / token ops  
- DNS or SSL changes in onboarding waves  
- Direct DB edits as routine workflow  
- Any mutation merely because credentials exist  

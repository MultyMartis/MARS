# I-SEO Report Hub — Production Environment Requirements v0.1

**Status:** POLICY / REQUIREMENTS ONLY — no provisioning; no `.env` creation; no deployment  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Charter 01  
**Related:** [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md)

---

## 1. Scope

Requirements for a **production / production-pilot** environment distinct from local Laragon MVP (`iseo-report-hub.test`, `iseo_report_hub_dev`).

Assumes recommended topology **Option C (VPS)** unless Decision 01 selects another validated path.

---

## 2. PHP requirements

| Item | Requirement |
|------|-------------|
| Preferred version | **PHP 8.3.x** (matches local attested 8.3.30) |
| Acceptable minimum | Operator-decided; must not be below what app `declare(strict_types=1)` + syntax need; document pin before deploy |
| SAPI | PHP-FPM preferred with Nginx/Apache; `mod_php` acceptable if operator prefers Apache |
| Required extensions | `pdo`, `pdo_mysql`, `mbstring`, `json`, `openssl`, `fileinfo`, `session` |
| Strongly recommended | `intl`, `curl`, `dom`/`xml`, `iconv`, `gd` (listed optional in local `/health` but useful) |
| Optional | `zip` (future package/export), `imagick`, `mysqli` |
| Production PHP flags | `display_errors=Off`; no stack traces to clients; appropriate `memory_limit` / `max_execution_time` for PDF jobs if generation runs on host |

Source of required/optional extension lists: local `HealthController` expected checks + charter constraints.

---

## 3. MySQL / MariaDB requirements

| Item | Requirement |
|------|-------------|
| Preferred | **MySQL 8.x** |
| Acceptable | MariaDB version compatible with current migrations / utf8mb4 |
| Charset / collation | **utf8mb4** |
| Database | Dedicated production DB name — **never** reuse `iseo_report_hub_dev` |
| User | Least-privilege application user (no SUPER / FILE unless proven needed) |
| Host | Local socket or private network; not world-exposed without firewall rule |
| Migrations | Apply from empty/controlled schema after backup; dry-run first |
| Fixtures | Local fixture tooling must **not** run against production unless explicitly safe and charter-approved |

---

## 4. Webserver requirements

| Item | Requirement |
|------|-------------|
| Server | Nginx **or** Apache |
| Document root | **Only** application `/public` |
| Rewrite | Front controller to `public/index.php` (existing app pattern) |
| HTTPS | Mandatory for production client-facing URLs |
| HTTP | Redirect to HTTPS |
| Headers | Support hardened response headers for public PDF stream (`X-Content-Type-Options: nosniff`, robots/noindex posture preserved) |
| Rate limiting | Plan for public share route (implementation may be webserver or app layer in later wave) |
| Listing | No directory listing; no `/share` index |

---

## 5. Filesystem / storage layout

Conceptual VPS layout (**do not create now**):

```text
/var/www/iseo-report-hub/current                 -> symlink to release
/var/www/iseo-report-hub/releases/<hash-or-ts>/
/var/www/iseo-report-hub/shared/.env.production
/var/www/iseo-report-hub/shared/storage/         # exports etc.
/var/www/iseo-report-hub/shared/logs/
public docroot = /var/www/iseo-report-hub/current/public
```

Rules:

- App code preferably read-only at runtime except intentional writable dirs.
- **Export artifacts** under shared storage **outside** public webroot.
- **Logs** outside public webroot.
- No public webroot artifact writes for report PDFs/HTML.
- Release hash pinned; rollback via symlink (or equivalent).

---

## 6. Public docroot

| Item | Requirement |
|------|-------------|
| Docroot | `/public` only |
| Forbidden in docroot | `.env*`, `storage/`, migrations, tools, source outside public entry |
| Health | `GET /health` available for uptime checks (no secrets) |
| Public share | `GET /share/report/{64hex}` only; no listing |

---

## 7. `.env.production` / secrets contour

| Item | Requirement |
|------|-------------|
| Location | Outside Git — e.g. `shared/.env.production` |
| `APP_ENV` | `production` |
| Debug | Off |
| `APP_URL` | HTTPS base URL used for share URL generation |
| DB credentials | Production-only; least privilege |
| Session | Secure cookie flags; HTTPS-only |
| Secrets | Not in reports, commits, screenshots, or chat logs |
| Local contour | Keep `.env.local` on workstation separate; never copy fixture passwords into production casually |

This charter does **not** create or edit any env file.

---

## 8. Session / cookie

| Item | Requirement |
|------|-------------|
| Transport | HTTPS only in production |
| Flags | Secure; HttpOnly; SameSite appropriate for app |
| Save path | Not public; not under docroot |
| Auth | Internal routes remain auth-required |

---

## 9. HTTPS / domain

| Item | Requirement |
|------|-------------|
| Domain | Stable operator-approved production domain/subdomain |
| Certificate | Let’s Encrypt / panel / reverse proxy — operator choice |
| Share URLs | Must use HTTPS base; HTTP-only production share URLs are a **STOP** |
| Separation | Production domain ≠ `iseo-report-hub.test` |

---

## 10. PDF / headless browser

Local MVP uses Edge headless (Chrome alternate) to generate PDF from HTML artifacts.

Production modes (operator Decision 01):

| Mode | When allowed |
|------|--------------|
| **P1** Headless browser on production host | Only after binary + fonts + smoke validation on target OS |
| **P2** Generate PDFs internally (local/staging) and upload artifacts | If production host cannot run headless safely |
| **P3** Serve pre-generated exports only | Narrow pilot; no on-host generation |

Compatibility requirements for P1:

- Chromium/Chrome/Edge (or equivalent) installable and runnable by app user
- Fonts sufficient for RU report templates
- Process isolation / resource limits understood
- Failure modes do not expose internal paths to public clients

If headless unavailable and generation is still claimed → **STOP** until mode P2/P3 chosen.

---

## 11. Public share requirements (environment impact)

| Item | Requirement |
|------|-------------|
| Route | `/share/report/{64hex}` unchanged as production candidate |
| Forbidden | `/share` listing; `/r/{token}`; public landing (deferred product) |
| Stream | Direct PDF stream remains candidate |
| Storage | Not public |
| Token sensitivity | Token in URL ⇒ access logs are sensitive |
| DB | Token hash only; no plaintext token storage |
| Behavior | Revoke / expiry / max_access must be re-tested after deploy |
| Robots | noindex/nofollow posture preserved |

---

## 12. Logging / monitoring

| Item | Requirement |
|------|-------------|
| App error logs | Protected; outside public |
| Webserver access logs | Protected; rotated; treat paths with tokens as sensitive |
| Migration logs | Protected |
| Uptime | `/health` check |
| Alerting | Deferred but planned |
| Reports | No secrets/tokens in operator reports |
| Audit cadence | Manual monthly audit until automation exists |

---

## 13. Backup / rollback

| Item | Requirement |
|------|-------------|
| Code | Rollback by Git hash / release symlink |
| DB | Dump **before** migration; retention policy operator-decided |
| Storage | Backup export artifacts before first real client delivery |
| Restore drill | Required before trusting production |
| Shares on rollback | If delivery broken: revoke active shares and/or pause share creation |

---

## 14. Deployment strategy options

| Method | Notes |
|--------|-------|
| Git-based deploy | Pin commit; release dirs; preferred for auditability |
| SFTP exact sync | Allowed if allowlisted paths only; high human-error risk |
| Release archive | Hash-named archive + shared env/storage |

Rules common to all:

- No secrets in Git
- Migrate only after backup
- No broad sync of local fixture DB
- Model A remains: versioned source in Active Brain; production is a deploy target, not a second SoT repo by default

---

## 15. Security posture

- HTTPS only for production client delivery
- `APP_ENV=production`; debug off; `display_errors` off
- Secure session cookies
- Auth-required internal routes
- CSRF for write actions
- Path traversal prevention for artifact download/stream
- Artifact checksum validation
- `X-Content-Type-Options: nosniff`
- noindex/nofollow for public shares
- Least-privilege DB user
- Minimal public surface (PDF stream route only for unauthenticated clients)

---

## 16. Separation from local dev

| Local | Production |
|-------|------------|
| `iseo-report-hub.test` HTTP | Operator domain HTTPS |
| `iseo_report_hub_dev` | Dedicated prod DB |
| `.env.local` on Localhost | `.env.production` outside Git |
| Fixture `LOCAL_FIXTURE_ONLY` | Real or approved pilot data only |
| Laragon workstation | VPS (recommended) or other Decision 01 choice |

Never treat local PASS gates A–D as waiver of environment requirements.

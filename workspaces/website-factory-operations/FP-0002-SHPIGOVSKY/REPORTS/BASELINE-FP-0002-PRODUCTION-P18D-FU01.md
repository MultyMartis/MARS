# BASELINE — FP-0002 PRODUCTION P18D-FU01

**Baseline ID:** `FP-0002-PROD-BASELINE-2026-08-19-P18D-FU01`  
**Established:** 2026-08-19  
**Wave:** `PROD-P18D-FU01 SMTP Closeout + Olya Intake`  
**Evidence:** `REPORTS/evidence/prod-p18d-fu01-smtp-closeout/`

## Current runtime truth

| Field | Value |
|-------|-------|
| Live domain | `https://shpigovsky.ru` |
| Public apex | WordPress currently visible |
| Working host | `http://shpigovsky.beget.tech/` redirects to live domain |
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| WordPress | 7.0.4 |
| SMTP state | **VERIFIED / ACTIVE** |
| SMTP host | `smtp.beget.com` |
| SMTP port | `465` |
| SMTP encryption | `ssl` |
| SMTP auth | yes |
| Sender | `noreply@shpigovsky.ru` |
| Recipient count | `2` |
| Recipient labels | `Андрей Русецкий`, `Ольга Дягилева` |
| Password | configured, hidden |
| Temporary suppression MU | **physically removed** |
| `pre_wp_mail` blocker | none |
| Lead registry | `fp02_form_leads` ACTIVE |
| Lead retention | `0` days, operator decision still required |
| Indexing | **CLOSED** |
| `robots.txt` | `Disallow: /` with sitemap on live domain |

## Authority split

| Surface | Authority |
|---------|-----------|
| Production filesystem (`theme`, `shpigovsky-core`, runtime files) | **LIVE RUNTIME TRUTH** after fresh intake and exact parity check |
| Production database content/settings edited via normal WordPress Admin | **LIVE EDITORIAL / ADMIN TRUTH** |
| MARS Git `WORDPRESS/` | **CODE AUTHORITY** after drift intake and canonization |

Editorial/Admin changes are acknowledged in this baseline but are **not** frozen into Git as DB payload.  
Old backups remain rollback artifacts, not the source of current editorial truth.

## Olya/Admin intake

- Recent `admin` edits on 2026-08-16..2026-08-18 affected pages, services, specialists, and legal pages.
- These are treated as legitimate editorial/Admin production truth and were preserved.
- Recent SMTP recipient/settings changes are technical/Admin state, not content drift.
- One `indexing_opened` event on 2026-08-19 was detected in Activity Log; FU01 re-closed indexing per current launch gate.

## Source / production parity

Verified source-owned file reality before closeout:

- `MailOps.php` — MATCH
- `SmtpTransport.php` — MATCH
- `ConsultationHandler.php` — MATCH
- `ActivityLog.php` — MATCH
- `LeadRegistry.php` — MATCH
- `SystemDashboard.php` — stale before FU01 sync
- `shpigovsky-core.php` — stale before FU01 sync
- `fp02-pre-cutover-mail-suppression.php` — existed in runtime, now removed

## Validation lifecycle

- `WORDPRESS/validation/p18d-smtp-correct-and-verify.php` — source-only controlled validation tool
- `WORDPRESS/validation/p18d-activate-delivery.php` — source-only controlled validation tool
- `WORDPRESS/validation/p18d-form-qa.php` — source-only controlled validation / QA tool
- `WORDPRESS/validation/p18d-retire-suppression-mu.php` — source-only controlled readiness tool

These tools are **not** part of the public webroot baseline and must stay execution-scoped only.

## Open tails

1. Public-domain finalization only if operator observes a routing regression.
2. Olya approval before re-opening indexing.
3. Sitemap submissions after indexing opens.
4. Final crawl after sitemap submission.
5. Lead retention period remains an operator business decision.

## Historical note

`REPORTS/REPORT-FP-0002-PROD-P18D-SMTP-VERIFICATION.md` remains historical.  
FU01 supersedes its assumptions about current runtime, MU status, public apex visibility, and editorial/Admin intake.

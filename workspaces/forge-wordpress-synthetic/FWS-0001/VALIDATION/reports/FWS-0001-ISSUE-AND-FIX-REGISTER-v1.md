# FWS-0001 — Issue and Fix Register v1

**Document type:** Issue and fix register  
**Version:** v1  
**Case:** FWS-0001  
**Maintained:** FW-05 (static) → FW-05R (live)

---

## FW-05 — Static synthetic validation (2026-06-22)

| ID | Issue | Severity | Status | Fix / disposition |
|----|-------|----------|--------|-------------------|
| IF-05-01 | PHPCS/php -l not executed on host | Medium | **Closed (FW-05R)** | Live pass — 24/24 syntax PASS |
| IF-05-02 | Live WordPress render not captured | Medium | **Closed (FW-05R)** | 12 reference + 12 rendered screenshots |
| IF-05-03 | Runtime plugin activation not verified | Medium | **Closed (FW-05R)** | fws-synthetic-core active on MLI |
| IF-05-04 | ACF Pro not available | Low | **Open (accepted)** | ACF Free 6.8.4 + Settings API deviation |
| IF-05-05 | Visual diff NOT EXECUTED | Medium | **Closed (FW-05R)** | PASS WITH DOCUMENTED DEVIATIONS |
| IF-05-06 | No live wp-admin walkthrough | Low | **Partial** | Admin reachability PASS; U-03 not executed |
| IF-05-07 | Playground population incomplete | Medium | **Partial** | Manual WP-CLI worked; script fix pending |

---

## FW-05R — Live synthetic validation (2026-06-23)

| ID | Issue | Severity | Status | Fix / disposition |
|----|-------|----------|--------|-------------------|
| IF-05R-01 | `fws-0001.test` not in hosts file | Low | **Open** | HTTP 200 via Host header / Playwright resolver; operator elevation pending |
| IF-05R-02 | PHPCS 6 errors, 9 warnings post-phpcbf | Low | **Open (accepted)** | File comment style, template var false positives, minified asset warnings |
| IF-05R-03 | Populate script options JSON | Medium | **Open** | `mars-runtime/scripts/populate-fws-0001.ps1` — manual wp population succeeded |
| IF-05R-04 | WV6 operator visual approval | Medium | **Open** | Automated parity PASS WITH DEVIATIONS; operator sign-off PENDING |
| IF-05R-05 | Full wp-admin field-order walkthrough | Low | **Open** | Deferred to operator if required for FW-06 |
| IF-05R-06 | Lighthouse / axe not run | Low | **Open (accepted)** | Out of FW-05R synthetic scope |
| IF-05R-07 | RC2 zip packaging | Medium | **Pending** | Pre-handoff simulation v2 created; zip run pending |
| IF-05R-08 | AG-WP-001 registry promotion | Info | **Open** | ELIGIBLE WITH DOCUMENTED LIMITATIONS — charter still required |

---

## Fix log

| Date | ID | Action |
|------|-----|--------|
| 2026-06-23 | IF-05R-02 | CRLF fixed via phpcbf |
| 2026-06-23 | IF-05-01 | php -l 24/24 PASS |
| 2026-06-23 | MLI | `mysqlx=0` — port 33060 closed |
| 2026-06-23 | IF-05-02, IF-05-05 | Screenshot pairs captured |

---

*Issue and fix register v1 — FWS-0001.*

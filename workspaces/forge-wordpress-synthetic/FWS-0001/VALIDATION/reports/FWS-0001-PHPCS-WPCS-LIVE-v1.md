# FWS-0001 — PHPCS / WPCS Live Validation v1

**Document type:** PHPCS validation report  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-05R  
**Runtime:** MLI-WP-SYN-001  
**Git checkpoint:** commit `4a46267` on `mars/post-cycle8-live-tests`

---

## Scope

Theme `fws-synthetic` and plugin `fws-synthetic-core` — WordPress Coding Standards profile (MLI PHPCS toolchain).

---

## Summary

| Metric | Before phpcbf | After phpcbf |
|--------|---------------|--------------|
| Errors | — | **6** |
| Warnings | — | **9** |
| CRLF line endings | Present | **Fixed** via `phpcbf` |

---

## Remaining findings (post phpcbf)

| Category | Count | Severity | Notes |
|----------|-------|----------|-------|
| File comment style on `index.php` | 1 | Error | WPCS file header expectation |
| Template-parts variable naming | Several | Error | Documented false positives on template variables |
| Minified CSS/JS in theme assets | Several | Warning | Vendor/minified bundles excluded from manual fix scope |
| Meta query coding style | Several | Warning | Non-blocking WPCS suggestions |

---

## Assessment

| Check | Result |
|-------|--------|
| Blocking security patterns (eval, unsanitized output) | **None detected in PHPCS security-relevant rules** |
| Auto-fixable style (CRLF) | **Resolved** |
| Residual errors | **Documented** — no runtime impact proven |

---

## Verdict

**PASS WITH DOCUMENTED LIMITATIONS** — residual PHPCS errors are style/naming false positives and minified asset warnings; not treated as FW-05R blockers.

---

## Related

- [FWS-0001-PHP-SYNTAX-LIVE-v1.md](FWS-0001-PHP-SYNTAX-LIVE-v1.md)
- [FWS-0001-ISSUE-AND-FIX-REGISTER-v1.md](FWS-0001-ISSUE-AND-FIX-REGISTER-v1.md)

---

*PHPCS WPCS live validation v1 — FWS-0001.*

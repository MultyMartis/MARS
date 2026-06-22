# Forge WordPress FW-05R — Live Synthetic Validation Report v1

**Document type:** Capability evaluation (live)  
**Version:** v1  
**Date:** 2026-06-23  
**Case:** FWS-0001  
**Stage:** FW-05R  
**Overall outcome:** **PROVEN WITH LIMITATIONS**

---

## Executive summary

FW-05R executed Forge theme/plugin install, ACF compatibility, content population, code quality, functional, visual, and validator suite on MLI-WP-SYN-001 live runtime. Core capability chain is proven; operator WV6 and hosts elevation remain documented limitations.

**Git checkpoint:** commit `4a46267` on `mars/post-cycle8-live-tests`

---

## Capability evaluation (live)

| Capability area | Result | Evidence |
|-----------------|--------|----------|
| Local runtime install | **PROVEN** | MLI-WP-SYN-001, theme + plugin active |
| PHP syntax | **PROVEN** | 24/24 PASS |
| PHPCS / WPCS | **PROVEN WITH LIMITATIONS** | 6 errors, 9 warnings post-phpcbf |
| WordPress correctness | **PROVEN** | CPT, templates, routes HTTP 200 |
| ACF workflow | **PROVEN WITH LIMITATIONS** | ACF Free 6.8.4, 3 field groups |
| Functional smoke | **PROVEN WITH LIMITATIONS** | Manual population; script gap |
| Security | **PROVEN WITH LIMITATIONS** | No blocking code findings |
| Visual parity | **PROVEN WITH LIMITATIONS** | 12 pairs; WV6 PENDING |
| Admin UX | **PROVEN WITH LIMITATIONS** | Reachability PASS |
| Validators FW-V-01–07 | **PROVEN WITH LIMITATIONS** | Live reports complete |
| Packaging RC2 | **PROVEN** | FWS-0001-RC2 zips + validation evidence |
| FP-0002 isolation | **PROVEN** | Untouched |

---

## Infrastructure alignment

| Check | Result |
|-------|--------|
| MySQL 127.0.0.1:3306 | **PASS** |
| `wp db check` | **PASS** |
| MySQL X Protocol 33060 | **HARDENED** (`mysqlx=0`) |
| Hosts `fws-0001.test` | **PENDING** — Host header workaround used |

---

## Execution summary

| Step | Status |
|------|--------|
| Pre-install backup | COMPLETE |
| Theme/plugin/ACF install | COMPLETE |
| Content population | COMPLETE (manual wp) |
| PHP syntax | PASS |
| PHPCS | PASS WITH LIMITATIONS |
| Route smoke | PASS |
| Visual comparison | PASS WITH DEVIATIONS |
| Validator suite | COMPLETE |
| RC2 zip | COMPLETE |
| WV6 operator gate | PENDING |

---

## Next authorized stage

**FW-06 — Pilot Intake** (after operator WV6 if required by charter)

---

## Post-validation closure (2026-06-23 checkpoint)

Additive records — historical results above unchanged.

| Closure item | Result |
|--------------|--------|
| Direct domain gate | **NOT CLOSED** — hosts elevation blocked from Cursor (exit 3) |
| Direct URL smoke | **NOT EXECUTED** |
| Host-header supplementary smoke | **PASS** — all core routes HTTP 200 |
| Playwright without resolver | **NOT EXECUTED** |
| Operator WV6 | **PENDING** |
| Synthetic source Git persistence | **DECIDED** — narrow whitelist |
| Git checkpoint | This closure task |

See [FORGE-WORDPRESS-FW-05R-DIRECT-DOMAIN-CLOSURE-v1.md](FORGE-WORDPRESS-FW-05R-DIRECT-DOMAIN-CLOSURE-v1.md), [FORGE-WORDPRESS-FW-05R-OPERATOR-WV6-REVIEW-PACKAGE-v1.md](FORGE-WORDPRESS-FW-05R-OPERATOR-WV6-REVIEW-PACKAGE-v1.md), [FORGE-WORDPRESS-FWS-0001-SOURCE-PERSISTENCE-DECISION-v1.md](FORGE-WORDPRESS-FWS-0001-SOURCE-PERSISTENCE-DECISION-v1.md).

---

## Final status (checkpoint)

```text
FW-05R — COMPLETE
Capability — PROVEN WITH LIMITATIONS
Direct local domain — PENDING HOSTS ELEVATION (not PASS)
Operator WV6 — PENDING
ACF Pro — NOT PROVEN
AG-WP-001 formal registration — NOT PERFORMED
FW-06 — AUTHORIZED BUT WAITING FOR APPROVED CLIENT FRONTEND
FP-0002 — NOT READY
```

---

## Related

- [FORGE-WORDPRESS-FW-05-SYNTHETIC-VALIDATION-REPORT-v1.md](FORGE-WORDPRESS-FW-05-SYNTHETIC-VALIDATION-REPORT-v1.md)
- [FORGE-WORDPRESS-FW-05R-PRE-INSTALL-BASELINE-v1.md](FORGE-WORDPRESS-FW-05R-PRE-INSTALL-BASELINE-v1.md)
- [FORGE-WORDPRESS-FW-05R-DIRECT-DOMAIN-CLOSURE-v1.md](FORGE-WORDPRESS-FW-05R-DIRECT-DOMAIN-CLOSURE-v1.md)
- [FORGE-WORDPRESS-POST-FW-05R-PILOT-WAIT-STATE-v1.md](../../reports/FORGE-WORDPRESS-POST-FW-05R-PILOT-WAIT-STATE-v1.md)
- Workspace: `workspaces/forge-wordpress-synthetic/FWS-0001/`

---

*FW-05R live synthetic validation report v1.*

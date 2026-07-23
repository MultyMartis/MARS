# ISEO-SU-SITE-OPS SAFE UNKNOWN Register v1

**Status:** ACCEPTED; **updated Phase 2B** 2026-07-24  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

Rule: do **not** invent values. Resolve only with evidence.

## Phase links

| Artifact | Path |
|----------|------|
| Read-only production audit | [ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md](ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md) |
| Boundary map | [ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md](ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md) |
| WordPress inventory | [ISEO-SU-WORDPRESS-INVENTORY-v1.md](ISEO-SU-WORDPRESS-INVENTORY-v1.md) |

---

## Resolved or updated in Phase 2B

| ID | Item | Outcome | Classification |
|----|------|---------|----------------|
| U-002 | Beget panel URL | Local profile host `cp.beget.com` | CONFIRMED BY LOCAL PROFILE (non-secret host) |
| U-003 | Docroot | `…/i-seo.su/public_html` (account redacted) | CONFIRMED BY SFTP |
| U-004 | WordPress physical path | Same as docroot (root install) | CONFIRMED BY SFTP |
| U-005 | Static / WP routing | Hybrid: physical HTML + WP rewrite; HTML executed as PHP | CONFIRMED BY SANITIZED EVIDENCE |
| U-006 | WordPress version | 7.0.2 | CONFIRMED BY SFTP + public generator |
| U-008 | Theme / child | `iseoblog` only; not child | CONFIRMED BY SFTP |
| U-009 | Plugins | Inventory captured from filesystem (+ Yoast/Jetpack REST live) | CONFIRMED BY SFTP / PARTIAL active-state |
| U-011 | CPT | `offer` registered in theme | CONFIRMED BY SFTP |
| U-012 | Header / footer ownership | Dual: static HTML embeds + WP theme parts; home via WP template | CONFIRMED BY SANITIZED EVIDENCE |
| U-013 | Tariff cards | Present (static + theme + forms) | CONFIRMED BY SANITIZED EVIDENCE |
| U-014 | Calculator | Present (`js/common.js`, `calc__FORM.php`, WP tariff page) | CONFIRMED BY SANITIZED EVIDENCE |
| U-016 | Forms | Multiple `*__FORM.php` handlers | CONFIRMED BY SFTP |
| U-021 | Staging | Absent | CONFIRMED BY OPERATOR (unchanged) |
| U-024 | FTP/SFTP model | SFTP port 22 to docroot | CONFIRMED BY AUDIT |
| — | WPilot on production | Absent | CONFIRMED BY SFTP |

---

## Still open / deferred

| ID | Item | Classification | Risk | Evidence needed | Earliest phase |
|----|------|----------------|------|-----------------|----------------|
| U-007 | PHP **runtime** version | SAFE UNKNOWN | Compatibility planning | Browser Admin Site Health or hosting panel | 2C / 4B HITL |
| U-009b | Exact plugin active/inactive matrix | SAFE UNKNOWN | Wrong conflict assumptions | Browser Admin plugins screen | 2C / 4B |
| U-010 | ACF field groups / options | SAFE UNKNOWN | Wrong field SoT | Admin ACF UI or export | 3 / 2C |
| U-015 | Web-KP exact URL/tool | SAFE UNKNOWN | Tool breakage | Operator confirms whether `/offers`+CPT `offer` is web-KP | 2C HITL |
| U-017 | Mail delivery path (SMTP vs mail()) | SAFE UNKNOWN | Silent form failure | Handler review under charter / mail plugin settings | 3 |
| U-018 | Integrations beyond Jetpack/Yoast | SAFE UNKNOWN | Side effects | Inventory pass | 3 |
| U-019 | Cache/CDN/WAF edge details | PARTIAL (Jetpack WAF dir; WP-Optimize present) | False smoke | Panel/CDN attestation | 3–6 |
| U-020 | Restore method details | SAFE UNKNOWN | Irrecoverable change | Restore drill notes | 3–4 |
| U-022 | Maintained canonical source outside production | SAFE UNKNOWN | Wrong sync | Operator attestation | 3 |
| U-023 | Manual production drift inventory | PARTIAL (dual home/blog files known) | Overwrite | Ongoing drift log | 3–7 |
| U-025 | WPilot production compatibility | **PARTIAL → CONDITIONAL GO** (Phase 4B static review) | Failed install | Operator accept 4B-1..4B-3; then 6A | 4B COMPLETE / 6A |
| U-026 | WPilot endpoint inventory for this site | **DOCUMENTED FROM SOURCE** (routes known); production behavior SAFE UNKNOWN | Wrong smoke | GATE 6D | 6D |
| U-027 | Rollback implementation proof | SAFE UNKNOWN (plugin rollback proven on DEV only) | Unrecoverable write | Restore evidence + optional 6E | 4–6 |
| U-028 | WPilot token format for production | **PATH DECIDED** (`wpilot-prod-iseo-su.token`); file **NOT CREATED** | Secret leakage | GATE 6C | 6C |
| U-035 | PHP syntax lint of WPilot package on agent host | SAFE UNKNOWN (`php` binary unavailable) | Missed parse error | Lint on machine with PHP, or rely on DEV proven package | 4C optional |
| U-036 | `X-WPilot-Token` header forwarding on i-seo.su | SAFE UNKNOWN | Auth smoke failure | GATE 6D | 6D |
| U-037 | WPilot uninstall residual tables/options | SAFE UNKNOWN (no uninstall.php) | Orphan DB objects | Document on future uninstall charter | later |
| U-029 | Backup evidence Storage paths | SAFE UNKNOWN | Misplaced artefacts | Policy when authorized | 4–6 |
| U-030 | ATLAS mint | DEFERRED | Duplicate identity | Separate charter | later |
| U-031 | Local mirror need | NOT DECIDED | Wasted/risky copy | Phase 5 | 5 |
| U-032 | Firefox Browser Workstation | DEFERRED | Session leakage | Future charter | deferred |
| U-033 | Menus / widgets contents | SAFE UNKNOWN | Nav regression | Browser Admin | 2C / 3 |
| U-034 | Whether `.html` files use PHP includes for shared partials | SAFE UNKNOWN | Partial edit misses includes | Bounded PHP read charter | 2C / 3 |

---

## Summary

Phase 2B resolved the hybrid architecture, docroot, WP root install, version, theme, plugin filesystem inventory, calculator/tariffs/forms presence, and WPilot absence.  

Phase 4B completed static package + source compatibility review: **ACCEPTED MATCH** RC5 package; **CONDITIONAL GO** pre-install.  

Remaining gaps are mainly **Admin-UI-only facts** (PHP runtime, plugin actives, ACF UI, menus), **web-KP naming**, header/WAF smoke, restore drill, plus long-standing SoT items.

---

*SAFE UNKNOWN Register v1 · updated 2026-07-24 Phase 4B.*

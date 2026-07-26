# REPORT — METALLKA SITE OPS PHASE 2A READ-ONLY DISCOVERY CHARTER



**Programme:** METALLKA-RU-SITE-OPS  

**Task:** PHASE 2A — READ-ONLY DISCOVERY CHARTER PREPARATION  

**Date:** 2026-07-25  

**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  

**Status:** **COMPLETE — READ-ONLY DISCOVERY CHARTER PREPARED**



---



## Status



Phase 2A documentation package prepared. Production remains **NOT CONNECTED**. Gate A is **NOT APPROVED**. Phase 2B does **not** auto-start.



```text

THIS PHASE DOES NOT AUTHORIZE ACCESS.

```



---



## Environment



| Check | Result |

|-------|--------|

| cwd | `X:\AI MARS` |

| Volume X: | **AI WS** |

| Branch | `mars/canonical-post-recovery` |

| HEAD | `b546e3e299606075d27c4364c676f8abf3896f7f` |

| Staged index | **Empty** (unchanged) |

| Foreign WIP | Present elsewhere — **not touched** |



---



## Files Created



| File |

|------|

| `projects/metallka-ru-site-ops/METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md` |

| `projects/metallka-ru-site-ops/METALLKA-READ-ONLY-DISCOVERY-PLAN-v1.md` |

| `projects/metallka-ru-site-ops/METALLKA-ACCESS-INTAKE-REQUIREMENTS-v1.md` |

| `projects/metallka-ru-site-ops/METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md` |

| `projects/metallka-ru-site-ops/METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md` |

| `projects/metallka-ru-site-ops/reports/REPORT-METALLKA-SITE-OPS-PHASE-2A-READ-ONLY-DISCOVERY-CHARTER.md` |



---



## Files Modified



| File |

|------|

| `projects/metallka-ru-site-ops/OPERATIONAL-INDEX.md` |

| `projects/metallka-ru-site-ops/METALLKA-ARTIFACT-REGISTER-v1.md` |



No other programme or sibling files modified.



---



## Future Read Scope



After Gate A approval only — stages **R0–R12** (public surface → hosting → WP core → themes → plugins → WPBakery pages → The7 ownership → nav/forms → ACF → custom code → cache → backup/restore model → WPilot compatibility inspection).



Allowed future classes (when approved): public HTTP · WP Admin read-only · hosting metadata read-only · SFTP/FTP read-only · DB metadata only if separately authorized · WPilot presence inspection only (no REST).



---



## Explicitly Forbidden Scope



File upload/edit · plugin install/activation · theme/plugin updates · option/DB writes · WPilot token/bridge/REST smoke · write enable · cache purge · backup creation that mutates production (unless separately approved) · local mirror import · account changes · credentials in chat · secret files in Phase 2A · ATLAS/registry mutation · WPilot/ISEO/Forge/FP-0002 mutation.



---



## Evidence Rules



Allowed: versions, plugin/theme names, sanitized paths, hashes, non-secret screenshots, page IDs, templates, HTTP status/headers, sanitized excerpts, inventories.



Must redact: passwords, FTP/SFTP creds, tokens/hashes, cookies, session IDs, salts, API keys, SMTP/DB passwords, private keys, webhook secrets, unnecessary PII, wp-config secrets, unsanitized sensitive logs.



**REPORT must never contain secret material.**



---



## STOP Conditions



Twenty mandatory STOPs including: missing approval · identity/credential uncertainty · mutation prompts · write-only surfaces · security disable / plugin update requests · ambiguous docroot · multi-copy / staging ambiguity · source authority conflict · secret exposure · 5xx / fatals · DB inconsistency · ownership ambiguity · read-triggers-mutation · WAF/rate-limit · unknown deploy · ghost WPilot.



**Do not fix while discovering.**



---



## Gate A Definition



```text

APPROVE METALLKA GATE A — PRODUCTION READ-ONLY DISCOVERY

```



Project-local convention. Authorizes only the accepted read-only charter scope. Does **not** authorize writes, install, activation, token, bridge, smoke, backup creation, or cache purge.



---



## Required Operator Input



Non-secret confirmations only (no credentials):



1. Hosting provider.  

2. Whether operator has hosting panel access.  

3. Whether WP Admin access exists.  

4. Whether FTP or SFTP access exists.  

5. Whether there is known staging/dev.  

6. Whether a hosting backup can be created/restored.  

7. Whether source/Git/theme archive exists outside production.  

8. Whether operator authorizes Gate A later.



Credentials via approved local secret workflow later — **not** in chat.



---



## Next Phase



**GATE A operator decision** → **PHASE 2B** production read-only discovery.



Phase 2B must **not** start automatically.



---



## Files Changed



Created: 6 files under `projects/metallka-ru-site-ops/` (5 charters/plans + this report).  

Modified: `OPERATIONAL-INDEX.md`, `METALLKA-ARTIFACT-REGISTER-v1.md`.



---



## Git Operations



| Operation | Status |

|-----------|--------|

| Staging | **None** |

| Commit | **None** |

| Push | **None** |



---



## Risks



| Risk | Mitigation |

|------|------------|

| Operator treats Phase 2A as access approval | Charter §0 explicit non-authorization |

| Phase 2B auto-start | OPERATIONAL-INDEX + charter forbid auto-start |

| Secret paste into chat | Intake + evidence rules forbid |

| Analogy fill from ISEO/triumph | SAFE UNKNOWN + transfer bans retained |

| Foreign WIP contamination | Scope limited to metallka locus; no broad staging |



---



## Stop Condition



**COMPLETE — READ-ONLY DISCOVERY CHARTER PREPARED**



STOP after this REPORT. Do not request credentials. Do not begin Phase 2B.



---



## Validation (Phase 2A)



| Check | Result |

|-------|--------|

| No external requests | **PASS** |

| No secrets | **PASS** |

| No local secret files created | **PASS** |

| No production contact | **PASS** |

| No WPilot operations | **PASS** |

| No ATLAS changes | **PASS** |

| No local mirror | **PASS** |

| No backup triggered | **PASS** |

| No cache changes | **PASS** |

| Only allowed project files changed | **PASS** |

| Staged index unchanged | **PASS** |

| Charter says preparation ≠ access | **PASS** |

| Phase 2B does not auto-start | **PASS** |



---



*REPORT · METALLKA SITE OPS Phase 2A · 2026-07-25 · no secrets · no access.*



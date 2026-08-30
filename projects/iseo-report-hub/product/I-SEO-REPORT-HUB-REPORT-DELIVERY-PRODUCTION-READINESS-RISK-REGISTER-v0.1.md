# I-SEO Report Hub — Report Delivery Production Readiness Risk Register v0.1

**Status:** POLICY / RISK REGISTER ONLY — no remediation implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Report Delivery Production Readiness Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md)

---

## Severity / likelihood scale

| Level | Severity | Likelihood |
|-------|----------|------------|
| High | Client data exposure, irreversible data loss, security bypass | Probable without controls |
| Medium | Broken delivery, operational failure, compliance/process gap | Possible |
| Low | Nuisance, debt, incomplete UX | Unlikely or limited blast radius |

---

## Risk register

| ID | Risk | Severity | Likelihood | Mitigation | Readiness gate |
|----|------|----------|------------|------------|----------------|
| R01 | Local-only runtime mistaken as production | High | Medium | Explicit non-production facts; Environment Charter before deploy; never call Localhost “prod” | E |
| R02 | Fixture / `LOCAL_FIXTURE_ONLY` data sent to real client | High | Medium | Segregate fixtures; Gate K before any external share on prod domain; handoff checklist | K, D |
| R03 | No production HTTPS / domain — share links unusable or intercepted | High | High (if forced early) | HTTPS mandatory; stable domain; forbid public share over plain HTTP in prod | E, C |
| R04 | Token URL exposure in webserver/app logs | High | Medium | Avoid logging full share URL; treat access logs as sensitive; redact in evidence | C, J |
| R05 | No backup / restore test before migration or deploy | High | Medium | Pre-deploy dump; storage backup; restore drill attested | H, G |
| R06 | No production DB secret / least-privilege policy | High | Medium | Secrets outside Git; least-privilege DB user; rotate from local root habits | F, G |
| R07 | PDF generation (Edge headless) incompatible on hosting | Medium | Medium | Probe PDF path on chosen host in Environment Charter; fallback policy | E, B |
| R08 | Storage path / public webroot misconfiguration exposes artifacts | High | Medium | Docroot=`public/` only; storage/logs/artifacts outside; path traversal tests | E, B, C |
| R09 | Revoked share row accumulation without retention policy | Low | High (over time) | Retention/pruning charter; no ad-hoc delete of audit rows | L |
| R10 | No delivery events (DB-11) — weak delivery audit trail | Medium | Medium | Manual process + share access_count; open DB-11 only if operator requires | M, J |
| R11 | No email / portal — operators paste URLs manually (error/leak risk) | Medium | Medium | Handoff copy pack; once URL; revoke+recreate; training | D, N |
| R12 | Insufficient monitoring / logging — silent outages or abuse | Medium | Medium | `/health`; error/access logs; monthly manual audit | J |
| R13 | Manual deployment error (wrong sync, wrong `.env`, wrong DB) | High | Medium | Deploy checklist; dry-run; backup; exact allowlist sync; STOP conditions | E, F, G, H |
| R14 | Broad Git / foreign WIP risk during release ops | Medium | Medium | Exact-path staging; clean worktree/runtime-checkouts; no `git add .` | Process (MARS git model) |
| R15 | Real client data import mistakes (wrong client, wrong period, wrong PDF) | High | Medium | Import charter; dual-check; readiness panel; revoke on error | K, D, A |

---

## Highest severity themes

1. **Environment / HTTPS / secrets** (R01, R03, R06, R08) — do not deploy until Environment + Secrets gates pass.
2. **Data authenticity** (R02, R15) — fixture segregation and real-client import discipline.
3. **Recoverability** (R05, R13) — backup/restore and careful deploy procedure.
4. **Token privacy** (R04) — log hygiene for share URLs.

---

## Explicit non-mitigations in this wave

This charter does **not** implement mitigations in code/runtime/DB. It only registers risks and maps them to gates for subsequent operator-approved waves.

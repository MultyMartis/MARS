# REPORT — ISEO-SU SITE OPS PHASE 2A WAVE A REVIEW AND LOCAL ACCESS BOOTSTRAP

**Task ID:** ISEO-SU-SITE-OPS-PHASE-2A-WAVE-A-REVIEW-AND-LOCAL-ACCESS-BOOTSTRAP  
**Date:** 2026-07-22  
**Final status:** **PHASE 2A — COMPLETE / AWAITING OPERATOR LOCAL ACCESS ENTRY**  
**Production connection:** NOT AUTHORIZED  

---

## 1. Execution Summary

Wave A operator evidence was accepted and persisted in the programme locus. WordPress Admin URL was correctly classified as WordPress administration (not Beget panel). Canonical local-access pattern was derived from WPilot local-storage policy + OCPilot SITE-002 secret separation + ROL credential boundaries. Empty local-only templates were created under `X:\AI MARS\local\sites\iseo-su-production\` with proven Git ignore. No production, browser, Beget, WordPress, FTP/SFTP, Storage, Localhost, registry, ATLAS, or Git stage/commit/push actions were performed.

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (full) | `e02f90fef0697bb7a8c9280eca59c4abfa71ceae` |
| HEAD (short) | `e02f90fe` |
| Upstream | `origin/mars/canonical-post-recovery` |
| Ahead / behind (local knowledge) | ahead **11** / behind **52** vs origin |
| Staged diff | **empty** |
| Foreign WIP | **Present** — preserved (Forge/OCPilot/workspace noise and `.recovery-temp` untracked material outside this locus) |

Read before writes: AGENTS.md, `.cursorrules`, X-drive authority, infrastructure reality, programme OPERATIONAL-INDEX, access classification, evidence intake, non-secret evidence request, redaction guide.

---

## 3. Wave A Evidence Accepted

| Fact | Classification |
|------|----------------|
| Site `https://i-seo.su/` | CONFIRMED BY OPERATOR |
| Hosting provider Beget | CONFIRMED BY OPERATOR |
| WordPress Admin URL `https://i-seo.su/wp-admin/` | CONFIRMED BY OPERATOR |
| Hosting access exists | CONFIRMED BY OPERATOR |
| FTP or SFTP access exists | CONFIRMED BY OPERATOR |
| WordPress administrator access exists | CONFIRMED BY OPERATOR |
| Staging / DEV does not exist | CONFIRMED BY OPERATOR |
| Work will be on production after future authorization | CONFIRMED BY OPERATOR |
| Full Beget backup intended before every future task/work package | CONFIRMED BY OPERATOR |
| Production runtime is the only confirmed source location | CONFIRMED BY OPERATOR |
| Contributors: Andrey / Anton / Nikita (roles as stated) | CONFIRMED BY OPERATOR |
| No permanently untouchable zone declared | CONFIRMED BY OPERATOR (does **not** authorize broad mutation) |

---

## 4. Corrections and Classifications

1. **`https://i-seo.su/wp-admin/` = WordPress Admin** — not Beget control panel.  
2. **Beget control-panel URL = SAFE UNKNOWN** until operator identifies it in local files.  
3. Exact protocol/host/port/username/password = SAFE UNKNOWN until local-only fill (values never enter this REPORT).  
4. Maintained canonical local/Git source outside production = SAFE UNKNOWN (do not claim no local copies exist).  
5. Architecture static/WordPress split = SAFE UNKNOWN pending later authorized read-only audit.  
6. Operator Beget backup rule does **not** remove need for exact task scope, scoped backup, validation, rollback, HITL, evidence.  
7. All site surfaces remain protected from mutation until separately chartered.

---

## 5. Canonical Access Pattern Research

| Source | Finding used |
|--------|----------------|
| WPilot `local-storage-policy.md` | Local roots `local\sites\` and `local\tokens\`; ignore `/local/` |
| WPilot `sites.example.json` | Non-secret metadata + path references |
| WPilot DEV references (`dev.gktriumph.ru`, `wpilot-dev-gktriumph.token`) | Token stays in separate `local\tokens\` file; not created for i-seo.su now |
| OCPilot SITE-002 access brief / production profile | Tracked docs = capability + path refs only; secrets external |
| OCPilot SITE-002 secrets practice | Empty operator-fill sections; registration ≠ connection |
| ROL | Credentials operator-managed; never into chat |
| Root `.gitignore` | `/local/` proven via `git check-ignore` |

**Selected model:** site alias `iseo-su-production` under `X:\AI MARS\local\sites\iseo-su-production\` with:

- non-secret `site-profile.json`;
- secrets `secrets.local.md` (empty template);
- reserved future token path documented only (file **not** created).

Storage secrets path was **not** used (Storage writes not authorized). No conflicting `local\sites\iseo-su-production` path existed before creation.

---

## 6. Local Files Created

Paths only (contents **not** printed here):

1. `X:\AI MARS\local\sites\iseo-su-production\site-profile.json`  
2. `X:\AI MARS\local\sites\iseo-su-production\secrets.local.md`  

No real secret values were inserted. No WPilot token file created. No Windows ACL procedure found in MARS sources for this case — ACL not applied.

---

## 7. Operator Fill Instructions

See Russian operator guide:

[ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md](../ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md)

Summary: open the two local paths above; fill Beget / FTP|SFTP / WordPress fields in `secrets.local.md`; leave unknowns empty; never paste secrets into chat; reply only `ACCESS FILES FILLED` plus which classes are populated.

---

## 8. Dedicated WordPress Account Recommendation

A separate WordPress administrator account for MARS is **RECOMMENDED**.  
It must **not** be created in this task. Future HITL requirements: unique username/password, administrator only if required, operator-controlled recovery email, no shared personal account, audit-friendly display name, remove/downgrade when unused. Final username not prescribed.

---

## 9. Project Documents Updated

Under `projects/iseo-su-site-ops/` only:

| Document | Action |
|----------|--------|
| `ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md` | Updated — Wave A accepted |
| `ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md` | Updated — root route R-001 INTAKE |
| `ISEO-SU-ACCESS-CLASSIFICATION-v1.md` | Updated — capability vs A3–A8 NOT AUTHORIZED |
| `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md` | Updated — resolved/remaining unknowns |
| `ISEO-SU-LOCAL-ACCESS-MODEL-v1.md` | Created |
| `ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md` | Created |
| `OPERATIONAL-INDEX.md` | Updated after validation |
| `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md` | Updated — new artifacts |
| `reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2A-WAVE-A-REVIEW-AND-LOCAL-ACCESS-BOOTSTRAP.md` | This file |

---

## 10. Git Ignore and Secret Safety

| Check | Result |
|-------|--------|
| `.gitignore` rule | `/local/` |
| `git check-ignore` for created local paths | **Matched** (ignored) |
| Secrets in tracked docs / this REPORT | **None** |
| Real secret values written by this task | **None** |
| `.gitignore` modification | **Not required / not performed** |

---

## 11. Validation

| # | Check | Result |
|---|-------|--------|
| 1 | Project-doc writes under `projects/iseo-su-site-ops/` | PASS |
| 2 | Secret-profile writes under `X:\AI MARS\local\` | PASS |
| 3 | Local files ignored by Git | PASS |
| 4 | No real secrets added by task | PASS |
| 5 | No access data in project docs or REPORT | PASS |
| 6 | No files outside authorized loci changed by this task | PASS (foreign WIP untouched) |
| 7 | No production/network/browser access | PASS |
| 8 | No Storage or Localhost writes | PASS |
| 9 | Registry / ATLAS / WPilot / Report Hub unchanged | PASS |
| 10 | Staged diff empty | PASS |

---

## 12. Risks

| Risk | Mitigation |
|------|------------|
| Operator pastes secrets into chat | Setup guide forbids; reply format without values |
| wp-admin confused with Beget panel | Explicit correction in docs |
| Local fill treated as connection authorization | Access classification + OPERATIONAL-INDEX HOLDs |
| Operator Beget backup treated as sole safety | Intake records residual scoped backup/validation/rollback/HITL/evidence need |
| Branch divergence (ahead 11 / behind 52) | Recorded; no pull/push in this task |
| Foreign WIP pollution | Selective scope; no `git add .` |

---

## 13. SAFE UNKNOWN

- Beget control-panel URL  
- Exact FTP/SFTP protocol/host/port/username/password (until local fill; never in REPORT)  
- Static/WordPress architecture split  
- Maintained canonical local/Git source outside production  
- Additional public routes beyond root  
- Hosting restore method details  
- WPilot production compatibility / token for this site  

---

## 14. Required Operator Action

1. Open and fill the exact local files listed in [ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md](../ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md).  
2. Reply only:

```text
ACCESS FILES FILLED
- Beget: yes/no
- FTP/SFTP: yes/no
- WordPress admin: yes/no
- hosting_panel_url known: yes/no
```

3. Do not paste secret values into Cursor REPORT or Web-GPT.

---

## 15. Next Gate

**ISEO-SU-SITE-OPS — PHASE 2B LOCAL ACCESS FILE PRESENCE REVIEW**

Phase 2B initially verifies file presence and non-empty required fields **locally**.  
It does **not** connect unless a separate external-access charter is approved.

---

## 16. Stop Condition

At task end:

- no production connection;
- no browser access;
- no Beget login;
- no WordPress login;
- no FTP/SFTP connection;
- no credential validation;
- no WPilot installation;
- no WPilot token;
- no REST;
- no database access;
- no Storage;
- no Localhost;
- no ATLAS or registry mutation;
- no Git stage/commit/push;
- wait for the operator to fill the exact local files.

---

*REPORT · Phase 2A · 2026-07-22 · no secrets.*

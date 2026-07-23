# REPORT — ISEO-SU SITE OPS PHASE 2 NON-SECRET EVIDENCE INTAKE

**Task ID:** ISEO-SU-SITE-OPS-PHASE-2-NON-SECRET-SITE-EVIDENCE-INTAKE  
**Date:** 2026-07-22  
**Lane:** A — Existing Site Operations / Integration  
**Final status:** **PHASE 2 — OPEN / AWAITING OPERATOR WAVE A EVIDENCE**

---

## 1. Execution Summary

Prepared the canonical Phase 2 non-secret evidence intake structure for `https://i-seo.su/`: intake ledger, operator evidence-request waves, empty public route register, access-class model, hybrid discovery questionnaire, and redaction guide. Updated OPERATIONAL-INDEX, Artifact Register, SAFE UNKNOWN Register, and Phase Model.

No production connection, crawl, FTP/SFTP, WordPress login, WPilot install, token, REST, database access, Localhost, ATLAS mutation, registry mutation, or Git stage/commit/push was performed.

Phase 2 is **not** marked COMPLETE. Next gate is Wave A evidence review after operator answers.

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
| Ahead / behind (local knowledge) | **ahead 11, behind 52** |
| Staged changes | **empty** (preflight) |
| Foreign WIP | Present extensively outside authorized locus — **preserved** |
| Governance read | AGENTS.md, `.cursorrules`, X-drive authority, infrastructure reality, site-ops OPERATIONAL-INDEX |

---

## 3. Files Created or Updated

**Created:**

```text
projects/iseo-su-site-ops/ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md
projects/iseo-su-site-ops/ISEO-SU-NON-SECRET-EVIDENCE-REQUEST-v1.md
projects/iseo-su-site-ops/ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md
projects/iseo-su-site-ops/ISEO-SU-ACCESS-CLASSIFICATION-v1.md
projects/iseo-su-site-ops/ISEO-SU-HYBRID-DISCOVERY-QUESTIONNAIRE-v1.md
projects/iseo-su-site-ops/ISEO-SU-EVIDENCE-REDACTION-GUIDE-v1.md
projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2-NON-SECRET-EVIDENCE-INTAKE.md
```

**Updated:**

```text
projects/iseo-su-site-ops/OPERATIONAL-INDEX.md
projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md
projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md
projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md
```

All writes confined to `projects/iseo-su-site-ops/`.

---

## 4. Evidence Classification Model

Every intake fact uses one of:

CONFIRMED BY REPOSITORY · CONFIRMED BY OPERATOR · CONFIRMED BY SANITIZED EVIDENCE · PUBLICLY OBSERVABLE — OPERATOR PROVIDED · OPERATOR CONTEXT · INFERENCE · CONFLICTING · DEFERRED · SAFE UNKNOWN · EXCLUDED

Operator beliefs are recorded as **OPERATOR CONTEXT** and are not promoted to confirmed technical fact without evidence.

---

## 5. Operator Context Recorded

Recorded without elevating to confirmed architecture:

- existing production site;
- Андрей originally created frontend layout;
- main pages believed static HTML;
- WordPress used for blog;
- WordPress may provide header/footer;
- ACF may be used;
- tariff cards, SEO calculator, web commercial-proposal tool exist;
- FTP/file-level work may be needed later;
- WordPress/WPilot may later apply to WordPress-owned surfaces.

Programme identity (`https://i-seo.su/`, i-SEO, Andrey) remains as previously confirmed in charter/locus docs.

---

## 6. Evidence Request Waves

| Wave | Scope | Status |
|------|-------|--------|
| **A** | Basic architecture (hosting, panel, FTP/SFTP existence, WP admin existence, staging, key URLs, static/WP split, source, maintainers, critical pages) | **REQUESTED NOW** |
| **B** | Sanitized hosting/filesystem | DEFERRED until Wave A review |
| **C** | Sanitized WordPress | DEFERRED |
| **D** | Custom tools depth | DEFERRED |
| **E** | Backup and ownership | DEFERRED |

---

## 7. Access Classes

Defined A0–A8 without storing access data.

- **A0** — public docs only from operator-provided evidence  
- **A1/A2** — allowed when manually supplied (screenshots / sanitized exports)  
- **A3–A8** — **NOT AUTHORIZED** (hosting RO, WP RO, FTP RO, WPilot RO, controlled write, emergency rollback)

---

## 8. Redaction Rules

Redaction guide requires removal of passwords, tokens, cookies, auth headers, unnecessary usernames/emails/IPs, license/API/SMTP secrets, WordPress salts, account home-path segments, and secret-bearing URLs. Product/version/plugin/theme/folder/route names and redacted docroot shape may be retained.

---

## 9. Current Evidence State

| Item | State |
|------|-------|
| Phase 2 intake structure | CREATED |
| Operator Wave A package | **NONE RECEIVED** |
| Public route register | **EMPTY** (domain identity only; no accepted route inventory) |
| Hosting / WP / tools facts | SAFE UNKNOWN or OPERATOR CONTEXT |
| Phase 2 programme | **OPEN** — not COMPLETE |

---

## 10. Risks

| Risk | Mitigation |
|------|------------|
| Treating OPERATOR CONTEXT as verified | Classification model + intake ledger |
| Secret leakage via screenshots | Redaction guide + forbidden list |
| Premature Waves B–E / Phase 3 | Wave A gate; Phase 3 HOLD |
| Agent crawl temptation | Explicit no-crawl rule; A0 operator-provided only |
| Dual SoT drift | Boundaries + this locus SoT |

---

## 11. SAFE UNKNOWN

All U-001–U-032 remain unresolved without new evidence. Phase 2 links added to SAFE UNKNOWN Register (intake, questionnaire, evidence request, route register). No invented resolutions.

---

## 12. Git and Foreign WIP

| Item | State |
|------|--------|
| Stage | Not performed |
| Commit | Not performed |
| Push | Not performed |
| Staged diff | Must remain empty |
| Foreign WIP | Preserved (Forge FP-0002, OCPilot, workspaces, `.recovery-temp`, etc.) |
| Ahead/behind | ahead 11 / behind 52 — recorded; no fetch/pull/rebase |

---

## 13. Validation

Performed after writes (see closeout validation commands in session):

| Check | Expected |
|-------|----------|
| Required Phase 2 files exist and readable | PASS |
| Writes only under `projects/iseo-su-site-ops/` | PASS |
| No secret values in new/updated docs | PASS |
| No production / network / crawl access | PASS |
| No Localhost / Storage writes | PASS |
| `registry/project-registry.md` unchanged | PASS |
| `projects/atlas/` unchanged | PASS |
| `projects/wpilot/` unchanged | PASS |
| Staged empty | PASS |
| Scoped diff limited to site-ops locus | PASS |

---

## 14. Required Operator Input

**WAVE A only** (do not send Waves B–E yet):

1. Hosting provider name.  
2. Control panel name.  
3. Whether FTP/SFTP access exists.  
4. Whether WordPress admin exists.  
5. Whether staging/dev exists.  
6. Public list of key URLs.  
7. Plain-language split between static and WordPress sections.  
8. Whether current source code exists locally or in Git.  
9. Who besides the operator has changed the site.  
10. Known business-critical pages/tools that must not be touched.

Do not send passwords, tokens, cookies, `wp-config.php`, database dumps, full archives, or secret-bearing URLs.

---

## 15. Next Gate

Recommend only:

**ISEO-SU-SITE-OPS — PHASE 2A WAVE A EVIDENCE REVIEW**

This gate occurs only after the operator supplies Wave A answers.  
Do **not** authorize Phase 3 yet.

---

## 16. Stop Condition

At task end:

- no site connection;
- no public crawling;
- no browser access;
- no hosting login;
- no FTP/SFTP;
- no WordPress login;
- no WPilot installation;
- no token;
- no REST;
- no database access;
- no Localhost;
- no ATLAS mutation;
- no registry mutation;
- no Git stage/commit/push;
- **wait for operator Wave A evidence.**

---

*PHASE 2 — OPEN / AWAITING OPERATOR WAVE A EVIDENCE · 2026-07-22.*

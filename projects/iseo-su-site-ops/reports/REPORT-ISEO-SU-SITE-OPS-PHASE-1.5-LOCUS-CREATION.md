# REPORT — ISEO-SU SITE OPS PHASE 1.5 LOCUS CREATION

**Task ID:** ISEO-SU-SITE-OPS-PHASE-1.5-PROJECT-CHARTER-AND-LOCUS  
**Date:** 2026-07-22  
**Lane:** A — Existing Site Operations / Integration  
**Final status:** **PHASE 1.5 — COMPLETE**

---

## 1. Execution Summary

Created the canonical MARS programme locus for existing production site operations of `https://i-seo.su/` and persisted accepted Phase 0 / Phase 1 decisions as documentation only.

No production connection, FTP/SFTP, WordPress access, WPilot install, token creation, REST, ATLAS mint, project-registry mutation, Localhost mirror, Browser Workstation implementation, or Git stage/commit/push was performed.

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
| Staged changes | **empty** |
| Locus before task | **ABSENT** (safe to create) |
| Foreign WIP | Present extensively outside authorized locus — **preserved** |

Governance sources read (Lane B support): AGENTS.md, `.cursorrules`, `governance/mars-x-drive-root-authority-v1.md`, `governance/mars-infrastructure-reality-v1.md`, `governance/current-operational-state-v1.md`, `governance/mars-operational-evolution-state-after-cycles-1-8-v0.md`, `registry/project-registry.md`.

Supporting programme indexes / WPilot / Forge experience sources reviewed per task list (exact repo paths; see §7).

---

## 3. Files Created

```text
X:\AI MARS\projects\iseo-su-site-ops\
  OPERATIONAL-INDEX.md
  README.md
  ISEO-SU-SITE-OPS-CHARTER-v1.md
  ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md
  ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md
  ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md
  ISEO-SU-SITE-OPS-DECISION-REGISTER-v1.md
  ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md
  ISEO-SU-SITE-OPS-CROSS-CHAT-HANDOFF-CLOSEOUT-v1.md
  ISEO-SU-SITE-OPS-FIREFOX-BROWSER-WORKSTATION-DEFERRED-v1.md
  reports\
    REPORT-ISEO-SU-SITE-OPS-PHASE-0-PREFLIGHT-CLOSEOUT.md
    REPORT-ISEO-SU-SITE-OPS-PHASE-1-CROSS-CHAT-INTAKE-CLOSEOUT.md
    REPORT-ISEO-SU-SITE-OPS-PHASE-1.5-LOCUS-CREATION.md
```

No tokens/, credentials/, FTP/, backups/, evidence/, plugin source, or Localhost trees were created.

---

## 4. Programme Locus

| Field | Value |
|-------|-------|
| Programme | ISEO-SU-SITE-OPS |
| Site | https://i-seo.su/ |
| Organization | i-SEO |
| Operator | Andrey |
| Canonical locus | `X:\AI MARS\projects\iseo-su-site-ops\` |
| Lifecycle | DOCUMENTARY INTAKE / PRE-CONNECTION |
| Phase after this REPORT | PHASE 1.5 — COMPLETE |
| Production connection | NOT AUTHORIZED |

Preliminary architecture remains **OPERATOR-CONTEXT**: hybrid static HTML + WordPress (not verified technical evidence).

---

## 5. Authority and Boundaries

Main SoT for hybrid site operations documentation is this locus.

Supporting / sibling only:

- `projects/wpilot/` — WordPress pilot / plugin contracts
- `projects/iseo-report-hub/` — sibling product
- `projects/mars-website-factory/` — static methodology
- `projects/mars-website-factory/subsystems/forge-wordpress/` — WP methodology; do not copy FP-0002 architecture
- `projects/atlas/` — identity registry; mint deferred
- `projects/mars-survivability/` — safety methodology
- `projects/mars-localhost-infrastructure/` — optional future mirror authority
- `projects/remote-operations-layer/` — remote-ops discipline; not authorization

Normative detail: `ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md`.

---

## 6. Accepted Decisions

Persisted in `ISEO-SU-SITE-OPS-DECISION-REGISTER-v1.md` (decision date **2026-07-22**), including:

- dedicated locus ownership;
- Report Hub sibling;
- WPilot WordPress-only;
- Forge / Website Factory methodology-only;
- ATLAS mint deferred;
- no production connection;
- no credentials in docs;
- runtime-first audit;
- no broad sync;
- preserve operator manual production changes;
- bounded promote;
- plugin backup ≠ hosting backup;
- production compatibility SAFE UNKNOWN;
- Firefox Developer Edition → separate Browser Workstation (implementation deferred).

---

## 7. Cross-Chat Reconciliation

Closeout: `ISEO-SU-SITE-OPS-CROSS-CHAT-HANDOFF-CLOSEOUT-v1.md`.

Reconciled:

- **A.** SoT = this locus; no second full passport under `projects/wpilot/sites/`
- **B.** Token format SAFE UNKNOWN; preferred principle = separate token file + path metadata
- **C.** Heavy backups default toward `X:\AI MARS STORAGE\` (verify policy later; no paths created)
- **D.** DEV backup/rollback capability exists; production proof SAFE UNKNOWN
- **E.** DEV proof is not a minimum-version contract

Chat handoff = supporting evidence only.

---

## 8. Firefox Browser Workstation Deferred Record

Created: `ISEO-SU-SITE-OPS-FIREFOX-BROWSER-WORKSTATION-DEFERRED-v1.md`.

Classification: **APPROVED DIRECTION / IMPLEMENTATION DEFERRED**.  
No install, profile, login, cookies, proxy/VPN, extensions, automation, or production access authorized.

---

## 9. Git and Foreign WIP

| Item | State |
|------|-------|
| Stage | Not performed |
| Commit | Not performed |
| Push | Not performed |
| Staged diff | Remains empty |
| Foreign WIP | Preserved (Forge FP-0002 reports, OCPilot site-002, workspaces, `.recovery-temp`, etc.) |
| Ahead/behind | ahead 11 / behind 52 — recorded; no fetch/pull/rebase |

**Registry proposal (NOT executed):** add `project_id` `iseo-su-site-ops` to `registry/project-registry.md` in a later chartered task.

---

## 10. Validation

| Check | Result |
|-------|--------|
| All required files exist | PASS |
| Markdown readable | PASS |
| Secret scan (passwords, tokens, Authorization headers, X-WPilot-Token values, FTP/WP admin credentials, private keys, secret-like real values) | PASS — no secret values found |
| Files outside authorized locus changed by this task | PASS — none |
| `registry/project-registry.md` unchanged | PASS |
| `projects/atlas/` unchanged | PASS |
| `projects/wpilot/` unchanged | PASS |
| `projects/iseo-report-hub/` unchanged | PASS |
| Storage / Localhost writes | PASS — none |
| Staged empty | PASS |
| Scoped diff limited to `projects/iseo-su-site-ops/` | PASS (untracked new locus) |

---

## 11. Risks

| Risk | Mitigation |
|------|------------|
| Dual SoT drift into WPilot/Report Hub | Boundaries + Decision Register |
| Treating hybrid architecture as verified | OPERATOR-CONTEXT + SAFE UNKNOWN register |
| Premature connection | Phase model HOLDs; Phase 6 NOT AUTHORIZED |
| Registry absence | Propose row later; do not imply registered product |
| Monorepo ahead/behind divergence | No push; foreign WIP preserved |

---

## 12. SAFE UNKNOWN

See `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md` (hosting, docroot, versions, routing, tools, backups, WPilot compatibility, token format, Storage paths, ATLAS, local mirror, Browser Workstation profile, etc.).

---

## 13. Next Authorized Phase

Recommend only:

**ISEO-SU-SITE-OPS — PHASE 2 — NON-SECRET SITE EVIDENCE INTAKE**

Phase 2 remains **HOLD** until operator acceptance of this Phase 1.5 REPORT.

---

## 14. Required Operator Review

Please review and accept:

1. Locus ownership and boundaries
2. Decision register
3. Phase model (especially Phase 2 HOLD → authorize)
4. SAFE UNKNOWN register completeness for intake planning
5. Firefox Browser Workstation deferred posture
6. Optional later task: project-registry row proposal

---

## 15. Stop Condition

At end of Phase 1.5:

- no production access;
- no FTP/SFTP;
- no WordPress access;
- no plugin installation;
- no token;
- no REST request;
- no ATLAS mutation;
- no project-registry mutation;
- no Localhost creation;
- no Browser Workstation implementation;
- no Git stage/commit/push;
- **wait for operator review.**

---

*PHASE 1.5 — COMPLETE · 2026-07-22.*

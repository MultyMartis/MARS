# METALLKA-RU SITE OPS — Operational Index

**Lane:** A — Existing Site Operations / Integration  
**Classification:** operational programme locus  
**Domain root:** [README.md](README.md)

---

## Programme identity

| Field | Value |
|-------|-------|
| **Programme name** | METALLKA-RU-SITE-OPS |
| **project_id (intended)** | `metallka-ru-site-ops` — **not registered** in `registry/project-registry.md` (registry mutation **NOT AUTHORIZED**) |
| **Site / domain** | `metallka.ru` |
| **Canonical locus** | `X:\AI MARS\projects\metallka-ru-site-ops\` |
| **Primary lane** | Lane A — Existing Site Operations / Integration |

---

## Current state

| Field | Value |
|-------|-------|
| **Current stage** | **PHASE 4C-R1 — GATE E RETRY EXECUTION** |
| **Lifecycle** | **COMPLETE — WPILOT PRODUCTION AUTH + READ-ONLY REST PROVEN** |
| **Production** | **CONNECTED** — architecture captured; CHANGE 0001 validated; WPilot installed + read bridge |
| **CHANGE-0001** | **COMPLETE — PRODUCTION VALIDATED** |
| **WP Admin write workflow (bounded text)** | **PROVEN** for CHANGE 0001 class |
| **WPilot on metallka** | **INSTALLED / ACTIVE** (`metacode-wpilot` 0.3.0 / RC6 / schema 0.2.0) |
| **WPilot baseline** | **i-seo-proven `0.3.0-RC6`** — package SHA `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6`; aggregate `f2be244567da7c0c69e210f3b7a4dce1680889ce79f5d6c1dfd9654db3ee37ed` |
| **Phase 4B RC6 install** | **HISTORICAL SUCCESS** — not failed; baseline assumption reconciled via FIX01 against live i-seo |
| **WPilot compatibility** | **INSTALL PROVEN** (4B) + **CODE == ISEO** (FIX01) + **AUTH + READ REST PROVEN** (4C-R1); Gate E blocked historically; semantics **SAFE WITH CONDITIONS** |
| **WPilot install authorization** | **EXECUTED** (Phase 4B) |
| **Credentials** | SSH/FTP/DB usable; **WP Admin password VALIDATED**; Beget panel fields still incomplete |
| **Token** | **YES** — local-only `wpilot-prod-metallka-ru.token` (gitignored); **auth PROVEN** (4C-R1); token generations this wave **0** |
| **Bridge / REST smoke / writes** | bridge **ON** · write **OFF** · `dev_confirmed` **ON** · authenticated REST **PROVEN** (5 GET) · writes **BLOCKED** |
| **`dev_confirmed` semantics** | **SAFE WITH CONDITIONS** — operator confirmation gate (label historically misleading); production use authorized under 4C-R1 |
| **Local mirror** | **DEFER** |
| **ATLAS binding** | **PARTIAL / INCOMPLETE** (`PER-0003` only) |
| **Gate A** | **APPROVED** and **EXECUTED** (read-only) |
| **Gate E** | **AUTHORIZED** · **EXECUTED AS BLOCKED STOP** (Phase 4C historical) |
| **Gate E retry** | **EXECUTED COMPLETE** (Phase 4C-R1) — final posture T/T/F MODEL A |
| **Site Ops write readiness** | **PROVEN** for bounded WP Admin / WPBakery page-local text (CHANGE 0001 class); WPilot writes still **BLOCKED** |
| **Git persistence** | **REMOTE BASELINE PERSISTENCE COMPLETE** — remote commit `0a39638d5cf0e593c5c262f98bfd6722808f6307` on `origin/mars/canonical-post-recovery` (parent `dc1fa5c48255efd8819b1947408d82f67bf020ca`). Push **COMPLETE** (fast-forward / no force). Primary Active Brain synchronization **NOT PERFORMED**. Post-push documentation follow-up **PREPARED** (Phase 4C-P5; push **NOT AUTHORIZED**). Historical provenance only: `980fa320` / `c781a55a` / `ac0f37b7`. |
| **MARS Git model** | One monorepo; dirty `X:\AI MARS` = Active Brain / INPUT SOURCE (read-only for Git waves); foreign WIP out of scope; persistence/sync = Storage `git-sync-*\repo`; remote canonical tip is integration authority |

---

## Next recommended stage

| Field | Value |
|-------|--------|
| **Does NOT auto-start** | Phase 4D write smoke / write enable / backup / dry-run / scoped-replace |
| **Next phase** | Push prepared **P5 post-push documentation follow-up** (separate approval) → then **PHASE 4D — FIRST WPILOT CONTROLLED WRITE SMOKE CHARTER PREPARATION** (not authorized here) |
| **Push approval used** | `APPROVE METALLKA GIT PUSH — PUSH SCOPED PERSISTENCE COMMIT TO ORIGIN CANONICAL` (P4-R3) |
| **Required approval (future P5 push)** | `APPROVE METALLKA P5 PUSH — PUSH POST-PUSH DOCUMENTATION FOLLOW-UP TO ORIGIN CANONICAL` (not granted in P5 prep) |
| **Evidence (4C-R1)** | [METALLKA-WPILOT-GATE-E-RETRY-EXECUTION-EVIDENCE-v1.md](METALLKA-WPILOT-GATE-E-RETRY-EXECUTION-EVIDENCE-v1.md) |
| **Evidence (4C-P2/P3)** | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P2-CLEAN-WORKTREE-CORPUS-PERSISTENCE.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P2-CLEAN-WORKTREE-CORPUS-PERSISTENCE.md) · [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P3-CANONICAL-INTEGRATION-READINESS.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P3-CANONICAL-INTEGRATION-READINESS.md) |
| **Evidence (4C-P4-R1)** | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R1-CANONICAL-PROMOTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R1-CANONICAL-PROMOTION.md) (historical BLOCKED) |
| **Evidence (4C-P4-R2)** | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R2-REMOTE-CANONICAL-PERSISTENCE-PREP.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R2-REMOTE-CANONICAL-PERSISTENCE-PREP.md) (included in P5 follow-up) |
| **Evidence (4C-P4-R3)** | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R3-REMOTE-CANONICAL-PUSH.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R3-REMOTE-CANONICAL-PUSH.md) (included in P5 follow-up) |

---

## Canonical reading order (this locus)

| # | Document |
|---|----------|
| 1 | [README.md](README.md) |
| 2 | This [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) |
| 3 | [METALLKA-SITE-PASSPORT-v1.md](METALLKA-SITE-PASSPORT-v1.md) |
| 4 | [METALLKA-ACCESS-MODEL-v1.md](METALLKA-ACCESS-MODEL-v1.md) |
| 5 | [METALLKA-WP-ENTITY-MAP-v1.md](METALLKA-WP-ENTITY-MAP-v1.md) |
| 6 | [METALLKA-THE7-WPBAKERY-MAP-v1.md](METALLKA-THE7-WPBAKERY-MAP-v1.md) |
| 7 | [METALLKA-PAGE-INVENTORY-v1.md](METALLKA-PAGE-INVENTORY-v1.md) |
| 8 | [METALLKA-PLUGIN-INVENTORY-v1.md](METALLKA-PLUGIN-INVENTORY-v1.md) |
| 9 | [METALLKA-FORM-MAP-v1.md](METALLKA-FORM-MAP-v1.md) |
| 10 | [METALLKA-CUSTOM-CODE-MAP-v1.md](METALLKA-CUSTOM-CODE-MAP-v1.md) |
| 11 | [METALLKA-CACHE-MAP-v1.md](METALLKA-CACHE-MAP-v1.md) |
| 12 | [METALLKA-BACKUP-ROLLBACK-MODEL-v1.md](METALLKA-BACKUP-ROLLBACK-MODEL-v1.md) |
| 13 | [METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md](METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md) |
| 14 | [METALLKA-LOCAL-MIRROR-DECISION-v1.md](METALLKA-LOCAL-MIRROR-DECISION-v1.md) |
| 15 | [METALLKA-PROTECTED-ZONES-v1.md](METALLKA-PROTECTED-ZONES-v1.md) |
| 16 | [METALLKA-SAFE-UNKNOWN-REGISTER-v1.md](METALLKA-SAFE-UNKNOWN-REGISTER-v1.md) |
| 17 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-2B-PRODUCTION-READ-ONLY-DISCOVERY.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-2B-PRODUCTION-READ-ONLY-DISCOVERY.md) |
| 18 | [METALLKA-CHANGE-REQUEST-0001-ABOUT-TEXT-v1.md](METALLKA-CHANGE-REQUEST-0001-ABOUT-TEXT-v1.md) |
| 19 | [METALLKA-CHANGE-0001-EXECUTION-CHARTER-v1.md](METALLKA-CHANGE-0001-EXECUTION-CHARTER-v1.md) |
| 20 | [METALLKA-CHANGE-0001-EXECUTION-EVIDENCE-v1.md](METALLKA-CHANGE-0001-EXECUTION-EVIDENCE-v1.md) |
| 21 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-3A-CHANGE-0001-PREPARATION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-3A-CHANGE-0001-PREPARATION.md) |
| 22 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-CHANGE-0001-PRODUCTION-EXECUTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-CHANGE-0001-PRODUCTION-EXECUTION.md) |
| 23 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-R1-CHANGE-0001-PRODUCTION-EXECUTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-R1-CHANGE-0001-PRODUCTION-EXECUTION.md) |
| 24 | [METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md](METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md) |
| 25 | [METALLKA-WPILOT-RC6-PACKAGE-ACCEPTANCE-v1.md](METALLKA-WPILOT-RC6-PACKAGE-ACCEPTANCE-v1.md) |
| 26 | [METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md](METALLKA-WPILOT-INSTALL-ROLLBACK-PLAN-v1.md) |
| 27 | [METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md](METALLKA-WPILOT-TOKEN-LOCAL-STORAGE-PLAN-v1.md) |
| 28 | [METALLKA-WPILOT-POST-INSTALL-VALIDATION-PLAN-v1.md](METALLKA-WPILOT-POST-INSTALL-VALIDATION-PLAN-v1.md) |
| 29 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4A-WPILOT-INSTALLATION-ONBOARDING-CHARTER.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4A-WPILOT-INSTALLATION-ONBOARDING-CHARTER.md) |
| 30 | [METALLKA-WPILOT-RC6-INSTALLATION-EVIDENCE-v1.md](METALLKA-WPILOT-RC6-INSTALLATION-EVIDENCE-v1.md) |
| 31 | [METALLKA-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md](METALLKA-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md) |
| 32 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4B-WPILOT-RC6-PRODUCTION-INSTALL-ACTIVATE-TOKEN.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4B-WPILOT-RC6-PRODUCTION-INSTALL-ACTIVATE-TOKEN.md) |
| 33 | [METALLKA-WPILOT-CURRENT-BASELINE-RECONCILIATION-v1.md](METALLKA-WPILOT-CURRENT-BASELINE-RECONCILIATION-v1.md) |
| 34 | [METALLKA-WPILOT-FIX01-UPDATE-EVIDENCE-v1.md](METALLKA-WPILOT-FIX01-UPDATE-EVIDENCE-v1.md) |
| 35 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4B-FIX01-ISEO-WPILOT-BASELINE-RECONCILIATION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4B-FIX01-ISEO-WPILOT-BASELINE-RECONCILIATION.md) |
| 36 | [METALLKA-WPILOT-GATE-E-READ-SMOKE-EVIDENCE-v1.md](METALLKA-WPILOT-GATE-E-READ-SMOKE-EVIDENCE-v1.md) |
| 37 | [METALLKA-WPILOT-CONNECTION-STATE-v1.md](METALLKA-WPILOT-CONNECTION-STATE-v1.md) |
| 38 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-WPILOT-GATE-E-BRIDGE-READ-SMOKE.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-WPILOT-GATE-E-BRIDGE-READ-SMOKE.md) |
| 39 | [METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md](METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md) |
| 40 | [METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md](METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md) |
| 41 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R0-GATE-E-RETRY-CHARTER.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R0-GATE-E-RETRY-CHARTER.md) |
| 42 | [METALLKA-WPILOT-GATE-E-RETRY-EXECUTION-EVIDENCE-v1.md](METALLKA-WPILOT-GATE-E-RETRY-EXECUTION-EVIDENCE-v1.md) |
| 43 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R1-WPILOT-GATE-E-RETRY-EXECUTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R1-WPILOT-GATE-E-RETRY-EXECUTION.md) |
| 44 | [METALLKA-GIT-PERSISTENCE-AUDIT-v1.md](METALLKA-GIT-PERSISTENCE-AUDIT-v1.md) |
| 45 | [METALLKA-GIT-PERSISTENCE-ALLOWLIST-v1.txt](METALLKA-GIT-PERSISTENCE-ALLOWLIST-v1.txt) (historical P1) |
| 46 | [METALLKA-GIT-PERSISTENCE-ALLOWLIST-v2.txt](METALLKA-GIT-PERSISTENCE-ALLOWLIST-v2.txt) (**current** staging authority) |
| 47 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P2-CLEAN-WORKTREE-CORPUS-PERSISTENCE.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P2-CLEAN-WORKTREE-CORPUS-PERSISTENCE.md) |
| 48 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P3-CANONICAL-INTEGRATION-READINESS.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P3-CANONICAL-INTEGRATION-READINESS.md) |
| 49 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R1-CANONICAL-PROMOTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R1-CANONICAL-PROMOTION.md) |
| 50 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R2-REMOTE-CANONICAL-PERSISTENCE-PREP.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R2-REMOTE-CANONICAL-PERSISTENCE-PREP.md) |
| 51 | [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R3-REMOTE-CANONICAL-PUSH.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-P4-R3-REMOTE-CANONICAL-PUSH.md) |
| 52 | [METALLKA-GIT-POST-PUSH-FOLLOWUP-ALLOWLIST-v1.txt](METALLKA-GIT-POST-PUSH-FOLLOWUP-ALLOWLIST-v1.txt) (P5 follow-up staging authority) |

---

## Active HOLDs

| HOLD | Status |
|------|--------|
| Beget panel credential fill (local) | **PENDING** (optional; useful for backup UI proof) |
| Valid WP Admin password in local secrets | **CLEARED** (R1 validated) |
| CHANGE-0001 production mutation | **CLEARED — COMPLETE** |
| Production writes (general) | **HOLD** except exact future authorized CHANGE |
| WPilot install / activation / token | **CLEARED — Phase 4B COMPLETE**; FIX01 confirmed CODE == i-seo (no further update) |
| Gate E bridge / authenticated read smoke | **CLEARED — Phase 4C-R1 COMPLETE** (auth + read REST PROVEN; posture T/T/F) |
| Write enable / WPilot writes | **HOLD / BLOCKED** (bridge remains ON for read; writes not authorized) |
| Local mirror / MLI profile | **HOLD / DEFER** |
| ATLAS ORG / WEB / DOM | **HOLD** |
| Registry project row | **HOLD** |
| Git corpus remote baseline | **CLEARED — P4-R3 PUSH COMPLETE** — `0a39638d5cf0e593c5c262f98bfd6722808f6307` on `origin/mars/canonical-post-recovery`; primary sync **NOT PERFORMED**; P5 post-push docs follow-up **PREPARED / PUSH NOT AUTHORIZED** |

---

## Authority order

1. `AGENTS.md` / `.cursorrules` / `governance/mars-x-drive-root-authority-v1.md`  
2. This programme locus: `projects/metallka-ru-site-ops/`  
3. Supporting methodology from siblings — **patterns only**  
4. Operator HITL charters for later gates  
5. Chat handoffs — supporting evidence only  

---

*METALLKA-RU-SITE-OPS Operational Index · Phase 4C-R1 COMPLETE — WPilot T/T/F reads PROVEN; writes BLOCKED; Git: remote baseline COMPLETE @ `0a39638d5cf0` on origin/canonical; primary sync NOT PERFORMED; P5 post-push docs PREPARED (push not authorized); Phase 4D not started.*

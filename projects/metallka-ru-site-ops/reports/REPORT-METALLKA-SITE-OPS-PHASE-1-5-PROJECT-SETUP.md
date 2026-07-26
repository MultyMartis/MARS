# REPORT — METALLKA SITE OPS PHASE 1.5 PROJECT LOCUS & BASELINE

**Task:** METALLKA-SITE-OPS — PHASE 1.5 PROJECT LOCUS & CONSOLIDATED BASELINE  
**Date:** 2026-07-25  
**Locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Decision:** **COMPLETE — PROJECT LOCUS AND DOCUMENTATION BASELINE ESTABLISHED**

---

## Status

**COMPLETE — PROJECT LOCUS AND DOCUMENTATION BASELINE ESTABLISHED**

Documentation-only. No production access. No credentials. No WPilot install/token/bridge/smoke/writes. No ATLAS mint. No registry mutation. No commit.

---

## Environment

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume | `X:` / label **AI WS** |
| `AGENTS.md` / `.cursorrules` | Present |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `fb039af2199a6aadf59beb53095f351a5e46ddbf` |
| Staged index | **Empty** (unchanged) |
| Foreign WIP | Present — **untouched** |
| Unpushed commits vs origin | Present (pre-existing; **no commit/push** this task) |
| HEAD vs `origin/mars/canonical-post-recovery` | Diverged (pre-existing; **no pull/rebase/push**) |

---

## Files Created

| Path |
|------|
| `projects/metallka-ru-site-ops/README.md` |
| `projects/metallka-ru-site-ops/OPERATIONAL-INDEX.md` |
| `projects/metallka-ru-site-ops/METALLKA-SITE-OPS-CHARTER-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-SITE-OPS-CURRENT-BASELINE-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-SAFE-UNKNOWN-REGISTER-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-PROTECTED-ZONES-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-ARTIFACT-REGISTER-v1.md` |
| `projects/metallka-ru-site-ops/reports/REPORT-METALLKA-SITE-OPS-PHASE-1-5-PROJECT-SETUP.md` |

Directory `reports\` created as container for the report above.

---

## Baseline Recorded

- Programme METALLKA-RU-SITE-OPS; site `metallka.ru`
- Phase 1.5 documentation locus; production **NOT CONNECTED**
- Precedent split: i-seo (security/onboarding), triumph DEV (The7/WPBakery), FP-0002/Forge (methodology)
- Gates A–F defined; next = Phase 2A charter **preparation** only

---

## WPilot Baseline

| Field | Value |
|-------|-------|
| Programme | ACTIVE Reference Implementation |
| Proven DEV | 0.3.0-RC5 |
| Deployment baseline | 0.3.0-RC6 |
| Plugin / schema | 0.3.0 / 0.2.0 |
| Source | `projects/wpilot/plugin/metacode-wpilot/` |
| Package | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` (**match**) |
| Remediation commit | `27dfe624eec8b10b73e34c4a5f6df323258ecd1b` |
| On metallka | **NOT INSTALLED / NOT VERIFIED** |

Production-proven (i-seo only): install, activation, RC5→RC6, safe defaults, token generation.  
Not production-proven: REST auth, ping, reads, backup, dry-run, scoped replace, rollback, writes.

Safe defaults: `bridge_enabled=false`, `write_enabled=false`, `dev_confirmed=false`. Token independent of bridge/`dev_confirmed` on RC6.

---

## Precedent Model

Recorded in charter + baseline. None is 1:1 blueprint. Transfer bans documented.

---

## ATLAS State

| Field | Value |
|-------|-------|
| Binding | **PARTIAL / INCOMPLETE** |
| Known | `PER-0003` |
| Organization / Website / Domain | **NOT FOUND** |
| Ownership implication | **None** from Person record |

No ATLAS rows created.

---

## Protected Zones

31 default surfaces classified **PROTECTED-BY-DEFAULT** until mapped (see `METALLKA-PROTECTED-ZONES-v1.md`).

---

## SAFE UNKNOWN Count / Summary

| Metric | Value |
|--------|-------|
| Count | **44** |
| Resolved by discovery | **0** |
| Analogy fills | **0** |

---

## Source / Runtime Policy

Production runtime = provisional authority until source discovered. Exact-file fetch/hash/before-copy/compare/resolve/modify/deploy/verify/QA. Admin-first where UI owns; filesystem-first for code-owned surfaces only. No broad sync.

---

## Local Mirror Decision

**DEFER.** No runtime profile created.

---

## Next Phase

**PHASE 2A — PRODUCTION READ-ONLY DISCOVERY CHARTER PREPARATION**

Does **not** authorize access, credentials, FTP/SFTP, WP Admin, WPilot, token, bridge, smoke, or writes.

---

## Files Changed

Only the eight paths under `projects/metallka-ru-site-ops/` listed above (plus empty `reports\` directory as parent of the report).

**Not modified:** registry, ATLAS, WPilot, ISEO, Forge, FP-0002, global governance.

---

## Git Operations

| Action | Result |
|--------|--------|
| Stage | **None** |
| Commit | **None** |
| Push | **None** |
| Staged index after task | Remains **empty** |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Overclaiming production readiness | Explicit NOT CONNECTED / NOT VERIFIED language |
| Analogy drift into SAFE UNKNOWN | Register forbids analogy fill |
| Foreign WIP contamination | Allowlisted paths only; no broad add |
| Unpushed / diverged remote state | Noted; no commit/push this task |
| ATLAS Person misread as ownership | Explicit non-implication recorded |

---

## Stop Condition

**STOP after REPORT.** No further gates executed. No production contact. No commit unless separately authorized.

---

## Validation checklist

| Check | Result |
|-------|--------|
| Files exist | **PASS** |
| Internal links to locus docs | **PASS** |
| No secrets / credentials / tokens in files | **PASS** |
| No production claim inflation | **PASS** |
| RC6 package/hash exact | **PASS** |
| ATLAS not overclaimed | **PASS** |
| No external access performed | **PASS** |
| Diff scope = allowlisted metallka docs only | **PASS** (verify at close) |
| Staged index unchanged | **PASS** |

---

*End of Phase 1.5 setup report.*

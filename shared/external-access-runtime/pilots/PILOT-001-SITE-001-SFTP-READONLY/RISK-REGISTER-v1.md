# PILOT-001 — Risk Register v1

**Pilot ID:** `PILOT-001`  
**Date:** 2026-06-01  
**Review cadence:** At Approval, Implementation Sub-Charter, and Assessment

**Scale:** Likelihood and Impact — **Low** | **Medium** | **High**

---

## 1. Summary

| Rating | Count |
|--------|-------|
| High impact (any likelihood) | 2 |
| Medium | 5 |
| Low | 2 |

**Waived for charter (Phase 3 soft gaps):** machine schema, vault product, automated validation — see [PILOT-CHARTER-v1.md](PILOT-CHARTER-v1.md) §9.

---

## 2. Risk register

### R-01 — Credential exposure

| Field | Value |
|-------|-------|
| **Description** | SFTP passwords, keys, or session tokens leak into git, snapshots, logs, or chat |
| **Likelihood** | Medium |
| **Impact** | High |
| **Mitigation** | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md); external `secrets/` only; redaction audit before any publish; stop ST-10/11 |
| **Residual** | Operator discipline — no automated secret scanner in repo |
| **Waived?** | No |

### R-02 — Partial evidence published as complete

| Field | Value |
|-------|-------|
| **Description** | SFTP-only leg lacks DB/theme sections but snapshot published without `safe-unknown` |
| **Likelihood** | Medium |
| **Impact** | High |
| **Mitigation** | Level 1 quality mapping; SC-09; Validate gate; stop ST-14/16 |
| **Residual** | Manual Validate — human error possible |
| **Waived?** | No |

### R-03 — Version mismatch (platform claim vs files)

| Field | Value |
|-------|-------|
| **Description** | ocStore 3.0.3.8 (rs.2) claim disagrees with version file evidence |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | Version proof files in SFTP scope; consumer cross-check; downgrade or `safe-unknown` |
| **Residual** | Stale TEST tree possible |
| **Waived?** | No |

### R-04 — Missing manifest

| Field | Value |
|-------|-------|
| **Description** | Listing fails or incomplete — cannot support `file-manifest` |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | Partial connector status; no Level 1 publish; stop ST-22; Offline ZIP fallback is **separate charter** |
| **Residual** | Host limits unknown until Execution |
| **Waived?** | No |

### R-05 — Environment confusion (TEST vs PROD)

| Field | Value |
|-------|-------|
| **Description** | Operator connects to wrong host or publishes PROD-labeled data |
| **Likelihood** | Low |
| **Impact** | High |
| **Mitigation** | TEST-only charter; metadata `environment: TEST`; stop ST-07/09 |
| **Residual** | DNS/hosting mislabel **SAFE UNKNOWN** until operator confirms |
| **Waived?** | No |

### R-06 — Human error (scope, path, site)

| Field | Value |
|-------|-------|
| **Description** | Wrong remote root, wrong site folder, accidental download of cache/tmp with secrets |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | Implementation Sub-Charter path exclusions; pre-acquisition checklist; acquisition log |
| **Residual** | Always present for Mode 2 |
| **Waived?** | No |

### R-07 — False readiness assumptions

| Field | Value |
|-------|-------|
| **Description** | Stakeholders interpret Phase 4 charter as “EAR runtime ready” or “Run 5 unblocked” |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md); truth tables in charter and STATUS; SC-16 |
| **Residual** | Communication discipline |
| **Waived?** | Partially — governance docs address |

### R-08 — Pilot-to-runtime confusion

| Field | Value |
|-------|-------|
| **Description** | Connector code merged or accessed without Implementation Sub-Charter |
| **Likelihood** | Low |
| **Impact** | High |
| **Mitigation** | Phase 5 gate; stop ST-17/18/19; no code in Phase 4 |
| **Residual** | Agent/operator boundary |
| **Waived?** | No |

### R-09 — Channel availability unverified

| Field | Value |
|-------|-------|
| **Description** | Repo claims SFTP YES but live host blocks or offers FTP only |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) honesty; preflight at Execution; stop ST-21 |
| **Residual** | **SAFE UNKNOWN** until operator confirms |
| **Waived?** | Acknowledged at charter |

### R-10 — SFTP write-capable account

| Field | Value |
|-------|-------|
| **Description** | Provider grants write-capable SFTP user; read-only claim is procedural only |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | Dedicated read-only account if available; connector deny-list mutating ops; stop ST-13 |
| **Residual** | Hosting policy **SAFE UNKNOWN** |
| **Waived?** | No |

### R-11 — Large tree / timeout / cost

| Field | Value |
|-------|-------|
| **Description** | `image/` or cache dirs cause partial listing or operator pressure to expand scope |
| **Likelihood** | Medium |
| **Impact** | Low |
| **Mitigation** | Narrow CON-L1-A scope; exclude globs in sub-charter; partial status honest |
| **Residual** | May defer full manifest |
| **Waived?** | Yes for Level 1 narrow manifest |

### R-12 — No machine-readable schema

| Field | Value |
|-------|-------|
| **Description** | Manual Validate inconsistency across operators |
| **Likelihood** | Medium |
| **Impact** | Low |
| **Mitigation** | Checklists in success criteria; Phase 5 may require schema decision |
| **Residual** | Accepted for first pilot per Phase 3 |
| **Waived?** | **Yes** — pilot charter |

### R-13 — OCPilot Run 5 pressure

| Field | Value |
|-------|-------|
| **Description** | Urgency to publish incomplete snapshot to unblock Run 5 |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Mitigation** | Stop ST-14; consumer guide blocks version-dependent work without proof |
| **Residual** | Project management outside EAR |
| **Waived?** | No |

---

## 3. Risk acceptance (charter authority)

| Risk ID | Accepted for charter? | Notes |
|---------|----------------------|-------|
| R-12 | Yes | Documented soft gap |
| R-09 | Yes (conditional) | Confirmed at Execution or track change |
| R-11 | Yes | Level 1 narrow scope |
| All others | Require active mitigation | Not waived |

---

## 4. Review log

| Date | Event |
|------|-------|
| 2026-06-01 | Initial register — Phase 4 |

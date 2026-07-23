# ISEO-SU-SITE-OPS Cross-Chat Handoff Closeout v1

**Status:** ACCEPTED (Phase 1.5 documentary closeout of Phase 1 intake)  
**Decision date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

**Caveat:** Chat handoff is **supporting evidence**, not repository authority. On conflict after reconciliation, this locus + governance win.

---

## Handoffs received (summary)

| Stream | Scope summarized | Repository anchors cited |
|--------|------------------|--------------------------|
| **WPilot Development** | RC5 reference implementation; DEV proof; maintenance HOLD; production not authorized | `projects/wpilot/OPERATIONAL-INDEX.md`; `projects/wpilot/WPILOT-FINAL-STATE-RC5.md`; `projects/wpilot/WPILOT-AUTHORITY-STATE-RC5.md`; `projects/wpilot/WPILOT-LIFECYCLE-STATE.md`; `projects/wpilot/WPILOT-MAINTENANCE-POLICY-v1.md`; `projects/wpilot/WPILOT-PROVEN-CAPABILITIES-v1.md`; `projects/wpilot/local-storage-policy.md` |
| **WPilot Plugin MVP** | Plugin REST safety loop; clean-install checklist posture; Sprint 3 HOLD | `projects/wpilot/WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md`; plugin under `projects/wpilot/plugin/` (not modified); proven capabilities register above |
| **dev.gktriumph.ru** | Handled **inside WPilot Development** as DEV environment — not an i-seo.su production fact | WPilot OPERATIONAL-INDEX / FINAL-STATE (DEV URL `https://dev.gktriumph.ru`) |
| **WP Forge proger** | Methodology + FP-0002 experience patterns; admin/ACF/git lessons — not project ownership | `projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md`; `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/DOCS/FORGE-PROGER-EXPERIENCE-PACK/v9-06-batch-01/INDEX.md`; `PATTERNS-LEARNED.md`; `ANTI-PATTERNS-AND-FAILURES.md`; `ACF-SOT-GUIDELINES.md`; `GIT-PERSISTENCE-LESSONS.md` |
| **ATLAS** | Identity registry documentation; no mint for this programme now | `projects/atlas/OPERATIONAL-INDEX.md` |

Supporting siblings also reviewed for boundaries:

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/mars-survivability/OPERATIONAL-INDEX.md`
- `projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md`
- `projects/remote-operations-layer/OPERATIONAL-INDEX.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`

---

## Accepted findings

1. i-seo.su needs a **dedicated hybrid site-ops locus** separate from WPilot and Report Hub.
2. WPilot is valuable as **WordPress-only** tooling/methodology; RC5 is DEV-proven, not production authorization.
3. Forge/Website Factory contribute **safety and process patterns**, not site ownership.
4. ATLAS mint must wait for an explicit later charter.
5. Survivability + ROL supply backup/remote discipline patterns for later connection phases.
6. Report Hub is a **sibling product** that may touch i-seo.su ecosystem without owning site ops.
7. Hybrid static + WordPress is **operator context** until evidence intake confirms boundaries.

---

## Conflicts observed

| Topic | Conflict | Notes |
|-------|----------|-------|
| Project locus | Risk of passport under `projects/wpilot/sites/` vs dedicated programme | Reconciled → site-ops locus |
| Token format | Conflicting handoff recommendations | Remains SAFE UNKNOWN |
| Backup path | Repo-local vs Storage-heavy paths | Prefer Storage for heavy prod evidence subject to policy check |
| Backup/rollback endpoints | Capability-level DEV lifecycle vs exact production route proof | Production proof SAFE UNKNOWN |
| Compatibility | DEV environment proof vs production minimum versions | DEV ≠ contract |

---

## Reconciled decisions

### A. Project locus

**Main SoT = `projects/iseo-su-site-ops/`**  
Do **not** create a second full site passport under `projects/wpilot/sites/` for this production programme.

### B. Token format

Conflicting handoff recommendations.  
**Final format remains SAFE UNKNOWN** pending canonical source review in later planning.  
**Preferred principle (non-binding):** separate token file + metadata references path only (consistent with `projects/wpilot/local-storage-policy.md` patterns).

### C. Backup path

Heavy production evidence/backups should default to `X:\AI MARS STORAGE\`, subject to current policy verification.  
**Do not create paths now.**

### D. Backup/rollback endpoints

Capability-level DEV lifecycle exists (inspect → backup → apply → validate → rollback) per WPilot FINAL-STATE / proven capabilities.  
Exact RC5 route inventory applicability and **production proof** remain **SAFE UNKNOWN**.

### E. Compatibility

DEV environment proof is **not** a minimum-version contract for i-seo.su.

---

## Unresolved conflicts / open items

- Token/profile canonical format for i-seo.su
- Exact production backup/rollback implementation
- WPilot production compatibility
- ATLAS entity IDs (deferred)
- Local mirror necessity
- Browser Workstation concrete security profile

All tracked in [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md).

---

## Source-path discipline

Only paths verified present in the repository at Phase 1.5 time are cited above.  
Missing named files (if any in earlier prompts) would be marked SAFE UNKNOWN — in this pass, required WPilot/Forge/sibling indexes and the listed experience-pack files were found.

---

*Cross-Chat Handoff Closeout v1 · 2026-07-22.*

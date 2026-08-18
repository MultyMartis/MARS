# ISEO-SU-SITE-OPS — Firefox Browser Workstation (Deferred) v1

**Status:** APPROVED DIRECTION / IMPLEMENTATION DEFERRED  
**Decision date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Related decision:** Decision Register D-015 / D-016

---

## Operator rule

**Firefox Developer Edition** becomes a separate **MARS Browser Workstation** — a dedicated operator browser surface for controlled investigation and QA, distinct from personal browsing.

This record persists the direction only. It does **not** implement infrastructure.

---

## Classification

| Field | Value |
|-------|-------|
| Direction | APPROVED |
| Implementation | DEFERRED |
| Authorization for production access | **NONE** (Browser Workstation ≠ access charter) |
| Ownership of infra programmes | Unchanged — this task does **not** modify MLI, Survivability, or other infra packs |

---

## Future possible support (not authorized now)

When separately chartered, the Workstation **may** later support:

- Browser QA
- DevTools inspection
- Screenshots
- Authenticated operator sessions (under HITL)
- Frontend regression checks
- Read-only investigation

---

## Explicitly not defined / not authorized by this task

- Installation of Firefox Developer Edition
- Profile creation
- Login to i-seo.su or any production surface
- Cookie handling procedures
- Password storage
- Proxy configuration
- VPN posture
- Production access
- Downloads policy execution
- Extensions install
- Automation / RPA
- Remote debugging enablement

---

## Future required decisions (checklist)

| Decision | Notes |
|----------|-------|
| Executable path | Where Firefox Developer Edition is installed |
| Profile path | Isolated profile root |
| Profile name | Stable operator label |
| Separation from personal browser | Mandatory isolation |
| Cookie / session policy | Retention, wipe, production rules |
| Credential manager policy | Prefer no stored production passwords unless chartered |
| Proxy / VPN posture | Allowed / denied / conditional |
| Extension allowlist | Default deny |
| Downloads path | Controlled folder |
| Screenshot / evidence path | Prefer Storage when heavy; policy TBD |
| DevTools / remote-debug policy | Default deny remote debug |
| Production HITL | Required before authenticated prod sessions |
| Cleanup / rotation | Session and profile hygiene |
| Backup / recovery | Profile recoverability |
| Ownership | Which MARS programme owns Workstation infra docs |
| Integration with i-seo.su browser QA | Link to future `BROWSER-QA-PLAN-v1` |

---

## Boundary reminder

Browser Workstation is **not**:

- authorization for external access;
- a substitute for FTP/WPilot charters;
- a credential vault;
- proof that QA has been executed.

See also [ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md](ISEO-SU-SITE-OPS-SYSTEM-BOUNDARIES-v1.md).

---

*Firefox Browser Workstation deferred record v1 · 2026-07-22.*

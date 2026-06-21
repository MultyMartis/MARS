# WPilot — Operational Index

**Lane:** B — External Systems (WordPress).  
**Status:** **ACTIVE** — documented navigation only; **not** automated router or service registry.  
**Domain root:** [README.md](README.md)

---

## Authority State (RC5)

| Field | Value |
|-------|-------|
| **Status** | **ACTIVE** |
| **Lifecycle state** | **Reference Implementation** |
| **Authority State** | `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19` |
| **Commit** | `648632acbdd42703427fd76a0cb1fd8d88641dcc` |
| **Release candidate** | `v0.3.0-RC5` |
| **Plugin version** | `0.3.0` (schema `0.2.0`) |
| **Runtime maturity** | `proven_content_writes` + `proven_connection_runtime` |
| **Environment** | DEV only — `https://dev.gktriumph.ru` |
| **Token storage** | `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| **Notes** | No token value in repo. Sprint 3 **HOLD**. Next phase: explicit HITL charter only. |

---

## Current phase

| Field | Value |
|-------|-------|
| **Lifecycle state** | **Reference Implementation** |
| **Phase** | RC5 Finalized — maintenance reference |
| **Final state** | [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) |
| **Maintenance policy** | [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) |
| **Sprint 3** | **HOLD** |
| **Next allowed phase** | Explicit HITL charter only |

---

## Canonical reading order

| # | Topic | Document |
|---|--------|----------|
| 1 | **Final state (RC5)** | [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) |
| 2 | **Authority state (RC5)** | [WPILOT-AUTHORITY-STATE-RC5.md](WPILOT-AUTHORITY-STATE-RC5.md) |
| 3 | **Lifecycle state** | [WPILOT-LIFECYCLE-STATE.md](WPILOT-LIFECYCLE-STATE.md) |
| 4 | **Maintenance policy** | [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) |
| 5 | **Program overview** | [README.md](README.md) |
| 6 | **RC5 release candidate** | [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md) |
| 7 | **State freeze (RC5)** | [reports/wpilot-state-freeze-2026-06-19.md](reports/wpilot-state-freeze-2026-06-19.md) |
| 8 | **Core freeze** | [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md) |
| 9 | **Proven capabilities** | [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md) |
| 10 | **Plugin MVP roadmap** | [metacode-wpilot-plugin-mvp-roadmap.md](metacode-wpilot-plugin-mvp-roadmap.md) |
| 11 | **Local token policy** | [local-storage-policy.md](local-storage-policy.md) |
| 12 | **Ecosystem sync (RC5)** | [ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md](ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md) |

---

## Completed milestones (RC5 cycle)

| ID | Title | Status |
|----|-------|--------|
| WPILOT-MILESTONE-001 | First Proven Runtime Write Path | **PROVEN** |
| UX-01 | Admin UI alignment | **Complete** |
| OPS-01 | Release readiness audit | **Complete** |
| OPS-02 | RC baseline decision (Variant B) | **Complete** |
| UX-02 | Operator dashboard + connection tracking | **Complete** |
| BUGFIX-01 | Connection tracker independence | **Complete** |
| BUGFIX-02 | Connection metadata persistence | **Complete** |
| RC5 | Connection proof on live DEV | **Complete** |
| WPILOT-MILESTONE-002 | RC5 Finalization | **COMPLETE** |

**Partial:** TEST-01 clean ZIP install — not a blocker for RC5 live proof.

---

## Ecosystem cross-references

| System | Relationship |
|--------|--------------|
| **OCPilot** | Sibling — CMS/Ecommerce Pilots family; pattern reuse only |
| **Website Factory** | Planned upstream for Mode A payloads |
| **ATLAS** | Consumer — `WEB-*` context; no CMS runtime in ATLAS |
| **MARS registry** | `wpilot` — [registry/project-registry.md](../../registry/project-registry.md) |

---

## Explicit exclusions (normative)

| Excluded | Reason |
|----------|--------|
| Sprint 3 | **HOLD** until explicit HITL charter |
| New REST endpoints | RC5 freeze |
| Plugin/runtime changes | RC5 freeze |
| Production deploy | DEV only |
| Token values in repo | Security baseline |

---

*WPilot Operational Index · Reference Implementation · RC5 finalization (2026-06-19).*

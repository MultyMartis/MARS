# WPilot Ecosystem Sync — RC5 (2026-06-19)

**Classification:** Cross-system visibility notes — documentation only.  
**Date:** 2026-06-19  
**Authority State:** `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19`  
**Commit:** `648632acbdd42703427fd76a0cb1fd8d88641dcc`  
**Trigger:** RC5 live on DEV — authenticated REST, connection tracking, MARS ↔ WPilot token handoff proven.

**Scope:** Notes for sibling systems. **Does not modify** OCPilot, Website Factory, ATLAS, plugin code, or runtime.

---

## What changed

| Area | RC5 delta |
|------|-----------|
| **Runtime maturity** | Added `proven_connection_runtime` alongside existing `proven_content_writes` |
| **Connection proof** | Last Successful Connection and Last Endpoint populate in admin after authenticated REST |
| **BUGFIX-02** | Partial `update_options()` for `last_token_used_at` — connection metadata no longer erased |
| **MARS token standard** | DEV token path fixed: `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| **UX-02** | Operator dashboard deployed (tabs, compact Overview, Connection panel) |
| **Phase posture** | **Reference Implementation — RC5 Finalized** — Sprint 3 **HOLD** |

Prior proven path unchanged: `inspect` → `backup` → `scoped-replace` → `validate` → `rollback` on DEV.

---

## Why it matters

1. **MARS can trust the bridge** — local token file → authenticated REST → observable connection state in WordPress admin.
2. **Connection tracking is independent evidence** — not inferred from content-write success alone.
3. **Freeze boundary is explicit** — RC5 closes the connection-runtime proof loop; expansion requires HITL charter, not default sprint continuation.
4. **Ecosystem indexes can align** — OPERATIONAL-INDEX, registry, and reality index can cite one authority state without claiming production or Sprint 3 readiness.

---

## Reusable pattern for OCPilot

WPilot RC5 proved a **CMS Pilot runtime discipline** that OCPilot should reuse **conceptually**, not as WordPress-specific code:

| Pattern element | WPilot proof | OCPilot application |
|-----------------|--------------|---------------------|
| **Write safety loop** | `inspect → backup → apply → validate → rollback` | Same human-supervised sequence before any OpenCart mutation |
| **Typed REST operations** | Scoped replace on one proven primitive | Narrowest OpenCart write primitive; refuse ambiguity |
| **Backup before mutation** | Plugin-owned snapshot required | Mandatory rollback source before apply |
| **Rollback proof before expansion** | Rollback proven before scoped-replace scope growth | Do not widen write surface until recovery path re-proven |
| **Connection tracking** | Success/failure metadata + admin visibility | Operator-visible last-success signal for bridge health |
| **Local token file standard** | `C:\AI MARS\local\tokens\` — never in git | Same local-only credential boundary |

**OCPilot must not:** copy WordPress REST routes, WPBakery logic, or WPilot plugin code.

---

## Reusable pattern for CMS Pilot family

Shared family pattern (WPilot + OCPilot + future pilots):

```
inspect → backup → apply → validate → rollback
```

Connection pattern:

```
local token file → authenticated REST → connection tracker → admin visibility
```

Reference: [cms-ecommerce-pilots-family.md](../../ocpilot/cms-ecommerce-pilots-family.md), [shared/external-access-patterns/](../../../shared/external-access-patterns/README.md).

---

## What is not yet proven

| Item | Status |
|------|--------|
| Sprint 3 features | **HOLD** — not started |
| RC5 clean ZIP install on disposable WordPress | **UNKNOWN** — TEST-01 PARTIAL |
| Production runtime | Not proven — DEV only |
| Menu / widget / CSS plugin endpoints | Not implemented |
| Factory Mode A pipeline integration | Planned — not proven |
| Multisite | Not proven |
| Autonomous execution | Not proven — human-supervised only |

---

## What must not be copied blindly

| Anti-pattern | Reason |
|--------------|--------|
| WordPress-specific REST namespace (`wpilot/v1`) | Platform-specific; OCPilot needs OpenCart contract |
| WPBakery scoped-replace semantics | Builder-specific; not transferable to OpenCart themes |
| Assuming connection proof = content-write proof | RC5 separates bridge health from mutation capability |
| Skipping rollback proof before new write primitives | WPilot sequence that worked: rollback before apply expansion |
| Token values in repo, reports, or chat intended for git | MARS security baseline |
| Treating RC5 freeze as Sprint 3 authorization | Explicit HITL charter required |
| Production deploy from RC5 DEV evidence | Environment scope is DEV only |

---

## Related documents

| Document | Role |
|----------|------|
| [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](../WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md) | RC5 specification |
| [reports/wpilot-state-freeze-2026-06-19.md](../reports/wpilot-state-freeze-2026-06-19.md) | Release freeze audit |
| [WPILOT-PROVEN-CAPABILITIES-v1.md](../WPILOT-PROVEN-CAPABILITIES-v1.md) | Evidence register |
| [WPILOT-ECOSYSTEM-SYNC-2026-06-v1.md](WPILOT-ECOSYSTEM-SYNC-2026-06-v1.md) | Prior sync (content writes focus) |
| [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) | WPilot navigation index |

---

## Document status

| Field | Value |
|-------|-------|
| Version | RC5 sync pass |
| Date | 2026-06-19 |
| Modifies external systems | No |
| Implements runtime | No |

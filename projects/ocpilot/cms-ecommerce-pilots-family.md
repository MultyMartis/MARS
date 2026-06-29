# CMS / Ecommerce Pilots — Family Classification

**Classification:** architectural family idea inside MARS External Systems lane.  
**Status:** documentation only — **not** a runtime, **not** an autonomous agent fleet.

## What this family is

**CMS / Ecommerce Pilots** is a naming and pattern-sharing grouping for standalone human-supervised bridge programs. Each pilot targets a specific CMS or site platform. Pilots are **siblings**, not parent/child hierarchies.

## Current and possible members

| Pilot | Platform | Lifecycle | Status in MARS |
|-------|----------|-----------|----------------|
| **WPilot** | WordPress | **Reference Implementation** | **ACTIVE** — `v0.3.0-RC5` proven on DEV; RC5 development focus **closed**; authority [WPILOT-AUTHORITY-STATE-RC5.md](../wpilot/WPILOT-AUTHORITY-STATE-RC5.md); see [OPERATIONAL-INDEX.md](../wpilot/OPERATIONAL-INDEX.md) |
| **OCPilot** | OpenCart / ocStore | **Architecture / Development** | **ACTIVE** — operational documentation + site work; no in-repo plugin REST runtime proof; see [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) |
| **MODxPilot** | MODx | — | possible future bridge — not chartered in-repo |
| **CustomSitePilot** | Custom / static / PHP / HTML sites (operator-built) | — | possible lightweight manager — not chartered in-repo |

**Lifecycle** describes each pilot's evidence-backed maturity and ecosystem role inside MARS — not marketing labels. **Reference Implementation** means proven runtime frozen as a validation baseline and pattern source (WPilot RC5); **Architecture / Development** means policy, workflows, and site ops exist without equivalent formal runtime proof.

**WPilot reference role:** WPilot serves as the **validation baseline and runtime reference** for future CMS Pilots — pattern reuse (safety loop, connection tracking, token standard) is encouraged; **feature parity with WPilot is not required** for sibling pilots.

### Capability comparison (facts only)

| Capability | WPilot | OCPilot |
|------------|--------|---------|
| **Lifecycle** | Reference Implementation | Architecture / Development |
| **Platform** | WordPress | OpenCart / ocStore |
| **In-repo bridge code** | Yes — `metacode-wpilot` plugin source | No — documentation and site ops only |
| **Formal plugin REST runtime** | Proven on DEV (`wpilot/v1`) | Not in-repo |
| **Canonical safety loop** (`inspect → backup → apply → validate → rollback`) | Proven via plugin REST on DEV | Documented discipline; site writes via FTP/PMA/browser — not same formal loop |
| **Connection tracking** (token → REST → metadata → operator visibility) | Proven on DEV (RC5) | Not proven as formal connection runtime |
| **Local token standard** | Proven — `X:\AI MARS\local\tokens\` | Documented access patterns; site credentials external |
| **Human-supervised site writes** | Proven (DEV + helper paths + plugin REST) | Proven (site-level ops e.g. SITE-001 W1A — OpenCart-specific) |
| **Evidence register** | [WPILOT-PROVEN-CAPABILITIES-v1.md](../wpilot/WPILOT-PROVEN-CAPABILITIES-v1.md) | Site reports under `sites/` — no family-equivalent proven-capabilities register |
| **Authority state document** | [WPILOT-AUTHORITY-STATE-RC5.md](../wpilot/WPILOT-AUTHORITY-STATE-RC5.md) | None — Phase 0+ operational index |
| **Production deploy** | EXCLUDED (DEV only) | External hosting — not MARS-owned |
| **Autonomous CMS admin** | EXCLUDED | EXCLUDED |
| **Sibling relationship** | Standalone member | Standalone member — not child of WPilot |

**JoomlaPilot is not planned.**

## Explicit boundaries

| Statement | Meaning |
|-----------|---------|
| Family classification only | Shared vocabulary and patterns — not a merged product |
| No autonomous agent fleet | No claim of orchestrated multi-pilot runtime in-repo |
| Each pilot standalone | OCPilot is not a child of WPilot; WPilot is not a parent of OCPilot |
| Human-supervised | HITL, REPORT, SAFE UNKNOWN apply per pilot |
| Pattern reuse allowed | Access safety, site passport, backup/rollback, dry-run, read-only audit, battle pilot freeze |

## Shared pattern layer

Pilots may reference common documentation under:

- [shared/external-access-patterns/](../../shared/external-access-patterns/) — browser, FTP, database access patterns and safety boundaries

Pilot-specific workflows remain under each pilot's `projects/<pilot>/` tree.

### WPilot RC5 — reference implementation baseline (2026-06-19)

WPilot RC5 on DEV is the **Reference Implementation** for the CMS Pilots family — a proven runtime pattern that sibling pilots (including OCPilot) may reuse **conceptually**, not as WordPress-specific code. **No feature parity requirement** applies to siblings:

- typed REST operations
- backup before mutation
- rollback proof before expansion
- connection tracking (local token → authenticated REST → admin visibility)
- local token file standard (`X:\AI MARS\local\tokens\` — no value in repo)

Write safety loop: `inspect → backup → apply → validate → rollback`.

Canonical pattern doc: [CMS-PILOT-RUNTIME-PATTERN-v1](../shared/runtime-patterns/CMS-PILOT-RUNTIME-PATTERN-v1.md).  
Authority state: [WPILOT-AUTHORITY-STATE-RC5.md](../wpilot/WPILOT-AUTHORITY-STATE-RC5.md).  
Canonical sync note: [WPilot ecosystem sync RC5](../wpilot/ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md).

## OCPilot position

OCPilot is a **member** of this family and a **standalone** OpenCart/ocStore bridge. It reuses family patterns where applicable; it does not inherit WordPress logic from WPilot.

## SAFE UNKNOWN

- Whether MODxPilot or CustomSitePilot will be chartered — unknown until separate human charter.
- Whether a unified pilot index across all members will exist — unknown; each pilot keeps its own OPERATIONAL-INDEX until decided otherwise.

## Related docs

- [OCPilot README](README.md)
- [OCPilot architecture](architecture.md)
- [OCPilot access and safety](access-and-safety.md)

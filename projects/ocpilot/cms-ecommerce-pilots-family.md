# CMS / Ecommerce Pilots — Family Classification

**Classification:** architectural family idea inside MARS External Systems lane.  
**Status:** documentation only — **not** a runtime, **not** an autonomous agent fleet.

## What this family is

**CMS / Ecommerce Pilots** is a naming and pattern-sharing grouping for standalone human-supervised bridge programs. Each pilot targets a specific CMS or site platform. Pilots are **siblings**, not parent/child hierarchies.

## Current and possible members

| Pilot | Platform | Status in MARS |
|-------|----------|----------------|
| **WPilot** | WordPress | existing program under `projects/wpilot/` |
| **OCPilot** | OpenCart / ocStore | existing program under `projects/ocpilot/` |
| **MODxPilot** | MODx | possible future bridge — not chartered in-repo |
| **CustomSitePilot** | Custom / static / PHP / HTML sites (operator-built) | possible lightweight manager — not chartered in-repo |

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

## OCPilot position

OCPilot is a **member** of this family and a **standalone** OpenCart/ocStore bridge. It reuses family patterns where applicable; it does not inherit WordPress logic from WPilot.

## SAFE UNKNOWN

- Whether MODxPilot or CustomSitePilot will be chartered — unknown until separate human charter.
- Whether a unified pilot index across all members will exist — unknown; each pilot keeps its own OPERATIONAL-INDEX until decided otherwise.

## Related docs

- [OCPilot README](README.md)
- [OCPilot architecture](architecture.md)
- [OCPilot access and safety](access-and-safety.md)

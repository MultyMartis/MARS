# CMS Pilot Runtime Pattern v1

**Classification:** Shared runtime pattern — CMS / Ecommerce Pilots family.  
**Status:** Documented v1 (2026-06-19).  
**Proven by:** WPilot RC5 — [WPILOT-AUTHORITY-STATE-RC5.md](../../wpilot/WPILOT-AUTHORITY-STATE-RC5.md)  
**Scope:** Documentation only. **Not** a runtime product, **not** orchestration, **not** WordPress-universal implementation spec.

---

## Purpose

This document captures the **canonical CMS Pilot runtime pattern** proven by WPilot RC5 as a **family-level reference** for sibling pilots (OCPilot, possible future pilots). It describes **what was proven conceptually** and **what remains platform-specific**.

**Family home:** [projects/ocpilot/cms-ecommerce-pilots-family.md](../../ocpilot/cms-ecommerce-pilots-family.md)  
**Access patterns (shared):** [shared/external-access-patterns/](../../../shared/external-access-patterns/README.md)

---

## Canonical runtime pattern

Human-supervised mutation safety loop:

```
inspect → backup → apply → validate → rollback
```

| Phase | Intent | Operator gate |
|-------|--------|---------------|
| **inspect** | Read current state; establish baseline before mutation | Required before apply |
| **backup** | Capture recoverable pre-apply snapshot | Required before apply |
| **apply** | Execute scoped, typed change | HITL authorization |
| **validate** | Confirm post-apply integrity (checksum, scope checks) | Required before closeout |
| **rollback** | Restore from backup; re-validate | Required proof before expansion |

**Proven by WPilot:** Full loop on DEV via plugin REST for `page.post_content` scoped-replace; rollback 3/3 PASS (Runtime Proof Sprint + Sprint 2).

**Not claimed universally:** Specific REST routes, DB schema, or CMS APIs — those are **implementation-specific**.

---

## Connection pattern

Operator ↔ bridge ↔ CMS visibility chain:

```
local token
  → authenticated REST
    → connection tracking
      → operator visibility
```

| Element | Intent |
|---------|--------|
| **local token** | Secret stored outside repo on operator machine; never committed |
| **authenticated REST** | Typed bridge API; token validates before read/write paths |
| **connection tracking** | Sanitized metadata only (timestamps, status, endpoint label) — no secrets in logs |
| **operator visibility** | Admin or report surface shows last successful connection and last endpoint |

**Proven by WPilot:** MARS token file → `X-WPilot-Token` → connection tracker options → WPilot admin Connection tab on DEV.

**Family token convention (WPilot-established):** storage root `C:\AI MARS\local\tokens\` — no token value in repo.

---

## What is proven by WPilot (family-reusable concepts)

| Concept | WPilot RC5 evidence | Reusable by siblings? |
|---------|---------------------|------------------------|
| Safety loop order | inspect → backup → apply → validate → rollback | **Yes — conceptual** |
| Backup before mutation | Plugin REST backup + checksum | **Yes — conceptual** |
| Rollback proof before expansion | 3/3 PASS rollback on DEV | **Yes — conceptual** |
| Scoped write primitive | Narrow target + exact-once replace | **Yes — conceptual** (target types differ per CMS) |
| Audit trail per operation | `operation_id` lifecycle events | **Yes — conceptual** |
| Checksum pipeline | `sha256:` on inspect/backup/apply/rollback | **Yes — conceptual** |
| Local token → REST auth | MARS token file + auth header | **Yes — conceptual** (header name CMS-specific) |
| Connection metadata persistence | Success/failure timestamps, endpoint label | **Yes — conceptual** |
| Operator admin visibility | Connection tab with last success/endpoint | **Yes — conceptual** |
| DEV-only human-supervised scope | All proof on test site | **Yes — discipline** |
| Evidence register discipline | Proven Capabilities doc — facts only | **Yes — documentation pattern** |

**Authority reference:** [WPILOT-AUTHORITY-STATE-RC5.md](../../wpilot/WPILOT-AUTHORITY-STATE-RC5.md)  
**Evidence register:** [WPILOT-PROVEN-CAPABILITIES-v1.md](../../wpilot/WPILOT-PROVEN-CAPABILITIES-v1.md)

---

## What remains implementation-specific

Each CMS Pilot **must** define its own:

| Concern | Examples (vary by platform) |
|---------|----------------------------|
| **Bridge technology** | WordPress plugin REST vs OpenCart file/DB scripts vs MODx connectors |
| **Auth mechanism** | Header name, token storage key, capability model |
| **Target registry** | page/post_content vs twig/controller vs chunk/template |
| **Write primitives** | scoped-replace vs file patch vs SQL with rollback bundle |
| **Backup storage** | Plugin DB table vs file snapshots vs DB dumps (external) |
| **Validation signals** | Checksum fields, theme integrity, shortcode counts |
| **Admin UI** | WP admin page vs OCPilot reports-only vs future panel |
| **Deploy path** | FTP plugin upload vs SFTP theme deploy vs EAR snapshots |

**OCPilot today:** Architecture and operational documentation; site-level human-supervised writes via FTP/PMA/browser patterns — **not** the same formal plugin REST loop as WPilot. See family comparison in [cms-ecommerce-pilots-family.md](../../ocpilot/cms-ecommerce-pilots-family.md).

---

## Anti-patterns (do not copy blindly)

| Anti-pattern | Why |
|--------------|-----|
| Copy WordPress REST routes into OpenCart | Platform mismatch — pattern only |
| Treat WPilot plugin source as OCPilot dependency | Siblings — pattern reuse, not inheritance |
| Claim family pattern = autonomous runtime | Human-supervised only |
| Skip rollback proof before new write surfaces | RC5 freeze discipline |
| Store tokens or secrets in repo | Security baseline |

---

## Relationship to other layers

| Layer | Role |
|-------|------|
| **CMS Pilot family doc** | Member classification, sibling boundaries |
| **This pattern doc** | Proven runtime + connection concepts |
| **shared/external-access-patterns/** | FTP, PMA, browser access discipline |
| **Pilot OPERATIONAL-INDEX** | Per-pilot navigation and evidence |
| **registry/project-registry.md** | MARS `project_id` lifecycle rows |

---

## Version history

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-06-19 | Initial pattern registration from WPilot RC5 authority state |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Whether OCPilot will implement formal plugin-style REST bridge | **UNKNOWN** — architecture/development today |
| Unified pilot runtime index across all members | **UNKNOWN** |
| MODxPilot / CustomSitePilot charter | **UNKNOWN** |

---

*CMS Pilot Runtime Pattern v1 · family reference · proven by WPilot RC5 · 2026-06-19.*

# Forge WordPress — Handoff Boundaries v1

**Document type:** Boundary model (full contracts deferred to FW-02)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

---

## 1. Boundary overview

```text
[B1] Website Factory ──approved frontend──► Forge WordPress
[B2] Forge WordPress internal: Architecture → Implementation → Validation
[B3] Forge WordPress ──release candidate──► WPilot
```

---

## 2. B1 — Website Factory → Forge WordPress

### Must be approved before Forge WordPress intake (FWP-01)

| Requirement | Evidence |
|-------------|----------|
| Factory project declared in LOC-ZONE | Passport |
| `production_mode` declared | `PIXEL_PERFECT` \| `TEMPLATE_ART` |
| Frontend validation chain complete to **VL6** (or documented waiver) | Factory QA reports |
| Reproducible frontend build | `npm run build` instructions + dist |
| Handoff manifest | `FRONTEND-HANDOFF` artifact |
| Block/page inventory | Mapping input |
| Operator acknowledgment | G1 gate |

### Factory retains ownership (non-transfer)

| Remains Factory | Reason |
|-----------------|--------|
| Design source and design QA | Upstream layer |
| Frontend code changes post-handoff | Requires change-control back to Factory |
| Gulp/Forge overlay discipline | Not WordPress lane |
| VL0–VL6 validation semantics | Orthogonal to WV |

### FW-02 contract

**Website Factory → Forge WordPress Handoff Contract** — formalizes B1.

---

## 3. B2 — Forge WordPress internal handoffs

### Architecture → Implementation (G5 gate)

| Transfers | Does not transfer |
|-----------|-------------------|
| Approved `IMPLEMENTATION-SPEC` | Tacit knowledge |
| `VALIDATION-PLAN` | Unapproved WAD changes |
| All FWP-03–05 artifacts | Production deploy rights |

### Implementation → Validation

| Transfers | Does not transfer |
|-----------|-------------------|
| Implementation branch / tag | Merge authority |
| Build instructions | Operator sign-off |
| Plugin register realized state | WPilot operations |

### Validation → Packaging

| Transfers | Does not transfer |
|-----------|-------------------|
| WV reports (WV0–WV9) | Release to production |
| `VISUAL-QA-REPORT` | Autonomous deploy |

**Rule:** Each internal handoff requires **artifact completeness** — no verbal handoff.

---

## 4. B3 — Forge WordPress → WPilot

### Must be complete before WPilot operations (FWP-11)

| Package element | Purpose |
|-----------------|---------|
| `RELEASE-MANIFEST` | Version, components, dependencies |
| Theme + functionality plugin packages (or repo ref) | Deployable code |
| `WPILOT-HANDOFF` document | Operational instructions |
| `EDITABLE-REGIONS-MAP` | Frozen vs editable zones |
| `PLUGIN-REGISTER` | Approved third-party set |
| WV9 report | Packaging validation |
| Validation evidence bundle | WV2–WV8 as applicable |
| **No production credentials** | Security |

### WPilot owns after handoff

| WPilot domain | Forge WordPress does not |
|---------------|--------------------------|
| Controlled content writes (proven RC5) | Re-implement theme |
| DEV/staging deploy (chartered) | Direct production coding |
| Backup-first operations | Live DB surgery |
| Connection/runtime plugin ops | ACF architecture changes without change request |

### Alignment note

WPilot docs describe **Factory-native WordPress** as preferred long-term target — B3 package format is **SAFE UNKNOWN** detail until FW-02 handoff contract and WPilot charter update.

### FW-02 contract

**Forge WordPress → WPilot Handoff Contract** — formalizes B3.

---

## 5. Anti-patterns

| Violation | Consequence |
|-----------|-------------|
| Forge WordPress starts without B1 | **STOP** at WV0 |
| WPilot asked to build theme | Reject — wrong boundary |
| Factory modifies WP theme in LOC-ZONE without charter | Boundary violation |
| Handoff without editable-regions map | **BLOCK** G10 |

---

## 6. FW-02 contract inventory (from B1/B3)

| Contract | Boundary |
|----------|----------|
| Website Factory → Forge WordPress Handoff Contract | B1 |
| WordPress Project Intake Contract | B1 detail |
| Forge WordPress → WPilot Handoff Contract | B3 |

See [reports/FORGE-WORDPRESS-FW-02-CONTRACTS-AND-STANDARDS-INPUT-v1.md](reports/FORGE-WORDPRESS-FW-02-CONTRACTS-AND-STANDARDS-INPUT-v1.md).

---

## Related documents

- [FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md](FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md)
- [projects/wpilot/OPERATIONAL-INDEX.md](../../../wpilot/OPERATIONAL-INDEX.md)

---

*Handoff boundaries v1 — model only; contracts in FW-02.*
